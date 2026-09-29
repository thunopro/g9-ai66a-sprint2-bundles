## Closes

Closes #46

## What changed

Fills sections 1 and 5 of `docs/design.md`: a container-level architecture diagram with every arrow labelled, and three ADRs (web framework, double-booking prevention, database).

## How to test it

1. Open `docs/design.md` section 1: at least 4 components, no arrow without a label
2. Section 5: each ADR has at least 2 options and a concrete condition that would change the decision

## Screenshot / output

<!-- Drag a screenshot here if the change is visible. -->

---

## Definition of Done

- [x] Every acceptance criterion on the linked issue passes
- [x] The code runs from a clean clone (`git clone` then the setup commands in README)
- [ ] At least one automated test covers the new behaviour
- [ ] CI is green
- [x] No secrets, API keys, `.env` files, or database dumps in the diff
- [x] No commented-out dead code left behind
- [x] README or `docs/` updated if the setup steps changed

## Author declaration

- [x] I wrote this code, or I have named every other contributor below
- [x] Where I used an AI assistant, I have said so and I can explain every line if asked

AI assistance used (tool and what for, or "none"): AI assistant used to draft the code and text from the tested team draft; I read every line, ran it locally and can explain it.

## Reviewer

@lequangk2006-sys
