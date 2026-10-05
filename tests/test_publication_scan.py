"""Compatibility coverage for the consolidated publication audit."""

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from publication_scan import scan


class PublicationScanCompatibilityTests(unittest.TestCase):
    def test_synthetic_fixture_is_allowed(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "example.txt").write_text("service.example.com", encoding="utf-8")
            self.assertEqual(scan(root), [])


if __name__ == "__main__":
    unittest.main()
