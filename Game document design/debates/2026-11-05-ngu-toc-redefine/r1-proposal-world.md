# R1 Proposal — WORLD (đã cập nhật theo Bổ sung của người dùng)

## 1. Cách tôi hiểu yêu cầu
Tộc nay là **loài sinh vật**. Mỗi tộc cần một thế mạnh không tộc nào thay được, có ma trận 5×5 sinh/khắc/bổ trợ/cộng sinh đo được, và MVP = **5 tộc × 1 nhân vật lite**. Nấm không bị xóa, chỉ không còn là tộc. Mọi quyết định khác của GDD v1.0 giữ nguyên.

## 2. Hook
**Nước là thứ duy nhất nhớ mà không giữ hình.** Mộng Hỏa tan vào nước khi chết, Thủy Tộc canh dòng đó, nên Luân Hồi (đổi hình) là việc của nước. Năm tộc nuôi nhau thành một vòng khép kín, đúng S2.

## 3. Đề xuất

### WORLD-01: Lore Thủy Tộc, vì sao nước giữ luân hồi *(§2.1 S1–S2, §2.7)*
- Linh Mạch (rễ Kiến Mộc) cũng là **mạch nước ngầm**; chỗ trồi lên là **Linh Tuyền**. Kiến Mộc ngã thì nhựa mộng chảy theo nước, nên Mộng Hỏa cũng trôi theo nước.
- S2 đổi: *nắng → cây → thú ăn cỏ → thú săn → xác → **đất/nước** → Linh Mạch*.
- Phân giải trên cạn do **Trùng Tộc** (giòi, bọ, kiến); ven nước do Thủy Tộc (tôm cua). Vai Thủy: *"dòng chảy, ký ức, giữ luân hồi"*.
- Cơ chế: vùng 64×64 có ao/suối hồi Linh Quỹ **+1%/h** (nước là bể chứa). Người chơi *làm* gì: tìm nước để hồi Quỹ, theo dòng để định hướng.

### WORLD-02: Cụ Ngao thay Bà Khuẩn *(§2.7, §7.2, §12)*
- **Cụ Ngao**: rùa cổ mai phủ rêu, ngồi giữa **Ao Gương** (Trung Lâm), bất động, 3 lời chào theo Tâm Hướng (tái dùng template Lão Tùng). Tên "Ngao" để không trùng "Quy Căn".
- Trung Ấm đặt **trên mặt nước**: camera nhìn xác qua gương nước, xác chìm/tan, Cụ Ngao nói 1 câu. 1 ảnh, cùng ngân sách cũ.
- Giọng: chậm, ngắn, lặp "ừ". Lời mẫu:

| Cách chết | Câu |
|---|---|
| FTUE (giữ) | *"Ngươi đã mang nó cả đời. Giờ nó mang ngươi."* |
| Bị Lang ăn | *"Răng nó nhớ ngươi lâu hơn ngươi nhớ nó. Ừ."* |
| Đói | *"Bụng rỗng thì nước cũng lạnh. Uống đi, rồi đi."* |
| Cây héo | *"Rễ ngươi khát từ lâu. Nước không giận ai."* |
| Kiếp thất bại | *"Sét chỉ hỏi một câu. Ngươi chưa trả lời xong."* |
| Có Nghiệp | *"Nước rửa được máu. Không rửa được tên."* |
| Hậu Duệ | *"Nhỏ xuống đây, rồi mọc lên kia. Ừ."* |

- **Pool ~60 câu**: giữ cấu trúc (≈12 nhóm cách chết × 5); bỏ từ *nấm, bào tử, ủ, mục*, thay *nước, dòng, gương, chìm, trôi, đục/trong*. Chi phí 0.

### WORLD-03: Nước trên map 256² *(§2.3, §2.4, §5.4)*
Một **dòng Linh Tuyền** chảy từ Linh Nhãn ra Bìa Rừng, đúng hướng linh khí chảy ra ngoài. **Ngược dòng = vào trong** (breadcrumb thay minimap).

| Vòng | Nước |
|---|---|
| Linh Nhãn | Mắt suối (ao nhỏ, đầu nguồn) |
| Thâm Lâm | **Đầm Mục**: nước sâu duy nhất, bùn, xác phân giải nhanh hơn, **Liễu Chết** ven đầm |
| Trung Lâm | Suối nông, đá bậc, **Ao Gương** (Cụ Ngao) |
| Bìa Rừng | Cửa suối, vũng mưa quanh **vòng nấm tiên** |

- **3 loại ô:** *nước nông* (Tốc ×0,75, xóa mùi/vệt máu như mưa; Thủy của cây tính 3× như cũ) · *nước sâu* (chỉ Đầm Mục, chặn mọi tộc trừ Thủy; không đuối nước) · *bến cạn* (3 chỗ qua Đầm, điểm nghẽn PvP).
- Cá/ếch/cua AI là swarm VFX dưới mặt nước, không hitbox. Dùng lại palette Thâm Lâm + lớp nước.

### WORLD-04: Nấm, Mộng Ấn *(§2.4, §4.2, §5.5, §5.7, E7, §16.4)*
- Nấm = "da của Linh Mạch", **không có Mộng Hỏa, không thuộc tộc nào**: *"Nấm không mộng nên không nhớ. Nó chỉ làm sạch."* Giữ: vòng nấm tiên, nấm ăn được, **Tơ Nấm** (nền cộng sinh của cây [1.0]), "rễ/nấm" trong Sổ Sinh Năng → "rễ, Tơ Nấm, Trùng/Thủy AI trong 3 ô". Bỏ loài Khuẩn và cột Khuẩn §6.2.
- **MA1**: vòng nấm quanh vũng nước; bình minh thấy bóng mình trên vũng. **MA3**: Liễu Chết soi xuống Đầm, bóng người cầm rìu hiện trên **nước**. Chủ đề *"nước nhớ"*. Chi phí 0.
- **E7 Bào Tử Triều → Triều Mộng** [1.0]: sương dâng từ ao sau ngày nhiều chết; thắng: Thủy Tộc, đầu thai ven nước +1 Duyên.
- §5.7 "cây/nấm" → "cây".

### WORLD-05: Thế mạnh 5 tộc và 5 nhân vật MVP *(§4.1, §4.2, §2.7, §16)*
| Tộc | Thế mạnh (không tộc nào thay được) | Nhân vật MVP | Lite tới |
|---|---|---|---|
| **Mộc** | **Nuôi**: lãnh thổ, hạ tầng, Linh Quỹ | **Linh Mộc** (giữ nguyên) | C4 |
| **Thú** | **Săn**: burst, tốc độ | **Lang** (kẻ săn cho persona P2) | C4 |
| **Trùng** | **Bầy + dọn xác**: sức mạnh theo số, biến xác thành Quỹ nhanh ×2 | **Linh Nghĩ** (kiến; 1 "Nghĩ Chúa" + swarm VFX tái dùng Kiến lite) | C2 |
| **Thủy** | **Dòng**: ẩn/hồi/neo trong nước, kéo kẻ địch | **Thanh Oa** (ếch lưỡng cư; nước sâu = Hang) | C2 |
| **Vũ** | **Mắt**: Thần Thức +30%, ping party, vượt địa hình | **Linh Kê** (gà rừng; Sải Cánh 3s, CD 20s, tốn 60 Thể Lực, không né sát thương, nên không có tầng cao phá top-down) | C2 |

- **Linh Thử** hạ xuống AI (con mồi, Hạt Quên) hoặc FTUE-only. Lang được giữ vì sói là lời hứa với P2.
- **FTUE đề xuất: "Kiến mang hạt"** (kiến tha hạt là có thật); fallback B: giữ chuột FTUE-only (+0,5 tuần). Cụ Ngao, Lão Tùng, hạt nảy mầm từ xác đều giữ nguyên.
- Tên cảnh giới (C1–C3 trước): **Linh Nghĩ** Ấu Nghĩ · Thợ Nghĩ · Binh Nghĩ. **Thanh Oa** Nòng Nọc · Rụng Đuôi · Thượng Ngạn → Thiềm Yêu (Hóa Hình). **Linh Kê** Gà Con · Kê Gáy · Kê Sải. Hậu bán: Linh Ngư (cá chép, vượt Vũ Môn hóa Giao Long) [Post], Cua [Post].

### WORLD-06: Ma trận 5×5 *(mới, §4.5)*
Khớp Ngũ Hành: Mộc-Mộc · Thú-Hỏa · Trùng-Thổ · Vũ-Kim · Thủy-Thủy. **Sinh:** Mộc→Thú→Trùng→Vũ→Thủy→Mộc. **Khắc:** Mộc⊣Trùng⊣Thủy⊣Thú⊣Vũ⊣Mộc. Đủ 10 cặp, không tộc nào khắc cả bốn hay bị cả bốn khắc.

| Hành động → | Mộc | Thú | Trùng | Vũ | Thủy |
|---|---|---|---|---|---|
| **Mộc** | tranh rễ | sinh | khắc | bị khắc | được sinh |
| **Thú** | được sinh | tranh mồi | sinh | khắc | bị khắc |
| **Trùng** | bị khắc | được sinh | bầy chồng bầy | sinh | khắc |
| **Vũ** | khắc | bị khắc | được sinh | tranh tầm | sinh |
| **Thủy** | sinh | khắc | bị khắc | được sinh | cùng ao |

| Cặp | Hiệu ứng đo được |
|---|---|
| Mộc→Thú (sinh, cộng sinh hạt) | Quả Ước +15 No (đã có); Thú trong 8 ô Tán hồi Thể Lực +20% |
| Thú→Trùng (sinh) | Xác thú: Nghĩ ăn trong 2s (thay vì 4s), Sinh Năng Đất ×1,5 |
| Trùng→Vũ (sinh) | Kê ăn Nghĩ/sâu No +6, và thấy bầy trong 20 ô |
| Vũ→Thủy (sinh) | Kê gáy bình minh: sương +15 Thủy trong 8 ô; Kê ghé ao thì đàn cá +1/ngày-rừng |
| Thủy→Mộc (sinh, cộng sinh) | Oa "Dẫn Nước": +6 Thủy/phút cho cây trong 4 ô; Oa trong ô rễ được ẩn và hồi 1%/5s |
| Mộc⊣Trùng | Gai/Độc ×1,15 lên Nghĩ; bầy <3 bị đẩy khỏi ô rễ (trừ cây nuôi kiến: cộng sinh) |
| Trùng⊣Thủy | Bầy Nghĩ ≥3 làm bờ "đục" 20s: Oa mất ẩn/hồi ở ô đó |
| Thủy⊣Thú | Nước sâu chặn Lang; Oa "Quăng Lưỡi" kéo/chậm 1s, CD 12s |
| Thú⊣Vũ | Lang ×1,15 lên Kê khi Sải Cánh đang CD; Kê thấy Lang trong 20 ô để tránh |
| Vũ⊣Mộc | Kê phá Mầm-Neo nhanh ×2 và đánh dấu Tâm Rễ cho party 30s |

**Luật cân bằng:** hệ số tộc-khắc ≤×1,15, **không cộng dồn với E Huyết Mạch §6.4 (lấy giá trị lớn hơn)** để giữ trần ×1,32. Khắc chủ yếu là **cơ chế** (chặn, đục, kéo, lộ vị), không phải sát thương. PROG xác nhận.

### WORLD-07: Ngũ Hành, Thần Vị, Mộc gồm cỏ, Vũ Tộc *(§2.7, §4.1, §5.6, §9.3)*
- 5 Thần Vị giữ biome (Thủy = Đầm Mục); thêm lore: thần đầu của ghế là "tổ" tộc tương ứng, **ai cũng nhập vị được**. Tag Ngũ Hành Huyết Mạch §6.4 không đổi.
- Linh Thảo **vẫn loài riêng [1.0], giới Mộc**; cỏ AI tính cùng cây khi cân bằng ("Mộc <15%"). Vật phẩm Thiên Tài Địa Bảo "Linh Thảo" → **Hoàng Tinh Thảo**.
- **Quạ Già giữ** (Sứ giả). Diều hâu AI, Quạ Linh thuộc Vũ Tộc. "Vũ Tộc chơi được [Won't]" → Linh Kê **[MVP lite]**. Chim bay tự do vẫn [Won't].

## 4. Mục FINAL bị đổi
§0 TL;DR (3 loài → 5 tộc) · §2.1 S1–S2 · §2.4 · §2.7 · §4.1–4.2 · §4.5 (thêm ma trận) · §5.5, §5.7 · §6.2 (xóa cột Khuẩn, thêm 3 cột) · §7.2 Trung Ấm · §10 E7 · §12 FTUE · §16.1 (#3–#5) · §16.4 · §19 (D6, thêm D20).

## 5. Scope delta (gợi ý, PX chốt)
- **+** Linh Nghĩ lite 0,75 · Thanh Oa lite + ô nước 1,25 · Linh Kê lite 0,75 · ma trận 10 cặp (script nhỏ) 0,5 = **+3,25**.
- **−** Linh Thử playable −1,0 · Kiến lite dùng chung hạ tầng với Linh Nghĩ −0,5 · Hóa Hình Mộng −0,25 · Huyết Mạch tộc lite = 1 nhánh/tộc (không chọn) −0,5 · palette/Quạ Linh dùng lại −0,3 = **−2,55**. Ròng **≈+0,7**, đệm còn ~3,5 tuần (7%): **scope risk**.
- Fallback: ba tộc lite chỉ C1 + 1 skill, hoặc ra mắt theo đợt (Mộc, Thú, Trùng trước; Thủy, Vũ ở U1).

## 6. Rủi ro và câu hỏi mở
- Ba tộc lite kẹt ở C2: PROG xử lý Hồi Ức/Túc Tuệ khi Luân Hồi từ C4 sang tộc lite (cần kẹp theo trần C2).
- 5 tộc làm test cân bằng ×5 (PvP 10 cặp): PX cân nhắc chỉ bật 4 cặp có hiệu ứng mạnh ở MVP.
- Nước sâu có thể tạo vùng chết: 3 bến cạn là cách kiểm.
- Q: FTUE kiến hay chuột? Tôi chọn kiến (không thêm nhân vật), giữ chuột làm fallback B.
