# Release governance

SagaSmithAI repositories version and release independently. A platform milestone is a tested compatibility set, not one monolithic version.

## Version policy

- Python packages and MCP servers use Semantic Versioning.
- `0.x` minor releases may change public contracts, but the change must be documented and coordinated with direct consumers.
- Domain monorepo tags version the compatible Domain, MCP, Skills, UI, and generator set together.
- Domain packages declare compatible `sagasmith-core` ranges; deployers pin the exact domain repository revision.

## Required release evidence

1. The repository CI passes on the intended tag commit.
2. Public schemas, tool lists, configuration examples, and README status are current.
3. Cross-repository consumers pass a vertical integration test against the exact dependency versions.
4. Database/schema changes include upgrade validation. No legacy migration is required unless the release notes explicitly promise it.
5. Security, visibility, actor-knowledge, branch, idempotency, and GM-judgment boundaries are regression-tested when affected.
6. A changelog entry states breaking changes, upgrade steps, known limitations, and the compatibility set.
7. The release contains no secrets, local state, imported commercial books, or campaign data.
8. A Content Library publication records each Pack checksum and rights metadata; repository visibility alone is never treated as redistribution approval.
9. A SagaSmith Web compatibility set pins exact Agent, Core, and domain-monorepo revisions and proves a real Lobby -> Play -> Combat -> Play or system-equivalent path.
10. The same contract suite passes against local stdio MCP, local Streamable HTTP MCP, and hosted
    network MCP without schema, capability, error, authority, revision, or idempotency drift.
11. Hosted releases use the exact component revisions recorded by
    `SagaSmith-Web/component-versions.json`; archived standalone repositories are never release
    inputs or compatibility fallbacks.
12. MCP `2026-07-28` evidence covers sessionless `server/discover`, per-request version,
    capability and authorization metadata, deterministic authorization-scoped catalogs with
    `ttlMs`/`cacheScope`, explicit handle expiry, and header/body routing agreement. Any retained
    handshake-era path is tested separately and documented as compatibility-only.
13. Agent evaluations record both the authorized catalog candidate count and the smaller
    model-visible selection. The host selects concrete tool IDs by system, phase, role, and task,
    fails closed on unknown or empty selections, and never treats model visibility as permission.

## Tagging

Create signed or GitHub-verified tags from the protected default branch. Publish immutable package or GitHub Pages artifacts from CI, then create a GitHub Release that links the exact tests and dependency compatibility. Do not silently replace an existing tag or artifact. Public visibility does not replace the license declared by each repository or content artifact.
