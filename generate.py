# https://github.com/microsoft/win32metadata
# https://github.com/marlersoft/win32json

import io
import json
import re
from pathlib import Path

ARCHITECTURE = "X64"

class MetadataTranspiler:
    def transpile(self, ns: dict) -> str:
        self.out = io.StringIO()
        self.write(Path("head.py").read_text())
        for e in ns.values():
            self.visit_head(e)
        for e in ns.values():
            match e["_Category"]:
                case "Types":
                    self.visit_type(e)
                case "Functions":
                    self.visit_function(e)
                case "Constants":
                    self.visit_constant(e)
        return self.out.getvalue()

    def visit_head(self, e) -> None:
        match e:
            case {"Kind": "Com", "Name": name, "Interface": interface}:
                base = interface["Name"] if interface else "c_void_p"
                self.writeline(f"class {name}({base}):")
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
            self.writeline(f"{mt['Name']}.{m['Name']} = COMMETHOD(WINFUNCTYPE({ts}, use_last_error={m['SetLastError']})({m['_vtbl_index']}, '{m['Name']}', {ps}))")

    def visit_com_class_id(self, mt) -> None:
        guid = repr(mt["Guid"])
        self.writeline(f"{mt['Name']} = Guid({guid})")

    def visit_enum(self, mt) -> None:
        self.writeline(f"{mt['Name']} = {mt['IntegerBase']}")
        for v in mt["Values"]:
            self.writeline(f"{v['Name']} = {v['Value']}")

    def visit_function_pointer(self, mt) -> None:
        types = [self.to_pytype(mt["ReturnType"])]
        for p in mt["Params"]:
            types.append(self.to_pytype(p["Type"]))
        ts = ",".join(types)
        self.writeline(f"""{mt['Name']} = CFUNCTYPE({ts}, use_last_error={mt['SetLastError']})""")

    def visit_typedef(self, mt) -> None:
        pytype = self.to_pytype(mt["Def"])
        self.writeline(f"{mt['Name']} = {pytype}")

    def visit_struct(self, mt, nested: bool = False) -> None:
        if nested:
            base = self.get_struct_base(mt)
            self.writeline(f"class {mt['Name']}({base}):")
            self.writeline(f"    pass")
        for nt in mt["NestedTypes"]:
            self.visit_struct(nt, True)
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
        self.writeline("try:")
        self.writeline(f"""    {ft['Name']} = WINFUNCTYPE({ts}, use_last_error={ft['SetLastError']})(("{ft['Name']}", windll["{dll}"]), {ps})""")
        if ua := ft.get("_UnicodeAlias"):
            self.writeline(f"    {ua} = {ft['Name']}")
        self.writeline("except (FileNotFoundError, AttributeError):")
        self.writeline("    pass")

    def visit_constant(self, ct) -> None:
        pyvalue = self.to_pyvalue(ct)
        self.writeline(f"{ct['Name']} = {pyvalue}")

    def to_pytype(self, mt) -> str:
        match mt:
            case {"Kind": "PointerTo", "Child": {"Kind": "MissingClrType"}}:
                return "c_void_p"       # MissingClrType?
            case {"Kind": "PointerTo", "Child": {"Kind": "Native", "Name": "Void"}}:
                return "c_void_p"
            case {"Kind": "PointerTo", "Child": {"Kind": "Native", "Name": "Byte"}}:
                return "c_char_p_no"    # safe?
            case {"Kind": "PointerTo", "Child": {"Kind": "Native", "Name": "Char"}}:
                return "c_wchar_p_no"   # safe?
            case {"Kind": "PointerTo", "Child": c}:
                pointee = self.to_pytype(c)
                return f"POINTER({pointee})"
            case {"Kind": "LPArray", "Child": c}:
                pointee = self.to_pytype(c)
                return f"POINTER({pointee})"
            case {"Kind": "Array", "Shape": shape, "Child": c}:
                size = shape["Size"] if shape else 0
                element_type = self.to_pytype(c)
                return f"{element_type} * {size}"
            case {"Kind": "ApiRef", "Name": name}:
                return name
            case {"Kind": "Native", "Name": name}:
                return name
            case _:
                raise RuntimeError(f"unknown type {mt}")

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

    def write(self, s: str) -> None:
        self.out.write(s)

    def writeline(self, s: str) -> None:
        self.write(s)
        self.write("\n")

class DependencyResolver:
    def resolve(self, ns: dict) -> dict:
        resolved = {}
        waitfor = {}
        defined = set()
        for e in ns.values():
            e["_Ref"] = self.collect_apiref(e, ns, set())
        for e in ns.values():
            if e["_Ref"] <= defined:
                self.define(e, resolved, defined, waitfor)
            else:
                for ref in e["_Ref"]:
                    if ref not in defined:
                        if ref not in waitfor:
                            waitfor[ref] = []
                        waitfor[ref].append(e)
        if waitfor:
            pending = {e["_ApiName"]: p for pp in waitfor.values() for p in pp}
            for e in sorted(pending.values(), key=lambda e: f"{e['_ApiName']}"):
                ref = [ref for ref in e['_Ref'] if ref not in defined]
                print(f"{e['_ApiName']} -> {ref}\n")
            raise RuntimeError("pending")
        return resolved

    def define(self, e, resolved, defined, waitfor):
        resolved[e["_ApiName"]] = e
        defined.add(e["_ApiName"])
        if e["_ApiName"] in waitfor:
            for p in waitfor[e["_ApiName"]]:
                if p["_ApiName"] not in defined and p["_Ref"] <= defined:
                    self.define(p, resolved, defined, waitfor)
            del waitfor[e["_ApiName"]]

    def collect_apiref(self, node: dict, ns: dict, ref: set) -> set:
        match node:
            case {"Kind": "Com", "Interface": interface, "Methods": [*methods]}:
                if interface:
                    ref.add(f"{interface['Api']}.{interface['Name']}")
                for e in methods:
                    self.collect_apiref(e, ns, ref)
            case {"Kind": "PointerTo", "Child": {"Kind": "ApiRef", "Name": name, "Api": api}}:
                if name.endswith("_e__Struct") or name.endswith("_e__Union"):
                    pass
                elif ns[f"{api}.{name}"]["Kind"] in ("Struct", "Union", "Com"):
                    pass
                else:
                    ref.add(f"{api}.{name}")
            case {"Kind": "ApiRef", "Name": name, "Api": api, "TargetKind": targetkind}:
                if name.endswith("_e__Struct") or name.endswith("_e__Union"):
                    pass
                elif targetkind == "Com":
                    pass
                else:
                    ref.add(f"{api}.{name}")
            case {}:
                for e in node.values():
                    self.collect_apiref(e, ns, ref)
            case [*_]:
                for e in node:
                    self.collect_apiref(e, ns, ref)
        return ref

class Preprocessor:
    def preprocess(self, allmeta: dict) -> dict:
        ns = self.make_namespace(allmeta)
        ns = self.patch_name_conflict(ns)
        ns = self.patch_struct_nested_type(ns)
        ns = self.patch_enum(ns)
        ns = self.patch_com_vtbl_index(ns)
        return ns

    def make_namespace(self, allmeta: dict) -> dict:
        ns = {}
        ua = {}
        for api, meta in allmeta.items():
            for a in meta["UnicodeAliases"]:
                ua[f"{a}W"] = a
        for api, meta in allmeta.items():
            for e in meta["Constants"]:
                apiname = f"{api}.{e['Name']}"
                e["_Category"] = "Constants"
                e["_Api"] = api
                e["_ApiName"] = apiname
                ns[apiname] = e
        for api, meta in allmeta.items():
            for e in meta["Types"]:
                if e["Architectures"] and ARCHITECTURE not in e["Architectures"]:
                    continue
                apiname = f"{api}.{e['Name']}"
                e["_Category"] = "Types"
                e["_Api"] = api
                e["_ApiName"] = apiname
                ns[apiname] = e
        for api, meta in allmeta.items():
            for e in meta["Functions"]:
                if e["Architectures"] and ARCHITECTURE not in e["Architectures"]:
                    continue
                apiname = f"{api}.{e['Name']}"
                e["_Category"] = "Functions"
                e["_Api"] = api
                e["_ApiName"] = apiname
                e["_UnicodeAlias"] = ua.get(e["Name"])
                ns[apiname] = e
        return ns

    # Rename conflicted name to put them in one namespace.
    def patch_name_conflict(self, ns: dict) -> dict:
        newns = {}
        defined = set()
        for apiname, e in ns.items():
            if e["Name"] in defined:
                print("patch_name_conflict:", e["_ApiName"])
                newname = e["_ApiName"].replace(".", "_")
                newapiname = f"{e['_Api']}.{newname}"
                self.patch_name(ns, e["_Api"], e["Name"], newname)
                e["Name"] = newname
                e["_ApiName"] = newapiname
                newns[newapiname] = e
            else:
                defined.add(e["Name"])
                newns[apiname] = e
        return newns

    def patch_name(self, node, api: str, name: str, newname: str) -> None:
        match node:
            case {"Kind": "ApiRef", "Api": api_, "Name": name_} if api_ == api and name_ == name:
                node["Name"] = newname
            case {}:
                for e in node.values():
                    self.patch_name(e, api, name, newname)
            case [*_]:
                for e in node:
                    self.patch_name(e, api, name, newname)

    def patch_struct_nested_type(self, ns: dict) -> dict:
        for e in ns.values():
            match e:
                case {"_Category": "Types", "Kind": "Struct" | "Union"}:
                    self.patch_nested_type(e)
        return ns

    # Rename nested type to {struct_name}_{nested_name}_e__{Struct|Union}.
    def patch_nested_type(self, e: dict) -> None:
        renamed = {}
        for n in e["NestedTypes"]:
            newname = f"{e['Name']}_{n['Name']}"
            if not (newname.endswith("_e__Struct") or newname.endswith("_e__Union")):
                newname = f"{newname}_e__{n['Kind']}"
            renamed[n["Name"]] = newname
            n["Name"] = newname
            self.patch_nested_type(n)
        for f in e["Fields"]:
            t = self.get_element_type(f["Type"])
            if t["Name"] in renamed:
                t["Name"] = renamed[t["Name"]]

    def get_element_type(self, e) -> str:
        match e:
            case {"Child": c}:
                return self.get_element_type(c)
            case _:
                return e

    def patch_enum(self, ns: dict) -> dict:
        for e in ns.values():
            match e:
                case {"_Category": "Types", "Kind": "Enum"}:
                    # IntegerBase can be null.  Default to Int32.
                    if not e["IntegerBase"]:
                        e["IntegerBase"] = "Int32"
                    # FIXME: enum value name? (NAME or ENUM_NAME or ENUM.Name?)
                    if self.enum_need_prefix(e):
                        for v in e["Values"]:
                            v["Name"] = f"{e['Name']}_{v['Name']}"
        return ns

    def enum_need_prefix(self, e: dict) -> bool:
        for v in e["Values"]:
            if not ("_" in v["Name"] or v["Name"].isupper()):
                return True
        return False

    # Add vtbl_index to COM methods.
    def patch_com_vtbl_index(self, ns: dict):
        for e in ns.values():
            match e:
                case {"_Category": "Types", "Kind": "Com", "Interface": interface, "Methods": [*methods]}:
                    vtbl_index = self.count_interface_method(interface, ns)
                    for m in methods:
                        m["_vtbl_index"] = vtbl_index
                        vtbl_index += 1
        return ns

    def count_interface_method(self, interface: dict, ns: dict) -> int:
        if not interface:
            return 0
        cls = ns[f"{interface['Api']}.{interface['Name']}"]
        return len(cls["Methods"]) + self.count_interface_method(cls["Interface"], ns)


class JsonLoader:
    def loadall(self, apipath):
        allmeta = {}
        for jsonfile in Path(apipath).glob("*.json"):
            api = jsonfile.stem
            allmeta[api] = json.loads(jsonfile.read_text())
        return allmeta

def main():
    allmeta = JsonLoader().loadall("win32json/api")
    ns = Preprocessor().preprocess(allmeta)
    ns = DependencyResolver().resolve(ns)
    s = MetadataTranspiler().transpile(ns)
    Path("win32more/all.py").write_text(s)

if __name__ == "__main__":
    main()
