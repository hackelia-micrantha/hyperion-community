# Architecture

Hyperion Community separates four concerns:

1. **OpenTofu/Terraform** — deployment-neutral infrastructure contracts and synthetic examples.
2. **Ansible** — host/bootstrap automation with fail-safe public defaults.
3. **Kubernetes/Kustomize** — synthetic runtime resources and security policy.
4. **Flux** — the documented GitOps reconciliation boundary for consumers of reviewed public revisions.

The public repository owns deployment-neutral implementation after publication review. The privately operated source owns real environment composition, credentials, live topology, operational policy, and private integrations.

The first slice intentionally uses `terraform_data` so Terraform validation requires no provider credentials and creates no external resources. The K3s role performs no mutation by default and can opt into checksum-verified binary installation. The Kubernetes fixture is synthetic, policy-constrained, and independently rendered/schema-validated.

Flux bootstrap into a live cluster is deliberately not part of the basic verification path; `k8s/flux/README.md` documents an immutable public-source consumption pattern.