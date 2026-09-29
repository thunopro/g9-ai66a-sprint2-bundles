# #51 [Chore] Sprint 2 wrap-up

- **Người làm:** @peng543 (Nguyen Khoi Nguyen)
- **Reviewer:** @lequangk2006-sys (Le Quang)
- **Branch:** `51-sprint-2-wrap-up`
- **Phải chờ merge trước:** #48, #49, #50
- **Khi nào làm:** 03/10, sau Sprint Review và Retro

> Mọi thứ lên GitHub (commit, PR, comment) đều bằng **tiếng Anh** - lệnh bên dưới đã viết sẵn.
> Đọc hiểu từng file trước khi commit: thầy có thể hỏi bất kỳ dòng nào.
> KHÔNG commit `apply.py`, `GUIDE.md`, `pr-body.md` - chúng chỉ nằm trong gói tải về.

## Các bước

```bash
# Terminal Git Bash (Windows) / Terminal (macOS, Linux)
cd ~/G9_AI66A_SE
PKG=~/Downloads/g9-nguyen/51-sprint-2-wrap-up   # thư mục chứa gói này
PY=python          # macOS/Linux: nếu lệnh python không có thì đổi thành PY=python3
git checkout main
git pull origin main
git checkout -b 51-sprint-2-wrap-up
```

Kéo thẻ #51 trên board sang **In Progress**.


```bash
$PY "$PKG/apply.py" replace docs/sprint-log.md "## Sprint 2" "$PKG/snippets/sprint-log-sprint-2.md"
```

Số liệu phải là số thật trên board:

```bash
# Mở docs/sprint-log.md, điền mọi chỗ TODO và <n>/<pr>: số PR thật, velocity,
# nội dung Sprint Review, điểm danh, SM Sprint 3. Xoá các dòng TODO.
```

**Commit 1** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add docs/sprint-log.md
git commit -m "docs: record Sprint 2 committed, completed and velocity" \
  -m "Refs #51"
```

```bash
$PY "$PKG/apply.py" replace docs/retro.md "## Sprint 2" "$PKG/snippets/retro-sprint-2.md"
```

```bash
# Mở docs/retro.md, điền Keep/Stop/Try từ buổi retro và ĐÚNG 1 action có 1 owner.
```

**Commit 2** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add docs/retro.md
git commit -m "docs: add Sprint 2 retrospective with one action and one owner" \
  -m "Closes #51"
```

Kiểm tra lần cuối rồi đẩy lên và mở PR:

```bash
git status                  # phải sạch, không còn file lạ (KHÔNG commit apply.py, .env, data/venues.db)
git log --oneline -5
git push -u origin 51-sprint-2-wrap-up
gh pr create --base main --head 51-sprint-2-wrap-up \
  --title "[#51] Record Sprint 2 results, review and retrospective" \
  --body-file "$PKG/pr-body.md" \
  --reviewer lequangk2006-sys --assignee @me
```

Thẻ tự sang **In Review**. Nhắn @lequangk2006-sys vào review. Khi đã được **Approve** và CI xanh:

```bash
gh pr merge --merge --delete-branch
git checkout main && git pull origin main
```

