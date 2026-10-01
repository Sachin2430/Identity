# Identity Labs

One lab per cluster of modules, built as you reach it — not all 33 modules upfront. Each lab is **predict → run → explain**: guess first, do the real exercise, then explain it back in your own words. These are the full, standalone version of testing your learning; the short inline "Try it" boxes inside `../identity-learning.html` stay as quick prompts, but **these labs are the ones done in the evening Revision slot**, not the morning teaching block.

**Keep every lab minimal but reproducible** (his rule, 2026-10-01): a fixed, concrete procedure with a single clear deliverable — a filled table, a specific decoded token, one incident record — not open-ended prose. Anyone redoing the same lab on a different day should land on the same kind of output.

Numbered to match the course's own 6 phases. A lab is only written once its modules have actually been taught — don't jump ahead.

| # | Lab | Covers | Status |
|---|---|---|---|
| 01 | [Identity Inventory](lab-01-identity-inventory.md) | M1 — What is an identity? | ✅ Written |
| 02 | The Four Questions, Live | M2 — IAAA | Not yet — M2 not taught |
| 03 | Who Talks to Whom, Credential Audit | M3–4 — interaction patterns, credentials | Not yet |
| 04 | MFA Strength Check | M5 — Authentication & MFA | Not yet |
| 05 | Authorization Models in the Wild | M6 — Authorization | Not yet |
| 06 | Directory & Lifecycle Trace | M7, M9 — directories, JML lifecycle | Not yet |
| 07 | Windows Auth Deep Dive | M8 — NTLM/Kerberos | Not yet (needs a Windows box — see the MVP track's UTM VM) |
| 08 | SSO & SAML Trace | M10–11 — SSO, SAML | Not yet |
| 09 | OAuth/OIDC Token Decode | M12 — OAuth 2.0, OIDC | Not yet |
| 10 | Governance, PAM/PIM, CIAM Mapping | M13–15 | Not yet |
| 11 | Attack Chain Walkthrough | M16–17 — attacks, attack chain | Not yet |
| 12 | Defending & Tier 0 Audit | M18–19 — Zero Trust, ITDR, ISPM, control plane | Not yet |
| 13 | Detection & Incident Tabletop | M20–21 | Not yet |
| 14 | NHI Audit | M22–24 — non-human identities | Not yet |
| 15 | AI Agent & MCP Permission Audit | M26–27 — AI agents, securing agents | Not yet |
| 16 | Deepfake-Resistant Procedure + Shadow AI | M25, M28 | Not yet |
| 17 | Cloud IAM & Standards Mapping | M29–30 | Not yet |
| 18 | Capstone — Design Your Identity Program | M31–33 | Not yet (this is Module 33 itself — the lab *is* the capstone) |

## How a lab gets written

When you reach a module cluster above, say so in a `/identity` session and the next lab gets built then — grounded in what was actually taught, not generic advice. Each lab file has:
1. **Predict** — a short guess before you start, so you notice what you got wrong.
2. **Run** — the real, hands-on exercise. Free tools only (developer tenants, your own accounts, browser dev tools, `.claude/tools`) unless you already have paid access to something.
3. **Explain** — answer in your own words; this is what actually sticks.
4. **Cross-check** — compare against the matching concept card in [`../identity.html`](../identity.html).
