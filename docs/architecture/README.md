# Architecture

Hyperion separates four concerns: OpenTofu/Terraform for infrastructure contracts; Ansible for host configuration; Kubernetes/Kustomize for runtime resources; and Flux as the GitOps reconciliation boundary.

The public repository owns reusable, deployment-neutral implementation. The private repository owns real environment composition and operational state.

The first slice intentionally uses `terraform_data` so validation requires no credentials and creates no external resources. The K3s role exposes a minimal configuration contract. The Kubernetes example is synthetic and hardened as a validation fixture.
