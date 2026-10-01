# Identity learning progress

Current module: **2: The four questions (IAAA)**
Starting level: very basic
Goal: expert in identity security, traditional and in the age of AI
Target pace: four evenings a week, 45–60 min each (roughly 16 weeks)

## Checklist

### Phase 1: Foundations
- [x] M1 What is an identity?
- [ ] M2 The four questions (IAAA)
- [ ] M3 Who talks to whom: user-to-machine, user-to-user, machine-to-machine
- [ ] M4 Credentials: what actually proves identity
- [ ] M5 Authentication and MFA in depth
- [ ] M6 Authorization in depth

### Phase 2: How organizations run identity
- [ ] M7 Directories and the source of truth
- [ ] M8 Windows authentication: NTLM and Kerberos
- [ ] M9 The identity lifecycle
- [ ] M10 Single sign-on, from first principles
- [ ] M11 SAML in depth
- [ ] M12 OAuth 2.0 and OpenID Connect
- [ ] M13 Identity governance (IGA)
- [ ] M14 Privileged access (PAM) and privileged identity management (PIM)
- [ ] M15 Customer identity (CIAM)

### Phase 3: Identity security
- [ ] M16 How identities get attacked
- [ ] M17 The identity attack chain
- [ ] M18 Defending identity: Zero Trust, ITDR, ISPM
- [ ] M19 Protecting the identity control plane
- [ ] M20 Identity detection engineering
- [ ] M21 Identity incident response

### Phase 4: Non-human identities
- [ ] M22 What is a non-human identity?
- [ ] M23 How NHIs break
- [ ] M24 Securing workloads and secrets

### Phase 5: Identity in the age of AI
- [ ] M25 AI-powered attacks on identity
- [ ] M26 AI agents as identities
- [ ] M27 Securing AI agents: a reference architecture
- [ ] M28 AI for identity defenders, and shadow AI

### Phase 6: Advanced and professional
- [ ] M29 Cloud IAM and entitlement management
- [ ] M30 Standards and frameworks
- [ ] M31 The market landscape
- [ ] M32 Becoming an identity security expert
- [ ] M33 Capstone: design an identity program

## Session log

<!-- Newest first. Format: YYYY-MM-DD · Module · What clicked · What's fuzzy · Next -->
- 2026-10-01 · Labs infrastructure, corrected · Created `Labs/` as a standalone hands-on lab series, used in the evening Revision slot. First pass built a reflective Q&A "lab" for Module 1 — he pointed out it wasn't a real lab (no technical artifact) and that not every module needs one. Redone: surveyed all 33 modules for where a genuine technical exercise exists (a real token, command, tool or config to touch) — only 10 modules qualify (M5, 8, 10–11, 12, 17, 20, 21, 23, 27, 29) plus the capstone. `Labs/README.md` now holds that honest, sparser index with the reasoning per module. No lab built yet — the first real one (M5, set up a passkey) waits until that module is taught. · -- · Continue module sequence at Module 2
- 2026-10-01 · OEM products (separate track) · Read two Cisco Live decks (BRKSEC-2879 "Duo Identity Security", BRKSEC-2162 "Identity Intelligence Demystified") and added a new "OEM products" section to identity.html: Duo's true-passwordless/device-trust/AD-Defense-for-legacy-Kerberos-NTLM product, and Cisco Identity Intelligence (CII, formerly Oort) as a real ITDR/ISPM implementation -- multi-IdP correlation, "checks" as detection rules, streaming vs API sync detection-speed gap, a worked Evilginx/AiTM session-hijack example, User Trust Level. Real sourced numbers added (44% of identity attacks target AD, 60% of breaches involve identity, up to 92:1 projected machine-to-human identity ratio). This is a separate track from the 33-module course sequence, not counted against module progress. · -- · Continue module sequence at Module 2; next OEM session whenever more vendor material is added
- 2026-09-30 · Course update + M1 taught · Module 14 expanded to properly teach PIM (Entra ID's eligible/active, time-bound role activation) alongside PAM (vaulting, rotation, session brokering) as two related but distinct concepts -- was previously PAM-only with a passing PIM mention. Then actually taught Module 1 for real (first session with real content, after four setup-only sessions on 2026-09-28): entity/identifier/attribute/credential, human vs. non-human identities, why identity is "the new perimeter," the office-building analogy. · -- · Read Module 2 (the four questions: identify, authenticate, authorize, audit)
- 2026-09-28 · Knowledge base · Created identity.html as the searchable knowledge base; Claude captures learnings there after every session · — · Read Module 1
- 2026-09-28 · Course update · Goal set to identity security expert (traditional + AI); added Security lens to every module, attack chain, Tier 0, detection, incident response, AI phase, expert path; evening plan · — · Read Module 1
- 2026-09-28 · Course update · Added modules on U2M/U2U/M2M, credentials, NTLM and Kerberos, SSO and SAML; expanded MFA · — · Read Module 1
- 2026-09-28 · Setup · Course, plan and study method created on mobile · — · Read Module 1
