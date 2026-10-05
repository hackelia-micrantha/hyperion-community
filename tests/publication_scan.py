from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", ".venv", ".mise"}
RULES = {
    "private domain": re.compile(r"(?i)(?:[a-z0-9-]+\.)*micrantha\.(?:com|net|org|dev|local|test)"),
    "personal path": re.compile(r"/home/(?!example(?:/|$))[A-Za-z0-9._-]+/"),
    "age recipient": re.compile(r"\bage1[0-9a-z]{20,}"),
    "private key": re.compile(r"-----BEGIN (?:OPENSSH |RSA |EC )?PRIVATE KEY-----"),
    "private IPv4": re.compile(r"\b(?:10\.(?!42\.|43\.)\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})\b"),
    "tailscale detail": re.compile(r"(?i)\b(?:tailscale|tailnet|tskey-)\b"),
}
ALLOWED = {
    "docs/architecture/public-private-boundary.md",
    "README.md",
    "SECURITY.md",
    "tests/publication_scan.py",
    "tests/test_publication_scan.py",
}


def scan(root: Path) -> list[str]:
    errors: list[str] = []
    for path in root.rglob("*"):
        if not path.is_file() or any(part in SKIP for part in path.parts):
            continue
        rel = path.relative_to(root).as_posix()
        if root == ROOT and rel in ALLOWED:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in RULES.items():
            if pattern.search(content):
                errors.append(f"{rel}: matched {label}")
        if rel.endswith((".enc.yaml", ".enc.yml")):
            errors.append(f"{rel}: encrypted deployment file is not public input")
    return errors


if __name__ == "__main__":
    target = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT
    errors = scan(target)
    if errors:
        raise SystemExit("\n".join(errors))
    print("publication boundary scan passed")
