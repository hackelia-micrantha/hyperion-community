# K3s bootstrap role

This public role is intentionally bounded.

By default it validates the exact K3s release pin and performs no host mutation. Setting `k3s_install_binary: true` downloads the selected upstream K3s binary only after resolving and matching the architecture-specific upstream SHA-256 checksum.

The first public slice does not configure server/agent systemd units, distribute cluster tokens, expose kubeconfig, or encode environment-specific topology. Those lifecycle operations require privileged runtime integration evidence before they can be represented as supported public behavior.