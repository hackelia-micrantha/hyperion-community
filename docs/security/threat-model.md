# Threat model

## Security objective

Publishing reusable platform engineering must not disclose or create authority over the privately operated environment.

## Trust boundary

```text
untrusted contributor / pull request
             |
             v
       public source
             |
             v
 GitHub-hosted validation
             |
             X  no private credential/deployment path
             |
 private deployment composition -> live infrastructure
```

## Assets kept outside the public repository

- credentials, private keys, password material, and deployment tokens;
- live encrypted secrets and key recipients;
- environment inventories and cluster/application topology;
- private network, SSH/VPN, runner, and capability details;
- live Terraform state/plans and production GitOps overlays;
- private deployment workflows and operator context.

## Threats and controls

| Threat | Control |
|---|---|
| Secret/ciphertext publication | Synthetic fixtures, path/content publication audit, exact-tree review; live encrypted files remain private. |
| Topology/identity disclosure | Documentation-only fixtures; no real inventories, domains, personal paths, repository identifiers, or exact private revision identifiers. |
| Private history exposure | Clean public history; exact private provenance evidence is retained privately. |
| CI supply-chain substitution | Third-party Actions pinned by commit SHA; tool versions pinned; hosted runner with read-only repository permission. |
| Unsafe container substitution | Example image bound to an OCI digest. |
| Unsafe Kubernetes defaults | Restricted Pod Security namespace labels, non-root/read-only container, dropped capabilities, seccomp, probes/resources, ServiceAccount token disabled, NetworkPolicy. |
| Terraform plan/state leakage | Provider-free synthetic module; no plan/state artifacts retained. |
| Mutable remote bootstrap script | K3s role downloads an exact release binary only after matching the upstream checksum; no curl-pipe-shell installer. |
| SSH trust bypass | No SSH deployment path exists in the first slice. |
| Self-hosted runner exposure | Public CI uses GitHub-hosted runners only. |
| Documentation overclaim | README separates source-level evidence from deferred runtime capabilities. |
| Public/private code divergence | One-owner model with immutable private consumption after migration. |

## Residual risk

Static gates cannot prove absence of every sensitive semantic relationship. Exact-candidate publication review remains required. End-to-end K3s lifecycle, cloud provisioning, and production Flux bootstrap are not yet validated public capabilities.