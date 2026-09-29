# #48 [Task] Write docs/SETUP.md and test it on a clean machine

- **Người làm:** @PhunghoaAI (Nguyen Phung Hoa)
- **Reviewer:** @peng543 (Nguyen Khoi Nguyen)
- **Branch:** `48-setup-guide`
- **Phải chờ merge trước:** #45
- **Khi nào làm:** 01/10, sau khi #45 merge

> Mọi thứ lên GitHub (commit, PR, comment) đều bằng **tiếng Anh** - lệnh bên dưới đã viết sẵn.
> Đọc hiểu từng file trước khi commit: thầy có thể hỏi bất kỳ dòng nào.
> KHÔNG commit `apply.py`, `GUIDE.md`, `pr-body.md` - chúng chỉ nằm trong gói tải về.

## Các bước

```bash
# Terminal Git Bash (Windows) / Terminal (macOS, Linux)
cd ~/G9_AI66A_SE
PKG=~/Downloads/g9-hoa/48-setup-guide   # thư mục chứa gói này
PY=python          # macOS/Linux: nếu lệnh python không có thì đổi thành PY=python3
git checkout main
git pull origin main
git checkout -b 48-setup-guide
```

Kéo thẻ #48 trên board sang **In Progress**.


```bash
mkdir -p "$(dirname docs/SETUP.md)" && cp "$PKG/files/docs/SETUP.md" docs/SETUP.md
```

**Commit 1** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add docs/SETUP.md
git commit -m "docs: add SETUP.md for a clean machine" \
  -m "Prerequisites with versions, commands for Windows and macOS/Linux, configuration, one command to create and seed the database, how to know it worked, and five troubleshooting entries." \
  -m "Refs #48"
```

```bash
$PY "$PKG/apply.py" replace README.md "## Setup" "$PKG/snippets/readme-setup.md"
```

```bash
$PY "$PKG/apply.py" replace README.md "## Project board" "$PKG/snippets/readme-setup-link.md"
```

**Commit 2** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add README.md
git commit -m "docs: link SETUP.md from the first screen of README" \
  -m "Refs #48"
```

Bắt buộc: người test phải ở nhóm khác, trên máy không phải của bạn:

```bash
# Nhờ 1 bạn NHÓM KHÁC clone repo trên máy của họ và làm theo docs/SETUP.md từng chữ.
# Bấm giờ. Sửa SETUP.md nếu bạn ấy bị vướng chỗ nào.
# Điền dòng 'Tested by' ở cuối docs/SETUP.md: tên GitHub, hệ điều hành, ngày, số phút.
```

**Commit 3** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add docs/SETUP.md
git commit -m "docs: record who tested SETUP.md on a clean machine" \
  -m "Closes #48"
```

Kiểm tra lần cuối rồi đẩy lên và mở PR:

```bash
git status                  # phải sạch, không còn file lạ (KHÔNG commit apply.py, .env, data/venues.db)
git log --oneline -5
git push -u origin 48-setup-guide
gh pr create --base main --head 48-setup-guide \
  --title "[#48] Add SETUP.md and link it from README" \
  --body-file "$PKG/pr-body.md" \
  --reviewer peng543 --assignee @me
```

Thẻ tự sang **In Review**. Nhắn @peng543 vào review. Khi đã được **Approve** và CI xanh:

```bash
gh pr merge --merge --delete-branch
git checkout main && git pull origin main
```

