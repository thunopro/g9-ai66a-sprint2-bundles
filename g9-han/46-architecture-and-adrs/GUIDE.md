# #46 [Task] Design doc: architecture diagram and design decisions

- **Người làm:** @htngochan2802 (Hoang Thi Ngoc Han)
- **Reviewer:** @lequangk2006-sys (Le Quang)
- **Branch:** `46-architecture-and-adrs`
- **Phải chờ merge trước:** #42
- **Khi nào làm:** 28/09, ngay sau khi #42 merge (không cần chờ code)

> Mọi thứ lên GitHub (commit, PR, comment) đều bằng **tiếng Anh** - lệnh bên dưới đã viết sẵn.
> Đọc hiểu từng file trước khi commit: thầy có thể hỏi bất kỳ dòng nào.
> KHÔNG commit `apply.py`, `GUIDE.md`, `pr-body.md` - chúng chỉ nằm trong gói tải về.

## Các bước

```bash
# Terminal Git Bash (Windows) / Terminal (macOS, Linux)
cd ~/G9_AI66A_SE
PKG=~/Downloads/g9-han/46-architecture-and-adrs   # thư mục chứa gói này
PY=python          # macOS/Linux: nếu lệnh python không có thì đổi thành PY=python3
git checkout main
git pull origin main
git checkout -b 46-architecture-and-adrs
```

Kéo thẻ #46 trên board sang **In Progress**.


```bash
mkdir -p "$(dirname docs/images/architecture.png)" && cp "$PKG/files/docs/images/architecture.png" docs/images/architecture.png
```

```bash
$PY "$PKG/apply.py" replace docs/design.md "## 1." "$PKG/snippets/design-1-architecture.md"
```

**Commit 1** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add docs/design.md docs/images/architecture.png
git commit -m "docs: write design section 1 - architecture" \
  -m "Container diagram with six components and every arrow labelled with what travels on it, plus a table of technology, location and responsibility per component." \
  -m "Refs #46"
```

```bash
$PY "$PKG/apply.py" replace docs/design.md "## 5." "$PKG/snippets/design-5-adr-1-2.md"
```

**Commit 2** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add docs/design.md
git commit -m "docs: add ADR 1 and ADR 2 - web framework and double-booking prevention" \
  -m "ADR 1: Flask vs FastAPI+React vs Express. ADR 2: how BR11 is enforced - check in code vs UNIQUE on booking vs one booking_slot row per hour." \
  -m "Refs #46"
```

```bash
$PY "$PKG/apply.py" replace docs/design.md "## 5." "$PKG/snippets/design-5-design-decisions.md"
```

**Commit 3** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add docs/design.md
git commit -m "docs: add ADR 3 - SQLite vs PostgreSQL vs MySQL" \
  -m "Each ADR now lists the options, the choice, why, and what would change our mind." \
  -m "Closes #46"
```

Kiểm tra lần cuối rồi đẩy lên và mở PR:

```bash
git status                  # phải sạch, không còn file lạ (KHÔNG commit apply.py, .env, data/venues.db)
git log --oneline -5
git push -u origin 46-architecture-and-adrs
gh pr create --base main --head 46-architecture-and-adrs \
  --title "[#46] Write design sections 1 and 5 - architecture and ADRs" \
  --body-file "$PKG/pr-body.md" \
  --reviewer lequangk2006-sys --assignee @me
```

Thẻ tự sang **In Review**. Nhắn @lequangk2006-sys vào review. Khi đã được **Approve** và CI xanh:

```bash
gh pr merge --merge --delete-branch
git checkout main && git pull origin main
```

