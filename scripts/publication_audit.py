#!/usr/bin/env python3
"""Fail closed on representative public/private boundary leaks."""

from __future__ import annotations

import re
import sys
from pathlib import Path

SKIP_DIRS = {".git", ".venv", ".mise", ".terraform", "__pycache__"}
SKIP_FILES = {
    Path("scripts/publication_audit.py"),
    Path("tests/test_publication_audit.py"),
}
TEXT_SUFFIXES = {
    ".cfg",
    ".html",
    ".json",
    ".md",
    ".py",
    ".tf",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}
TEXT_NAMES = {"LICENSE", "SECURITY.md", "CONTRIBUTING.md"}

FORBIDDEN_PATHS = (
    re.compile(r"(^|/)\.sops\.ya?ml$", re.IGNORECASE),
    re.compile(r"(^|/)vault\.ya?ml$", re.IGNORECASE),
    re.compile(r"\.enc\.ya?ml$", re.IGNORECASE),
    re.compile(r"(^|/)ansible/inventories?(/|$)", re.IGNORECASE),
)

CONTENT_RULES: dict[str, re.Pattern[str]] = {
    "private repository reference": re.compile(
        r"hackelia-micrantha/hyperion(?!-community)", re.IGNORECASE
    ),
    "live Micrantha domain": re.compile(
        r"(?<![A-Za-z0-9-])(?:[A-Za-z0-9-]+\.)*micrantha\."
        r"(?:com|dev|net|org|local|test)\b",
        re.IGNORECASE,
    ),
    "personal home path": re.compile(r"/home/[A-Za-z0-9._-]+"),
    "age recipient": re.compile(r"\bage1[0-9a-z]{20,}\b"),
    "RFC1918 IPv4 address": re.compile(
        r"\b(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|"
        r"172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2})\b"
    ),
    "operational Tailscale reference": re.compile(r"\btailscale\b", re.IGNORECASE),
    "private key marker": re.compile(
        r"-----BEGIN (?:OPENSSH |RSA |EC |DSA )?PRIVATE KEY-----"
    ),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "GitHub token-like value": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    "private runner identifier": re.compile(r"\brunner-hyperion\b", re.IGNORECASE),
    "live secret interface": re.compile(
        r"\b(?:ANSIBLE_VAULT_PASSWORD|SSH_PRIVATE_KEY|MICRANTHA_[A-Z0-9_]+)\b"
    ),
    "private project host reference": re.compile(
        r"gitlab\.com/(?:hackelia-)?micrantha/", re.IGNORECASE
    ),
    "non-example email address": re.compile(
        r"\b[A-Z0-9._%+-]+@(?!example\.com\b)[A-Z0-9.-]+\.[A-Z]{2,}\b",
        re.IGNORECASE,
    ),
}


def _iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if rel in SKIP_FILES:
            continue
        yield path, rel


def audit(root: Path) -> list[str]:
    findings: list[str] = []
    for path, rel in _iter_files(root):
        rel_text = rel.as_posix()

        for rule in FORBIDDEN_PATHS:
            if rule.search(rel_text):
                findings.append(f"{rel_text}: forbidden publication path")
                break

        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in TEXT_NAMES:
            continue

        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        for label, pattern in CONTENT_RULES.items():
            if pattern.search(content):
                findings.append(f"{rel_text}: {label}")

    return sorted(set(findings))


def main(argv: list[str]) -> int:
    root = Path(argv[1] if len(argv) > 1 else ".").resolve()
    findings = audit(root)
    if findings:
        print("publication audit failed:", file=sys.stderr)
        for finding in findings:
            print(f"  - {finding}", file=sys.stderr)
        return 1
    print("publication audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
