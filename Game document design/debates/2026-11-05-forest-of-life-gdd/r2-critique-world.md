# R2 Critique — WORLD

> Lăng kính: *"Cơ chế này đang nói gì về thế giới, và nó có cùng thông điệp với theme "Kẻ mạnh nhất không phải kẻ ăn nhiều nhất, mà là kẻ nuôi được cả khu rừng" không?"*
> Tôi thừa nhận trước 3 điểm mình sai/thua lý ở R1: **(1)** 9 cảnh giới → tôi chấp nhận **7** của PROG; **(2)** 9 Thần Vị → chấp nhận **5 (Ngũ Hành)**; **(3)** "Đạo Tâm" của tôi (la bàn hành vi) trùng tên với tiền tệ meta của PROG/PX → tôi đổi tên thành **Tâm Hướng**.

---

## Về SURV

### Giữ lại (Keep)
- **SURV-03 (3 lớp thân: Tán/Thân/Tâm Rễ):** câu trả lời đúng nhất cho M1 của PX. Lore cũng hợp: Tâm Rễ chính là chỗ Mộng Hỏa trú ngụ.
- **SURV-07 (6 động từ + 5 áp lực):** biến cây thành nhân vật chính chứ không phải idle game. Session mẫu 30' là tài liệu tốt nhất trong cả 4 bản.
- **SURV-10 (gặm cỏ: thú nhận 40%, cây không chết vì bị gặm):** đúng sinh học, đúng theme. Ăn quả thì có lợi cho cả hai, gặm lá thì có lợi cho một bên.
- **SURV-17 ("mỗi sự kiện có kẻ thắng và kẻ thua theo giới"):** tôi nhận đây là quy tắc chung cho mọi world event.

### Mượn (Steal)
- **SURV-13 "Ý Chí Rừng" (Director):** tôi lấy làm lore chính thức. Director là **giấc mộng còn sót của Kiến Mộc**. Khi một sinh linh bị dồn quá mức, "rừng thương nó" (quả rơi, mưa xóa mùi). Lời giải thích có sẵn trong thế giới nên không cần UI.
- **SURV-15 Mộc Mộ:** gộp với Mộ Linh (WORLD-08). **Mộ Linh** (hoa + 1 dòng biên niên) dùng cho mọi sinh linh C4+. **Mộc Mộ** (landmark 2 ngày, +2 mật độ) chỉ dùng cho cây C5+.
- **SURV-08 Linh Hóa Địa:** đây là hành động "nuôi rừng" rõ nhất trong cả 4 proposal. Tôi sẽ đặt nó làm trụ của điều kiện Thần Cách (xem PROG).

### Phản biện (Challenge)
| ID | Mức độ | Vấn đề | Tình huống người chơi | Đề xuất thay thế / cách kiểm chứng |
|---|---|---|---|---|
| SURV-09 | **Major** | Sổ Năng Lượng 40/20/40 **bảo toàn hoàn hảo**: giết bao nhiêu thì năng lượng cũng quay về đất. Vì vậy "săn sạch một vùng" **không có hậu quả sinh thái**, và theme chỉ còn là lời nói. Chỗ rò rỉ thật là linh khí bị khóa vào tu vi của kẻ mạnh, nhưng ledger không theo dõi nó. | 4 sói C4 farm Thung Lũng Sương 3 tối. Trong ledger mọi thứ vẫn "cân", rừng không xám đi, không ai cần nấm. | Gộp SURV-09 với **WORLD-03b (quỹ linh khí vùng)**. Linh Mạch nạp quỹ với tốc độ cố định. Tu luyện và **upkeep cảnh giới (SURV-08)** rút từ quỹ. Phần 40% về đất trả lại quỹ **chậm** (qua phân giải, nấm làm nhanh ×3). Quỹ <30% thì Khô Linh. Kiểm chứng: PROG thêm quỹ vùng vào `prog_sim.py` và chứng minh 4 thú săn C4 làm vùng Khô Linh trong ≤3 ngày-rừng, còn 2 thú + 1 cây + 1 nấm thì không. |
| SURV-15 | **Major** | "Đầu thai Hậu Duệ" chỉ mất 1 tiểu cảnh nên cái chết gần như vô giá (khoảng 10 phút với R1–R2, khoảng 2 session với R5). Nó cũng đá trực tiếp với PROG-10 (mất cảnh giới, catch-up ×3). Về theme thì tôi **rất muốn** giữ Hậu Duệ: "Ta để lại gì?" là arc hồi 3. | Sói C5 luôn đẻ sẵn 2 Huyết Noãn trong hang, chết là sống lại ngay. PvP ở Cổ Đại mất sức nặng. | Giữ Hậu Duệ nhưng **rơi về đầu đại cảnh giới hiện tại**, giữ Huyết Mạch, **không** nhận Đạo Tâm (vì không qua Trung Ấm). Đổi loài thì nhận Đạo Tâm + catch-up. Đây là đánh đổi "dòng dõi vs khai ngộ". PROG chốt số. |
| SURV-11 / SURV-07 | Minor | Va chạm từ vựng. SURV dùng "Bế Quan" cho việc tu trong session (×1.5), PX dùng "Bế Quan" cho việc offline. SURV dùng "Xuất Khiếu" cho skill cây R1, PROG dùng "Xuất Khiếu" làm tên cảnh giới C6. | Người chơi đọc "Bế Quan" trong tutorial cây, rồi tắt app, rồi không hiểu vì sao báo mộng gọi cũng là Bế Quan. | Theo **Glossary đề xuất** ở cuối. Skill cây R1 đổi thành **Linh Thức** (tên của PROG), tới C6 tiến hóa thành Xuất Khiếu thật. Bản thân việc đổi tên này đã là một arc tiến trình. |
| SURV-17 | Minor | Linh Triều có 3 nhịp khác nhau: SURV 1 lần/tuần, PX 2 lần/ngày, WORLD 1 lần/2 mùa. | — | Đặt **Linh Tức** ("rừng thở") 2 lần/ngày × 15' (PX). **Linh Triều** 1 lần/tuần × 2h (SURV). **Khô Mục Xâm Lấn** của SURV làm mối đe dọa của cả kỷ nguyên, với lore là **dấu vết Nhân Tu rút Linh Mạch** (hồi 2). |

### Câu hỏi cho SURV
1. Bạn có chấp nhận rằng upkeep cảnh giới (SURV-08) rút từ **quỹ vùng** chứ không chỉ từ kho cá nhân không? Đây là chỗ biến "kẻ mạnh ở lâu thì làm rừng đói" thành luật.
2. Khi đổi sang mùa 3,5 ngày (xem Xung đột), tần suất Đại Hạn và Trùng Tai "1/mùa" có còn ổn không?

---

## Về PROG

### Giữ lại (Keep)
- **PROG-01 (7 cảnh giới × 3 tầng):** tôi đổi ý. Lý do: 18 tầng đã có sim, độ khó đọc với casual, và **khung 7 khớp hoàn hảo với 3 cấp rừng của tôi**. Rừng Non là C1–C3 (trần Áp Chế n=9). Nguyên Sinh là C4–C5 (trần n=15). Cổ Đại là C6–C7. Ba kiếp lớn của PROG-07 đều là ngưỡng cửa: Trung Kiếp C3→C4 = phi thăng Hạ Lâm→Linh Lâm, Đại Kiếp C5→C6 = phi thăng Linh Lâm→Thần Lâm, Thiên Kiếp = Thành Thần. Tôi không phải bẻ gì cả.
- **PROG-03 ("phương sai là bản sắc loài"):** đây là cách nói cơ học đẹp nhất của câu "cây chậm mà chắc, sói được ăn cả ngã về không".
- **PROG-05 (Huyết Mạch Ấn, learn-by-doing):** "con đường được viết từ cách mình sống" đúng với pillar Rừng Nhớ.
- **PROG-11 (Tốc không scale):** đây là luật chống bắt nạt có tính sinh thái nhất. Con mồi luôn có thể chạy.

### Mượn (Steal)
- **PROG-05 → Tâm Hướng (WORLD-13b):** tôi **bỏ hệ đo hành vi riêng**. Tâm Hướng (Sinh↔Sát, Hợp↔Độc) trở thành *một lớp hiển thị* đọc từ chính dữ liệu Huyết Mạch Ấn/Đạo Ngộ. Dùng 1 nguồn dữ liệu cho 2 mục đích: lựa chọn nhánh (PROG) và aura, lời NPC, biến thể Tâm Ma (WORLD).
- **PROG-07 Tâm Ma:** bản sao kỹ năng của chính mình làm **nền** (rẻ). Tâm Hướng thêm **modifier**: nghiêng Sát thì thêm 2–4 bóng con mồi đã ăn, nghiêng Hợp thì phải cứu ảo ảnh đồng đội. Có trần độ khó để Sát không bị phạt kép.

### Phản biện (Challenge)
| ID | Mức độ | Vấn đề | Tình huống người chơi | Đề xuất thay thế / cách kiểm chứng |
|---|---|---|---|---|
| PROG-13 | **Major** (ludonarrative) | Thần Cách có lối "hạ một Cổ Thú", và Thần Lực lấy một phần từ Tín Ngưỡng. Con đường thành thần vẫn có thể là **giết**. Kẻ ăn nhiều nhất lên đỉnh, ngược hẳn với theme. | Huyết Lang C6 Hậu farm Cổ Thú, lên thần mà chưa từng nuôi gì. Sau đó Thần Vực của nó cũng chẳng cần sống. | Thần Cách = **tích lũy Sinh Khí đã trả cho rừng** (Linh Hóa Địa, Quả Ước bị ăn, xác trả quỹ, Hộ Pháp, bảo vệ vùng trong world event), ngưỡng chung cho mọi loài. Sói thì đạt bằng cách giữ quần thể mồi khỏe, đẩy Nhân Tu, Hộ Pháp. Thần Lực = f(sinh khí Thần Vực) theo WORLD-02. "Hạ Cổ Thú" vẫn tính, nhưng **chỉ khi Linh Hạch được trả về quỹ vực** chứ không nuốt. Kiểm chứng: sim thời gian để đạt Thần Cách theo loài phải trong ±20%. |
| PROG-02 | Minor→Major | Tên C5 của các loài là "Thụ Nhân/Lang Nhân/Lộc Tiên", ngầm định đã chọn Nhân Hình. PROG-08 lại có Bản Thể Đạo từ chối hóa hình. Con sói giữ yêu thân mà vẫn bị gọi "Lang Nhân". Ngoài ra PX để Hóa Hình là "Could" (rig đắt). | Người chơi chọn Bản Thể, rồi UI gọi họ là "người". | Tên C5 **phân nhánh theo Đạo**: Nhân Hình là "Thụ Nhân/Lang Nhân", Bản Thể là "Cổ Mộc Yêu/Yêu Lang". **MVP: C5 chỉ có Bản Thể** (không cần rig mới), còn Nhân Hình ra sau. Bảng tên hợp nhất ở cuối. |
| PROG-08 | Minor | Nhân Hình "nói chuyện với phe NPC, chế tác, bí cảnh Nhân giới" cần NPC người sống, trái với A2 (NPC bất động) và tốn chi phí. | — | Giữ fantasy, đổi nội dung. Nhân Hình là **hình dạng của kẻ đã chặt Kiến Mộc**, nên mở được việc đọc khắc đá trận pháp, vào **trại Nhân Tu bỏ hoang** (bí cảnh), và trà trộn giảm aggro của đoàn Nhân Tu trong E5. Không có NPC người biết nói. Câu hỏi đạo đức "mang hình hài kẻ thù" là miễn phí. |
| PROG-04 | Minor | Tĩnh Tu Tích Lũy là thiết kế tốt (chống AFK). Nhưng nó đang đá với PX-04 (60% tu thụ động offline). | Xem Xung đột #3. | Tôi đứng về PROG ở phần CT, và mượn ý của PX ở phần *thế giới thay đổi thấy được*. |

### Câu hỏi cho PROG
1. Thêm biến "quỹ vùng" vào sim có làm vỡ mục tiêu 1.0 CT/phút không? Tôi chấp nhận lệch ±15% theo tình trạng vùng, coi đó là tín hiệu sinh thái.
2. 5 Thần vị/server với server Rừng Non 24–40 người thì có quá nhiều không? Hay Thần Vị chỉ tồn tại ở tầng Cổ Đại/solo?

---

## Về PX

### Giữ lại (Keep)
- **PX-03 (bảng mâu thuẫn brief):** đây là bản đồ rủi ro trung thực nhất. M3 giải đúng bệnh "thần chiếm server".
- **PX-12 luật skin không đổi silhouette:** đồng thời bảo vệ **khả năng đọc chuỗi thức ăn**, tức pillar P1.
- **PX-16 Thiên Đạo cân bằng loài:** đây là ludonarrative harmony thuần, *rừng tự cân bằng*. Lore: Ý Chí Rừng "gọi" Mộng Hỏa về loài đang thiếu.
- **PX-14 tự kiểm "không cắt cây/luân hồi/độ kiếp/PvP chung":** tôi ký tên.

### Mượn (Steal)
- **PX-09 Linh Ảnh → "Mộng Ảnh":** trong lore, đây là dư ảnh của những Mộng Hỏa khác trong giấc mộng Kiến Mộc. Solo vẫn "có người thật" mà không cần giải thích kỹ thuật.
- **PX-04 Báo mộng → "Mộng Báo":** khớp S3 (người chơi là Mộng Hỏa). Khi offline, Mộng Hỏa chìm về giấc mộng, và khi tỉnh thì kể lại.
- **PX-05 "Oán Linh":** mở rộng thành **móc trả thù emergent**. Nạn nhân bị lấn yếu nhận Duyên với loài của kẻ giết (WORLD-11) cùng 1 lần "Oán Truy" (thấy hướng kẻ đó trong 1 ngày-rừng ở kiếp sau). Phải có trần chống alt-farm: tối đa 1 Oán Linh/24h.

### Phản biện (Challenge)
| ID | Mức độ | Vấn đề | Tình huống người chơi | Đề xuất thay thế / cách kiểm chứng |
|---|---|---|---|---|
| PX-08 | **Major** | Lý do để kiếp đầu là thú nhỏ đúng (vui trong 30s, chết trong FTUE). Nhưng hook của brief và của chính USP PX là "**bạn có thể là cái cây**". Theo kịch bản hiện tại, cây là phần thưởng an ủi sau một cái chết bị script ép. Thêm vào đó, cái chết do sói AI "gần như chắc chắn" lại dạy rằng *rừng bất công* chứ không phải *rừng tuần hoàn*. | Người chơi tải game vì trailer "kiếp sau em là cổ thụ", rồi phải làm chuột 14 phút, rồi bị sói giết vô cớ. | **Giữ chuột, đổi xương sống.** (1) Phút 0:00 là Mộng Hỏa rơi qua tán một cổ thụ khổng lồ. Giọng đầu tiên là **cái cây** (Lão Tùng, 1 câu), nên cây có ý thức ngay giây thứ 10. (2) Phút 8–11, cây AI phản kích con chuột, rồi thả **Linh Quả**. Chuột ăn quả và **mang hạt** (tutorial Quả Ước, WORLD-14d). Linh Thử là loài trữ hạt, đúng sinh học. (3) Chuột chết ở Linh Tức, **hạt trong bụng nảy mầm từ xác**. Lựa chọn luân hồi mặc định là "trở thành hạt giống ngươi đã mang". Toàn bộ theme hiện ra trong 16 phút: ăn → mang hạt → chết → nuôi → thành cây. Kiểm chứng: A/B test "chuột→hạt" với "chọn loài ngay", đo H2/H3. |
| PX-09 / PX-15 | **Major** | Kỷ nguyên 14/28 ngày không khớp với lịch 6,5 tuần của PROG để tới Thiên Kiếp, cũng không khớp với "Kiếp ~7 tuần" của tôi. PX-07 lại cho thành thần diễn ra ở "cảnh giới cuối" trên một server mà MVP chỉ có C1–C5. | Người chơi Mid ở Rừng Non 14 ngày, reset, rồi không bao giờ thấy được thần. | Xem Xung đột #2: lịch lồng nhau theo cấp rừng. 14 và 28 ngày của PX được **giữ nguyên** và được gán nghĩa lore. |
| PX-07 | Major (từ vựng/lore) | "Phi Thăng" được dùng cho 2 việc: chuyển cấp rừng và thành thần rời bàn chơi. Thần bị loại khỏi thế giới thì endgame chỉ còn là một tấm bia. | — | **Phi Thăng** chỉ dùng cho chuyển cấp rừng. **Thành Thần** = cắm rễ vào Thần Vị: rời *chuỗi thức ăn* (không ăn, không nhận thưởng giết, Thần Quy của PROG) nhưng **ở lại thế giới** như một vùng sống. Cuối kỷ nguyên, thần **Quy Căn** (歸根, "trở về gốc"), tên được khắc lên Thần Bia, rồi luân hồi. Giữ được M3 của PX mà thần vẫn có mặt. |
| PX-04 | Minor | Trần 25% lãnh thổ ngoài của PX, 20% Tán của SURV và 60s "nhập định" của PX với 30s "Hồn Thoát" của SURV là các số khác nhau cho cùng một luật. | — | Một luật, một tên: **Nhập Định**. SURV chốt số. |
| PX-01 hook | Minor | Hook trailer nói "ngọn cỏ bị dẫm nát", nhưng MVP không có loài cỏ. | Marketing hứa thứ game chưa có. | Đổi thành "Kiếp này em là con chuột mang hạt. Kiếp sau em là cổ thụ mọc từ xác chính mình", khớp với FTUE mới. |

### Câu hỏi cho PX
1. Mộc Độn (14f) và Ký Hồn Mộc (14i) đều rẻ và là lý do để rủ bạn chơi cây. PX có đưa chúng vào bậc "Should" cùng co-op không?
2. Tiền Kiếp Ấn (kiếm được, không bán) có làm giảm giá trị skin nền không?

---

## Ludonarrative Audit (theme: "kẻ nuôi được cả khu rừng")

| Hệ thống | Hài hòa / Mâu thuẫn | Sửa |
|---|---|---|
| SURV-10 Quả Ước / ăn quả | ✅ Cho đi có lợi hơn bị cướp | — |
| SURV-08 Linh Hóa Địa, PROG-03 cộng sinh 60/60 | ✅ Hợp tác là trò chơi dương | Tính vào Thần Cách |
| PX-16 cân bằng loài | ✅ | — |
| SURV-09 ledger không có khan hiếm vùng | ⚠️ Săn sạch không tốn gì | WORLD-03b quỹ vùng |
| PROG-12 thưởng hạ người chơi 8 CT > săn AI 4.4 CT | ⚠️ Nhẹ: PvP vẫn là mỏ tu vi tốt nhất | Chấp nhận (P1 cần), nhưng mỗi kill PvP ở vùng Khô Linh ×0.5 |
| PROG-13 Thần Cách qua giết Cổ Thú | ❌ Kẻ ăn nhiều nhất thành thần | Thần Cách = Sinh Khí đã trả |
| Tâm Hướng "Sát" | ⚠️ Rủi ro biến săn mồi thành "tà đạo" | **Săn tự nhiên không phải tội.** Chỉ Sát Nghiệp (lấn yếu) bị phạt. Sát là một đạo hợp lệ, có Keystone riêng |
| PX-04 offline 60% tu thụ động | ⚠️ Tu vi đến từ ngủ chứ không từ sống | Dùng rested của PROG (Xung đột #3) |

---

## Xung đột liên domain phát hiện được

| # | Xung đột | Các ID | Lập trường của tôi | Gợi ý giải quyết |
|---|---|---|---|---|
| 1 | **Số và tên cảnh giới** | PROG-01/02, WORLD-12, SURV A4 | **Chấp nhận 7.** Ánh xạ: Non C1–3 / Nguyên Sinh C4–5 / Cổ Đại C6–7 | Bảng tên hợp nhất bên dưới. Tên khung chung theo PROG |
| 2 | **Lịch thời gian & reset** | SURV A1–A2, WORLD-08, PX-09/15, PROG-04/13 | **Lịch lồng nhau, mỗi cấp rừng có nghĩa lore riêng** | Ngày = 20' (SURV). **Mùa = 3,5 ngày thực, năm-rừng = 14 ngày.** Rừng Non: kỷ nguyên = **1 năm (14 ngày)**, "rừng non sống một năm", kết bằng Đại Di Cư/Phi Thăng. Nguyên Sinh = 2 năm (28 ngày, khớp Pass "Kỷ Nguyên" của PX). Cổ Đại = 4 năm (~8 tuần), kết bằng **Đại Kiếp** (Kiến Mộc trổ chồi), thần Quy Căn. MVP chưa có Cổ Đại thì Thần Vị chỉ có ở **solo** (PROG-13). Đánh đổi: SURV mất nhịp 2 ngày/mùa, nhưng mỗi tuần vẫn có 2 mùa |
| 3 | **Offline / Bế Quan** | SURV-12, PX-04, PROG-04 | CT offline = 0. Rested pool của PROG giữ nguyên. Thứ thấy được khi tỉnh dậy: rễ lan ≤2 ô, quả chín, Mộng Báo | Lore: Mộng Hỏa chìm về Linh Mạch để mộng, nên chỉ an toàn nơi rễ/hang của mình chạm đất. "Mộng Tích" (rested) đầy sau 8h |
| 4 | **Chống bắt nạt** | SURV-11 Sát Nghiệp, PROG-12 Sát Nghiệp, PX-05 Nghiệp Lực, WORLD-16 Thiên Phạt | **Một tên: Sát Nghiệp.** Chỉ tính khi chênh ≥2 đại cảnh giới *sau Áp Chế* (bỏ mức +1 của PX: chênh 1 cảnh giới là chuỗi thức ăn tự nhiên). Nạn nhân đánh trước thì không tính | Thang hậu quả: 1–2 Nghiệp: thưởng theo `0.25^g` (PROG), aura đỏ, kiếp +10%/Nghiệp. 3–4: **Huyết Sát** hiện map, thưởng ×3 cho người hạ. 5: **Thiên Phạt**, sét đuổi 1 ngày-rừng. Sống sót thì Nghiệp về 0 nhưng mất 10% CT tầng. Chết thì Trung Ấm ×2 thời gian. Giảm 1 mỗi 2h *chơi* (PROG), không phải ngày thực |
| 5 | **Từ vựng va chạm** | SURV/PX/PROG/WORLD | Bắt buộc có glossary | **Bế Quan** = thoát an toàn. **Nhập Định** = trạng thái dễ tổn thương khi thoát sai chỗ. **Đả Tọa** = luyện linh khí→tu vi trong session. **Mộng Tích** = rested. **Linh Thức** (C1–5) → **Xuất Khiếu** (C6). **Đạo Tâm** = meta. **Tâm Hướng** = la bàn hành vi. **Phi Thăng** = chuyển cấp rừng. **Thành Thần / Quy Căn** |
| 6 | **Mở khóa loài** | WORLD-11 Nghiệp Duyên, PROG-10/PX-12 Đạo Tâm | Tôi lùi một bước: Duyên **giảm giá** chứ không khóa cứng | Giá Đạo Tâm để mở loài X × (1 − 0.2 × Duyên, sàn 0.4) |
| 7 | **Số loài MVP** | SURV (4), PROG (Mộc/Lộc/Lang), PX (Thử/Mộc/Lang) | Ủng hộ **Linh Thử** của PX: vai trò trữ hạt nối thẳng với cây. Hươu là AI gây áp lực lá | — |

**Bảng tên cảnh giới hợp nhất (đề xuất, ≤4 âm tiết):**
| C | Khung | Linh Mộc | Linh Thử | Lang | Khuẩn |
|---|---|---|---|---|---|
| 1 | Khai Linh | Manh Nha | Khai Trí | Ấu Lang | Bào Tử |
| 2 | Tụ Linh | Trát Căn | Linh Thử | Lang Nha | Khuẩn Ty |
| 3 | Trúc Cơ | Thành Tán | Ẩn Huyệt | Lang Cốt | Khuẩn Võng |
| 4 | Kết Đan | Niên Luân Kết Tâm | Thử Đan | Lang Đan | Ngưng Tán |
| 5 | Hóa Hình | Thụ Nhân ‖ Cổ Mộc Yêu | Thử Nhân ‖ Yêu Thử | Lang Nhân ‖ Yêu Lang | Khuẩn Nhân ‖ Khuẩn Yêu |
| 6 | Xuất Khiếu | Mộc Hồn | Thử Hồn | Nguyệt Lang Hồn | Địa Mạch Hồn |
| 7 | Thành Thần | Thần Mộc | Thử Thần | Thiên Lang | Luân Hồi Mẫu |

---

## Top 3 điều team phải chốt
1. **Glossary + lịch lồng nhau** (Xung đột #1, #2, #5): 7 cảnh giới ↔ 3 cấp rừng ↔ 3 kiếp lớn ↔ kỷ nguyên 14/28/~56 ngày. Nếu chưa chốt điều này, mọi bảng số và mọi dòng UI vẫn sẽ còn va nhau.
2. **Một mô hình năng lượng khép kín** gồm ledger của SURV, CT của PROG và quỹ vùng của WORLD. Đây là nơi duy nhất theme "nuôi được rừng" trở thành *luật* chứ không chỉ là lời, và nó quyết định Thần Cách.
3. **Giá của cái chết và nhịp chết đầu tiên:** Hậu Duệ vs đổi loài (SURV-15 vs PROG-10), Sát Nghiệp hợp nhất, và FTUE "chuột mang hạt → cây mọc từ xác".
