# SagaSmithAI Organization Documentation Guide

## Scope

This repository owns the organization profile, contribution contract, release
policy, and shared GitHub metadata. It describes the current public topology; it
must not invent runtime behavior or duplicate component-level contracts.

## Current topology

- `sagasmith-core` is the neutral runtime.
- `sagasmith-dnd`, `sagasmith-coc`, and `sagasmith-narrative` are vertical
  repositories that own their Domain package, MCP, Skills, and UI where present.
- `SagaSmith-agent` is the generic Agent host and MCP consumer.
- **SagaSmith Web** is the hosted browser product in the repository currently named
  `SagaSmith-service`; its control plane is one backend responsibility alongside the frontend,
  API/BFF, collaboration, Forge, Module Studio, Agent orchestration, and operations.
- `SagaSmith-dnd-content-library` is a rights-aware Pack catalog.
- `SagaSmithAI.github.io` is the public website.

Former standalone MCP, Skills, UI, and generic Module Generator repositories are
archived read-only. Do not list them as current entry points, build inputs, or
compatibility paths. Historical news may keep accurate historical names.

## Documentation rules

- Keep Chinese and English claims aligned where both are present.
- Link current component docs into the relevant vertical monorepo path.
- Distinguish repository visibility, software license, and per-Pack/content
  rights.
- Keep authority boundaries explicit: Agent owns model orchestration and conversational judgment;
  domain MCP contracts own tool semantics and all authoritative rule/state writes; domain runtimes
  resolve deterministic mechanics; Core owns neutral primitives; SagaSmith Web owns hosted product
  and control-plane concerns.
- Keep the Local Agent Kit independent of SagaSmith Web. Local stdio/local HTTP and hosted network
  transports must expose the same authoritative MCP schemas, errors, revisions, and idempotency.
- Update the website developer map whenever the organization profile topology
  changes.
