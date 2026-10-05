# Publication boundary review

Hyperion Community is a clean public implementation surface, not a mirror of the privately operated platform. Exact private-source revision evidence is retained in private operational tracking rather than embedded in this public repository.

Private Git history is never imported. Reusable concepts cross the boundary only after review, and deployment-specific data is replaced by purpose-built synthetic fixtures rather than redacted live files.

| Component family | Classification | Public treatment |
|---|---|---|
| `terraform/modules/` patterns | PUBLIC-AFTER-SANITIZATION | Publish deployment-neutral modules only after removing environment identities and assumptions. |
| Terraform environment roots, backends, state composition | PRIVATE-DEPLOYMENT | Use synthetic/provider-free examples publicly. |
| cloud-init patterns | PUBLIC-AFTER-SANITIZATION | Rebuild around synthetic identities and secret-free defaults. |
| generic `ansible/roles/` | PUBLIC-AFTER-SANITIZATION | Publish individually reviewed roles with deployment-neutral inputs. |
| Ansible inventories, host/group vars, Vault material | PRIVATE-DEPLOYMENT / PRIVATE-SECURITY | Never copy live inventories or secret-bearing configuration. |
| K3s bootstrap patterns | PUBLIC-AFTER-SANITIZATION | Publish bounded primitives; no live tokens, users, addresses, or operator paths. |
| Flux/GitOps support | PUBLIC-AFTER-SANITIZATION / PUBLIC-EXAMPLE-ONLY | Publish immutable-source patterns; keep live bootstrap credentials and environment reconciliation private. |
| `k8s-gitops/` application/service base | PUBLIC-EXAMPLE-ONLY | Live service inventory stays private; public manifests are synthetic equivalents. |
| cluster/environment overlays | PRIVATE-DEPLOYMENT | Do not publish production/staging/dev composition. |
| `.sops.yaml`, age recipients, SOPS/Vault ciphertext | PRIVATE-SECURITY | Never publish live deployment material merely because it is encrypted. |
| deployment workflows with credential interfaces | PRIVATE-SECURITY | Remain private. |
| reusable validation workflows | PUBLIC-AFTER-SANITIZATION | Rewrite for hosted, least-privilege CI with no live infrastructure assumptions. |
| `mise.toml` task interface | PUBLIC-AFTER-SANITIZATION | Public tasks own only public verification paths. |
| operational `scripts/` | NEEDS-DECISION | Review one-by-one; do not bulk-copy. |
| architecture/security `docs/` | PUBLIC-AFTER-SANITIZATION | Publish public contracts, not topology or operator details. |
| AI/prompt/context documents | PRIVATE-SECURITY | Outside the initial public distribution. |
| Dubnium/runner/capability integration | PRIVATE-SECURITY | Secondary; publish only future deployment-neutral contracts after separate review. |
| application/service manifests | PRIVATE-DEPLOYMENT | Replace with synthetic examples. |
| legacy Make compatibility surface | OBSOLETE for public distribution | The public task interface is mise. |

## Synthetic fixture rules

Public fixtures use:

- `example.com` names and documentation-only identities;
- documentation address ranges where network values are needed;
- no private keys, passwords, API tokens, or real encrypted secrets;
- no live/private hostnames, inventories, or operator filesystem paths;
- no private repository identifiers or exact private provenance revisions;
- no production application/service inventory.

## Review rule

A component crosses the boundary only when the exact candidate passes publication audit, static/security checks, documentation consistency review, and the applicable merge gate. Uncertainty resolves to private-by-default.
