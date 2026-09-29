# Gói Sprint 2 của @PhunghoaAI (Nguyen Phung Hoa)

Giải nén gói này vào **`~/Downloads/g9-hoa/`** (đúng tên này, vì các lệnh dùng đường dẫn đó).
Hướng dẫn cài đặt Antigravity, Git, GitHub CLI, Python, kết nối GitHub: xem **`Huong-dan-Sprint2-nhom.pdf`** ngay trong gói này (chương 4-5). Làm xong phần cài đặt mới bắt đầu issue.

## Việc của bạn

| Issue | Việc | Khi nào | Mở file |
|---|---|---|---|
| #48 | [Task] Write docs/SETUP.md and test it on a clean machine | 01/10, sau khi #45 merge | `48-setup-guide/GUIDE.md` |

Mở từng `GUIDE.md` và chạy lệnh theo đúng thứ tự trong đó.

## Review bạn phải làm (bắt buộc, chiếm 15% hệ số cá nhân)

| PR của issue | Việc | Câu hỏi gợi ý (tiếng Anh, sửa theo ý bạn) |
|---|---|---|
| #45 | [Task] Walking skeleton: /search reads venues from the database (của @peng543) | ``:sport = ''` means any sport - what does the page do for an unknown value like `?sport=Golf`, and is there a test for it?` |
| #50 | [Task] Design doc: what changed since M1 and Milestone 2 submission (của @thunopro) | `Change 1 caps a booking at 4 hours - which acceptance criterion in US05 now tests the cap, and should it be added to the story file too?` |

Cách review:

```bash
gh pr list --search "review-requested:@me"     # xem PR đang chờ bạn
gh pr checkout <số-PR>                          # lấy code về máy để chạy thử (nếu là PR code)
```

Rồi trên web: mở PR → tab **Files changed** → bấm vào một dòng cụ thể, viết câu hỏi (tiếng Anh) →
**Review changes** → chọn **Approve** (hoặc Request changes) → **Submit review**.
Không bấm "ok" suông, không comment ở ô cuối trang - như thế **không được tính là review**.
Xong thì `git checkout main`.
