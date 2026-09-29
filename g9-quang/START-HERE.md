# Gói Sprint 2 của @lequangk2006-sys (Le Quang)

Giải nén gói này vào **`~/Downloads/g9-quang/`** (đúng tên này, vì các lệnh dùng đường dẫn đó).
Hướng dẫn cài đặt Antigravity, Git, GitHub CLI, Python, kết nối GitHub: xem **`Huong-dan-Sprint2-nhom.pdf`** ngay trong gói này (chương 4-5). Làm xong phần cài đặt mới bắt đầu issue.

## Việc của bạn

| Issue | Việc | Khi nào | Mở file |
|---|---|---|---|
| #49 | [Task] Traceability: Story, Screen, Endpoint, Table | 30/09, sau khi #44 và #47 merge | `49-traceability-endpoints-tables/GUIDE.md` |

Mở từng `GUIDE.md` và chạy lệnh theo đúng thứ tự trong đó.

## Review bạn phải làm (bắt buộc, chiếm 15% hệ số cá nhân)

| PR của issue | Việc | Câu hỏi gợi ý (tiếng Anh, sửa theo ý bạn) |
|---|---|---|
| #46 | [Task] Design doc: architecture diagram and design decisions (của @htngochan2802) | `ADR 3 says we move to PostgreSQL if the Sprint 4 concurrency test fails - which issue will hold that test, and who owns it?` |
| #51 | [Chore] Sprint 2 wrap-up (của @peng543) | `Velocity counts only merged issues - is any Sprint 2 issue carried over, and is it labelled `carried-over` on the board?` |

Cách review:

```bash
gh pr list --search "review-requested:@me"     # xem PR đang chờ bạn
gh pr checkout <số-PR>                          # lấy code về máy để chạy thử (nếu là PR code)
```

Rồi trên web: mở PR → tab **Files changed** → bấm vào một dòng cụ thể, viết câu hỏi (tiếng Anh) →
**Review changes** → chọn **Approve** (hoặc Request changes) → **Submit review**.
Không bấm "ok" suông, không comment ở ô cuối trang - như thế **không được tính là review**.
Xong thì `git checkout main`.
