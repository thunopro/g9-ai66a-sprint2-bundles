# #50 [Task] Design doc: what changed since M1 and Milestone 2 submission

- **Người làm:** @thunopro (Nguyen Khac Thu)
- **Reviewer:** @PhunghoaAI (Nguyen Phung Hoa)
- **Branch:** `50-m2-design-document`
- **Phải chờ merge trước:** #44, #45, #46, #47
- **Khi nào làm:** 02/10, sau khi #44-#47 merge

> Mọi thứ lên GitHub (commit, PR, comment) đều bằng **tiếng Anh** - lệnh bên dưới đã viết sẵn.
> Đọc hiểu từng file trước khi commit: thầy có thể hỏi bất kỳ dòng nào.
> KHÔNG commit `apply.py`, `GUIDE.md`, `pr-body.md` - chúng chỉ nằm trong gói tải về.

## Các bước

```bash
# Terminal Git Bash (Windows) / Terminal (macOS, Linux)
cd ~/Documents/code/univ/G9_AI66A_SE
PKG=~/Documents/code/univ/G9_AI66A_SE/document_nguyenkhacthu/sprint02/packages/50-m2-design-document   # thư mục chứa gói này
PY=python          # macOS/Linux: nếu lệnh python không có thì đổi thành PY=python3
git checkout main
git pull origin main
git checkout -b 50-m2-design-document
```

Kéo thẻ #50 trên board sang **In Progress**.


```bash
$PY "$PKG/apply.py" replace docs/design.md "## 6." "$PKG/snippets/design-6-what-changed.md"
```

Phải tự xử lý 2 TODO trước khi commit:

```bash
# Mở docs/design.md, tìm 2 chỗ 'TODO @thunopro' trong mục 6:
#  - xác nhận giới hạn 4 giờ/booking với nhóm
#  - thêm feedback M1 của giảng viên (nếu đã có), rồi xoá dòng TODO
```

**Commit 1** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add docs/design.md
git commit -m "docs: write design section 6 - what changed since M1" \
  -m "Three changes: bookings are 1-4 whole hours (BR11, US05), the owner gives each venue a sport and an area from fixed lists (BR9, US06), and email verification is stubbed for Sprint 2 (BR4)." \
  -m "Refs #50"
```

Sửa BR9, BR11 và thêm tiêu chí 5 cho US05, US06 trong requirements.md, traceability.md cho khớp mục 6:

```bash
$PY "$PKG/update_requirements.py"
```

**Commit 2** (làm xong phần nào commit phần đó, đừng dồn):

```bash
git add docs/requirements.md docs/traceability.md
git commit -m "docs: update BR9, BR11, US05 and US06 to match the design changes" \
  -m "New acceptance criterion 5 in US05 (whole hours, at most 4) and in US06 (sport and area from drop-downs). requirements.md and traceability.md now say the same as design.md section 6." \
  -m "Closes #50"
```

Kiểm tra lần cuối rồi đẩy lên và mở PR:

```bash
git status                  # phải sạch, không còn file lạ (KHÔNG commit apply.py, .env, data/venues.db)
git log --oneline -5
git push -u origin 50-m2-design-document
gh pr create --base main --head 50-m2-design-document \
  --title "[#50] Write design section 6 and finalise the Milestone 2 document" \
  --body-file "$PKG/pr-body.md" \
  --reviewer PhunghoaAI --assignee @me
```

Thẻ tự sang **In Review**. Nhắn @PhunghoaAI vào review. Khi đã được **Approve** và CI xanh:

```bash
gh pr merge --merge --delete-branch
git checkout main && git pull origin main
```

