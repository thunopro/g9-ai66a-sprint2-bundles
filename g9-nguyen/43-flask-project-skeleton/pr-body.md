## Closes

Closes #43

## What changed

Creates the Python project every later story is built in: `requirements.txt`, `.env.example`, `src/db.py` (one connection helper with foreign keys on), `src/app.py` (app factory and `GET /health`), and the first test so CI has something to run.

## How to test it

1. `python -m venv .venv` then activate it (`source .venv/bin/activate`, Windows: `.venv\Scripts\Activate.ps1`)
2. `pip install -r requirements.txt` and `cp .env.example .env`
3. `pytest` → `1 passed`
4. `python src/app.py`, open http://localhost:5000/health → `{"status": "ok"}`

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

@thunopro
