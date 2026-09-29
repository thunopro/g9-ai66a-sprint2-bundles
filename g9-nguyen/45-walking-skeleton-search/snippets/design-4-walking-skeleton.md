## 4. Walking skeleton

| | |
|---|---|
| **Route** | `GET /search` (also served at `/`), with optional `?sport=` and `?area=` |
| **Table read** | `venue` - **24 rows**, seeded from `data/venues.csv` by `python src/init_db.py` |
| **Story it slices** | US03 Customer searches for venues (#16) - BR9 |
| **Code** | `src/app.py` (route), `src/templates/search.html` (page), `src/db.py` (connection) |
| **Test** | `tests/test_search.py` - 4 tests, including one that inserts a row *after* start-up and sees it on the page, which an array in the code could never do |

**The query behind the page**

```sql
SELECT v.id, v.name, v.sport, v.area, v.address, v.hourly_price, v.open_hour, v.close_hour
FROM venue v
WHERE v.active = 1
  AND (:sport = '' OR v.sport = :sport)
  AND (:area  = '' OR v.area  = :area)
ORDER BY v.area, v.sport, v.name;
```

Both filters must match at the same time (BR9); with no match the page shows exactly
**"No venues found"**. Parameters are bound, never pasted into the SQL string.

**Screenshot** - `http://localhost:5000/search`, all 24 venues:

![Walking skeleton running](images/walking-skeleton.png)

**Settings** live in `.env.example` (`PORT`, `DATABASE_PATH`, `SECRET_KEY`), which is
committed; `.env` itself and `data/venues.db` are in `.gitignore`. Full install steps:
[`docs/SETUP.md`](SETUP.md).
