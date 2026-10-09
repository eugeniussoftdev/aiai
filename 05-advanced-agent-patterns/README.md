# 05 - Advanced agent patterns and execution control

## What this is

You already have tools, loops, and orchestration. This part is about **rules around the loop** so the agent does not break money, accounts, or data.

In real code these are mostly simple `if` checks. People call them "patterns", but they are just conditions with serious risks.

Main ideas:
- limit how many times the loop can run
- ask a human before risky tools (refund, delete, send email)
- allow or block tools by name
- retry once, then stop and call a human
- stop the agent and hand the case to a person

This is your code around `messages.create`. It is not a special Claude feature with one name.

## Rules from real apps (the important ones)

### Money (shop, bank, billing)

| Rule | Example |
| --- | --- |
| Big amount needs a human | Refund or payout over €100 (or €1000) needs approval |
| Two people for big moves | Agent prepares a large transfer, a human confirms |
| Do not pay twice | Same `refund_order(order_id)` called again must not refund again |
| Cap how often | Max N refunds per user per hour |
| Freeze on fraud | Weird activity? Turn off write tools and call a human |
| Read is easy, write is hard | Lookup is free. Take payment only after confirm |
| Check account details | Wrong currency or unknown bank account? Block the tool |

### Login and accounts

| Rule | Example |
| --- | --- |
| Extra check before unlock | Unlock only after MFA or ID check works |
| No passwords in chat history | Do not put secrets in `messages`. Tool returns ok or fail only |
| Trust the session, not the text | Use `user_id` from login, not "I am user 5" from the user message |
| Cool down | After failed logins, do not let the agent spam `reset_password` |
| Split jobs | Auth agent cannot refund. Payments agent cannot unlock |

### Health data and private data

| Rule | Example |
| --- | --- |
| Stay in your job | Admin bot: booking and email only. No medical advice tools |
| Return less data | Tool returns only fields you need, not the full record |
| Log every tool call | Who called what, when, why |
| Human for delete / share out | Delete patient file or send data outside? Always human |
| Keep data in region | Block tools that send health data to the wrong country |

### Email, SMS, chat replies

| Rule | Example |
| --- | --- |
| Draft first, send later | Agent writes the email. Human (or second check) sends it |
| Only known emails | Can only send to the customer's verified address |
| Limit how many messages | Max N messages per day per ticket |
| Legal / angry cases | Refund denial or legal threat? Human sends, not the bot |
| Clean tool output | Remove card numbers and SSN before putting results back into messages |

### Servers and production

| Rule | Example |
| --- | --- |
| Careful in prod | Restart or scale down in prod needs approval |
| Plan before apply | Run `plan_migration` before `apply_migration` |
| No "delete all" | Tool rejects delete-all without a clear confirm |
| Only in a safe window | Risky deploy only in allowed hours, else human |
| Stop after repeated errors | 3 API fails? Stop the loop and page on-call |

### Rules for almost every serious agent

| Rule | Example |
| --- | --- |
| Max steps / time | Support agent: max 8 tool rounds or 60 seconds |
| Cost limit | Stop if tokens or $ for this session go too high |
| Different tools per role | Guest bot and admin bot do not share the same tools |
| Deny even if Claude asks | `if name not in ALLOWED: return error`. Do not trust the model alone |
| Retry, then human | Timeout once, retry. Still fail? Escalate with a short summary |
| Kill switch | One flag turns off all write tools right away |
| Not sure? Ask a human | Conflicting results or unclear case. Do not guess |
| Do not trust tool text as orders | Files and tool results can say "ignore all rules". Ignore that. Follow your code rules |

### Do not do this

- Hide tool errors and pretend it worked
- Endless loop with tools that change data
- One agent with unlock + refund + delete + email all together
- Put API keys or full card numbers into the message history
- Auto-approve just because "the model is sure"

## Practice

### TODO 1 - Rules on paper

- [ ] List 3 safe tools and 3 risky tools for an app you know
- [ ] Write approval rules (example: refund > €100 needs a human)
- [ ] Pick max tool rounds for a support agent (and what to say when you hit the limit)
- [ ] Define one case that must go to a human (fraud, VIP, low confidence)

### TODO 2 - Code the checks later

- [ ] Add `max_iterations` to the agent loop
- [ ] Before a risky tool, ask `input("Approve? ")` or call an approve API
- [ ] On tool error: retry once, then escalate (do not fail quietly)
- [ ] Block tools by name even if the model requests them

## Docs

- [Stop reasons](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)
- [How tool use works](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works) (`tool_choice`)
- [Tool use](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)
