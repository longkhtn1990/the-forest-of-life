---
name: design-debate
description: Điều phối team 4 Senior Game Designer (gd-survival, gd-progression, gd-world, gd-experience) tự đề xuất, phản biện chéo, sửa đổi và giải quyết xung đột qua nhiều vòng để ra một tài liệu thiết kế cuối cùng. Dùng khi người dùng đưa ra yêu cầu thiết kế game (cơ chế, hệ thống, nhân vật, thế giới, GDD, tính năng…) và muốn team debate, hoặc gọi /design-debate.
argument-hint: "[--quick | --deep] <yêu cầu thiết kế>"
---

# Design Debate — Orchestrator

Bạn (main thread) là **orchestrator / moderator**. Bạn KHÔNG tự thiết kế thay team; bạn chạy các vòng, viết tài liệu xung đột, và tổng hợp bản cuối. 4 agent:

| Code | Agent | Domain |
|---|---|---|
| SURV | `gd-survival` | Sinh tồn, needs, tài nguyên, crafting, mối đe dọa, base, cái chết |
| PROG | `gd-progression` | Phát triển nhân vật, skill tree, công thức, build, meta-progression, mô phỏng số |
| WORLD | `gd-world` | Chủ đề, lore, nhân vật & arc, nhiệm vụ, biome, thế lực |
| PX | `gd-experience` | Tâm lý người chơi, FTUE, kinh tế, retention, thị trường, scope, playtest (red team) |

Protocol chi tiết cho agent: `.claude/skills/design-debate/protocol.md` (đường dẫn tương đối từ project root).

## Chế độ
- `--quick`: R1 → R2 → R5 (tổng hợp) — 8 lượt agent. Cho câu hỏi nhỏ / brainstorm nhanh.
- **mặc định (standard)**: R1 → R2 → R3 → R4 (nếu còn xung đột) → R5 → R6 — ~16–20 lượt agent.
- `--deep`: như standard nhưng thêm một vòng R2' (critique các bản revision) trước R4, và R6 có thể lặp tối đa 2 lần.

## R0 — Chuẩn bị (orchestrator)
1. Đọc yêu cầu của người dùng và các tài liệu liên quan trong `Game document design/` (GDD trước đó, các FINAL.md cũ) để nối tiếp, không làm lại từ đầu.
2. Chỉ hỏi người dùng nếu thiếu thông tin **chặn hoàn toàn** việc thiết kế. Bình thường hãy tự đặt giả định hợp lý và ghi vào brief.
3. Tạo session: `Game document design/debates/<YYYY-MM-DD>-<slug>/` (và thư mục con `sim/` cho PROG).
4. Viết `00-brief.md`:
   - Yêu cầu nguyên văn của người dùng
   - Bối cảnh dự án (tên game, thể loại, nền tảng, quy mô team nếu biết)
   - Ràng buộc & giả định (ghi rõ cái nào là giả định)
   - Deliverable mong muốn (GDD section? spec hệ thống? danh sách ý tưởng?)
   - Tài liệu tham khảo trong repo cần đọc
   - Ngôn ngữ output (mặc định: ngôn ngữ người dùng dùng)
5. Báo người dùng 1 dòng: session ở đâu, chế độ nào, bắt đầu R1.

## Cách gọi agent mỗi vòng
- Gọi **4 agent song song trong cùng một lượt** (4 Agent tool call trong một message) với `subagent_type` tương ứng.
- Mỗi prompt phải tự đủ (agent khởi động lạnh). Mẫu:

```
Vòng: R<n> — <tên vòng>
SESSION: Game document design/debates/<...>/
Việc cần làm:
1. Đọc .claude/skills/design-debate/protocol.md, mục R<n>.
2. Đọc <danh sách file đầu vào của vòng này>.
3. Viết output vào <SESSION>/<file output>.
Lưu ý riêng cho vòng này: <nếu có — vd xung đột cần tập trung, góp ý của người dùng>
Trả về: tóm tắt ≤150 từ + đường dẫn file.
```

- Sau mỗi vòng: kiểm tra đủ 4 file tồn tại và đúng định dạng cơ bản. Thiếu thì gọi lại đúng agent đó (tối đa 1 lần), nếu vẫn lỗi thì ghi chú và đi tiếp.
- Cập nhật cho người dùng **1–2 dòng sau mỗi vòng** (điểm nổi bật/xung đột chính). Không dán nội dung file.

## Các vòng

| Vòng | Đầu vào | Output |
|---|---|---|
| R1 Proposal | `00-brief.md` | `r1-proposal-<code>.md` |
| R2 Critique | brief + 3 proposal của người khác | `r2-critique-<code>.md` |
| R3 Revision | brief + proposal của mình + cả 4 critique | `r3-revision-<code>.md` |
| R2' (chỉ `--deep`) | 4 revision | `r2b-critique-<code>.md` (cùng format R2) |
| R4 Conflicts | `r4-conflicts.md` + các revision | `r4-position-<code>.md` |
| R5 Synthesis | toàn bộ session | `FINAL.md` (orchestrator viết) |
| R6 Sign-off | `FINAL.md` | `r6-signoff-<code>.md` |

### Trước R4 — orchestrator viết `r4-conflicts.md`
Đọc 4 file revision (và critique nếu cần). Liệt kê **3–7 xung đột chưa giải quyết quan trọng nhất** (bỏ qua chuyện vặt). Mỗi xung đột:
- `C<n>`: tên, domain liên quan, domain owner
- Tóm tắt lập trường từng người (trích ID)
- 2–4 phương án (A/B/C, có thể gồm phương án lai do bạn đề xuất)

Nếu không còn xung đột đáng kể → bỏ qua R4 và ghi chú vào decision log.

### Quy tắc phán quyết R4
1. Tổng điểm có trọng số: domain owner của xung đột có trọng số **×1.5**, người khác ×1.
2. Phương án lai được ≥3 người ủng hộ được ưu tiên.
3. Hòa → domain owner quyết.
4. Bất kể kết quả, PX được quyền gắn cờ **"scope risk"** — khi đó FINAL phải ghi phương án cắt giảm (fallback).
5. Ghi mọi quyết định vào bảng Decision Log, kèm dissent.

## R5 — Viết `FINAL.md` (orchestrator)
Đọc lại toàn bộ session. Ưu tiên nội dung của các bản revision (R3) và quyết định R4. Không thêm ý tưởng mới không có trong debate (nếu cần lấp chỗ trống, đánh dấu `[orchestrator]`). Điều chỉnh cấu trúc theo loại deliverable; khung mặc định:

```markdown
# <Tên thiết kế>
> Session: <đường dẫn> · Chế độ: <...> · Ngày: <...>

## TL;DR (≤5 dòng)
## Theme & Design Pillars
## Core Loops (moment / activity / session / campaign)
## Hệ thống chi tiết
### <Hệ thống> — owner: <CODE> · nguồn: <IDs>
(quy tắc, bảng số, công thức, tình huống minh họa)
## Phát triển nhân vật & tiến trình
## Thế giới, câu chuyện & nhân vật
## Trải nghiệm người chơi (FTUE, độ khó, accessibility)
## Kinh tế (source/sink)
## Phạm vi: MVP / Vertical Slice / Sau này (MoSCoW + chi phí)
## Rủi ro & Giả thuyết playtest
## Decision Log
| # | Quyết định | Phương án bị loại | Ai ủng hộ / phản đối | Lý do |
## Dissent & Câu hỏi mở
```

## R6 — Sign-off
Gọi 4 agent song song đọc `FINAL.md`. Sau đó:
- Áp dụng các sửa đổi BLOCK hợp lệ (và NOTE hợp lý) trực tiếp vào `FINAL.md`.
- Nếu có BLOCK mà bạn không áp dụng, ghi lý do vào mục Dissent.
- `--deep`: nếu có BLOCK, chạy R6 lần 2 chỉ với agent đã BLOCK.

## Kết thúc
1. Copy `FINAL.md` ra `Game document design/<slug>.md` (bản dễ tìm).
2. Trả lời người dùng: kết quả chính (TL;DR), 2–3 quyết định gây tranh cãi nhất và ai thắng, các câu hỏi mở cần người dùng chốt, đường dẫn file.
3. Nếu người dùng góp ý sau đó: chạy vòng bổ sung nhắm đúng phần bị góp ý (có thể chỉ gọi 1–2 agent liên quan + PX), cập nhật FINAL, không chạy lại toàn bộ.
