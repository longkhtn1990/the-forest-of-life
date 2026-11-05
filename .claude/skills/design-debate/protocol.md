# Design Debate Protocol

File này quy định cách 4 designer (SURV, PROG, WORLD, PX) làm việc trong từng vòng debate. Mỗi agent **phải đọc file này** trước khi làm bài và tuân thủ đúng định dạng output của vòng được giao.

## Nguyên tắc chung
- **Một nguồn sự thật:** mọi thứ nằm trong thư mục session (`<SESSION>`), orchestrator sẽ cho đường dẫn. Đọc `00-brief.md` trước tiên.
- **ID cho mọi ý tưởng:** `<CODE>-<số>` (vd `SURV-03`). Khi sửa một ý tưởng, giữ ID và thêm hậu tố phiên bản: `SURV-03b`. Ý tưởng mượn từ người khác ghi rõ nguồn: `PROG-07 (từ WORLD-02)`.
- **Cụ thể và đo được:** con số, bảng, ví dụ tình huống người chơi. Tránh tính từ mơ hồ.
- **Phản biện có trách nhiệm:** mỗi lời phê bình phải có (1) vấn đề cụ thể, (2) tình huống người chơi minh họa, (3) đề xuất thay thế hoặc cách kiểm chứng.
- **Chống xu nịnh:** không được đồng ý hoàn toàn với mọi thứ. Mỗi bản critique phải có ít nhất 2 phản biện thực chất cho mỗi đề xuất được đọc.
- **Chống bảo thủ:** khi bị phản biện đúng, phải thừa nhận và sửa. Bác bỏ chỉ được chấp nhận khi có lập luận.
- **Tôn trọng domain:** được quyền phê bình mọi lĩnh vực, nhưng domain owner có tiếng nói nặng hơn trong lĩnh vực của mình.
- **Độ dài:** đủ để rõ, không lan man. Proposal ~1.200–2.500 từ, critique ~800–1.500 từ, các vòng khác ngắn hơn.
- **Trả về orchestrator:** tóm tắt ≤150 từ + đường dẫn file. Không dán nội dung file.

---

## R1 — Proposal (độc lập)
**File:** `<SESSION>/r1-proposal-<code>.md`
Không đọc proposal của người khác ở vòng này.

```markdown
# R1 Proposal — <CODE>

## 1. Cách tôi hiểu yêu cầu
(1 đoạn + các giả định đặt ra)

## 2. Ý tưởng cốt lõi (hook)
(1–2 câu)

## 3. Đề xuất chi tiết
### <CODE>-01: <tên>
- Mô tả:
- Số liệu / quy tắc:
- Tình huống người chơi minh họa:
- Vì sao nó tốt:
(lặp lại cho mỗi ý tưởng; tập trung vào domain của mình nhưng được đề xuất ngoài domain)

## 4. Kết nối với các domain khác
(những gì tôi cần/kỳ vọng từ SURV/PROG/WORLD/PX)

## 5. Rủi ro tự nhận diện
## 6. Câu hỏi mở
```

## R2 — Cross-Critique
**File:** `<SESSION>/r2-critique-<code>.md`
Đọc `00-brief.md` và 3 proposal của người khác.

```markdown
# R2 Critique — <CODE>

## Về <OTHER_CODE>
### Giữ lại (Keep)
- <ID>: vì sao tốt
### Mượn (Steal) — tôi muốn tích hợp vào thiết kế của mình
- <ID>: sẽ dùng thế nào
### Phản biện (Challenge)
| ID | Mức độ (Blocker/Major/Minor) | Vấn đề | Tình huống người chơi | Đề xuất thay thế / cách kiểm chứng |
### Câu hỏi cho <OTHER_CODE>

(lặp lại cho cả 3 người)

## Xung đột liên domain phát hiện được
| Xung đột | Các ID liên quan | Lập trường của tôi | Gợi ý giải quyết |

## Top 3 điều team phải chốt
```

## R3 — Revision & Rebuttal
**File:** `<SESSION>/r3-revision-<code>.md`
Đọc tất cả 4 file critique (tìm mọi phần nhắc tới CODE của mình hoặc ID của mình).

```markdown
# R3 Revision — <CODE>

## Phản hồi phản biện
| Phản biện (từ ai, ID) | Quyết định (Accept / Partial / Reject) | Lý do | Thay đổi cụ thể |

## Đề xuất đã sửa
(chỉ ghi các ý tưởng đã đổi/thêm mới, dùng hậu tố b/c; ý tưởng giữ nguyên chỉ cần liệt kê ID)

## Những thứ tôi mượn từ người khác
## Lập trường giữ vững (và vì sao)
## Điều tôi sẵn sàng đánh đổi
```

## R4 — Conflict Resolution
**File:** `<SESSION>/r4-position-<code>.md`
Đọc `<SESSION>/r4-conflicts.md` (orchestrator viết, gồm các xung đột chưa giải quyết, mỗi cái có 2–4 phương án).

Với mỗi xung đột:
```markdown
## C<n>: <tên xung đột>
| Phương án | Fun cho người chơi | Hợp chủ đề | Chiều sâu hệ thống | Khả thi sản xuất | Khác biệt thị trường | Tổng |
(chấm 1–5 mỗi tiêu chí)
- Lựa chọn của tôi:
- Lập luận mạnh nhất (≤80 từ):
- Phương án lai đề xuất (nếu có):
- Điều kiện để tôi đổi ý:
```

## R5 — Synthesis
Orchestrator viết `FINAL.md`. Agent không tham gia vòng này.

## R6 — Sign-off Review
**File:** `<SESSION>/r6-signoff-<code>.md`
Đọc `FINAL.md`.

```markdown
# R6 Sign-off — <CODE>
**Verdict:** APPROVE | APPROVE-WITH-NOTES | BLOCK

## Blockers (chỉ khi BLOCK)
| Vị trí trong FINAL | Vấn đề | Sửa cụ thể (viết sẵn đoạn thay thế) |
## Notes (không chặn)
## Nhất quán số liệu (PROG bắt buộc kiểm tra; người khác tùy chọn)
## Dissent ghi nhận (nếu vẫn không đồng ý một quyết định nhưng chấp nhận)
```
BLOCK chỉ dùng cho: mâu thuẫn logic nội tại, số liệu sai/không nhất quán, vi phạm trực tiếp brief, hoặc rủi ro khiến game không thể vui/không thể làm. Không BLOCK vì khác khẩu vị.
