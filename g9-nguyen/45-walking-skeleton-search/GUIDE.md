# #45 [Task] Walking skeleton: /search reads venues from the database

- **Người làm:** @peng543 (Nguyen Khoi Nguyen)
- **Reviewer:** @PhunghoaAI (Nguyen Phung Hoa)
- **Branch:** `45-walking-skeleton-search`
- **Phải chờ merge trước:** #44
- **Khi nào làm:** 30/09, sau khi #44 merge

> Mọi thứ lên GitHub (commit, PR, comment) đều bằng **tiếng Anh** - lệnh bên dưới đã viết sẵn.
> Đọc hiểu từng file trước khi commit: thầy có thể hỏi bất kỳ dòng nào.
> KHÔNG commit `apply.py`, `GUIDE.md`, `pr-body.md` - chúng chỉ nằm trong gói tải về.

## Các bước

```bash
# Terminal Git Bash (Windows) / Terminal (macOS, Linux)
cd ~/G9_AI66A_SE
PKG=~/Downloads/g9-nguyen/45-walking-skeleton-search   # thư mục chứa gói này
PY=python          # macOS/Linux: nếu lệnh python không có thì đổi thành PY=python3
git checkout main
git pull origin main
git checkout -b 45-walking-skeleton-search
```

Kéo thẻ #45 trên board sang **In Progress**.


```bash
mkdir -p "$(dirname src/app.py)" && cp "$PKG/files/src/app.py" src/app.py
mkdir -p "$(dirname src/templates/search.html)" && cp "$PKG/files/src/templates/search.html" src/templates/search.html
```

**Commit 1** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add src/app.py src/templates/search.html
git commit -m "feat: add /search page reading venues from SQLite" \
  -m "GET /search (also /) filters by sport and area with bound parameters; both must match (BR9) and no match shows 'No venues found'. /health now reports the venue count." \
  -m "Refs #45"
```

```bash
mkdir -p "$(dirname tests/test_search.py)" && cp "$PKG/files/tests/test_search.py" tests/test_search.py
mkdir -p "$(dirname tests/test_health.py)" && cp "$PKG/files/tests/test_health.py" tests/test_health.py
```

Phải ra `15 passed`:

```bash
[ -d .venv ] || $PY -m venv .venv
source .venv/bin/activate   # Windows Git Bash: source .venv/Scripts/activate
pip install -r requirements.txt
[ -f .env ] || cp .env.example .env
python src/init_db.py
pytest
```

**Commit 2** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add tests/test_search.py tests/test_health.py
git commit -m "test: cover /search filters and data read at request time" \
  -m "Includes a test that inserts a venue after start-up and finds it on the page - an array in the code could never pass it." \
  -m "Refs #45"
```

Mở http://localhost:5000/search trên trình duyệt THẬT, chụp màn hình THẤY THANH ĐỊA CHỈ, lưu đè vào docs/images/walking-skeleton.png (ảnh trong gói chỉ là ảnh tạm). Ctrl+C để tắt.:

```bash
python src/app.py
```

```bash
mkdir -p "$(dirname docs/images/walking-skeleton.png)" && cp "$PKG/files/docs/images/walking-skeleton.png" docs/images/walking-skeleton.png
```

```bash
$PY "$PKG/apply.py" replace docs/design.md "## 4." "$PKG/snippets/design-4-walking-skeleton.md"
```

Đổi trạng thái `/search` trong traceability thành In progress:

```bash
sed -i.bak 's/^\(| `\/search` .*\)| Spec done |$/\1| In progress |/' docs/traceability.md && rm docs/traceability.md.bak
```

**Commit 3** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add docs/design.md docs/images/walking-skeleton.png docs/traceability.md
git commit -m "docs: write design section 4 - walking skeleton" \
  -m "Route, table, row count, the SQL behind the page and a screenshot of it running. /search moves to In progress in docs/traceability.md." \
  -m "Closes #45"
```

Kiểm tra lần cuối rồi đẩy lên và mở PR:

```bash
git status                  # phải sạch, không còn file lạ (KHÔNG commit apply.py, .env, data/venues.db)
git log --oneline -5
git push -u origin 45-walking-skeleton-search
gh pr create --base main --head 45-walking-skeleton-search \
  --title "[#45] Add /search walking skeleton reading from SQLite" \
  --body-file "$PKG/pr-body.md" \
  --reviewer PhunghoaAI --assignee @me
```

Thẻ tự sang **In Review**. Nhắn @PhunghoaAI vào review. Khi đã được **Approve** và CI xanh:

```bash
gh pr merge --merge --delete-branch
git checkout main && git pull origin main
```

