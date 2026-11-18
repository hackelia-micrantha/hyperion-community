# Hyperion Community

**Reproducible infrastructure. Secure delivery. Inspectable engineering.**

[![CI](https://github.com/hackelia-micrantha/hyperion-community/actions/workflows/ci.yml/badge.svg)](https://github.com/hackelia-micrantha/hyperion-community/actions/workflows/ci.yml) [![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)

Hyperion Community is a public platform engineering reference implementation for infrastructure as code, Kubernetes, GitOps, CI/CD and infrastructure security. It demonstrates how to separate infrastructure provisioning, host bootstrap and workload reconciliation while keeping validation reproducible and deployment authority bounded.

The repository contains executable, deployment-neutral modules and examples, not just architecture documents. It is the reusable public surface of a privately operated platform; live environment composition, credentials and operational state remain private.

[Explore the architecture](docs/architecture/README.md) · [Inspect CI](https://github.com/hackelia-micrantha/hyperion-community/actions/workflows/ci.yml) · [Verify from a fresh clone](#fresh-clone-verification)

## Engineering evidence

| Discipline | Inspectable implementation | Verification |
| --- | --- | --- |
| Infrastructure as code | [Reference environment](terraform/modules/reference_environment/) and [Incus instance module](terraform/modules/incus_instance/) | OpenTofu validation against synthetic inputs and a locked provider schema; TFLint |
| Host automation | [K3s bootstrap role](ansible/roles/k3s/) | Ansible syntax, check mode and lint; opt-in checksum-verified binary acquisition |
| Kubernetes security | [Hardened workload](k8s/base/) and [local overlay](k8s/examples/local/) | Kustomize rendering, strict Kubernetes schema checks, IaC policy scanning |
| GitOps | [Immutable source consumption](k8s/flux/) | Documented Flux integration boundary; no live reconciliation claim |
| Secure software delivery | [Hosted CI](.github/workflows/ci.yml) and [mise tasks](mise.toml) | Read-only, commit-pinned Actions; common local and CI tasks |
| Threat modeling and governance | [Threat model](docs/security/threat-model.md) and [publication audit](scripts/publication_audit.py) | Regression tests for representative private-data leakage classes |

### Design decisions

- **Separate ownership:** OpenTofu/Terraform defines infrastructure, Ansible handles bootstrap, Kubernetes defines workloads, and Flux provides the intended reconciliation boundary. See the [ownership model](docs/architecture/ownership.md).
- **Fail-safe automation:** validation does not provision infrastructure or require operational secrets; installation effects are explicit.
- **Security by construction:** restricted Pod Security, default-deny networking, immutable image references and least-privilege CI are inspectable in source.
- **Evidence over claims:** distinguish schema and source validation from runtime qualification. The [draft source-alpha notes](docs/releases/v0.1.0-alpha.1.md) document the current limits; no release has been published.

## What is implemented

- **OpenTofu/Terraform** — a provider-free synthetic reference-environment module and a deployment-neutral Incus instance module with a credential-free provider-schema validation example.
- **Ansible/K3s** — a non-mutating-by-default K3s bootstrap role with checksum-verified opt-in binary installation.
- **Kubernetes/Kustomize** — a synthetic hardened workload, ServiceAccount, Service, NetworkPolicies, restricted Pod Security namespace, and local overlay.
- **Flux/GitOps** — a pinned Flux CLI and documented immutable-source consumption pattern.
- **CI/CD** — GitHub-hosted, least-privilege CI using the same mise contract as local verification.
- **Security/validation** — publication leakage tests, Terraform lint/validation, Ansible lint/check mode, Kubernetes schema validation, Trivy, and Checkov.
- **Architecture/governance** — public/private boundary, ownership model, provenance review, and threat model.

## Fresh-clone verification

The hosted verification path runs on Ubuntu 24.04. In a disposable checkout, install [mise](https://mise.jdx.dev/), then run:

```bash
mise install
mise run doctor
mise run lint
mise run ci
```

The basic path requires no private repository, private cluster, cloud credential, or deployment secret. It downloads public tools and dependencies and creates local validation files.

CI validates the provider-free Terraform example and initializes the Incus example only to check provider/schema compatibility (no plan, apply, backend state, or Incus API connection). It also executes the Ansible example in check mode, renders synthetic Kubernetes manifests, and runs static/publication security checks. It does not deploy infrastructure.

## Repository layout

```text
terraform/
  modules/reference_environment/  provider-free reusable Terraform contract
  modules/incus_instance/         provider-backed Incus instance abstraction
examples/local/                   synthetic Terraform consumer
examples/incus-instance/          credential-free Incus schema-validation consumer
ansible/
  roles/k3s/                      checksum-verified K3s bootstrap primitive
  playbooks/reference.yml         non-mutating public validation path
k8s/
  base/                           synthetic hardened runtime fixture
  examples/local/                 Kustomize example
  flux/                           immutable-source GitOps guidance
web/                              static provider-neutral project site
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

## Website publication

The public landing page is the static artifact under [`web/`](web/README.md).
It does not require a Cloudflare Workers runtime, Node compatibility flags,
provider observability, or deployment credentials.

Repository CI validates the site source as part of the normal test suite but
does not deploy it. External preview/hosting availability is intentionally
non-authoritative: a preview-provider failure must not make source CI red or
justify adding runtime compatibility, telemetry, or credentials that the
static site does not otherwise need.

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

Current maturity: an independently inspectable source reference with synthetic validation. It is not a production-ready distribution or a published release. This slice does **not** claim:

- end-to-end K3s cluster creation or upgrade lifecycle;
- production-ready cloud provisioning;
- parity with any private environment;
- production Flux bootstrap;
- backup/restore or observability deployment;
- production portability of private composition.

Those capabilities require separate runtime evidence before they can be represented as supported.

## Roadmap — planned, not shipped

The next milestones prioritize runtime and consumer evidence over adding new platform components.

| Horizon | Engineering outcome | Tracking |
| --- | --- | --- |
| Now | Qualify the public source alpha through independent fresh-clone acceptance, archive integrity and publication review | [#29](https://github.com/hackelia-micrantha/hyperion-community/issues/29) |
| Next | Prove disposable K3s server/agent lifecycle and Flux reconciliation, including readiness and teardown | [#16](https://github.com/hackelia-micrantha/hyperion-community/issues/16), [#18](https://github.com/hackelia-micrantha/hyperion-community/issues/18) |
| Next | Qualify version-pinned component consumption and Incus lifecycle independently of provider-schema validation | [#11](https://github.com/hackelia-micrantha/hyperion-community/issues/11) |
| Later | Distribute Hyperctl as a verifiable, independently installable operator CLI package | [#2](https://github.com/hackelia-micrantha/hyperion-community/issues/2) |

Longer-term platform engineering goals include rootless Podman-backed role testing, exact-revision deployment readiness evidence, signed build and deployment provenance (Sigstore/in-toto), and exercised rollback, drift detection and recovery. These are design directions, not capabilities distributed or validated by this repository. No release dates or production-readiness guarantees are implied.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Apache License 2.0. See [LICENSE](LICENSE).

This license applies to Hyperion Community only; it does not change the licensing or visibility of privately operated source.
