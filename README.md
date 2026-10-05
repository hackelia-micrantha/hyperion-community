# Hyperion Community

Hyperion Community contains the reusable, deployment-neutral components of a privately operated infrastructure platform. Environment configuration, credentials, live cluster state, and deployment-specific composition remain private.

This is an inspectable public reference implementation, not a dump or mirror of the private operational source.

## What is implemented

- **OpenTofu/Terraform** — a provider-free synthetic reference-environment module.
- **Ansible/K3s** — a non-mutating-by-default K3s bootstrap role with checksum-verified opt-in binary installation.
- **Kubernetes/Kustomize** — a synthetic hardened workload, ServiceAccount, Service, NetworkPolicies, restricted Pod Security namespace, and local overlay.
- **Flux/GitOps** — a pinned Flux CLI and documented immutable-source consumption pattern.
- **CI/CD** — GitHub-hosted, least-privilege CI using the same mise contract as local verification.
- **Security/validation** — publication leakage tests, Terraform lint/validation, Ansible lint/check mode, Kubernetes schema validation, Trivy, and Checkov.
- **Architecture/governance** — public/private boundary, ownership model, provenance review, and threat model.

## Fresh-clone verification

Install [mise](https://mise.jdx.dev/), then run:

```bash
mise install
mise run doctor
mise run lint
mise run ci
```

The basic path requires no private repository, private cluster, cloud credential, or deployment secret.

CI initializes only the provider-free synthetic Terraform example, executes the Ansible example in check mode, renders synthetic Kubernetes manifests, and runs static/publication security checks. It does not deploy infrastructure.

## Repository layout

```text
terraform/
  modules/reference_environment/  provider-free reusable Terraform contract
examples/local/                   synthetic Terraform consumer
ansible/
  roles/k3s/                      checksum-verified K3s bootstrap primitive
  playbooks/reference.yml         non-mutating public validation path
k8s/
  base/                           synthetic hardened runtime fixture
  examples/local/                 Kustomize example
  flux/                           immutable-source GitOps guidance
scripts/
  publication_audit.py            deterministic publication-boundary audit
tests/
  test_publication_audit.py       regression tests for the audit
docs/
  architecture/                   boundary, ownership, provenance
  security/                       threat model and publication review
.github/workflows/ci.yml           hosted read-only CI
mise.toml                          reproducible task/tool interface
```

## Architecture

OpenTofu/Terraform owns infrastructure contracts. Ansible owns host/bootstrap automation. Kubernetes owns runtime resources. Flux is the intended GitOps reconciliation boundary for consumers of reviewed public revisions.

The public and private trust domains are deliberately separate. Public CI cannot read or deploy private state.

See:

- [architecture overview](docs/architecture/README.md)
- [publication boundary](docs/architecture/public-private-boundary.md)
- [ownership model](docs/architecture/ownership.md)
- [provenance/licensing review](docs/architecture/provenance.md)
- [threat model](docs/security/threat-model.md)

## Security properties in the reference slice

- synthetic/documentation-only identities and networks;
- no live SOPS/Vault ciphertext or age recipients;
- no private environment inventories or cluster overlays;
- fail-safe K3s role default;
- exact K3s release pin and upstream SHA-256 verification before binary installation;
- digest-pinned example container;
- restricted Pod Security namespace labels;
- non-root/read-only container with dropped capabilities and RuntimeDefault seccomp;
- disabled ServiceAccount token automount;
- ingress/egress default-deny NetworkPolicy with bounded namespace-local ingress;
- read-only public CI permissions and commit-pinned third-party Actions;
- no Terraform plan/state artifacts uploaded.

See [SECURITY.md](SECURITY.md) and [publication review](docs/security/publication-review.md).

## Maturity and limitations

The source-level and synthetic validation path is real. This initial slice does **not** claim:

- end-to-end K3s cluster creation or upgrade lifecycle;
- production-ready cloud provisioning;
- parity with any private environment;
- production Flux bootstrap;
- backup/restore or observability deployment;
- production portability of private composition.

Those capabilities require separate runtime evidence before they can be represented as supported.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Apache License 2.0. See [LICENSE](LICENSE).

This license applies to Hyperion Community only; it does not change the licensing or visibility of privately operated source.
