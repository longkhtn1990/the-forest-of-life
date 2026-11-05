# R3 Revision — PROG

Sim mới: `sim/prog_r3_sim.py` → `sim/prog_r3_sim_output.md` (đường cong nén, Monte Carlo vòng đời theo persona × 3 chế độ bảo vệ, liệt kê build Lang, trần Ω, giữ di sản theo luật mất).
Bản này đã tính đủ Bổ sung 1, 2, 3 và các điểm R2 đã hội tụ: **Thú = Lang · Trùng = Linh Nghĩ (kiến) · Thủy = Linh Oa (ếch) · Vũ = Linh Kê (gà rừng) · FTUE chuột · NPC Lão Quy · vòng Ngũ Hành**.

**Sửa số liệu cho cả team trước khi đọc tiếp:** Mid = 5 phiên × 40'/tuần = **64 CT/phiên** (FINAL dòng 7, đã gồm Mộng Tích), tức **≈1,6 CT/phút chơi**. Mấy con số trước đây như "C3 ≈ Phiên 6 ≈ 1,5h" (PX) và "C4 ≈ 11,5h" (PROG R2) đều quy đổi sai. Theo đường cong v1.0, Phiên 6 ≈ 4h chơi và C4 ≈ 7,2h chơi. Mọi thời lượng bên dưới tính bằng **giờ chơi tích cực**, đã gồm chết và độ kiếp lại.

---

## Phản hồi phản biện

| Phản biện (từ ai, ID) | Quyết định | Lý do | Thay đổi cụ thể |
|---|---|---|---|
| SURV · PROG-01 Nghĩ ×1,75 ≈ 1 cảnh (Major) | **Accept** | Đúng. 3 Lính với hệ số 0,25 cộng thêm 120 HP thì gần như được tặng thêm một cảnh | PROG-16: mỗi Lính +0,15 → **×1,45** (3 Lính). Lính thứ 4 lấy qua thẻ Bậc II → ×1,60. Lính có 12% HP của Hậu, hồi sinh ở tổ 20s hoặc tại chỗ mất 6 No. Dùng chung No/Thể Lực với Hậu, không có thanh riêng |
| SURV/PX · Lý nước sâu bất tử, bị nhốt (Major ×2) | **Accept** | Fallback Oa của tôi ở R1 thực ra đã là câu trả lời | Lý → [Post] (Vũ Môn). Thủy MVP = **Linh Oa**. Nước sâu = bể ẩn theo bảng địa hình của SURV (§B) |
| SURV · PROG-03 E đổi theo nhánh Huyết Mạch (Major) | **Accept, và lỗi tự hết** | D thay Huyết Mạch bằng thẻ, nên **mỗi nhân vật chỉ có một Hành = Hành của tộc**. Không còn chuyện "một người hai Hành" | PROG-12: một ô Q ở cấp tộc, không có E theo nhánh |
| SURV/PX/WORLD · Thú = Linh Thử | **Accept** (đã rút ở R2) | — | Lang là đại diện Thú. Thử chỉ còn là Tiền Thân FTUE + AI |
| WORLD · Hành Thú=Thổ/Trùng=Hỏa/Vũ=Kim (Blocker lore) | **Accept** | Ánh xạ theo Tứ Tượng là đúng. Ba cách xếp đều là vòng 5, chỉ khác nhãn (R2) | Dùng **Mộc · Vũ=Hỏa · Trùng=Thổ · Thú=Kim · Thủy**. Sinh: Mộc→Vũ→Trùng→Thú→Thủy→Mộc. Khắc: Thú⊣Mộc⊣Trùng⊣Thủy⊣Vũ⊣Thú. Không số nào trong sim phải tính lại (trả lời câu hỏi của WORLD). Thần Vị chỉ đổi nhãn |
| PX · Thứ tự Mộc→Thú→Trùng→Vũ→Thủy | **Partial** | Thứ tự này cũng đúng Ngũ Hành (Thú=Hỏa). WORLD nói "không phải Ngũ Hành" là nhầm. Tôi theo nhãn Tứ Tượng vì lore khớp hơn, và mọi số của tôi không đổi theo nhãn | Orchestrator chốt. Thẻ D không phụ thuộc vào nhãn |
| PX/WORLD · Tước → Kê | **Accept** | — | Linh Kê: Sải Cánh (60 Thể Lực, CD 20s, theo SURV) + Hạ Cánh Đạp (WORLD) |
| PX · PROG-05 lite 3 kỹ năng + Ngộ Đạo draft (Major) | **Partial** | Bỏ Ngộ Đạo draft, vì D thay nó. A1 của bản lite làm dạng data-only (biến thể BN1). Nhưng lite vẫn cần 4 mốc chọn (PROG-14) | Lite: BN1, BN2, A1 data-only. Có 10 thẻ, 4 lượt chọn |
| PX · D "chọn mỗi cảnh" | **Partial** | Chỉ chọn ở đột phá cảnh thì lượt chọn đầu đến sau 14' (SURV muốn ≤5'), còn lite chỉ có 2 lượt nên F không random được gì | Chọn ở đột phá cảnh **cộng thêm 2 mốc giữa cảnh**: vào C1 Trung (phút 4) và vào C3 Hậu (cùng C4 Hậu với bản full). Bảng ở PROG-08 |
| PX · Mobile: "5 thẻ cùng lúc, ≤6 chữ" | **Accept** | — | Hiện đủ 3–5 thẻ, không vuốt. Tên ≤2 từ (WORLD), mô tả ≤12 chữ, icon trục, gắn ★ Gợi ý theo hành vi |
| PX · F: lite là đường tắt farm di sản | **Accept** | Lite Viên Mãn sau 2,3h, full sau 4,8h | Di sản từ lite có phẩm **Sơ**, từ full có phẩm **Thâm** (≈0,6×). Tính theo giờ thì hai đường ngang nhau (PROG-13) |
| PX · F: qua tộc thì ×0,5 nếu không có tag | **Reject** | Bảng dịch theo trục chỉ có 25 dòng data (~0,1 t-n), còn ×0,5 làm di sản đổi tộc thành bẫy, đi ngược G | Dịch theo trục (PROG-13) |
| PX · Cấu hình B: lite cap C2 | **Reject** (giữ C3) | Xem lập trường ở PROG-14. Đã thiết kế sẵn fallback C2 để D/F vẫn chạy được | Fallback C2 nằm trong PROG-14 |
| PX/WORLD · Hệ số khắc ≤×1,15 | **Partial** | Khắc ở cấp tộc đã có **cơ chế** đi kèm (chặn, Ướt, lộ vị), trị giá khoảng +5%. Cộng ×1,15 vào thì bên khắc thắng ~72%. ×1,10 cộng cơ chế cho **67%** | Q = ×1,10 / ×0,91 (PROG-12) |
| PX · tộc vắng người chơi: +Đạo Quả, PROG chọn số | **Accept** | Đạo Quả giờ chỉ mở khóa ngang, nên thưởng thêm không làm lệch cân bằng | +20% Đạo Quả cho tộc <8% số lượt chọn trong phòng, tính trong 3 ngày |
| PX · câu hỏi Hồi Ức C4→lite / farm Đạo Quả | Trả lời | Hồi Ức đã bỏ (E). Đạo Quả không mua sức mạnh nên farm lite không có lợi gì | — |
| SURV · D: mỗi bộ thẻ phải có ≥1 lựa chọn sống sót | **Accept** | Đúng điểm mù của tôi | Mỗi tộc có một Đạo **Tồn**. Đạo này luôn được chào ở mốc kế tiếp cho tới khi đầy Bậc III |
| SURV · D: lite 2 mốc × 3 thẻ | **Reject** | 2 thẻ thì không thể "random 3" được (F) | Lite 4 mốc |
| SURV · F: 1 slot, thay thế | **Partial** | Phương án S1 được đưa cho người dùng chốt. Tôi khuyến nghị S2 (PROG-13) | — |
| SURV · F: di sản không mất | **Accept** (là khuyến nghị) | Sim D: luật "mất hết" chỉ giữ được 2,2 Đạo Chủng sau 10 đời (p=0,7), luật "không mất" giữ được 7,0 | Ba phương án cho người dùng chốt (PROG-13) |
| SURV · E: ngưỡng mất ≤40' (C1–C2) / ≤90' (C3+) | **Partial** | Lite đạt: trung bình 69' mỗi lần chết. Full **không đạt**: 130' mỗi lần chết. Nhưng tính kỳ vọng mỗi lần Viên Mãn chỉ mất 44' | Đề nghị SURV đổi KPI sang "phút mất kỳ vọng mỗi lần Viên Mãn ≤60'". Nếu vẫn giữ 90'/lần thì có núm vặn: C4 nén thêm (PROG-11) |
| SURV-R2-01 · Kiếp thất bại lùi về đầu cảnh | **Partial** | Lùi về đầu C4 là mất 140 CT ≈ 88', ngang với chết | Lùi về **đầu tầng Hậu** (C4: −52 CT ≈ 33'), giữ thẻ, CD 10'. Sau 3 lần thất bại liên tiếp: Đạo Cơ Tổn 20' |
| WORLD · Kiếp thất bại = chết | **Reject** | Sim B: full nén, Mid, kiếp = chết → **P(hoàn thành đời đầu) = 13%**, 7,9 đời cho một lần Viên Mãn. Kiếp ≠ chết → **68%**. Đây là núm vặn lớn nhất của cả hệ thống | Kiếp ≠ chết. Chỉ chết khi HP = 0 trong kiếp |
| WORLD-11 · Vòng gỗ / Đạo Ý | **Accept** | Ẩn dụ đẹp và trùng với cấu trúc kế thừa | UI "Niên Luân": vòng đồng tâm, mỗi mốc một vòng. WORLD đặt tên thẻ, tên của tôi là tạm |
| WORLD-13 · Trần 3 | **Accept** | Khớp S2 (tối đa 3 ô) | — |
| WORLD-13 · Đời sau chết thì mất hết Đạo Chủng | **Reject làm mặc định**, đưa vào phương án | Sim D. Mất hết thì ô 2–3 gần như không bao giờ mở | Đưa L2 cho người dùng, cùng phương án lai L3 |
| WORLD-14 · 5 trục Sát/Hộ/Sinh/Hành/Thức | **Accept** | Gọn hơn bộ "Động/Hồi" của tôi ở R2 | Bảng dịch 5 trục × 5 tộc (PROG-13) |
| WORLD · câu hỏi: dịch đủ mọi ô hay chỉ ô dịch được? | Trả lời | Theo trục thì **ô nào cũng dịch được**, nên luật "ô không dịch được thì loại" không cần nữa | — |
| SURV · câu hỏi: Lính dùng chung No? Nghĩ có Hậu thứ hai trước cổng? | Trả lời | Chung No và Thể Lực. **Không** có Hậu thứ hai ở MVP: Yêu Nghĩ là C5 (U1) | — |
| PROG R2 (tự sửa) · Ô Q {0,80; 1; 1,25}, trần 1,73 | **Sửa** | E theo nhánh đã mất cùng Huyết Mạch | Q ∈ {0,91; 1; 1,10}. Trần tổng **Ω ≤ 1,60** (PROG-12) |

---

## Đề xuất đã sửa

Giữ nguyên: PROG-06 phần "nước nông/sâu" (đã nhường bảng số cho SURV), PROG-07 (Thần Vị, chỉ đổi nhãn: Thổ – Rừng Tro → **Trùng**, Kim – Vách Đá Rêu → **Thú**, Hỏa → **Vũ**; vực nào khớp thì WORLD chọn).

### PROG-01b: Năm nhân vật MVP
| Tộc (Hành) | Nhân vật | Thế mạnh | Điểm yếu cố ý | Động từ riêng (G) | Bậc MVP |
|---|---|---|---|---|---|
| Mộc (Mộc) | **Linh Mộc** | Neo: lãnh thổ, phòng thủ, offline bất tử | Bất động | Bén Rễ + Vệt Nắng (đã có) | Full C4 |
| Thú (Kim) | **Lang** | Săn: burst, đuổi | Ít công cụ giữ chỗ | **Đánh Hơi** (vệt máu/xác 12 ô) | Full C4 |
| Trùng (Thổ) | **Linh Nghĩ** | Bầy + hậu cần + Căn Thương | Lính chết vì AoE | **Gọi Bầy / Tha** | Lite C3 |
| Thủy (Thủy) | **Linh Oa** | Hồi động, kiểm soát bờ nước | Ẩm trên cạn | **Lặn + Quăng Lưỡi** | Lite C3 |
| Vũ (Hỏa) | **Linh Kê** | Thấy xa, báo tin, lướt | Mỏng | **Sải Cánh + Báo Tin + Bới** | Lite C3 |

**Base n=1** (Mộc, Lang giữ §6.9):
| | HP | Công | d | Tốc | Thần Thức |
|---|---|---|---|---|---|
| Linh Nghĩ | Hậu 300 · Lính 12% HP Hậu (36) | 22 + 0,15×Công mỗi Lính (tối đa 3) | 0,25 | 5,4 | 12 |
| Linh Oa | 330 | 30 | 0,30 | 5,6 cạn · ×1,2 nước nông | 14 |
| Linh Kê | 260 | 26 | 0,25 | 6,4 (+Sải Cánh) | 18 |

### PROG-02b: Nguồn tu vi cho Oa và Kê (Nghĩ giữ R1)
| Loài | Chính | Phụ | Đặc thù | Phương sai ước |
|---|---|---|---|---|
| Linh Oa | Lưỡi bắt côn trùng/mồi nhỏ 45% | Dẫn Nước, cộng sinh ven nước 25% | Thoát Sinh 2 CT, nuốt mồi AI 30% | ~21% |
| Linh Kê | Bới hạt/sâu 40% | Báo Tin cho đồng minh/thấy Linh Hạch 25% | Thoát Sinh 2 CT, Hạ Cánh Đạp 35% | ~27% |
Cùng mô hình Poisson R1. Chuẩn 1,0 CT/phút ±10% chỉ là tham số data.

### PROG-08 (mới): Khung "Đạo Ý" thay Huyết Mạch, Keystone, Ngộ Đạo, Notable/Minor (§6.4–6.5)
**Cấu trúc chung cho cả 5 tộc (một template, một UI):**
- **3 Đạo × 3 Bậc = 9 thẻ.** Mỗi tộc có đúng một Đạo **Tồn** (sống sót), một Đạo **Sát**, một Đạo **Vai** (khuếch đại thế mạnh tộc hoặc hỗ trợ party).
- **1 Thiên Phú tộc** (khuếch đại động từ riêng), chọn được từ mốc 2.
- **Hợp Đạo** (chỉ bản full): 3 thẻ, mỗi cặp Đạo một thẻ. Điều kiện: có Bậc II ở cả hai Đạo. Chỉ xuất hiện ở mốc 6.
- **Thâm Hóa** (thẻ đệm chung): chỉ xuất hiện khi bộ thẻ có <3 lựa chọn. Tăng thẻ vừa nhận lên ×1,3. Sim: với luật này, **mọi mốc đều có ≥3 thẻ** (không có nó thì có một nhánh đường đi chỉ còn 2).
- **Kế thừa:** Bậc k chỉ hiện khi đã có Bậc k−1 cùng Đạo. Bậc III **sửa hành vi của Bậc I** (vd Huyết Bộc kích nổ chảy máu mà Răng Cưa tạo ra). Hợp Đạo nối hai Đạo.
- **Còn hiệu quả đến hết đời:** (1) Không có số cố định. Mọi giá trị là % Công/HP/CD/tầm hoặc nhân với chỉ số theo tầng. (2) Thẻ chỉ được bám vào kỹ năng **đã mở** ở mốc sớm nhất mà thẻ đó có thể xuất hiện: Bậc I chỉ bám BN1/bị động, Bậc II được bám BN2, Bậc III được bám A1. (3) **A1 không bị bỏ ở C4.** A2 là **A1 Thăng** (cùng nút), nên HUD vẫn là 3 skill và không thẻ nào thành thẻ chết vì bị rút khỏi loadout. (4) Kiểm tra Lão Hóa: giá trị tương đối của thẻ ở Viên Mãn phải ≥0,8× lúc nhận.
- **Pool cố định, hiện trước** trong Codex. Random chỉ xảy ra ở F. **★ Gợi ý:** Đạo khớp với hành vi 10' gần nhất được gắn sao (thay cho Ấn của learn-by-doing).
- **Không respec trong đời.**

**Mốc chọn (đường cong nén PROG-11, Mid):**
| Mốc | Khi nào | Phút (Mid) | Thẻ hiện | Full | Lite |
|---|---|---|---|---|---|
| M1 | Vào C1 Trung | 4' | 3 (Bậc I × 3) | ✔ | ✔ |
| M2 | Đột phá C1→2 | 14' | 3–4 (+Thiên Phú) | ✔ | ✔ |
| M3 | Đột phá C2→3 | 50' | 3–4 | ✔ | ✔ |
| M4 | Vào C3 Hậu | 86' | 3–4 | ✔ | ✔ |
| M5 | Đột phá C3→4 | 116' | 3–4 | ✔ | Viên Mãn |
| M6 | Vào C4 Hậu | 171' | 3–5 (+Hợp Đạo) | ✔ | — |
| Viên Mãn | Vượt Kiếp Viên Mãn C4 | 218' | (F) | ✔ | — |
Khoảng cách dài nhất giữa hai mốc là 55'. Lần chọn đầu ở phút 4 (SURV-R2-04 ≤5' đạt). Thời gian chọn mục tiêu ≤20s (PX HD1).

**Số thẻ phải viết:** full 9 + 1 + 3 = 13 (×2), lite 9 + 1 = 10 (×3), Thâm Hóa 1 ⇒ **57 thẻ**. Kỹ năng: 3 nút mỗi loài (A2 là bản Thăng của A1) ⇒ 15 kỹ năng + 2 bản Thăng, phần lớn là data. So với v1.0 là 18 kỹ năng + 42 node + 18 Minor + 6 Huyết Mạch (kèm đổi sprite) + Keystone.
**Chi phí ước:** 57 thẻ × ~0,012 = 0,7 · UI Niên Luân 0,25 · di sản 0,4 ⇒ +1,35. Cắt: sprite Huyết Mạch −0,3, Ngộ Đạo draft −0,2, Keystone −0,1 ⇒ **ròng ≈ +0,75** (PX tính D+F = +1,5). PX chốt số cuối.

### PROG-09 (mới): Mẫu chi tiết — Lang
**Kit (3 nút, không đổi theo build):** BN1 **Lang Nha** (C1): lao cắn 4 ô, ×1,5 Công, CD 12s · BN2 **Hú** (C2): lộ vị con mồi trong 20 ô trong 4s, CD 30s · A1 **Xé** (C3): ×1,6 Công + chảy máu 4s (tổng 40% Công), CD 10s → A2 **Xé Thăng** (C4): ×1,8, chảy máu 6s · Bị động **Đánh Hơi**: thấy vệt máu/xác trong 12 ô, nước xóa vệt.

| Đạo (trục) | Bậc I (mở M1) | Bậc II (từ M2) | Bậc III (từ M3) |
|---|---|---|---|
| **Truy Huyết** (Sát) | **Răng Cưa**: Lang Nha gây chảy máu 45% Công/3s | **Khứu Huyết**: mục tiêu đang chảy máu hiện trên Đánh Hơi tới 20 ô. Đòn lên mục tiêu chảy máu +10% | **Huyết Bộc**: Xé kích nổ phần chảy máu còn lại ×1,5 và hồi 30% lượng đó. *Kế thừa Răng Cưa* |
| **Đầu Đàn** (Vai) | **Dẫn Đàn**: party thấy vệt Đánh Hơi của bạn. Đi theo vệt +5% Tốc | **Hú Bầy**: Hú cho đồng minh trong 12 ô +8% Tốc 4s. Solo: mục tiêu bị lộ chậm 15% trong 3s | **Lang Vương**: Hú gắn Dấu Săn 5s. Party đánh +6%, mục tiêu không vào được Hang/Ẩn. Solo: Lang Nha −30% CD lên mục tiêu có Dấu |
| **Độc Hành** (Tồn) | **Ẩn Phong**: đứng yên/đi chậm 2s ngoài giao tranh thì ẩn khỏi Thần Thức đối thủ ngoài 6 ô. Đòn đầu ×1,3 | **Nuốt Vội**: ăn xác ×2 tốc, mỗi cắn hồi 2% HP | **Kẻ Đơn Độc**: HP <35% thì +15% Tốc 4s, xóa đánh dấu, kích Ẩn Phong ngay. CD 60s. *Kế thừa Ẩn Phong* |
| Thiên Phú (Thức) | **Mũi Sói**: Đánh Hơi 12 → 18 ô, còn ngửi được vệt của kẻ vừa vào Hang trong 5s | | |
| Hợp Đạo (M6) | Truy Huyết × Đầu Đàn **Huyết Nguyệt**: chảy máu do đồng minh gây cũng bị Huyết Bộc kích nổ · Truy Huyết × Độc Hành **Bóng Máu**: đòn đầu từ Ẩn Phong gây chảy máu ×2 · Đầu Đàn × Độc Hành **Ảnh Dẫn**: khi bạn ẩn, đồng minh trong 8 ô cũng ẩn ngoài 10 ô | | |

**Kiểm chứng (sim C, hệ số dps × ehp ước theo nhịp đòn của Lang):**
| Kiểm tra | Kết quả |
|---|---|
| Số build khác nhau (6 lượt chọn) | **43** |
| Số thẻ hiện ít nhất ở một mốc | **3** (đạt yêu cầu 3–5) |
| Chênh mạnh/yếu nhất (solo / party) | **1,17 / 1,11** (ngưỡng ≤1,25) |
| Thẻ có mặt ở 100% top 20% build | Solo: Răng Cưa, Khứu Huyết, Ẩn Phong (yếu, top 20% chỉ có 8 build). Party: **không có** |
| Archetype | Truy Huyết thuần 1,38 · Độc Hành thuần 1,39 · Lai Huyết–Bóng 1,41 · **Đầu Đàn: solo 1,28, party 1,38** |

**Build Archetype Cards (Lang):**
| Build | Fantasy | Thẻ lõi | Mạnh | Yếu / đối trọng |
|---|---|---|---|---|
| Huyết Ảnh | Sát thủ rình | Ẩn Phong → Răng Cưa → Bóng Máu | Mở giao tranh bằng đòn ×1,3 cộng chảy máu | Bị Kê Báo Tin lộ vị, Oa đục nước xóa vệt |
| Huyết Bộc | Đấu tay đôi kéo dài | Truy Huyết I–III | Tự hồi giữa trận | Thiếu đường thoát |
| Sói Cô | Sống sót, ăn xác | Độc Hành I–III + Mũi Sói | Rất khó bị gank | Sát thương thấp nhất |
| Đầu Đàn | Bầy săn | Đầu Đàn I–III + Huyết Nguyệt | Party ×1,30 dps | Solo yếu hơn 8%. **Rủi ro trap cho người chơi solo** → thẻ gắn nhãn "Bầy" + có giá trị solo. Đo pick-rate solo |

### PROG-10 (mới): Khung thẻ cho 4 nhân vật còn lại
Các số dưới đây là giá trị khởi điểm. Ngân sách mỗi thẻ: Bậc I ≈ +4%, II ≈ +5%, III ≈ +6–8% (dps hoặc ehp hoặc giá trị tiện ích tương đương). WORLD đặt lại tên.

**Linh Mộc (full).** Kit: Gai Bạo · Độc Tiết · A1 **Vỏ Cứng** (−50% sát thương 5s, C3) → **Thiết Bì** (C4, thêm phản 10%). Động từ: Vệt Nắng, Vươn rễ, Mầm-Neo, Quả Ước, Kiến, Linh Thức (đã có).
| Đạo | I | II | III |
|---|---|---|---|
| **Thiết Mộc** (Tồn/Hộ) | Vỏ Gai: Gai Bạo phản 15 → 22% | Nhựa Đắng: Độc Tiết −30% hồi máu đối thủ 6s | Bàn Căn: Tâm Rễ +40%, Căn Thương lên mình −25% |
| **Bách Thảo** (Vai: **cỏ trong Mộc tộc**) | Thảm Cỏ: ô rễ mới mọc cỏ. Vươn rễ 20 → 14s/ô, giá −25% | Cỏ Gai: kẻ địch trên thảm −10% Tốc | Phản Sinh: Đổ thì Mộc Tàn 120 → 80s, Tán mọc lại từ thảm ×2 |
| **Linh Quả** (Sát/Hợp) | Quả Ngọt: Quả Ước −20% giá, +25% No cho kẻ ăn | Quả Linh: đồng minh ăn quả +10% Tốc 20s hoặc hồi 8% HP | Khế Ước Kiến: +1 tổ (3), kiến gây 0,1 × Công cây/s |
Thiên Phú **Rễ Cảm** (báo kẻ đến trong 20 ô). Hợp Đạo: Thảm Gai · Quả Đắng · Vườn Hoang (+1 Mầm Con trên thảm).
→ **Yêu cầu "Mộc gồm cỏ" có trong MVP với chi phí 0 loài mới**: một cây theo Đạo Bách Thảo chơi như thảm cỏ lan nhanh. Linh Thảo vẫn là Thiên Tài Địa Bảo. Loài cỏ riêng để [Post].

**Linh Nghĩ (lite).** Kit: BN1 **Xung** (ra lệnh bầy đánh một mục tiêu 4s, Lính ×1,5, CD 10s; C1 có 2 Lính, C2 có 3) · BN2 **Toan Dịch** (nón 3 ô, 0,8×Công, chậm 20%, CD 12s) · A1 **Đục Rễ** (data trên Xung: Căn Thương, xem PROG-16). Động từ: **Tha**.
| Đạo | I | II | III |
|---|---|---|---|
| **Binh Nghĩ** (Sát) | Hàm Thép: Lính +15% sát thương | Lính Thứ Tư: +1 Lính, HP mọi Lính −15% | Vạn Nghĩ Xung: Xung 6s. Lính chết trong Xung hồi sinh ngay 1 lần |
| **Hậu Cần** (Vai) | Vai Rộng: Tha 2 vật. Tốc khi Tha −30% → −10% | Đường Mùi: vệt mùi giúp đồng minh/Lính +15% Tốc. CT từ Tha ×1,2 | Kho Tổ: Lính hồi sinh 20 → 10s. Trong 4 ô quanh tổ hồi 1% HP/3s |
| **Thổ Thành** (Tồn) | Hầm Ngầm: chui đất 2s, không bị chọn làm mục tiêu, CD 25s | Tổ Phụ: +1 tổ phụ (hồi sinh Lính, điểm chui) | Lính Đỡ: 25% sát thương lên Hậu chuyển sang Lính gần nhất |
Thiên Phú **Hậu Mẫu**: Lính hồi sinh không tốn No khi No >70%.

**Linh Oa (lite).** Kit: BN1 **Quăng Lưỡi** (4 ô, 1,0×Công, chậm 30% 1s; kéo mồi AI/vật phẩm, **không kéo người chơi ở MVP** theo SURV) · BN2 **Nhảy Vọt** (4 ô; đáp xuống nước thì đục nước 3 ô trong 4s, kẻ trong vùng mất dấu Oa; CD 12s) · A1 **Lưỡi Độc** (data: thêm độc 30% Công/3s, chậm 40%). Động từ: **Lặn** + Ẩm (SURV).
| Đạo | I | II | III |
|---|---|---|---|
| **Lưỡi Mồi** (Sát) | Lưỡi Dài: tầm 4 → 5,5 ô | Nuốt Chửng: Lưỡi lên mồi AI <30% HP thì nuốt luôn. Lên người chơi +20% | Lưỡi Kép: Quăng Lưỡi có 2 lần sạc |
| **Dòng Nước** (Vai: hồi động) | Dẫn Nước: tưới cây đồng minh trong 3 ô +6 Thủy/phút | Suối Lành: đồng minh trong 3 ô ở nước nông hồi 0,5% HP/5s | Mưa Rào: Nhảy Vọt mang theo vũng nông 3×3 trong 15s, CD 45s |
| **Da Ẩm** (Tồn) | Da Dày: Ẩm cạn chậm hơn 30% (10' → 13') | Ngụy Bùn: đứng yên 1,5s ở nước nông/bùn thì ẩn ngoài 4 ô | Ngủ Bùn: HP <30% trong nước sâu/bùn: hồi 3% HP/s trong 4s, CD 90s |
Thiên Phú **Rung Nước**: cá/ếch AI trong 12 ô báo khi có kẻ đến.

**Linh Kê (lite).** Kit: BN1 **Sải Cánh** (lướt 4 ô qua bụi/nước nông, 60 Thể Lực, CD 20s, không đánh/ăn khi lướt) + **Hạ Cánh Đạp** (đòn đầu trong 1,5s sau khi đáp ×1,4) · BN2 **Báo Tin** (ping 20 ô 8s cho party; solo thấy Linh Hạch trên xác trong 20 ô) · A1 **Mổ Liên Hoàn** (data: 3 mổ × 0,6 Công). Động từ: **Bới** (lộ hạt/sâu, xới ô +Dưỡng Chất).
| Đạo | I | II | III |
|---|---|---|---|
| **Cựa Sắt** (Sát) | Cựa Nhọn: Hạ Cánh Đạp ×1,4 → ×1,6 + chảy máu 2s | Mổ Mắt: đòn thường thứ 3 liên tiếp làm mục tiêu mất 50% Thần Thức trong 2s, CD 15s | Liên Hoàn Cựa: Mổ Liên Hoàn ngay sau Sải Cánh thành 4 mổ |
| **Gáy Sáng** (Vai: Thức) | Mắt Gà Rừng: Thần Thức +15% | Báo Tin Xa: 20 → 28 ô, ping 8 → 12s | Gáy Bình Minh: Báo Tin đầu ngày-rừng, cây trong 8 ô +15 Thủy, đồng minh +10 Thể Lực |
| **Bới Đất** (Tồn/Sinh) | Bới Nhanh: Bới ×1,5 tốc, No từ sâu ×1,5 | Diều Hâu!: kẻ cảnh cao hơn/Diều hâu vào 14 ô thì cảnh báo 2s, lần Sải Cánh kế −50% CD | Ổ Rơm: Bới 3s tạo 1 Ổ (ẩn tại chỗ, hồi 1% HP/3s) |
Thiên Phú **Lẩn Bụi**: Sải Cánh vào bụi thì ẩn 2s.

### PROG-11 (mới): Đường cong nén (vì chết = mất trắng)
Giữ công thức `CT_tầng = CT_cảnh × (0,30/0,33/0,37)` và chỉ số ×1,10/tầng (×1,77/cảnh). **Chỉ đổi hằng số CT_cảnh, xấp xỉ ×0,5.**
| C | CT tầng S/T/H | CT cảnh | Kiếp (CT) | Lũy kế | v1.0 lũy kế | Phút Mid (không chết) | Mở khóa |
|---|---|---|---|---|---|---|---|
| 1 Khai Linh | 6/7/7 | 20 | 3 | 23 | 41 | 14' | BN1, động từ tộc, M1 |
| 2 Luyện Khí | 15/16/18 | 50 | 8 | 80 | 156 | 50' | BN2, co-op, Linh Thức + Kiến (cây), M2 |
| 3 Trúc Cơ | 27/30/33 | 90 | 15 | 185 | 366 | 116' | A1, Căn Thương (Nghĩ), M3–M4. **Viên Mãn lite** |
| 4 Kết Đan | 42/46/52 | 140 | 23 | 348 | 691 | 218' | Thâm Lâm, A1 Thăng, M5–M6. **Viên Mãn full** |
| 5 [U1] | 57/63/70 | 190 | 35 | 573 | 1.141 | — | |
| 6 [Post] | 78/86/96 | 260 | — | 833 | 1.661 | — | |
Ấu Linh "3h hoặc hết C2" thực tế kết thúc ở phút ~50. Áp Chế n=9 của Hạ Lâm không đổi.

**Vòng đời theo persona (sim B, chế độ 2 = kiếp ≠ chết + Ấu Linh tới hết C2 + Trọng Thương C3+):**
| Persona (h chết/giờ, % PvP) | Full: P(đời đầu Viên Mãn) | Full: giờ tới 1 Viên Mãn | Lite: P | Lite: giờ | Mất TB/lần chết (full / lite) |
|---|---|---|---|---|---|
| P1 xe buýt (0,06, 40%) | 83% | 4,6h ≈ **7–8 ngày** (37'/ngày) | 92% | 2,3h ≈ 4 ngày | 131' / 68' |
| P3 làm vườn (0,08, 50%) | 78% | 4,7h ≈ 9 phiên 30' (≈1,9 tuần) | 90% | 2,3h ≈ 1 tuần | 129' / 67' |
| Mid (0,10, 60%) | 75% | 4,8h ≈ 7 phiên (≈1,4 tuần) | 89% | 2,3h ≈ 3,5 phiên | 132' / 69' |
| P2 kẻ săn (0,18, 75%) | 63% | 5,3h ≈ 5 phiên 60' (≈1 tuần) | 82% | 2,4h | 126' / 68' |

**So sánh để thấy từng núm vặn đóng góp gì (Mid, full C4):**
| Cấu hình | P(đời đầu) | Giờ / Viên Mãn | Số đời |
|---|---|---|---|
| v1.0, kiếp = chết | 9% | 25,4h | 10,8 |
| v1.0, kiếp ≠ chết + bảo vệ | 56% | 11,4h | 1,8 |
| Nén, kiếp = chết | 13% | 10,4h | 7,9 |
| **Nén, kiếp ≠ chết + bảo vệ (đề xuất)** | **75%** | **4,8h** | **1,33** |
Phút mất kỳ vọng mỗi lần Viên Mãn = (số đời − 1) × phút mất/lần: full Mid 44', P2 74'. Lite Mid 8', P2 15'.
**Núm vặn nếu SURV vẫn giữ ≤90' mỗi lần chết:** C4 = 100 CT (lũy kế 302 ≈ 189') thì mất TB ~110'. Muốn đạt 90' thật phải đưa full xuống còn ~2,5h, khi đó C4 mỏng hơn lite C3 cộng thêm. Tôi không khuyến nghị.
**Tổng nội dung lần đầu (Mid):** Viên Mãn cả 5 tộc ≈ 2 × 4,8 + 3 × 2,3 ≈ **16,5h**, chưa tính chơi lại để đổi build hay góp ô di sản.

### PROG-12 (sửa PROG-R2-01): Trần hệ số — ô Q và trần tổng Ω
1. **Ô Q (quan hệ tộc):** đúng **một** hệ số sát thương từ quan hệ: khắc **×1,10**, bị khắc **×0,91**, còn lại ×1. Áp từ C1, áp **cả lên AI cùng tộc** (theo PX, để ma trận được cảm thấy ở CCU thấp). Không thẻ, di sản hay sự kiện nào được nhân thêm vào Q.
2. **Khắc chủ yếu là cơ chế** (chặn, Ướt, lộ vị, đục nước). Ngân sách cơ chế ≈ +5% tương đương. Q 1,10 cộng cơ chế cho bên khắc thắng **67%** duel cùng cảnh, Q 1,15 cho 69%, E cũ 1,25 cho 79%.
3. **%HP bỏ qua Áp Chế bị cấm.** Mọi hiệu ứng %HP (Căn Thương, lao 25% HP của SURV) nhân thêm 0,5^(chênh cảnh) khi người đánh thấp cảnh hơn.
4. **Trần tổng Ω** (mọi nguồn ngoài cảnh giới, tấn công): `Ω = M_thẻ × Q × (1 + DS_Sát) × [Bản Thể U1] ≤ 1,60`. Sim C2: M_thẻ max 1,34 (Lang party) × 1,10 × 1,035 = **1,53** trong MVP. Có Bản Thể U1 ×1,10 thì 1,68 → khi đó **Bản Thể phải bớt còn ×1,04**, hoặc M_thẻ bị kẹp ở 1,30. Ghi vào checklist U1.
5. Crit giữ nguyên (5% × 1,5). Tốc tổng từ mọi nguồn trong ±15%.

### PROG-13 (sửa PROG-R2-04): Di Sản — "Đạo Chủng"
**Luật cố định (tôi đề xuất, không cần người dùng chốt):**
- Kích hoạt khi **Viên Mãn**. Pool = mọi thẻ đã nhận trong đời (trừ Thâm Hóa). Random **3 không lặp, trọng số đều** (lite rút 3 trong 4 thẻ, full rút 3 trong 6). Chọn 1 thẻ, thẻ đó thành **Đạo Chủng** giữ tên và **trục** của thẻ gốc.
- Đạo Chủng **không phải bản sao thẻ** (nếu là bản sao thì đời mới bắt đầu với Bậc III). Nó là một hiệu ứng nhỏ theo trục, **dịch theo động từ của tộc đang chơi**:

| Trục | Phẩm Sơ (Viên Mãn lite) / Thâm (full) | Mộc | Lang | Nghĩ | Oa | Kê |
|---|---|---|---|---|---|---|
| **Sát** | +2% / +3,5% sát thương | gai/rễ quất | Lang Nha, Xé | Lính | Quăng Lưỡi | Hạ Cánh Đạp, mổ |
| **Hộ** | −3% / −5% sát thương nhận | Thân, Tâm Rễ | thân | Hậu + Lính | thân | sau khi đáp 2s: ×2 giá trị |
| **Sinh** | +5% / +8% hồi | hồi Tán, Thủy | hồi khi ăn xác | Lính hồi sinh nhanh hơn | hồi trong nước nông | No từ Bới |
| **Hành** | +3% / +5% (trong trần Tốc ±15%) | thời gian Vươn rễ/ô | Tốc chạy | Tốc khi Tha | CD Nhảy Vọt | CD Sải Cánh |
| **Thức** | +8% / +12% | Rễ Cảm/Thần Thức | tầm Đánh Hơi | Thần Thức | tầm Rung Nước | tầm Báo Tin |
25 dòng data. Ô nào cũng dịch được. Cùng tộc hay khác tộc đều như nhau (không thưởng việc chơi lặp một tộc, giữ tinh thần G). Phẩm Sơ ≈ 0,6× Thâm, nên **tính theo giờ thì Sơ/h ≈ Thâm/h**: farm lite không lợi hơn.
- **Đời mới:** Đạo Chủng có hiệu lực từ C1. Tối đa 1 Đạo Chủng mỗi trục.
- **Nhân vật Viên Mãn:** thành **Hóa Tích** (WORLD-12) + trang Biên Niên. Không chơi tiếp, người chơi chọn tộc mới ngay (≤20s tới khi điều khiển).
- **1.0:** khi tộc lite có C4 thì Viên Mãn của tộc đó dời sang C4. Đạo Chủng Sơ đã có vẫn giữ.

**Cần người dùng chốt 1: trần cộng dồn**
| PA | Luật | Chênh với người mới cùng cảnh (win-rate) | Retention / độ sâu |
|---|---|---|---|
| S1 (SURV/PX) | 1 ô, Viên Mãn mới thì **thay** cái cũ | ≤ +5% → ~54% | Đơn giản nhất. Sau lần Viên Mãn thứ 2 hết mục tiêu dài hạn |
| **S2 (PROG khuyến nghị)** | **Sổ Đạo Chủng** vĩnh viễn (sưu tập). Ô trang bị: **1** → **2** (sau 3 lần Viên Mãn ở ≥2 tộc) → **3** (sau 6 lần ở ≥3 tộc). **Ô 3 chỉ nhận Hành/Thức** | ô 1–2 (Sát 3,5% + Hộ 5%): ≈ ×1,09 → ~56% (sát ngưỡng HF2 ≤55% của PX; nếu vượt thì Thâm Sát 3,5% → 3%). Ô 3 không thêm sức chiến đấu | Có mục tiêu khoảng 16–30h. Điều kiện "≥2/≥3 tộc" đẩy người chơi đổi tộc (G) |
| S3 (WORLD) | Tối đa 3 Đạo Chủng, đầy thì thay. Không có điều kiện tộc | ≈ ×1,12 → ~58% (vượt HF2) | Dễ hiểu. Snowball nhẹ |

**Cần người dùng chốt 2: đời sau chết giữa chừng thì Đạo Chủng có mất không**
| PA | Luật | Sim D: Đạo Chủng còn sau 10 đời (p = 0,7) | Nhận xét |
|---|---|---|---|
| **L1 (PROG/SURV/PX khuyến nghị)** | **Không mất.** Sổ là vĩnh viễn, mỗi đời trang bị lại | 7,0 | Chết đã mất trắng sức mạnh của đời đó. Mất thêm Đạo Chủng là phạt hai lần |
| L2 (WORLD) | Mất **hết** Sổ (Mộng Hỏa tan thì Đạo Chủng tan) | 2,2 (p = 0,55: 1,2) | Viên Mãn rất nặng ký. Nhưng ô 2–3 gần như không bao giờ mở, và P1 sẽ dồn sang chơi Mộc |
| L3 (lai) | Sổ không mất. Đạo Chủng **đang trang bị** của đời vừa chết thì **"Ngủ"** trong 1 đời kế tiếp (không trang bị được), và hiện thành Hóa Tích mờ ở chỗ chết | ≈7,0 (chỉ bị khóa tạm) | Có cái giá và đúng lore của WORLD, không xóa vĩnh viễn. Chi phí +0,05 (một cờ cho mỗi Đạo Chủng) |
Tôi khuyến nghị **S2 + L1**. Nếu người dùng muốn Viên Mãn nặng ký hơn thì chọn **L3**, không chọn L2.

### PROG-14 (sửa PROG-05): "Giai đoạn cuối" ở MVP + lập trường lite C3
| Nhân vật | Giai đoạn cuối | Kiếp Viên Mãn (template sẵn có) | Phút Mid (không chết) |
|---|---|---|---|
| Linh Mộc, Lang | Đỉnh C4 Hậu kỳ | Template Phi Thăng Kiếp I/Trung Kiếp (lôi + Tâm Ma sao chép 3 nút), 2' | 218' |
| Nghĩ, Oa, Kê | Đỉnh C3 Hậu kỳ | Cùng template, 2'. Tâm Ma sao chép BN1/BN2/A1 (đủ 3 nút ở C3) | 116' |
Phi Thăng Kiếp I của lite **được thay bằng Kiếp Viên Mãn**, không còn bị khóa. Câu "Đạo này còn nảy mầm" thay bằng câu của WORLD: *"Ngươi đã đi hết con đường lúc này cho phép."*

**Lập trường: lite = C3, không phải C2.**
1. **F cần pool đủ để random.** C3 có 4 thẻ (rút 3 trong 4). C2 chỉ có 3 thẻ, tức chọn 3 trong 3, không còn ngẫu nhiên.
2. **Áp Chế n=9 ở Hạ Lâm là đỉnh C3 Hậu.** Lite Viên Mãn đúng ở trần sức mạnh của vùng có nhiều PvP nhất. Ở đó lite C3 đứng ngang Mộc/Lang C4 ghé xuống, nên ma trận Q được cảm thấy thật. Nếu cap C2 thì lite luôn thấp hơn ≥1 cảnh (×1,77), và ma trận thành trang trí (đúng như SURV chỉ ra).
3. **Kiếp Viên Mãn cần 3 nút cho Tâm Ma**, mà nút thứ 3 (A1) mở ở C3. Độ kiếp C3 nằm trong danh sách "không bao giờ cắt" của PX.
4. **Căn Thương của Nghĩ mở ở C3** (PROG-16). Cap C2 thì Tâm Rễ không còn kẻ đe dọa nào ngoài lửa, hạn, sét.
5. **Thời lượng:** đời C2 sau khi nén chỉ 50'. Quá ngắn để có bản sắc, và cho Đạo Chủng mỗi 50' (dễ farm).
Chi phí: +0,45 (PX), đã có một phần trong PROG-08.
**Fallback nếu cổng tuần 30 trượt:** lite = C2. Mốc đổi thành M1 C1 Trung · M2 C1→2 · M3 vào C2 Hậu. Viên Mãn = Tiểu Kiếp đỉnh C2, Tâm Ma bỏ. D và F vẫn chạy (3 thẻ, F chọn 3 trong 3). Tiết kiệm −0,45.

### PROG-15 (sửa PROG-04): Bảng tên cảnh giới §6.2
Nhãn Hành theo PROG-01b. Cột Linh Thử chỉ dùng cho FTUE (C1–C2 kịch bản). WORLD có quyền đổi tên.
| C | Khung | Linh Mộc | Lang | **Linh Nghĩ** | **Linh Oa** | **Linh Kê** |
|---|---|---|---|---|---|---|
| 1 | Khai Linh | Manh Nha | Ấu Lang | Noãn Nghĩ | **Khoa Đẩu** (nòng nọc) | Phá Xác |
| 2 | Luyện Khí | Trát Căn | Lang Nha | Công Nghĩ | **Thoát Vĩ** (rụng đuôi) | Khai Vũ |
| 3 | Trúc Cơ | Thành Tán | Lang Cốt | Khai Sào | **Thượng Ngạn** | Báo Hiểu |
| 4 | Kết Đan | Ngưng Tâm Mộc | Lang Đan | Nghĩ Đan [1.0] | Thiềm Đan [1.0] | Kê Đan [1.0] |
| 5 | Hóa Hình | Thụ Nhân ‖ Cổ Mộc Yêu | Lang Nhân ‖ Yêu Lang | Nghĩ Nhân ‖ Yêu Nghĩ | Oa Nhân ‖ **Kim Thiềm** | Kê Nhân ‖ **Xích Kê** |
| 6 | Nguyên Anh | Mộc Hồn | Nguyệt Lang Hồn | Nghĩ Hậu Hồn | **Thiềm Cung Hồn** | Chu Tước Hồn |
| 7 | Thành Thần | Mộc Thần | Lang Thần | Nghĩ Thần | Thiềm Thần | Chu Tước Thần |
Tên gắn với cơ chế: Oa C2 *Thoát Vĩ* là lúc lên cạn được (Ẩm bắt đầu), Kê C3 *Báo Hiểu* gắn với Báo Tin/Gáy Bình Minh, Nghĩ C3 *Khai Sào* là lúc có Tổ Phụ và Căn Thương. Bỏ cột Khuẩn, Linh Thảo, Lộc, Trùng [Post] cũ. Bách Thảo là một Đạo của Linh Mộc nên không cần cột riêng.

### PROG-16 (mới): Số liệu Nghĩ — Lính và Căn Thương
- Công hiệu dụng = Công Hậu × (1 + 0,15 × Lính sống). 3 Lính → ×1,45. Có Lính Thứ Tư → ×1,60, đi kèm HP Lính −15%. Lính 12% HP Hậu, theo tầng. Hồi sinh ở tổ 20s, hoặc tại chỗ mất 6 No.
- **Căn Thương (A1 Đục Rễ, mở C3):** 0,33% Tâm Rễ/s cho mỗi Lính, tối đa 3 Lính (1%/s). **Chỉ chạy khi cây đang Mộc Tàn** (Thân = 0, tức đã có ai làm cây Đổ). Mộc Tàn ×2 → 2%/s, **tức 50s, đúng mốc "3 Lang + Độn Thử, chết thêm 50s"** của v1.0. Nhân thêm 0,5^(chênh cảnh) nếu Nghĩ thấp cảnh hơn. Cây offline bất tử, nên không có chuyện kiến một mình giết cây offline. Đáp ứng điều kiện "cần phối hợp" của PX.

---

## Những thứ tôi mượn từ người khác
- **SURV:** bảng địa hình nước, Ẩm, Trọng Thương C3+, chống gank theo cảnh, quy tắc "mỗi bộ thẻ có lựa chọn sống sót", Lính tốn No. Đưa vào sim B và PROG-08.
- **WORLD:** Niên Luân (vòng gỗ), Đạo Chủng, 5 trục Sát/Hộ/Sinh/Hành/Thức, Hóa Tích, câu "Chết giữa đường, ngươi trả lại cho rừng. Đi hết đường, rừng trả lại cho ngươi.", nhãn Hành theo Tứ Tượng, Hạ Cánh Đạp, tên Khoa Đẩu/Thoát Vĩ/Thượng Ngạn (đã Hán-Việt hóa).
- **PX:** luật data-only cho A1 của lite, HD1–HD3/HF2 làm ngưỡng kiểm, Q áp cả lên AI, ý "thưởng cho tộc vắng người", phẩm di sản thấp hơn cho lite.

## Lập trường giữ vững (và vì sao)
1. **Kiếp thất bại không phải chết.** Đây là núm vặn lớn nhất: P(Viên Mãn đời đầu) 13% → 68–75%. Tôi sẽ BLOCK nếu FINAL ghi kiếp = chết.
2. **Lite = C3** (5 lý do ở PROG-14, có fallback C2 đã thiết kế sẵn).
3. **Nén CT_cảnh ×0,5.** Không nén thì Mid cần 11,4h cho một lần Viên Mãn full, kể cả khi đã có mọi lớp bảo vệ.
4. **Một ô Q ×1,10, trần Ω ≤1,60, cấm nhân chồng.** Bất kỳ hệ số khắc mới nào cũng phải đi qua ô Q.
5. **Đạo Chủng là hiệu ứng theo trục, không phải bản sao thẻ.**

## Điều tôi sẵn sàng đánh đổi
- Q 1,10 → **1,15** nếu team bỏ bớt cơ chế khắc (còn ≤4 cặp có cơ chế).
- Hợp Đạo (6 thẻ) → hoãn sang 1.0 nếu ngân sách cần: tiết kiệm ~0,1, Lang/Mộc còn 5 lượt chọn (sim: vẫn ≥3 thẻ mỗi mốc nhờ Thâm Hóa).
- Mốc M4 (vào C3 Hậu) của lite có thể bỏ nếu PX cần −0,05. Khi đó F rút 3 trong 3.
- Tên thẻ và tên cảnh giới: nhường hết cho WORLD.
- S2 → S1 nếu người dùng muốn đơn giản nhất. L1 → L3 nếu người dùng muốn Viên Mãn nặng ký hơn. **Không đổi sang L2** trừ khi alpha cho thấy retention sau chết ≥ HE1.
