## Closes

Closes #45

## What changed

Adds the walking skeleton: `GET /search` reads table `venue` (24 seeded rows) and renders it, with sport and area filters (BR9). Tests prove the page follows the database. Section 4 of `docs/design.md` records the route, the SQL and a screenshot.

## How to test it

1. `python src/init_db.py` then `python src/app.py`
2. Open http://localhost:5000/search → `24 venue(s) found`
3. Choose Football + Cau Giay → exactly 2 venues; Tennis + Ha Dong → `No venues found`
4. `pytest` → `15 passed`

## Screenshot / output

<!-- Drag a screenshot here if the change is visible. -->

---

## Definition of Done

- [x] Every acceptance criterion on the linked issue passes
- [x] The code runs from a clean clone (`git clone` then the setup commands in README)
- [x] At least one automated test covers the new behaviour
- [ ] CI is green
- [x] No secrets, API keys, `.env` files, or database dumps in the diff
- [x] No commented-out dead code left behind
- [x] README or `docs/` updated if the setup steps changed

## Author declaration

- [x] I wrote this code, or I have named every other contributor below
- [x] Where I used an AI assistant, I have said so and I can explain every line if asked

AI assistance used (tool and what for, or "none"): AI assistant used to draft the code and text from the tested team draft; I read every line, ran it locally and can explain it.

## Reviewer

@PhunghoaAI
