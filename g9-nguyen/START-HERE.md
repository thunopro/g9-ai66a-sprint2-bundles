# Gói Sprint 2 của @peng543 (Nguyen Khoi Nguyen)

Giải nén gói này vào **`~/Downloads/g9-nguyen/`** (đúng tên này, vì các lệnh dùng đường dẫn đó).
Hướng dẫn cài đặt Antigravity, Git, GitHub CLI, Python, kết nối GitHub: xem **`Huong-dan-Sprint2-nhom.pdf`** ngay trong gói này (chương 4-5). Làm xong phần cài đặt mới bắt đầu issue.

## Việc của bạn

| Issue | Việc | Khi nào | Mở file |
|---|---|---|---|
| #43 | [Task] Set up Flask project skeleton and CI tests | 28/09, ngay sau khi #42 merge | `43-flask-project-skeleton/GUIDE.md` |
| #45 | [Task] Walking skeleton: /search reads venues from the database | 30/09, sau khi #44 merge | `45-walking-skeleton-search/GUIDE.md` |
| #51 | [Chore] Sprint 2 wrap-up | 03/10, sau Sprint Review và Retro | `51-sprint-2-wrap-up/GUIDE.md` |

Mở từng `GUIDE.md` và chạy lệnh theo đúng thứ tự trong đó.

## Review bạn phải làm (bắt buộc, chiếm 15% hệ số cá nhân)

| PR của issue | Việc | Câu hỏi gợi ý (tiếng Anh, sửa theo ý bạn) |
|---|---|---|
| #42 | [Chore] Refine backlog for Sprint 2 (của @thunopro) | `Should #49 wait until #47 is merged, or can Quang start from the endpoint list in the issue?` |
| #48 | [Task] Write docs/SETUP.md and test it on a clean machine (của @PhunghoaAI) | `On Windows, typing `python` can open the Microsoft Store instead of Python - should Troubleshooting mention the App execution aliases setting?` |

Cách review:

```bash
gh pr list --search "review-requested:@me"     # xem PR đang chờ bạn
gh pr checkout <số-PR>                          # lấy code về máy để chạy thử (nếu là PR code)
```

Rồi trên web: mở PR → tab **Files changed** → bấm vào một dòng cụ thể, viết câu hỏi (tiếng Anh) →
**Review changes** → chọn **Approve** (hoặc Request changes) → **Submit review**.
Không bấm "ok" suông, không comment ở ô cuối trang - như thế **không được tính là review**.
Xong thì `git checkout main`.
