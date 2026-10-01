# Identity learning progress

Current module: **4: Credentials: what actually proves identity**
Starting level: very basic
Goal: expert in identity security, traditional and in the age of AI
Target pace: four evenings a week, 45–60 min each (roughly 16 weeks)

## Checklist

### Phase 1: Foundations
- [x] M1 What is an identity?
- [x] M2 The four questions (IAAA)
- [x] M3 Who talks to whom: user-to-machine, user-to-user, machine-to-machine
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
- 2026-10-02 · Doodle icons on every analogy · He asked for images in the course to make it visually easier to understand (visual-learner profile). Added a small hand-drawn line-art SVG doodle next to each of the course's 11 analogy boxes, matching each story: a building + badge (Module 1), a wristband (Module 2), a courier parcel (Module 3), a signet ring + padlock (Module 4), a wax seal (Module 5), a clipboard checklist (Module 7), a theme-park ticket (Module 8), a rubber stamp (Module 10), a valet key fob (Module 12), a safe + spare key (Module 14), and a building with every floor checked (Module 17, Zero Trust). Icons use the page's existing colour tokens (good/accent) so they match the existing diagram style, sit inline via a new flex layout on `.analogy`, and shrink on phone width. Republished identity.html. · -- · Continue module sequence at Module 4
- 2026-10-02 · Course audit: define-before-use · He read Module 4 (credentials: passkey, SAML, ID token, service tickets, FIDO2) and said terms were thrown in without context -- a direct application of his standing "define before use" rule to the course content itself, not just live teaching. Audited the full 33-module course for terms used before the module that actually explains them. Real fixes: Module 3's protocol table now has a note explaining the names are deliberately unexplained at that point (with forward citations to Modules 8/11/12), plus inline citations in its mutual-authentication paragraph; Module 4's "primary vs derived credentials" section was rewritten with inline glosses and module citations for identity provider, SAML assertion, ID token, Kerberos TGT/service tickets, OAuth tokens, plus 7 credential-table rows got "(Module N)" citations; Module 5 and 6 each had a bare "identity provider" mention before its real explanation in Module 10, now glossed inline; Module 8 got citations for ITDR and Tier 0; Module 14 got a citation for Tier 0. Checked but left alone as already fine: honeytoken (M4, self-defined in the same sentence), BloodHound (M7, got a light citation anyway), Golden SAML (correctly placed inside the SAML module itself), confused deputy (M26, defined in the same breath it's used). Republished identity.html. · -- · Continue module sequence at Module 4
- 2026-10-02 · M2-M3 recap (gap closed) · Recapped both modules properly: IAAA and why AuthN != AuthZ (most breaches are authorization failures, not authentication ones), tokens-as-wristbands, the four caller/callee patterns, the human-present test as the reason machine identity is a separate discipline, delegation vs impersonation. Checked the knowledge base: its Concepts cards for both modules were already accurate (pre-seeded 2026-09-28), nothing needed fixing. Security-lens reinforcement now done for M1-M3. · -- · Module 4: Credentials
- 2026-10-02 · M2, M3 self-read on mobile · He read Modules 2 (the four questions: IAAA) and 3 (who talks to whom) independently on his phone, outside a guided session -- not taught live. Checklist updated to reflect it. Flagged: unlike M1, these two have no live note / knowledge-base capture yet, since the usual explain-back + security-lens-reinforcement cycle didn't happen. Offered a quick recap; his call whether to take it or move straight to M4. · No KB entry yet for M2-M3 -- worth a short recap if he wants the security lens reinforced · Module 4: Credentials
- 2026-10-01 · Labs plan, audited for real feasibility · He pushed back twice: first on a reflective-Q&A "lab," then on whether the 11-lab plan was genuinely connected and live-demoable, not just asserted. Audited every lab against "can this actually be clicked through live on a real free app, reproducibly." Found two real gaps, not cosmetic ones: (1) Lab 05 (detection) would have needed an extra Azure Log Analytics signup for real KQL -- decided on the light version instead (filter/export real sign-in logs in the Entra portal, no extra signup); (2) Labs 07-08 (Kerberos, attack path) were wrongly planned against the MVP track's bare Windows client, which has no domain controller and couldn't produce a real Kerberos ticket -- the honest fix is GOAD (a real small AD forest), which is parked for now rather than faked with a lighter substitute. Also named the real SAML app (Azure AD SAML Toolkit) and upgraded the AWS lab from reading a policy to actually testing a real Allow/Deny. Thread A (Entra tenant + the course's own "Priya" persona, Labs 01-06) is the one fully ready to build when reached. · -- · Continue module sequence at Module 2
- 2026-10-01 · Labs infrastructure, corrected · Created `Labs/` as a standalone hands-on lab series, used in the evening Revision slot. First pass built a reflective Q&A "lab" for Module 1 — he pointed out it wasn't a real lab (no technical artifact) and that not every module needs one. Redone: surveyed all 33 modules for where a genuine technical exercise exists (a real token, command, tool or config to touch) — only 10 modules qualify (M5, 8, 10–11, 12, 17, 20, 21, 23, 27, 29) plus the capstone. `Labs/README.md` now holds that honest, sparser index with the reasoning per module. No lab built yet — the first real one (M5, set up a passkey) waits until that module is taught. · -- · Continue module sequence at Module 2
- 2026-10-01 · OEM products (separate track) · Read two Cisco Live decks (BRKSEC-2879 "Duo Identity Security", BRKSEC-2162 "Identity Intelligence Demystified") and added a new "OEM products" section to identity.html: Duo's true-passwordless/device-trust/AD-Defense-for-legacy-Kerberos-NTLM product, and Cisco Identity Intelligence (CII, formerly Oort) as a real ITDR/ISPM implementation -- multi-IdP correlation, "checks" as detection rules, streaming vs API sync detection-speed gap, a worked Evilginx/AiTM session-hijack example, User Trust Level. Real sourced numbers added (44% of identity attacks target AD, 60% of breaches involve identity, up to 92:1 projected machine-to-human identity ratio). This is a separate track from the 33-module course sequence, not counted against module progress. · -- · Continue module sequence at Module 2; next OEM session whenever more vendor material is added
- 2026-09-30 · Course update + M1 taught · Module 14 expanded to properly teach PIM (Entra ID's eligible/active, time-bound role activation) alongside PAM (vaulting, rotation, session brokering) as two related but distinct concepts -- was previously PAM-only with a passing PIM mention. Then actually taught Module 1 for real (first session with real content, after four setup-only sessions on 2026-09-28): entity/identifier/attribute/credential, human vs. non-human identities, why identity is "the new perimeter," the office-building analogy. · -- · Read Module 2 (the four questions: identify, authenticate, authorize, audit)
- 2026-09-28 · Knowledge base · Created identity.html as the searchable knowledge base; Claude captures learnings there after every session · — · Read Module 1
- 2026-09-28 · Course update · Goal set to identity security expert (traditional + AI); added Security lens to every module, attack chain, Tier 0, detection, incident response, AI phase, expert path; evening plan · — · Read Module 1
- 2026-09-28 · Course update · Added modules on U2M/U2U/M2M, credentials, NTLM and Kerberos, SSO and SAML; expanded MFA · — · Read Module 1
- 2026-09-28 · Setup · Course, plan and study method created on mobile · — · Read Module 1
