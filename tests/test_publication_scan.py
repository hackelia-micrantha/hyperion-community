from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from publication_scan import scan


class PublicationScanTests(unittest.TestCase):
    def assert_blocked(self, name: str, content: str) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / name).parent.mkdir(parents=True, exist_ok=True)
            (root / name).write_text(content, encoding="utf-8")
            self.assertTrue(scan(root), content)

    def test_rejects_live_domain(self):
        self.assert_blocked("config.txt", "api.micrantha.com")

    def test_rejects_personal_home(self):
        self.assert_blocked("config.txt", "/home/operator/.ssh/id_ed25519")

    def test_rejects_age_recipient(self):
        self.assert_blocked("config.txt", "age1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")

    def test_rejects_private_key(self):
        self.assert_blocked("key.txt", "-----BEGIN OPENSSH PRIVATE KEY-----")

    def test_rejects_private_address(self):
        self.assert_blocked("inventory.ini", "node=192.168.50.12")

    def test_rejects_vpn_detail(self):
        self.assert_blocked("network.txt", "tailscale operator route")

    def test_rejects_encrypted_deployment_file(self):
        self.assert_blocked("secret.enc.yaml", "ciphertext")

    def test_allows_synthetic_cluster_ranges(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "example.txt").write_text("10.42.0.0/16 10.43.0.0/16", encoding="utf-8")
            self.assertEqual(scan(root), [])


if __name__ == "__main__":
    unittest.main()
