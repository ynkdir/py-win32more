# https://github.com/microsoft/win32metadata
# https://github.com/marlersoft/win32json

import json
import re
from pathlib import Path

ARCHITECTURE = "X64"

py_builtins = ("False", "True", "None")

knowntype = {"PSTR":"c_char_p", "PWSTR":"c_wchar_p", "BSTR":"c_wchar_p"}

class MetadataTranspiler:
    def __init__(self, pyfile: Path) -> None:
        self.pyfile = pyfile
        self.out = pyfile.open("w")

    def __del__(self):
        self.out.close()

    def transpile(self, meta) -> None:
        self.namespace = {}
        for e in meta["Resolved"]:
            self.namespace[f"{e['_Api']}.{e['Name']}"] = e
        self.unicode_aliases = {f"{ua}W": ua for ua in meta["UnicodeAliases"]}
        self.write(Path("head.py").read_text())
        for e in meta["Resolved"]:
            self.visit_head(e)
        for e in meta["Resolved"]:
            match e["_Category"]:
                case "Types":
                    self.visit_type(e)
                case "Functions":
                    self.visit_function(e)
                case "Constants":
                    self.visit_constant(e)

    def visit_head(self, e) -> None:
        match e:
            case {"Kind": "Com", "Name": name}:
                interface = e["Interface"]["Name"] if e["Interface"] else "c_void_p"
                self.writeline(f"class {name}({interface}):")
                self.writeline(f"    pass")
            case {"Kind": "Struct", "Name": name}:
                self.writeline(f"class {name}(Structure):")
                self.writeline(f"    pass")
            case {"Kind": "Union", "Name": name}:
                self.writeline(f"class {name}(Union):")
                self.writeline(f"    pass")

    def visit_type(self, mt) -> None:
        match mt["Kind"]:
            case "Com":
                self.visit_com(mt)
            case "ComClassID":
                self.visit_com_class_id(mt)
            case "Enum":
                self.visit_enum(mt)
            case "FunctionPointer":
                self.visit_function_pointer(mt)
            case "NativeTypedef":
                self.visit_typedef(mt)
            case "Struct":
                self.visit_struct(mt)
            case "Union":
                self.visit_struct(mt)
            case _:
                raise RuntimeError(f"unknown type {mt['Kind']}")

    def visit_com(self, mt) -> None:
        guid = repr(mt["Guid"])
        vtbl_index = self.count_interface_method(mt["Interface"])
        self.writeline(f"{mt['Name']}.Guid = Guid({guid})")
        for m in mt["Methods"]:
            types = [self.to_pytype(m["ReturnType"])]
            params = []
            for p in m["Params"]:
                types.append(self.to_pytype(p["Type"]))
                inout = 1
                params.append((inout, p["Name"]))
            ts = ",".join(types)
            if params:
                ps = "(" + ",".join(f"({inout}, '{name}')" for inout, name in params) + ",)"
            else:
                ps = "()"
            self.writeline(f"{mt['Name']}.{m['Name']} = COMMETHOD(WINFUNCTYPE({ts}, use_last_error={m['SetLastError']})({vtbl_index}, '{m['Name']}', {ps}))")
            vtbl_index += 1

    def count_interface_method(self, interface):
        if not interface:
            return 0
        cls = self.namespace[f"{interface['Api']}.{interface['Name']}"]
        return len(cls["Methods"]) + self.count_interface_method(cls["Interface"])

    def visit_com_class_id(self, mt) -> None:
        guid = repr(mt["Guid"])
        self.writeline(f"{mt['Name']} = Guid({guid})")

    def visit_enum(self, mt) -> None:
        # FIXME: enum value name?
        intbase = mt["IntegerBase"] if mt["IntegerBase"] else "Int32"   # IntegerBase can be null
        self.writeline(f"{mt['Name']} = {intbase}")
        need_prefix = self.enum_need_prefix(mt)
        for v in mt["Values"]:
            if need_prefix:
                name = f"{mt['Name']}_{v['Name']}"
            else:
                name = self.to_pyname(v["Name"])
            self.writeline(f"{name} = {v['Value']}")

    def enum_need_prefix(self, mt) -> bool:
        for v in mt["Values"]:
            if not ("_" in v["Name"] or v["Name"].isupper()):
                return True
        return False

    def visit_function_pointer(self, mt) -> None:
        types = [self.to_pytype(mt["ReturnType"])]
        for p in mt["Params"]:
            types.append(self.to_pytype(p["Type"]))
        ts = ",".join(types)
        self.writeline(f"""{mt['Name']} = CFUNCTYPE({ts}, use_last_error={mt['SetLastError']})""")

    def visit_typedef(self, mt) -> None:
        if mt["Name"] in knowntype:
            pytype = knowntype[mt["Name"]]
        else:
            pytype = self.to_pytype(mt["Def"])
        self.writeline(f"{mt['Name']} = {pytype}")

    def visit_struct(self, mt) -> None:
        if mt["Name"].endswith("_e__Struct") or mt["Name"].endswith("_e__Union"):
            base = self.get_struct_base(mt)
            self.writeline(f"class {mt['Name']}({base}):")
            self.writeline(f"    pass")
        for nt in mt["NestedTypes"]:
            self.visit_struct(nt)
        anonymous = []
        for f in mt["Fields"]:
            if re.match(r"^Anonymous\d*$", f["Name"]):
                anonymous.append(f["Name"])
        if anonymous:
            self.writeline(f"{mt['Name']}._anonymous_ = [")
            for name in anonymous:
                self.writeline(f"    '{name}',")
            self.writeline("]")
        if mt["Fields"]:
            self.writeline(f"{mt['Name']}._fields_ = [")
            for f in mt["Fields"]:
                pytype = self.to_pytype(f["Type"])
                self.writeline(f"""    ("{f['Name']}", {pytype}),""")
            self.writeline("]")

    def get_struct_base(slef, mt) -> str:
        match mt["Kind"]:
            case "Struct":
                return "Structure"
            case "Union":
                return "Union"
            case _:
                raise RuntimeError(f"unknown struct kind {mt['Kind']}")

    def visit_function(self, ft) -> None:
        dll = ft["DllImport"]
        types = [self.to_pytype(ft["ReturnType"])]
        params = []
        for p in ft["Params"]:
            types.append(self.to_pytype(p["Type"]))
            inout = 1   # p["Attrs"] has "In" (1) or "Out" (2) or both (3)
            params.append((inout, p["Name"]))
        ts = ",".join(types)
        if params:
            ps = "(" + ",".join(f"({inout}, '{name}')" for inout, name in params) + ",)"
        else:
            ps = "()"
        ua = self.unicode_aliases.get(ft["Name"])
        self.writeline("try:")
        self.writeline(f"""    {ft['Name']} = WINFUNCTYPE({ts}, use_last_error={ft['SetLastError']})(("{ft['Name']}", windll["{dll}"]), {ps})""")
        if ua:
            self.writeline(f"    {ua} = {ft['Name']}")
        self.writeline("except (FileNotFoundError, AttributeError):")
        self.writeline("    pass")

    def visit_constant(self, ct) -> None:
        name = self.to_pyname(ct["Name"])
        pyvalue = self.to_pyvalue(ct)
        self.writeline(f"{name} = {pyvalue}")

    def to_pytype(self, mt) -> str:
        match mt["Kind"]:
            case "PointerTo":
                pointee = self.to_pytype(mt["Child"])
                if pointee == "Void":   # WORKAROUND
                    return "c_void_p"
                else:
                    return f"POINTER({pointee})"
            case "LPArray":
                pointee = self.to_pytype(mt["Child"])
                return f"POINTER({pointee})"
            case "Array":
                if mt["Shape"] is None:
                    size = 0
                else:
                    size = mt["Shape"]["Size"]
                element_type = self.to_pytype(mt["Child"])
                return f"{element_type} * {size}"
            case "ApiRef":
                return mt["Name"]
            case "Native":
                return mt["Name"]
            case "MissingClrType":
                # TODO
                return "Void"
            case _:
                raise RuntimeError(f"unknown type kind {mt['Kind']}")

    def to_pyvalue(self, ct) -> str:
        match ct["ValueType"]:
            case "Byte"| "SByte"| "Char"| "Int16"| "UInt16"| "Int32"| "UInt32"| "Int64"| "UInt64":
                return str(ct["Value"])
            case "Single" | "Double":
                return str(ct["Value"])
            case "String":
                return repr(ct["Value"])
            case "PropertyKey":
                # TODO: other type?
                fmtid = repr(ct["Value"]["Fmtid"])
                pid = ct["Value"]["Pid"]
                return f"PROPERTYKEY(Fmtid={fmtid}, Pid={pid})"
            case _:
                raise RuntimeError(f"unknown value type {ct['ValueType']}")

    def to_pyname(self, name) -> str:
        if name in py_builtins:
            return f"{name}_"
        else:
            return name

    def write(self, s: str) -> None:
        self.out.write(s)

    def writeline(self, s: str) -> None:
        self.write(s)
        self.write("\n")

class DependencyResolver:
    def resolve(self, meta):
        ns = set()
        resolved = []
        pending = {}
        for e in self.collect(meta):
            if e["_Ref"] <= ns:
                resolved.append(e)
                ns.add(e["_ApiName"])
                has_resolved = True
                while has_resolved:
                    has_resolved = False
                    remove = []
                    for name in pending:
                        if pending[name]["_Ref"] <= ns:
                            resolved.append(pending[name])
                            ns.add(pending[name]["_ApiName"])
                            remove.append(name)
                            has_resolved = True
                    for name in remove:
                        del pending[name]
            else:
                pending[e["Name"]] = e
        if pending:
            for e in sorted(pending.values(), key=lambda e: f"{e['_ApiName']}"):
                ref = [ref for ref in e['_Ref'] if ref not in ns]
                print(f"{e['_ApiName']} -> {ref}\n")
            raise RuntimeError("pending")
        meta["Resolved"] = resolved
        return meta

    def collect(self, meta):
        namespace = {}
        for e in meta["Constants"]:
            e["_Category"] = "Constants"
            namespace[e["_ApiName"]] = e
        for e in meta["Types"]:
            if e["Architectures"] and ARCHITECTURE not in e["Architectures"]:
                continue
            e["_Category"] = "Types"
            if e["Kind"] in ("Struct", "Union"):
                self.patch_nested_type(e)
            namespace[e["_ApiName"]] = e
        for e in meta["Functions"]:
            if e["Architectures"] and ARCHITECTURE not in e["Architectures"]:
                continue
            e["_Category"] = "Functions"
            namespace[e["_ApiName"]] = e
        for e in namespace.values():
            e["_Ref"] = self.collect_apiref(e["Name"], e, {}, namespace, set())
        self.patch_name_conflict(namespace)
        return namespace.values()

    def collect_apiref(self, clsname, seq, parent, namespace, ref):
        match seq:
            case {"Kind": "ApiRef", "Name": name, "Api": api, "TargetKind": targetkind}:
                if name == clsname or name.endswith("_e__Struct") or name.endswith("_e__Union"):
                    pass
                elif namespace[f"{api}.{name}"]["Kind"] in ("Struct", "Union") and parent.get("Kind") == "PointerTo":
                    pass
                elif targetkind == "Com" and seq is not parent.get("Interface"):
                    pass
                else:
                    ref.add(f"{api}.{name}")
            case {}:
                for x in seq.values():
                    self.collect_apiref(clsname, x, seq, namespace, ref)
            case [*_]:
                for x in seq:
                    self.collect_apiref(clsname, x, seq, namespace, ref)
        return ref

    def patch_nested_type(self, e):
        names = {}
        for n in e["NestedTypes"]:
            name = f"{e['Name']}_{n['Name']}"
            if not (name.endswith("_e__Struct") or name.endswith("_e__Union")):
                name = f"{name}_e__{n['Kind']}"
            names[n["Name"]] = name
            n["Name"] = name
            self.patch_nested_type(n)
        for f in e["Fields"]:
            t = self.get_element_type(f["Type"])
            if t["Name"] in names:
                t["Name"] = names[t["Name"]]

    def get_element_type(self, e) -> str:
        match e:
            case {"Child": c}:
                return self.get_element_type(c)
            case _:
                return e

    # WORKAROUND
    def patch_name_conflict(self, namespace):
        ns = set()
        for e in namespace.values():
            if e["Name"] in ns:
                print("patch_name_conflict:", e["_ApiName"])
                newname = e["_ApiName"].replace(".", "_")
                self.patch_name(namespace, e["_Api"], e["Name"], newname)
                e["Name"] = newname
            else:
                ns.add(e["Name"])

    def patch_name(self, seq, api, name, newname):
        match seq:
            case {"Kind": "ApiRef"}:
                if seq["Api"] == api and seq["Name"] == name:
                    seq["Name"] = newname
            case {}:
                for x in seq.values():
                    self.patch_name(x, api, name, newname)
            case [*_]:
                for x in seq:
                    self.patch_name(x, api, name, newname)

def loadall():
    def addapi(seq, api):
        for e in seq:
            e["_Api"] = api
            e["_ApiName"] = f"{e['_Api']}.{e['Name']}"
        return seq
    meta = {"Constants": [], "Types": [], "Functions": [], "UnicodeAliases": []}
    for jsonfile in Path("win32json/api").glob("*.json"):
        api = jsonfile.stem
        o = json.loads(jsonfile.read_text())
        meta["Constants"].extend(addapi(o["Constants"], api))
        meta["Types"].extend(addapi(o["Types"], api))
        meta["Functions"].extend(addapi(o["Functions"], api))
        meta["UnicodeAliases"].extend(o["UnicodeAliases"])
    return meta

def main():
    meta = DependencyResolver().resolve(loadall())
    MetadataTranspiler(Path("win32more/all.py")).transpile(meta)

if __name__ == "__main__":
    main()
