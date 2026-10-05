# Reusable-code ownership

Deployment-neutral reusable components become public-owned only after their publication boundary, provenance, and validation are established here. Private Hyperion remains the owner of environment composition, credentials, live topology, operational policy, and private integrations.

The intended dependency direction is one-way:

```text
versioned public component -> pinned private consumer -> private environment values
```

Private deployment code must not be mirrored back into this repository. When a reusable private component is migrated, the public implementation becomes canonical and the private repository should consume an immutable public revision or release. Components that cannot safely cross the boundary remain private; public documentation may use a synthetic example instead.

This first slice does not change private Hyperion consumption. That migration requires a separate compatibility and rollback review.
