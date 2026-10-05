# Security policy

Hyperion Community is a public reference implementation. Do not publish private deployment credentials, inventories, live encrypted secrets, key recipients, topology, personal/operator paths, or operational network/runner details in issues, pull requests, fixtures, or logs.

For a vulnerability in public example code that contains no sensitive deployment information, open a normal GitHub issue with a minimal reproduction.

For sensitive reports, use GitHub's private vulnerability-reporting/security-advisory path when available. Do not place sensitive values or private infrastructure details in a public issue.

## Supported surface

Security support covers the exact public source on `main` and published releases when releases exist. Runtime behavior that the README marks deferred or unvalidated is not represented as a supported production deployment.

A secret remains sensitive when encrypted. Live SOPS/Vault ciphertext and real key recipients are not acceptable public fixtures.
