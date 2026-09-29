# #42 [Chore] Refine backlog for Sprint 2

- **Người làm:** @thunopro (Nguyen Khac Thu)
- **Reviewer:** @peng543 (Nguyen Khoi Nguyen)
- **Branch:** `42-refine-backlog-sprint-2`
- **Phải chờ merge trước:** không
- **Khi nào làm:** Ngay bây giờ (27/09)

> Mọi thứ lên GitHub (commit, PR, comment) đều bằng **tiếng Anh** - lệnh bên dưới đã viết sẵn.
> Đọc hiểu từng file trước khi commit: thầy có thể hỏi bất kỳ dòng nào.
> KHÔNG commit `apply.py`, `GUIDE.md`, `pr-body.md` - chúng chỉ nằm trong gói tải về.

## Các bước

```bash
# Terminal Git Bash (Windows) / Terminal (macOS, Linux)
cd ~/Documents/code/univ/G9_AI66A_SE
PKG=~/Documents/code/univ/G9_AI66A_SE/document_nguyenkhacthu/sprint02/packages/42-refine-backlog-sprint-2   # thư mục chứa gói này
PY=python          # macOS/Linux: nếu lệnh python không có thì đổi thành PY=python3
git checkout main
git pull origin main
git checkout -b 42-refine-backlog-sprint-2
```

Kéo thẻ #42 trên board sang **In Progress**.


PR này có file trong .github/workflows/ nên token gh cần quyền `workflow` (làm 1 lần, mở trình duyệt xác nhận). Thiếu bước này push sẽ bị từ chối:

```bash
gh auth refresh -h github.com -s workflow
```

```bash
mkdir -p "$(dirname .github/workflows/board-in-review.yml)" && cp "$PKG/files/.github/workflows/board-in-review.yml" .github/workflows/board-in-review.yml
```

**Commit 1** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add .gitignore .github/workflows/board-in-review.yml
git commit -m "chore: add board In Review workflow and ignore the Sprint 2 brief" \
  -m "The workflow moves a card to In Review when its pull request opens; it was missing since Sprint 1 (see retro). The Sprint 2 brief stays out of the repository like the Sprint 1 one." \
  -m "Refs #42"
```

```bash
mkdir -p "$(dirname docs/backlog.md)" && cp "$PKG/files/docs/backlog.md" docs/backlog.md
```

**Commit 2** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add docs/backlog.md
git commit -m "docs: add Sprint 2 backlog with owners, points and order" \
  -m "10 issues, 22 points committed, the critical path #43 -> #44 -> #45, and the business-rule range for each member (Sprint 1 retro action)." \
  -m "Refs #42"
```

```bash
mkdir -p "$(dirname docs/design.md)" && cp "$PKG/files/docs/design.md" docs/design.md
```

**Commit 3** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add docs/design.md
git commit -m "docs: add design.md skeleton with one owner per section" \
  -m "Six headings in the order the brief asks for, each naming its owner and issue, so every member fills their own section in their own pull request without merge conflicts." \
  -m "Refs #42"
```

```bash
mkdir -p "$(dirname README.md)" && cp "$PKG/files/README.md" README.md
```

**Commit 4** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add README.md
git commit -m "docs: name the Sprint 2 Scrum Master and the English-only rule" \
  -m "Scrum Master for Sprint 2 is @peng543. Branch names now follow the course convention <issue>-<slug>, and everything on GitHub is written in English." \
  -m "Closes #42"
```

Kiểm tra lần cuối rồi đẩy lên và mở PR:

```bash
git status                  # phải sạch, không còn file lạ (KHÔNG commit apply.py, .env, data/venues.db)
git log --oneline -5
git push -u origin 42-refine-backlog-sprint-2
gh pr create --base main --head 42-refine-backlog-sprint-2 \
  --title "[#42] Plan Sprint 2 backlog and design.md skeleton" \
  --body-file "$PKG/pr-body.md" \
  --reviewer peng543 --assignee @me
```

Thẻ tự sang **In Review**. Nhắn @peng543 vào review. Khi đã được **Approve** và CI xanh:

```bash
gh pr merge --merge --delete-branch
git checkout main && git pull origin main
```

