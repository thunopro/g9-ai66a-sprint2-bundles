# Gói Sprint 2 của @thunopro (Nguyen Khac Thu)

Giải nén gói này vào **`~/Downloads/g9-thu/`** (đúng tên này, vì các lệnh dùng đường dẫn đó).
Hướng dẫn cài đặt Antigravity, Git, GitHub CLI, Python, kết nối GitHub: xem **`Huong-dan-Sprint2-nhom.pdf`** ngay trong gói này (chương 4-5). Làm xong phần cài đặt mới bắt đầu issue.

## Việc của bạn

| Issue | Việc | Khi nào | Mở file |
|---|---|---|---|
| #42 | [Chore] Refine backlog for Sprint 2 | Ngay bây giờ (27/09) | `42-refine-backlog-sprint-2/GUIDE.md` |
| #44 | [Task] Create database schema, ERD and seed 24 venues | 29/09, sau khi #43 merge | `44-database-schema-seed/GUIDE.md` |
| #50 | [Task] Design doc: what changed since M1 and Milestone 2 submission | 02/10, sau khi #44-#47 merge | `50-m2-design-document/GUIDE.md` |

Mở từng `GUIDE.md` và chạy lệnh theo đúng thứ tự trong đó.

## Review bạn phải làm (bắt buộc, chiếm 15% hệ số cá nhân)

| PR của issue | Việc | Câu hỏi gợi ý (tiếng Anh, sửa theo ý bạn) |
|---|---|---|
| #43 | [Task] Set up Flask project skeleton and CI tests (của @peng543) | `Why pin Flask as `>=3.0,<4` instead of an exact version - could a new 3.x release break the instructor's install on review day?` |
| #47 | [Task] Design doc: API design (của @htngochan2802) | `Row 6 returns 409 when a slot was just taken but 422 when the slot is blocked - why two codes for what the customer sees as the same problem?` |

Cách review:

```bash
gh pr list --search "review-requested:@me"     # xem PR đang chờ bạn
gh pr checkout <số-PR>                          # lấy code về máy để chạy thử (nếu là PR code)
```

Rồi trên web: mở PR → tab **Files changed** → bấm vào một dòng cụ thể, viết câu hỏi (tiếng Anh) →
**Review changes** → chọn **Approve** (hoặc Request changes) → **Submit review**.
Không bấm "ok" suông, không comment ở ô cuối trang - như thế **không được tính là review**.
Xong thì `git checkout main`.
