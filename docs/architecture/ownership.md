# Reusable-code ownership

Deployment-neutral reusable components become public-owned only after their publication boundary, provenance, compatibility, and independent validation are established here.

The intended dependency direction is one-way:

```text
versioned public component
        |
        v
pinned private consumer
        |
        v
private environment composition
```

The private operational source continues to own environment values, inventories, overlays, secrets, runtime topology, deployment policy, and private integrations.

## Migration rule

A reusable component moves to public ownership only when:

- the public implementation has passed publication/security review;
- license/provenance is clear;
- public validation is independently runnable;
- an immutable public revision or release exists;
- private consumption can migrate with compatibility and rollback evidence.

Until then, the current private implementation remains the operational source of truth. A public analogue must not be represented as the production implementation.

After migration, private composition should consume an immutable public release/revision rather than copying the public source back into a second maintained implementation.

## No mirror

There is no automated private-to-public source mirror. Public CI has no authority to read or mutate private deployment state.
