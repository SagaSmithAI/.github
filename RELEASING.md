# Release governance

SagaSmithAI repositories version and release independently. A platform milestone is a tested compatibility set, not one monolithic version.

## Version policy

- Python packages and MCP servers use Semantic Versioning.
- `0.x` minor releases may change public contracts, but the change must be documented and coordinated with direct consumers.
- UIs and Skills use dated or semantic tags once they have a distributable artifact; before that, the default branch is the only supported channel.
- System plugins declare compatible `sagasmith-core` ranges. Domain MCPs declare compatible Core and system-runtime ranges.

## Required release evidence

1. The repository CI passes on the intended tag commit.
2. Public schemas, tool lists, configuration examples, and README status are current.
3. Cross-repository consumers pass a vertical integration test against the exact dependency versions.
4. Database/schema changes include upgrade validation. No legacy migration is required unless the release notes explicitly promise it.
5. Security, visibility, actor-knowledge, branch, idempotency, and GM-judgment boundaries are regression-tested when affected.
6. A changelog entry states breaking changes, upgrade steps, known limitations, and the compatibility set.
7. The release contains no secrets, local state, imported commercial books, or campaign data.
8. A Content Library publication records each Pack checksum and rights metadata; repository visibility alone is never treated as redistribution approval.
9. A hosted Service compatibility set pins exact Agent, Core, system, MCP, and Skills revisions and proves a real Lobby -> Play -> Combat -> Play or system-equivalent path.

## Tagging

Create signed or GitHub-verified tags from the protected default branch. Publish immutable package or GitHub Pages artifacts from CI, then create a GitHub Release that links the exact tests and dependency compatibility. Do not silently replace an existing tag or artifact. Public visibility does not replace the license declared by each repository or content artifact.
