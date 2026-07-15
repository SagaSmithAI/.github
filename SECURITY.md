# Security Policy

## Reporting a vulnerability

Do not open a public issue for vulnerabilities that could expose credentials, private campaign data, GM-only content, arbitrary files, or remote execution. Use GitHub's private vulnerability reporting for the affected repository. If private reporting is unavailable, contact the organization owner through the address published on the SagaSmithAI GitHub profile and include only the minimum reproduction details needed to establish contact.

## Supported code

The current default branch of each active repository receives security fixes. Tagged releases may receive fixes when they are still used by the current platform, but there is no long-term support promise yet.

## Security boundaries

- MCP stdio servers are intended for trusted local execution. Remote HTTP/SSE adapters require explicit authentication, origin policy, and network allowlists.
- Agent-supplied principal identifiers are not trusted. Hosts must inject a principal derived from the authenticated channel, and MCP servers must enforce campaign and actor grants.
- Player-visible responses must not contain GM-only rules, scenes, hidden combatants, private actor knowledge, or another branch's state.
- Imported PDFs, rulebooks, modules, templates, and skill assets are untrusted input. Enforce allowlisted roots, size/type limits, content-addressed storage, and provenance.
- Never submit provider keys, bot tokens, local config files, campaign databases, Chroma stores, imported commercial content, or generated artifacts containing private play data.

Security fixes should include a regression test that demonstrates the prior boundary failure without publishing sensitive production data.
