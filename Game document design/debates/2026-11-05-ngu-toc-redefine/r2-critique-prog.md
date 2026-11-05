# R2 Critique — PROG
Sim: `sim/prog_r2_sim.py` (+ `prog_r2_sim_output.md`). Đã đưa vào Bổ sung 1, 2, 3 của người dùng.

## Tự phê (PROG R1)
- **Rút lại Linh Thử làm đại diện Thú.** Cả 3 người chọn Lang, và họ đúng: Lang là bộ kỹ năng chiến đấu duy nhất đã có C1–C4 + sim PvP; vai "Thú khắc Mộc / săn" cần Lang. Linh Thử thành AI + Tiền Thân FTUE.
- **Rút lại ma trận Hành của tôi** (Trùng=Hỏa, Thú=Thổ) và **cách tôi áp E ×1,25 thẳng lên cấp tộc**. Tôi còn gắn thêm ×1,25 theo từng cặp (mổ Tán, săn Lý nông, ăn Lính), nên chồng lên E thành ×1,56. Đó là lỗi.

## Phát hiện số liệu quan trọng nhất (ảnh hưởng cả 3 bản)
**"Trần ×1,32" trong FINAL không chứa E.** r3-revision-prog xác nhận 1,32 = Huyết Cuồng 1,20 × Bản Thể 1,10 (không crit, không E). Trần thực = 1,32 × 1,25 = **1,65**, chỉ còn 7% so với 1 cảnh (×1,77). WORLD ("≤×1,15 nằm trong trần 1,32") và PX ("hệ số khắc nằm trong trần 1,32") đều hiểu sai: cộng thêm ×1,15 là **1,90 > 1,77**, tức bị khắc còn mạnh hơn chênh một cảnh. SURV chưa tính "Gai ×1,5 lên bầy": 1,32×1,25×1,5 = **2,48**.

| Quy tắc | Trần tấn công | Với 1,77 |
|---|---|---|
| E nhánh (v1.0) | 1,65 | ok |
| E × tộc-khắc 1,15 | 1,90 | vượt |
| E × Gai 1,5 (SURV) | 2,48 | vượt |
| **max(E, tộc-khắc)** | 1,65 | ok |

Win-rate duel cùng cảnh (σ hiệu chỉnh từ bảng PvP v1.0): tộc ×1,10/0,91 → bên khắc thắng 64%; ×1,15/0,87 → 69%; E 1,25/0,80 → **79%**; E nhân tộc → 91%. Mở rộng khắc ra cấp tộc làm **40% cặp gặp nhau (10 khắc/bị khắc trong 25 cặp có thứ tự)** chịu swing đó, trong khi v1.0 chỉ áp từ C3 cho 3 loài.

**Luật tôi đề xuất (PROG-R2-01), áp cho cả team:**
1. Khắc cấp tộc là **cơ chế** (chặn, đục, Ướt, lộ vị, tài nguyên). Không có hệ số sát thương riêng.
2. Hệ số sát thương chỉ tồn tại ở **một ô Q = max(E nhánh, hệ số cơ chế) ∈ {0,80; 1; 1,25}**. Không nhân. Mọi "×1,5 Gai", "×1,25 cắn trong nước" phải đổi thành CC/Tốc/CD, hoặc nằm dưới 1,25 và tính vào ô Q.
3. Tộc lite chưa có Huyết Mạch → không có E, chỉ có cơ chế. Tránh "một người hai Hành" (Lang tộc Kim nhưng nhánh Huyết Lang là Hỏa).
4. Tổng mọi nguồn tấn công ≤ 1,65 × (1 + di sản ≤ 5%) = 1,73 < 1,77.

**Ma trận (b): ba cách xếp khác nhau chỉ là đổi nhãn.** Cả ba là vòng 5 (sinh i→i+1, khắc i⊣i+2). Mệnh đề cấu trúc: với mọi cặp sinh (i, i+1), bên nhận khắc đúng kẻ khắc bên cho, nên không tộc nào khắc cả bốn hay bị bốn khắc, và không cặp nào kín hoàn toàn. Vì vậy chọn theo chủ đề: **SURV (Thú=Kim, Vũ=Hỏa, Trùng=Thổ, Thủy, Mộc)** khớp Tứ Tượng (Bạch Hổ, Chu Tước, Huyền Vũ, Thanh Long) và khớp động tác: Thú cào Thân (Kim khắc Mộc), Vũ lao xuống Thú (Hỏa khắc Kim), Thủy làm Ướt Vũ. Chọn SURV; WORLD/PX dùng Thú=Hỏa, Vũ=Kim hợp lý nhưng "chim khắc cây" yếu hơn "sói cào thân".

## Về SURV
**Giữ:** SURV-03 (cơ chế, không nhân E) và SURV-04 (Căn Thương → Linh Nghĩ); controller chung SURV-01; Linh Thử → Tiền Thân; 0 need mới.
**Mượn:** luật "khắc là cơ chế" làm nền PROG-R2-01.
| ID | Mức | Vấn đề | Tình huống | Thay thế / kiểm chứng |
|---|---|---|---|---|
| SURV-03 (Gai ×1,5, cắn ×1,25, lao 25% HP) | Major | Vi phạm ô Q (xem trên); 25% HP Thú nhỏ là burst %HP bỏ qua Áp Chế | Trĩ C1 lao Lang C4: ăn 25% | Lao = choáng 1s + gây sát thương theo Công, chịu Áp Chế; Gai ×1,5 → ×1,25 vào ô Q hoặc đổi thành Tốc −20% |
| SURV-01/06 Quy + nước sâu | Major | Nước sâu "không combat dưới nước" = vùng bất tử; cá làm mồi cho Quy → farm CT an toàn vô hạn | Quy lặn hồ Linh Nhãn, ăn cá, chờ | Nguồn No/CT của Quy nằm ở nước nông/bờ; sâu chỉ lánh ≤20s (tốn Thể Lực); AFK ×0,2 áp dụng. Test: CT/giờ ở sâu ≤ 0,3 so với bờ |
| SURV-04 Căn Thương Nghĩ 1%/s | Major | %HP không phụ thuộc cảnh: Nghĩ C2 giết cây C4 khi Mộc Tàn (Đổ cần Lang phá Thân trước). 1%/s×2 (Mộc Tàn) = 50s, bằng Độn Thử cũ nhưng mở sớm hơn | Nghĩ C2 + Lang C4 giết Linh Mộc C4 | Căn Thương nhân 0,5^(chênh cảnh) khi người đánh thấp hơn; mở từ **C3** (A1). Đây là lý do Trùng cần C3 (xem (e)) |
| SURV scope | Minor | −0,6 Linh Thử và −0,3 Kiến chưa đối chiếu với dòng #4, #5c của §16.1 (Linh Thử 1,0, Kiến lite 1,0) | — | PX chốt |

Câu hỏi: "≥3 Nghĩ" là 3 follower của một người hay 3 người chơi? Nếu follower thì Trùng solo thành Độn Thử.

## Về WORLD
**Giữ:** WORLD-02 (Cụ Ngao, Trung Ấm trên mặt nước; sẽ phải sửa theo E), WORLD-04 (nấm = da Linh Mạch), WORLD-06 (thế mạnh 5 tộc + luật "lấy giá trị lớn hơn").
**Mượn:** Oa "Quăng Lưỡi" kéo/chậm (kỹ năng Thủy cần động từ chủ động).
| ID | Mức | Vấn đề | Tình huống | Thay thế / kiểm chứng |
|---|---|---|---|---|
| WORLD-06 | **Blocker** | "≤×1,15, nằm trong trần 1,32" sai (1,90 > 1,77) | Huyết Lang khắc Thiết Mộc + khắc tộc | Áp PROG-R2-01 |
| WORLD-05 lite C2 | Major | C2 = 2,2 phiên Mid (~2,6h), chưa có Ngộ Đạo draft (bắt đầu C3 Hậu). Trái Bổ sung 2: cần 3–5 lựa chọn mỗi mốc | Oa C2: không có lựa chọn nào ngoài 2 Bản Năng cố định | Lite = C3 (xem D) |
| WORLD-06 "Mộc→Thú sinh: Thể Lực +20%" | Minor | Thú ăn Quả Ước +15 No đã có; thêm hồi Thể Lực chồng thế mạnh | — | Chọn một |
| WORLD-07 Quạ Già, Thiên Tài Địa Bảo | Minor | OK; nhưng gán Kê "đánh dấu Tâm Rễ 30s" cho Vũ khắc Mộc là thông tin, không phải sát thương, tốt, nhưng Mầm-Neo phá ×2 là sát thương %HP | — | Giữ đánh dấu, bỏ ×2 |

Câu hỏi: Oa hay Quy? Tôi nghiêng **Thanh Oa** (kỹ năng chủ động kéo/nhảy, không dính "bất tử dưới nước", lưỡng cư nên không bị nhốt); Lão Quy/Cụ Ngao giữ cho NPC để NPC khác hẳn loài chơi được.

## Về PX
**Giữ:** PX-04 cổng 16/30 và danh sách "không bao giờ cắt"; HN4/HN6/HN8 làm tiêu chí; PX-07 (Linh Thảo → Post, tên Dược Thảo).
**Mượn:** HN3 (8–32% lượt chọn mỗi tộc) làm KPI cân bằng chính.
| ID | Mức | Vấn đề | Tình huống | Thay thế / kiểm chứng |
|---|---|---|---|---|
| PX-03 "khắc nằm trong trần 1,32" | **Blocker** | Cùng lỗi WORLD-06 | — | PROG-R2-01 |
| PX-01 lite C1–C2, không Huyết Mạch | Major | Với Bổ sung 2, C2 chỉ có 0 lựa chọn Ngộ; "Đạo Quả lite ≤39" nay vô nghĩa vì Hồi Ức/Đạo Quả sức mạnh bị bỏ | Chạm trần sau ~2,6h | C3 lite, 3 lựa chọn; ngân sách C3 tính lại (dưới) |
| PX-04 +1,45 | Major | Ước tính 0,5–0,6/loài thấp nhất bản (SURV 1,0; PROG 1,5; WORLD 0,75+0,5 nước). Chưa tính D–G | — | PX tính lại: đơn giá lite C3 = controller chung + 3 kỹ năng + 3 thẻ/mốc ×3 + 1 cơ chế tộc ≈ **0,9–1,0** |
| PX-03 chỉ 3 cặp có cộng sinh thật | Minor | Chấp nhận (scope), nhưng 7 cặp còn lại phải có ít nhất 1 cơ chế đo được, không chỉ hệ số vì hệ số bị cấm | — | Mỗi cặp: 1 cơ chế bằng data |

Câu hỏi: ngưỡng "đệm" mới sau khi cộng D–G (xem cuối)?

## (c)(d)(e)(f) tóm tắt lập trường
- **(a)** Thú=Lang. Thủy=Oa (tạm), Vũ=gà rừng **Linh Kê** (Phi Lược/lướt 2,5s, không đánh/ăn khi lướt; SURV & PROG đồng ý, hợp với cả Trĩ). Trùng=Linh Nghĩ. Đừng đặt thêm tên mới.
- **(e)** Lite = **C3** cho cả ba (không Phi Thăng Kiếp I). Ngoại lệ fallback: Vũ C2. Lý do: Căn Thương cần C3; Ngộ Đạo cần ≥3 mốc.
- **(f)** Con số 0,7–3,5 lệch vì đơn giá lite 0,5–1,5; tôi đề nghị cùng một danh sách việc/đơn giá, PX chốt.

---

## D. Cấu trúc lựa chọn (PROG-R2-02) — thay Huyết Mạch/Keystone/Bản Năng của §6.4–6.5
**Khung "Đạo Lộ"** (chung 5 tộc): mỗi tộc có **3 Nhánh cố định** (tên theo tộc) × 3 Bậc. Lựa chọn tại **mỗi đột phá cảnh** (độ kiếp thành công), không phải mỗi tầng (tránh choice paralysis; mobile thấy ≤ 1 màn chọn/giờ).

| Mốc | Số thẻ hiện | Cấu thành | Lite C3 | Full C4 |
|---|---|---|---|---|
| C1→2 | 3 | Bậc 1 của 3 nhánh | ✔ | ✔ |
| C2→3 | 4 | 3 nhánh (Bậc kế tiếp của nhánh đang theo, hoặc Bậc 1 nhánh mới) + 1 **Thiên Phú Tộc** | ✔ | ✔ |
| C3→4 | 4 | tương tự | — | ✔ |
| Hậu kỳ C4 | 5 | thêm **Hợp Đạo** (cần ≥2 nhánh) | — | ✔ |
- **Kế thừa:** Bậc k chỉ xuất hiện khi có Bậc k−1 cùng nhánh; Hợp Đạo là thẻ lai.
- **Hiệu quả đến hết đời:** mọi thẻ dạng % hoặc theo Công/cảnh, **cấm số cố định** (+20 HP); thêm quy tắc kiểm: giá trị ở C4 ≥ 0,8× lúc nhận. Thẻ Bậc 1 có "dạng mạnh lên" ở C4 (đổi tên, tăng cấp tự động).
- **Pool cố định, hiển thị trước** (học được, build có tên); random chỉ ở Di Sản (F). Thẻ gợi ý có sao theo hành vi (giữ "learn-by-doing").
- **Số lượng tối thiểu MVP:** lite = 3 mốc × (3+4+4 thẻ khác nhau, 9 thẻ viết thật: 3 nhánh × 3 bậc). Full = 3 nhánh + Thiên Phú + Hợp Đạo.
- **Sim cây:** lite 3 pick → **19 build khác nhau**, power max/min = 1,23; full 4 pick → 28 (1,21); 6 pick → 34 (1,20). Chênh power ≤1,25 nằm trong ngưỡng chấp nhận được (so với E 1,25). Chưa có "build chết" theo tiêu chí đã ghi; cần playtest cho trap choices.
- Cắt: Keystone C4 → thẻ Hợp Đạo (dùng chung template), Huyết Mạch 6 → 3 nhánh/tộc ở dạng thẻ, Ngộ Đạo draft riêng bỏ. Số thẻ viết: Mộc 9+2+1, Lang 9+2+1, ba lite 9+2 mỗi tộc ≈ **44 thẻ**, so với 42 node + 18 Minor của v1.0: **ngang hoặc ít hơn**.

## E. Chết = làm lại hoàn toàn (PROG-R2-03): vấn đề số liệu
Một đời C4 Mid ≈ 691 CT ≈ 11,5h (1 CT/phút); lite C3 ≈ 6,1h; C2 ≈ 2,6h. Hồi Ức, Đạo Quả sức mạnh, Túc Tuệ, Hậu Duệ biến mất, nên **không còn catch-up**. Monte Carlo (hazard theo giờ, tăng dần theo tiến trình, Ấu Linh giảm ở 20% đầu):

| Độ dài đời | h=0,05/giờ | h=0,10 | h=0,20 |
|---|---|---|---|
| 6,1h (lite C3 hiện tại) | 74%, 7,5h/hoàn thành | 54%, 9,1h | 30%, 13,8h |
| 11,5h (C4 hiện tại) | 56%, 16h | **32%, 24h** | **10%, 55h** |
| 5,5h (nén) | 76%, 6,4h | 58%, 7,6h | 33%, 10,9h |
Kết luận: giữ đường cong hiện tại thì người chơi PvP (h≥0,1/giờ) **chỉ hoàn thành C4 1 lần trong 3**, và P3/P1 hoàn thành chủ yếu sau nhiều giờ vô ích. Đề xuất:
1. **Nén đường cong ×0,5 (một đời C4 ≈ 5,5–6h, lite C3 ≈ 3h, tức "một run")**; chỉnh bằng hằng số CT_cảnh, không đổi công thức. Mục tiêu: P(hoàn thành) ≥ 55% ở h=0,1.
2. **Độ kiếp thất bại không phải chết:** lùi 1 tầng, giữ thẻ (đã có Mộc Tàn tương tự). Chỉ chết khi HP=0 trong kiếp.
3. **Ấu Linh kéo dài tới hết C2** (không PvP mạnh vào C1–C2) và Hồn Hộ 10' sau sống lại giữ; chống gank = giới hạn mất: **chết ở C1–C2 mất <40 phút** là chấp nhận được.
4. Không tặng sức mạnh khi chết (đúng quyết định); thứ giữ: skin, Biên Niên, Mộ Linh, kiến thức, Codex, **mở khóa ngang** (tộc, thẻ cosmetic). Đạo Quả: bỏ vai "tiền mua sức mạnh", chỉ mua mở khóa ngang (tộc/skin/tên cảnh).
5. Cây offline bất tử, Sổ Sinh Năng không đổi (xác vẫn nuôi rừng).
KPI đề xuất: tỉ lệ rời game sau chết ở C3+ ≤ 25%; P(hoàn thành) ≥ 55%.

## F. Di Sản (PROG-R2-04)
- **"Giai đoạn cuối" MVP:** Mộc/Lang = vượt Trung Kiếp C4; ba tộc lite = vượt **Kiếp Viên Mãn C3** (template Tiểu Kiếp, thay Phi Thăng Kiếp I). Mọi tộc đều có đích hoàn thành.
- Sau hoàn thành: nhân vật **Phi Thăng thành Mộ Linh/Dấu Ấn** (NPC ngủ, đóng góp Linh Quỹ +3% vùng), người chơi chọn tộc mới (hoặc cùng tộc), bắt đầu C1.
- **Chọn:** hệ thống random 3 từ các thẻ đã nhận trong đời (≥4 thẻ; lite có 3–4, nên rút từ thẻ + Thiên Phú, nếu <3 thẻ thì chỉ hiện số có).
- **Mỗi thẻ có hai dạng:** *Lõi* (theo tộc) và *Dư Âm* (một trong 5 kênh chung: Sát/Hộ/Động/Hồi/Thức). Di Sản luôn mang **Dư Âm** và "dịch" theo chất tộc mới (G).
- **Trần:** Di Sản tích lũy trong Sổ; trang bị tối đa **1 ô (hoàn thành lần 1), 2 ô (lần 3), 3 ô (lần 6)**. Mỗi ô ≤ +2% kênh Sát và ≤ +5% các kênh khác; tổng Sát ≤ 5% (trần chung 1,73 < 1,77). Không cộng dồn cùng kênh quá 1 lần.
- **Mất khi chết giữa chừng?** Không mất khỏi Sổ, chỉ ô trang bị của đời đó bị tiêu (đã áp dụng lên đời hiện tại; đời sau chọn lại). Như vậy chết không xóa tài sản đã hoàn thành, nhưng không thể gank để "đánh mất" cả di sản.
- **Đối chiếu "không mang sức mạnh":** Di Sản là phần thưởng hoàn thành do người dùng chốt, được giới hạn ngang (≤5%, ưu tiên tiện ích).

## G. Chất riêng mỗi tộc (PROG-R2-05) trên khung chung
**Chung (~85% code/UI):** controller mặt đất Lang, HUD 4+1, needs, cảnh giới, Đạo Lộ thẻ, độ kiếp, Di Sản.
**Riêng (1–2 cơ chế, đo được, chi phí tuần-người):**
| Tộc | Động từ riêng | Nhịp | Cơ chế riêng (data/Script) | Chi phí |
|---|---|---|---|---|
| Mộc | **Bám rễ** | chậm, lên kế hoạch | Có sẵn (rễ, Tán, Neo) | 0 (đã có) |
| Thú | **Vồ / Săn** | burst, đuổi | Có sẵn (lao, Hang) | 0 |
| Trùng | **Gọi bầy** | số đông | k follower (Công = base×(0,5+0,1k)); "Tha" mang mồi/mầm/xác về tổ | 0,25 |
| Thủy | **Dẫn nước / Kéo** | chủ động theo dòng | Quăng Lưỡi kéo/chậm; "ẩn và hồi" ở nước nông; Tưới | 0,3 |
| Vũ | **Lướt / Thấy** | ngắt quãng, trinh sát | Phi Lược; Thần Thức +30–50%, ping party | 0,25 |
Ước tính này đã nằm trong đơn giá lite ≈ 0,9–1,0.
**Dịch Di Sản:** Dư Âm → Động = Tốc bước của Thú, CD lướt của Vũ, tốc bò rễ của Mộc, tốc lan bầy của Trùng, tốc bơi của Thủy. Tương tự cho 4 kênh còn lại; bảng dịch 5×5 = 25 ô data, ~0,1 tuần.
Kiểm chứng "mới mẻ": HN2' = ≥70% tester mô tả được "tộc nào chơi khác thế nào" trong một câu sau 1 đời mỗi tộc.

## Xung đột liên domain
| Xung đột | ID | Lập trường | Gợi ý |
|---|---|---|---|
| Hệ số khắc vs trần 1,77 | SURV-03, WORLD-06, PX-03 | Một ô Q, tối đa 1,25 | PROG-R2-01 |
| Thủy là Quy hay Oa; nước sâu bất tử | SURV-06, WORLD-05, PX-01 | Oa; nước sâu chỉ lánh | Test CT/giờ |
| Lite C2 vs C3 | SURV, PROG, WORLD, PX | C3 (D cần ≥3 mốc, Căn Thương C3) | PX tính lại |
| Reset hoàn toàn vs độ dài đời | Bổ sung 2 | Nén ×0,5, kiếp không chết | PX/SURV |
| Trùng và Căn Thương | SURV-04, PX-02 | Mở C3, giảm theo chênh cảnh | Sim sau R3 |

## Top 3 điều team phải chốt
1. **Luật ô Q (max, không nhân; 1,65 + di sản ≤ 5%).** Bác bỏ "trần 1,32 chứa E" trong tài liệu hiện tại.
2. **Lite = C3 + độ dài đời ×0,5 + độ kiếp thất bại không chết** (cùng nhau trả lời Bổ sung 2, tức một đời ≈ 3h/6h; sau đó PX tính lại ngân sách với đơn giá lite ≈ 0,9–1,0 và 44 thẻ).
3. **Ma trận Hành theo SURV (Thú=Kim, Vũ=Hỏa, Trùng=Thổ)** + Thanh Oa cho Thủy + Căn Thương mở C3.
