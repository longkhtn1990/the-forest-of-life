# R2 Critique — PROG

> Vai trò thêm ở vòng này: **kiểm chứng số liệu** của team. Mô phỏng mới: `sim/prog_r2_sim.py` → `sim/prog_r2_sim_output.md` (mục F–M). Mọi con số "(sim X)" dưới đây lấy từ file đó.
> Đơn vị chung tôi dùng để đối chiếu: **1 CT = tu vi chuẩn của 1 phút chơi tích cực** (PROG-03). Người chơi Mid chơi 5 phiên × 40 phút mỗi tuần, được khoảng 320 CT/tuần, tức khoảng 64 CT/phiên.

## Tóm tắt kiểm chứng số liệu (đọc trước)
| # | Con số được rà | Nguồn | Kết quả |
|---|---|---|---|
| 1 | Offline nhận 60% tốc độ tu luyện, trần 8h | PX-04 | **Vỡ đường cong.** CT/tuần tăng ×7.3, chạm Thiên Kiếp sau 0.7 tuần. Nếu thêm quảng cáo +2h thì ×8.9 (sim H) |
| 2 | Mùa/kỷ nguyên 14 hoặc 28 ngày | PX-09 | Với 28 ngày, **0% người chơi Mid** chạm Thiên Kiếp (cả đường cong cũ lẫn mới). Với 14 ngày, chỉ 1% Casual xong Rừng Non (sim I) |
| 3 | Một Kiếp ≈ 7 tuần, 48 ngày | WORLD-08 | **Khớp nếu dùng đường cong mới.** 63% người Mid chạm Thiên Kiếp, trung vị ngày 36. Đường cong R1 của tôi chỉ đạt 29%, trung vị ngày 44, quá sát ngày reset (sim I) |
| 4 | Đại Kiếp kích hoạt khi đủ 9 Thần Vị | WORLD-02/E8 | **Kết thúc mùa quá sớm.** Người Core chạm Thiên Kiếp trung vị ngày 20–21, nên 9 ghế có thể đầy vào khoảng ngày 25 và reset xảy ra khi người Mid mới ở C5–C6 |
| 5 | Tiến trình −1 tiểu cảnh (Hậu Duệ), hồi phục ≤2 tuần với R7+ đã đầu tư 60h | SURV-15 | Không nhất quán với nhau. Theo đường cong thực tế, C8 chỉ mất 15.4h đầu tư. Muốn "60h hồi trong 2 tuần" thì cần hệ số catch-up ×9. Hậu Duệ chỉ tốn 0.2 tuần, rẻ hơn đổi loài 3–6 lần (sim J) |
| 6 | Sinh Năng chia 40/20/40 | SURV-09 | Nếu Sinh Năng = tu vi lũy kế thì giết một người C6 cho **359 CT (6 giờ chơi)** và kill-trading lãi +188 CT/giờ (sim M) |
| 7 | Cộng dồn bonus đầu kiếp | cả 4 người | Nhân dồn trong trường hợp xấu nhất lên tới **×82** (sim K) |
| 8 | Sự kiện 8–24 phút (Huyết Nguyệt, Linh Triều) | WORLD-10 | Người Mid chỉ gặp trong **4–6% số tuần** (sim L) |
| 9 | Hệ số 1.6–1.8× combat power mỗi cảnh | PX-05 | R1 của tôi là ×1.77, đạt yêu cầu. Bản Cửu Cảnh là ×1.59 (sim G) |
| 10 | Ngày-rừng 20' (SURV) và 24' (WORLD); mùa 48h; năm 8 ngày | SURV/WORLD | Mùa và năm khớp nhau. **Độ dài ngày lệch nhau**, cần chốt một con số |

---

## Về SURV
### Giữ lại (Keep)
- **SURV-01** (HUD 2+2): một bộ code needs cho mọi giới, và người vừa luân hồi không phải học lại HUD.
- **SURV-03** (3 lớp thân cây): đây là lời giải tốt nhất cho bài toán "cây bất động trong PvP tự do".
- **SURV-07** (6 động từ cây + Plant Pressure Map): cây có quyết định thật. Ý này cũng trả lời được rủi ro H3 của PX.
- **SURV-10** (thú chỉ nhận 40% so với phần cây mất): nguyên tắc đúng. Nhưng xem phản biện số 2 về đơn vị.
- **SURV-12** (quy tắc offline: Nhập Định, Hồn Thoát 30s), **SURV-13** (Director), **SURV-15** (Hồn Hộ 10'), **SURV-16** (cây phải chuẩn bị trước khi độ kiếp).

### Mượn (Steal)
- **SURV-03 → PROG-11b:** ngân sách sức mạnh `PB(n)` của thực vật chia thành Tán 20%, Thân 50%, Tâm Rễ 30%. TTK được tính đến lúc Thân về 0 (cây Đổ), không tính đến Tâm Rễ.
- **SURV-11** (Ấu Thể Ẩn Khí, Thoát Sinh) → đưa vào Thiên Đạo Luật hợp nhất (xem phần xung đột). Thưởng Thoát Sinh là 2 CT, đúng bằng "Kinh Hồn Ngộ Đạo" của Lộc.
- **SURV-07** (sợi mệnh bán kính 30 ô) → thêm vào PROG-08 Nhân Hình Đạo cho thực vật.
- **SURV-18** (Thiên Tài Địa Bảo) → dùng làm vật phẩm **Cơ Duyên** cho đột phá (PROG-07).

### Phản biện (Challenge)
| ID | Mức độ | Vấn đề | Tình huống người chơi | Đề xuất thay thế / cách kiểm chứng |
|---|---|---|---|---|
| SURV-15 | **Blocker** | Bảng cost-of-death tự mâu thuẫn. (a) Số giờ đầu tư (R5–R6 20–50h, R7+ 60h+) gấp 3–4 lần đường cong mà cả PROG lẫn PX đều nhắm (Mid tới Thiên Kiếp ≈17–22h). (b) "×2 tới 50% đỉnh" cho C8 mất **3.46 tuần** để hồi, trái với mục tiêu ≤2 tuần. (c) Hậu Duệ chỉ mất 1 tiểu cảnh, tốn 0.20–0.26 tuần, trong khi đổi loài tốn 0.7–1.6 tuần. Mọi người sẽ chọn Hậu Duệ và USP "luân hồi đổi loài" chết (sim J) | Lan là sói C5 bị giết. Nếu đầu thai Hậu Duệ, cô mất 1 buổi tối chơi. Nếu đổi loài, cô mất 1.4 tuần. Cô không bao giờ thử làm cây | **Hậu Duệ (b):** rơi 1 cảnh giới (không phải 1 tiểu cảnh), giữ Huyết Mạch và lãnh thổ, cày lại với tốc độ ×1.5. Ở C5 tốn 0.47 tuần. **Đổi loài:** dùng PROG-10 (×3/×1.5) cộng Túc Tuệ và Đạo Quả, ở C5 tốn 0.69 tuần. Hậu Duệ rẻ hơn một chút nhưng phụ thuộc vào neo, mà neo thì bị phá được. Kiểm chứng qua telemetry: tỉ lệ chọn đổi loài cần ≥35% |
| SURV-09, SURV-02 | **Major** | Có 5 đơn vị năng lượng (No, Quang Tinh, linh khí, Sinh Năng, tu vi) nhưng không có bảng quy đổi. (a) Thú ăn cỏ chỉ cần 25 lần cắn (37.5s) cho mỗi 6 phút để đầy No. Nếu tu vi chỉ đến từ việc ăn thì Lộc chỉ tu được khoảng 10% thời gian chơi. (b) Sinh Năng chưa định nghĩa. Nếu Sinh Năng = tu vi lũy kế thì giết một người C6 cho 359 CT và kill-trading lãi +188 CT/giờ (sim M) | Hai người bạn C4 luân phiên giết nhau tại neo Hậu Duệ để cày tu vi | **Sinh Năng = 20 CT chuẩn hóa** (hiển thị phóng to theo cảnh giới). Chia 40/20/40 thành: **8 CT** cho kẻ ăn (đúng 8 CT của PROG-12), 4 CT vào Linh Hạch, 8 CT vào đất (Khuẩn nhận khoảng 3 CT, đúng giả định trong sim D của R1). Ăn khi đã no vẫn được: phần dư chuyển thành linh khí với hiệu suất 50%, nhờ vậy CT từ việc gặm không bị No chặn trần |
| SURV-06, SURV-08 | **Major** | Bế Quan "tu vi ×1.5" và tĩnh tọa hấp thu +3 đến +25/phút. Nếu đây là tốc độ *sinh* tu vi, ngồi im trong Hang sẽ là chiến lược trội (AFK, an toàn, ×1.5) | Người chơi P1 vào game, bế quan 40 phút rồi thoát. Không ăn, không săn | Bế Quan **chỉ luyện hóa linh khí đã tích** theo tỉ lệ 1:1 (Hang cấp 3 thì ×1.2), không sinh linh khí mới. Tĩnh tọa cho tối đa 40% tốc độ chơi tích cực và về ×0.2 sau 3 phút (giống luật chống AFK của PROG-03) |
| SURV-16 | Major | Kiếp thất bại phải chờ 24h thực. Với 8 lần đột phá và tỉ lệ thất bại lần đầu 30–40%, mỗi kiếp trung bình bị chặn khoảng 2.8 ngày. Người Casual (3 phiên/tuần) mất tới gần 1 tuần | Người chơi thất bại kiếp ở phút 35 tối thứ Sáu. Phiên Chủ nhật không làm gì được | Thay bằng debuff "Đạo Cơ Tổn" 20 phút và mất 30% CT tầng (PROG-07). Thời gian chờ tự nhiên là phiên kế tiếp |
| SURV-03 | Minor | Mỗi ô rễ ở đất ẩm cho +2 Thủy/phút. 12 ô cho +24/phút, trong khi decay chỉ −3/phút, nên need Thủy gần như không tồn tại | Cây vươn 3 ô rễ là không bao giờ khát nữa | Thủy hấp thu `= 6 × (1 − e^(−ô_ẩm/4))`/phút, trần khoảng 6. Đại Hạn ×2.5 decay thì vẫn có áp lực |
| SURV-07 | Minor | Rễ ×2 mỗi đại cảnh giới, nên C8 có 1.536 ô. Phí duy trì Quang Tinh và hiệu năng lưới đều nổ | Một cây C8 phủ kín cả một Thần Vực | Đổi thành ×1.6 mỗi cảnh giới, C8 còn khoảng 322 ô |
| SURV-12 | Minor | Quang hợp offline 25%. Nếu được tính vào CT thì CT/tuần ×3.6 (sim H) | Mọi người chọn chơi cây vì cây tự lớn khi offline | Quang hợp offline chỉ ra **Quang Tinh** (tài nguyên có trần), không ra CT |

### Câu hỏi cho SURV
1. "Bế quan tu vi ×1.5" là hiệu suất quy đổi linh khí hay tốc độ sinh?
2. Bảng giờ đầu tư trong SURV-15 dựa trên đường cong nào? Có đồng ý neo theo tổng ≈1.700 CT (17h Mid) không?
3. Có chấp nhận Sinh Năng = 20 CT chuẩn hóa thay vì tỉ lệ theo tu vi tích lũy không?

---

## Về WORLD
### Giữ lại (Keep)
- **WORLD-02** (4 sự thật): giải thích được luân hồi, reset và endgame chỉ trong 1 phút đọc.
- **WORLD-04** (3 cấp rừng = 3 giới phi thăng, phân thân bị giới hạn khi quay về): chính là Thiên Đạo Áp Chế của tôi nhưng có lore.
- **WORLD-05** (wayfinding), **WORLD-11** (Trung Ấm, Tiền Kiếp Ấn, biên niên tự sinh), **WORLD-14d/f/i** (Quả Ước, Mộc Độn, Ký Hồn Mộc).
- **WORLD-12** (tên cảnh giới): tôi chấp nhận toàn bộ bộ tên. Tên của WORLD gắn với sinh học tốt hơn bộ tên của tôi (ví dụ Kết Kén là kiếp của côn trùng).

### Mượn (Steal)
- **WORLD-12 + A3 → PROG-01b "Cửu Cảnh".** Tôi **đổi lập trường từ 7 sang 9 cảnh giới**: 8 cảnh giới để cày × 3 tầng, cộng C9 Thành Thần. Phân bổ 3/3/3 theo cấp rừng. Lý do là sim F và I: khi giữ tổng thời gian cố định, 9 cảnh giới cho nhịp 2.5–4.4 phiên mỗi cảnh (khớp PX-10) và vừa với Kiếp 48 ngày. Bảng đường cong mới:

| C | Cấp rừng | CT cả cảnh | Lũy kế (gồm kiếp) | Tuần Casual / Mid / Core | Lời hứa mở khóa |
|---|---|---|---|---|---|
| 1 Khai Linh | Non | 36 | 41 | 0.3 / 0.1 / 0.1 | Bản Năng, 2 kỹ năng |
| 2 Luyện Khí | Non | 90 | 141 | 1.1 / 0.4 / 0.2 | Co-op, Linh Thức (cây) |
| 3 Trúc Cơ | Non | 160 | 321 | 2.5 / **1.0** / 0.6 | Huyết Mạch → kiếp phi thăng |
| 4 Kết Đan | Nguyên Sinh | 190 | 541 | 4.2 / 1.7 / 1.0 | Đạo Đồ, Keystone 1 |
| 5 Hóa Hình | Nguyên Sinh | 210 | 791 | 6.2 / 2.5 / 1.4 | Hóa Hình / Bản Thể, Thần Thông |
| 6 Nguyên Anh | Nguyên Sinh | 230 | 1.071 | 8.4 / **3.3** / 1.9 | Xuất Khiếu, Nguyên Thần Bất Diệt → Đại Kiếp phi thăng |
| 7 Phản Hư | Cổ Đại | 260 | 1.391 | 10.9 / 4.3 / 2.5 | Keystone 2, đấu Nguyên Thần ở Linh giới |
| 8 Hợp Đạo | Cổ Đại | 280 | **1.671** | 13.1 / **5.2** / 2.9 | Lĩnh Vực (aura đổi địa hình), Thần Cách |
| 9 Thành Thần | — | Thiên Kiếp | — | — | Thần Vị / Thần Vực |

  Tổng thời gian chơi thực của người Mid giảm từ 21.8h xuống **17.4h**. Ở phiên đầu, các tầng xong lần lượt ở phút 7, 14 và 22, khớp nhịp 8–12 phút của PX. Hệ số mỗi tầng giảm từ ×1.10 xuống **×1.08**, tức ×1.26 chỉ số và ×1.59 combat power mỗi cảnh. Tổng biên độ sức mạnh từ đầu đến cuối vẫn giữ khoảng ×5.9 chỉ số.
- **WORLD-13** (la bàn Đạo Tâm) → đưa vào **Huyết Mạch Ấn** (PROG-05b): mỗi loài có 1 nhánh nghiêng Sinh, 1 nhánh nghiêng Sát, 1 nhánh trung tính. **Chỉ có một điểm rẽ nhánh** ở C3, không thêm ngã rẽ Thụy/Hung riêng ở C4. Tôi chặn điểm mù "quá nhiều tầng" của chính mình.
- **WORLD-11 Nghiệp Duyên** → cách mở loài trong Đạo Quả Bàn (PROG-10b).
- **WORLD-07 Lôi Trì** → nơi luyện kiếp.
- **WORLD-16** (luật ai đánh trước thì không bị Nghiệp; Thiên Phạt) → bậc 5 của Thiên Đạo Luật hợp nhất.

### Phản biện (Challenge)
| ID | Mức độ | Vấn đề | Tình huống người chơi | Đề xuất thay thế / cách kiểm chứng |
|---|---|---|---|---|
| WORLD-02 S4, E8 | **Blocker** | Đại Kiếp kích hoạt khi đủ 9 Thần Vị. Sim I: người Core chạm Thiên Kiếp trung vị ngày 20–21, mà 15% Core trên server 120 người đã là 18 ứng viên. 9 ghế có thể đầy vào khoảng ngày 25 và reset cả rừng trong lúc người Mid (trung vị ngày 36) mới ở C5–C6 | Người Mid cày 3.5 tuần, đang ở Hóa Hình thì "Kiến Mộc trổ chồi" và mọi thứ về 0 | **Lịch cố định:** Đại Kiếp diễn ra ở ngày 48 (6 năm-rừng). Thần Vị mở từ khoảng ngày 14. Kiến Mộc cần tổng Thần Lực tích lũy, và về toán học không thể đầy trước ngày 42. Giữ được câu chuyện mà không phụ thuộc người nhanh nhất |
| WORLD-10 | **Major** | Sự kiện đo bằng ngày-rừng (8–24 phút thực) thì hầu như không ai thấy. Sim L: Huyết Nguyệt 8 phút mỗi tuần chỉ được 6% số tuần của người Mid gặp, Linh Triều 24 phút mỗi 4 ngày chỉ 4%. Brief yêu cầu "thường xuyên có sự kiện lớn" mà người chơi *cảm nhận được* | Người chơi 5 tối/tuần cả Kiếp chỉ thấy Huyết Nguyệt 0.4 lần | Sự kiện lớn đo bằng **ngày thực** (24–48h) và có đỉnh 30 phút vào giờ vàng (20h). Mô hình này phủ **85%** số tuần của Mid. Vẫn giữ biến thể ngày-rừng làm sự kiện vi mô |
| WORLD-13 | **Major** | Tâm Ma khó hơn khi nghiêng Sát. Sói vốn sống bằng việc giết nên luôn bị phạt kép, phá luật tương đương giữa các loài (PROG-02) | Hai người cùng C6, một sói một cây. Kiếp của sói khó hơn chỉ vì sói là sói | Sinh/Sát **đo so với baseline của loài**: sói săn NPC là bình thường, chỉ giết người chơi thấp hơn ≥2 cảnh, phản bội hay giết thừa mới tính là Sát. Ngân sách độ khó Tâm Ma cố định, chỉ *mẫu* thay đổi theo Đạo Tâm |
| WORLD-03 | Major | Khô Linh cho tu luyện −50% áp lên **cây không chạy được**. Kẻ phá có thể cố tình hút cạn vùng của cây. Luật cũng chưa có số liệu sức chứa và dòng vào | 4 sói càn vùng có cây C4 của người khác. Cây mất nửa tốc độ cả ngày | Khô Linh áp −50% cho kẻ tiêu thụ nhưng chỉ −20% cho thực vật/nấm. Hành động "hồi linh" cho +CT. Định nghĩa: sức chứa quỹ nuôi bền vững 6 người/vùng, chỉ kích hoạt khi mật độ >2× trong ≥1 ngày thực |
| WORLD-05 | Minor | Linh Nhãn ×8 mật độ linh khí. Nếu ánh xạ vào CT, người ở lõi tu nhanh ×8 | Cả server cắm trại ở Linh Nhãn | Mật độ chỉ tác động tài nguyên và upkeep. Bonus CT theo vòng là ×1 / 1.15 / 1.3 / 1.5 (trần +50%, như PROG-03) |
| WORLD-04 | Minor | Mật độ người chơi trên mỗi màn hình (khoảng 576 ô) là 0.26 / 0.18 / 0.11 cho Non / Nguyên Sinh / Cổ Đại, tức càng sâu càng vắng | Rừng Cổ Đại "hùng vĩ" nhưng 5 phút không gặp ai | Nguyên Sinh 384², Cổ Đại 512² (giữ được khoảng 0.25/màn). Cảm giác "khổng lồ" đến từ camera và scale (PX A4) |
| WORLD-11 | Minor | Nghiệp Duyên kiểu "bị sói ăn 3 lần" không có đường cho cây, vì sói không ăn cây (ma trận SURV-09) | Người chơi cây không bao giờ mở được sói | Duyên còn đến từ: hấp thu xác loài X, cộng sinh, Mộng Cảnh. Mục tiêu: người Mid mở loài thứ 2 trong kiếp 1 |
| WORLD-08 | Minor | Ngày 24 phút, trong khi SURV dùng 20 phút và đã dựng tension graph trên đó | — | Chốt **20 phút** (SURV-19), giữ nguyên mùa 48h và năm 8 ngày |

### Câu hỏi cho WORLD
1. C7 Phản Hư và C8 Hợp Đạo hứa hẹn gameplay gì? Tôi đề xuất Linh giới và Lĩnh Vực. WORLD có lore nào mạnh hơn không?
2. "Thành Thần" (C9, ai qua Thiên Kiếp cũng đạt) và "Thần Vị" (9 ghế) có tách riêng không? Sim cho thấy khoảng 30 người qua Thiên Kiếp mỗi Kiếp, trên server 120 người.

---

## Về PX
### Giữ lại (Keep)
- **PX-01** (3 persona), **PX-03** (bảng mâu thuẫn), **PX-04** (thân bất tử khi bế quan, 60s nhập định chống combat-log, báo mộng), **PX-06** (quay lại chơi sau ≤20s), **PX-08** (chết trong FTUE), **PX-09** (server theo bậc, Linh Ảnh), **PX-12** (luật skin và ads không cho sức mạnh), **PX-13**, **PX-14**, **PX-16**.

### Mượn (Steal)
- **PX-06** → Đạo Quả = **25% CT lũy kế của kiếp** (tuyến tính, dễ giải thích; thay công thức 10·C² của tôi). Chết trong kiếp thì +10%, chết vì Oán linh thì +25%.
- **PX-08** → FTUE Linh Thử là *Tiền Thân* với hệ số ×3, đột phá C1 ở phút 6–8. Sau khi chết ở phút 14, Hồi Ức ×3 đưa cây qua C1 trong khoảng 7 phút. Hai cơ chế ăn khớp nhau.
- **PX-11** (vòng màu cảnh giới), **PX-05** (đền bù cho nạn nhân), **PX-16** (đưa vào luật cộng dồn bonus).

### Phản biện (Challenge)
| ID | Mức độ | Vấn đề | Tình huống người chơi | Đề xuất thay thế / cách kiểm chứng |
|---|---|---|---|---|
| PX-04, PX-12 | **Blocker** | Offline 60% × 8h cho **2.336 CT/tuần (×7.3)**, chạm Thiên Kiếp sau 0.7 tuần. Ad "+2h bế quan" nâng lên ×8.9. Cả mùa 48 ngày sụp, và ad trở thành tăng sức mạnh, trái tinh thần G3 (sim H) | Người không chơi gì, chỉ mở app xem ad mỗi ngày, vẫn lên C6 trước người chơi thật 5 tối/tuần | **Offline = 0 CT.** Offline chỉ nạp hồ Tĩnh Tu (×2 cho 30 phút đầu, đầy sau 8h) và tích tài nguyên (Quang Tinh, lá mọc lại, rễ). Báo mộng hiển thị *tăng trưởng nhìn thấy được* thay cho con số tu vi. Ad tối đa: +5 phút hồ, 1 lần/ngày (≈ +8%) |
| PX-10 | Major | "Linh khí dồi dào ×1.5 cho 30 phút đầu/ngày" trùng với Tĩnh Tu ×2. Nếu cộng dồn thì CT/tuần ×1.47 | — | Gộp làm một cơ chế. Giữ tên PX ("Linh khí dồi dào") trên UI, dùng số liệu PROG |
| PX-09 | **Major** | Kỷ nguyên 14/28 ngày không khớp đường cong nào. 28 ngày: 0% Mid chạm Thiên Kiếp. 14 ngày: chỉ 1% Casual xong Rừng Non (sim I) | Người Casual bị wipe mãi ở Trúc Cơ, không bao giờ phi thăng | **Kiếp 48 ngày** cho Nguyên Sinh và Cổ Đại. Rừng Non làm mới bản đồ ở ngày 24 nhưng **không** xóa nhân vật, vì Áp Chế đã chặn power creep ở đó. **Pass 24 ngày** (= 3 năm-rừng), mỗi Kiếp 2 pass |
| PX-05 | Major | (a) Chênh +1 cảnh đã bị +1 Nghiệp, phạt cả chuỗi thức ăn tự nhiên (sói C4 ăn hươu C3). (b) Linh Quang Hộ Thể kéo dài "45 phút hoặc hết C1", nhưng C1 xong ở phút khoảng 22, ngay trong FTUE solo. Kết quả là vào rừng chung với **0 phút** bảo vệ | Người mới xong FTUE, bước vào rừng chung và bị ăn ngay phút đầu | (a) Chênh 1 cảnh: thưởng 50%, Nghiệp 0. (b) Chỉ tính **thời gian ở rừng chung**: 3h hoặc tới hết C2, giảm 60% sát thương nhận từ người cao hơn ≥2 cảnh |
| PX-14 | Major | MVP gồm "C1–5" + "Rừng Non 1 map". Theo cấu trúc 3/3/3, Rừng Non chỉ có C1–3, tức **1 tuần** tiến trình dọc cho Mid. Khó gọi là "nhiều tuần" | Người Mid hết nội dung dọc ngay tuần đầu | Bản đồ MVP = Rừng Non + vòng lõi "Linh Lâm" cho C4–C6 (không bị Áp Chế). Cao trào là **Đại Kiếp C6 → Phi Thăng** (Bia + luân hồi nhận nhiều Đạo Quả), khoảng 3.3 tuần Mid. Chi phí: +1 vòng map, tái dùng biome |
| PX-12 | Minor | "Linh Khí" vừa là tiền trong kiếp vừa có sink "đột phá", trùng chức năng với tu vi. "Đạo Tâm" (tiền meta) trùng tên với la bàn Đạo Tâm của WORLD-13 | Người chơi thấy hai chữ "Đạo Tâm" mang hai nghĩa | Ví tiền gồm: Linh Khí (tiêu cho kỹ năng, khiên, luyện hóa), **Đạo Quả** (meta), Hoa Lộ, Ngọc Tinh. Tu vi là *thanh tiến độ*, không phải ví. Tên "Đạo Tâm" để dành cho la bàn |
| PX-10 | Minor | PX ước tính 25–35h tới phi thăng. Cửu Cảnh cho 17.4h với Mid, Core đạt 2.9 tuần | — | Tôi giữ mức 17h vì là điều kiện để 63% Mid về đích trong 48 ngày. Nếu PX muốn 25h thì Kiếp phải kéo dài khoảng 70 ngày |

### Câu hỏi cho PX
1. Chấp nhận offline 0 CT nếu báo mộng cho thấy cây/hang *lớn lên thật* (rễ, lá, kho) không?
2. Pass 24 ngày có ổn với mô hình doanh thu không?
3. MVP có thể thêm vòng "Linh Lâm" C4–C6 không? Chi phí ước lượng là M.

---

## Xung đột liên domain phát hiện được
| Xung đột | Các ID liên quan | Lập trường của tôi | Gợi ý giải quyết |
|---|---|---|---|
| Số cảnh giới | PROG-01, WORLD-12/A3, SURV A4 | **Đổi sang 9** (Cửu Cảnh). WORLD đúng về cấu trúc, PX đúng về nhịp | Bảng F: 1.671 CT, ×1.08/tầng |
| Độ dài mùa / reset | WORLD-08, PX-09, PROG-13 | Kiếp **48 ngày, lịch cố định**. Rừng Non làm mới ở ngày 24, không xóa nhân vật. Thần Vị mở từ ngày 14, mỗi Thần 14 ngày rồi Phi Thăng | Sim I: Mid 63% chạm Thiên Kiếp, thêm Bù Đắp +50% thì 69% |
| Hệ số sức mạnh giữa cảnh | PX-05, PROG-11/12 | ×1.26 chỉ số, ×1.59 combat power mỗi cảnh. 1v1 vượt 1 cảnh thắng 21%, 2 người hạ được người cao hơn 2 cảnh 84%, 3 người hạ người cao hơn 3 cảnh 96% | Chốt theo bảng G |
| Chống bắt nạt (4 phiên bản) | PROG-12, SURV-11, WORLD-16, PX-05 | **Thiên Đạo Luật hợp nhất** (bảng dưới) | — |
| Tiến trình offline | PX-04/10, SURV-12, PROG-04 | 0 CT offline, chỉ một hồ Tĩnh Tu | Sim H |
| Chết: Hậu Duệ / đổi loài / Nguyên Thần | SURV-15, PROG-09/10, PX-06 | Hậu Duệ rơi 1 cảnh. Đổi loài dùng ×3/×1.5 kèm Túc Tuệ. Nguyên Thần Bất Diệt từ C6 | Sim J; tỉ lệ đổi loài cần ≥35% |
| Đơn vị năng lượng / Sinh Năng | SURV-09, WORLD-03, PX-12 | CT là đơn vị gốc. Sinh Năng = 20 CT. Xác trả về quỹ vùng bằng *linh khí*, không bằng CT | Sim M |
| Cộng dồn bonus | PROG-04/10, PX-10/12/16, SURV-15, WORLD-10 | Nhân dồn xấu nhất ×82. Tất cả gộp **cộng** vào "Thiên Đạo Gia Trì", **trần ×3** (×4 trong 30 phút đầu sau luân hồi) | Sim K |
| Độ dài sự kiện | WORLD-10, SURV-17, PX-15 | Sự kiện lớn kéo dài theo ngày thực, có đỉnh vào giờ vàng. Hiện có 3 phiên bản "Linh Triều" khác nhau cần gộp làm một | Sim L |
| Phạt kiếp theo Nghiệp | PROG-07 (+10%), SURV-11 (+15%), PX-05 (+1 đợt sét) | +10% mỗi Nghiệp, trần +50% | — |
| Kiếp thất bại | SURV-16 (chờ 24h), PROG-07 (20 phút) | Debuff 20 phút, −30% CT tầng | — |

**Thiên Đạo Luật hợp nhất (đề xuất PROG-12b).** Chênh lệch tính bằng cảnh giới, *sau* khi đã áp Áp Chế.

| Chênh (kẻ giết − nạn nhân) | Tu vi kẻ giết nhận | No/thức ăn | Nghiệp | Nạn nhân nhận |
|---|---|---|---|---|
| ≤0 | 8 CT × (1 + 0.5·\|g\|) "Nghịch Thiên" | 100% | 0 | — |
| 1 | 50% | 100% | 0 | +10% Đạo Quả |
| ≥2 | **0%** | 100% (sinh tồn vẫn thật) | +1 (+2 nếu nạn nhân đang được Ấu Linh) | +25% Đạo Quả, tối đa 1 lần/ngày |

Các bậc Nghiệp: **≥1** hào quang đỏ thấy được trong 20 ô (SURV), mỗi điểm +10% sát thương kiếp. **≥3** Huyết Sát: hiện trên bản đồ, ai hạ được nhận thưởng ×3 (PROG/PX). **≥5** Thiên Phạt: sét truy đuổi trong 1 ngày-rừng (WORLD). Nghiệp giảm 1 điểm sau mỗi 2 giờ *online*. Đánh trả người tấn công trước không sinh Nghiệp (WORLD). Ấu Linh: ẩn khỏi Thần Thức của người cao hơn (SURV) và giảm 60% sát thương nhận (PX), áp dụng trong 3h đầu ở rừng chung hoặc tới hết C2. Áp Chế: trần C3 Hậu trong Rừng Non. **Bỏ** cơ chế trừ HP vì linh khí loãng (PX), vì nó trùng với Áp Chế và chặn người mạnh quay về dẫn bạn mới.

## Top 3 điều team phải chốt
1. **Khung thời gian**: Cửu Cảnh (1.671 CT, Mid 5.2 tuần nếu không chết), Kiếp 48 ngày theo lịch cố định, offline 0 CT. Mọi con số khác (decay, sự kiện, pass, chi phí chết) đều phụ thuộc ba con số này.
2. **Một đơn vị năng lượng chung**: CT là gốc, Sinh Năng = 20 CT, mọi bonus cộng dồn theo kiểu cộng với trần ×3, tách tên Đạo Tâm (la bàn) và Đạo Quả (tiền meta).
3. **Thiên Đạo Luật hợp nhất và giá của cái chết**: bảng trên, cộng Hậu Duệ rơi 1 cảnh so với đổi loài ×3/×1.5, sao cho luân hồi đổi loài vẫn là lựa chọn hấp dẫn (≥35%).
