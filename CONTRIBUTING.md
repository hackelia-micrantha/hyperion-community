# Contributing

Contributions should improve the deployment-neutral public contract.

Before opening a pull request:

    mise install
    mise run doctor
    mise run lint
    mise run ci

## Publication rules

- create purpose-built synthetic fixtures; do not paste a private deployment file and redact it in place;
- do not contribute live encrypted secrets, key recipients, environment inventories, topology, private repository identifiers, personal paths, or operator network details;
- keep examples fail-safe and clearly distinguish source validation from runtime-tested support;
- bind external CI actions and runtime images immutably where supported.

## Pull-request evidence

Describe the observable outcome, affected component, security/publication impact, and exact-candidate validation. Call out any change to the public/private ownership boundary.

Copied/vendored third-party material requires explicit provenance and license review before merge.
