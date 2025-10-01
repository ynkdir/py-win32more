import re
from pathlib import Path

event_names = set()

for p in Path("packages").glob("**/Microsoft/UI/Xaml/**/*.py"):
    for line in p.read_text().splitlines():
        m = re.match(r"^    (.*) = event\(\)$", line)
        if m:
            event_names.add(m.group(1))

for name in sorted(event_names):
    print(name)
