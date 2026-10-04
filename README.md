# Identity Learning Track

Self-study track on identity management, identity security, non-human identities (NHI) and identity in the age of AI, from first principles to expert level. **Goal: become an expert in identity security, both traditional and in the age of AI.** It lives under `PA/office/identity` and is meant to be opened in Claude Desktop later as a study workspace.

## What's in this folder

| File | Purpose |
|---|---|
| `identity.html` | **One file, everything** (consolidated 2026-10-01). Two tabs: **Course** (33 modules in 6 phases, analogies, diagrams, a Security lens on every foundation and IAM module, dedicated security/NHI/AI phases, self-checks and labs — tick modules off as you go, progress saved in that browser) and **Knowledge Base** (everything learned, condensed and searchable: concepts, protocol cheat sheets, an attack → detect → defend matrix with MITRE IDs, a detection library, IR playbooks, incident files, NHI and AI quick reference, OEM product deep-dives, standards, glossary, open questions — Claude adds your session learnings here). Open it in any browser, published and pinned on your phone. |
| `CLAUDE.md` | Instructions for Claude on how to tutor you with this material. Claude reads it automatically when you open this folder. |
| `progress.md` | Your study log: what you finished, what clicked, what's still fuzzy. Claude uses it to pick up where you left off. |
| `notes/` | Your own notes, one file per module (e.g. `notes/m10-sso.md`). Write them in your own words. |
| `Labs/` | Standalone, numbered hands-on labs — one per module cluster where a real technical exercise exists, built as you reach it. |

## Learning goals

By the end you should be able to:

1. Explain identity from first principles: entity, identifier, attribute, credential; AuthN vs AuthZ; user-to-machine, user-to-user and machine-to-machine interactions; every common credential type and MFA method.
2. Describe how an enterprise runs identity: directories, NTLM and Kerberos, lifecycle, SSO, SAML, OAuth/OIDC, IGA, PAM, CIAM.
3. Think like an attacker: follow an intrusion from first login to domain takeover, and know how each step is detected and stopped.
4. Protect Tier 0, write identity detections, and run identity incident response.
5. Secure NHIs: secrets, workload identity, third-party integrations.
6. Handle identity in the age of AI: deepfake-resistant processes, AI-agent identity and authorization, shadow AI, and AI as a defender.
7. Hold your own with architects, auditors and vendors, and design an identity program (capstone).

## The plan (about 3 months, daily weekdays)

**Rhythm (updated 2026-10-02, effective 2026-10-03):** weekday mornings, 90 minutes, right after GYM/Exercise. The evening revision pass was dropped in this overhaul. Longer labs fit a weekend if you want them.

| Session | What to do |
|---|---|
| 1 | Read the next module (25–30 min) |
| 2 | Explain it back to Claude; answer "Check yourself" |
| 3 | Security lens: attacker's view, detection, defense; ask Claude to quiz you. Start the next module. |
| 4 | Lab, then capture takeaways in `identity.html` and one line in `progress.md` |

(Renamed from "Evening" 2026-10-02 — this rotation now runs in the 90-minute morning slot, not the evening.)

| Week | Modules | Focus | Hands-on |
|---|---|---|---|
| 1 | 1–3 | What identity is; the four questions; who talks to whom | Map one office process hop by hop |
| 2 | 4–5 | Credentials; authentication and MFA | Set up a passkey |
| 3 | 6–7 | Authorization; directories | Free Entra ID or Okta developer tenant |
| 4 | 8 | NTLM and Kerberos | Run `klist` on a work PC |
| 5 | 9–10 | Lifecycle; single sign-on | Trace one leaver through every app |
| 6 | 11–12 | SAML; OAuth and OIDC | SAML-tracer; decode an ID token |
| 7 | 13–15 | IGA, PAM, CIAM | Sketch your company's access-review process |
| 8 | 16–17 | Attacks; the attack chain | BloodHound sample data or GOAD (weekend) |
| 9 | 18–19 | Defending identity; protecting Tier 0 | Count your admins and break-glass accounts |
| 10 | 20–21 | Detection engineering; incident response | Query sign-in logs; tabletop with Claude |
| 11 | 22–24 | NHI basics, failures, workload identity | Audit your GitHub tokens and OAuth apps |
| 12 | 25–26 | AI-powered attacks; AI agents as identities | Write a deepfake-resistant help-desk procedure |
| 13 | 27–28 | Securing AI agents; AI for defenders and shadow AI | Review your Claude Desktop MCP connectors |
| 14 | 29–31 | Cloud IAM, standards, market | Read AWS policies; compare vendors in one category |
| 15 | 32 | Becoming an expert | Set up your home lab; choose a certification path |
| 16 | 33 | Capstone | Write an identity program; have Claude critique it as a CISO |

Fall behind? Don't skip Phase 1, Modules 8–12 (Kerberos, NTLM, SSO, SAML, OAuth/OIDC) or Phase 3; everything later depends on them.

Useful prompts once you're in Claude Desktop with this folder:

- `Start my next identity session.` (Claude reads `progress.md` and continues.)
- `Quiz me on Module 11 (SAML), five questions, harder than the ones in the file.`
- `Explain Kerberoasting like I'm new to Active Directory, then draw it as a sequence.`
- `Security lens drill: pick a random module and ask me how it's attacked, detected and defended.`
- `Run an identity incident tabletop: a stolen session token in finance. You play the attacker and the logs.`
- `What's changed in AI agent identity and MCP security since this course was written?`
- `Give me a real-world scenario from my office and ask me how I'd handle it.`
- `Update the HTML with a deeper section on <topic>.`
- `Add this to my knowledge base: <what you learned or a question>.`
- `Search my knowledge base for everything on token theft and quiz me on it.`

## Using this on Claude Desktop

This folder was created on mobile in the GitHub repo `sachin2430/test`, on branch `claude/identity-management-learning-14itys`. To bring it to your laptop:

```bash
git clone -b claude/identity-management-learning-14itys https://github.com/sachin2430/test.git
# then copy test/PA/office/identity into your local PA/office folder
```

Or merge the branch into `main` and pull it on the laptop. After that, point Claude Desktop (or a Claude project) at `PA/office/identity` so it picks up `CLAUDE.md`.
