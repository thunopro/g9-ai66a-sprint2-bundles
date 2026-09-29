## Closes

Closes #47

## What changed

Fills section 3 of `docs/design.md`: 14 endpoints (Method / Path / Who / Input / Success / Error codes / Story), covering all six P0 stories, with error codes tied to business rules.

## How to test it

1. For each P0 story US01-US06 in `docs/requirements.md` section 4, find at least one row in the API table
2. Pick two error messages in the table and find the same sentence in the acceptance criteria

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

@thunopro
