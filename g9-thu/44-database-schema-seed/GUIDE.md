# #44 [Task] Create database schema, ERD and seed 24 venues

- **Người làm:** @thunopro (Nguyen Khac Thu)
- **Reviewer:** @htngochan2802 (Hoang Thi Ngoc Han)
- **Branch:** `44-database-schema-seed`
- **Phải chờ merge trước:** #43
- **Khi nào làm:** 29/09, sau khi #43 merge

> Mọi thứ lên GitHub (commit, PR, comment) đều bằng **tiếng Anh** - lệnh bên dưới đã viết sẵn.
> Đọc hiểu từng file trước khi commit: thầy có thể hỏi bất kỳ dòng nào.
> KHÔNG commit `apply.py`, `GUIDE.md`, `pr-body.md` - chúng chỉ nằm trong gói tải về.

## Các bước

```bash
# Terminal Git Bash (Windows) / Terminal (macOS, Linux)
cd ~/Documents/code/univ/G9_AI66A_SE
PKG=~/Documents/code/univ/G9_AI66A_SE/document_nguyenkhacthu/sprint02/packages/44-database-schema-seed   # thư mục chứa gói này
PY=python          # macOS/Linux: nếu lệnh python không có thì đổi thành PY=python3
git checkout main
git pull origin main
git checkout -b 44-database-schema-seed
```

Kéo thẻ #44 trên board sang **In Progress**.


```bash
mkdir -p "$(dirname src/schema.py)" && cp "$PKG/files/src/schema.py" src/schema.py
```

**Commit 1** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add src/schema.py
git commit -m "feat: add database schema for seven tables" \
  -m "user, venue, pricing_rule, blocked_slot, booking, booking_slot, review. Each CHECK and UNIQUE names the business rule it enforces; UNIQUE (venue_id, slot_start) on booking_slot makes a double booking impossible (BR11). Kept in a .py file because CI rejects committed *.sql files." \
  -m "Refs #44"
```

```bash
mkdir -p "$(dirname data/venues.csv)" && cp "$PKG/files/data/venues.csv" data/venues.csv
mkdir -p "$(dirname src/init_db.py)" && cp "$PKG/files/src/init_db.py" src/init_db.py
```

**Commit 2** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add data/venues.csv src/init_db.py
git commit -m "feat: seed 24 venues, 6 users and 5 bookings" \
  -m "python src/init_db.py drops and recreates every table, so it is safe to run twice. Peak-hour bookings are priced per segment (BR12)." \
  -m "Refs #44"
```

```bash
mkdir -p "$(dirname tests/conftest.py)" && cp "$PKG/files/tests/conftest.py" tests/conftest.py
mkdir -p "$(dirname tests/test_schema.py)" && cp "$PKG/files/tests/test_schema.py" tests/test_schema.py
```

Tạo môi trường Python nếu chưa có, rồi chạy - phải thấy `venue 24 rows` và `10 passed`:

```bash
[ -d .venv ] || $PY -m venv .venv
source .venv/bin/activate   # Windows Git Bash: source .venv/Scripts/activate
pip install -r requirements.txt
[ -f .env ] || cp .env.example .env
python src/init_db.py
pytest
```

**Commit 3** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add tests/conftest.py tests/test_schema.py
git commit -m "test: check the schema rejects rows that break a business rule" \
  -m "Duplicate email (BR1), bad phone (BR3), the same hour booked twice (BR11), name and price limits (BR13), rating outside 1-5 (BR18), and per-segment pricing (BR12)." \
  -m "Refs #44"
```

```bash
mkdir -p "$(dirname docs/images/erd.png)" && cp "$PKG/files/docs/images/erd.png" docs/images/erd.png
```

```bash
$PY "$PKG/apply.py" replace docs/design.md "## 2." "$PKG/snippets/design-2-data-model.md"
```

**Commit 4** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add docs/design.md docs/images/erd.png
git commit -m "docs: write design section 2 - data model and ERD" \
  -m "ERD image plus one row per table: purpose, columns and types, PK, FK, and the business rule each constraint enforces. The ERD and the table agree." \
  -m "Closes #44"
```

Kiểm tra lần cuối rồi đẩy lên và mở PR:

```bash
git status                  # phải sạch, không còn file lạ (KHÔNG commit apply.py, .env, data/venues.db)
git log --oneline -5
git push -u origin 44-database-schema-seed
gh pr create --base main --head 44-database-schema-seed \
  --title "[#44] Add database schema, ERD and seed data" \
  --body-file "$PKG/pr-body.md" \
  --reviewer htngochan2802 --assignee @me
```

Thẻ tự sang **In Review**. Nhắn @htngochan2802 vào review. Khi đã được **Approve** và CI xanh:

```bash
gh pr merge --merge --delete-branch
git checkout main && git pull origin main
```

