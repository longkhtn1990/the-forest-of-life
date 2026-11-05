# R2 Critique — PX

> Vai trò: red team và domain owner của FTUE, kinh tế, retention, scope/MVP, playtest.
> Đơn vị chi phí: S ≈ 1 tuần, M ≈ 2.5 tuần, L ≈ 5 tuần, XL ≈ 10 tuần-người (đã tính AI hỗ trợ). "Mid" = người chơi 5 phiên × 40 phút/tuần ≈ 64 CT/phiên (theo PROG-04).
> Tự sửa trước: (1) Mô hình offline "60% tu vi thụ động" trong PX-04 của tôi thua mô hình rested của PROG-04, nên tôi bỏ nó. (2) Ad "tăng tốc bế quan" ở Rừng chung trong PX-12 là tăng sức mạnh, nên chuyển sang ❌. (3) Cơ chế "+50% Đạo Tâm cho nạn nhân" trong PX-05 farm được bằng tài khoản phụ, nên thêm trần 1 lần/ngày, chỉ tính khi chênh lệch cảnh giới *thật* ≥2. (4) Ước lượng 40–48 tuần của tôi ở R1 quá lạc quan (chi tiết ở mục Scope).

---

## Về SURV

### Giữ lại (Keep)
- **SURV-01 (HUD 2+2):** một bố cục cho mọi giới. Đây là quyết định UI tốt nhất trong cả 4 proposal: luân hồi sang loài khác không phải học lại HUD.
- **SURV-03 (cây có 3 lớp thân):** giải mâu thuẫn M1 của tôi tốt hơn "Đạo Căn" tôi đề xuất. Tôi bỏ Đạo Căn và nhận Tâm Rễ.
- **SURV-07 (6 động từ + Plant Pressure Map + session mẫu 30'):** đây là bằng chứng đầu tiên rằng cây có thể có khoảng 1 quyết định/30 giây.
- **SURV-10 (kinh tế gặm cỏ 40%, quả mời):** bất đối xứng có chủ đích, cây bị chậm lại chứ không chết. Đúng cái P3 cần.
- **SURV-15 (Mộc Mộ), SURV-18 (item sinks):** có sink tự nhiên, không có kho vô hạn. Tôi đồng ý.

### Mượn (Steal)
- **SURV-12 Hồn Thoát 30s:** thay mức 60s của tôi. Trên mobile, cuộc gọi đến hoặc OS kill app sẽ gây rớt mạng ngoài ý muốn, 60s là quá phạt.
- **SURV-11 Thoát Sinh + Ấu Thể Ẩn Khí:** đưa vào gói Thiên Đạo hợp nhất (xem bảng xung đột). Cả hai chi phí S và thưởng cho con mồi.
- **SURV-13 Director (Áp Lực):** dùng làm pacing cho FTUE (script đợt ăn lá ở phút 4–6) và để lấp rừng khi server vắng.

### Phản biện (Challenge)
| ID | Mức độ | Vấn đề | Tình huống người chơi | Đề xuất thay thế / cách kiểm chứng |
|---|---|---|---|---|
| SURV-07 + PROG-03 | **Major** | Vệt Nắng (AFK mất 40% thu nhập) cộng với Linh Thức Tán Loạn của PROG (không chạm trong 3' thì CT ×0.2) biến cây thành **game chạm liên tục 40 phút**. Kiểu này xung đột với P3 (cozy) và chế độ một tay. | P1 chơi cây trên xe buýt bằng một tay. Sau 15', ngón cái mỏi vì phải chạm 3–6 vệt/phút, đồng thời kéo rễ và bấm phòng thủ. | Vệt Nắng là **cửa sổ bonus** (mỗi 45–60s có 1 vệt, kéo dài 15s, ×3), không phải nguồn chính. AFK chỉ mất ≤20%. Ngưỡng tán loạn đổi thành "không có *quyết định* trong 5'". **Đo:** số lần chạm/phút cần để đạt 90% thu nhập ≤6. H3 (≥50% thử cây chơi ≥10') |
| SURV-03/07 | **Major** | Cây có quá nhiều thứ phải đọc: 3 lớp HP + Thủy + Quang Tinh + Dưỡng Chất + Linh Khí + Ánh Sáng% + mật độ L0–L5, cộng 6 động từ và 4 skill phòng thủ. Đếm ra **13 chỉ báo và khoảng 13 nút** (bảng UI bên dưới) | Ở phút 16 FTUE, người chơi mới đầu thai thành cây và nhận cùng lúc 7 thanh. Họ thoát ra trước khi thấy rễ mọc | **Unlock theo bậc:** phút 16–20 chỉ có Vệt Nắng, rễ, 1 gai. Hạt/neo mở ở C1 Hậu, kiến ở C2, Linh Thức ở C2. Gộp 3 lớp HP thành **1 widget vòng 3 lớp**. Dưỡng Chất vào panel phụ. Ánh Sáng% hiện bằng hình ảnh trên tán, không làm thanh |
| SURV-15 vs PROG-10 | **Blocker** (chưa thống nhất) | "Đầu thai Hậu Duệ" của SURV chỉ mất 1 tiểu cảnh, còn luân hồi của PROG mất toàn bộ cảnh giới. Đây là hai mô hình cái chết khác nhau. Nếu Hậu Duệ rẻ, gần như không ai đổi loài, và USP luân hồi bị rỗng | Sói C4 chết thì 95% sẽ chọn Hậu Duệ (mất ~150 CT) thay vì luân hồi (mất 553 CT). Bánh xe luân hồi trở thành màn hình bị bỏ qua | Dùng **mô hình lai** ở bảng xung đột: Hậu Duệ có trần chi phí, 1 lần/24h, và neo có thể bị phá. **Đo:** ≥30% số lần chết chọn đổi loài |
| SURV-17 + SURV-12 | **Major** | Đại Hạn kéo dài 6h thực và Thủy ×2.5. Proposal chưa nói rõ cây đang offline có mất Thủy không. Nếu có, người chơi 15 phút/ngày sẽ quay lại thấy cây đã chết | P1 ngủ 8 tiếng đúng lúc Đại Hạn. Sáng ra Tâm Rễ héo, mất 2 tuần tiến độ vì một sự kiện mà họ không thể tham gia | Ghi thành luật cứng: **Nhập Định offline miễn mọi decay needs và mọi sự kiện môi trường**. Sự kiện chỉ ảnh hưởng người đang online, thời lượng ≥2h để người chơi phiên ngắn bắt kịp |
| SURV-08/11 | Minor | Ba cơ chế cùng đẩy người mạnh ra khỏi vùng ngoài: Linh Khí Thất Thoát (SURV), CT ×0.5^chênh (PROG), −2% HP/phút (PX). Thừa | Người chơi không hiểu vì sao mình bị trừ máu, trừ linh khí và tu vi chậm cùng một lúc | **Chỉ giữ CT ×0.5^chênh của PROG + Áp Chế chỉ số.** Bỏ thất thoát của SURV và −HP của tôi |
| SURV-13/14 | Minor (scope) | 6 archetype AI, 5 loại thời tiết, lũ | — | MVP: 4 archetype (ăn cỏ đàn, kẻ săn, bầy côn trùng, ăn xác) và 2 thời tiết (mưa, giông/sét, dùng lại cho Độ Kiếp). Ký sinh, boss, sương mù, lũ để bản 1.0 |

### Câu hỏi cho SURV
1. Ở R1, thú ăn cỏ ăn tự động khi giữ nút, hay mỗi cú cắn là 1 lần chạm? (Nếu chạm: khoảng 10 lần/6 phút. Chấp nhận được, nhưng cần xác nhận.)
2. Có đồng ý mùa Đông **không** làm cây ngừng tu luyện không (xem xung đột với WORLD-14h)? Một mùa = 2 ngày thực, tức 25% năm-rừng cây không có CT.

---

## Về PROG

### Giữ lại (Keep)
- **PROG-01 (7 cảnh giới × 3 tầng) + PROG-02 (tên là lớp vỏ của n):** chi phí nội dung thấp nhất, dễ đọc trên mobile.
- **PROG-03 (Chu Thiên + Monte Carlo):** với studio 1 người, đây là công cụ quan trọng nhất của cả team. Phương sai là bản sắc loài, nhận xét rất hay.
- **PROG-04 (Tĩnh Tu rested):** thay mô hình offline của tôi. Không biến cây thành idle game, mà vẫn thưởng việc quay lại.
- **PROG-11 (Tốc không tăng theo cảnh giới, Thần Thức +5%):** đòn bẩy chống bắt nạt rẻ nhất và mạnh nhất. Đây là thứ phải chốt.
- **PROG-10 (Đạo Tâm Bàn không có chỉ số chiến đấu, trần +10% CT):** kinh tế meta đúng đạo đức.

### Mượn (Steal)
- **CT làm đơn vị kế toán** cho sơ đồ kinh tế của tôi. Mọi source/sink/ad được quy về CT/tuần.
- **Rested pool** gộp với "Linh khí dồi dào ×1.5" của tôi (PX-10) thành **một** bonus hằng ngày duy nhất. Hai cơ chế song song là thừa.
- **Áp Chế (level-sync)** làm xương sống của gói chống bắt nạt.

### Phản biện (Challenge)
| ID | Mức độ | Vấn đề | Tình huống người chơi | Đề xuất thay thế / cách kiểm chứng |
|---|---|---|---|---|
| PROG-10 | **Blocker** (với F2P mobile) | Chết ở C5 tốn **6.5 phiên Mid** (1.3 tuần), ở C6 tốn 9.8 phiên. Tôi cho rằng không game F2P mobile nào giữ được người chơi bị trừ 1 tuần tiến độ vì một pha gank 5 giây (TTK 4–6s theo PROG-11). Trong mùa 7–8 tuần, chết ở tuần 4 coi như mất mục tiêu của cả mùa | P1 đạt C5 sau 19 ngày. Đi xe buýt mất sóng, quay lại thì đã bị 2 sói C5 cắn chết. Phải mất 6–7 lần mở app để quay lại chỗ cũ. Họ gỡ game | **Trần chi phí cái chết:** ≤2 phiên Mid (~130 CT) khi còn neo, ≤1 tuần khi luân hồi đổi loài (dùng ×4 như PROG đã gợi ý). Xem mô hình lai ở bảng xung đột. **Đo:** người chết vì PvP ở C≥4 quay lại trong 72h ≥60%, tách theo cảnh giới |
| PROG-06 | **Major** (scope + nhận thức) | Có 7 lớp hệ thống: Bản Năng 6, Huyết Mạch 10, Đạo Đồ 24, Đạo Ngộ, Keystone, Túc Tuệ, Đạo Tâm Bàn 20, Pháp Bảo. MVP có 33 skill | — | MVP gồm Bản Năng + **2** Huyết Mạch/loài, tổng 3 × (2 + 2×3) = **24 skill**, 6 bộ sprite variant. Đạo Đồ chung và khóa kép Đạo Ngộ để bản 1.0. Đạo Tâm Bàn MVP chỉ 8 node |
| PROG-06 (loadout) | **Major** (UI) | 4 chủ động + 1 Thần Thông + đánh thường là 6 nút bên tay phải. Cộng thêm ăn, né, chạy là 9 | Sói trên điện thoại 6 inch: ngón cái che mất nút né đúng lúc cần thoát | **3 chủ động + 1 Thần Thông** trên **mọi** nền tảng (giữ công bằng PvP chéo nền tảng). Đánh thường kiêm ăn/tương tác theo ngữ cảnh. Chạy bằng đẩy joystick ra mép. Né bằng vuốt |
| PROG-04 vs PX-08 | **Major** (FTUE) | Tầng 1 xong ở phút 3, tầng 2 ở phút 9, C2 ở phút 21–25. FTUE của tôi cần đột phá "hùng tráng" ở phút 5–8 và lần luân hồi đầu tiên ở phút 14. Đường cong thật không chứa được cả hai | Người chơi web (CrazyGames/Poki) có khoảng 3–5 phút để quyết định ở lại. Phải đến phút 21 mới có khoảnh khắc lớn đầu tiên thì 50% đã thoát | **Kiếp FTUE (Linh Thử) dùng đường cong nén riêng** (×3, scripted, không tính vào sim). Tiểu Kiếp C1→C2 ở phút 7. Kiếp thứ hai (cây) mới dùng đường cong chuẩn, có Tiền Kiếp ×3. **Đo:** H1 ≥80% đạt đột phá ở phút 8 |
| PROG-04/10/PX-16 | **Major** (kinh tế) | Các hệ số nhân chồng lên nhau: Tiền Kiếp ×3 × rested ×2 × Bù Đắp 1.25 × loài thiếu 1.25 (PX-16) × Mộc Mộ 1.2 = **×11 CT** trong 30 phút | Cách lợi dụng: chết có chủ đích ở C2, đầu thai loài thiếu tại Mộc Mộ khi hồ rested đầy. Chết gần như miễn phí, phá đường cong PROG | **Cộng các bonus theo kiểu cộng (additive), trần tổng ×3.** PROG thêm case này vào sim |
| PROG-07/13 | Major | Đại Kiếp được báo cả server, 4 phút bị kẹt vòng với 50% sát thương. Thiên Kiếp thất bại thì **chết** sau 6.5 tuần đầu tư. Người chơi Mid sẽ không dám độ kiếp | Cả server kéo tới phá kiếp của P1. P1 thất bại 3 lần, rơi 1 tầng | Có 2 lựa chọn: **Ẩn Kiếp** (riêng tư, khó hơn 20%) và **Công Kiếp** (công khai, có Hộ Pháp, cho cosmetic Pháp Tướng, cũng là móc monetization tự nhiên). Thiên Kiếp thất bại = Kiếp Thương + rơi 2 tầng. Chỉ chết thật nếu HP về 0 do người chơi khác giết |
| PROG-08 | Minor (scope) | Nhân Hình cần rig humanoid chung, Pháp Bảo, chế tác, phe NPC. Riêng phần này là XL | — | MVP/1.0 chỉ có **Bản Thể Đạo** (scale sprite +30%, chi phí S). Nhân Hình để sau launch |
| PROG-04 (ads) | Minor (đạo đức) | Ad "+5 phút rested/ngày" ≈ +8% CT trong thế giới PvP vẫn là pay-to-win bằng thời gian xem quảng cáo | — | Rừng chung: ad = **0 CT**. Rested ad chỉ có ở solo/co-op riêng |

### Câu hỏi cho PROG
1. Sát Nghiệp tính **sau** Áp Chế. Vậy C6 bị nén về n=9 giết C2 Trung (n=5) chỉ chênh ~1.3 cảnh giới, **không sinh Nghiệp**. Có phải lỗ hổng không? Tôi đề xuất Nghiệp tính theo cảnh giới **thật**.
2. Sau khi mùa reset (Đại Kiếp), Tiền Kiếp ×3 có áp dụng tới đỉnh mùa trước không? Nếu có, mùa 2 cựu binh lấy lại C6 trong khoảng 2 tuần và khoảng cách với người mới còn lớn hơn mùa 1. Tôi đề xuất reset mùa chỉ cho ×1.5, trần tới C4.
3. Co-op 85% + 10%/người: party 4 người mỗi người nhận 115%. Bầy 4 sói sẽ thống trị Rừng Non. Có cần trần thấp hơn trong vùng Áp Chế không?

---

## Về WORLD

### Giữ lại (Keep)
- **WORLD-02 (4 sự thật) + WORLD-04 (3 cấp rừng = Hạ/Linh/Thần Giới):** người đọc tiên hiệp hiểu ngay. Giá trị marketing cao, chi phí authored thấp.
- **WORLD-05 (wayfinding không cần minimap):** rẻ, và **bắt buộc** cho màn hình nhỏ.
- **WORLD-11 Trung Ấm + Biên niên kiếp chia sẻ thành ảnh:** UA tự nhiên. Ảnh Biên niên là tài sản viral rẻ nhất của game.
- **WORLD-12 quy tắc đặt tên cho pipeline AI:** đúng tinh thần 1 người + AI.
- **WORLD-14d Quả Ước:** trùng với "quả mời" của SURV-10, có thể gộp ngay.
- **WORLD-01 P1 vs P3:** theme được bảo vệ bằng cơ chế. Đây đúng là thứ tôi dễ cắt nhầm, nên tôi giữ.

### Mượn (Steal)
- **"Reset server = Đại Kiếp" (E8):** tôi nhận hoàn toàn cho kỷ nguyên reset của mình. Wipe trở thành sự kiện câu chuyện.
- **Quạ Già báo trước:** thông báo world event trong thế giới game, thay cho push UI.
- **Tiền Kiếp Ấn kiếm được, không bán:** prestige kiếm được đứng song song với skin bán được. Luật render: Ấn là lớp overlay, **skin không được che Ấn**.

### Phản biện (Challenge)
| ID | Mức độ | Vấn đề | Tình huống người chơi | Đề xuất thay thế / cách kiểm chứng |
|---|---|---|---|---|
| WORLD-12/A3 | **Major** | 9 cảnh giới. Nếu giữ hệ số ×1.77/cảnh giới, khoảng cách C1–C9 là ×96, hoặc phải hạ hệ số xuống và bảng PvP của PROG-12 vỡ. Cần thêm 2 bộ kỹ năng, kiếp, vùng. Tổng 54 tên cần bản địa hóa | — | **7 cảnh giới, ánh xạ 3/2/2:** Rừng Non C1–3, Nguyên Sinh C4–5, Cổ Đại C6–7. Ba cột mốc phi thăng trùng đúng ba loại kiếp của PROG: Trung Kiếp C3→C4, Đại Kiếp C5→C6, Thiên Kiếp C6→C7. Logic "mỗi cấp rừng có một kiếp lớn" của WORLD được giữ nguyên |
| WORLD-08 | **Major** | Mùa server 7 tuần, nhưng Mid cần 6.5 tuần **nếu không chết**. Chết một lần ở C5 là thành 7.8 tuần. Người vào giữa mùa (tuần 4) không có mục tiêu | Người mới tới từ trailer ở tuần 5. Họ thấy server đã có thần, mình còn 2 tuần trước khi bị xóa | Mùa theo bậc, xem bảng xung đột (MVP 28 ngày; bản đầy đủ: Kiếp lớn 8 tuần + Rừng Non có phòng xoay vòng 28 ngày) |
| WORLD-11 Nghiệp Duyên | **Major** | Khóa loài sau "bị X ăn 3 lần". P2 tới game để làm sói nhưng phải chết 3 lần dưới nanh sói. MVP có 3 nguồn mở loài chồng nhau: FTUE (PX-08), Đạo Tâm Bàn (PROG-10), Nghiệp Duyên | P2 bị khóa ngoài sói suốt 2 phiên vì Rừng Non lúc đó không có sói người chơi nào. Họ thoát | MVP: cả 3 loài mở sau FTUE. Nghiệp Duyên dùng để mở **Huyết Mạch biến thể, Tiền Kiếp Ấn và loài thứ 5+**. **Đo:** % P2 thoát trước khi chơi loài săn mồi |
| WORLD-13 | **Major** | (1) **Trùng tên:** "Đạo Tâm" vừa là tiền tệ meta (PROG/SURV/PX) vừa là la bàn đạo đức. (2) Aura 4 màu luôn bật chồng lên vòng màu cảnh giới dưới chân (PX-11), nên người chơi không đọc được trong 1 giây. (3) Tâm Ma sinh từ con mồi phạt thú ăn thịt hai lần | Sói trên mobile thấy 2 vòng màu dưới chân con mồi, đọc nhầm "đỏ = cao hơn mình" thành "đỏ = Sát" | Đổi tên la bàn thành **"Đạo Hướng"**. Aura chỉ hiện khi soi bằng Thần Thức. Tâm Ma có trần độ khó bằng nhau cho mọi Đạo Hướng (PROG cân) |
| WORLD-14 | **Major** (scope) | 10 ý tưởng cây, trong đó lựa chọn MVP của WORLD có Mộc Độn và Trận Pháp. Mộc Độn vô nghĩa trên map 256² ở MVP. Trận Pháp cần nhận dạng hình học, nội dung khắc đá và UI đặt cây chính xác trên mobile (khoảng M+M) | — | MVP gộp 3 ý vào SURV: 14d = quả mời, 14i = neo Mầm Con, 14e = cảm ứng rễ + Nhật Ký Rễ (bản lite). Mộc Độn và Trận Pháp (2 trận) để bản 1.0. 14c, 14j để sau launch |
| WORLD-10 | Major (scope + FOMO) | 8 sự kiện chồng lên 7 sự kiện của SURV (trùng khoảng 5). Huyết Nguyệt chỉ kéo dài **8 phút**, một lần/tuần theo giờ cố định, nên phụ thuộc múi giờ. Tu Sĩ Nhập Sơn cần cả một phe AI mới và cờ Minh Ước (L) | Người chơi VN online lúc 21h, Huyết Nguyệt rơi vào 3h sáng. Họ bỏ lỡ tuần này | Hợp nhất danh sách sự kiện. Sự kiện tuần **kéo dài ≥2h thực, lặp lại mỗi đêm game** trong khoảng đó. MVP có 2 sự kiện (Linh Triều S, Huyết Nguyệt S), Đại Hỏa/Rừng Tro ở bản 1.0. Bỏ Minh Ước (cờ tắt PvP, trái brief) |
| WORLD-11 Trung Ấm | Minor | 30–60s mỗi lần chết. E7 lại lấy việc "rút ngắn Trung Ấm" làm phần thưởng, tức là thưởng bằng cách bớt khó chịu | — | Lần đầu 45s đầy đủ. Từ lần sau 8–12s và bỏ qua được. Đổi phần thưởng E7 thành "đầu thai tại Mộ Linh +Duyên" |
| WORLD-03 Khô Linh | Minor | Có thể bị dùng để grief: bầy sói cố tình rút cạn vùng quanh cây đối thủ | — | Khô Linh không áp dụng ở Bìa Rừng. Cần SURV chạy sim với 30 người/256² trước khi chốt ngưỡng |

### Câu hỏi cho WORLD
1. Có chấp nhận 7 cảnh giới với ánh xạ 3/2/2 không? Tên riêng có thể lấy 7 trong 9 dòng của WORLD-12.
2. Diễn thế giảm xuống **3 giai đoạn (trống / cỏ / rừng) + Tro** ở MVP được không? Mỗi giai đoạn × biome là một bộ tile art.

---

## Ước lượng SCOPE tổng (theo yêu cầu orchestrator)

| Nguồn | Số ý | Phần nặng nhất | Ước lượng nếu làm đủ |
|---|---|---|---|
| SURV | 19 | 3 hệ needs, lưới sinh thái, 6 AI + Director, 5 thời tiết + lửa/lũ, Hang 4 cấp, 7 sự kiện, Luyện Hóa | ~45 tuần |
| PROG | 15 | 6 loài × 3 Huyết Mạch (20 bộ sprite), 55 skill, Đạo Đồ 3 lớp, 5 loại kiếp + Tâm Ma, Hóa Hình 2 đạo + rig, Xuất Khiếu/Linh giới, Thần vị | ~70 tuần |
| WORLD | 17 | 3 map (256²/512²/1024²), 6+1 biome, 4 template bí cảnh, 12 NPC, 8 sự kiện, diễn thế, 10 ý tưởng cây, 9 Mảnh Mộng, bản địa hóa | ~90 tuần |
| PX | 16 | Server T2–T3, UI 2 chế độ điều khiển, 4 bản port, monetization, Linh Ảnh, accessibility | ~45 tuần |
| **Tổng** | **67** | trừ ~15% phần trùng, cộng ~25% tích hợp/QA/live-ops | **≈260 tuần-người ≈ 5 năm-người** |

So với G4 (MVP trong 26–52 tuần), toàn bộ đề xuất **gấp khoảng 5–10 lần**. Ước lượng R1 của tôi (40–48 tuần) tính "3 loài = L", nhưng chỉ riêng cây theo SURV-07 đã là L. Danh sách bên dưới cộng lại khoảng 52 tuần, cộng 20% đệm là ~62 tuần. Muốn đúng G4 thì phải chia giai đoạn:

| Nhãn | Nội dung | Chi phí |
|---|---|---|
| **MVP-A (tháng 0–11, web solo + co-op AI-PvP + Linh Ảnh)** | Core sim 256² (L), Colyseus ngay từ đầu (solo = room local, M) · Cây bản lite: Vệt Nắng, rễ, 2 phòng thủ, hạt/neo, quả, kiến, 3 lớp HP (L) · Lang + Thử (M+M) · Needs 2+2, 4 mùa, 2 thời tiết (M) · 4 AI + Director lite (M) · 7 cảnh giới, nội dung C1–C4, CT, rested, 2 Huyết Mạch/loài, 24 skill từ 12 template (L+) · Tiểu + Trung Kiếp (M) · Luân hồi lai + Đạo Tâm Bàn 8 node + Trung Ấm ngắn + Biên niên (M) · 1 map, 3 vòng, 3 biome, wayfinding (L−) · 2 sự kiện (S) · FTUE + UI + accessibility cơ bản (L) · Telemetry + lore 4k từ (S) | ~44 tuần + đệm |
| **MVP-B (tháng 12–15, soft launch)** | Rừng chung T2 24–40 người + gói Thiên Đạo + anti-cheat (L) · Shop skin, pass, rewarded ads (M) · C5 Bản Thể (S) · Android (M) | ~13 tuần |
| **1.0** | Khuẩn (L), Linh Thảo (M+), Đạo Đồ chung, Đạo Ngộ, Mộc Độn, Trận Pháp (2 trận), Linh Thức/Xuất Khiếu, Đông Tàng Mộng Du, Đại Hỏa + Rừng Tro + diễn thế 3 giai đoạn, 2 bí cảnh (Lôi Trì, Mộng Cảnh), Hang cấp 2–4, 6 Lão NPC, Steam | — |
| **Post-launch** | Nguyên Sinh (XL), Nhân Hình + Pháp Bảo (XL), Thần vị/Thần Vực/Thiên Kiếp (XL), Phong/Trùng (XL), Tu Sĩ Nhập Sơn, Ký Sinh Đoạt Xá, Truyền Mộng, Trùng Sào, iOS | — |
| **Won't (giai đoạn này)** | Rừng Cổ Đại 80–200 người/1024², chat tự do, Minh Ước, thời tiết sương mù/lũ, 9 cảnh giới | — |

**Tự kiểm tra điểm mù "cắt quá tay":** MVP-A vẫn giữ cây chơi được, luân hồi đổi loài, độ kiếp, chuỗi thức ăn 3 bậc và PvP (với AI/Linh Ảnh). Bốn thứ đó là khác biệt của game. Cái tôi chấp nhận đánh đổi: **PvP người thật đến muộn khoảng 3–4 tháng.** Nếu team cho rằng PvP người thật là bắt buộc ở bản đầu tiên, phải cắt thứ khác bằng khoảng 13 tuần. Gợi ý cắt: Huyết Mạch còn 1 nhánh + 1 nhánh mặc định (−4 tuần), FTUE bỏ Linh Thử và vào thẳng Lang (−2.5 tuần), map còn 2 vòng (−2.5 tuần).

## Kiểm tra độ phức tạp UI trên mobile

| | Theo proposal hiện tại | Ngân sách PX đề xuất |
|---|---|---|
| **Cây – chỉ báo** | Tán, Thân, Tâm Rễ, Linh Khí, Thủy, Quang Tinh, Dưỡng Chất, Ánh Sáng%, mật độ L, tu vi, CD Linh Thức, Nghiệp, la bàn Đạo Hướng = **13** | **4 + 1:** vòng 3 lớp (Tán/Thân/Tâm Rễ), Thủy, Quang Tinh, Linh Khí, cộng thanh tu vi. Nghiệp chỉ hiện khi >0 |
| **Cây – nút** | 4 phòng thủ, hạt, 3 cộng sinh, quả, Linh Thức, Bế Quan, Độ Kiếp, Thần Thông, Linh Hóa Địa = **~13** | **≤5** + kéo trên map: Phòng thủ (bánh xe 2), Hạt, Quả, Cộng sinh, Thần Thông. Bế Quan/Độ Kiếp nằm trong menu ngữ cảnh |
| **Thú – chỉ báo** | HP, Linh Khí, No, Thể Lực, tu vi, Nghiệp, la bàn, Ấn Huyết Mạch, trạng thái = **~9** | **4 + 1** (Thể Lực là vòng quanh joystick) |
| **Thú – nút** | Đánh thường, 4 skill, Thần Thông, chạy, né, ăn, Hang, Hóa Hình, Xuất Khiếu = **12** + joystick | **5** + joystick: đánh/ăn theo ngữ cảnh, 3 skill, Thần Thông. Né bằng vuốt, chạy bằng đẩy joystick ra mép |

Luật đề xuất cho GDD: **≤4 thanh cố định + 1 thanh tu vi, ≤5 nút hành động, nút ≥48dp, HUD ≤18% màn hình.** Mọi thứ khác dùng ngữ cảnh hoặc bánh xe. **Đo:** tỉ lệ bấm nhầm nút <5% trong playtest mobile.

---

## Xung đột liên domain phát hiện được

| Xung đột | Các ID liên quan | Lập trường của tôi | Gợi ý giải quyết |
|---|---|---|---|
| **Số cảnh giới** | PROG-01 (7), WORLD-12/A3 (9), SURV-A4 (R1–R9) | **7** | Ánh xạ 3/2/2 vào 3 cấp rừng (xem phản biện WORLD). MVP-A có nội dung C1–C4, MVP-B thêm C5 Bản Thể. Map MVP có vòng trong không trần Áp Chế để C4 vẫn có ý nghĩa (nếu toàn map nén về n=9 thì lên C4 vô nghĩa) |
| **Độ dài mùa / reset** | WORLD-08 (~7 tuần), PX-09 (14/28 ngày), PROG-04 (Mid 6.5 tuần, Casual 13–16) | Đổi 14 ngày của tôi thành **28 ngày cho MVP**. Bản đầy đủ: mùa theo bậc | **MVP (1 map, C1–C5):** 28 ngày. Mid đạt C5 ở ngày ~19, Casual đạt C4 ở ngày ~24 (có Bù Đắp). Ai cũng có một cột mốc trước Đại Kiếp, khớp với pass 28 ngày. **Bản đầy đủ:** Kiếp lớn **8 tuần** (Nguyên Sinh + Cổ Đại; 7 tuần + đệm cho 1 lần chết), còn Rừng Non chạy **phòng xoay vòng 28 ngày** để người mới vào lúc nào cũng có điểm xuất phát công bằng. Lore Đại Kiếp dùng cho cả hai |
| **Offline** | SURV-12, PROG-04, PX-04 | Hợp nhất 1 bộ luật | (1) Trong Hang/lãnh thổ: thoát ngay. Ngoài đó: Hồn Thoát 30s. (2) Thân bất tử, **miễn decay needs và sự kiện môi trường**. (3) Tu vi offline = 0, chỉ có rested 8h → ×2 CT trong 30' (gộp với PX-10). (4) Cây hồi Tán/Quang Tinh ở 25% tốc độ, trần 8h (vật liệu, không phải CT), để "cây đã lớn" vẫn là hook D1. (5) Phần mất được (Tán/lãnh thổ ngoài) có trần **20%/lần offline**. Ô rễ teo dần nếu offline >48h. (6) Báo mộng gộp với Nhật Ký Rễ |
| **Chống bắt nạt** | SURV-11, PROG-12, WORLD-16, PX-05 | **Gói "Thiên Đạo" 4 lớp, mỗi lớp 1 con số** | **L1 Hộ Thể:** sau FTUE, 60' trong Rừng chung hoặc đến C2. Sát thương từ người cao hơn ≥1 cảnh giới −70%, kẻ tấn công không nhận thưởng. Mất bảo vệ nếu người mới tấn công người chơi trước. Thêm Ấu Thể Ẩn Khí cho C1–C2. **L2 Áp Chế** (PROG) + CT ×0.5^chênh, bỏ các cơ chế thất thoát/−HP. **L3 Sát Nghiệp:** tính theo **cảnh giới thật**, chênh ≥2. Thưởng = 8 CT × 0.25^g. +1 Nghiệp: +10% sát thương kiếp. Từ 3 Nghiệp: Huyết Sát hiện trên map, bounty ×3. Từ 5 Nghiệp: sét Thiên Phạt (Could). Giảm 1 Nghiệp/2h chơi. **L4 Đền bù nạn nhân:** Thoát Sinh + Đạo Tâm +50% (trần 1/ngày). Cùng một cặp: 30'. **Đo:** H5 ≤10% số kill ở chênh ≥2 |
| **Chi phí cái chết** | PROG-10, SURV-15, PX-06 | **Trần ≤2 phiên khi còn neo, ≤1 tuần khi luân hồi** | **Trùng Tu (neo còn sống, 1 lần/24h):** giữ cảnh giới và Huyết Mạch, mất tối đa 130 CT, không nhận Đạo Tâm. **Luân Hồi (đổi loài, hoặc neo bị phá):** Đạo Tâm (công thức PROG), Tiền Kiếp ×4, Túc Tuệ. PvP vẫn có sức nặng nhờ chiến thuật "tận diệt" (phá neo trước). Nguyên Thần Bất Diệt giữ ở C6 |
| **Dòng năng lượng khi chết** | SURV-09 (40/20/40), PROG-10/12 (8 CT × m, xác 20%), WORLD-03 (40% về quỹ / 60% Mộng Hỏa), PX-06 (20–35% → Đạo Tâm) | **Một sổ cái duy nhất** | Cấu trúc theo SURV (kẻ ăn / Linh Hạch / đất). Lượng cho kẻ ăn tính bằng công thức CT của PROG. Đạo Tâm tính riêng theo công thức PROG. Bỏ tỉ lệ 60% của WORLD và 20–35% của tôi |
| **Tu vi trực tiếp hay luyện khi Bế Quan** | SURV-06 (linh khí → tu vi ×1.5 khi Bế Quan), PROG-03 (CT trực tiếp) | CT trực tiếp | Thanh tu vi đầy ngay (cảm giác .io cho FTUE). Linh Khí dư khi Bế Quan đổi được ra CT, **trần 15% CT của phiên**. Như vậy Bế Quan vẫn là điểm dừng đẹp mà không có hai pipeline song song |
| **Mùa Đông của cây** | SURV-12 Ngủ Đông (không tu luyện), WORLD-14h (xuất khiếu ×2) | Mùa Đông = mùa linh hồn | Ngủ Đông chỉ áp dụng khi offline. Khi online, cây kiếm CT bằng Linh Thức ×2 để giữ parity 1.0 CT/phút (PROG sim lại) |
| **Ads ở thế giới PvP** | PROG-04, SURV (không hồi giữa PvP), PX-12 | **0 CT từ ad ở Rừng chung** | Ad ở Rừng chung chỉ cho Hoa Lộ ×2 và Đạo Tâm +30% (chỉ mở khóa ngang). Rested/hồi sinh chỉ có ở solo/co-op riêng. Không thêm thời gian chờ để bán nút "bỏ qua" (thời gian chờ 60s trong PX-16 của tôi đổi thành chỉ có bonus cho loài thiếu, không phạt loài thừa) |
| **Mở khóa loài** | PX-08, PROG-10, WORLD-11 | Một nguồn | MVP: mở hết 3 loài sau FTUE. Nghiệp Duyên dùng cho biến thể/Ấn/loài 5+. Đạo Tâm Bàn chỉ mở khóa ngang |
| **Linh Triều** | SURV-17 (2h/tuần), WORLD-E1 (24'/2 mùa), PX-15 (15' × 2/ngày) | 1 định nghĩa | Đại Linh Triều 2h, mỗi 2 mùa (4 ngày). Bỏ bản 2 lần/ngày của tôi vì nó là hẹn giờ kiểu FOMO |

## Top 3 điều team phải chốt
1. **Khung cảnh giới và mùa:** 7 cảnh giới ánh xạ 3/2/2 vào 3 cấp rừng. MVP là 1 map 3 vòng, C1–C5, mùa 28 ngày. Bản đầy đủ: Kiếp lớn 8 tuần + Rừng Non xoay vòng 28 ngày. Nếu không chốt điều này, PROG không sim được, WORLD không dựng được map, tôi không định giá được pass.
2. **Trần chi phí cái chết và luật offline, một bộ duy nhất:** Trùng Tu ≤130 CT (≤2 phiên) / Luân Hồi ≤1 tuần. Offline miễn decay và miễn sự kiện. Hệ số nhân cộng dồn kiểu cộng, trần ×3. Đây là ranh giới giữa "khắc nghiệt vừa" và "gỡ game".
3. **Đường cắt MVP và ngân sách UI:** chấp nhận MVP-A khoảng 44 tuần + đệm (PvP người thật lùi sang MVP-B tháng 12–15), hoặc giữ PvP người thật trong MVP-A và cắt khoảng 13 tuần ở chỗ khác. Áp luật UI ≤4+1 thanh, ≤5 nút, 3+1 skill trên mọi nền tảng. Mọi ý tưởng mới ở R3 phải ghi rõ nó thay thế cái gì trong danh sách MVP.
