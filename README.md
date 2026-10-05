# Hyperion Community

Hyperion Community contains the reusable, deployment-neutral components of a privately operated infrastructure platform. Environment configuration, credentials, live cluster state, and deployment-specific composition remain private.

This repository is intentionally a small public reference implementation, not a dump of the private operational repository. It demonstrates the same engineering boundaries with synthetic inputs and independent validation.

## What is here

- `terraform/modules/` — deployment-neutral OpenTofu/Terraform modules.
- `ansible/roles/` — reusable host/K3s configuration contracts.
- `k8s/base/` and `k8s/examples/` — synthetic Kubernetes/Kustomize configuration.
- `examples/local/` — a no-cloud local Terraform example using `terraform_data`.
- `tests/` — publication-boundary checks.
- `.github/workflows/` — hosted CI using the same `mise` tasks as local validation.
- `docs/` — architecture, publication boundary, ownership, and threat model.

The private Hyperion repository remains the operational source for real environments and deployment-specific composition. It is not required to validate this repository.

## Verification

Install mise, then run:

```bash
mise install
mise run doctor
mise run lint
mise run ci
```

The CI path is rootless and does not deploy infrastructure. It validates Terraform, Ansible, Kubernetes/Kustomize, and publication-boundary rules. A disposable K3s deployment is not yet claimed by this first slice.

## Architecture

OpenTofu/Terraform owns infrastructure inputs and outputs. Ansible owns host configuration. Kubernetes owns runtime resources. Flux is the intended reconciliation boundary for GitOps deployments. This public slice keeps those contracts inspectable without publishing real environments, inventories, service topology, or credentials.

See `docs/architecture/README.md` and `docs/architecture/ownership.md`.

## Public/private boundary

Public code must be deployment-neutral. Do not publish production inventories, real environment roots, live cluster overlays, encrypted production secrets, real key recipients, private service inventory, personal filesystem paths, internal domains, private repository relationships, or operational SSH/VPN details.

See `docs/architecture/public-private-boundary.md` and `docs/security/threat-model.md`.

## Maturity

This is an initial extraction. The validation path is real; the example infrastructure is intentionally non-destructive. The repository does not yet claim production portability, a complete local K3s deployment, cloud provisioning, production GitOps bootstrap, backup/restore, or observability deployment.

## License

Licensing is intentionally pending the provenance and compatibility review tracked in issue #5. Repository visibility is not a license grant. The private Hyperion repository remains separately licensed and private.
