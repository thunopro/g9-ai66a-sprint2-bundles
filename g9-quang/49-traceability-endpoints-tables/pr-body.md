## Closes

Closes #49

## What changed

Adds a Story → Screen → Endpoint → Table table to `docs/traceability.md`, one row per P0 story, with endpoints taken from design.md section 3 and tables from section 2.

## How to test it

1. For each row, search the endpoint in `docs/design.md` section 3 - same method and path
2. For each table name, find it in the ERD in section 2

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

@htngochan2802
