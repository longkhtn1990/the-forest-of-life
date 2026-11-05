# The Forest of Life

Dự án ý tưởng game. Tài liệu thiết kế nằm trong `Game document design/`.

## Team thiết kế
Có 4 subagent Senior Game Designer trong `.claude/agents/`:
- `gd-survival` (SURV) — hệ thống sinh tồn
- `gd-progression` (PROG) — phát triển nhân vật & systems math
- `gd-world` (WORLD) — thế giới, câu chuyện, nhân vật
- `gd-experience` (PX) — trải nghiệm người chơi, kinh tế, scope (red team)

Khi người dùng đưa ra yêu cầu thiết kế game, mặc định dùng skill `design-debate` để team đề xuất → phản biện chéo → sửa → giải quyết xung đột → tổng hợp `FINAL.md`. Chỉ trả lời trực tiếp không qua team khi người dùng nói rõ (vd "trả lời nhanh", "không cần debate").

Các session debate lưu tại `Game document design/debates/`. Trước mỗi session mới, đọc các `FINAL.md` trước đó để thiết kế nhất quán.
