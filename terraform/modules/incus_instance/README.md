# Incus instance module

A deployment-neutral Incus instance abstraction reconstructed for Hyperion Community.

The module intentionally does not encode a remote endpoint, project topology, network, storage pool, credentials, cloud-init payload, live hostname, or deployment secret. Consumers provide those concerns through their own provider configuration and inputs.

The example is validation-oriented. Running `tofu apply` requires a consumer-controlled Incus endpoint and may create infrastructure.

## Provenance

The interface is a clean public reconstruction of the generic Incus-instance concept used by private Hyperion. No private Git history or environment configuration is imported. Compatibility with private consumers is not implied until migration issue #11 records an explicit pinned cutover.
