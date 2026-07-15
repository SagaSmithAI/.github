# Contributing to SagaSmithAI

SagaSmithAI is a multi-repository AI-native TTRPG platform. Start by choosing the layer that owns the behavior:

- Agent identity, sessions, channels, and MCP client behavior belong in `SagaSmith-agent`.
- System-neutral persistence, branches, memory, actor knowledge, imports, and retrieval belong in `sagasmith-core`.
- Rules and pure settlement logic belong in the relevant system runtime.
- Agent-facing domain operations and storage ownership belong in the relevant MCP server.
- Procedural GM guidance belongs in a Skills repository; Skills must not impersonate executable rules.
- Player and GM presentation belongs in a UI repository; UI writes must go through the domain service boundary.

## Before opening a change

1. Open or link an issue when the change crosses repositories or alters a public contract.
2. State the authority boundary: what is deterministic engine behavior, what requires GM judgment, and what is display-only.
3. Preserve principal, campaign, branch, actor, and visibility scopes in every read and write path.
4. Add tests at the narrowest owner and at least one integration test when a contract crosses repositories.
5. Update adjacent README, Skills, configuration examples, and UI contracts whenever behavior changes.

## Validation

Python repositories use `pytest` and `ruff check .`. Astro repositories use `npm run build`. Skills repositories validate `SKILL.md`, structured data, and included Python sources through their CI workflow.

Commits must be focused and must not include AI attribution, `Co-Authored-By`, `Signed-off-by`, or other trailers unless the repository owner explicitly requests them. Do not commit local configuration, API keys, imported commercial books, campaign databases, or generated runtime state.

## Content rights

Only contribute content you have the right to redistribute. Commercial TTRPG rules and adventures must not be copied into the repositories. Import tooling should retain provenance without publishing the source text.
