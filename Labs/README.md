# Identity Labs

**One holistic environment, not five disconnected ones (redesigned 2026-10-03, his explicit request — "a holistic lab, not independent different labs").** Earlier this was five separate threads (Entra tenant, parked on-prem AD, a GitHub/Claude self-audit, an AWS account, and Keycloak). Now it's **one self-hosted Keycloak realm, one consistent test user ("Priya," the course's own persona), and every module's use case run against that same running system** — so nothing is a cold start, and everything you learn about the environment in Lab 1 carries into every lab after it.

**Not every module gets a lab** — only where there's a real technical artifact to produce. A module that's pure vocabulary or a reading/mapping exercise doesn't get one; the course's own inline "Try it" box is enough there.

**Keep every lab minimal but reproducible:** one concrete deliverable per lab, free tools only. Built live with Sachin, one command at a time, same rule as the F_AI labs: Claude generates the commands and explains what each proves; Sachin runs every command himself; results get captured from his real output, never invented.

---

## The holistic lab: one Keycloak realm, one Priya

**One-time setup:**
```bash
docker run -d --name identity-lab -p 8080:8080 \
  -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin \
  quay.io/keycloak/keycloak start-dev
```
Minutes, no signup, no credit card, fully disposable (`docker stop identity-lab && docker rm identity-lab` to start clean). Admin console: http://localhost:8080

| # | Lab | Module | Builds on | What it proves |
|---|---|---|---|---|
| 1 | Stand up Keycloak, create a realm, add Priya by hand | M7 — Directories and the source of truth | *(starts the thread)* | A directory is something you build, not a pre-populated tenant you're handed |
| 2 | Enroll Priya's passkey (WebAuthn), see what's actually stored | M5 — Authentication & MFA | Lab 1's realm + user | What a passkey credential really is on the IdP side |
| 3 | Register a SAML client, SSO as Priya, capture the real assertion | M10–11 — SSO, SAML | Lab 1 | The real XML assertion Keycloak issues, not a diagram of one |
| 4 | Register an OIDC client, run the authorization code flow, decode the real ID token | M12 — OAuth 2.0, OIDC | Lab 1 | You control the IdP issuing the token, not just the client side |
| 5 | Provision and deprovision Priya via the Admin REST API instead of the UI | M9 — The identity lifecycle | Lab 1 | A genuine SCIM-adjacent exercise, not a reading |
| 6 | Filter Priya's real sign-in events out of Keycloak's own event log — the ones Labs 2–4 just generated | M20 — Identity detection engineering | Labs 2, 3, 4's real events | Detection against real, self-generated log data |
| 7 | Incident tabletop: "Priya's session is compromised" — actually revoke her real session, review the real audit trail | M21 — Identity incident response | Everything above | A real incident response action, not a hypothetical |

Every lab after Lab 1 reuses the same realm and the same Priya — nothing is re-created from scratch, and findings compound (Lab 6's detection literally reads the events Labs 2–4 produced).

---

## What stays separate, and why (not consolidated — different technology, not a shortcut)

| Lab | Module | Why it can't fold into the Keycloak environment |
|---|---|---|
| Kerberos ticket inspection, BloodHound attack-path mapping | M8 — NTLM/Kerberos, M17 — Attack chain | A real Kerberos ticket needs a real Windows domain controller. Keycloak can't produce one. **Parked** — needs [GOAD (Game of Active Directory)](https://github.com/Orange-Cyberdefense/GOAD), a real small AD forest, not faked with a lighter substitute. |
| Real IAM Allow/Deny test | M29 — Cloud IAM | AWS IAM is a different paradigm — resource permissions, not an identity provider issuing tokens. Its own small lab: a restrictive IAM user + policy, one allowed S3 action, one denied one, on the AWS Free Tier. |
| Audit your own GitHub tokens and OAuth app connections | M23 — How NHIs break | This audits *your real account*, not a lab environment — nothing to consolidate. |
| Audit your own Claude Desktop/Code MCP connector permissions | M27 — Securing AI agents | Same — your real setup, not a simulated one. |
| PIM (eligible → active role activation) | M14 — PAM/PIM | No honest free equivalent exists on Keycloak (no built-in time-bound role activation). Flagged openly rather than faked. **Optional:** a free Microsoft 365 Developer Program tenant gives real Entra ID P2 (which is what unlocks PIM) if you want this one module's hands-on piece specifically — a deliberate side-trip, not folded into the main thread. |

## Capstone

Module 33 draws on real findings from the holistic lab plus the separate items above (a real revoked session, a real IAM Deny, a real GitHub token gap) as evidence, not hypotheticals.

## Modules with no lab

M1–4, 6, 13, 15–16, 18–19, 22, 24–26, 28, 30–32 — vocabulary, classification or reading/mapping. The inline "Try it" box covers them where one exists.

## How a lab actually gets written

Said in a `/identity` session once you reach it — built live, one command at a time, Claude generating the commands and explaining what's about to be proven, Sachin running every command himself and reporting the real result. Each lab states its one concrete deliverable up front and ends with a cross-check against [`../identity.html`](../identity.html). Visual companion pages go in `Work/Identity/Lab_Pages/NN-<slug>/lab.html` (cream/card style, same as the F_AI labs), prompts styled `Lab1:`, `Lab2:` … matching this table's numbering.
