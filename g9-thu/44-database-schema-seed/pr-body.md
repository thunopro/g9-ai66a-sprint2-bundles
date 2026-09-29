## Closes

Closes #44

## What changed

Adds the SQLite schema (7 tables, every constraint citing its business rule), the seed script and `data/venues.csv` (24 venues), tests proving the database itself refuses rule-breaking rows, and section 2 of `docs/design.md` with the ERD.

## How to test it

1. Activate the virtual environment, `pip install -r requirements.txt`
2. `python src/init_db.py` → prints `venue 24 rows` (run it twice: same counts)
3. `pytest` → `10 passed`
4. Open `docs/images/erd.png` next to the table in design.md section 2 - every table, PK and FK in one must be in the other

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

@htngochan2802
