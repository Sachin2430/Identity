# Identity Labs

**Not every module gets a lab** — only where there's a real technical artifact to produce. A module that's pure vocabulary or a reading/mapping exercise doesn't get one; the course's own inline "Try it" box is enough there.

**The labs are connected, not a bag of isolated exercises.** Four threads, each building on its own earlier labs instead of starting cold every time. Every lab below was checked against one bar: **can you actually click through it live, on a real free application, and reproduce it on demand** — not read about it, not run it against sample data someone else generated.

**Keep every lab minimal but reproducible:** one concrete deliverable per lab, free tools only.

## Thread A: the Priya tenant (Microsoft Entra ID, free)

**One-time setup, done as part of Lab 01** — the [Microsoft 365 Developer Program](https://developer.microsoft.com/microsoft-365/dev-program) gives a free sandbox tenant with Entra ID P2 (which is what unlocks PIM in Lab 02 — a paid feature everywhere else, free here). No credit card, auto-renews every 90 days with activity.

| # | Lab | Module | Builds on | App |
|---|---|---|---|---|
| 01 | Create the tenant + Priya, enroll her first passkey | M5 — Authentication & MFA | *(starts the thread)* | Entra ID (native) |
| 02 | Make Priya PIM-eligible for a role, then activate it — real eligible→active, real audit entry | M14 — PAM/PIM | Lab 01's tenant + user | Entra ID PIM (native) |
| 03 | Register a SAML app, SSO as Priya, capture the real assertion | M10–11 — SSO, SAML | Lab 01's user | **Azure AD SAML Toolkit** — Microsoft's free sample app built specifically for practicing SAML claims, not a placeholder |
| 04 | Register an OAuth app, run the flow, decode Priya's real ID token | M12 — OAuth 2.0, OIDC | Lab 01's user | Entra app registration (native) + jwt.io |
| 05 | Filter and export Priya's real sign-in logs — the ones Labs 01/03/04 just generated | M20 — Detection engineering | Labs 01, 03, 04's real log entries | **Light version (decided 2026-10-01):** the Entra portal's own Sign-in logs blade — filter, search, export. No Azure Log Analytics / KQL, no second Azure signup, no card required. Full KQL version stays an explicit later upgrade, not assumed. |
| 06 | Incident tabletop: "Priya's session is compromised" — actually click **Revoke sessions** on the real user, review the real audit trail | M21 — Incident response | Everything above | Entra ID (native) |

## Thread B: on-prem AD — **parked for now (decided 2026-10-01)**

Originally planned as Kerberos ticket inspection (M8) + attack-path mapping (M17), sharing one AD lab environment. **Corrected:** a bare Windows client (what the MVP track's UTM VM is) has no domain controller and no Kerberos realm — `klist` against it would show nothing real. A genuine version needs an actual small AD forest: [GOAD (Game of Active Directory)](https://github.com/Orange-Cyberdefense/GOAD), a free Vagrant+Ansible-deployed vulnerable domain, is the honest way to get real tickets for Lab 07 and real BloodHound data (via SharpHound) for Lab 08 from the *same* deployment. That's a heavier one-time setup than anything else here — parked until there's time to actually stand it up, not faked with a lighter substitute that wouldn't produce real data.

| # | Lab | Module | Status |
|---|---|---|---|
| 07 | `klist` — inspect a real Kerberos TGT and service ticket | M8 — NTLM/Kerberos | Parked — needs GOAD |
| 08 | BloodHound / SharpHound — map a real attack path to Domain Admin | M17 — Attack chain | Parked — needs GOAD, same deployment as 07 |

## Thread C: your real footprint

| # | Lab | Module | Builds on |
|---|---|---|---|
| 09 | Audit your actual GitHub tokens and OAuth app connections | M23 — How NHIs break | Your real GitHub account |
| 10 | Audit your actual Claude Desktop/Code MCP connector permissions | M27 — Securing AI agents | Your real setup |

## Thread D: cloud IAM (AWS)

| # | Lab | Module | App |
|---|---|---|---|
| 11 | Create a real restrictive IAM user + least-privilege policy; try an allowed S3 action and a denied one, watch the real Allow/Deny | M29 — Cloud IAM | AWS Free Tier account (IAM itself is always free; stay inside S3's free tier for the test resource) |

Upgraded 2026-10-01 from "read and annotate a sample policy" — that wasn't a live demo, just reading JSON.

## Capstone

Module 33 is already the lab — and should explicitly draw on real findings from Threads A, C and D (a real PIM activation, a real GitHub token gap, a real IAM Deny) as evidence, not hypotheticals.

## Modules with no lab

M1–4, 6–7, 9, 13, 15–16, 18–19, 22, 24–26, 28, 30–32 — vocabulary, classification or reading/mapping. The inline "Try it" box covers them where one exists.

## How a lab actually gets written

Said in a `/identity` session once you reach it — built then, grounded in what was taught, referencing the real artifacts earlier labs in its thread produced. Each lab states its one concrete deliverable up front and ends with a cross-check against [`../identity.html`](../identity.html).
