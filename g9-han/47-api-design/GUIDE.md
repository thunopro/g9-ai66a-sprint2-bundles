# #47 [Task] Design doc: API design

- **Người làm:** @htngochan2802 (Hoang Thi Ngoc Han)
- **Reviewer:** @thunopro (Nguyen Khac Thu)
- **Branch:** `47-api-design`
- **Phải chờ merge trước:** #42
- **Khi nào làm:** 29/09, sau khi #42 merge (không cần chờ code)

> Mọi thứ lên GitHub (commit, PR, comment) đều bằng **tiếng Anh** - lệnh bên dưới đã viết sẵn.
> Đọc hiểu từng file trước khi commit: thầy có thể hỏi bất kỳ dòng nào.
> KHÔNG commit `apply.py`, `GUIDE.md`, `pr-body.md` - chúng chỉ nằm trong gói tải về.

## Các bước

```bash
# Terminal Git Bash (Windows) / Terminal (macOS, Linux)
cd ~/G9_AI66A_SE
PKG=~/Downloads/g9-han/47-api-design   # thư mục chứa gói này
PY=python          # macOS/Linux: nếu lệnh python không có thì đổi thành PY=python3
git checkout main
git pull origin main
git checkout -b 47-api-design
```

Kéo thẻ #47 trên board sang **In Progress**.


```bash
$PY "$PKG/apply.py" replace docs/design.md "## 3." "$PKG/snippets/design-3-api-auth.md"
```

**Commit 1** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add docs/design.md
git commit -m "docs: add API conventions and the authentication endpoints" \
  -m "Error format, how the session cookie works, what 401 and 403 mean, and endpoints 1-3 for US01 and US02 with their error codes (BR1-BR6)." \
  -m "Refs #47"
```

```bash
$PY "$PKG/apply.py" replace docs/design.md "## 3." "$PKG/snippets/design-3-api-p0.md"
```

**Commit 2** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add docs/design.md
git commit -m "docs: add API endpoints for search, venue detail, booking and add venue" \
  -m "Endpoints 4-7 complete the P0 stories US03-US06; error messages are copied from the acceptance criteria." \
  -m "Refs #47"
```

```bash
$PY "$PKG/apply.py" replace docs/design.md "## 3." "$PKG/snippets/design-3-api-design.md"
```

**Commit 3** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add docs/design.md
git commit -m "docs: add API endpoints for the P1 and P2 stories" \
  -m "Endpoints 8-14 cover booking history, cancellation, blocking, the owner booking list, pricing and reviews, so Sprint 3 does not redesign the API." \
  -m "Closes #47"
```

Kiểm tra lần cuối rồi đẩy lên và mở PR:

```bash
git status                  # phải sạch, không còn file lạ (KHÔNG commit apply.py, .env, data/venues.db)
git log --oneline -5
git push -u origin 47-api-design
gh pr create --base main --head 47-api-design \
  --title "[#47] Write design section 3 - API design" \
  --body-file "$PKG/pr-body.md" \
  --reviewer thunopro --assignee @me
```

Thẻ tự sang **In Review**. Nhắn @thunopro vào review. Khi đã được **Approve** và CI xanh:

```bash
gh pr merge --merge --delete-branch
git checkout main && git pull origin main
```

