# Provenance and licensing review

## Public history

The repository's pre-existing public history and the first implementation slice are first-party contributions under the same project ownership. No private Git history is imported.

The initial implementation was reconstructed from reviewed architectural concepts and sanitized for a deployment-neutral contract. Live environment files, ciphertext, identities, topology, and private composition are not public fixtures.

## Third-party material

The repository does not vendor third-party implementation source in the initial slice.

External tools, Actions, Python packages, container images, and upstream K3s release artifacts are referenced as dependencies and retain their own licenses. GitHub Actions are bound by immutable commit SHA; public tool versions are pinned; the example container is bound by digest.

## License decision

No ownership or compatibility blocker was found for licensing the public implementation under Apache License 2.0. This decision applies only to Hyperion Community. It does not relicense or change the visibility of privately operated source.

Future copied or vendored material must record origin, applicable license, and required notices before merge.
