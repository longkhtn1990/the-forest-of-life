# R2 Critique — PX

Quy ước: tuần-người (t-n). Mọi ước tính dưới đây là bottom-up của PX (mục "Ngân sách thực" cuối file), đối chiếu với `FINAL.md` v1.0 §16.1. Quyết định "5 tộc × 1 nhân vật" là chốt; tôi chỉ gắn cờ rủi ro và fallback.

## Tự kiểm R1 của PX (trước khi phê người khác)
- **PX-04 thiếu thực tế.** Tôi tính 3 loài lite C1–C2 = 1,65 (0,55/loài). Bottom-up cho ~0,7–0,9/loài (sprite+anim 0,3, cơ chế riêng 0,2–0,4, 2 skill+VFX+SFX, netcode, balance) cộng 0,55 chung (UI bánh xe, tên cảnh giới, sim). Tôi nâng net từ +1,45 lên **+2,2**.
- **Cap C2 làm lite chưa từng thấy Tiểu Kiếp** (v1.0 liệt kê độ kiếp vào "không bao giờ cắt"). Đây là điểm PROG/SURV đúng hơn tôi (xem PROG-05).
- **Fallback "bánh xe 3 lớn + Xem thêm" (PX-10) sai:** với 5 thẻ, ẩn 2 thẻ làm mất khám phá. Đổi: 5 thẻ cùng lúc, mỗi thẻ ≤6 chữ nêu vai.

---

## Về SURV
### Giữ lại (Keep)
- SURV-03: mỗi tộc "khắc 1, bị khắc 1, nuôi 1, được nuôi 1" và **khắc là cơ chế, không nhân thêm hệ số E**. Đây là kỷ luật cân bằng đúng.
- SURV-04: phân giải = quy trình; nấm = props. Chi phí 0, sạch.
- SURV-06: không thêm need, không oxy, không combat dưới nước. Cắt đúng chỗ cần cắt.
- SURV-02: Linh Thử → Tiền Thân FTUE, giữ nhịp D12.
### Mượn (Steal)
- SURV-06 cá bầy = f(Linh Quỹ) làm chỉ báo Khô Linh (H13) không cần UI mới. Dùng cho Thủy.
- SURV-01 "Một controller mặt đất chung" cho mọi loài lite: biến thành **luật ngân sách**: lite chỉ được dùng tối đa 3 primitive mới toàn MVP (dash/lướt, pull/kéo, follower-bầy).
### Phản biện
| ID | Mức | Vấn đề | Tình huống | Đề xuất / kiểm chứng |
|---|---|---|---|---|
| SURV-01 Quy (Thủy) | Major | Tốc 3,5 ô/s trên cạn (so Lang gấp đôi) nhưng nước chỉ ~3% map. Spawn Thủy ở Bìa có 1 suối: người chơi Quy đi bộ chậm tới nước trong 15' đầu | Phút 2–6 chỉ thấy rùa lê trên đất, đúng lúc quyết định D1 | Thủy MVP = **Oa** (ếch lưỡng cư, WORLD-05). Có động từ vui ngay giây 1 (Quăng Lưỡi kéo mồi). Quy giữ làm NPC |
| SURV-01 Trĩ | Minor | "Không đánh/ăn khi lướt, 40 Thể Lực, CD 10s" khá chặt; Vũ solo không có động từ thưởng | Gà chạy, lướt, không thấy lợi ích "tầm nhìn" khi một mình | Thêm phần thưởng solo: Thần Thức thấy **Linh Hạch trên xác trong 20 ô** (đã có Quạ cướp). Cost 0 |
| SURV-03 | Major | **10 cộng sinh opt-in = 10 cơ chế mới**: ~0,1–0,2 t-n mỗi cái = 1,0–2,0. SURV tính cả ma trận+nước chỉ 0,5 | Quy cõng Vũ qua đầm, Nghĩ đào Căn Thương, Lang vồ cá không phạt... mỗi cái cần code, UI gợi ý, test | MVP: **10 hệ số dạng data + 4 cộng sinh thật** (Mộc–Trùng Khế ước đã có, Thủy–Mộc Tưới, Trùng–Thú Mở Xác, Vũ–Thú ping). 6 còn lại [1.0] |
| SURV-03 hệ số | Major | Độc/Gai ×1,5 lên bầy, trong khi trần stress-test ×1,32 | Cây ×1,5 vs Nghĩ 3 Lính: Lính chết trong 1 chạm gai, Trùng vô dụng ở ô rễ | Tộc-khắc ≤×1,15 (WORLD/PX), áp **max(Hành tộc, E Huyết Mạch)**, không cộng |
| SURV-04 Căn Thương→Nghĩ | Major | "≥3 Nghĩ, 1%/s" khiến **Nghĩ đứng một mình giết cây** (1%/s = 100s). Mất nguyên tắc "cần phối hợp nhiều loài" | Một người chơi kiến 3 Lính lên Tâm Rễ khi chủ cây offline, cây chết lúc offline | Căn Thương 0,5%/s/Nghĩ chỉ chạy khi **Thú hoặc Vũ hạ phòng ngự** (Cào/Mổ Tán) trong 30s. Test: không solo-kiến nào giết cây không phối hợp |
| SURV §4 scope | Minor | Net +2,6 nhưng cắt bù "Gà/Ếch/Chim Sẻ lùi sau MVP" là AI/prop (chi phí đã ~0 nếu skin Hươu), không phải tiết kiệm thật | — | Chỉ tính cắt khi file dev tồn tại ở v1.0 |
### Câu hỏi cho SURV
Vũ ⊣ Thú "choáng 1s + 25% HP Thú nhỏ": với Lang (HP cao) có còn ý nghĩa? Số lần Ướt (−20% Tốc, CD ×1,5) của Vũ hạ cánh ở nước nông có biến nước nông thành bẫy Vũ (HN8) không?

---

## Về PROG
### Giữ lại (Keep)
- PROG-05: cổng lite tại C3 + quy đổi CT dư 100% sang Đạo Quả + Hồi Ức vẫn chạy. Chuyển "tường cụt" thành "đạo quả nảy mầm". Hay hơn "C2 Hậu" của tôi.
- PROG-03 stress-test E ×1,25 < cảnh ×1,77, trần ×1,32.
- PROG-02: sim phương sai theo thế mạnh.
### Mượn (Steal)
- PROG-05 cổng C3: thay PX-01 cap C2. **PX-01b**: lite = C1–C3 "data-only A1" (A1 là skill 1 tăng số, không VFX mới).
- Tooltip 3 icon quan hệ trên mục tiêu (PROG §5-5) thay cho "học ma trận".
### Phản biện
| ID | Mức | Vấn đề | Tình huống | Đề xuất / kiểm chứng |
|---|---|---|---|---|
| PROG-01 Thú = Linh Thử | **Major** | 3/4 bản chọn Lang. Không có sát thủ đất liền, mất persona P2 trong 5 đại diện; Thú "Cơ động+trữ" nhưng "trữ" (Kho Hạt/hang) đã bị cắt ở v1.0 | Hardcore vào Rừng chung chỉ có Thử 300 HP, Mộc, và 3 lite: không ai săn | **Lang**; Thử giữ Tiền Thân FTUE (cost ≈0,4 vì reskin controller Lang). Test VS: P2 chọn Thú ≥ 55% khi luân hồi |
| PROG-01 "Lang → AI −2,0" | Major | Hàng 3 của v1.0 (2,5) gồm **controller chung**, vẫn cần cho Thử/Nghĩ/Oa/Gà. Phần riêng của Lang ≈1,2–1,5 | Net +3,5 của PROG bị lệch lên/xuống 0,5–0,8 | PROG tách lại "controller" vs "Lang-only" |
| PROG-01 Lý (cá chép) | **Major** | Nhân vật **chỉ ở nước** (≈6–8% map) nghĩa là hai chế độ di chuyển + bản đồ nhỏ. Đã cần fallback "Oa" ngay trong R1 | Lý spawn ở suối; Rừng chung PvP chỉ khi ở nước 4.000 ô: vùng chết; không thể sang ao khác | **Oa**. Loại Lý khỏi MVP, đưa về [Post] (đã có "Vũ Môn" ở PX-08) |
| PROG-01 Tước | Minor | Chim sẻ không bay mà "Vỗ Cánh lướt" lệch kỳ vọng; người dùng nói "chim, gà". Gà rừng lướt ngắn tự nhiên hơn | Người chơi bấm chim sẻ, mong bay, thấy chỉ lướt 5 ô | **Gà rừng** (Kê/Trĩ). Hook "gà tu tiên" có sức lan truyền hơn |
| PROG-03 Hành gán | Minor | Thú=Thổ, Trùng=Hỏa, Vũ=Kim sinh ra chuỗi sinh Mộc→Trùng→Thú→Vũ→Thủy. Hai mắt xích sinh yếu về sinh thái: Trùng→Thú, Thú→Vũ (Hiệu ứng "lộ Linh Hạch 2s") | Casual đọc "Thú nuôi Vũ" không hiểu | Dùng thứ tự Mộc→Thú→Trùng→Vũ→Thủy (xem mục xung đột b) |
| PROG-05 lite 3 skill | Major | Kiến, Oa, Gà mỗi con 3 skill + 4 Bản Năng pool + Ngộ Đạo nghĩa là 9 skill mới + draft ở lite. Giá thực ≈ +0,45 ngoài 2 skill | Lite "chưa sâu" nhưng có Ngộ Đạo thì còn nhiều combinatorial | Lite: 2 Bản Năng + **A1 = skill 1 tăng số**, **không** Ngộ Đạo draft (chọn Bản Năng bằng Ấn) |
### Câu hỏi cho PROG
Hồi Ức khi Luân Hồi từ C4 xuống lite C3: kẹp trần ra sao để không "hạ cấp" gây ức chế? Đạo Quả lite có tạo exploit (farm lite C3 để ra Đạo Quả)?

---

## Về WORLD
### Giữ lại (Keep)
- WORLD-06 lõi: vòng sinh Mộc→Thú→Trùng→Vũ→Thủy→Mộc là chuỗi **trực quan nhất** (quả→thú→xác→bọ→chim; chỉ Vũ→Thủy yếu), và "hệ số khắc ≤×1,15, lấy lớn hơn không cộng".
- WORLD-06: khắc chủ yếu là **cơ chế** (chặn, đục, kéo, lộ vị). Gợi ý "chỉ bật 4 cặp mạnh" ở MVP: chấp nhận.
- WORLD-03: dòng Linh Tuyền Linh Nhãn → Bìa, "ngược dòng = vào trong". Wayfinding miễn phí.
- WORLD-04: Nấm "không mộng nên không nhớ", Tơ Nấm; WORLD-02 pool 60 câu nước.
### Mượn (Steal)
- WORLD-05 Oa "nước sâu = Hang" (tái dùng Hang của Lang). WORLD-03 3 bến cạn qua Đầm (chống vùng chết).
- WORLD-04 Mộng Ấn 1 bóng trên vũng nước.
### Phản biện
| ID | Mức | Vấn đề | Tình huống | Đề xuất / kiểm chứng |
|---|---|---|---|---|
| WORLD-05 FTUE kiến | **Major** | Kiến là nhân vật lite C1–C2 đang cần polish nhất; FTUE (đường cong Tiền Thân ×3, C2 ở phút 7) biến nó thành thứ được test nhiều nhất. Kiến chết không tạo đồng cảm bằng chuột | Phút 14: "chuột bị diều hâu bắt" đọc được ngay, "một con kiến của bầy" thì không. Cũng lệch D12 vừa chốt, chưa có dữ liệu thay | Giữ **chuột (Linh Thử)**. Nghiệm thu: VS H11 + HN-FTUE: ≥70% muốn chơi kiếp tiếp. Nếu có thời gian, A/B Kiến ở alpha |
| WORLD-05 "lite C2, fallback C1 + 1 skill" | Major | 1 skill không tạo được "vai" (Quăng Lưỡi, lướt, bầy). Lite phải có ≥2 động từ + 1 bị động | Oa chỉ có Quăng Lưỡi: không có né, đối kháng 1 nút = demo | Tối thiểu C1–C2 với 2 skill. Fallback đúng là **hoãn cả loài**, không giảm skill |
| WORLD-02 "Cụ Ngao" | Minor | "Ngao" trong tiếng Việt là con **nghêu/ngao** (động vật hai mảnh vỏ), không phải rùa; art là rùa | Người chơi thấy rùa, đọc "Cụ Ngao" hình dung nghêu | **Lão Quy** (SURV/PX) hoặc "Cụ Rùa". WORLD quyết tên, quy tắc: không trùng loài chơi được |
| WORLD-05 Thanh Oa + Cụ Ngao + Ao Gương | Minor | Oa (chơi được) và NPC cùng chủ đề nước: nếu Thủy NPC là rùa, Thủy chơi được là ếch, sprite không tái dùng được (SURV-05 dựa vào Quy chơi được để tint) | NPC cần sprite riêng: +0,1 | Chấp nhận +0,1; 1 sprite tĩnh |
| WORLD scope delta | Major | Net +0,7 bị đếm trùng: Huyết Mạch tộc lite −0,5 (lite C2 vốn không có HM, nên không tiết kiệm so v1.0), palette "dùng lại" −0,3 (không phải tiết kiệm), Kiến lite −0,5 (Khế ước Kiến giữ ở ma trận nên không cắt được) | Đệm báo 7% nhưng thực ≈4% | Dùng bảng "Ngân sách thực" |
| WORLD-06 Thủy⊣Thú | Minor | "Nước sâu chặn Lang" chỉ đúng nếu có nước sâu: tiêu 0,3–0,5 t-n | — | Nước sâu chỉ ở Đầm Mục, 3 bến cạn (WORLD-03) |
### Câu hỏi cho WORLD
Thần Thức +30% (Kê) và +50% (PX) là số nào? Đạo "Mắt" của Vũ có chạm lore của Quạ Già (Sứ giả) không?

---

## Phân xử các điểm lệch (a)–(f)
**(a) Đại diện.** Mộc=Linh Mộc, Thú=**Lang**, Trùng=**Linh Nghĩ** (4/4 đồng ý), Thủy=**Oa** (WORLD+PX; SURV: Quy, PROG: Lý), Vũ=**Gà rừng** (SURV Trĩ, WORLD Kê, PX Kê/Trĩ; PROG: Tước). Tên: WORLD chốt, tôi dùng "Linh Kê".
**(b) Vòng sinh/khắc.** Tôi chọn **Mộc→Thú→Trùng→Vũ→Thủy→Mộc**, khắc Mộc⊣Trùng⊣Thủy⊣Thú⊣Vũ⊣Mộc (WORLD/PX). Hành: Mộc, Thú=Hỏa, Trùng=Thổ, Vũ=Kim, Thủy. Ba bản đều khớp Ngũ Hành chặt; khác nhau ở ánh xạ. Chỉ bản này có 4/5 mắt xích sinh trực quan (SURV 3/5 yếu; PROG 3/5 yếu). PROG kiểm tra: không mâu thuẫn Hành Huyết Mạch Lang hiện có.
**(c) NPC Trung Ấm.** Rùa, tên Lão Quy. Sprite tĩnh, nước phản chiếu = shader. Cost 0,3 gồm pool câu mới.
**(d) FTUE.** Giữ Linh Thử (xem WORLD-05 ở trên). Bánh xe 15:30: 5 thẻ cùng lúc.
**(e) C2 vs C3.** **C3-lite** (PX-01b): 2 Bản Năng + A1 data-only, Tiểu Kiếp dùng template chung, khóa Phi Thăng Kiếp I, không Ngộ Đạo draft, không HM. Thời gian: C2 ≈ Phiên 2–3, C3 ≈ Phiên 6 (≈1,5h) so với C4 Phiên 11; lite là điểm vào, không phải điểm cuối. Cap C2 bỏ qua cảm giác Kiếp: không chấp nhận.
**(f) Ngân sách.** Xem dưới.

## Đánh giá 15 phút đầu theo tộc
| Tộc | "Wow" đầu tiên (phút) | Thứ đã vui | Rủi ro 15' |
|---|---|---|---|
| Mộc | 1–2 đặt Neo, 5 Quả đầu | Có sẵn VS | thấp |
| Thú (Lang) | 1 đuổi, 3–5 hạ mồi | burst | đối thủ lite quá yếu: Lang thống trị |
| Trùng (Nghĩ) | **<1 Lính tỏa theo**, 3 tha hạt/xác về tổ, 8 Mở Xác | hình ảnh bầy | "tổ" là một công trình mới (+0,15 chưa ai tính); hitbox gộp |
| Thủy (Oa) | 1 Quăng Lưỡi kéo mồi, 3 chui nước = trốn | kéo/chui | Bìa chỉ có 1 suối: **spawn Thủy phải ở nước** (+0,1); nếu không phút 3 chưa thấy nước |
| Vũ (Kê) | 1 Lướt, 3 thấy Linh Hạch xa | cơ động | solo thiếu động từ thưởng; mất "Mắt" nếu không có party |
**Loãng?** Không loãng vì số tộc mà vì **độ sâu lite + 1 loài/tộc**: "tộc" và "loài" trùng nhau, người chơi không cảm "tộc" nào. Lite là điểm tham quan C3, rồi Luân Hồi sang Mộc/Lang (C4). Đo: HN2 (nhớ ≥4/5 tộc), HN3 (mỗi tộc 8–32% lượt chọn), HN4 (chạm cổng không thoát).

## Matchmaking / phân bố loài ở CCU 24–40
- Giả sử Mộc 45%, bốn tộc còn lại ~14% mỗi tộc. CCU 24: Mộc ~11, mỗi tộc kia ~3. CCU 8 (ngưỡng gộp phòng): mỗi tộc lite kỳ vọng ~1,1; **xác suất một tộc vắng = 0,86⁸ ≈ 30%**.
- Hệ quả: ma trận 10 cặp PvP gần như **không bao giờ xảy ra** giữa người với người trong 15'. Ma trận chỉ cảm nhận được nếu (1) hệ số tộc-khắc áp **cả lên AI cùng tộc** (Lang AI, Diều/Quạ, bầy sâu, cá/ếch AI; chi phí 0 vì data), và (2) cộng sinh tập trung vào **party 2–4 người** (nơi người chơi chủ động chọn tộc bổ trợ). Không có "matchmaking theo tộc": quá mức với 40 CCU.
- Rừng vắng không được để vai nào phụ thuộc tộc khác có mặt (Vũ "ping party" ở solo, Thủy "hồi đồng đội"). Mỗi tộc phải có 1 động từ solo (Oa kéo, Kê Linh Hạch, Nghĩ Mở Xác).
- Đề xuất nhẹ: bánh xe hiện số người mỗi tộc trong phòng. Nếu một tộc <5% ở CCU ≥24 trong 3 ngày, bật +5% Đạo Quả cho tộc đó (PROG chọn số). Telemetry bắt buộc: share tộc theo phòng/giờ, thời gian sống theo tộc, số cặp (khắc) gặp nhau/phiên.

## Ngân sách thực (bottom-up của PX, so với các bản)
| Hạng mục | t-n | Ghi chú |
|---|---|---|
| 3 loài lite C1–C2 (Nghĩ 0,9 · Oa 0,8 · Kê 0,7) + UI/tên/sim chung 0,55 | **+2,95** | R1 PX 1,65: thiếu; SURV 3,0 (C1–C3 nhưng giả định reuse), PROG 4,5 (C1–C3, sát hơn), WORLD 2,25 |
| Nước (tile+autotile 0,2, layer/tốc 0,1, nước sâu+spawn 0,1, cá/ếch decor 0,1, Ướt+âm 0,1, đặt lại map 0,1) | +0,7 | R1 PX 0,35 thấp |
| Ma trận: data 0,3 + icon 0,1 + 4 cộng sinh thật 0,4 | +0,8 | SURV 0,5 gồm cả nước; WORLD 0,5; PX 0,4 |
| Trung Ấm nước, Lão Quy, pool câu, rename Khuẩn | +0,3 | |
| **Tổng thêm** | **+4,75** | |
| Cắt: Thử → FTUE-only (−0,8) · Hóa Hình Mộng (−0,25) · HM 6→4 (−0,3) · Linh Thức → do thám (−0,4) · swarm Kiến dùng chung (−0,3) · palette mùa 4→2 (−0,2) · shop 6→4 (−0,1) · Linh Tức vi mô (−0,1) · pool 60→40 (−0,1) | **−2,55** | Không tính hai lần |
| **Net C1–C2** | **≈ +2,2** | đệm 4,25 → **2,05 (4,3%)** |
| C3-lite (A1 data-only + Tiểu Kiếp template ×3) | +0,45 | net **+2,65**, đệm **1,6 (3,3%)** |
So sánh: SURV +2,6 / PROG +3,5 / WORLD +0,7 / PX R1 +1,45. WORLD thực ≈+2,0 sau khi bỏ đếm trùng. **Dải tin cậy +1,5 đến +3,2.**
**Cờ: SCOPE RISK ĐỎ.** Đệm 3,3% < 8,5% v1.0 < 14% an toàn. Không cắt được thêm mà vẫn giữ "5 tộc" ngoài các biện pháp dưới.

## Fallback có cổng
1. **Luật lite (Definition of Lite):** ≥2 động từ chủ động + 1 bị động, vai nhận ra trong 30s; chỉ 3 primitive mới (dash, pull, follower-bầy); 0 need mới, 0 AI archetype mới.
2. **Cổng tuần 16 (VS = Mộc + Thử FTUE + Lang AI + 2 client):** thêm **Oa prototype** (pull + nước) chạy 1 client. Nếu VS vượt >1 t-n: hoãn Kê (−0,7) sang đợt 2.
3. **Cổng tuần 30:** trễ >2 t-n: Oa sang đợt 2 (−1,5 gồm nước sâu), ra mắt 3 tộc chơi được + 2 tộc "Sắp Giáng Lâm" (AI/NPC). Không giảm skill.
4. Hạ C3-lite → C2 (−0,45) là chốt cuối trước khi hoãn loài.
5. Không bao giờ cắt: Linh Mộc, Lang, luân hồi, độ kiếp C3, Rừng chung PvP, FTUE, **≥3 tộc chơi được ngày 1** (ưu tiên 4).

## Xung đột liên domain
| Xung đột | ID | Lập trường PX | Gợi ý |
|---|---|---|---|
| Thú: Lang vs Thử | PROG-01 / SURV-01, WORLD-05 | Lang | Thử → Tiền Thân FTUE + AI |
| Thủy: Oa / Quy / Lý | WORLD-05, SURV-01, PROG-01 | Oa | Quy = NPC, Lý [Post] |
| Vòng sinh | SURV-03, PROG-03, WORLD-06 | WORLD/PX | Mộc→Thú→Trùng→Vũ→Thủy |
| Hệ số khắc ×1,5 / 1,25 / 1,15 | SURV-03, PROG-03, WORLD-06 | ≤1,15, max không cộng | PROG xác nhận stress-test |
| FTUE Kiến vs Chuột | WORLD-05 / SURV-02, PROG | Chuột | VS đo H11 |
| C2 vs C3 | PX-01 / PROG-05, SURV | C3-lite data-only | Cổng 30 hạ về C2 |
| Căn Thương cho Nghĩ | SURV-04 / PX-02 | cần phối hợp | Chỉ chạy khi Thú/Vũ hạ phòng ngự 30s |

## Top 3 điều team phải chốt
1. **Ba đại diện còn tranh chấp (Thú, Thủy, Vũ)** và bản Hành/vòng sinh duy nhất. Đề xuất: Lang, Oa, Linh Kê; Mộc→Thú→Trùng→Vũ→Thủy.
2. **Mức lite và số ngân sách chung:** C3-lite data-only, net +2,65, đệm 3,3%, với cổng 16/30 và luật 3 primitive. PROG/SURV/WORLD nộp lại số theo bảng bottom-up ở R3.
3. **Ma trận chỉ bật 10 hệ số + 4 cộng sinh, áp cả lên AI, ưu tiên party.** Mọi cộng sinh thứ 5 trở đi là [1.0].

---

# Hệ quả của Bổ sung 2 và 3 với domain của PX
Quyết định D–G là chốt; dưới đây chỉ là cờ rủi ro, số liệu, giả thuyết và phương án giữ scope. Số ngân sách ở trên là baseline "5 tộc × 1 nhân vật" (net +2,65 với C3-lite).

## D. 3–5 lựa chọn mỗi mốc, kế thừa, hiệu quả hết đời
- **Quy tắc đề xuất cho PROG:** chọn **mỗi cảnh** (không mỗi tầng): Mộc/Lang 4 mốc, lite 2–3 mốc. Mỗi tầng = 12 quyết định × 3–5 thẻ = 36–60 hiệu ứng/loài, vượt khả năng làm và test. Hiệu ứng là **augment dạng data** của primitive sẵn có (đổi số, thêm điều kiện), không VFX mới.
- **Choice paralysis trên mobile:** hiển thị **3 thẻ**, vuốt ngang tới 5; mỗi thẻ ≤12 chữ + 1 icon; nhãn "Gợi ý" cho người mới; không timer; Cho phép xem lại ở menu. Mốc đột phá đang là khoảnh khắc ăn mừng, không được thành màn đọc.
- **Hệ quả cho F:** lite phải có **≥3 hiệu ứng** trong đời mới có "random 3". Lite C2 chỉ có 2 mốc → 2 hiệu ứng. Quy tắc: hiện min(3, đang có); hoặc lite có mốc chọn ngay đầu C1.
- **Chi phí:** UI thẻ + pipeline data 0,3 · nội dung lite 3 loài × 3 mốc × 3 thẻ ≈ 27 hiệu ứng ×~0,015 = 0,4 · tái cấu trúc Mộc/Lang (thay 18 skill + 6 Huyết Mạch) 0,3 = **+1,0**.
- **Giả thuyết:** HD1 trung vị thời gian chọn ≤20s trên mobile, ≥70% chọn không mở chi tiết; HD2 ≥60% tester nói hai build cùng loài "khác nhau"; HD3 không hiệu ứng nào được chọn >50% (dominant), không <5% (chết).

## E. Chết giữa chừng = làm lại hoàn toàn
**Cờ: rủi ro retention lớn nhất của cả session.** v1.0 thiết kế P3 "Cái chết là hạt giống" (≥60% quay lại 72h sau chết PvP ở C≥3) dựa vào Hậu Duệ/Túc Tuệ. Giờ chết ở C4 Phiên 9–11 = mất ~2,5h; PvP luôn bật; P1 (cozy, sợ gank) thấy mức phạt gấp nhiều lần mức đã được kiểm.
- **Thời lượng một đời:** FTUE 16' → C3 ≈ Phiên 6 (~1,5h) → C4 ≈ Phiên 11 (~2,8h Mid). Chết ở phút 14 FTUE = mất 14'. Chết ở C3 Hậu = mất ~1,5h.
- **Hệ quả đo được:** P1 sẽ dồn vào Mộc (cây offline bất tử, tức "bến an toàn"); bánh xe lệch hơn HN7 (Mộc ≥45%) và lite không ai chọn. Ngược lại hardcore/P2 chơi bình thường.
- **Đề xuất giảm thiểu (không đổi quyết định):**
  1. Khung bảo vệ theo **tiến độ, không theo giờ**: Ấu Linh bảo hộ PvP đến hết C2; từ C3 có "Kiếp Báo" 60s + Tâm Rễ/Hang có hiệu lực, cho phép tuyệt cảnh.
  2. **Độ kiếp thất bại ≠ chết**: lùi 1 tầng (mất đột phá hiện tại, giữ hiệu ứng đã chọn). Nếu tính là chết, tỉ lệ bỏ cuộc tại C3 cao.
  3. Hồi sinh mới **<30s** (Trung Ấm 45s skip sau lần 3), Lão Quy cho 1 dòng thoại; hiển thị "Ngươi để lại: Mộ Linh, Biên Niên, xác nuôi rừng (Sổ Sinh Năng)".
  4. Thứ giữ lại (không phải sức mạnh): skin, Biên Niên, Mộ Linh, sách sưu tầm, kiến thức bản đồ, mở khóa loài.
- **Telemetry:** tỉ lệ rời game ≤60s sau chết theo cảnh; số đời bắt đầu/ngày; nguyên nhân chết (PvP/AI/kiếp) × cảnh; tỉ lệ chết do người chơi cùng phòng ở C≥3.
- **Giả thuyết:** HE1 chết ở C≥3 do PvP: ≥45% quay lại ≤72h (hạ từ 60%; nếu <35% thì bật Kiếp Báo mặc định); HE2 chết trước C3: ≥65% bắt đầu đời mới ≤2'; HE3 P1 (nhóm cozy) không bỏ game >40% ở Phiên 1–6; HE4 Mộc không vượt 55% lượt chọn.
- **Chi phí:** bỏ Hậu Duệ + Túc Tuệ + Hồi Ức + Đạo Quả Bàn sức mạnh **−0,8**; thêm Kiếp Báo, UI "ngươi để lại" +0,2.

## F. Hoàn thành → random 3 hiệu ứng → mang 1 sang đời sau
- **"Giai đoạn cuối" MVP:** Mộc/Lang = C4 Hậu qua Phi Thăng Kiếp I; lite = cổng C3 (PROG-05) hoặc C2 Hậu nếu cap C2. Nhân vật cũ → Mộ Linh + Biên Niên (vĩnh viễn, đã có), không cần NPC mới.
- **Rủi ro kinh tế (source/sink):** faucet = mỗi lần hoàn thành 1 di sản; **sink = 0**. Nếu cộng dồn qua các đời: đời 5 có 5 hiệu ứng, người cũ vs người mới trong PvP luôn bật mất cân bằng (vượt trần ×1,32?). Đề xuất: **1 slot**, hoàn thành mới thay thế; hoặc ≤2 slot; hiệu ứng nằm trong trần ×1,32 theo quy tắc "lấy giá trị lớn hơn". Không bị mất khi đời sau chết (di sản không bị tiêu thụ; mất 2 lần là phạt kép), chỉ không thay mới.
- **Lite = đường tắt farm di sản:** lite hoàn thành trong ~1,5h (C3) hay 45' (C2) trong khi Mộc/Lang ~2,8h. Người chơi chọn lite để lấy di sản nhanh rồi sang Lang. Giảm: hiệu ứng từ lite được gắn tier thấp (×0,5), hoặc di sản chỉ mở **sau khi hoàn thành 1 loài full**.
- **Qua tộc:** di sản gắn **loại** (Thân, Tốc, Hồi, Sát...) và "dịch" theo chất tộc mới (tag dịch 0,2). Nếu không có tag, chỉ số gốc ×0,5 qua tộc khác. Cần PROG/WORLD xác nhận.
- **Chi phí:** random 3 UI + slot persistence + dịch tag **+0,5**.
- **Giả thuyết:** HF1 ≥70% người chơi hoàn thành chọn trong ≤15s và nói muốn chơi đời tiếp; HF2 tỉ lệ người có di sản thắng PvP cùng cảnh ≤55% (so không di sản); HF3 ≥50% người hoàn thành lite đổi sang tộc khác trong 1 đời.

## Kinh tế Đạo Quả sau E
Đạo Quả sức mạnh (Bàn 3 node) bị loại, nên **mất mục tiêu giữa chu kỳ D7–D30**. Nếu Đạo Quả chuyển thành tiền mở khóa ngang: faucet = cảnh đạt theo đời, sink = mở loài (4 tộc × ~1 lần), skin, danh hiệu, Mộ Linh. Danh mục hữu hạn ⇒ **bão hòa trong ~8–10h**, không có sink lặp lại. Đề xuất: sink lặp (nâng Mộ Linh, khắc Biên Niên, Đạo hiệu), cap Đạo Quả/đời, và coi **5 tộc mỗi tộc một "chất" (G) + di sản (F)** là hook D7/D30 thay cho progression bền. Cảnh báo KPI: D30 ≥3% (v1.0) có thể không giữ; đề xuất đo cohort sớm ở alpha.
Giả thuyết HK1: người chơi chơi ≥3 tộc khác nhau trước khi ngưng ≥50% ở D7; HK2 Đạo Quả dư >40% người chơi sau 10h (nghĩa là thiếu sink).

## G. "Chất" riêng mỗi tộc
- **Khung chung (không đổi, chiếm >85% code/UI):** HUD 4+1, No/Thể Lực, cảnh giới, thẻ lựa chọn, Rừng chung.
- **Phần riêng và chi phí:**
| Tộc | Cơ chế riêng (1–2) | Nhịp | Chi phí đã tính trong baseline | Thêm vì G |
|---|---|---|---|---|
| Mộc | Rễ/Neo, Vệt Nắng (có sẵn) | chậm, quyết định lớn | 0 | 0 |
| Thú (Lang) | Săn burst, Hang (có sẵn) | nhanh, có đỉnh | 0 | 0 |
| Trùng (Nghĩ) | Bầy follower + **Tha** (carry) | trung bình, công việc | 0,4 | +0,15 (carry) |
| Thủy (Oa) | Quăng Lưỡi (pull) + **ẩn/hồi trong nước** | chờ rình | 0,3 | +0,1 |
| Vũ (Kê) | Lướt + **Ping/Thần Thức** | ngắn, cơ động | 0,2 | +0,15 (ping netcode) |
| Chung | Tag di sản dịch qua tộc 0,2 · mini-hint "động từ tộc" 60s mỗi tộc ×5 0,25 | | | **+0,45** |
Tổng G thêm ≈ **+0,85**. Luật primitive nâng từ 3 lên 4 (dash, pull, follower, carry). Nguyên tắc "teach one thing": hint động từ tộc xuất hiện **khi luân hồi lần đầu** vào tộc đó, không thêm vào FTUE.
- **Giả thuyết:** HG1 ≥65% tester mô tả được "tộc X chơi khác chỗ nào" trong 1 câu sau 10'; HG2 ≥50% đổi tộc ít nhất một lần trong 5 đời đầu.

## Ngân sách sau Bổ sung 2–3
| Config | Net | Đệm | Nhận xét |
|---|---|---|---|
| Baseline (C3-lite) | +2,65 | 1,60 (3,3%) | Bảng trên |
| **A: đầy đủ D+E+F+G** (D +1,0, E −0,6, F +0,5, G +0,85 = +1,75) | **≈ +4,4** | **≈ −0,15 (âm)** | **Không khả thi** |
| **B: cấu hình an toàn** | **≈ +1,6** | **≈ 2,65 (5,3%)** | xem dưới |
**Cấu hình B:** lite **cap C2** (−0,45; tôi rút lại C3-lite ở R2 nếu người dùng giữ D+F) · G chỉ **1 cơ chế riêng/tộc**, bỏ cơ chế phụ (−0,4) · lite 2 mốc chọn, F hiện min(3, đang có) (−0,15) · di sản qua tộc dùng ×0,5 chỉ số gốc, bỏ tag dịch (−0,2) · và **cắt trước** Linh Quỹ động → mật độ tĩnh (−0,75, cắt trong v1.0 là ở cổng 30; đề nghị cắt từ đầu) · Bế Quan/catch-up rút gọn (−0,5). Đệm 5,3% vẫn dưới 8,5%: **SCOPE RISK ĐỎ**.
**Thứ tự hoãn loài nếu cổng trượt:** Kê → đợt 2 (−0,7) · Oa → đợt 2 (−1,5) · F cross-tộc [1.0].
**Cờ mới:** D+E+F+G chạm đúng cả 4 hệ thống cốt lõi (progression, death, meta, species identity) trong cùng 1 MVP của 1 người. Mô-đun hóa: D và E có thể ra trước F và G mà game vẫn đóng; ưu tiên **E trước** (đơn giản hơn Hậu Duệ), D, rồi F, rồi G phần phụ.
