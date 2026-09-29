## Closes

Closes #48

## What changed

Adds `docs/SETUP.md`, the guide the instructor follows word for word on a new machine, and links it from the first screen of the README. Tested by a student from another team on their own laptop (see the Tested by line).

## How to test it

1. On a machine that has never cloned this repo, follow `docs/SETUP.md` word for word
2. http://localhost:5000/search shows 24 venues, with no error and no question asked
3. The Tested by line names someone outside the team

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

@peng543
