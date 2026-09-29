# Gói Sprint 2 của @htngochan2802 (Hoang Thi Ngoc Han)

Giải nén gói này vào **`~/Downloads/g9-han/`** (đúng tên này, vì các lệnh dùng đường dẫn đó).
Hướng dẫn cài đặt Antigravity, Git, GitHub CLI, Python, kết nối GitHub: xem **`Huong-dan-Sprint2-nhom.pdf`** ngay trong gói này (chương 4-5). Làm xong phần cài đặt mới bắt đầu issue.

## Việc của bạn

| Issue | Việc | Khi nào | Mở file |
|---|---|---|---|
| #46 | [Task] Design doc: architecture diagram and design decisions | 28/09, ngay sau khi #42 merge (không cần chờ code) | `46-architecture-and-adrs/GUIDE.md` |
| #47 | [Task] Design doc: API design | 29/09, sau khi #42 merge (không cần chờ code) | `47-api-design/GUIDE.md` |

Mở từng `GUIDE.md` và chạy lệnh theo đúng thứ tự trong đó.

## Review bạn phải làm (bắt buộc, chiếm 15% hệ số cá nhân)

| PR của issue | Việc | Câu hỏi gợi ý (tiếng Anh, sửa theo ý bạn) |
|---|---|---|
| #44 | [Task] Create database schema, ERD and seed 24 venues (của @thunopro) | `A cancelled booking deletes its booking_slot rows - is there a test showing the hour becomes free again, or only the design text saying so?` |
| #49 | [Task] Traceability: Story, Screen, Endpoint, Table (của @lequangk2006-sys) | `US03 lists both `GET /search` and `GET /api/venues` - should the row say which one the walking skeleton actually uses today?` |

Cách review:

```bash
gh pr list --search "review-requested:@me"     # xem PR đang chờ bạn
gh pr checkout <số-PR>                          # lấy code về máy để chạy thử (nếu là PR code)
```

Rồi trên web: mở PR → tab **Files changed** → bấm vào một dòng cụ thể, viết câu hỏi (tiếng Anh) →
**Review changes** → chọn **Approve** (hoặc Request changes) → **Submit review**.
Không bấm "ok" suông, không comment ở ô cuối trang - như thế **không được tính là review**.
Xong thì `git checkout main`.
