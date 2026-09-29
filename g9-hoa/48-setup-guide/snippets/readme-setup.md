## Setup

**To run the project on a new machine, follow [`docs/SETUP.md`](docs/SETUP.md)** - it
lists the prerequisites, the commands for Windows and macOS/Linux, and how to check that
it worked. In short:

```bash
git clone https://github.com/SE-FDA-NEU/G9_AI66A_SE.git
cd G9_AI66A_SE
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1
cp .env.example .env                                 # Windows: copy .env.example .env
pip install -r requirements.txt
python src/init_db.py      # creates data/venues.db with 24 venues
python src/app.py          # open http://localhost:5000/search
```

Start reading with [`docs/requirements.md`](docs/requirements.md), then
[`docs/design.md`](docs/design.md).
