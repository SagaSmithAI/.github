# Organization issue audit — 2026-09-22

全部开放 issue 已检查：20 个仓库纳入清点，41 项逐条审查，关闭 5 项已完成事项，保留 36 项有效缺口或后续范围；修正 17 项描述，41 项均已写回证据。检查完成不代表剩余功能已经实现。

Every issue open at the beginning of this pass has an individual finding, source reference, disposition and next step. A fresh GitHub inventory confirms exactly 36 remain open. All five closures were re-read and have `state_reason=completed`. No issue was closed simply because the product became local-first or a synthetic fixture passed.

## Scope and repository coverage

The inventory covers 20 repositories: nine active public product/documentation repositories, ten archived public repositories, and one private workspace whose issue tracker is disabled. No private advisory details are included here. Archived repositories remain historical; this audit does not reactivate them.

| Repository | Initial open | Final open | Audited main / status |
| --- | ---: | ---: | --- |
| [SagaSmith-agent](https://github.com/SagaSmithAI/SagaSmith-agent) | 1 | 1 | [b574183](https://github.com/SagaSmithAI/SagaSmith-agent/tree/b5741839a448974d2863955ec24421d53ca25ee2) |
| [Sagasmith-dnd](https://github.com/SagaSmithAI/Sagasmith-dnd) | 34 | 34 | [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57) |
| [SagaSmith-dnd-content-library](https://github.com/SagaSmithAI/SagaSmith-dnd-content-library) | 1 | 1 | [672a0f9](https://github.com/SagaSmithAI/SagaSmith-dnd-content-library/tree/672a0f91892d8ae3f80bc170031d43f379ee6494) |
| [Sagasmith-core](https://github.com/SagaSmithAI/Sagasmith-core) | 0 | 0 | [aec5d4d](https://github.com/SagaSmithAI/Sagasmith-core/tree/aec5d4d5b3bbeb3774b231dc376d37298a7c6bb7) |
| [SagaSmith-Web](https://github.com/SagaSmithAI/SagaSmith-Web) | 0 | 0 | [7555790](https://github.com/SagaSmithAI/SagaSmith-Web/tree/7555790df8e709bbd955ca4fde991c4156d3155b) |
| [sagasmith-narrative](https://github.com/SagaSmithAI/sagasmith-narrative) | 1 | 0 | [175fd97](https://github.com/SagaSmithAI/sagasmith-narrative/tree/175fd977a2eab76a1a0d64781e32ca866ba37c0c) |
| [SagaSmithAI.github.io](https://github.com/SagaSmithAI/SagaSmithAI.github.io) | 0 | 0 | [bb309c8](https://github.com/SagaSmithAI/SagaSmithAI.github.io/tree/bb309c810bace3ba1dd7682242ca36fc88cf86f1) |
| [Sagasmith-coc](https://github.com/SagaSmithAI/Sagasmith-coc) | 2 | 0 | [967e99d](https://github.com/SagaSmithAI/Sagasmith-coc/tree/967e99da28f9d2ee1cf712098f6156791259db0b) |
| [.github](https://github.com/SagaSmithAI/.github) | 2 | 0 | [2d1d0e1](https://github.com/SagaSmithAI/.github/tree/2d1d0e11bb9284167359f5a07d4b6443d5c1f2e5) |
| [SagaSmith-coc-mcp](https://github.com/SagaSmithAI/SagaSmith-coc-mcp) | 0 | 0 | Archived; zero open issues |
| [SagaSmith-coc-skills](https://github.com/SagaSmithAI/SagaSmith-coc-skills) | 0 | 0 | Archived; zero open issues |
| [sagasmith-coc-ui](https://github.com/SagaSmithAI/sagasmith-coc-ui) | 0 | 0 | Archived; zero open issues |
| [SagaSmith-dnd-mcp](https://github.com/SagaSmithAI/SagaSmith-dnd-mcp) | 0 | 0 | Archived; zero open issues |
| [SagaSmith-dnd-skills](https://github.com/SagaSmithAI/SagaSmith-dnd-skills) | 0 | 0 | Archived; zero open issues |
| [sagasmith-dnd-ui](https://github.com/SagaSmithAI/sagasmith-dnd-ui) | 0 | 0 | Archived; zero open issues |
| [SagaSmith-module-gen-skills](https://github.com/SagaSmithAI/SagaSmith-module-gen-skills) | 0 | 0 | Archived; zero open issues |
| [SagaSmith-narrative-mcp](https://github.com/SagaSmithAI/SagaSmith-narrative-mcp) | 0 | 0 | Archived; zero open issues |
| [SagaSmith-narrative-skills](https://github.com/SagaSmithAI/SagaSmith-narrative-skills) | 0 | 0 | Archived; zero open issues |
| [sagasmith-ui](https://github.com/SagaSmithAI/sagasmith-ui) | 0 | 0 | Archived; zero open issues |

The earlier [D&D local-first audit](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/main/docs/audits/2026-09-22-local-first-issues.md) started with 45 D&D issues and closed 11. Those already-closed issues are outside this pass's 41-open-issue snapshot. Historical closures are not silently counted again.

## Audit method and evidence limits

Issue bodies were compared with current-main implementations, bundled rule sources, existing acceptance tests and GitHub configuration. Each retained issue below identifies the remaining behavior rather than treating a matching name, catalog entry or source card as an executor. Absence findings are source-inspection conclusions; focused reproductions and executed tests are identified separately.

Local-first continues to mean Host-managed protocol metadata over an authoritative Runtime/Core boundary. Principal, branch, revision, transaction, idempotency, source provenance, random-stream rollback and unresolved player choices remain enforced. Moving protocol work into Host does not make unfinished gameplay rules obsolete.

Today's focused validation passed nine selected cases: one Narrative public-facade case, three CoC cases and five D&D domain/public-MCP cases. These runs used the existing D&D Python environment with the audited repositories on PYTHONPATH. They do not certify every rule, private Pack or a complete real-LLM campaign.

## Closed as completed

### [sagasmith-narrative #17: Make actor_change input type explicit and output-compatible](https://github.com/SagaSmithAI/sagasmith-narrative/issues/17)

Current main normalizes type/character_type for create/update, rejects conflicts before writes, exposes fields in tools/list and permits NPC conversation. Public-facade regression passed today.

Evidence: [packages/mcp/tests/test_tool_contract_quality.py::test_public_actor_change_type_alias_conflict_and_npc_eligibility](https://github.com/SagaSmithAI/sagasmith-narrative/blob/175fd977a2eab76a1a0d64781e32ca866ba37c0c/packages/mcp/tests/test_tool_contract_quality.py). [Audit comment](https://github.com/SagaSmithAI/sagasmith-narrative/issues/17#issuecomment-5772801391). Closure and `completed` reason were verified through the GitHub API.

### [Sagasmith-coc #26: Reject unindexable generated module starts before persistence](https://github.com/SagaSmithAI/Sagasmith-coc/issues/26)

Unknown fields and unheaded generated text are rejected before staging/job creation; valid headed text yields indexed evidence. Regression passed today.

Evidence: [packages/mcp/tests/test_vertical_slice.py::test_generated_module_start_validates_before_persistence_and_indexes_headings](https://github.com/SagaSmithAI/Sagasmith-coc/blob/967e99da28f9d2ee1cf712098f6156791259db0b/packages/mcp/tests/test_vertical_slice.py). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-coc/issues/26#issuecomment-5772801836). Closure and `completed` reason were verified through the GitHub API.

### [Sagasmith-coc #39: Legacy runtime derivation rejects dotted current Pack IDs](https://github.com/SagaSmithAI/Sagasmith-coc/issues/39)

Current main normalizes dotted IDs and keeps lineage root identical. Both current ID-shape regressions pass today; merged PR #40 records actual two-Pack/four-ending stdio/replay/restart acceptance.

Evidence: [packages/mcp/tests/test_emergent_memory_runtime.py::test_legacy_current_private_pack_ids_derive_stable_runtime_keys](https://github.com/SagaSmithAI/Sagasmith-coc/blob/967e99da28f9d2ee1cf712098f6156791259db0b/packages/mcp/tests/test_emergent_memory_runtime.py); `PR #40`. [Audit comment](https://github.com/SagaSmithAI/Sagasmith-coc/issues/39#issuecomment-5772802449). Closure and `completed` reason were verified through the GitHub API.

### [.github #8: Enable a working private vulnerability and repository security baseline](https://github.com/SagaSmithAI/.github/issues/8)

All nine active product/docs repositories now report private vulnerability reporting, secret scanning, push protection and Dependabot security updates enabled; alerts endpoints return 204. Organization and Agent security policies have current ownership/reporting guidance.

Evidence: `GitHub API verified 2026-09-22`; `SECURITY.md`; `SagaSmith-agent/SECURITY.md`. [Audit comment](https://github.com/SagaSmithAI/.github/issues/8#issuecomment-5772802978). Closure and `completed` reason were verified through the GitHub API.

### [.github #6: Upgrade active GitHub Actions off the deprecated Node 20 runtime](https://github.com/SagaSmithAI/.github/issues/6)

All workflow action references and the two nested composite action pins resolve to node24 or node24 composites. Previous post-merge acceptance is recorded on this issue; fresh profile-sync and Pages log checks contain no Node-20 warning.

Evidence: `All nine .github/workflows directories`; `upstream action.yml`; `issue completion comment`. [Audit comment](https://github.com/SagaSmithAI/.github/issues/6#issuecomment-5772803399). Closure and `completed` reason were verified through the GitHub API.

## Retained issues and execution order

Priorities are audit planning ranks, not vulnerability severity or promises of completion: P0 addresses authoritative settlement correctness; P1 expands essential rule coverage or tracks security exposure; P2 covers further gameplay/publishing; P3 is a broader product roadmap. Work should follow dependencies rather than treating the ranks as independent batches.

### P0 — 8 issues

#### [Sagasmith-dnd #158: Fix 2014 scene-object attack and damage-threshold settlement](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/158)

**Finding (confirmed gap):** Object input still excludes damage_threshold, takes immunities from request data and validates a source citation without binding the supplied numerical object model.

**Next acceptance step:** Derive object statistics from a validated source model and apply damage thresholds atomically.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/runtime/src/sagasmith_dnd_runtime/services/attacks.py:2390](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/runtime/src/sagasmith_dnd_runtime/services/attacks.py#L2390). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/158#issuecomment-5772789344).

#### [Sagasmith-dnd #139: Execute the predeclared 2014 readied spell on release](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/139)

**Finding (confirmed gap):** Release still accepts a new declaration, changes the holding effect/reaction and returns ready_release_effect pending_ruling instead of executing the stored spell.

**Next acceptance step:** Persist the readied spell response and execute that exact response on release with atomic resource timing.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/runtime/src/sagasmith_dnd_runtime/services/spells.py:2950](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/runtime/src/sagasmith_dnd_runtime/services/spells.py#L2950). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/139#issuecomment-5772793071).

#### [Sagasmith-dnd #133: Bind Ready release to and execute the predeclared response](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/133)

**Finding (confirmed gap):** Release still logs/returns caller declaration and spends reaction without executing the original stored action response.

**Next acceptance step:** Persist and execute the original Ready response; reject caller replacement declarations.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/runtime/src/sagasmith_dnd_runtime/services/combat.py:4340](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/runtime/src/sagasmith_dnd_runtime/services/combat.py#L4340). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/133#issuecomment-5772793568).

#### [Sagasmith-dnd #127: Close the unbound legacy-input gap in 2014 Help](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/127)

**Finding (partial):** Structured attack target binding and task Help consumption now exist and pass tests. A NEW empty Help payload still creates unbound legacy Help; reproduced in the audit probes.

**Next acceptance step:** Reject newly submitted untyped Help or require explicit target/task binding; isolate persisted legacy migration from new declarations.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/combat_engine.py:9216](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/combat_engine.py#L9216); [packages/runtime/src/sagasmith_dnd_runtime/services/combat.py:6773](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/runtime/src/sagasmith_dnd_runtime/services/combat.py#L6773). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/127#issuecomment-5772795155).

#### [Sagasmith-dnd #116: Enforce 2014 spell components before casting](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/116)

**Finding (confirmed gap):** consume_spell_cast still emits ordinary V/S/M as ruling_required after settlement; authoritative speech/free-hand/focus eligibility is not a complete pre-spend gate.

**Next acceptance step:** Resolve ordinary V/S/M eligibility before slots, actions, RNG or state mutate.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/spells.py:1187](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/spells.py#L1187); [packages/domain/src/sagasmith_dnd/spells.py:1367](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/spells.py#L1367). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/116#issuecomment-5772795601).

#### [Sagasmith-dnd #110: Bind opportunity-attack triggers to weapon reach](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/110)

**Finding (partial):** Weapon IDs/reach are recorded, but max(reach) selects the outermost crossed boundary. Probe: whole path first offers long; split path first offers short/unarmed. Full path equivalence is not fixed.

**Next acceptance step:** Produce ordered per-weapon reach crossings and prove full-route/segmented-route equivalence.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/combat_engine.py:5851](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/combat_engine.py#L5851). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/110#issuecomment-5772797178).

#### [Sagasmith-dnd #109: Model off-turn self-powered movement for opportunity attacks](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/109)

**Finding (confirmed gap):** Voluntary/aggressive movement remains current-turn-only; forced/teleport movement bypasses opportunity attacks. Off-turn self-powered action/reaction movement has no independent payment contract.

**Next acceptance step:** Model self-powered off-turn movement with its own action/reaction payment and opportunity-attack eligibility.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/combat_engine.py:5460](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/combat_engine.py#L5460). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/109#issuecomment-5772797643).

#### [Sagasmith-dnd #107: Pause movement before resolving opportunity attacks](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/107)

**Finding (confirmed gap):** Movement assigns the final destination before adding reaction windows. Probe records x=3 while its unresolved reaction boundary is x=2; no resumable movement continuation exists.

**Next acceptance step:** Pause at the first reaction boundary and persist a resumable movement continuation.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/combat_engine.py:5801](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/combat_engine.py#L5801). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/107#issuecomment-5772798137).

### P1 — 16 issues

#### [Sagasmith-dnd #173: Verify exact-source Battle Smith grants and subclass-order parity](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/173)

**Finding (partial):** Battle Smith has executable Eberron grants and Steel Defender flows; exact Tasha-source acceptance and complete ordering/rebuild evidence remain unverified.

**Next acceptance step:** Run both subclass-selection/leveling orders with the exact Tasha Pack and compare complete cards, Defender lifecycle, replay and restart receipts.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/steel_defender.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/steel_defender.py); [packages/mcp/tests/test_artificer_play_official_archive_mcp.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/mcp/tests/test_artificer_play_official_archive_mcp.py). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/173#issuecomment-5772785100).

#### [Sagasmith-dnd #168: Enforce 2014 Sunlight Sensitivity on attacks and sight checks](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/168)

**Finding (missing):** Sunlight Sensitivity is descriptive content and synthetic test input; no production trait consumer derives attack/sight-check disadvantage from scene sunlight.

**Next acceptance step:** Bind direct-sunlight and sight-use facts to attacks and Perception before RNG; cover cancellation and fact expiry.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/standard_content.py:409](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/standard_content.py#L409); [packages/domain/tests/test_combat_engine.py:6321](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/tests/test_combat_engine.py#L6321). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/168#issuecomment-5772785855).

#### [Sagasmith-dnd #164: Implement generic source-correct 2014 passive checks](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/164)

**Finding (partial):** Derived passive Perception and chase/hide consumers exist; a generic ability/skill passive resolver with net +/-5, secret output and a shared modifier path does not.

**Next acceptance step:** Introduce a shared passive-check resolver and reconcile existing Perception/chase consumers without secret leakage.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/character_schema.py:5376](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/character_schema.py#L5376); [packages/domain/src/sagasmith_dnd/chase_engine.py:79](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/chase_engine.py#L79). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/164#issuecomment-5772786683).

#### [Sagasmith-dnd #152: Implement source-correct 2014 vision, obscuration, and light settlement](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/152)

**Finding (partial):** can_see handles blinded/hidden/invisible and explicit visibility lists; it does not derive illumination, obscuration, darkvision/blindsight/truesight range.

**Next acceptance step:** Derive visibility from authoritative light, obscuration and sense ranges before attack/check settlement.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/combat_engine.py:9398](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/combat_engine.py#L9398). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/152#issuecomment-5772790162).

#### [Sagasmith-dnd #151: Implement 2014 food, water, and starvation exhaustion lifecycle](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/151)

**Finding (partial):** Long rests use food_and_drink for exhaustion recovery; daily ration/water debt, hot-weather intake, source-owned deprivation and day-boundary saves are absent.

**Next acceptance step:** Track daily food/water intake and debt and settle deprivation at authoritative time boundaries.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/lifecycle.py:1113](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/lifecycle.py#L1113); [packages/domain/src/sagasmith_dnd/edition_strategies.py:9](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/edition_strategies.py#L9). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/151#issuecomment-5772790680).

#### [Sagasmith-dnd #149: Enforce 2014 occupied-space and squeezing movement rules](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/149)

**Finding (partial):** Willingly occupied destinations already fail; hostile traversal by size, occupied-path terrain cost and squeezing state/attack/save modifiers remain absent.

**Next acceptance step:** Extend path occupancy and squeezing settlement while retaining the already-working occupied-endpoint rejection.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/combat_engine.py:5674](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/combat_engine.py#L5674). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/149#issuecomment-5772791675).

#### [Sagasmith-dnd #148: Implement source-correct 2014 underwater combat settlement](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/148)

**Finding (missing):** Swim movement speed exists; submerged attack exceptions, beyond-normal-range automatic miss and fully immersed fire resistance are not integrated.

**Next acceptance step:** Integrate underwater weapon/range exceptions and immersion-based fire resistance into attack/damage settlement.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/combat_engine.py:5655](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/combat_engine.py#L5655); [packages/domain/src/sagasmith_dnd/lifecycle.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/lifecycle.py). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/148#issuecomment-5772792150).

#### [Sagasmith-dnd #129: Implement source-correct 2014 multiclass advancement](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/129)

**Finding (missing):** advance_single_class_level still enforces one existing class and equal total/class level; adding a second class and combined spell-slot settlement is not supported.

**Next acceptance step:** Support a second class with source prerequisites, combined slots and choice/rebuild parity.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/progression.py:830](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/progression.py#L830). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/129#issuecomment-5772794146).

#### [Sagasmith-dnd #128: Implement remaining high-level 2014 Rogue mechanics](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/128)

**Finding (missing):** No source-bound settlement was found for Reliable Talent, Blindsense, Slippery Mind, Elusive or Stroke of Luck; resource/display text cannot satisfy those mechanics.

**Next acceptance step:** Implement the five named high-level Rogue mechanics with source-owned choices and resources.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/core_content.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/core_content.py); [packages/domain/src/sagasmith_dnd/combat_engine.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/combat_engine.py). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/128#issuecomment-5772794640).

#### [Sagasmith-dnd #113: Implement 2014 Paladin Divine Smite settlement](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/113)

**Finding (missing):** Paladin source content exists but there is no source-bound post-hit Divine Smite choice, slot spend and radiant damage settlement.

**Next acceptance step:** Add the optional post-hit, pre-damage Divine Smite choice and atomic slot/damage settlement.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/core_content.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/core_content.py); [packages/domain/src/sagasmith_dnd/combat_engine.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/combat_engine.py). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/113#issuecomment-5772796001).

#### [Sagasmith-dnd #112: Implement actual 2014 Bardic Inspiration settlement](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/112)

**Finding (partial):** Bard use pools and die scaling exist; grant/range/hearing, ten-minute recipient state and post-d20/pre-outcome spend windows are absent.

**Next acceptance step:** Persist the recipient benefit and enforce granting eligibility, duration and post-d20 spending.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/core_content.py:1356](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/core_content.py#L1356). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/112#issuecomment-5772796457).

#### [Sagasmith-dnd #111: Implement actual 2014 Barbarian Rage settlement](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/111)

**Finding (incorrect requirement):** Rage still needs an executor. Correct the issue: heavy armor gates the listed benefits, not activation itself; honor the 15th-level Persistent Rage exception to early ending.

**Next acceptance step:** Implement Rage from the corrected source requirements, including benefit gating and Persistent Rage.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/core_content.py:1342](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/core_content.py#L1342); [skills/full/skills/dnd-dm/srd/references-2014-en/02_Classes/Barbarian.md](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/skills/full/skills/dnd-dm/srd/references-2014-en/02_Classes/Barbarian.md). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/111#issuecomment-5772796812).

#### [Sagasmith-dnd #106: Execute all selected 2014 Fighting Styles](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/106)

**Finding (partial):** Dueling and Two-Weapon Fighting integration exist; remaining Archery, Defense, Great Weapon Fighting and Protection effects are not fully implemented. The old claim that all but Dueling do nothing is stale.

**Next acceptance step:** Implement Archery, Defense, Great Weapon Fighting and Protection; retain Dueling and Two-Weapon Fighting regression coverage.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/combat_engine.py:2272](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/combat_engine.py#L2272); [packages/domain/src/sagasmith_dnd/combat_engine.py:3381](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/combat_engine.py#L3381). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/106#issuecomment-5772798664).

#### [Sagasmith-dnd #104: Implement 2014 Legendary Resistance settlement](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/104)

**Finding (missing):** Legendary Resistance text survives import, but no reviewed use resource and failed-save choice window integrated across save paths was found.

**Next acceptance step:** Create a failed-save Legendary Resistance choice bound to a reviewed resource pool across save paths.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/statblocks.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/statblocks.py); [packages/domain/src/sagasmith_dnd/combat_engine.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/combat_engine.py). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/104#issuecomment-5772799056).

#### [Sagasmith-dnd #97: Implement 2014 grapple and shove attack replacements](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/97)

**Finding (missing):** Grappled/Restrained conditions and generic escape exist; source-owned 2014 grapple/shove attack replacements, contests, release and dragging transitions do not.

**Next acceptance step:** Add 2014 grapple/shove attack replacements, source-owned conditions, escape/release and dragging.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/combat_engine.py:2001](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/combat_engine.py#L2001); [packages/domain/src/sagasmith_dnd/combat_engine.py:6327](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/combat_engine.py#L6327). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/97#issuecomment-5772799465).

#### [Sagasmith-dnd #51: Track unfixed ChromaDB authorization and code-injection advisories](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/51)

**Finding (upstream blocked):** All three GitHub advisories still return first_patched_version=null and affected ranges through 1.5.9. Default text-only local installs do not establish that optional Chroma server deployments are fixed.

**Next acceptance step:** Keep optional server exposure documented; only upgrade/close after patched versions or an effective verified mitigation cover all three advisories.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): `uv.lock`; `SECURITY.md`. [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/51#issuecomment-5772799851).

### P2 — 11 issues

#### [Sagasmith-dnd #169: Implement source-correct 2014 adventuring gear settlement](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/169)

**Finding (missing):** Generic consumables and selected official item effects exist; there is no complete source-bound mundane gear action catalog covering the listed items.

**Next acceptance step:** Implement a reviewed item-by-item action matrix; retain source-bound quantities, timing and unresolved environmental choices.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/consumables.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/consumables.py); [packages/domain/src/sagasmith_dnd/native_content/equipment.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/native_content/equipment.py). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/169#issuecomment-5772785466).

#### [Sagasmith-dnd #165: Implement source-correct 2014 working-together checks](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/165)

**Finding (missing):** Group checks and combat Help are separate existing features; no noncombat helper/leader/task eligibility and productive-collaboration transaction exists.

**Next acceptance step:** Add one helper/leader/task transaction with source eligibility and productive-collaboration facts.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/combat_engine.py:9302](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/combat_engine.py#L9302); [packages/runtime/src/sagasmith_dnd_runtime/services/combat.py:6773](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/runtime/src/sagasmith_dnd_runtime/services/combat.py#L6773). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/165#issuecomment-5772786290).

#### [Sagasmith-dnd #163: Implement 2014 lifestyle and downtime activity settlement](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/163)

**Finding (missing):** Campaign time exists; source-bound 8-hour activity days, crafting costs/proficiency, profession, recuperation, research and training settlement are absent.

**Next acceptance step:** Implement activity-day accounting and each source-defined cost/proficiency/result transition.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/game_time.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/game_time.py); [packages/runtime/src/sagasmith_dnd_runtime/services/campaigns.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/runtime/src/sagasmith_dnd_runtime/services/campaigns.py). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/163#issuecomment-5772787118).

#### [Sagasmith-dnd #162: Implement source-correct 2014 madness effects and cures](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/162)

**Finding (missing):** No short/long/indefinite madness table executor, source-owned effect lifecycle, suppression or cure procedure was found; Crown of Madness vocabulary is unrelated.

**Next acceptance step:** Implement source table rolls, durations, effect provenance, suppression and cure tiers.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/standard_spell_ids.py:50](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/standard_spell_ids.py#L50); [packages/domain/src/sagasmith_dnd/lifecycle.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/lifecycle.py). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/162#issuecomment-5772787576).

#### [Sagasmith-dnd #161: Implement source-bound 2014 trap detection, disabling, and settlement](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/161)

**Finding (missing):** Generic scene hazards/source attacks are not a persisted trap model with detection, disarm, trigger, one-shot and complex-initiative lifecycle.

**Next acceptance step:** Persist trap detection/disable/trigger/lifecycle state and integrate existing spatial, damage and initiative paths.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/runtime/src/sagasmith_dnd_runtime/services/combat.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/runtime/src/sagasmith_dnd_runtime/services/combat.py); [packages/mcp/tests/test_scene_hazard_save_mcp.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/mcp/tests/test_scene_hazard_save_mcp.py). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/161#issuecomment-5772788031).

#### [Sagasmith-dnd #160: Implement source-correct 2014 poison delivery and lifecycles](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/160)

**Finding (missing):** Typed poison damage/conditions exist, but doses/coatings, four delivery gates, named poison counters, midnight and protected-damage lifecycle do not.

**Next acceptance step:** Add source-owned doses, delivery eligibility, named poison timers/counters and cleanup.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/lifecycle.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/lifecycle.py); [packages/domain/src/sagasmith_dnd/consumables.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/consumables.py). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/160#issuecomment-5772788541).

#### [Sagasmith-dnd #159: Implement source-correct 2014 disease lifecycles](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/159)

**Finding (missing):** Generic effects/rests do not implement Cackle Fever, Sewer Plague or Sight Rot incubation, recurring saves, transmission, rest restrictions and exact cures.

**Next acceptance step:** Add source-defined disease onset, recurring saves, transmission, restrictions and cures.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/lifecycle.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/lifecycle.py); [packages/runtime/src/sagasmith_dnd_runtime/services/campaigns.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/runtime/src/sagasmith_dnd_runtime/services/campaigns.py). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/159#issuecomment-5772788932).

#### [Sagasmith-dnd #157: Implement source-correct 2014 travel pace and forced-march settlement](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/157)

**Finding (missing):** The clock advances time but has no party travel distance/pace ledger, passive-perception pace modifiers or hourly forced-march settlement.

**Next acceptance step:** Add travel distance/pace bookkeeping and hourly forced-march saves using the campaign clock.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/game_time.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/game_time.py); [packages/runtime/src/sagasmith_dnd_runtime/services/campaigns.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/runtime/src/sagasmith_dnd_runtime/services/campaigns.py). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/157#issuecomment-5772789757).

#### [Sagasmith-dnd #150: Implement source-correct 2014 long-jump and high-jump settlement](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/150)

**Finding (missing):** Movement charges path/travel/crawl costs but has no bound run-up and Strength-derived long/high jump declaration or landing-check procedure.

**Next acceptance step:** Bind jump type, run-up, distance, movement spend and landing checks to the selected source.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/combat_engine.py:5439](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/combat_engine.py#L5439). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/150#issuecomment-5772791218).

#### [Sagasmith-dnd #147: Implement source-correct 2014 mounted combat lifecycle](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/147)

**Finding (missing):** Dependent-actor support is not a rider/mount contract; mounting cost, controlled/independent turns and forced dismount saves remain absent.

**Next acceptance step:** Add rider/mount relations, turn ownership, movement costs and dismount lifecycle.

Evidence at [a8ae77e](https://github.com/SagaSmithAI/Sagasmith-dnd/tree/a8ae77e0cb49c688a4525d7c77d36919f482bf57): [packages/domain/src/sagasmith_dnd/combat_engine.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/combat_engine.py); [packages/domain/src/sagasmith_dnd/dependent_actor_relations.py](https://github.com/SagaSmithAI/Sagasmith-dnd/blob/a8ae77e0cb49c688a4525d7c77d36919f482bf57/packages/domain/src/sagasmith_dnd/dependent_actor_relations.py). [Audit comment](https://github.com/SagaSmithAI/Sagasmith-dnd/issues/147#issuecomment-5772792649).

#### [SagaSmith-dnd-content-library #10: Refresh public catalog metadata from the current source index](https://github.com/SagaSmithAI/SagaSmith-dnd-content-library/issues/10)

**Finding (confirmed gap):** Metadata-only publishing and freshness check now exist, but the live marker is 2026-09-09 while main index is 2026-09-10. The CLI freshness check fails for that exact mismatch.

**Next acceptance step:** Publish permitted metadata matching the current catalog and require the freshness check to pass.

Evidence at [672a0f9](https://github.com/SagaSmithAI/SagaSmith-dnd-content-library/tree/672a0f91892d8ae3f80bc170031d43f379ee6494): [scripts/check_catalog_freshness.py](https://github.com/SagaSmithAI/SagaSmith-dnd-content-library/blob/672a0f91892d8ae3f80bc170031d43f379ee6494/scripts/check_catalog_freshness.py); `website public/library-catalog-status.json`. [Audit comment](https://github.com/SagaSmithAI/SagaSmith-dnd-content-library/issues/10#issuecomment-5772800727).

### P3 — 1 issues

#### [SagaSmith-agent #13: Track ordered NanoBot updates after the July ancestry bridge](https://github.com/SagaSmithAI/SagaSmith-agent/issues/13)

**Finding (roadmap):** Ordered upstream integration remains a selective roadmap with unchecked batches. Local DND work does not satisfy every provider/channel/plugin/TUI requirement.

**Next acceptance step:** Continue the selective upstream batches only when compatible with current ownership, licensing and product scope.

Evidence at [b574183](https://github.com/SagaSmithAI/SagaSmith-agent/tree/b5741839a448974d2863955ec24421d53ca25ee2): `Issue body and main history`; `preserve licensing and upstream commit attribution.`. [Audit comment](https://github.com/SagaSmithAI/SagaSmith-agent/issues/13#issuecomment-5772800314).

## Corrections to issue scope

Seventeen issue bodies were updated. This preserves issue history while replacing inaccurate current-state claims and incomplete sentences.

- D&D #111 now distinguishes heavy-armor benefit gating from Rage activation and retains the level-15 Persistent Rage exception.
- D&D #106, #127, #149, #110 and #173 acknowledge existing mechanics, then identify the remaining style, legacy-input, traversal, reach-boundary or exact-source acceptance gap.
- D&D #97's escaped/corrupted text was repaired. Truncated sentences in #169, #168, #165, #164, #163, #162 and #161 were completed from their cited sources and intact requirements; unknown omitted scope was not invented. The current weapons and lifestyle source paths were corrected.
- Content #10 now names the actual 2026-09-09 versus 2026-09-10 metadata mismatch. The metadata-only surface and checker are already implemented.
- Organization #6 and #8 now distinguish historical reproduction from the verified current state and use the current SagaSmith-Web repository name.

## Reproduced remaining D&D defects

[Machine-readable probe output](2026-09-22-dnd-probes.json) records three domain-level counterexamples at D&D a8ae77e. No user campaign data was used.

| Issue | Observed result | Meaning |
| --- | --- | --- |
| #110 | A whole path first offers `long`; its first legal segment offers `short` and `unarmed-strike`. | Weapon IDs are recorded, but selecting the outermost reach still loses earlier crossings. |
| #107 | Mover position is already x=3 while the unresolved reaction boundary is x=2. | Movement does not yet pause and resume around the reaction. |
| #127 | A new empty Help payload creates `kind=legacy` without an enemy target. | New declarations can still bypass the structured Help binding. |

The selected Help/reach tests passed alongside these reproductions. Passing existing tests therefore does not justify closing the larger acceptance gaps. Reproductions use deterministic domain fixtures and do not claim public-protocol or live-campaign completion.

## Repository configuration and CI evidence

[Sanitized security settings](2026-09-22-repository-security.json) record enabled private vulnerability reporting, secret scanning, push protection and Dependabot security updates for all nine active public repositories. Vulnerability-alert endpoints returned HTTP 204. Non-provider-pattern scanning and validity checks remain disabled; they are not represented as enabled by this audit.

[Action runtime evidence](2026-09-22-action-runtimes.json) covers all referenced action versions and the nested pins used by the two composite actions. No workflow uses `ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION`. Fresh profile-sync run [35678322648](https://github.com/SagaSmithAI/.github/actions/runs/35678322648) and Pages run [34848349557](https://github.com/SagaSmithAI/SagaSmithAI.github.io/actions/runs/34848349557) succeeded and their inspected logs contained no Node-20 warning. Organization #6 also records prior post-merge acceptance of the affected workflows.

- D&D [35697690302](https://github.com/SagaSmithAI/Sagasmith-dnd/actions/runs/35697690302), code head a8ae77e: all four jobs passed, including locked Python 3.11 and compatibility Python 3.12.
- Agent [35697730031](https://github.com/SagaSmithAI/SagaSmith-agent/actions/runs/35697730031), head b574183: all eleven jobs passed.
- CoC [34848333295](https://github.com/SagaSmithAI/Sagasmith-coc/actions/runs/34848333295) and Narrative [34848359522](https://github.com/SagaSmithAI/sagasmith-narrative/actions/runs/34848359522) had successful main CI, in addition to today's focused tests.
- CoC #39's real two-Pack/four-ending stdio, replay and restart evidence is the prior record in [merged PR #40](https://github.com/SagaSmithAI/Sagasmith-coc/pull/40); private Pack acceptance was not rerun today.
- Web nightly [35661092282](https://github.com/SagaSmithAI/SagaSmith-Web/actions/runs/35661092282) failed on the older f0fe32d head because private storage was unavailable. It predates current 7555790 and is not a Node migration failure. This audit does not certify current deployed backup/recovery.

## Remaining external and scope boundaries

D&D #51 stays open: all three queried GitHub advisories still reported no first patched version (GHSA-2wm9-hf6c-p5cr, GHSA-xph7-9rjv-w5fr, GHSA-36p7-vc44-83pf). The default text-only local path reduces relevant exposure but does not fix optional Chroma server deployments.

Content #10's current checker failed against the live surface with `published='2026-09-09', main='2026-09-10'`. A metadata publication and successful live freshness check are still required. Private source archives are not part of this public audit.

Agent #13 remains a selective upstream integration roadmap. Its providers, channels, plugins and TUI batches are broader than the immediate local D&D chain; local D&D improvements do not complete those unchecked batches.

The complete structured record is [2026-09-22-all-issues.json](2026-09-22-all-issues.json). Its retained set was compared exactly with the final GitHub open-issue inventory.
