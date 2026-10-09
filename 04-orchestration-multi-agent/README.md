# 04 — Orchestration & Multi-Agent Architecture

## Concept: Orchestration

You already know **why** multiple agents exist (permissions, context, specialization).  
**Orchestration** is **who coordinates them**: a manager/router that splits work, calls specialists, merges results, and decides stop vs escalate to a human.

Common patterns:
- **Hub-and-spoke** — one orchestrator calls specialists (most common)
- **Pipeline** — A → B → C in a fixed order
- **Handoff** — agent gives up to another agent or a human

Specialists are scoped (own system prompt + tools + usually trimmed context). They don’t need to be “smarter” — just **narrower**.

### Bank / fintech sketch

```text
User: "Unlock me, dispute a charge, replace my card"
        │
        ▼
   Orchestrator (triage + merge)
        │
        ├──► Auth agent      (IAM / MFA tools only)
        ├──► Payments agent  (disputes / transactions only)
        └──► Cards agent     (card issuer tools only)
        │
        ▼
   One customer reply (or human handoff)
```

## Practice

### TODO 1 — Design (no code required)

- [ ] Pick one real product (support, bank, shop) and list 3 specialist agents + 1 orchestrator
- [ ] For each specialist: one-line job + which tools it may use (and must NOT use)
- [ ] Draw hub-and-spoke vs pipeline for that flow; pick which fits and why
- [ ] Write the rule: when to escalate to a human (e.g. fraud, refund > $X)

### TODO 2 — Tiny orchestrator loop (code later)

- [ ] Sketch (or implement) an orchestrator that: classifies intent → calls 1–2 fake specialists → merges answers
- [ ] Give each specialist a different `system` prompt and a tiny tool allow-list
- [ ] Pass specialists a **short brief**, not the full messy user history
- [ ] Add max steps / stop condition so orchestration can’t loop forever

## Docs

- [How tool use works](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works) (specialists still use tools)
- [Stop reasons](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)
- [Agent SDK overview](https://platform.claude.com/docs/en/agent-sdk/overview) (later: managed multi-agent patterns)
