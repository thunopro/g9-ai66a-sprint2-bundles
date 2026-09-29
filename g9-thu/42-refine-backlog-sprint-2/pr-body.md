## Closes

Closes #42

## What changed

Adds the Sprint 2 section of `docs/backlog.md` (owners, points, order, business-rule ranges), a `docs/design.md` skeleton with one owner per section, the missing `board-in-review.yml` workflow, and README updates (Sprint 2 Scrum Master, branch convention, English-only rule).

## How to test it

1. Open `docs/backlog.md` and check the Sprint 2 table matches the board (points and owners).
2. Open `docs/design.md` and check there are six sections in the order of the brief, each with an owner and an issue number.
3. Open README and check @peng543 is named Scrum Master (Sprint 2).

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
