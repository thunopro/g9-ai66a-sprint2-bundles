# #49 [Task] Traceability: Story, Screen, Endpoint, Table

- **Người làm:** @lequangk2006-sys (Le Quang)
- **Reviewer:** @htngochan2802 (Hoang Thi Ngoc Han)
- **Branch:** `49-traceability-endpoints-tables`
- **Phải chờ merge trước:** #44, #47
- **Khi nào làm:** 30/09, sau khi #44 và #47 merge

> Mọi thứ lên GitHub (commit, PR, comment) đều bằng **tiếng Anh** - lệnh bên dưới đã viết sẵn.
> Đọc hiểu từng file trước khi commit: thầy có thể hỏi bất kỳ dòng nào.
> KHÔNG commit `apply.py`, `GUIDE.md`, `pr-body.md` - chúng chỉ nằm trong gói tải về.

## Các bước

```bash
# Terminal Git Bash (Windows) / Terminal (macOS, Linux)
cd ~/G9_AI66A_SE
PKG=~/Downloads/g9-quang/49-traceability-endpoints-tables   # thư mục chứa gói này
PY=python          # macOS/Linux: nếu lệnh python không có thì đổi thành PY=python3
git checkout main
git pull origin main
git checkout -b 49-traceability-endpoints-tables
```

Kéo thẻ #49 trên board sang **In Progress**.


```bash
$PY "$PKG/apply.py" insert-before docs/traceability.md "## Business rules" "$PKG/snippets/traceability-part-1.md"
```

**Commit 1** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add docs/traceability.md
git commit -m "docs: trace US01-US03 to their screens, endpoints and tables" \
  -m "Refs #49"
```

```bash
$PY "$PKG/apply.py" replace docs/traceability.md "## Story → Screen → Endpoint → Table" "$PKG/snippets/traceability-story-endpoint-table.md"
```

Tự kiểm tra: mỗi endpoint trong bảng mới đều có trong design.md mục 3:

```bash
grep -n "POST /api/auth/register\|GET /api/venues\|POST /api/bookings\|POST /api/owner/venues" docs/design.md | head
```

**Commit 2** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add docs/traceability.md
git commit -m "docs: trace US04-US06 to their screens, endpoints and tables" \
  -m "One row per P0 story (US01-US06). Endpoints are copied from design.md section 3 and tables from section 2." \
  -m "Closes #49"
```

Kiểm tra lần cuối rồi đẩy lên và mở PR:

```bash
git status                  # phải sạch, không còn file lạ (KHÔNG commit apply.py, .env, data/venues.db)
git log --oneline -5
git push -u origin 49-traceability-endpoints-tables
gh pr create --base main --head 49-traceability-endpoints-tables \
  --title "[#49] Trace each P0 story to its screen, endpoints and tables" \
  --body-file "$PKG/pr-body.md" \
  --reviewer htngochan2802 --assignee @me
```

Thẻ tự sang **In Review**. Nhắn @htngochan2802 vào review. Khi đã được **Approve** và CI xanh:

```bash
gh pr merge --merge --delete-branch
git checkout main && git pull origin main
```

