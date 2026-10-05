# Threat model

The highest-risk boundary is private operational source to public source, so there is no automated bulk mirror. Contributor input is untrusted in CI. Examples are test inputs, not production defaults. Terraform plans and rendered secrets are not retained.

| Threat | Control |
|---|---|
| Secret or ciphertext leakage | Synthetic fixtures only; publication scan; no live encrypted deployment files. |
| Topology disclosure | Synthetic inputs; no real inventories or overlays. |
| History leakage | Clean public history; provenance records source SHA only. |
| CI supply-chain compromise | Immutable action SHAs; read-only permissions; pinned tools. |
| Unsafe Kubernetes examples | Non-root, read-only root filesystem, dropped capabilities, seccomp, resources. |
| Terraform leakage | Local synthetic resources; no plan artifacts. |
| SSH trust bypass | No SSH deployment path in the first slice. |
| Self-hosted runner exposure | Public CI uses hosted runners. |
| Documentation overclaim | README separates validation from unimplemented deployment paths. |
