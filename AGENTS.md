# SagaSmithAI Organization Documentation Guide

## Scope

This repository owns the organization profile, contribution contract, release
policy, and shared GitHub metadata. It describes the current public topology; it
must not invent runtime behavior or duplicate component-level contracts.

## Current topology

- `sagasmith-core` is the neutral runtime.
- `sagasmith-dnd`, `sagasmith-coc`, and `sagasmith-narrative` are vertical
  repositories that own their Domain package, MCP, Skills, and UI where present.
- `SagaSmith-agent` is the host; `SagaSmith-service` is the hosted control plane.
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
- Keep authority boundaries explicit: Agent decides semantics; domain mechanics
  resolve deterministic rules; MCP owns authoritative runtime state; Core owns
  neutral primitives; Service owns hosted control-plane concerns.
- Update the website developer map whenever the organization profile topology
  changes.
