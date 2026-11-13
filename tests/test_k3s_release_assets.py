"""Protect the architecture-to-release-asset contract of the public K3s role."""

from pathlib import Path
import unittest

import yaml


TASKS = yaml.safe_load(
    (Path(__file__).resolve().parents[1] / "ansible/roles/k3s/tasks/main.yml")
    .read_text(encoding="utf-8")
)


def task(name: str) -> dict:
    matches = [item for item in TASKS if item.get("name") == name]
    if len(matches) != 1:
        raise AssertionError(f"Expected one K3s task named {name!r}")
    return matches[0]


class K3sReleaseAssetsTests(unittest.TestCase):
    def test_supported_architectures_select_existing_upstream_assets(self):
        # Names verified against the upstream K3s v1.28.3+k3s2 release.
        mapping = task("Resolve K3s release architecture")["vars"]["k3s_arch_map"]
        self.assertEqual(
            mapping,
            {
                "x86_64": {"checksum_arch": "amd64", "asset": "k3s"},
                "aarch64": {"checksum_arch": "arm64", "asset": "k3s-arm64"},
                "armv7l": {"checksum_arch": "arm", "asset": "k3s-armhf"},
                "armv6l": {"checksum_arch": "arm", "asset": "k3s-armhf"},
            },
        )

    def test_checksum_selection_and_download_use_same_asset(self):
        resolver = task("Resolve K3s release architecture")["ansible.builtin.set_fact"]
        self.assertIn("k3s_arch_map.get(ansible_architecture", resolver["k3s_release_arch"])
        self.assertIn("k3s_arch_map.get(ansible_architecture", resolver["k3s_binary_asset"])

        checksum = task("Fetch upstream K3s checksum list")["ansible.builtin.uri"]
        self.assertIn("sha256sum-{{ k3s_release_arch }}.txt", checksum["url"])
        selector = task("Select checksum line for the K3s binary")["ansible.builtin.set_fact"]
        self.assertIn("k3s_binary_asset", selector["k3s_checksum_matches"])
        self.assertIn("'$'", selector["k3s_checksum_matches"])

        download = task("Download checksum-verified K3s binary")["ansible.builtin.get_url"]
        self.assertIn("{{ k3s_binary_asset }}", download["url"])
        self.assertEqual(download["checksum"], "{{ k3s_binary_checksum }}")
        self.assertTrue(task("Download checksum-verified K3s binary")["become"])

    def test_unsupported_architecture_is_rejected_before_fetch(self):
        guard = task("Require a supported K3s architecture")["ansible.builtin.assert"]["that"]
        self.assertIn("k3s_release_arch | length > 0", guard)
        self.assertIn("k3s_binary_asset | length > 0", guard)
        self.assertLess(TASKS.index(task("Require a supported K3s architecture")),
                        TASKS.index(task("Fetch upstream K3s checksum list")))


if __name__ == "__main__":
    unittest.main()
