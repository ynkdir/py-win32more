import re
import sys
from pathlib import Path
from subprocess import run

for p in Path(".").glob("packages/Microsoft.*"):
    name, version = re.split(r"\.(?=\d)", p.name, maxsplit=1)
    run([sys.executable, "scripts/build_subpackage.py", "--name", name, "--version", version], check=True)
