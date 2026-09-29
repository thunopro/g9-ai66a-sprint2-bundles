# #43 [Task] Set up Flask project skeleton and CI tests

- **Người làm:** @peng543 (Nguyen Khoi Nguyen)
- **Reviewer:** @thunopro (Nguyen Khac Thu)
- **Branch:** `43-flask-project-skeleton`
- **Phải chờ merge trước:** #42
- **Khi nào làm:** 28/09, ngay sau khi #42 merge

> Mọi thứ lên GitHub (commit, PR, comment) đều bằng **tiếng Anh** - lệnh bên dưới đã viết sẵn.
> Đọc hiểu từng file trước khi commit: thầy có thể hỏi bất kỳ dòng nào.
> KHÔNG commit `apply.py`, `GUIDE.md`, `pr-body.md` - chúng chỉ nằm trong gói tải về.

## Các bước

```bash
# Terminal Git Bash (Windows) / Terminal (macOS, Linux)
cd ~/G9_AI66A_SE
PKG=~/Downloads/g9-nguyen/43-flask-project-skeleton   # thư mục chứa gói này
PY=python          # macOS/Linux: nếu lệnh python không có thì đổi thành PY=python3
git checkout main
git pull origin main
git checkout -b 43-flask-project-skeleton
```

Kéo thẻ #43 trên board sang **In Progress**.


```bash
mkdir -p "$(dirname requirements.txt)" && cp "$PKG/files/requirements.txt" requirements.txt
mkdir -p "$(dirname .env.example)" && cp "$PKG/files/.env.example" .env.example
```

**Commit 1** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add requirements.txt .env.example
git commit -m "chore: add Python dependencies and .env.example" \
  -m "Flask 3, python-dotenv and pytest. .env.example documents PORT, DATABASE_PATH and SECRET_KEY; the real .env is git-ignored." \
  -m "Refs #43"
```

```bash
mkdir -p "$(dirname src/db.py)" && cp "$PKG/files/src/db.py" src/db.py
mkdir -p "$(dirname src/app.py)" && cp "$PKG/files/src/app.py" src/app.py
```

**Commit 2** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add src/db.py src/app.py
git commit -m "feat: add Flask app factory and /health route" \
  -m "create_app() lets tests build the app against a temporary database. db.connect() switches on SQLite foreign keys for every connection." \
  -m "Refs #43"
```

```bash
mkdir -p "$(dirname pytest.ini)" && cp "$PKG/files/pytest.ini" pytest.ini
mkdir -p "$(dirname tests/test_health.py)" && cp "$PKG/files/tests/test_health.py" tests/test_health.py
```

Tạo môi trường Python và chạy test - phải ra `1 passed`:

```bash
python -m venv .venv && source .venv/bin/activate   # Windows Git Bash: source .venv/Scripts/activate
pip install -r requirements.txt
cp .env.example .env
pytest
```

**Commit 3** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add pytest.ini tests/test_health.py
git commit -m "test: check /health answers ok" \
  -m "CI now has a test to run; a Python project with no tests makes pytest exit with code 5 and CI fail." \
  -m "Closes #43"
```

Kiểm tra lần cuối rồi đẩy lên và mở PR:

```bash
git status                  # phải sạch, không còn file lạ (KHÔNG commit apply.py, .env, data/venues.db)
git log --oneline -5
git push -u origin 43-flask-project-skeleton
gh pr create --base main --head 43-flask-project-skeleton \
  --title "[#43] Set up Flask project skeleton and CI tests" \
  --body-file "$PKG/pr-body.md" \
  --reviewer thunopro --assignee @me
```

Thẻ tự sang **In Review**. Nhắn @thunopro vào review. Khi đã được **Approve** và CI xanh:

```bash
gh pr merge --merge --delete-branch
git checkout main && git pull origin main
```

