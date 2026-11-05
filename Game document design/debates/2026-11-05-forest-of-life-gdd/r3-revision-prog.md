# R3 Revision — PROG

> Domain: cảnh giới, tiến hóa, nguồn tu vi, kỹ năng, độ kiếp, hóa hình, luân hồi/meta, công thức sức mạnh, unlock pacing, và kiểm chứng số liệu của team.
> Mô phỏng mới: `sim/prog_r3_sim.py` → `sim/prog_r3_sim_output.md`, gồm mục N–U. Mọi con số ghi "(sim X)" lấy từ file đó. Đơn vị: **1 CT = tu vi của 1 phút chơi tích cực**. Người chơi Mid chơi 5 phiên × 40 phút mỗi tuần, được 64 CT/phiên, 320 CT/tuần.
> Nhãn phạm vi: **[MVP-A]** (tháng 0–11, web solo + co-op, PvP với AI/Linh Ảnh) · **[MVP-B]** (soft launch, rừng chung với người thật) · **[1.0]** · **[Post]** (post-launch) · **[Cắt]**.

## 0. Các quyết định đã chốt (đọc trước)
| # | Quyết định | Con số chốt | Bằng chứng |
|---|---|---|---|
| 1 | Số cảnh giới | **7 (Thất Cảnh v2)**: 6 cảnh cày × 3 tầng, cộng C7 Thành Thần. Ánh xạ **3/2/2**: Rừng Non C1–3 · Nguyên Sinh C4–5 · Cổ Đại C6–7. **Bỏ Cửu Cảnh** | sim N |
| 2 | Tổng tu vi tới Thiên Kiếp | **1.661 CT**, tức 17,3 giờ chơi với Mid (5,2 tuần nếu không chết) | sim N |
| 3 | Độ dài Kiếp (reset nhân vật) | **56 ngày** ở bản đầy đủ = 2 Kỷ Nguyên × 28 ngày. **MVP-B: 28 ngày** | sim Q |
| 4 | Độ bền cây | HP 3 lớp, Tốc 0 đổi thành ×3 HP Thân. Một sói cùng cấp cần **43–54 s** để làm cây Đổ, và nếu có luật rút lui thì **không bao giờ** làm Đổ được. Ba sói cần 17 s | sim O |
| 5 | Chi phí chết | **Hậu Duệ** tại neo ≤1,3 phiên ở mọi cảnh. **Luân Hồi** ×4/×2: C5 mất 0,82 tuần | sim P |
| 6 | Hệ số sức mạnh | ×1,10/tầng, tức ×1,33 chỉ số và **×1,77 combat power** mỗi cảnh. **Tốc không tăng theo cảnh** | sim R |
| 7 | Offline | **0 CT.** Chỉ có Mộng Tích (rested): ×2 trong 30 phút đầu, đầy sau 8 giờ | R2 sim H |
| 8 | Cộng dồn bonus | Cộng các bonus lại thành "Thiên Đạo Gia Trì", trần **×3** (×4 khi đang Hồi Ức) | sim T |
| 9 | Phạm vi MVP | **3 loài** (Linh Mộc, Linh Thử, Lang) · **6 Huyết Mạch** · **24 kỹ năng chủ động** (18 ở MVP-A, cộng 6 Thần Thông ở MVP-B) dựng từ 12 template · 42 node bị động có script | §3 |

---

## Phản hồi phản biện
| Phản biện (từ ai, ID) | Quyết định | Lý do | Thay đổi cụ thể |
|---|---|---|---|
| SURV · PROG-11 **Blocker**: TTK 4–6 s giết cây | **Accept** | Đúng. Theo ví dụ R1 của chính tôi, cây chết trong 4 đòn. Cây không chạy được nên TTK phải dài hơn thú | PROG-11b: dùng HP 3 lớp của SURV-03. Thân = 3 × HP tham chiếu, Tán = 0,5 Thân, Tâm Rễ = 0,5 Thân và chỉ bị Căn Thương chạm tới. Sim O: 1 sói cần 43–54 s, 3 sói 17 s |
| PX · PROG-10 **Blocker**: chết ở C5 mất ~1,3 tuần | **Accept** | Không giữ được người chơi F2P mobile với mức phạt đó | PROG-10c: thêm tầng chết thứ nhất là Hậu Duệ (≤130 CT). Luân Hồi tăng catch-up lên ×4/×2. Sim P: Hậu Duệ ≤1,3 phiên, Luân Hồi ở C5 4,1 phiên (0,82 tuần) |
| SURV · PROG-10 Major: chỉ có một đường chết | Accept | Như trên | Như trên |
| SURV · PROG-10/12 Major: xác (36 CT) đáng giá hơn kill (8 CT) | Accept | Lỗi đơn vị của tôi ở R1 | Bỏ "xác = 20% CT tầng". Dùng một pool Sinh Năng = 20 CT × m(g), chia 8 / 4 / 8 (PROG-17) |
| SURV · PROG-03 Minor: cây "chạm mỗi 3 phút" | Partial | Đồng ý có vấn đề. Lấy cách đo của PX vì nó thân thiện với chế độ một tay hơn | Vệt Nắng thành cửa sổ bonus chiếm 20% thu nhập. Tán loạn khi **không có quyết định trong 5 phút**, thay cho "không chạm trong 3 phút" |
| SURV X1: dùng 7 cảnh, ánh xạ 2/2/2 | Partial | Đồng ý 7 cảnh. Chọn ánh xạ 3/2/2 (WORLD + PX) vì Huyết Mạch mở ở C3 phải nằm trong Rừng Non, nơi có Áp Chế n=9. Người mới cần có nhánh trước khi rời vùng an toàn | Upkeep của SURV (L0–L3) vẫn tự do gắn theo cảnh, không phụ thuộc cấp rừng |
| SURV X2 / PX / WORLD: độ dài mùa | Accept (56/28) | Sim Q bên dưới | PROG-16 |
| SURV X4: g dùng cảnh **thật**, +2 Nghiệp | Partial | Accept g thật. Mức +2 Nghiệp chỉ áp khi nạn nhân đang được Hộ Thể. Ngưỡng Thiên Phạt đặt ở 5 Nghiệp (theo WORLD/PX), không phải 6 | PROG-12c |
| SURV X5: Hậu Duệ mất 50% CT tầng | Partial | Chọn "về đầu tầng, trần 130 CT", trung bình bằng 50% CT tầng. Dễ giải thích hơn | PROG-10c |
| SURV Q1–Q3 | Accept | Hậu Duệ giữ Huyết Mạch, Ngộ Đạo và Keystone. Nhân Hình chết khi **Tâm Rễ** = 0. Sim TTK đã chạy (sim O) | — |
| WORLD · PROG-13 Major: lên thần bằng cách giết | **Accept** | Mâu thuẫn ludonarrative thật | PROG-13b: Thần Cách = **Sinh Khí đã trả cho rừng**. Cổ Thú chỉ tính khi Linh Hạch được trả về quỹ |
| WORLD · PROG-02: con sói giữ yêu thân vẫn bị gọi "Lang Nhân" | Accept | Đúng | Tên C5 tách theo Đạo (Nhân ‖ Yêu). MVP chỉ có tên Yêu (Bản Thể) |
| WORLD · PROG-08: Nhân Hình cần NPC người | Accept | Rẻ hơn, câu chuyện mạnh hơn | Nhân Hình [Post] mở trại Nhân Tu bỏ hoang, đọc khắc đá, trà trộn vào sự kiện E5 |
| WORLD Q1: quỹ vùng có phá chuẩn 1,0 CT/phút không | Accept ±15% | Ngoài Khô Linh, CT dao động ×0,85–1,0. Sim U: 4 thú săn làm vùng Khô Linh sau 2,8 ngày-rừng. Tổ hợp 2 thú + 1 cây + 1 nấm giữ quỹ ở 91% | PROG-17 |
| WORLD Q2: 5 Thần Vị cho server nhỏ | Partial | Thần Vị chỉ có ở Cổ Đại [Post] và chế độ solo | Số ghế = clamp(⌊dân/15⌋, 3, 5) |
| WORLD: Hậu Duệ rơi về đầu đại cảnh giới | **Reject** | Ở C5 mức này mất tới 380 CT, tức 5,9 phiên, vượt trần 2 phiên của PX (sim P) | Dùng "về đầu tầng, trần 130" |
| WORLD: lịch lồng nhau 14/28/56 | Partial | Giữ 28/56. Con số 14 dùng làm **nhịp mở phòng Rừng Non mới** (mỗi phòng sống 28 ngày, cứ 14 ngày mở thêm một phòng), không làm reset riêng | PROG-16 |
| WORLD: glossary (Đạo Tâm = tiền meta, Tâm Hướng = la bàn, Mộng Tích, Phi Thăng/Quy Căn) | Accept | Tôi rút lại tên "Đạo Quả" đã đề xuất ở R2 | Áp dụng trong toàn bộ file |
| WORLD audit: kill PvP 8 CT > săn AI | Accept | — | Kill PvP trong vùng Khô Linh ×0,5 |
| PX · PROG-06 Major: 7 lớp hệ thống, 33 skill | **Accept, cắt sâu hơn đề xuất** | Đúng điểm mù "thêm tầng" của tôi | MVP còn 2 Huyết Mạch/loài và 24 skill. **Bỏ đồ thị skill tree**, thay bằng **Ngộ Đạo dạng draft** (chọn 1 trong 3 mỗi lần đột phá). Đạo Ngộ không còn là khóa riêng mà thành trọng số của draft. Đạo Đồ chung để [1.0] |
| PX · PROG-06 loadout | Accept | — | 3 chủ động + 1 Thần Thông trên mọi nền tảng |
| PX · PROG-04 vs FTUE | Accept | — | Kiếp FTUE (Linh Thử) dùng đường cong kịch bản riêng: C2 ở phút 7. Cây xong C1 ở phút 29 (sim N) |
| PX · cộng dồn ×11 | Accept | — | Gia Trì cộng dồn, trần ×3/×4. Exploit "tự sát lấy bonus" lỗ 26 CT (sim T) |
| PX · PROG-07/13: Ẩn/Công Kiếp, Thiên Kiếp thất bại = chết | Partial | Trung Kiếp và Đại Kiếp được chọn Ẩn hoặc Công. Thiên Kiếp **luôn công khai** (xem phần lập trường). Thất bại do sét chỉ mất 50% tầng Hậu (1,5 phiên). Chỉ chết thật nếu bị người chơi khác giết | PROG-07b |
| PX · PROG-08 scope | Accept | — | MVP-B chỉ có Bản Thể. Nhân Hình [Post] |
| PX · ads +5 phút rested | Accept, mở rộng thêm | — | Rừng chung: ad cho 0 CT. **Bỏ luôn node "+% CT" khỏi Đạo Tâm Bàn**, vì ad +30% Đạo Tâm sẽ thành đường vòng để tăng sức mạnh |
| PX Q1: Sát Nghiệp tính sau Áp Chế là lỗ hổng | **Accept** | Đúng, bảng R2 của tôi sai chỗ này | Nghiệp tính theo cảnh **thật**. Chỉ số chiến đấu vẫn tính sau Áp Chế |
| PX Q2: catch-up sau reset mùa | Partial | ×2 nhưng chỉ tới **hết C3**. Cựu binh vì vậy rời Rừng Non nhanh gấp đôi, tức ít "ma cũ" hơn trong vùng của người mới, mà khoảng cách từ C4 trở đi không bị nới rộng | PROG-10c |
| PX Q3: party 4 người nhận 115% mỗi người | Accept | Sim S: bầy 4 con với công thức R1 kiếm 2,01 CT/phút mỗi con | Tổng CT nhóm = 1 + 0,6·min(k−1, 2). Bầy 3 con được ×1,17, bầy 4 con chỉ ×0,96 |
| PX: thanh tu vi đầy ngay; Đả Tọa trần 15% | Accept | — | PROG-03b |
| PX: Mùa Đông của cây | Accept | — | Có `k_s` theo mùa: Quang hợp ×0,5, Linh Thức ×2, tổng vẫn 1,0 ±10% |
| **Tự sửa (từ R2 của tôi):** Cửu Cảnh | Rút lại | Xem PROG-01c | — |
| **Tự sửa:** Blocker SURV-15 "Hậu Duệ rẻ thì USP luân hồi chết" | Rút một phần | Đại Kiếp ép **mọi người** luân hồi ít nhất 1 lần mỗi Kiếp, nên USP không phụ thuộc lựa chọn lúc chết giữa mùa. Sim Q2: dù 95% người chọn Hậu Duệ, tỉ lệ Mid chạm Thiên Kiếp chỉ đổi từ 78% lên 82%. Lựa chọn giữa hai đường là **ngang**, không phải chọn mạnh hay yếu | KPI ≥30% lần chết giữa mùa chọn Luân Hồi chỉ dùng để tinh chỉnh, không phải điều kiện sống còn |
| **Tự sửa:** Kiếp 48 ngày | Đổi sang 56 | Sim Q | PROG-16 |

---

## Đề xuất đã sửa

### PROG-01c: Thất Cảnh v2, và vì sao tôi bỏ Cửu Cảnh [MVP-A]
**Giải thích.** Ở R2 tôi chuyển sang 9 cảnh vì hai lý do: (a) WORLD dùng ánh xạ 3/3/3, (b) nhịp 2,5–4,4 phiên mỗi cảnh. Lý do (a) không còn, vì chính WORLD đã chuyển sang 7 cảnh với ánh xạ 3/2/2. Lý do (b) là vấn đề **đường cong**, không phải số cảnh: tôi điều chỉnh lại CT để 7 cảnh cho đúng tổng thời gian như Cửu Cảnh (1.661 so với 1.671 CT). Còn lại hai lập luận chống 9 cảnh mà tôi không bác được:
1. **SURV:** mỗi đại cảnh phải mở một khả năng mới về chất. C7 Phản Hư và C8 Hợp Đạo của tôi ở R2 chỉ là "Linh giới" và "Lĩnh Vực", tức nội dung mới phải làm thêm và chưa được thiết kế.
2. **PX:** 9 cảnh tốn thêm 29% chi phí cho mọi thứ nhân theo cảnh (tên × loài, kiếp, Thần Thông, bản địa hóa).

Cái giá của 7 cảnh là các cảnh muộn dài hơn: C6 mất 8,1 phiên, so với tối đa 4,4 phiên ở Cửu Cảnh. Tôi bù lại như sau. Tầng dài nhất là 192 CT, tức 3,0 phiên. Mỗi tầng ở C4–C6 đều có một thứ mới (xem bảng unlock). Ngộ Đạo xuất hiện ở mỗi tầng Hậu kỳ và mỗi lần độ kiếp.

| C | Khung chung | Vùng | Kiếp khi rời cảnh | Lời hứa mở khóa |
|---|---|---|---|---|
| 1 | Khai Linh | Rừng Non · Bìa | Tiểu Kiếp | 2 kỹ năng Bản Năng, ăn hoặc quang hợp |
| 2 | Tụ Linh | Rừng Non · Bìa → Trung Lâm | Tiểu Kiếp | Co-op, Linh Thức lite (cây), Huyết Mạch Ấn hiện trên UI |
| 3 | Trúc Cơ | Rừng Non · Trung Lâm (Áp Chế n=9) | **Trung Kiếp = Phi Thăng sang Nguyên Sinh** | **Chọn Huyết Mạch** (đổi sprite), kỹ năng A1 |
| 4 | Kết Đan | Nguyên Sinh (MVP: vòng lõi Linh Lâm; Áp Chế n=15) | Trung Kiếp | Keystone 1, kỹ năng A2 ([1.0]: chọn 1 Đạo) |
| 5 | Hóa Hình | Nguyên Sinh trong | **Đại Kiếp = Phi Thăng sang Cổ Đại** (ở MVP: khắc Bia rồi Luân Hồi) | Bản Thể (MVP) hoặc Nhân Hình ([Post]), Thần Thông |
| 6 | Xuất Khiếu | Cổ Đại (không Áp Chế) | **Thiên Kiếp** (cần Thần Cách) | Xuất Khiếu, Nguyên Thần Bất Diệt, Keystone 2 [Post] |
| 7 | Thành Thần | Lõi Cổ Đại / Thần Vực | — | Tán Thần / Thần Vị [Post] |

### PROG-02b: Tên cảnh giới theo loài (bảng hợp nhất cuối cùng) [MVP-A: 3 cột đầu]
Tên chỉ là lớp vỏ của `n`. UI hiển thị theo dạng "Lang Đan · Trung kỳ (C4)", kèm vòng màu cảnh giới (PX-11). Bộ tên Mộc/Thử/Lang/Khuẩn lấy của WORLD. Ở C5, tên nằm bên trái ‖ là Nhân Hình, bên phải là Bản Thể (yêu thân). MVP chỉ hiện tên Bản Thể.

| C | Khung | **Linh Mộc** | **Linh Thử** | **Lang** | Khuẩn [1.0] | Linh Thảo [1.0] | Lộc [Post] | Phong [Post] |
|---|---|---|---|---|---|---|---|---|
| 1 | Khai Linh | Manh Nha | Khai Trí | Ấu Lang | Bào Tử | Hạt Thức | Ấu Lộc | Ấu Trùng |
| 2 | Tụ Linh | Trát Căn | Linh Thử | Lang Nha | Khuẩn Ty | Diệp Tụ Linh | Lộc Nhung | Kết Kén |
| 3 | Trúc Cơ | Thành Tán | Ẩn Huyệt | Lang Cốt | Khuẩn Võng | Thảo Căn | Linh Giác | Phá Kén |
| 4 | Kết Đan | Niên Luân Kết Tâm | Thử Đan | Lang Đan | Ngưng Tán | Hoa Đan | Giác Đan | Phong Đan |
| 5 | Hóa Hình | Thụ Nhân ‖ **Cổ Mộc Yêu** | Thử Nhân ‖ **Yêu Thử** | Lang Nhân ‖ **Yêu Lang** | Khuẩn Nhân ‖ Khuẩn Yêu | Thảo Tiên ‖ Thảo Yêu | Lộc Nhân ‖ Yêu Lộc | Trùng Nhân ‖ Yêu Phong |
| 6 | Xuất Khiếu | Mộc Hồn | Thử Hồn | Nguyệt Lang Hồn | Địa Mạch Hồn | Vạn Diệp Hồn | Bạch Lộc Hồn | Phong Hồn |
| 7 | Thành Thần | Thần Mộc | Thử Thần | Thiên Lang | Luân Hồi Mẫu | Thảo Mẫu | Thần Lộc | Vạn Phong Mẫu |

### PROG-03b: Nguồn tu vi theo từng giới (chuẩn hóa về 1,0 CT/phút ±10%) [MVP-A: 3 loài đầu]
| Loài | Nguồn chính | Nguồn phụ | Nguồn đặc thù | Phương sai (bản sắc) |
|---|---|---|---|---|
| **Linh Mộc** | Quang hợp nền **45%**: 0,45 CT/phút × ánh sáng, chạy khi online và có quyết định trong mỗi 5 phút | **Vệt Nắng 20%**: cửa sổ 15 s, cứ 45–60 s có một lần, ×3. Bỏ lỡ hết thì mất ≤20%. **Cắm rễ/hấp thu 20%**: Linh Mạch, phần "đất" của Sinh Năng | Phản vệ thành công 2 CT (mỗi kẻ tấn công 1 lần/30 phút), Quả Ước bị ăn, cộng sinh: 15% | Thấp (~16%) |
| **Linh Thử** | **Ăn hạt/quả 45%** (Quả Ước, cả hai bên cùng lợi) | **Trữ/gieo hạt 25%**: mầm do mình gieo sống được 10 phút thì +CT | **Thoát Sinh** 2 CT (thoát kẻ săn cùng cảnh trở lên), đào hang, tìm Linh Tuyền: 30% | Trung bình (~22%) |
| **Lang** | **Săn 60%**: Sinh Năng 8 CT/con mồi cùng cảnh. Bầy đông thì tỉ lệ thành công cao hơn, nhưng chia theo PROG-17 | Ăn xác, đánh dấu lãnh thổ 25% | PvP theo Thiên Đạo Luật 15% | Cao (~34%) |
| Khuẩn [1.0] | Phân giải xác **50%** (~3 CT mỗi xác, lấy từ phần "đất"). Director bảo đảm sàn ≥1 xác NPC/5 phút/vùng | Lan tơ 0,30 CT/phút 25% | Khế ước cộng sinh 60/60 25% | Cao |
| Linh Thảo [1.0] | Lan hạt 0,9 CT/lần 50% | Quang hợp 35% | Phản Sinh 15% | Thấp |

**Hệ số áp lên CT** (nhân với nhau, ngoài Gia Trì):

| Hệ số | Giá trị |
|---|---|
| Vùng thấp hơn cảnh của bạn | ×0,5^chênh |
| Vùng cao hơn cảnh của bạn | +25% mỗi bậc chênh, trần +50% |
| Needs (SURV) | Comfort ×1,0 · Warning ×0,85 · Critical ×0,5 · Lethal ×0 |
| Quỹ vùng | ≥60%: ×1,0 · 30–60%: ×0,85–1,0 · Khô Linh: thú ×0,5, cây/nấm ×0,8 |
| Mùa Đông (cây) | `k_s` mùa, giữ 1,0 ±10% |
| Đả Tọa | Linh Khí dư luyện thành CT theo tỉ lệ 1:1, trần 15% CT của phiên |
| AFK | Không có quyết định trong 5 phút: ×0,2 |
| Offline | 0 |

### PROG-04c: Đường cong và lịch thời gian thực [MVP-A tới C4, MVP-B tới C5]
Công thức: `CT_tầng = CT_cảnh × (0,30 / 0,33 / 0,37)`, với CT_cảnh = 36 / 100 / 180 / 280 / 380 / 520. Chi phí Cơ Duyên và kiếp khi rời cảnh: 5 / 15 / 30 / 45 / 70. Con số TV hiển thị để người chơi thấy tăng: `TV = CT × 10 × 1,25^(n−1)`.

| C | CT tầng Sơ/Trung/Hậu | CT cả cảnh | Kiếp (CT) | Lũy kế khi xong cảnh | Phiên Mid trong cảnh | Tuần Casual | **Tuần Mid** | Tuần Core |
|---|---|---|---|---|---|---|---|---|
| 1 Khai Linh | 11/12/13 | 36 | Tiểu (5) | 41 | 0,6 | 0,3 | 0,1 | 0,1 |
| 2 Tụ Linh | 30/33/37 | 100 | Tiểu (15) | 156 | 1,6 | 1,2 | 0,5 | 0,3 |
| 3 Trúc Cơ | 54/59/67 | 180 | Trung · Phi Thăng (30) | 366 | 2,8 | 2,9 | **1,1** | 0,6 |
| 4 Kết Đan | 84/92/104 | 280 | Trung (45) | 691 | 4,4 | 5,4 | 2,2 | 1,2 |
| 5 Hóa Hình | 114/125/141 | 380 | Đại · Phi Thăng (70) | 1.141 | 5,9 | 8,9 | **3,6** | 2,0 |
| 6 Xuất Khiếu | 156/172/192 | 520 | Thiên Kiếp | **1.661** | 8,1 | 13,0 | **5,2** | 2,9 |

(Các con số tuần chưa tính chết và chưa tính Bù Đắp. Có tính chết thì xem PROG-16.)

**Unlock Timeline (Mid)**
| Thời điểm | Mở khóa | Gate |
|---|---|---|
| Phút 0–16 | FTUE Linh Thử (đường cong kịch bản): C2 ở phút 7, chết hoặc hết Thọ Nguyên ở phút 14–16, sau đó Trung Ấm 45 s | Kịch bản |
| Phút 16–29 | Đầu thai (mặc định là hạt giống, tức Linh Mộc), Hồi Ức ×4. Cây xong tầng 1 ở phút 20, tầng 2 ở phút 23, **C1 và Tiểu Kiếp lên C2 ở phút 29** (sim N) | Tu vi |
| Phiên 2 | Bản Năng 2, co-op, Linh Thức lite, Huyết Mạch Ấn, Ngộ Đạo đầu tiên | Tu vi |
| Phiên 3 (0,5 tuần) | **C3: chọn Huyết Mạch** (đổi hình), kỹ năng A1 | Tu vi + hành động |
| Phiên 6 (1,1 tuần) | **Trung Kiếp, Phi Thăng sang Nguyên Sinh/Linh Lâm.** Keystone 1, A2 | Kiếp + Cơ Duyên |
| Phiên 11 (2,2 tuần) | **C5: Bản Thể, Thần Thông** | Kiếp |
| Phiên 18 (3,6 tuần) | **Đại Kiếp, Phi Thăng sang Cổ Đại** (MVP: khắc Bia rồi Luân Hồi) | Kiếp |
| C6 Sơ / Trung / Hậu | Xuất Khiếu + Nguyên Thần Bất Diệt / Keystone 2 / mở lộ trình Thần Cách | [Post] |
| Phiên 26 (5,2 tuần) | Thiên Kiếp | Thần Cách |
| Lần chết đầu (phút 14) | Trung Ấm, Đạo Tâm Bàn, Túc Tuệ | Sự kiện |

Kiểm tra dry spell: mỗi tầng tối đa 3,0 phiên. Ở C4–C5 cứ khoảng 1,5–2 phiên có một Ngộ Đạo hoặc một kiếp. Phần nhịp nội dung (bí cảnh, sự kiện) do WORLD/PX lấp vào khoảng giữa.

### PROG-05b: Huyết Mạch — MVP 2 nhánh mỗi loài, tạo thành một vòng Ngũ Hành khép kín [MVP-A; nhánh thứ 3 ở 1.0]
Điều kiện mở nhánh dựa trên learn-by-doing như R1: nhánh có nhiều Ấn nhất luôn được mở. Sinh/Sát đo **so với hành vi bình thường của loài** (WORLD-13b, chính là Tâm Hướng). Sáu nhánh MVP được gán Ngũ Hành sao cho mỗi nhánh có đúng một nhánh mình khắc và một nhánh khắc mình, theo vòng tương khắc chuẩn Kim → Mộc → Thổ → Thủy → Hỏa → Kim:

| Loài | Nhánh MVP 1 | Nhánh MVP 2 | Nhánh [1.0] |
|---|---|---|---|
| Lang | **Huyết Lang** (Hỏa, nghiêng Sát): chảy máu, hút máu. *Ấn:* 20 đòn gây chảy máu hoặc 5 lần ăn xác tươi | **Phong Lang** (Mộc, nghiêng Hợp): lướt, săn bầy, buff tốc độ. *Ấn:* 5 lần săn thành công cùng đồng minh | Băng Lang (Thủy) |
| Linh Mộc | **Thiết Mộc** (Kim, trung tính/Hộ): gai, giữ Tâm Rễ. *Ấn:* 10 lần phản vệ thành công | **Linh Quả Thụ** (Mộc, nghiêng Sinh): kết quả buff đồng minh. *Ấn:* quả bị ăn 15 lần | Huyết Đằng (Hỏa) |
| Linh Thử | **Tàng Thử** (Thủy, nghiêng Sinh): trữ hạt, gieo Mầm Con làm neo cho cây đồng minh. *Ấn:* gieo 10 hạt | **Độn Thử** (Thổ, nghiêng Sát): đào hầm, **Căn Thương** lên Tâm Rễ, phá neo. *Ấn:* đào 300 ô | Ảnh Thử (ẩn thân) |

Vòng khắc: Huyết Lang khắc Thiết Mộc → Thiết Mộc khắc Phong Lang và Linh Quả Thụ → nhóm Mộc khắc Độn Thử → Độn Thử khắc Tàng Thử → Tàng Thử khắc Huyết Lang. Lửa của sự kiện Đại Hỏa và kỹ năng lửa là **Căn Thương sinh thái**, tách khỏi hệ số Ngũ Hành E (tức "lửa đốt cây" không phải luật tương khắc). Sau 10 giờ chơi ở MVP, người chơi khác nhau theo: 3 loài × 2 nhánh × 2 Keystone = **12 dạng**, × 4 bộ loadout (chọn 3 trong 4 kỹ năng chủ động), cộng thứ tự lấy Ngộ Đạo và Túc Tuệ mang từ kiếp trước.

### PROG-06b: Ngộ Đạo thay cho đồ thị skill tree [MVP-A]
**Cấu trúc mỗi loài, đọc được trong 30 giây:** "Mỗi lần đột phá, chọn 1 trong 3 Ngộ."
- **Kỹ năng chủ động (miễn phí, mở theo cảnh):** Bản Năng 1 (C1), Bản Năng 2 (C2), A1 (C3), A2 (C4), Thần Thông (C5). Loadout là **3 chủ động + 1 Thần Thông**. Từ C4 có 4 kỹ năng chủ động nên người chơi buộc phải bỏ 1.
- **Keystone (chọn cố định, không random):** một cặp loại trừ nhau ở C4, một cặp ở C6 [Post].
- **Ngộ Đạo (draft):** xuất hiện ở mỗi tầng Hậu kỳ của C3–C5 và mỗi lần độ kiếp thành công. MVP có 7 lần chọn, bản đầy đủ có 9. Mỗi lần hiện 3 lựa chọn rút từ pool gồm 4 node Bản Năng + 6 node Huyết Mạch (4 Notable, 2 Minor). Tỉ lệ lấy được ở MVP khoảng 70%. Từ [1.0], Đạo Đồ chung thêm 6 node của Đạo đã chọn vào pool, đưa tỉ lệ xuống khoảng 56%. **Trọng số rút ×2 cho node khớp với hành vi gần đây** (Đạo Ngộ cũ trở thành trọng số), và mỗi cảnh được đổi lựa chọn 1 lần.
- **Respec:** không có trong kiếp. Muốn làm lại build thì Luân Hồi hoặc Hậu Duệ (giữ nguyên Ngộ). Chủ đề "cái chết là cơ hội làm lại" vẫn giữ.
- **Vì sao đổi:** UI rẻ hơn đồ thị cây (khoảng −1 tuần), tiêu được ngân sách ≤5 nút của PX, và bỏ được lớp khóa Đạo Ngộ. Số lớp hệ thống còn lại là: Huyết Mạch, Keystone, Ngộ, Túc Tuệ, Đạo Tâm Bàn.

**Cây tiến hóa ví dụ 1: Lang → Huyết Lang (Hỏa)**
| Loại | Node | Hiệu ứng | Mở |
|---|---|---|---|
| Bản Năng chủ động | Lang Nha | Lao cắn, hệ số 1,5, CD 12 s | C1 |
| Bản Năng chủ động | Hú Gọi | Lộ vị trí con mồi ≤ cảnh mình trong 20 ô trong 4 s, CD 30 s | C2 |
| Bản Năng Ngộ (Notable) | Khứu Huyết | Thấy vệt máu của mục tiêu dưới 50% HP trong 30 ô. *Chuyển được qua Túc Tuệ* | pool |
| Bản Năng Ngộ (Notable) | Ẩn Phong | Đứng yên trong bụi 2 s thì Thần Thức của kẻ khác −30% khi tìm bạn | pool |
| Bản Năng Ngộ (Minor) | Bền Chân / Răng Sắc | +8% thể lực / −10% CD Lang Nha | pool |
| A1 | Huyết Trảo | Hệ số 1,6 + chảy máu 0,25×Công/s trong 4 s, CD 6 s | C3 |
| A2 | Huyết Bộc | Kích nổ mọi lớp chảy máu: 60% sát thương còn lại tính ngay, hồi máu bằng 30% lượng đó | C4 |
| Thần Thông | Huyết Nguyệt Cuồng | 8 s: +30% tốc đánh, hút máu ×2, bị Thần Thức của mọi người nhìn thấy | C5 |
| Keystone C4 | **Huyết Cuồng** ‖ **Thực Cốt** | HP <30% thì +20% sát thương và hút máu ×2, nhưng không nhận hồi máu từ nguồn khác ‖ Ăn xác cho 1 lớp Cốt (+4% Thủ, tối đa 5 lớp), mất 1 lớp mỗi 2 phút | C4 |
| Keystone C6 [Post] | Bất Tử Huyết ‖ Huyết Hải | Khi HP về 0: còn 1 HP trong 2 s, 1 lần/5 phút ‖ Chảy máu lan sang kẻ địch trong 3 ô | C6 |
| Huyết Mạch Ngộ (Notable ×4) | Răng Cưa · Nuốt Vội · Mùi Sợ Hãi · Kẻ Đơn Độc | Chảy máu cộng dồn 3 lớp · Ăn xác nhanh ×2 · Con mồi đang chạy trốn nhận thêm 10% sát thương · +10% sát thương khi trong 15 ô không có đồng minh | pool |
| Huyết Mạch Ngộ (Minor ×2) | Truy Huyết · Thịt Tươi | +6% Tốc khi đuổi mục tiêu đang chảy máu · +8% No từ thịt | pool |

**Cây tiến hóa ví dụ 2: Linh Mộc → Thiết Mộc (Kim)**
| Loại | Node | Hiệu ứng | Mở |
|---|---|---|---|
| Bản Năng chủ động | Vỏ Cứng | −50% sát thương trong 5 s, CD 15 s | C1 |
| Bản Năng chủ động | Vươn Rễ | Kéo thêm 1 ô rễ, tốn Quang Tinh | C2 |
| Bản Năng Ngộ | Rễ Cảm (Notable, *chuyển được*) · Nhựa Đắng (Notable) · Tán Dày / Hút Sâu (Minor) | Báo kẻ đến trong 20 ô qua mạng rễ · Kẻ gặm Tán nhận −30% No · +10% Tán / +10% hấp thu | pool |
| A1 | Vỏ Gai | Gai phản sát thương từ 10% lên 25% trong 8 s, CD 20 s | C3 |
| A2 | Căn Tỏa | Trói 1,5 s mọi kẻ địch trên mạng rễ trong bán kính 8 ô, CD 20 s | C4 |
| Thần Thông | Thiết Lâm Kết Giới | 10 s: đồng minh trong 10 ô −40% sát thương nhận | C5 |
| Keystone C4 | **Bàn Căn** ‖ **Thiết Tán** | Tâm Rễ +50%, Tán mọc lại chậm hơn 50% ‖ Tán chịu đòn như Thân (d +0,3), Quang hợp −15% | C4 |
| Keystone C6 [Post] | Vạn Niên ‖ Thiết Lâm | Mộc Tàn chỉ kéo dài 60 s ‖ Mỗi Mầm Con có 30% gai của bạn | C6 |
| Huyết Mạch Ngộ | Vòng Niên Luân · Hộ Pháp Thụ · Gai Độc · Thân Sắt (Notable) · Mầm Sắt · Lá Kim (Minor) | Mỗi lần Đổ trong kiếp +5% Thân (tối đa 3 lần) · Đồng minh độ kiếp trên mạng rễ được +15% HP kiếp · Gai làm chậm 20% · Thủ +0,15 khi Tán = 0 · … | pool |

### PROG-07b: Độ Kiếp [Tiểu + Trung: MVP-A · Đại: MVP-B · Thiên: Post]
| Đột phá | Kiếp | Thời lượng | Chế độ | Nội dung | Thất bại |
|---|---|---|---|---|---|
| C1→C2, C2→C3 | Tiểu Kiếp | 60–90 s | Riêng | Né lôi có báo trước | −10% CT tầng, thử lại ngay |
| C3→C4 | Trung Kiếp, **Phi Thăng sang Nguyên Sinh** | 2 phút | **Ẩn** (+20% khó, không ai thấy) hoặc **Công** (hiện trong vùng, có Hộ Pháp, cho cosmetic Pháp Tướng) | Lôi + Tâm Ma (bản sao 3 kỹ năng của chính bạn; Tâm Hướng chỉ đổi *mẫu* Tâm Ma, ngân sách độ khó cố định) | −30% CT tầng, debuff Đạo Cơ Tổn 20 phút (−10% chỉ số) |
| C4→C5 | Trung Kiếp | 3 phút | Ẩn / Công | Dùng lại template trên, chỉ đổi tham số (tiết kiệm khoảng 1 tuần sản xuất) | Như trên |
| C5→C6 | Đại Kiếp, **Phi Thăng sang Cổ Đại** | 4 phút | Ẩn (chỉ báo trong vùng, +20% khó) hoặc Công (báo cả server) | 3 pha, đổi thời tiết vùng. **MVP:** thành công = khắc tên lên Thần Mộc Bia, sau đó Luân Hồi với Đạo Tâm ×1,5 | −30% CT tầng + Đạo Cơ Tổn |
| C6→C7 | **Thiên Kiếp** | 10 phút | **Luôn Công** (world event) | Cần Thần Cách. Ai cũng có thể giúp hoặc phá | Thua vì sét: −50% CT tầng Hậu (1,5 phiên), Kiếp Thương 1 phiên online. **Bị người chơi giết: chết thật**, Luân Hồi với Đạo Tâm ×2 |

Công thức độ khó: sát thương kiếp = gốc × (1 + 0,10 × Sát Nghiệp, trần +50%) × (1 − 0,15 × số lần thất bại liên tiếp, sàn 0,55). Mục tiêu: 60–70% thành công ở lần đầu, ≥95% sau 3 lần. Kẻ độ kiếp bị kẹt trong vòng và chỉ gây 50% sát thương ra ngoài. Mọi trạng thái ẩn bị phá khi bước vào vòng kiếp. **Không có thời gian chờ 24 giờ.**

### PROG-08b: Hóa Hình [Bản Thể: MVP-B · Nhân Hình: Post]
- **Bản Thể Đạo** (chi phí S): sprite to hơn 30%, +10% chỉ số, 1 Keystone độc quyền, tên Yêu (Cổ Mộc Yêu, Yêu Thử, Yêu Lang).
- **Nhân Hình Đạo** [Post]: dùng một rig humanoid chung. Ở dạng người: −15% chỉ số chiến đấu, đổi lại có 2 ô Pháp Bảo, đọc được khắc đá, vào trại Nhân Tu bỏ hoang, trà trộn vào sự kiện E5 (WORLD). Với thực vật: dạng người rời khỏi Bản Thể trong bán kính sợi mệnh 30 ô (SURV-07). Bạn chết khi **Tâm Rễ** về 0.

### PROG-09b: Linh Thức và Xuất Khiếu
- **Linh Thức lite** [MVP-A, chi phí S]: thực vật có từ C2. Camera tách khỏi thân và do thám 30 s, CD 3 phút. Đây là fantasy cây cốt lõi theo brief. Chi phí được bù bằng việc dùng lại template Trung Kiếp cho kiếp C4→C5.
- **Xuất Khiếu** (C6) và **Nguyên Thần Bất Diệt** [Post]: giữ như R1. Khi thân chết, Nguyên Thần thoát ra. Về tới Linh Huyệt trong 60 s thì được tính như **Hậu Duệ không cần neo**.

### PROG-10c: Cái chết, Luân Hồi và meta [MVP-A; Hồi Ức Kỷ ở MVP-B]
| Đường | Khi nào | Mất | Giữ | Đạo Tâm |
|---|---|---|---|---|
| **Cây Đổ** (không phải chết) | Thân = 0 | Tán, 25% CT tầng hiện tại. Mộc Tàn 120 s: không quang hợp, Tâm Rễ nhận Căn Thương ×2 | Mọi thứ khác | 0 |
| **Đầu Thai Hậu Duệ** | Neo còn sống (Mầm Con, Huyết Noãn, Ký Hồn Mộc…), chưa dùng trong 24 giờ thực | CT tiến độ trong tầng (về đầu tầng, **trần 130 CT**), kho cá nhân | Cảnh giới, Huyết Mạch, Ngộ, Keystone, lãnh thổ | 0 (không qua Trung Ấm) |
| **Luân Hồi** | Tự chọn, hoặc bắt buộc khi không có neo, chết lần 2 trong 24 giờ, hay bị giết trong Thiên Kiếp | Cảnh giới, Huyết Mạch, Ngộ, vật phẩm (rơi tại xác), lãnh thổ (thành dinh dưỡng) | Đạo Tâm, **Túc Tuệ** (1 Notable "chuyển được"), Codex, Tiền Kiếp Ấn. **Hồi Ức ×4** tới hết cảnh (đỉnh − 1), ×2 tới đỉnh | **25% × CT lũy kế của kiếp** × (1 + 0,5 nếu Oán Linh, +1,0 nếu chết trong Thiên Kiếp) |
| **Đại Kiếp** (cuối Kiếp server) | Mọi người | Như Luân Hồi | Như Luân Hồi. **Hồi Ức Kỷ ×2 tới hết C3** nếu đỉnh cũ ≥ C4 | 25% × CT lũy kế × (1,0 / **1,5** nếu đã Phi Thăng Cổ Đại / **2,0** nếu Thành Thần), cộng 500 cho Thần Vị Quy Căn |

**Chi phí chết, tính bằng phiên Mid (sim P, chết ở giữa tầng Trung):**
| Chết tại | Đã đầu tư | Hậu Duệ | Luân Hồi R1 (×3/×1,5) | **Luân Hồi R3 (×4/×2)** | Đạo Tâm nhận |
|---|---|---|---|---|---|
| C2 | 0,9 h | 0,3 | 0,7 | 0,5 | 22 |
| C3 | 2,5 h | 0,5 | 1,7 | 1,3 | 60 |
| C4 | 5,2 h | 0,7 | 3,3 | 2,4 | 124 |
| C5 | 9,0 h | 1,0 | 5,4 | **4,1 (0,82 tuần)** | 217 |
| C6 | 14,4 h | 1,3 | 8,5 | 6,3 (1,27 tuần)* | 346 |

\*Ở C6, Luân Hồi chỉ xảy ra khi vừa mất neo vừa bị bắt Nguyên Thần (khoảng 12,5% số lần chết). Chi phí kỳ vọng ở C6 vì vậy khoảng 1,9 phiên. Trần của PX (Hậu Duệ ≤2 phiên, Luân Hồi ≤1 tuần) đạt ở C2–C5. C6 vượt trần nhưng có ngoại lệ đã nêu ở chú thích.

**Đạo Tâm Bàn MVP (8 node, 100% ngang, không node nào có chỉ số chiến đấu hay % CT):**
| Node | Hiệu ứng | Giá |
|---|---|---|
| Tiền Kiếp Ấn I | Khung prestige | 60 |
| Huyết Mạch Thiên Kiến | Thấy điều kiện Ấn từ C1 | 80 |
| Mộ Linh Đầu Thai | Đầu thai tại Mộ Linh cũ của mình (+0,2 Gia Trì trong 30 phút, +Duyên) | 120 |
| Loadout Preset II | Lưu 2 bộ 3+1 | 120 |
| Vùng Sinh | Chọn ô xuất phát trong Bìa Rừng | 150 |
| Codex Ký Ức | Codex nhớ vị trí Cơ Duyên đã gặp | 250 |
| Túc Tuệ ô 2 | Mang 2 Notable sang kiếp sau | 400 |
| Hào Quang Kiếp | Cosmetic khi độ kiếp | 500 |

Ước tính: Mid được khoảng 1.000 Đạo Tâm mỗi Kiếp đầy đủ, mở được 5–6 trong 8 node ngay Kiếp đầu. Casual được 250–380. Mở loài: ở MVP mở cả 3 loài sau FTUE. Từ loài thứ 4 trở đi, giá = 300 × (1 − 0,2 × Duyên, sàn 0,4) (WORLD-11).

### PROG-11b: Formula Sheet [MVP-A]
- **Chỉ số theo tầng `n` (1..18):** `HP, Thân, Tán, Tâm Rễ, Công, Linh Lực = base × 1,10^(n−1)`. `Thủ = d × K(n)`, với `K(n) = 100 × 1,10^(n−1)`.
- **DR** = `Thủ / (Thủ + K(n_tấn_công))`, trần 75%. Cùng tầng thì DR = d/(1+d).
- **Tốc** chỉ phụ thuộc loài, nhánh thay đổi tối đa ±15%, **không tăng theo cảnh**. **Thần Thức** = base × (1 + 0,05 × (C−1)).
- **Sát thương** `Dmg = Công × hệ số kỹ năng × (1 − DR) × E × Crit × Mit`. E: khắc ×1,25, bị khắc ×0,80, trung tính ×1. Crit: 5% cơ bản, trần 40%, ×1,5. Mit là kỹ năng phòng thủ (Vỏ Cứng ×0,5…).
- **Áp Chế:** khi ở trong vùng, `n_hiệu_lực = min(n, trần vùng)`. Rừng Non 9, Nguyên Sinh 15, Cổ Đại không trần. Áp Chế chỉ dùng cho **chỉ số**. Nghiệp và thưởng tính theo cảnh thật.

| Base tại n=1 | HP / Thân | Tán | Tâm Rễ | Công | d | Tốc (ô/s) | Thần Thức (ô) |
|---|---|---|---|---|---|---|---|
| Lang | 420 | — | — | 50 | 0,40 | 6,0 | 14 |
| Linh Thử | 300 | — | — | 26 | 0,30 | 6,6 (+ hang) | 16 |
| Linh Mộc | **Thân 1.260** (= 3 × 420; Tốc 0 đổi thành ×3) | 0,5 × Thân, đỡ đòn trước | 0,5 × Thân, **chỉ Căn Thương** chạm được | 30 (rễ quất 0,5×/s, gai 10%) | 0,80 | 0 | 10 (+ Rễ Cảm) |

**Căn Thương** (đòn duy nhất trừ Tâm Rễ), tính theo %/s Tâm Rễ tối đa và ×2 khi cây đang Mộc Tàn: Độn Thử đào 1% · lửa (Đại Hỏa, kỹ năng lửa) 2% · Mục Khuẩn [1.0] 1,5% · rễ đối thủ 0,5% · sét kiếp. Tâm Rễ = 0 là chết thật.

**TTK (sim O, n=10 = C4 Sơ):**
| Tình huống | Kết quả |
|---|---|
| Lang vs Lang cùng tầng | **7,5 s**, mất 26% HP trong 2 s mở màn (R1: 4–6 s) |
| Lang vs Linh Thử cùng tầng | 5,0 s. Thử phòng thủ bằng Tốc ×1,1, hang và Thần Thức |
| 1 Lang vs cây cùng tầng (trung tính / khắc / cây AFK) | 54 / 43 / 35 s nếu sói không rút. **Có luật rút lui (HP <35%) thì P(Đổ) = 0%** |
| 1 Lang cao hơn 1 cảnh vs cây | 36 s, Đổ 100% |
| 2 / 3 Lang cùng tầng vs cây | 27 / **17 s** (săn bầy khả thi) |
| 3 Lang + 1 Độn Thử | Đổ ở 17 s, Tâm Rễ chết thêm **50 s** sau đó (tận diệt cần phối hợp nhiều loài) |
| 2 Lang + Đại Hỏa | Đổ ở 27 s, chết thêm 25 s sau đó |

Mục tiêu "≥40 s" của SURV đạt cho cây có phản ứng. Cây AFK (35 s) là ngoại lệ có chủ đích; cây offline thì được bất tử nhờ Nhập Định.

### PROG-12c: Thiên Đạo Luật hợp nhất (một tên, một bảng) [Áp Chế + Hộ Thể: MVP-A · đầy đủ: MVP-B · Thiên Phạt: 1.0]
`g` = cảnh giới **thật** của kẻ giết − cảnh giới thật của nạn nhân.

| g | Tu vi kẻ giết nhận (từ Sinh Năng 8 CT) | No | Nghiệp | Nạn nhân |
|---|---|---|---|---|
| ≤0 | 8 × (1 + 0,5·\|g\|), danh hiệu "Nghịch Thiên" | 100% | 0 | — |
| 1 | 50% | 100% | **0** (chuỗi thức ăn tự nhiên) | — |
| ≥2 | **0** | 100% (ăn vẫn là ăn) | **+1** (+2 nếu nạn nhân đang được Hộ Thể) | **Oán Linh**: Đạo Tâm của lần chết đó +50%, 1 lần/24 giờ, cộng Oán Truy (WORLD) |

- **Bậc Nghiệp:**
  - ≥1: hào quang đỏ nhìn thấy trong 20 ô, mỗi điểm +10% sát thương kiếp (trần +50%).
  - ≥3: **Huyết Sát**, hiện trên bản đồ vùng, ai hạ được nhận thưởng ×3.
  - ≥5: **Thiên Phạt** [1.0], sét đuổi trong 1 ngày-rừng, mỗi 60 s một đòn 10% HP. Đồng hồ dừng khi offline. Sống sót thì Nghiệp về 0 nhưng mất 10% CT tầng.
  - Giảm 1 Nghiệp sau mỗi 2 giờ **online**.
- **Miễn trừ:** đánh trả người đã chủ động tấn công mình trong 60 s gần nhất (gai thụ động không tính là tấn công). Cùng một cặp người chơi: thưởng tu vi 1 lần/30 phút, Oán Linh và Nghiệp 1 lần/24 giờ.
- **Hộ Thể:** 60 phút trong rừng chung hoặc tới hết C2. Sát thương từ người có g≥2 giảm 60%, kẻ đánh không nhận gì và bị đánh dấu Bất Nhân 5 phút. Hộ Thể mất nếu người mới chủ động tấn công. Kèm **Ẩn Khí**: người C1–C2 không hiện trên radar Thần Thức của người có g≥2.
- **Áp Chế** n = 9 / 15 / ∞ (sim R: một C6 Hậu vào Rừng Non bị nén từ ×11,9 xuống ×2,14, người C2 vẫn thắng 9%). **Bỏ** cơ chế −HP vì linh khí loãng (PX) và thất thoát linh khí (SURV).
- **Bảng PvP theo chênh lệch** (sim R, combat ×1,77/cảnh):

| Chênh | P(1 người thấp thắng) | P(2 người thấp thắng) | P(3 người thấp thắng) |
|---|---|---|---|
| 1 cảnh | 15% | 96% | 100% |
| 2 cảnh | 2% | 70% | 99% |
| 3 cảnh | 0% | 26% | 86% |

### PROG-13b: Thành Thần [Post; ở solo là màn kết]
- **Thần Cách = tích lũy ≥250 Sinh Khí trong kiếp.** Sinh Khí là giá trị đã *trả cho rừng*: Quả Ước bị ăn (bằng CT người khác nhận được), Linh Hóa Địa, Hộ Pháp (2/phút), trả Linh Hạch về quỹ (4 mỗi lần), bảo vệ vùng trong world event (10), hạ Huyết Sát (5). Cổ Thú chỉ tính khi Linh Hạch được trả về quỹ. Kiểm chứng bằng telemetry: thời gian đạt Thần Cách giữa các loài phải nằm trong ±20%.
- **Qua Thiên Kiếp thì thành C7 Tán Thần:** rời chuỗi thức ăn (không ăn, không nhận thưởng giết). **Thần Quy:** không tấn công trực tiếp người dưới C5. **Thần Vị:** ngồi ghế của hành mình. Số ghế = clamp(⌊dân/15⌋, 3, 5) theo Ngũ Hành. Ghế đã có người thì phải **Thần Chiến** để giành. Thần Lực = f(sinh khí của Thần Vực) (WORLD-02).
- **Quy Căn** vào ngày 56: tên được khắc lên Thần Bia, nhận Đạo Tâm, rồi Luân Hồi. Core có thể **Quy Căn sớm** (khóa Đạo Tâm ×2) để chơi loài khác trong phần còn lại của Kiếp. Đây là van cho người Core chạm Thiên Kiếp ở ngày 20.

### PROG-16 (mới): Độ dài Kiếp — chốt bằng số [MVP-B: 28 ngày · bản đầy đủ: 56 ngày]
Kết quả sim Q: 3.000 người mỗi ô, 40% vào muộn, mô hình chết mới, Bù Đắp +0,5 khi dưới 60% tiến độ Mid.

| Chế độ | Kiếp | Casual: Phi Thăng Cổ Đại | Mid: Phi Thăng / chạm Thiên Kiếp / Thành Thần | Mid vào đầu Kiếp đạt đích | Core chạm Thiên Kiếp (trung vị ngày) |
|---|---|---|---|---|---|
| MVP (trần C5) | **28** | 0% (81% xong Rừng Non) | **52%** Phi Thăng | 75% | 85% Phi Thăng |
| MVP (trần C5) | 42 | 0% (69% vào C5) | 87% | 99% | — |
| Đầy đủ | 42 | 0% | 85 / 52 / 41% | 73% | 87% (21) |
| Đầy đủ | 48 (R2 của tôi) | 18% | 89 / 66 / 53% | 87% | 92% (20) |
| Đầy đủ | **56** | **55%** | **91 / 78 / 68%** | **95%** | 93% (20) |
| Đầy đủ | 63 | 61% | 94 / 83 / 76% | 99% | 96% (20) |

**Chốt:**
- **Kỷ Nguyên = 28 ngày:** làm mới bản đồ (địa hình, diễn thế, Khô Linh, lãnh thổ) và trùng với pass 28 ngày. Nhân vật được giữ.
- **Đại Kiếp = 56 ngày = 2 Kỷ Nguyên:** reset nhân vật.
- **MVP-B:** Đại Kiếp = 1 Kỷ Nguyên (28 ngày), vì nội dung dọc chỉ dài 3,6 tuần với Mid.
- **Rừng Non:** cứ 14 ngày mở một phòng mới, mỗi phòng sống 28 ngày. Người vào muộn luôn có phòng ≤14 ngày tuổi.
- **Lịch rừng đề xuất** (SURV/WORLD có quyền quyết cuối): 1 năm-rừng = 7 ngày thực, gồm 4 mùa × 42 giờ, ngày-rừng 24 phút. Một Đại Kiếp = 8 năm-rừng.

**Vì sao 56 mà không phải 48 hay 63:** từ 48 lên 56, Mid chạm Thiên Kiếp tăng 12 điểm % và Casual Phi Thăng tăng 37 điểm %. 56 là bội số của 28, và cả 3 thành viên kia đều đã đề xuất 8 tuần. Lên 63 chỉ thêm 5 điểm % và lệch với lịch pass. **Bù Đắp đổi ngưỡng từ 40% lên 60%** (sim Q3): Casual Phi Thăng từ 3% lên 54%, còn Mid chỉ thay đổi 3 điểm %. Đây là đòn bẩy rẻ nhất để Casual có cột mốc Cổ Đại.

### PROG-17 (mới): Sổ năng lượng thống nhất [MVP-A]
- **Sinh Năng** khi một sinh linh chết = 20 CT × m(g), chia: **8 cho kẻ ăn**, **4 vào Linh Hạch** (ai nhặt trước được), **8 vào đất** (rễ/nấm trong 3 ô; Khuẩn nhận khoảng 3; phần còn lại trả về quỹ vùng). Con mồi NPC nhân thêm theo cỡ: nhỏ ×0,5, vừa ×1, lớn ×2. Sau đó `k_s` của từng loài được chỉnh về 1,0 CT/phút.
- **Thiên Đạo Gia Trì:** cộng các bonus lại (Mộng Tích +1, Bù Đắp +0,5, loài đang thiếu +0,25, Mộ Linh +0,2, Linh Triều +1), **trần ×3**. Khi đang Hồi Ức, Hồi Ức tính là +3 (hoặc +1) và trần là ×4. Cộng thô tất cả là ×4,05, nên trần ×3 có tác dụng thật (sim T).
- **Party:** tổng CT nhóm = 1 + 0,6·min(k−1, 2), chia đều cho k người. Mỗi người nhận 100 / 80 / 73 / 55% khi k = 1 / 2 / 3 / 4. Hiệu suất mỗi người là ×1,00 / 1,08 / 1,17 / 0,96. Đi nhóm có lợi, nhưng bầy 4 con trở lên không còn lợi hơn (sim S).
- **Quỹ vùng** (WORLD-03b, SURV): mô hình đồ chơi trong sim U, Q = 200 LK, dòng vào 1,2 LK/phút. 4 thú săn làm vùng Khô Linh sau **2,8 ngày-rừng**. 2 thú + 1 cây + 1 nấm giữ quỹ 91%. 3 thú + 1 cây chạm Khô Linh sau 10 ngày-rừng. Bìa Rừng có sàn 50%. SURV sở hữu ngưỡng, WORLD sở hữu phần hiển thị.
- **Ads:** rừng chung 0 CT. Solo/co-op riêng: +5 phút Mộng Tích/ngày. **Offline: 0 CT.**

### PROG-15b: Build Archetype Cards (MVP)
| Build | Fantasy | Lõi | Mạnh | Yếu / đối trọng |
|---|---|---|---|---|
| Huyết Lang · Huyết Cuồng | Kẻ săn đơn độc | Chảy máu, Huyết Bộc | Burst, tự hồi máu | Tàng Thử (Thủy) khắc. Sát Nghiệp nếu săn kẻ yếu hơn ≥2 cảnh |
| Phong Lang · Thực Cốt | Bầy săn | Buff tốc, lướt | Bầy 3 con hạ cây trong 17 s | Party share chặn bầy ≥4. Thiết Mộc (Kim) khắc |
| Thiết Mộc · Bàn Căn | Pháo đài cổ thụ | Gai, Căn Tỏa, Kết Giới | Một sói cùng cấp không thể làm Đổ. Hộ Pháp kiếp cho clan | Bất động. Huyết Lang khắc. Độn Thử + lửa tận diệt được |
| Linh Quả Thụ + Tàng Thử (co-op 2 người) | Vườn cộng sinh | Quả Ước, Mầm Con làm neo | CT ổn định, Hậu Duệ an toàn | Phụ thuộc đồng minh. Độn Thử phá neo |
| Độn Thử · tận diệt | Kẻ phá rễ | Đào hầm, Căn Thương | Là loài duy nhất giết thật được cây | Mỏng (TTK 5 s trước sói). Nhóm Mộc khắc |

**Stress-test:** cộng dồn tối đa theo hướng tấn công (Huyết Cuồng +20%, Bản Thể +10%, crit) chỉ được khoảng ×1,32, thấp hơn khoảng cách 1 cảnh (×1,77). Combo nguy hiểm nhất: 3 Lang + Độn Thử giết cây trong 67 s. Cây có đối trọng: Rễ Cảm (báo trước 20 ô), Bàn Căn (Tâm Rễ +50%, thành khoảng 92 s), và Hậu Duệ từ Mầm Con.

---

## Bảng phạm vi theo ID
| ID | Nhãn | Chi phí (S≈1 / M≈2,5 / L≈5 tuần) |
|---|---|---|
| PROG-01c/02b/03b/04c (CT, đường cong, Mộng Tích, Áp Chế, tên 3 loài) | MVP-A | S + S |
| PROG-05b (6 Huyết Mạch, Ấn) | MVP-A | S (logic). Art 6 variant tính vào ngân sách art |
| PROG-06b: 18 kỹ năng từ 12 template | MVP-A | L |
| PROG-06b: Ngộ draft + 42 node có script (30 Notable, 12 Keystone) + 18 Minor | MVP-A | M |
| PROG-06b: 6 Thần Thông | MVP-B | S |
| PROG-07b: Tiểu Kiếp, Trung Kiếp C3→C4 (Tâm Ma) | MVP-A | M |
| PROG-07b: Kiếp C4→C5 (dùng lại template), Đại Kiếp | MVP-B | S |
| PROG-08b: Bản Thể | MVP-B | S |
| PROG-09b: Linh Thức lite | MVP-A | S |
| PROG-10c: Đổ / Hậu Duệ / Luân Hồi / Đạo Tâm Bàn 8 / Túc Tuệ | MVP-A | M |
| PROG-11b, PROG-17 | MVP-A | trong các mục trên |
| PROG-12c: Áp Chế + Hộ Thể + Ẩn Khí (với AI) | MVP-A | S |
| PROG-12c: Nghiệp đầy đủ, Huyết Sát, Oán Linh | MVP-B | S |
| PROG-12c: Thiên Phạt | 1.0 | S |
| PROG-16: Kiếp 28 ngày | MVP-B | — |
| PROG-16: Kiếp 56 ngày | Post (khi có Cổ Đại) | — |
| Nhánh Huyết Mạch thứ 3, Đạo Đồ chung (4 Đạo × 6 node vào pool draft), Khuẩn, Linh Thảo | 1.0 | M + L + L |
| C6 Xuất Khiếu, Nguyên Thần Bất Diệt, Keystone 2, Thiên Kiếp, Thần Cách, Thần Vị, Nhân Hình, Pháp Bảo, Lộc, Phong | Post | XL+ |
| Cửu Cảnh · đồ thị skill tree + Linh Điểm · Đạo Ngộ như khóa riêng · node "+% CT" trong meta · CT từ ad ở rừng chung · "xác = 20% CT tầng" · co-op 85% + 10% · thời gian chờ 24 giờ sau khi thất bại kiếp | **Cắt** | — |

**Tổng phần PROG ở MVP-A ≈ 13 tuần-người.** PX ước khoảng 11 tuần cho cùng khối việc. Phần chênh 2 tuần được bù khoảng 1 tuần nhờ UI draft rẻ hơn đồ thị cây. **Tôi ghi nhận còn vượt khoảng 1 tuần**; nếu phải cắt thì cắt Linh Thức lite trước, chuyển sang 1.0.

## Những thứ tôi mượn từ người khác
- **SURV:** HP 3 lớp và quy đổi "Tốc 0 → ×3 Thân" (SURV-03); Hậu Duệ và neo (SURV-15); hệ số needs → CT; Director bảo đảm sàn xác NPC; cấu trúc Sinh Năng 40/20/40 (SURV-09); tách Kỷ Nguyên 28 ngày khỏi Đại Kiếp 8 tuần (X2); g theo cảnh thật (X4).
- **WORLD:** bộ tên cảnh giới hợp nhất; tên C5 tách theo Đạo; Thần Cách = Sinh Khí đã trả; Quy Căn / Phi Thăng; glossary (Đạo Tâm, Tâm Hướng, Mộng Tích); Tâm Ma có modifier theo Tâm Hướng nhưng ngân sách cố định; quỹ vùng; nội dung Nhân Hình gắn với Nhân Tu; Duyên giảm giá mở loài; Linh Thử là loài trữ hạt nối thẳng với cây.
- **PX:** trần chi phí chết; MVP 3 loài / 2 nhánh / 24 skill; loadout 3+1; FTUE nén riêng; Ẩn Kiếp / Công Kiếp; Thiên Kiếp thất bại không phải lúc nào cũng chết; ad ở rừng chung cho 0 CT; Đả Tọa trần 15%; Kiếp MVP 28 ngày; phòng Rừng Non xoay vòng; Đạo Tâm = 25% CT lũy kế (PX-06).

## Lập trường giữ vững (và vì sao)
1. **Offline 0 CT.** Bây giờ cả team đã đồng ý. Ghi lại để không bị mở lại: chỉ 10% thụ động × 4 giờ/ngày đã làm CT/tuần ×1,52 (R2 sim H).
2. **Tốc không tăng theo cảnh, ×1,77 combat mỗi cảnh.** Đây là thứ giữ cho cả "trope cảnh giới áp đảo" lẫn lựa chọn "trốn" đều tồn tại. Không hạ xuống ×1,59 nữa, vì bản 7 cảnh không cần nén.
3. **TTK thú–thú vẫn ngắn (7,5 s), chỉ cây được kéo dài.** Nếu thú cũng 40 s thì chuỗi thức ăn biến mất. Con mồi phòng thủ bằng phát hiện sớm, tốc độ, hang và Hộ Thể, không phải bằng một thanh máu dày.
4. **Thiên Kiếp luôn công khai, và bị người chơi giết là chết thật.** Đó là đỉnh "hùng tráng + tàn khốc" của brief. Ẩn Kiếp chỉ dành cho Trung Kiếp và Đại Kiếp. Đã bù lại bằng: thất bại do sét chỉ mất 1,5 phiên, và Đạo Tâm ×2 khi chết.
5. **Lịch cố định, không kích hoạt Đại Kiếp theo số ghế Thần Vị.** Người Core chạm Thiên Kiếp ở trung vị ngày 20, nên kích hoạt theo ghế sẽ reset server trong lúc Mid còn ở C5.
6. **Đạo Tâm Bàn có 0 sức mạnh.** Lần này tôi còn cắt cả phần +10% CT mà R1 cho phép.
7. **Không chấp nhận Hậu Duệ "về đầu đại cảnh giới"** (WORLD), vì nó vượt trần PX tới 3 lần ở C5.

## Điều tôi sẵn sàng đánh đổi
- **Ngộ draft hay chọn cố định:** nếu playtest cho thấy người min-max ghét RNG (mục tiêu ≥70% người chơi hài lòng với lựa chọn Ngộ), tôi chuyển sang "chọn 1 trong 3 cố định theo cảnh", với cùng dữ liệu và cùng chi phí.
- **Linh Thức lite:** chuyển sang 1.0 nếu MVP-A vượt ngân sách.
- **Catch-up ×4/×2:** có thể hạ về ×3/×2 nếu telemetry cho thấy ≥70% người chết ở C≥4 quay lại trong 72 giờ (PX-H). Khi đó Luân Hồi ở C5 tốn khoảng 1 tuần.
- **Ngưỡng Bù Đắp 60% và Kiếp 56/63:** nếu tỉ lệ Casual quay lại Kiếp 2 dưới 40%, kéo lên 63 ngày (Casual Phi Thăng 61%) và chấp nhận lệch với lịch pass.
- **Ngưỡng Thần Cách 250 và số ghế Thần Vị:** chỉnh hoàn toàn theo telemetry. WORLD có quyền quyết phần lore.
