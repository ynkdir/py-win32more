import importlib.resources
import lzma

resources = importlib.resources.files() / "resources"


def exists(name: str) -> bool:
    return (resources / name).is_file() or (resources / name).is_dir()


def read_text(name: str) -> str:
    if name.endswith(".xz"):
        return lzma.decompress(read_bytes(name)).decode()
    return (resources / name).read_text()


def read_bytes(name: str) -> bytes:
    return (resources / name).read_bytes()
