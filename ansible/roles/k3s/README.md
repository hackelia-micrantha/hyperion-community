# K3s bootstrap role

This public role is intentionally bounded.

By default it validates the exact K3s release pin and performs no host mutation. Setting `k3s_install_binary: true` downloads the selected upstream K3s binary only after resolving and matching the architecture-specific upstream SHA-256 checksum.

Supported release assets are `k3s` with `sha256sum-amd64.txt` on x86_64, `k3s-arm64` with `sha256sum-arm64.txt` on aarch64, and `k3s-armhf` with `sha256sum-arm.txt` on supported 32-bit ARM. Unknown architectures fail closed. A valid checksum and binary download do not by themselves qualify cluster installation or lifecycle.

The first public slice does not configure server/agent systemd units, distribute cluster tokens, expose kubeconfig, or encode environment-specific topology. Those lifecycle operations require privileged runtime integration evidence before they can be represented as supported public behavior.
