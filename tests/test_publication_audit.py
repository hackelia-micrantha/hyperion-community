from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.publication_audit import audit


class PublicationAuditTests(unittest.TestCase):
    def test_accepts_synthetic_public_content(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "example.md").write_text(
                "endpoint=https://service.example.com\n"
                "contact=security@example.com\n",
                encoding="utf-8",
            )
            self.assertEqual(audit(root), [])

    def test_rejects_personal_home_path(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "leak.md").write_text(
                "key=/home/private-operator/.ssh/id_ed25519\n",
                encoding="utf-8",
            )
            self.assertTrue(any("personal home path" in item for item in audit(root)))

    def test_rejects_live_encrypted_secret_filename(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "credential.enc.yaml").write_text(
                "kind: Secret\n",
                encoding="utf-8",
            )
            self.assertTrue(
                any("forbidden publication path" in item for item in audit(root))
            )

    def test_rejects_private_repository_reference(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "source.md").write_text(
                "source=hackelia-micrantha/hyperion\n",
                encoding="utf-8",
            )
            self.assertTrue(
                any("private repository reference" in item for item in audit(root))
            )

    def test_rejects_private_network_address(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "inventory.txt").write_text(
                "node=192.168.50.12\n",
                encoding="utf-8",
            )
            self.assertTrue(
                any("RFC1918 IPv4 address" in item for item in audit(root))
            )

    def test_rejects_tailscale_detail(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "network.txt").write_text(
                "tailscale operator route\n",
                encoding="utf-8",
            )
            self.assertTrue(
                any("operational Tailscale reference" in item for item in audit(root))
            )

    def test_rejects_non_example_email(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "contact.md").write_text(
                "contact=operator@corp.invalid\n",
                encoding="utf-8",
            )
            self.assertTrue(
                any("non-example email address" in item for item in audit(root))
            )


if __name__ == "__main__":
    unittest.main()
