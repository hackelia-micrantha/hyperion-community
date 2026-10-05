# Publication boundary review

Reviewed private source: `hackelia-micrantha/hyperion` `main` at `fc35b8c0ee9911ecaf37636d5eacfb99f24f4b79`. This records provenance only; private Git history is not imported.

| Private path | Classification | Public treatment |
|---|---|---|
| `terraform/modules/` | PUBLIC-AFTER-SANITIZATION | Generic patterns only; remove deployment identities and assumptions. |
| `terraform/environments/` | PRIVATE-DEPLOYMENT | Synthetic `examples/local/` instead. |
| `cloud-init/` | PUBLIC-AFTER-SANITIZATION | Rework identities and credentials first. |
| `ansible/roles/k3s/` | PUBLIC-AFTER-SANITIZATION | Remove deployment user paths and harden downloads. |
| `ansible/roles/common/` | PUBLIC-AFTER-SANITIZATION | Review individual generic tasks. |
| `ansible/roles/security/` | PUBLIC-AFTER-SANITIZATION | Generic hardening only; no real key configuration. |
| `ansible/roles/flux/` | PUBLIC-AFTER-SANITIZATION | Private repository identity/credentials require redesign. |
| `ansible/inventories/` | PRIVATE-DEPLOYMENT | Never copy real inventories. |
| `k8s-gitops/**/base/` | PUBLIC-EXAMPLE-ONLY | Existing base reveals service inventory; use synthetic manifests. |
| `k8s-gitops/**/overlays/` | PRIVATE-DEPLOYMENT | Environment/domain topology remains private. |
| `k8s-gitops/secrets/`, `*.enc.yaml` | PRIVATE-SECURITY | Do not publish deployment ciphertext. |
| `.sops.yaml` | PRIVATE-SECURITY | Real recipient/key policy remains private. |
| deployment workflows | PRIVATE-DEPLOYMENT | Live credential interfaces/assumptions remain private. |
| standards workflow | PUBLIC-AFTER-SANITIZATION | Reuse rootless validation pattern on public runners. |
| `mise.toml` | PUBLIC-AFTER-SANITIZATION | Reuse task interface without private assumptions. |
| `scripts/` | NEEDS-DECISION | Review individually. |
| `docs/` | NEEDS-DECISION | Publish architecture concepts, not operational details. |
| AI/prompt/context | PRIVATE-SECURITY | Keep operational context private initially. |
| Dubnium integration | PRIVATE-SECURITY | Keep runner/capability details private initially. |
| application/service manifests | PRIVATE-DEPLOYMENT | Use synthetic examples. |
| legacy Make interface | OBSOLETE | Public interface is `mise`. |

The reviewed private tree contains deployment-specific domains, filesystem paths, inventories, private address material, VPN integration, encrypted secret configuration, and application/service names. This justifies synthetic reconstruction rather than bulk copying.

Target ownership is public for reusable deployment-neutral components and private for environment composition. Private Hyperion should consume stable public-owned components in a later synchronization phase.
