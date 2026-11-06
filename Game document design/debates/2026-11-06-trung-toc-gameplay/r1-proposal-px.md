# R1 Proposal — PX (Linh Nghĩ: điều khiển, onboarding, độ phức tạp, scope)

## 1. Cách tôi hiểu yêu cầu
Chỉ làm domain PX: ánh xạ điều khiển theo cảnh, 15' đầu đời Nghĩ, đường cong tải thao tác, chi phí. Giả định: 5 ô = Đánh/Ăn + BN1 + BN2 + A1 + ô Thần Thông (khóa tới U1, **không được mượn**). Controller chung có cử chỉ **vuốt né** (như Lang §4.4). Số combat/needs giữ nguyên v1.2.

**Mâu thuẫn trong v1.2 cần chốt:**
- M-1: §4.2 hint đầu đời *"Mang về tổ…"* và FTUE "thắng đầu: xác cạnh tổ" cho thấy Tha có từ C1, nhưng §6.2 ghi *"Lập Sào bắt đầu Tha"*. → PX-03.
- M-2: §5.1 Pip Lính 0–3, nhưng thẻ **Lính Thứ Tư** cho 4 Lính. → Pip 0–4 (ô thứ 4 chỉ hiện khi có thẻ).
- M-3: **Hầm Ngầm** (Chức Diệp I) và **Mạch Tổ** là kỹ năng chủ động nhưng không có nút. Hồi sinh Lính "tại chỗ, tốn 6 No" cũng không có input. → PX-01, PX-02.

## 2. Hook
*"Một ngón tay điều cả bầy":* người chơi chỉ điều khiển Hậu, bầy tự đọc ý định. Chỉ có **2 lệnh bầy** (Xung, Giữ), không cần nút thứ 6.

## 3. Đề xuất chi tiết

### PX-01: Luật một nút "Chạm để ăn, giữ để làm việc của kiến"
- Nút Đánh/Ăn đổi thành **Tương Tác ngữ cảnh** (giữ = 0,35s, có vòng tiến độ):
| Đối tượng | Chạm | Giữ |
|---|---|---|
| Kẻ địch | Đánh (Lính tự đánh cùng mục tiêu) | — |
| Vật nhỏ (hạt, sâu, miếng thịt, vỏ Thoát Xác) | Ăn | **Tha** |
| Xác lớn | Cắn ăn | **Mở Xác** (kênh 6s) |
| Cây đang Mộc Tàn (C3+) | — | gợi ý dùng A1 (Căn Thương) |
| Tổ / Tổ Phụ | Nhập Nơi Trú | **Mạch Tổ** (M6, kênh 2s) |
| Đất trống, ngoài combat | — | **Đặt Tổ Phụ** (khi có thẻ, giữ 2s) |
- Đang Tha: nút đổi icon thành "Thả"; Xung/BN2 vẫn dùng được.
- **Vuốt né** → thành **Hầm Ngầm** khi có thẻ (không tốn ô).
- Vì sao tốt: một luật học 1 lần, áp được cho Lang (Mở Xác) và các tộc khác → chi phí UI dùng chung.

### PX-02: Bầy 2 lệnh + AI mặc định
- **Theo (mặc định):** Lính tự bám cách Hậu 1,5–3 ô, tự đánh mục tiêu Hậu vừa đánh hoặc kẻ đánh Hậu; tự né nước nông (đi vòng; không vào được thì đứng ở bờ).
- **Xung (BN1):** có kẻ địch trong 6 ô → auto-target (ưu tiên: mục tiêu đang khóa > kẻ vừa đánh Hậu > gần nhất). **Không có mục tiêu → Lính "Giữ" tại chỗ** (không tốn CD), bấm lại → Theo. Giữ dùng cho: canh khi Mở Xác, đứng bờ (Trùng ⊣ Thủy), **Giữ bến C4**.
- **Chạm vòng Pip Lính** quanh HP (vùng chạm ≥48dp) = hồi sinh 1 Lính tại chỗ (6 No; miễn phí nếu Hậu Mẫu và No >70). Pip: sống = đặc, chết = rỗng + đếm ngược, **bị tách** (bên kia nước) = viền cam, Giữ = hình vuông (không phân biệt bằng màu).
- **Won't:** lệnh "đi tới điểm", chọn từng Lính, đội hình. Chỉ có 2 lệnh vì mỗi lệnh thêm sẽ cộng ~1 quyết định/phút và chiếm 1 vùng chạm.
- PC: WASD · chuột trái đánh/chạm · **E** Tương Tác (giữ = Tha) · **1/2/3** BN1/BN2/A1 · **Space** né/Hầm Ngầm · **G** Giữ/Theo (phím riêng) · **R** hồi sinh Lính · chuột trỏ = mục tiêu Toan Dịch/Đục Rễ. Controller: A/B/X/Y + LB Giữ, RB hồi sinh.

### PX-03: Bảng điều khiển theo cảnh (X1)
| Cảnh (Mid) | Nút đang hoạt động | Thêm mới | Pip |
|---|---|---|---|
| C1 Ấu Nghĩ 0–14' | Joystick · Tương Tác (chạm/giữ) · BN1 Xung · vuốt né | Tha **lite** (chỉ Hậu, 1 vật, về Ổ trứng) — giải M-1; Mở Xác | 2 |
| C2 Lập Sào 14–50' | + **BN2 Toan Dịch** (chạm = nón về mục tiêu gần nhất/hướng đi; kéo = ngắm) | Giữ (Xung khi không có mục tiêu); Tha cho CT đầy đủ + Lính hộ tống (ý nghĩa "Lập Sào"); co-op; Tổ Phụ/Hầm Ngầm nếu chọn thẻ | 3 |
| C3 Thành Quần 50–116' | + **A1 Đục Rễ** ngữ cảnh: cạnh cây Mộc Tàn ≤2 ô = Căn Thương; còn lại = đường hầm auto-target ≤4 ô (kéo = ngắm) | Căn Thương; Bậc III sửa hành vi | 3 (4 nếu có thẻ) |
| C4 Nghĩ Đan 116–218' | A1 → **Đục Rễ Thăng** (cùng nút) | Giữ bến Đầm Mục (Giữ thành lệnh chính); Hợp Đạo M6 (Mạch Tổ = giữ Tương Tác ở tổ) | 3–4 |

Ô 5 vẫn khóa (biểu tượng Thần Thông mờ), không thêm nút ở bất kỳ cảnh nào.

### PX-04: Onboarding đời Nghĩ đầu tiên (X2) — mỗi beat 1 động từ
| Phút | Director bày | Học | Cảm xúc | Thưởng | UI mở |
|---|---|---|---|---|---|
| 0:00–0:03 | Vignette + hint *"Mang về tổ…"* | — | Tò mò | — | HP, No |
| 0:03–1:30 | Xác thỏ cách Ổ 5 ô | Chạm = ăn, 2 Lính tự đi theo | Thỏa mãn | **Thắng đầu ≤90s**: No + tick tu vi | **Pip Lính** (nhấp nháy 1 lần) |
| 1:30–3:00 | 2 sâu AI yếu | Đánh → Lính đánh cùng | "Mình là cả bầy" | Sâu +6 | — |
| 3:00–4:30 | Hạt Linh Thảo cách 15 ô, vệt mùi chỉ đường | **Giữ = Tha**, về Ổ → toast *"Tổ nhớ"* | Hub–spoke | Lượt Tha đầu đẩy lên **C1 Trung → M1** | Đạo Lộ 3 thẻ (★ Gợi ý) |
| 4:30–6:30 | Ếch/Thử AI to hơn | **Xung** (nút sáng) | Quyền lực | Hạ mồi lớn | BN1 |
| 6:30–8:30 | 1 Lính chết (kịch bản) | Hy Sinh hồi HP; chạm Pip = hồi sinh | Hiểu Lính là "máu phụ" | HP hồi | Đếm ngược Pip |
| 8:30–10:30 | Bóng Nha AI bổ nhào vào Lính lạc | Giữ bầy gần, về Tổ ăn ×1,25 | Hồi hộp | Sống sót | Icon Nơi Trú |
| 10:30–13:30 | Xác lớn + Lang AI lảng vảng ở 12 ô | **Giữ = Mở Xác** trong khi Lính canh | Căng → thả | Xác Mở +12 | — |
| ~14:00 | Đột phá C1→C2 | **Thoát Xác** (hồi đầy, vỏ rơi), Lính thứ 3 nở | Hùng tráng (đỉnh) | M2 + Thiên Phú Hậu Mẫu | BN2, Pip 3 |

Giữ (Xung không mục tiêu) **chỉ dạy ở C2** khi gặp bờ nước đầu tiên (hint 1 câu), không dạy ở C1.

### PX-05: Đường cong tải điều khiển (X3)
"Thao tác có chủ đích" = chạm/giữ/vuốt, không tính joystick. Ngưỡng mobile đặt theo kinh nghiệm thể loại (giả thuyết, đo ở VS):
| Cảnh | Thao tác/phút (trung vị · đỉnh combat 20s) | Quyết định có ý nghĩa/phút | Mục tiêu đồng thời | Nút |
|---|---|---|---|---|
| C1 | 10 · 25 | 1–2 (ăn hay Tha, đánh hay né) | ≤2 | 2 |
| C2 | 14 · 32 | 2–3 | ≤3 | 3 |
| C3 | 18 · 40 | 3 | ≤3 | 4 |
| C4 | 20 · **≤45 trần** | 3–4 | ≤4 | 4 |

**Điểm nóng quá tải:**
- **P1 — Vào C3 (~50'):** A1 + Căn Thương + Bậc III + hết Ấu Linh (PvP) cùng xảy ra trong ≤1'. → Không bật hint Căn Thương lúc đột phá, chỉ bật khi lần đầu đứng ≤6 ô cạnh cây Mộc Tàn; dùng Chọn Sau cho M3 nếu đang có kẻ thù trong 15 ô.
- **P2 — M6:** 3–5 thẻ + Hợp Đạo (mô tả dài). → Hợp Đạo hiện "kết quả" ≤12 chữ, ví dụ: *"Hầm Phục: chui lên là Xung ngay"*.
- **P3 — Nước tách bầy C4:** người chơi tưởng Lính bị lỗi AI. → Viền cam trên Pip + Lính đứng ở bờ phát "chờ". Cần SURV xác nhận Lính tự về sau bao lâu.
- **P4 — Chạm nhầm** Xung lúc không có mục tiêu thành Giữ. → Toast 1,5s "Bầy giữ chỗ", bấm lại để hủy; mục tiêu <5% lượt Giữ bị hủy trong 2s.

**Accessibility:** giữ ↔ bật (một lần chạm bắt đầu Tha/Mở Xác, chạm lần nữa thì dừng) · auto-target bật mặc định cho cả 3 skill, kéo để ngắm là tùy chọn · thời gian giữ 0,2/0,35/0,6s · rung khi Lính chết · Pip phân biệt bằng hình dạng · tùy chọn "Tự hồi sinh Lính khi No >X" (mặc định tắt, vì nó tiêu tài nguyên mà người chơi không bấm).

## 4. Chi phí & scope (X4)
Dòng Nghĩ hiện tại: lite 1,0 + N1 0,40 + phần N9 ~0,08 ≈ **1,48 t-n**. Cổng tuần 24 trượt nếu **>1,7**.
| Hạng mục | t-n |
|---|---|
| PX-01 Tương Tác chạm/giữ + vòng tiến độ (code dùng chung 5 tộc) | +0,06 |
| PX-02 AI Lính 2 trạng thái + Giữ + chọn mục tiêu cho Xung | +0,10 |
| Pip 0–4, tách bầy, chạm hồi sinh | +0,04 |
| PX-04 6 beat Director (thêm vào dòng #5 "thắng đầu") | +0,08 |
| Accessibility (giữ↔bật, thời gian giữ: dùng chung) | +0,03 |
| Telemetry Nghĩ | +0,02 |
| **Thêm** | **+0,33** |
| Bớt: không có lệnh "đi tới điểm", chọn Lính, đội hình (vốn đã ngầm nằm trong N1) | −0,10 |
| Bớt: Hầm Ngầm/Mạch Tổ không cần nút/UI riêng | −0,05 |
| Bớt: kéo-ngắm A1 bỏ ở MVP (chỉ auto-target), PC dùng chuột | −0,03 |
| **Net** | **+0,15 → ~1,63 t-n** (dư 0,07 so với cổng) |
Nếu tuần 24 đo >1,7: cắt Tổ Phụ đặt tự do (cố định 1 vị trí gợi ý) trước, tiếp theo là viền "bị tách".

## 5. Giả thuyết playtest riêng cho Nghĩ
| ID | Giả thuyết | Ngưỡng | GĐ | Nếu trượt |
|---|---|---|---|---|
| HNg-1 | Thắng đầu nhanh | ≥85% ăn xác ≤90s, ≥80% hạ sâu cùng Lính ≤3' | VS | Xác gần hơn, bỏ beat sâu |
| HNg-2 | Hiểu Tha | ≥70% Tha ≥2 vật về Ổ trước phút 8 mà không cần nhắc lại | VS | Vệt mùi rõ hơn, toast CT lớn hơn |
| HNg-3 | Không quá tải | Thao tác/phút đúng bảng PX-05 ±20% · ≤20% trả lời "không kiểm soát được bầy" | Alpha | Bỏ Giữ, AI tự canh khi Mở Xác |
| HNg-4 | Đọc được Pip | ≥75% nói đúng số Lính sống trong 2s · Giữ nhầm <5% | VS | Pip lớn hơn, đặt số cạnh HP |
| HNg-5 | Giữ được dùng thật | ≥40% người C4 dùng Giữ ≥3 lần/phiên ở bến | Alpha | Bến tự kích Giữ khi Hậu đứng trong vùng |

## 6. Kết nối domain
- **SURV:** Lính đi vòng hay chờ khi gặp nước; thời gian tự về; Giữ có làm Lính tốn No khác không.
- **PROG:** chốt M-1 (Tha C1 lite hay C2); đánh giá auto-target Xung có làm đổi dps.
- **WORLD:** câu toast "Tổ nhớ", tên lệnh Giữ (≤2 chữ).

## 7. Rủi ro tự nhận diện & câu hỏi mở
- Gộp Xung và Giữ vào một nút có thể gây nhầm. Nếu HNg-4 trượt thì dùng nút Pip: chạm = Giữ, còn hồi sinh chuyển sang tự động.
- Tôi có thể đã cắt quá tay: bầy chỉ có 2 lệnh có thể làm fan RTS thấy nông. Chiều sâu của bầy phải đến từ Đạo Lộ, không đến từ micro.
- **Câu hỏi:** controller chung có cử chỉ vuốt né cho mọi tộc không? Nếu không, Hầm Ngầm cần chỗ khác (đề xuất: giữ BN1).
