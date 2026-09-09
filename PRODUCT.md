---
title: Task bounties Data Product Charter
status: local-source-pilot
created: 2026-08-08
updated: 2026-09-07
tags: [template, data-engineering, data-product, governance]
description: Outcome, consumers, ownership, contract, quality, privacy, and operating boundary for a data product.
---

# Data Product Charter

## Document control

| Field | Value |
|---|---|
| Data product ID/version | book-bounty-data / bounty.v1 |
| Product owner | bookchaowalit |
| Data owner/steward | bookchaowalit |
| Producer team | Domain repository |
| Status/review date | Local source pilot / 2026-09-07 |
| Evidence boundary | schema.json, demo.json and tests in this repository |

## Product contract

- Decision or user outcome: Find scoped paid tasks with clear acceptance and authorization.
- Consumers and use cases: Discovery applications; integration planned.
- Source systems and lake layers: One reviewed GitHub rules source → landing → Bronze through the shared local runtime.
- In scope/out of scope: Payment for accepted deliverables; ranked contests and ordinary employment stay separate.
- Freshness, availability, and volume expectation: Target source review every 24h; open filter rejects checks older than 72h; no live SLA.
- Data classification, residency, retention, and access: Public program metadata; no user profile; raw source bytes remain in the private local operational archive.
- Quality thresholds and incident route: Contract, live capture, replay and parser tests pass for the enabled source; owner handles source failures.
- Cost/capacity guardrail: Manual local capture only; six-hour source cooldown and max 10,000 records per envelope.
- Versioning, deprecation, and migration policy: Draft v1; breaking changes version separately; no legacy migration or live consumer yet.

## Acceptance and ownership

| Gate | Evidence | Owner | Result/status |
|---|---|---|---|
| Contract | Versioned schema and compatibility rules |  |  |
| Quality | Checks and threshold report |  |  |
| Lineage | Source-to-consumer map |  |  |
| Access/privacy | Classification and access review |  |  |
| Operations | Runbook, alert, replay, and recovery |  |  |

## Approval

| Role | Name/date | Decision |
|---|---|---|
| Product/data owner |  | Approve charter / revise |
| Producer owner |  | Accept delivery boundary |
| Consumer representative |  | Accept use and SLA |
