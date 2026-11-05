# R1 Proposal — PROG (Ngũ Tộc redefine, đã cập nhật theo BỔ SUNG của người dùng)

## 1. Cách tôi hiểu yêu cầu
Tộc nay là **loài sinh vật**. MVP đổi từ "3 loài" sang **5 tộc × đúng 1 nhân vật chơi được**, "chưa sâu". Giả định của tôi:
- Mỗi tộc một **vai** (thế mạnh) không tộc nào thay được; quan hệ 5×5 phải **đo được** bằng số, gắn Ngũ Hành (hệ số E đã có ở §6.4: khắc ×1,25 / bị khắc ×0,80).
- Nấm = môi trường (không thuộc tộc). Linh Thảo = Huyết Mạch của Linh Mộc, không còn là loài.
- Chiều sâu MVP chia hai bậc: **Linh Mộc và Linh Thử giữ thiết kế C1–C4 sẵn có** (đã có TTK, kỹ năng, FTUE); **3 tộc mới là bản lite C1–C3**.

## 2. Hook
Năm vai, năm cách thắng: **Mộc giữ đất, Thú chạy nhanh, Trùng đông, Thủy nuôi, Vũ thấy xa.** Mỗi cặp tộc có một mối quan hệ có số, nên ai cũng cần ai và không ai thống trị.

## 3. Đề xuất

### PROG-01: Năm nhân vật MVP và thế mạnh
| Tộc | Nhân vật MVP | Hành mặc định | **Thế mạnh (vai)** | Điểm yếu cố ý | Bậc MVP |
|---|---|---|---|---|---|
| Mộc | **Linh Mộc** (giữ) | Mộc | **Neo**: lãnh thổ, phòng thủ, hạ tầng | Bất động | C1–C4 |
| Thú | **Linh Thử** (giữ; **Lang → AI**, chơi được ở 1.0) | Thổ | **Cơ động + trữ**: Tốc 6,6, hang, mang hạt | Mỏng (300 HP) | C1–C4 |
| Trùng | **Linh Nghĩ** (kiến: Hậu + 3 Lính) | Hỏa | **Bầy**: nhiều mục tiêu nhỏ, đánh nhiều hướng, dọn xác | Lính chết 1 đòn diện rộng | C1–C3 lite |
| Thủy | **Linh Lý** (cá chép) | Thủy | **Hồi và nuôi**: Thanh Trì, nước sâu an toàn | Chỉ ở nước, sát thương thấp | C1–C3 lite |
| Vũ | **Linh Tước** (chim sẻ; Linh Kê (gà) [Post]) | Kim | **Tầm nhìn**: Thần Thức 20, chia sẻ tầm nhìn, Vỗ Cánh lướt | Mỏng nhất (240 HP) | C1–C3 lite |

- **Vì sao chọn Linh Thử, không phải Lang, làm đại diện Thú:** FTUE "Chuột mang hạt" (§12) đã là Linh Thử; giữ Lang sẽ buộc làm lại FTUE hoặc cả hai loài. Lang làm AI kẻ săn (đã có sẵn trong §5.8) và giữ tension. Đánh đổi: MVP mất vai "sát thủ PvP" của Lang, Độn Thử và Linh Nghĩ nhận một phần vai này.
- **Linh Nghĩ không phá công thức party:** Lính là đơn vị VFX/AI gắn vào Hậu, vẫn tính là 1 người chơi (k = 1). Công hiệu dụng = 22 × (1 + 0,25 × số Lính sống), tối đa 38,5.
- **Chọn kiến, không phải ong/bướm:** tái dùng swarm VFX + decal của Kiến lite (không rig mới).
- **Chọn chim sẻ, không phải chim bay thật/gà:** "bay" chỉ là Vỗ Cánh (xem PROG-06), nên top-down 2D không vỡ.

**Chỉ số cơ bản (n=1, theo §6.9):**
| | HP | Công | d | Tốc | Thần Thức |
|---|---|---|---|---|---|
| Linh Nghĩ | 300 (Hậu) · Lính 40 mỗi con | 22 + Lính | 0,25 | 5,4 | 12 |
| Linh Lý | 360 | 30 | 0,35 | 6,0 (nước) | 14 |
| Linh Tước | 240 | 24 | 0,20 | 6,6 + Vỗ Cánh | 20 |

### PROG-02: Bảng nguồn tu vi §4.2 mới (chuẩn 1,0 CT/phút ±10%)
| Loài | Nguồn chính | Nguồn phụ | Đặc thù | Phương sai |
|---|---|---|---|---|
| Linh Mộc | (giữ nguyên; "đất của xác" đổi thành "phần phân giải của xác") | | | ~16% |
| Linh Thử | (giữ nguyên) | | | ~22% |
| **Linh Nghĩ** | Mang mồi/dọn xác về tổ 40% | Tiếp tế Bầy (giữ đủ 3 Lính) 25% | Thoát Sinh 2 CT, Bầy phối hợp 35% | TB (~23%) |
| **Linh Lý** | Ăn tảo/ấu trùng/xác chìm 45% | Thanh Trì (Thủy Mạch) 25% | Thoát Sinh 2 CT, Ngược Dòng, cộng sinh cây ven nước 30% | Thấp–TB (~19%) |
| **Linh Tước** | Mổ hạt/côn trùng 40% | Do thám/báo tin cho đồng minh 25% | Thoát Sinh 2 CT, Vỗ Cánh, tranh đầu đàn 35% | Cao (~28%) |
| Lang [1.0] | giữ cũ (Săn 60%) | | | ~34% |

**Kiểm chứng** `sim/prog_r1_sim.py` (Poisson, phiên 30', 3.000 lần): Lý 0,997 CT/phút, CV 19,3% · Nghĩ 0,999, CV 22,8% · Tước 0,999, CV 28,4%. Tất cả trong ±10% mục tiêu. Hệ thống phương sai xếp đúng thế mạnh: Tước cao vì phụ thuộc cơ hội do thám.

### PROG-03: Hành mặc định và ma trận 5×5
**Quy tắc E:** nhân vật dùng **Hành của Huyết Mạch** nếu đã chọn (C3+), nếu chưa thì **Hành mặc định của tộc**. Khắc ×1,25 / bị khắc ×0,80 (đã có §6.4). Vòng sinh: Thủy→Mộc→Hỏa→Thổ→Kim→Thủy. Vòng khắc: Mộc→Thổ→Thủy→Hỏa→Kim→Mộc.

| Cặp (A–B) | Quan hệ | Hiệu ứng gameplay đo được |
|---|---|---|
| **Thủy → Mộc** | Sinh + cộng sinh | Cây trong 3 ô Thanh Trì: hao Thủy −30%, quang hợp +10%. Ngược lại rễ cây giữ bờ: ao trong 6 ô rễ không "cạn" mùa Hạ |
| **Mộc → Trùng** | Sinh + cộng sinh | Tán/Quả nuôi tổ: tổ kiến ở ô rễ không tốn Quang Tinh (−1/phút → 0) nhưng Lính hồi +50%. Trùng đáp lại −3 HP/s lên kẻ trong ô rễ (Kiến lite). Bầy sâu (AI) vẫn là áp lực |
| **Trùng → Thú** | Sinh | Thú ăn Trùng AI/xác dọn dở: +10 No. Linh Nghĩ dọn xác trước: Thú nhận ít hơn 25% |
| **Thú → Vũ** | Sinh + cộng sinh | Xác do Thú săn lộ Linh Hạch cho Vũ nhặt trước 2s; Tước báo kẻ săn (ping Thần Thức 20) cho Thú |
| **Vũ → Thủy** | Sinh + bổ trợ | Tước báo mưa/lộ mạch nước (+10% Thanh Trì trong 60s); Tước tắm nước nông hồi Thủy; Lý nhìn bờ qua tầm nhìn Tước |
| **Mộc ⊣ Thú** | Khắc | Mộc khắc Thổ: Độn Thử đào ô rễ chậm −20%; gai phản ×1,25. Thú đáp trả bằng Căn Thương (vẫn là kẻ duy nhất giết thật cây). Quả Ước: bổ trợ (Thử mang hạt) |
| **Thú ⊣ Thủy** | Khắc (nông) | Thổ khắc Thủy: Thú săn Lý ở **nước nông** ×1,25 (Lang AI, Thử đào bùn làm đục: Thanh Trì −50% 20s). Nước **sâu** miễn nhiễm |
| **Thủy ⊣ Trùng** | Khắc | Nước ngập tổ ven bờ: tổ −50% hiệu lực; Lý ăn ấu trùng/Lính ×1,25. Đổi lại: Trùng là mồi chính của Lý (nguồn chính 45%), nên Lý cần Trùng sống |
| **Trùng ⊣ Vũ** | Khắc | Hỏa khắc Kim: bầy ≥3 Lính trên Tước: Tốc −20%, ×1,25 sát thương. Nhưng Vũ ăn Trùng là nguồn chính; Tước bay qua bầy được bằng Vỗ Cánh |
| **Vũ ⊣ Mộc** | Khắc + bổ trợ | Kim khắc Mộc: mổ Tán −2 lá/mổ, ×1,25. Bù lại Tước ăn sâu (bầy sâu −50%) và ăn Quả Ước phát tán hạt xa gấp 2 |

**Ma trận 5×5 tóm tắt** (hàng = tác động lên cột):
| | Mộc | Thú | Trùng | Thủy | Vũ |
|---|---|---|---|---|---|
| **Mộc** | – | Khắc | Sinh | (nhận Sinh) | (nhận Khắc) |
| **Thú** | (nhận Khắc) | – | (nhận Sinh) | Khắc | Sinh |
| **Trùng** | Cộng sinh | Sinh | – | (nhận Khắc) | Khắc |
| **Thủy** | Sinh | (nhận Khắc) | Khắc | – | (nhận Sinh) |
| **Vũ** | Khắc | (nhận Sinh) | (nhận Khắc) | Sinh | – |

Mỗi tộc **1 quan hệ khắc ra, 1 bị khắc, 2 sinh/cộng sinh**, nên không có đỉnh thống trị. Đây là vòng Ngũ Hành khép kín, thay cho vòng chỉ có Huyết Mạch cũ.

**Kiểm tra thống trị (stress-test):** E ×1,25 so với khoảng cách 1 cảnh ×1,77 → khắc không bao giờ vượt cảnh. Cộng dồn Hành + Huyết Mạch tối đa ×1,32 (đã có §6.6) vẫn hợp lệ.

### PROG-04: Tên cảnh giới §6.2 mới
Bỏ cột Khuẩn và Linh Thảo. Cột loài MVP: Mộc, Thử, Nghĩ, Lý, Tước. Lang giữ [1.0].

| C | Khung | Linh Mộc | Linh Thử | **Linh Nghĩ** | **Linh Lý** | **Linh Tước** | Lang [1.0] |
|---|---|---|---|---|---|---|---|
| 1 | Khai Linh | Manh Nha | Khai Trí | Ấu Nghĩ | Ngư Tử | Sồ Tước | Ấu Lang |
| 2 | Luyện Khí | Trát Căn | Tàng Thực | Công Nghĩ | Nghịch Lưu | Mọc Vũ | Lang Nha |
| 3 | Trúc Cơ | Thành Tán | Ẩn Huyệt | Binh Nghĩ | Kim Lân | Đạp Phong | Lang Cốt |
| 4 | Kết Đan | Ngưng Tâm Mộc | Thử Đan | Nghĩ Đan | Ngưng Châu | Tước Đan | Lang Đan |
| 5 | Hóa Hình | Thụ Nhân ‖ **Cổ Mộc Yêu** (dạng Thảo: Thảo Tinh ‖ Dược Yêu) | Thử Nhân ‖ Yêu Thử | Nghĩ Nhân ‖ Yêu Nghĩ | Ngư Nhân ‖ **Giao Yêu** | Tước Nhân ‖ Yêu Tước | Lang Nhân ‖ Yêu Lang |
| 6 | Nguyên Anh | Mộc Hồn | Thử Hồn | Hậu Hồn | Vũ Môn Hồn | Thanh Điểu Hồn | Nguyệt Lang Hồn |
| 7 | Thành Thần | Mộc Thần | Thử Thần | Trùng Thần | Thủy Thần | Vũ Thần | Lang Thần |

Cột Lộc/Trùng cũ (Post) bỏ; loài thứ hai mỗi tộc thêm sau theo cùng kiểu.

### PROG-05: Giới hạn bản lite và Hóa Hình
- **Lite C1–C3 (Nghĩ, Lý, Tước):** 1 Bản Năng (C1) + 1 Bản Năng (C2) + A1 (C3) = 3 kỹ năng mỗi loài (9 tổng); Ngộ Đạo dùng pool 4 Bản Năng + **chưa có Huyết Mạch** (chỉ Ấn, xem nhánh mặc định). Hành = Hành tộc.
- **Cổng cuối MVP:** ở C3 Hậu của loài lite, Phi Thăng Kiếp I **khóa** ("Đạo này còn nảy mầm"). CT dư không mất mà **quy đổi 100% thành Đạo Quả** (meta, §7.3) và Hồi Ức vẫn chạy. Người chơi muốn lên cao luân hồi sang Mộc/Thử (C4). Thời lượng tới cổng ≈ Phiên 6 (1,1 tuần Mid), đủ cho thử.
- **Hóa Hình:** Hóa Hình Mộng (C4, MVP) vẫn chỉ Linh Mộc. **Bản Thể [U1]** theo template §6.7 và tên Yêu; **Lý**: Giao Yêu mở **Lên Bờ** (60s, Tốc ×0,7, CD 5'), Kiếp C4→5 = "Vượt Vũ Môn" (skin thác, cùng template Trung Kiếp). **Tước**: Yêu Tước mở **Bay Ngắn**. **Nghĩ**: Yêu Nghĩ mở Hậu thứ hai (4 Lính).
- **Huyết Mạch [1.0] cho tộc lite:** Lý: **Ngọc Lý** (Thủy, Sinh) ‖ **Kim Lân Lý** (Kim, Hộ). Nghĩ: **Hỏa Nghĩ** (Hỏa, Sát) ‖ **Thợ Nghĩ** (Thổ, Hợp). Tước: **Chu Tước** (Hỏa, Sát) ‖ **Phong Tước** (Mộc, Hợp). Mộc: **Bách Thảo** (Mộc, Sinh): rễ lan 1 ô/12s, Thân ×0,7, Phản Sinh sau khi chết, thay Linh Thảo (Plant Pressure giữ nguyên, thêm "Hươu ăn thảm": hồi Tán ×1,5).
- **Thiên Tài Địa Bảo "Linh Thảo"** giữ làm vật phẩm.

### PROG-06: Vũ Tộc, bay, và nước/cạn (quy tắc chung)
- **Vỗ Cánh** (Tước): lướt 5 ô trong 1,5s, vượt rào/bụi/nước, CD 10s; trong lúc lướt không né được đòn đang tới (tránh bất tử). Không có "bay thật" trong MVP/1.0. Chim bay thật (Ưng) là Post+ và tạo tầng "Không" riêng (Lực Cánh 8s), chưa cam kết.
- **Nước nông / sâu:** nông ai vào cũng được, loài cạn Tốc ×0,6. Sâu chỉ Thủy vào. Diện tích nước ≈ 6–8% map 256² (≈ 4.000–5.200 ô), đủ cho người chơi Lý. Fallback nếu Lý quá gò: đổi nhân vật Thủy MVP sang **Linh Oa** (ếch lưỡng cư).
- NPC giữ: Quạ Già (Vũ), Quạ Linh ăn xác, Diều hâu AI (Vũ AI).

### PROG-07: Ngũ Hành / Thần Vị (S4, §9.3)
Khớp tự nhiên với Hành tộc: Mộc – Rừng Lá Rộng · Thủy – Đầm Mục · Thổ – Đồng Cỏ (Thú) · Hỏa – Rừng Tro (Trùng) · Kim – Vách Đá Rêu (Vũ). Ai cũng giành được ghế nào; chỉ gợi ý lore + thưởng E ×1,05 cho tộc cùng Hành trong vực.

## 3b. Mục FINAL bị đổi
§2.7 · §4.1 (MVP 5 loài; Lang → AI + 1.0; Khuẩn/Linh Thảo bỏ) · §4.2 · §4.5 (thêm Nghĩ, Lý, Tước vào ma trận ăn nhau) · §5.6 · §6.1 (cổng lite) · §6.2 · §6.3 (Unlock Timeline: loài lite) · §6.4 (vòng Ngũ Hành 5×5) · §6.5 (ngân sách kỹ năng) · §6.7 · §6.9 (bảng base) · §9.3 · §16 (MVP/Won't).

## 4. Kết nối
- **SURV:** nước nông/sâu, HUD cho Nghĩ/Lý/Tước (4+1), sinh tồn đơn giản cho 3 tộc lite, sự kiện E7 đổi tên, Lang AI.
- **WORLD:** NPC Thủy thay Bà Khuẩn, tên 5 tộc, lore Vũ Môn.
- **PX:** FTUE giữ Linh Thử; ngân sách mới.

## 5. Rủi ro
1. **Scope (lớn nhất):** ước tính của tôi: cắt Lang −2,0 tuần-người (6 kỹ năng, 14 node, 1 sprite), thêm 3 loài lite +4,5 (mỗi loài 3 kỹ năng, sprite, HUD, đường cong) và luật nước +1,0 ⇒ **net ≈ +3,5**, vượt đệm 4,25 còn ≈0,75 (~1,6%). Cờ đỏ; cần PX tính lại.
2. **Fallback:** (a) Lý/Tước/Nghĩ ra mắt theo đợt (Nghĩ đợt 2, Tước đợt 3), (b) chỉ C1–C2 cho tộc lite, (c) bỏ nước sâu (một tầng nước).
3. Người chơi lite chạm cổng C3 thấy cụt → cần thông điệp tốt và Đạo Quả đủ thưởng.
4. Phương sai chỉ từ mô hình Poisson; thế mạnh "Bầy/Thanh Trì/Tầm nhìn" cần playtest.
5. Casual đọc 5×5 trong 30 giây? Chỉ hiện 3 icon quan hệ trên tooltip mục tiêu (khắc/sinh/bình thường).

## 6. Câu hỏi mở
Đại diện Thú là Thử hay Lang? Lý hay Oa? Nấm (môi trường) có cần icon riêng? Tộc lite có chia sẻ Mộng Tích không (tôi cho: có)?
