# Static site publication contract

The Hyperion Community landing page is the static content under this directory.

## Supported source contract

- `web/index.html` is the canonical public landing-page artifact.
- The repository does not require a server-side runtime, Cloudflare Workers,
  Node compatibility, or provider-specific observability to render the site.
- The page is intentionally usable as plain static HTML/CSS.
- Repository CI validates source and publication boundaries; it does not deploy
  the site and must not require an external preview service to be available.
- External hosting may serve the contents of `web/`, but hosting credentials,
  provider project identifiers, deployment hooks, and preview state are not
  part of the public verification contract.

Cloudflare Workers is therefore not a supported runtime assumption for the
current site. The superseded autoconfiguration that proposed
`nodejs_compat` and Workers observability should not be revived unless the
site gains a reviewed runtime requirement that cannot be satisfied by static
hosting.

## Privacy and observability

The current landing page has no JavaScript runtime and no repository-defined
analytics or telemetry integration. Do not add provider observability or client
telemetry merely to satisfy a hosting integration. Any future telemetry must be
an explicit, separately reviewed product/privacy decision.

## Local preview

A local preview needs only a static HTTP server, for example:

```bash
python -m http.server 8000 -d web
```

The repository's authoritative verification remains:

```bash
mise run lint
mise run ci
```

## External hosting

The repository homepage may point to a hosted copy of this directory, but that
host is a distribution endpoint, not a source-of-truth or CI dependency.

If an external Git/preview integration fails while repository CI is green,
repair or disable that integration outside the source-validation path. Do not
add a Workers runtime, compatibility flags, credentials, or telemetry solely
to make an optional preview provider green.
