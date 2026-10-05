from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", ".venv", ".mise"}
rules = {
    "private domain": re.compile(r"(?i)(?:[a-z0-9-]+\.)*micrantha\.(?:com|net|org|dev|local|test)"),
    "personal path": re.compile(r"/home/(?!example(?:/|$))[A-Za-z0-9._-]+/"),
    "age recipient": re.compile(r"\bage1[0-9a-z]{20,}"),
    "private key": re.compile(r"-----BEGIN (?:OPENSSH |RSA |EC )?PRIVATE KEY-----"),
}
allowed = {
    "docs/architecture/public-private-boundary.md",
    "README.md",
    "SECURITY.md",
    "tests/publication_scan.py",
}
errors = []
for path in ROOT.rglob("*"):
    if not path.is_file() or any(part in SKIP for part in path.parts):
        continue
    rel = path.relative_to(ROOT).as_posix()
    if rel in allowed:
        continue
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    for label, pattern in rules.items():
        if pattern.search(content):
            errors.append(f"{rel}: matched {label}")
    if rel.endswith((".enc.yaml", ".enc.yml")):
        errors.append(f"{rel}: encrypted deployment file is not public input")
if errors:
    raise SystemExit("\n".join(errors))
print("publication boundary scan passed")
