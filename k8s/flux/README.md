# Flux consumption pattern

Hyperion Community keeps public GitOps consumption separate from private cluster bootstrap.

A consumer should bind this public repository to an immutable reviewed public commit:

    flux create source git hyperion-community \
      --url=https://github.com/hackelia-micrantha/hyperion-community \
      --commit=<40-character-reviewed-public-commit> \
      --interval=5m

Then reconcile the synthetic example:

    flux create kustomization hyperion-community-example \
      --source=GitRepository/hyperion-community \
      --path="./k8s/examples/local" \
      --prune=true \
      --interval=10m

The commit placeholder is deliberate. The example does not turn a mutable branch into a production trust anchor, and the repository validation path does not require cluster credentials or private Git access.
