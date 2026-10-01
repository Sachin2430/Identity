# Identity Labs

**Not every module gets a lab** (his rule, 2026-10-01) — only where there's an actual technical artifact to produce: a real token to decode, a real command to run, a real tool to use, a real config to inspect. A module that's pure vocabulary or a reading/mapping exercise doesn't get one; the course's own inline "Try it" box (in `../identity-learning.html`) is enough there.

**Keep every lab minimal but reproducible:** a fixed, concrete procedure with a single clear deliverable — a decoded token, a filled-in finding, a query result — not open-ended prose or reflection questions. Anyone redoing the same lab on a different day should land on the same kind of output.

Labs are numbered in the order you'll reach them, not 1:1 with module numbers — most modules don't get one. **Done in the evening Revision slot**, not the morning teaching block. Built when you actually reach its module, not upfront.

| # | Lab | Module | Why this one gets a real lab | Status |
|---|---|---|---|---|
| 01 | Set up a passkey | M5 — Authentication & MFA | A real phishing-resistant credential you actually create | Not yet |
| 02 | Kerberos ticket inspection (`klist`) | M8 — NTLM/Kerberos | A real TGT/service ticket to inspect | Parked — needs the Windows VM (see the MVP track's UTM setup) |
| 03 | SAML login trace | M10–11 — SSO, SAML | SAML-tracer against a real SSO login, read the actual assertion | Not yet |
| 04 | Decode a real OIDC ID token | M12 — OAuth 2.0, OIDC | jwt.io against a token from an app you actually use | Not yet |
| 05 | Attack path mapping | M17 — The attack chain | BloodHound sample data or GOAD — a real graph, not a diagram | Not yet |
| 06 | Write a detection query | M20 — Detection engineering | A real KQL/SPL-style query against sample sign-in logs | Not yet |
| 07 | Incident response tabletop | M21 — Incident response | A live, interactive simulated incident — not a worksheet | Not yet |
| 08 | Audit your own GitHub tokens/OAuth apps | M23 — How NHIs break | Your actual GitHub Settings → Applications page, right now | Not yet |
| 09 | Audit your own MCP connector permissions | M27 — Securing AI agents | Your actual Claude Desktop/Code connector list, right now | Not yet |
| 10 | Read a real cloud IAM policy | M29 — Cloud IAM | A real AWS/Azure IAM JSON policy, annotated clause by clause | Not yet |
| — | Capstone | M33 | The module itself *is* the lab — no separate entry needed | — |

**Modules not listed above deliberately have no lab** — M1–4, 6–7, 9, 13–16, 18–19, 22, 24–26, 28, 30–32 are vocabulary, classification or reading/mapping exercises. The inline "Try it" box already covers them where one exists.

## How a lab gets written

When you reach one of the modules above, say so in a `/identity` session and that lab gets built then, grounded in what was actually taught. Each lab:
1. States the **one concrete deliverable** up front (a decoded token, a filled finding, a query result).
2. Uses **free tools only** unless you already have paid access to something.
3. Ends with a cross-check against the matching concept in [`../identity.html`](../identity.html).
