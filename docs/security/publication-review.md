# Publication review

Run this review against the exact candidate revision.

## Automated gates

1. `mise run publication-audit`
2. `mise run lint`
3. `mise run ci`

## Manual gates

- inspect the complete changed-file list and rendered synthetic manifests;
- confirm no private history, live deployment files, ciphertext, or exact private provenance identifiers were introduced;
- search for credentials, private keys/key paths, age recipients, private/internal identifiers, personal paths, live domains, private repository relationships, service/deployment identifiers, and SSH/VPN/operator details;
- confirm Terraform does not persist or upload state/plan data;
- confirm CI remains least-privilege and uses immutable Action references;
- confirm workload images are immutable by digest;
- confirm documentation claims match exact validated behavior;
- confirm no critical publication/security finding remains.

If sensitive data is found, review output records only its class, location, impact, and remediation—not the secret value.