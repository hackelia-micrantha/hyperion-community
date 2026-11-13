# Incus instance module

A deployment-neutral Incus instance abstraction reconstructed for Hyperion Community.

The module intentionally does not encode a remote endpoint, project topology, network, storage pool, credentials, cloud-init payload, live hostname, or deployment secret. Consumers provide those concerns through their own provider configuration and inputs.

The `examples/incus-instance` consumer is validation-oriented. From the repository root, `mise run terraform-validate` initializes this example with `-backend=false -lockfile=readonly` and runs `tofu validate` against the actual `lxc/incus` provider schema. The example checks in its public provider lockfile (currently resolving `lxc/incus` 1.2.0 with verified checksums). `mise run tflint` also checks the example. This path requires only the public provider registry; no private repositories, credentials, Incus endpoint, state, plan, or apply.

This is schema/compatibility evidence, **not** an Incus instance lifecycle test or proof of deployment compatibility. Running `tofu apply` separately requires a consumer-controlled Incus endpoint and may create infrastructure.

## Provenance

The interface is a clean public reconstruction of the generic Incus-instance concept used by private Hyperion. No private Git history or environment configuration is imported. Compatibility with private consumers is not implied until migration issue #11 records an explicit pinned cutover.
