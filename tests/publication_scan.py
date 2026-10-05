"""Compatibility wrapper for the consolidated publication audit."""

from scripts.publication_audit import audit


def scan(root):
    return audit(root)
