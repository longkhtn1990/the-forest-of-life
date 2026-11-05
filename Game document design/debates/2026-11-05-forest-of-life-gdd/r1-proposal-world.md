# R1 Proposal — WORLD

> Domain: theme & pillars, lore, cấu trúc thế giới (cấp rừng / vùng / biome / bí cảnh), rừng biến đổi theo thời gian, thế lực, world events, luân hồi (góc câu chuyện), đặt tên cảnh giới, phát triển nội tâm, ý tưởng chơi thực vật mới.
> Nguyên tắc tự áp: mỗi mảnh lore phải trả lời được câu "người chơi **làm** gì với nó?". Mỗi mục có dòng **[Chạm gameplay]** và **[Chi phí authored]**.

## 1. Cách tôi hiểu yêu cầu

Người dùng muốn một game sinh tồn–tu tiên nơi **người chơi là "yêu" chứ không phải "tu sĩ"**: một cái cây, ngọn cỏ, con sói, con kiến tu luyện trong khu rừng có chuỗi thức ăn thật (PvP tự do), chết thì luân hồi sang loài khác, mục tiêu tối thượng là sống sót và **thành thần**. Rừng có 3 cấp quy mô, mỗi map có vòng ngoài→trong, và rừng **thay đổi theo thời gian và hành động**. Tôi coi đây là game về **vòng tuần hoàn sự sống**, nên mọi hệ thống (EXP, cái chết, PvP, sự kiện, endgame) phải *vận hành như một vòng tuần hoàn*, không chỉ được trang trí bằng lời thoại về vòng tuần hoàn.

**Giả định của tôi:**
- **A1.** Ba cấp rừng ánh xạ thẳng vào trope **"phi thăng"** của tiên hiệp: Rừng Non ≈ Hạ Giới, Nguyên Sinh ≈ Linh Giới, Cổ Đại ≈ Thần Giới. Người đọc tiên hiệp hiểu ngay, không cần giải thích.
- **A2.** Không có cutscene, không voice. Câu chuyện chạy bằng: môi trường, ~12 NPC **bất động** (cây/đá cổ — rẻ nhất có thể), text ngắn, và **biên niên sử tự sinh** từ dữ liệu chơi.
- **A3.** Số cảnh giới tôi đề xuất là **9** (3 mỗi cấp rừng) để khung câu chuyện khớp; PROG là chủ con số cuối cùng — nếu PROG chọn số khác, tôi giữ logic "mỗi cấp rừng = 1 đại cảnh giới, có 1 độ kiếp lớn để phi thăng".
- **A4.** Solo/offline dùng cùng thế giới và sự kiện, đối thủ là AI; lore không phân biệt.

## 2. Ý tưởng cốt lõi (hook)

**"Trong tiểu thuyết tiên hiệp của người khác, bạn là gốc linh dược và con yêu thú bị săn. Ở đây, bạn tu luyện từ phía bên kia."** Rừng là xác đang tái sinh của Kiến Mộc — cây nối trời đất. Mỗi sinh linh có ý thức là một tia mộng của nó. Bạn ăn, bị ăn, chết, mọc lại. Thành thần không có nghĩa là thoát khỏi vòng tuần hoàn. Thành thần nghĩa là **trở thành nơi vòng tuần hoàn chảy qua**.

---

## 3. Đề xuất chi tiết

### WORLD-01: Theme Statement & 5 Design Pillars
- **Theme (1 câu):** *"Mọi sự sống đều được nuôi bằng một sự sống khác. Kẻ mạnh nhất không phải kẻ ăn nhiều nhất, mà là kẻ nuôi được cả khu rừng."*
- **Pillars (góc trải nghiệm cảm xúc):**

| # | Pillar | Người chơi phải cảm thấy | Kiểm chứng bằng cơ chế |
|---|---|---|---|
| P1 | **Ăn và bị ăn** | Hồi hộp thật, mỗi sinh linh khác là con mồi hoặc mối đe dọa tiềm năng | PvP tự do, chuỗi thức ăn có người chơi ở mọi bậc |
| P2 | **Chậm mà vĩ đại** | Kiên nhẫn có trả công: cây nhỏ hôm nay thành cổ thụ phủ bóng cả vùng sau 3 tuần | Thực vật lớn dần trên bản đồ, persistent |
| P3 | **Cái chết là hạt giống** | Chết thì đau nhưng có ý nghĩa: xác mình nuôi rừng, kiếp sau mạnh hơn | Luân hồi + dinh dưỡng xác + Đạo Tâm giữ lại |
| P4 | **Rừng nhớ** | Hành động của mình (và của người khác) để lại dấu vết trên thế giới | Diễn thế sinh thái, mộ linh, biên niên sử |
| P5 | **Trời đất chứng giám** | Độ kiếp, sự kiện lớn là khoảnh khắc hùng tráng mà cả server nhìn thấy | Độ kiếp công khai trên map, world events |

- **Vì sao tốt:** P1 và P3 xung khắc có chủ đích. P1 đẩy người chơi đi giết, P3 + WORLD-03 khiến "giết hết" tự phá hủy nguồn sống của chính mình. Lực kéo đó chính là theme. Ta không cần lời thoại giảng đạo nào.

### WORLD-02: Lore cốt lõi — Kiến Mộc, Linh Khí, Linh Trí, Thần Vị
Lore chỉ gồm **4 sự thật**. Mỗi sự thật gắn với một cơ chế:

| Sự thật | Nội dung | [Chạm gameplay] |
|---|---|---|
| **S1. Kiến Mộc đã ngã** | Xưa có Kiến Mộc (建木), cây nối trời và đất. Trong "Đại Kiếp" trước, nó bị chặt hạ (bởi ai thì là bí ẩn của hồi 3). Rễ của nó vẫn sống dưới đất, gọi là **Linh Mạch**. | Linh Mạch là các "đường" linh khí trên map, cũng là nơi đặt Linh Nhãn và bí cảnh. Thực vật cắm rễ trúng Linh Mạch nhận bonus. |
| **S2. Linh khí là hơi thở của rễ cũ** | Linh khí rỉ lên từ Linh Mạch, càng gần gốc (lõi map) càng đặc. Linh khí **không tự sinh thêm**, nó chỉ chuyển chủ: nắng→cây→thú ăn cỏ→thú săn mồi→xác→nấm→đất. | Nền lore cho luật bảo toàn linh khí (WORLD-03), lý do vùng trong giàu và nguy hiểm, lý do xác trả linh khí về đất. |
| **S3. Linh trí là mộng của Kiến Mộc** | Khi Kiến Mộc ngã, giấc mộng của nó vỡ thành vô số **Mộng Hỏa** (tia mộng). Sinh linh nào hấp thu đủ linh khí sẽ "bắt" được một tia và thức tỉnh linh trí. **Người chơi là một Mộng Hỏa.** Vì vậy cây, cỏ, nấm và thú đều có ý thức như nhau. | Giải thích luân hồi: Mộng Hỏa không chết, chỉ đổi vỏ. Cũng giải thích vì sao người chơi khác loài vẫn "nói chuyện" được với nhau (chat, emote). |
| **S4. Thần Vị là rễ của Kiến Mộc mới** | Trong Rừng Cổ Đại có **9 Thần Vị**, chính là 9 rễ cái đang chờ được lấp. Khi đủ 9 Thần Vị có chủ và nuôi đủ linh khí, Kiến Mộc mọc lại và một Đại Kiếp mới bắt đầu (= reset mùa server). | Endgame + live-ops season. Lời giải thích cho "server reset" là **sự kiện câu chuyện đỉnh điểm**, không phải bảo trì. |

- **"Thành thần" nghĩa là gì:** chiếm một Thần Vị và **trở thành chủ của một Thần Vực** (1 trong 9 vùng của Cổ Đại). Sức mạnh của thần **không đến từ việc giết**. Nó đến từ **tổng sinh khí của Thần Vực** (số sinh linh sống trong vực, độ phủ thực vật, dòng linh khí tuần hoàn). Kẻ săn mồi đỉnh chuỗi phải đổi vai, từ kẻ ăn thành người giữ vườn. Đó là arc lớn nhất của game.
- **Vì sao tốt:** 4 sự thật, đọc trong 1 phút, mà giải thích được: ý thức của vạn vật, nguồn linh khí, vùng trong nguy hiểm, luân hồi, endgame và reset mùa. **[Chi phí authored]:** ~1.500 từ lore rải trong NPC và bí cảnh.

### WORLD-03: Luật Linh Khí Tuần Hoàn (lore → luật hệ thống)
- **Mô tả:** mỗi vùng (region ~ 64×64 tile) có một **quỹ linh khí**. Sinh linh hút từ quỹ (quang hợp, ăn), chết thì trả lại quỹ qua xác (nấm/đất phân giải). Nếu tỷ lệ *hút ra / trả về* của một vùng vượt ngưỡng quá lâu, vùng rơi vào trạng thái **Khô Linh**: tốc độ tu luyện −50%, cây úa, thú NPC bỏ đi. Đây cũng là trigger của sự kiện Hạn Linh (WORLD-10).
- **Số liệu gợi ý (để SURV/PROG chỉnh):** Khô Linh kích hoạt khi quỹ < 30% sức chứa trong 1 ngày-rừng. Hồi về 60% thì hết. Xác của sinh linh cảnh giới N trả về quỹ ≈ 40% linh khí nó tích lũy, 60% còn lại theo Mộng Hỏa vào luân hồi (meta) và vào kẻ ăn xác.
- **Tình huống:** một bầy 4 sói (co-op) càn quét Thung Lũng Sương trong 2 tối. Đến tối thứ 3, cả vùng xám màu, nai NPC biến mất, chính bầy sói đói. Một người chơi nấm vào phân giải xác và hồi linh khí cho vùng, kiếm bộn EXP.
- **Vì sao tốt:** biến lời giảng "đừng tham" thành hậu quả cơ học. Tạo niche cho nấm/thực vật. Tránh mâu thuẫn ludonarrative kiểu "game về rừng mà cách mạnh nhất là phá rừng".

### WORLD-04: Ba cấp rừng = Ba giới (phi thăng)

| Cấp | Tên trong lore | Quy mô gợi ý | Người chơi/instance | Cảnh giới | Danh tính | Câu hỏi | Bí mật |
|---|---|---|---|---|---|---|---|
| 1 | **Rừng Non — "Hạ Lâm"** | ~256×256 tile, 3 vòng | Solo/co-op 1–4, server nhỏ ≤30 | 1–3 | Rừng trẻ, nắng nhiều, sáng sủa; nguy hiểm chủ yếu là NPC thú và người chơi cùng cấp | "Vì sao tôi tỉnh dậy biết nghĩ?" | Rừng Non mọc từ **một hạt** rơi từ Rừng Cổ Đại; lõi của nó là một cây mẹ đang ngủ |
| 2 | **Rừng Nguyên Sinh — "Linh Lâm"** | ~512×512, 4 vòng | 30–80 | 4–6 | Tán dày, tầng lớp sinh thái phức tạp, tu sĩ loài người hay xâm nhập | "Vì sao linh khí đang cạn dần?" | Tu sĩ loài người hút Linh Mạch từ ngoài vào; Kiến Mộc đã ngã vì họ |
| 3 | **Rừng Cổ Đại — "Thần Lâm"** | ~1024×1024, 9 Thần Vực | 80–200 | 7–9 | Cây cao như núi, gốc Kiến Mộc ở tâm, ánh sáng xanh tím phát quang | "Kiến Mộc có nên mọc lại?" | Thần cũ tự hiến thân làm rễ; mọc lại Kiến Mộc = một Đại Kiếp mới, xóa đi thế giới hiện tại |

- **Phi thăng (chuyển cấp):** đạt cảnh giới đỉnh của cấp (3 hoặc 6) **và** vượt Đại Độ Kiếp thì được phi thăng. Mỗi giới có cách phi thăng riêng, mỗi cách là một **khoảnh khắc**:
  - Thực vật: kết **Phi Thăng Tử** (hạt phi thăng), gió Linh Triều cuốn hạt bay lên. Người chơi điều khiển hạt bay qua mây trong 30 giây. Đây cũng là màn loading.
  - Động vật: theo **Đại Di Cư** (WORLD-10) đi qua Linh Mạch Môn ở lõi map.
  - Côn trùng/nấm: bám vào thân một sinh vật di cư hoặc bào tử theo Linh Triều.
- **Được ở lại hay quay về:** người đã phi thăng có thể trở về cấp dưới bằng **phân thân** đã bị giới hạn sức mạnh về cảnh giới tối đa của cấp đó. Như vậy họ có thể dẫn bạn mới, nhưng không thể nghiền nát người mới (hỗ trợ G1).
- **Vì sao tốt:** cấu trúc server/map (yêu cầu kỹ thuật) trở thành vũ trụ quan tiên hiệp quen thuộc. Mỗi cấp trả lời câu hỏi của cấp trước (mystery hook theo chuỗi). **[Chi phí]:** 3 bộ palette và tileset biến thể của cùng một bộ biome (WORLD-06), không phải 3 bộ art riêng.

### WORLD-05: Vòng ngoài → trong & wayfinding top-down

| Vòng | Tên | Mật độ linh khí | Nguy hiểm | Thị giác | Âm thanh |
|---|---|---|---|---|---|
| Ngoài | **Bìa Rừng** | ×1 | Thấp; là vùng ươm mầm (newbie spawn) | Xanh vàng ấm, nhiều nắng loang, tán thưa | Chim hót, gió |
| Giữa | **Trung Lâm** | ×2 | Trung bình | Xanh đậm, tán dày, vệt sáng hẹp | Côn trùng rỉ rả, tiếng thú xa |
| Trong | **Thâm Lâm** | ×4 | Cao; NPC "cổ thú" | Xanh lục–lam, sương, rêu phát quang | Ù trầm, tiếng gỗ kẽo kẹt |
| Tâm | **Linh Nhãn** | ×8 (vùng nhỏ) | Rất cao; nơi tranh đoạt | Tím–lam phát quang, hạt linh khí bay ngược lên | Hợp âm kéo dài, gần như im lặng |

- **Wayfinding (quan trọng vì top-down không có đường chân trời):**
  1. **Cột Linh Quang:** Linh Nhãn bắn một cột sáng. Khi nó nằm ngoài khung hình, một vệt sáng mờ hiện ở mép màn hình chỉ hướng tâm. Không cần minimap mà vẫn luôn biết "trong" ở đâu.
  2. **Hạt linh khí trôi về tâm.** Mật độ hạt tăng dần là thước đo trực quan cho độ sâu.
  3. **Giới Bia:** cột đá rêu đánh dấu ranh vòng. Đi qua thì có rung nhẹ và chữ "Thâm Lâm — Cảnh giới đề nghị 3+".
  4. **Color grading theo vòng.** Người chơi nhìn màu là biết mình đang ở vòng nào (có chế độ accessibility thêm icon).
- **Vì sao tốt:** rẻ (shader và particle), rõ ràng, nhất quán ở cả 3 cấp rừng.

### WORLD-06: Bộ biome module (6 biome, tái dùng qua 3 cấp)

| Biome | Danh tính | Câu hỏi | Bí mật | Độ khó | Tài nguyên đặc trưng | Loài hưởng lợi |
|---|---|---|---|---|---|---|
| **Đồng Cỏ Ven Rừng** | Rộng, sáng, không chỗ trốn | "Ở chỗ trống thì sống thế nào?" | Dưới cỏ là Thảo Mạch: đồng cỏ là **một** sinh linh cổ | 1 | Nắng ×1.5, hạt cỏ | Cỏ, thú ăn cỏ, ong |
| **Rừng Lá Rộng** | Rừng "chuẩn", cân bằng | "Ai đang trị vì vùng này?" | Cây lớn nhất chính là Lão NPC; dưới gốc là bia Thần cũ | 1–2 | Lá, quả, sâu | Mọi loài |
| **Đầm Mục** | Ẩm, thối rữa, nấm dày đặc | "Cái chết đi về đâu?" | Mạng khuẩn ty dưới đầm là cổng Trung Ấm (WORLD-11) | 2–3 | Xác, mùn, nước | Nấm, côn trùng |
| **Trúc Lâm Gió** | Thẳng đứng, gió liên tục, âm thanh rì rào | "Gió mang đi những gì?" | Gió chở hạt phi thăng; trúc nở hoa 1 lần/mùa server thì chết đồng loạt (sự kiện nhỏ) | 2 | Gió (phát tán hạt ×2), măng | Thực vật phát tán gió, chim |
| **Vách Đá Rêu** | Cao, hiểm, hang hốc | "Cái gì trốn trên cao?" | Khắc đá của **trận pháp cổ** (WORLD-14g) | 3 | Khoáng, rêu, tổ | Leo trèo, săn phục kích |
| **Hang Rễ** (ngầm) | Tối, hẹp, rễ Kiến Mộc lộ ra | "Gốc rễ của rừng ở đâu?" | Nối thẳng vào Linh Mạch, lối tắt tới vòng trong | 3+ | Linh tinh, nước ngầm | Nấm, côn trùng, rễ |
| *(Sinh ra từ sự kiện)* **Rừng Tro** | Đen xám, sau Đại Hỏa | "Sau khi mất hết thì sao?" | Đất tro dinh dưỡng ×3; hoa Phượng Hỏa chỉ nở ở đây | 2 | Tro, mầm | Cây tiên phong, côn trùng |

- **Phân bố theo cấp:** Rừng Non có 3 biome đầu, kèm Đầm Mục ở vòng trong. Nguyên Sinh có đủ 6. Cổ Đại có 9 Thần Vực, mỗi vực lấy 1 biome chủ đạo và phóng to ×2 (cây to như núi).
- **[Chi phí]:** MVP chỉ cần 3 biome (Đồng Cỏ, Lá Rộng, Đầm Mục). Biến thể cấp rừng làm bằng scale sprite, palette và mật độ.

### WORLD-07: Bí cảnh (instance ngắn, rule-based)
- **Mô tả:** không gian túi 10–20 phút, sinh từ **template + modifier** (không làm level tay từng cái). Có 4 loại template:

| Template | Lore | Cách mở (knowledge-gated) | Gameplay | Phần thưởng |
|---|---|---|---|---|
| **Mộng Cảnh Cổ Thụ** | Ký ức của một cây cổ đã chết | Đứng tại gốc cây chết **vào đêm trăng tròn** khi có Lão NPC chỉ điểm | Khám phá, giải đố môi trường, đọc ký ức (lore hồi chính) | Mảnh Đạo Tâm, công pháp hiếm |
| **Trùng Sào** | Tổ côn trùng vương | Theo dấu kiến lính về tổ (dấu vết trên map) | Dungeon co-op 2–4 | Vật liệu tiến hóa |
| **Lôi Trì** | Ao tích sét của trời | Mở sau mỗi bão | Luyện độ kiếp: tập né mẫu sét, không mất gì | Giảm độ khó độ kiếp kế |
| **Linh Mạch Huyệt** | Mạch linh khí lộ thiên | Xuất hiện ngẫu nhiên trong Linh Triều | PvP tranh đoạt có giới hạn cảnh giới (vd chỉ cảnh 2–3 vào được) | Linh khí ×10 trong 5 phút |

- **Tình huống:** người chơi cỏ nghe Lão Tùng nói "khi trăng tròn soi bóng gốc Liễu Chết, nàng sẽ kể lại". Đêm trăng tròn, họ tới đó và một vòng sáng mở ra. Trong Mộng Cảnh, họ thấy rừng 1.000 năm trước, khi Kiến Mộc còn đứng, và thấy bóng người cầm rìu.
- **Vì sao tốt:** lời khuyên của NPC trở thành *kiến thức để vào bí cảnh*, nên người chơi tiến bộ nhờ hiểu chứ không chỉ nhờ stat. Bí cảnh dạng PvP có giới hạn cảnh giới là "sân chơi công bằng" cho người mới.

### WORLD-08: Rừng biến đổi theo thời gian (3 lớp)
**Lớp 1 — Nhịp thời gian:**
- 1 ngày-rừng = **24 phút thực** (12 sáng / 8 tối / 4 hoàng hôn+bình minh). Một session 15–60 phút thấy được 1–2 chu kỳ ngày đêm.
- 1 mùa = **48 giờ thực**. 1 năm-rừng = 8 ngày thực. **1 Kiếp (mùa server) = 6 năm-rừng ≈ 7 tuần**, khớp với mong muốn "tiến trình nhiều tuần".
- Bốn mùa theo nguyên lý **Xuân Sinh – Hạ Trưởng – Thu Thu – Đông Tàng**:

| Mùa | Lore | Gameplay đề xuất |
|---|---|---|
| Xuân Sinh | Vạn vật nảy mầm | Thực vật tăng trưởng ×1.5, nảy mầm hạt; ấu thú NPC nhiều (mồi dễ) |
| Hạ Trưởng | Cạnh tranh gay gắt | Linh khí cao nhất; nguy cơ Đại Hỏa; PvP nóng |
| Thu Thu | Thu hoạch, béo lên | Quả chín (WORLD-14d), Đại Di Cư; tích trữ |
| Đông Tàng | Ẩn mình, bế quan | Thực vật ngủ đông **nhưng xuất khiếu mạnh ×2** (cây "mơ" xa hơn); thú cần tích trữ; tuyết để lại dấu chân (săn bằng dấu vết) |

**Lớp 2 — Diễn thế sinh thái (succession):** mỗi tile có giai đoạn 0–4: *Đất trống → Cỏ → Bụi → Rừng thưa → Rừng già*. Cuối mỗi mùa, tile tăng 1 bậc nếu dinh dưỡng ≥ ngưỡng và có hạt giống lân cận. Lửa đưa tile về 0 nhưng cho dinh dưỡng ×3. Lãnh thổ của người chơi thực vật đẩy diễn thế nhanh hơn. Kết quả: **bản đồ tuần 1 và tuần 6 trông khác nhau thật**.

**Lớp 3 — Vết tích (persistent marks):**
- **Mộ Linh:** nơi một sinh linh cảnh giới ≥4 chết sẽ mọc **Hoa Mộ Linh** trong 1 năm-rừng. Ai chạm vào sẽ đọc được 1 dòng: *"Nơi đây Hắc Lang 'Tro Tàn' (cảnh 5) ngã xuống dưới nanh Hổ 'Thanh Ảnh', mùa Hạ năm 3."*
- **Thần Vực:** biome của một Thần Vực trôi dần theo "đạo" của vị thần cai quản (thần Sát thì vực tối và gai góc, thần Sinh thì vực tươi và hoa nở).
- **[Chi phí]:** chủ yếu là code và data, gần như không cần authored content. Rủi ro hiệu năng: tôi cần PX/tech đánh giá việc lưu trạng thái ~65k–1M tile.

### WORLD-09: Thế lực — "Ngũ Tộc" + kẻ ngoài rừng

| Thế lực | Là ai | Vai trò hệ thống | Vai trò cảm xúc | NPC đại diện (bất động) |
|---|---|---|---|---|
| **Mộc Tộc** | Cây gỗ, cỏ, thảo dược | Lãnh thổ, hạ tầng, ký ức rừng | "Người ông" chậm rãi, nhớ mọi thứ | **Lão Tùng**: cổ thụ dạy đạo, chỉ đường bí cảnh |
| **Thú Tộc** | Ăn cỏ và ăn thịt | Săn bắt, di chuyển, tranh lãnh địa | Sức mạnh, bản năng, kiêu hãnh | **Bạch Lộc Tàn Hồn**: hồn hươu trắng ở suối |
| **Trùng Tộc** | Kiến, ong, bướm, bọ | Bầy đàn, cộng sinh, thụ phấn | Tập thể vs cá nhân | **Trùng Hậu Hóa Thạch**: tổ kiến cổ hóa đá |
| **Khuẩn Tộc** | Nấm, khuẩn ty | Phân giải, mạng ngầm, **quản luân hồi** | Người đưa đò, dịu dàng và lạnh | **Bà Khuẩn**: mạng nấm khổng lồ ở Đầm Mục, chủ Trung Ấm |
| **Vũ Tộc** *(NPC, có thể mở sau)* | Chim | Sứ giả liên rừng, chở hạt, tin tức | Tự do, tin đồn | **Quạ Già**: đậu trên Giới Bia, bán tin đồn về sự kiện sắp tới |
| **Nhân Tu** *(chỉ NPC, đối thủ ngoài rừng)* | Tu sĩ loài người vào rừng hái linh dược, săn yêu đan | Mối đe dọa của world event, mục tiêu đoàn kết | "Kẻ đi săn trong tiểu thuyết khác", phản chiếu chính người chơi | Không có NPC thân thiện, chỉ dấu vết: trại cháy, bẫy, cây bị đẽo |

- **Quan hệ:** không làm hệ thống danh tiếng phức tạp. Đề xuất **1 thanh "Thân Cận" cho mỗi Lão NPC** (0–5), tăng khi người chơi làm điều mà NPC trân trọng (Lão Tùng: trồng cây; Bà Khuẩn: trả xác về đất; Trùng Hậu: cộng sinh). Mỗi mức mở thêm 1 lời chỉ điểm bí cảnh hoặc 1 công pháp.
- **[Chi phí]:** ~12 NPC bất động (2–4 mỗi cấp rừng), mỗi NPC ~300–500 từ thoại. Tổng ~5.000 từ, viết với AI được.

### WORLD-10: Sự kiện lớn toàn rừng (8 sự kiện, hầu hết emergent-trigger)

| # | Sự kiện | Trigger | Thời lượng | Gameplay | Ý nghĩa câu chuyện |
|---|---|---|---|---|---|
| E1 | **Linh Triều** (thủy triều linh khí) | Định kỳ mỗi 2 mùa | 1 ngày-rừng (24') | Linh khí ×2 toàn map; vòng Thâm Lâm lan ra ngoài 1 vòng; Linh Mạch Huyệt mở; thú NPC cuồng loạn | Rừng "thở"; cửa sổ phi thăng cho thực vật |
| E2 | **Huyết Nguyệt** | Mỗi tuần thực, đêm thứ 7 | 1 đêm (8') | Thú ăn thịt +30% sức mạnh; cổ thú từ lõi đi ra vòng ngoài; con mồi chết rơi gấp đôi linh khí | Cá lớn nuốt cá bé ở đỉnh điểm; đêm sợ hãi có hẹn trước |
| E3 | **Đại Hỏa** | Mùa Hạ + Hạn Linh + sét (xác suất) | Lan dần 1–2 ngày-rừng | Lửa lan theo tile khô; thực vật phải chống chịu hoặc kết hạt chạy trốn; thú chạy; sau lửa thành **Rừng Tro** | Cái chết là hạt giống: phá hủy để tái sinh (P3) |
| E4 | **Đại Di Cư** | Mỗi mùa Thu | 1 ngày-rừng | Đàn thú NPC lớn băng qua map: bữa tiệc cho thú săn mồi; giẫm nát cây trên đường; **mang hạt đi xa** (cơ hội lan rộng cho thực vật); mở Linh Mạch Môn để phi thăng | Chuyển động giữa các giới |
| E5 | **Tu Sĩ Nhập Sơn** | Emergent: khi ≥N sinh linh cảnh ≥4 tụ một vùng ("linh khí tỏa ra thu hút tu sĩ") | 1–2 ngày-rừng | Đoàn Nhân Tu NPC vào từ Bìa Rừng, săn **mục tiêu cảnh giới cao nhất và linh dược quý nhất**; tạm có **"Vạn Linh Minh Ước"** (cờ đình chiến tùy chọn: ai bật thì không bị/không đánh người chơi khác cùng bật); phần thưởng cho đóng góp | "Từ bên ngoài nhìn vào, tất cả các ngươi đều là con mồi." Đoàn kết xuyên chuỗi thức ăn |
| E6 | **Hạn Linh** (khô linh) | Emergent: tổng vùng Khô Linh > 30% map | Đến khi phục hồi | Nguồn nước co lại, tu luyện chậm, Đại Hỏa dễ xảy ra; nhiệm vụ cộng đồng "hồi linh" (trồng cây, trả xác, khơi Linh Mạch) | Hậu quả của lòng tham, do chính người chơi gây ra |
| E7 | **Bào Tử Triều** | Emergent: sau một ngày có tỷ lệ chết cao (thường là sau E2/E3/E5) | 1 ngày-rừng | Sương bào tử phủ đầm và lan ra; tầm nhìn giảm; nấm ×3 sức mạnh; **luân hồi nhanh** (thời gian Trung Ấm −50%); mộ linh phát sáng | Cái chết nuôi sự sống; Khuẩn Tộc lên ngôi |
| E8 | **Thần Vị Khai → Đại Kiếp** | Cuối mỗi Kiếp (~tuần 6–7) | Tuần cuối | 9 Thần Vị mở cho tranh đoạt (cảnh 9); khi đủ 9 thần, Kiến Mộc trổ một chồi (cảnh tượng toàn server) → **Đại Kiếp**: rừng cháy sáng và reset, mọi người luân hồi về mùa mới với Đạo Tâm giữ lại; tên các thần được khắc vào **Thần Bia** vĩnh viễn | Thành thần, rồi vòng tuần hoàn bắt đầu lại ở quy mô vũ trụ |

- **Nhịp đề xuất:** mỗi tuần có E2 cố định, cộng 1–2 sự kiện mùa (E1/E4), cộng các sự kiện emergent. Quạ Già báo trước 1 ngày-rừng cho các sự kiện dự đoán được, để người chơi 15 phút cũng lên kế hoạch được.
- **Solo/offline:** E1–E4, E7 chạy y hệt. E5/E6 trigger theo hành vi AI và người chơi. E8 thu nhỏ thành "Thần Vị cá nhân" (đánh 9 thần AI).
- **[Chi phí]:** tất cả dựa trên luật và biến số map. Authored chỉ gồm: sprite Nhân Tu (3 loại), hiệu ứng lửa/sương/trăng, ~20 dòng thông báo.

### WORLD-11: Luân hồi dưới góc câu chuyện — "Trung Ấm" và "Nghiệp Duyên"
- **Trung Ấm (bardo), 30–60 giây có tương tác, cũng là màn chờ:**
  1. Camera giữ ở xác. Người chơi thấy xác phân hủy nhanh (timelapse 5 giây) và đọc dòng tóm tắt: *"Thân xác ngươi nuôi 3 cây non, 1 cụm nấm, trả 412 linh khí về Đầm Mục."*
  2. Mộng Hỏa rơi xuống mạng khuẩn ty, nơi **Bà Khuẩn** đón (1–2 câu, chọn ngẫu nhiên từ pool ~60 câu theo cách chết).
  3. Màn chọn đầu thai: chọn loài và chọn **điểm sinh** (chỗ sinh mặc định ở Bìa Rừng; nếu có bạn co-op là cây thì có thể sinh từ cây đó, xem WORLD-14i).
- **Nghiệp Duyên (cách mở khóa loài, đề xuất cho PROG):** *"Ăn gì thì hiểu nấy."* Mỗi tương tác chuỗi thức ăn với loài X (ăn X, bị X ăn, cộng sinh với X) cộng **Duyên** với X. Đủ Duyên thì X mở cho đầu thai, hoặc rẻ hơn. Bị sói ăn 3 lần thì bạn "hiểu" sói và có thể thành sói. Logic luân hồi Phật giáo trở thành logic mở khóa: muốn chơi loài mới thì phải **gặp** loài đó trong chuỗi thức ăn, không phải mua.
- **Tiền Kiếp Ấn:** mỗi kiếp đã sống để lại một dấu nhỏ trên sprite kiếp sau (sói có vân lá mờ vì từng là cây; nấm có ánh đỏ vì từng là hổ). Đây là cosmetic **kiếm được**, không bán, là "huy chương" cho người chơi lâu năm. PX có thể bán skin nền nhưng không bán ấn.
- **Biên niên kiếp (auto-generated):** mỗi kiếp sinh 1 trang nhật ký tự động: *"Kiếp thứ 4 — Sói Xám 'Khói'. Sống 9 ngày-rừng. Ăn 41 sinh linh. Phi thăng thất bại ở Lôi Kiếp thứ 2. Ngã xuống trong Đại Hỏa năm 2."* Có thể chia sẻ thành ảnh (marketing tự nhiên). **[Chi phí]:** template text khoảng 50 mẫu.
- **Vì sao tốt:** cái chết có *nghi thức* (Spiritfarer) thay vì màn "You Died", và người chơi thấy ngay xác mình nuôi rừng (P3). Mở khóa loài qua chuỗi thức ăn khiến PvP và cái chết thành con đường tiến bộ chứ không chỉ là mất mát.

### WORLD-12: Đặt tên cảnh giới — khung chung + tên riêng theo giới
**Quy tắc UI:** luôn hiển thị **số cảnh + tên riêng**, ví dụ "Cảnh 4 · Ngưng Tâm Mộc". Số dùng để đọc nhanh trong PvP, tên dùng để tạo không khí.

| Cảnh | Khung chung (Thiên Đạo gọi) | Mộc (cây gỗ) | Thảo (cỏ/thảo dược) | Thú (ăn cỏ ‖ ăn thịt) | Trùng (côn trùng) | Khuẩn (nấm) | Mốc |
|---|---|---|---|---|---|---|---|
| 1 | Khai Linh | Manh Nha | Phá Thổ | Khai Trí | Ấu Trùng | Bào Tử | Rừng Non |
| 2 | Luyện Khí | Trát Căn | Liên Căn | Linh Thú | Thoát Xác | Khuẩn Ty | |
| 3 | Trúc Cơ | Thành Tán | Thành Thảm | Yêu Binh | **Kết Kén** | Khuẩn Mạng | ⚡ Tiểu Kiếp → phi thăng |
| 4 | Kết Đan | Ngưng Tâm Mộc | Ngưng Dược Tính | Yêu Đan: *Thụy Thú* ‖ *Hung Thú* | Phá Kén | Ngưng Tán | Nguyên Sinh |
| 5 | Hóa Hình | Thụ Linh Hóa Hình | Thảo Tinh Hóa Hình | Yêu Hóa Hình | Trùng Nhân Hóa Hình | Khuẩn Linh Hóa Hình | |
| 6 | Nguyên Anh | Khai Hoa Kết Tử | Vạn Diệp Đồng Tâm | Yêu Vương | Vạn Trùng Đồng Thức | Địa Mạch Thông | ⚡ Đại Kiếp → phi thăng |
| 7 | Phản Hư | Niên Luân Vạn Tải | Thiên Niên Linh Dược | Yêu Hoàng: *Kỳ Lân* ‖ *Sơn Quân* | Cổ Trùng | U Minh Khuẩn | Cổ Đại |
| 8 | Hợp Đạo | Thông Thiên Cổ Thụ | Thảo Nguyên Chi Hồn | Đại Yêu | Trùng Hoàng | Luân Hồi Ty | ⚡ Thiên Kiếp |
| 9 | Thành Thần | **Mộc Thần** | **Bách Thảo Thần** | **Thú Thần** | **Trùng Thần** | **Luân Hồi Thần** | Thần Vị |

- **Tên phản ánh sinh học và ludonarrative:**
  - Côn trùng **Kết Kén** ở cảnh 3: độ kiếp của côn trùng là giai đoạn kén, bất động và dễ tổn thương. Bầy cộng sinh/co-op phải canh giữ. Khoảnh khắc này đã có sẵn trong sinh học.
  - Thảo **Ngưng Dược Tính** ở cảnh 4: lúc này bạn chính là "linh dược" mà Nhân Tu săn (liên kết E5).
  - Thú tách nhánh ở cảnh 4 (Thụy Thú/Hung Thú) theo **Đạo Tâm** (WORLD-13), không theo chế độ ăn cứng.
- **Quy tắc đặt tên cho pipeline AI** (để thêm loài mới mà không lệch giọng): Hán-Việt, 2–4 âm tiết; từ gốc theo giới: Mộc/Căn/Diệp/Niên Luân; Thảo/Dược/Hương; Huyết/Cốt/Nha/Yêu; Kén/Giáp/Sào; Ty/Bào/Tán/Mạch. Tên cảnh 9 luôn là "<X> Thần".

### WORLD-13: Đạo Tâm — phát triển nội tâm song song với tiến hóa
- **Mô tả:** 2 trục đo **bằng hành vi** (không có hộp thoại lựa chọn), hiển thị như một la bàn âm–dương nhỏ:
  - **Sinh ↔ Sát:** nuôi, cộng sinh, trả xác, trồng, chữa lành ↔ giết, ăn, chiếm đoạt.
  - **Hợp ↔ Độc:** co-op, cộng sinh, Minh Ước ↔ hành động đơn độc, phản bội, cướp mồi của đồng đội.
- **Đạo Tâm thay đổi những gì:**

| Hệ quả | Ví dụ |
|---|---|
| Nhánh tiến hóa (PROG) | Thú nghiêng Sinh thì nhánh Thụy Thú (Kỳ Lân, có hồi máu và vùng chúc phúc); nghiêng Sát thì Hung Thú (Sơn Quân, có uy áp làm con mồi chậm) |
| **Tâm Ma Kiếp** trong độ kiếp | Phần "tâm ma" của độ kiếp **sinh từ dữ liệu của chính người chơi**: nghiêng Sát thì bóng ma của những con mồi đã ăn (đúng loài, đúng số lượng có giới hạn) săn lại bạn; nghiêng Độc thì đối mặt bản sao chính mình; nghiêng Sinh/Hợp thì phải chọn hy sinh một phần lãnh thổ hoặc buff để cứu "ảo ảnh đồng đội". Emergent và rẻ: dùng lại sprite có sẵn |
| Lời Lão NPC | Lão Tùng chào khác nhau theo Đạo Tâm (3–4 biến thể mỗi NPC) |
| Ngoại hình | Aura nhẹ: xanh lá (Sinh), đỏ sẫm (Sát), ánh vàng (Hợp), xám lạnh (Độc). Người chơi khác **đọc được ý đồ** trước khi giao chiến, tạo thông tin cho PvP |
| Thần Vực | Biome của Thần Vực trôi theo Đạo Tâm của thần (WORLD-08 lớp 3) |
| Luân hồi | Một phần Đạo Tâm giữ lại qua kiếp (meta), nên "tính cách" của người chơi tồn tại xuyên loài |

- **Arc nội tâm theo cấp rừng** (khung cảm xúc, không phải script):
  - Rừng Non: **"Ta là gì?"** Bản năng sinh tồn, sợ hãi, thèm ăn.
  - Nguyên Sinh: **"Ta muốn gì?"** Lựa chọn Đạo, quan hệ, thù hận, cộng sinh.
  - Cổ Đại: **"Ta để lại gì?"** Thần Vực, hậu duệ, tên trên Thần Bia.
- **Vì sao tốt:** stat và nội tâm cùng một nguồn dữ liệu (hành vi), nên không có chuyện người chơi "chọn hội thoại tốt" rồi đi giết hết. Tâm Ma Kiếp biến độ kiếp thành khoảnh khắc *cá nhân*, mỗi người một khác.

### WORLD-14: Ý tưởng chơi thực vật mới (ngoài rễ/hạt, cộng sinh, xuất khiếu, hóa hình)
Mục tiêu: thực vật không bị thụ động, mà đóng **vai trò không thể thay thế** trong rừng: **ký ức, hạ tầng, ngoại giao, trận pháp**.

| ID | Tên | Cơ chế | Cơ sở sinh học/tiên hiệp | Chi phí ước |
|---|---|---|---|---|
| 14a | **Cầu Viện Hương** | Khi bị ăn lá, cây tỏa mùi gọi **thiên địch** (ong bắp cày NPC, hoặc ping cho người chơi thú ăn thịt gần đó kèm phần thưởng "bữa ăn có sẵn") | Thật: cây tiết chất bay hơi gọi ong ký sinh diệt sâu | Thấp |
| 14b | **Mị Hương** | Hoa tỏa hương mê hoặc: dụ mồi tới bẫy (cây ăn thịt) hoặc làm thú NPC đổi hướng | Hoa bắt ruồi; "mị thuật" tiên hiệp | Thấp |
| 14c | **Ký Sinh Đoạt Xá** (nhánh tầm gửi/đông trùng) | Gắn vào sinh vật **NPC** để đi nhờ (thực vật có di động); nấm đông trùng điều khiển côn trùng NPC. Với người chơi khác chỉ là debuff "Ký Sinh" hút linh khí, có thể gỡ | Đông trùng hạ thảo; trope đoạt xá | Trung bình |
| 14d | **Quả Ước** (fruit covenant) | Cây kết **Linh Quả**: ai ăn được buff, **và mang hạt của cây đi xa**, nơi hạt rơi thành lãnh thổ mới của cây. Cây chọn quả *lành* hay *độc*. Tạo hợp tác giữa người chơi cây và thú mà **không cần đình chiến** | Phát tán hạt qua động vật | Thấp. Rất quan trọng: nối thực vật và động vật bằng kinh tế chuỗi thức ăn |
| 14e | **Niên Luân Ký Ức** | Cây "ghi" mọi sự kiện trong vùng rễ: ai đi qua, ai giết ai, tài nguyên ở đâu. Người chơi cây có **bản đồ tình báo** chia cho party; người khác có thể *đọc niên luân* của một cây (nếu cây cho phép hoặc bị đánh gục) | Vòng gỗ ghi lại năm tháng; pillar "Rừng nhớ" | Trung bình |
| 14f | **Mộc Độn** | Đồng đội co-op dịch chuyển giữa các cây trong mạng rễ của người chơi cây. Cây trở thành **hạ tầng và fast-travel của nhóm** | Độn thuật tiên hiệp | Trung bình |
| 14g | **Trận Pháp Thực Vật** | Trồng cây/hạt theo **hình học** (tam giác, vòng tròn, ngũ hành) để kích hoạt trận: *Tụ Linh Trận* (linh khí ×1.5 trong vùng), *Mê Trận* (che vùng khỏi tầm nhìn người ngoài), *Kinh Cức Trận* (gai sát thương). Mẫu trận **học từ khắc đá cổ** ở Vách Đá Rêu và bí cảnh (knowledge-gated) | Trận pháp tiên hiệp; vòng nấm tiên (fairy ring) | Trung bình: chủ yếu là luật, ít asset |
| 14h | **Đông Tàng Mộng Du** | Mùa Đông thân cây ngủ nhưng xuất khiếu ×2 tầm. Đây là "mùa của linh hồn": người chơi cây đi khắp rừng dưới dạng linh thức, do thám, truyền mộng | Ngủ đông; tu bế quan | Thấp |
| 14i | **Ký Hồn Mộc** | Đồng đội chết có thể **đầu thai từ cây** của người chơi thực vật (điểm sinh gần, Trung Ấm ngắn hơn). Cây là "từ đường" của nhóm | Tục cây thiêng giữ hồn | Thấp |
| 14j | **Truyền Mộng** | Ban đêm, linh thức của cây chạm vào sinh vật đang ngủ: thú NPC sinh thiện cảm (không tấn công lãnh thổ), người chơi đang offline/ngủ (nếu có cơ chế ngủ) nhận buff/thông điệp ngắn | Báo mộng | Thấp–Trung bình |

- **Vai trò tổng hợp của thực vật trong một party co-op 4 người:** 1 cây (căn cứ, fast-travel, tình báo, hồi sinh) + 3 thú/côn trùng (săn, bảo vệ, mang hạt). Đây là **lý do để mời bạn chơi cây**, không phải nhân vật phụ.
- **Tôi ưu tiên cho MVP:** 14d Quả Ước, 14f Mộc Độn, 14g Trận Pháp (bản 2 trận), 14i Ký Hồn Mộc.

### WORLD-15: Kiến trúc mục tiêu & Narrative Beat Chart
**Phân tầng mục tiêu:**
- **Main thread (bí ẩn Kiến Mộc):** 9 **Mảnh Mộng** (3 mỗi cấp rừng) tìm trong Mộng Cảnh. Mỗi mảnh là 1 vignette ~150 từ và 1 hình minh họa tĩnh. Không bắt buộc để tiến hóa, nhưng mở công pháp và giải thích vì sao thế giới như vậy.
- **Regional arcs:** mỗi biome có 1 bí mật (bảng WORLD-06), giải bằng quan sát và chỉ điểm của Lão NPC.
- **Emergent goals:** world events, Khô Linh, thù hận PvP (WORLD-16).
- **Self-directed:** lãnh thổ, phi thăng, Thần Vị, tên trên Thần Bia.

| Hồi | Cấp rừng | Sự kiện chính | Mở khóa cơ chế | Cảm xúc mục tiêu |
|---|---|---|---|---|
| 1 "Tỉnh Mộng" | Rừng Non | Thức tỉnh linh trí, lần chết đầu tiên (Trung Ấm), Tiểu Kiếp đầu tiên | Cơ chế loài, luân hồi, Đạo Tâm | Sợ → tò mò → tự hào |
| 2 "Rừng Đói" | Nguyên Sinh | Khô Linh, Nhân Tu xâm nhập, phát hiện Kiến Mộc bị chặt | Hóa Hình, Minh Ước, trận pháp, Quả Ước | Giận → đoàn kết → day dứt |
| 3 "Rễ Mới" | Cổ Đại | Thần Vị Khai, lựa chọn mọc lại Kiến Mộc | Thần Vực, Thần quyền | Hùng tráng → hy sinh → khởi đầu lại |

### WORLD-16: Chống bắt nạt người mới bằng lore — "Thiên Phạt Lấn Yếu" (đề xuất ngoài domain, cho SURV/PX)
- **Mô tả:** PvP luôn tự do, nhưng **Thiên Đạo ghi nghiệp**. Giết sinh linh *người chơi* thấp hơn mình ≥2 cảnh giới thì nhận **Nghiệp Lực**. Nghiệp Lực cao gây ra: (1) linh khí nhận từ kill đó ≈ 0; (2) aura đỏ hiện trên bản đồ của mọi người trong vùng; (3) đạt ngưỡng thì **sét Thiên Phạt** đuổi theo bạn trong 1 ngày-rừng (giống độ kiếp mini), và ai giết được bạn lúc đó nhận thưởng.
- **Kết hợp:** Bìa Rừng có **Ấu Linh Che Chở** cho người chơi < 2 giờ chơi tổng (sát thương nhận −50% từ người chơi cao hơn ≥2 cảnh); phân thân giới hạn cảnh khi quay về cấp dưới (WORLD-04).
- **Tình huống:** người chơi hổ cảnh 5 vào Bìa Rừng Nguyên Sinh giết 3 thỏ cảnh 2. Mây đen tụ trên đầu nó, cả server thấy "Thiên Phạt giáng xuống Hổ 'Thanh Ảnh'". 4 người chơi sói cảnh 4 lập party đi săn nó.
- **Vì sao tốt:** không có vùng cấm PvP nhân tạo. Hậu quả là *thiên ý*, phù hợp tiên hiệp và tạo nội dung emergent (săn kẻ có nghiệp).

### WORLD-17: Tone & mood board bằng lời
- **Màu:** ban ngày vòng ngoài vàng–lục (#C9D97A, #6FA35A); vòng trong lục–lam (#2F6B5E, #1F4E5F); Linh Nhãn tím–lam phát quang (#7B6FD6, #9FE3F0). Độ kiếp: trắng–tím sét trên nền xám mây. Đại Hỏa: cam–đỏ với tro bay. Nhân Tu: sắc vải đỏ son và vàng kim, **màu duy nhất "nhân tạo"** trong game, để thấy ngay là kẻ lạ.
- **Âm thanh:** đàn tranh/sáo trúc + ambient tự nhiên; mỗi vòng thêm một lớp trầm; Huyết Nguyệt bỏ nhạc, chỉ còn tiếng tim đập và tiếng tru.
- **Nhịp:** 70% thời gian là "tĩnh căng" (ăn, lớn, quan sát), 20% là bùng nổ (săn, PvP), 10% là khoảnh khắc hùng tráng (độ kiếp, sự kiện).

---

## 4. Kết nối với các domain khác
- **PROG:** chốt số cảnh giới (tôi đề xuất 9, với 3 độ kiếp lớn ở cảnh 3/6/8). Cần công thức Đạo Tâm → nhánh tiến hóa. Cần Nghiệp Duyên là cơ chế mở khóa loài (WORLD-11). Cần tỷ lệ linh khí giữ lại khi luân hồi (tôi gợi ý 60% theo Mộng Hỏa, chia giữa meta và kẻ ăn xác). Cần kiểm tra Thần Vực có scale sức mạnh thần theo *sinh khí vùng* mà không vỡ cân bằng.
- **SURV:** quỹ linh khí vùng và Khô Linh (WORLD-03) là luật sinh thái. Cần SURV đặt needs của từng giới theo mùa (Đông Tàng). Lửa lan theo độ khô. Kiểm tra chuỗi thức ăn có đủ NPC đệm để rừng không "rỗng" khi ít người chơi.
- **PX:** đánh giá chi phí lưu trạng thái diễn thế tile (WORLD-08). Kiểm tra Trung Ấm 30–60 giây có làm người chơi mobile bực không (có thể skip sau lần đầu). Đánh giá Tiền Kiếp Ấn (không bán) có xung đột với skin không. Thiết kế UI hiển thị "Cảnh N · tên riêng". Thông báo world event cho người chơi 15 phút. Cần PX quyết định thứ tự platform để tôi biết có cần cân nhắc màn hình nhỏ khi làm wayfinding không.
- **Tất cả:** đồng thuận rằng **server reset = Đại Kiếp** (sự kiện câu chuyện) chứ không phải wipe vô cảm.

## 5. Rủi ro tự nhận diện
1. **Lore quá dày.** Đã giới hạn ở 4 sự thật + 9 Mảnh Mộng + ~12 NPC. Tổng authored text ước **~12.000–15.000 từ** cho toàn game; MVP chỉ cần ~4.000.
2. **Diễn thế tile và vết tích tốn hiệu năng/lưu trữ** trên Web/Mobile. Phương án dự phòng: diễn thế theo *chunk* 8×8 thay vì từng tile.
3. **Tâm Ma Kiếp sinh từ dữ liệu có thể khó cân bằng** (người giết nhiều thì tâm ma khó hơn, tức bị phạt kép). Cần giới hạn trên, và PROG cân bằng sao cho Sát vẫn khả thi chứ không bị coi là "đạo sai".
4. **Thiên Phạt có thể bị lạm dụng** (người mới cố tình khiêu khích để lừa người mạnh nhận nghiệp). Cần quy tắc: ai đánh trước thì người kia không nhận Nghiệp Lực.
5. **Vạn Linh Minh Ước (E5) làm loãng PvP tự do.** Nó là tùy chọn và chỉ có trong sự kiện; PX/SURV có thể muốn bỏ hẳn.
6. **10 ý tưởng thực vật quá nhiều cho 1 người.** MVP chỉ nên lấy 4, còn lại để roadmap.
7. **Tên Hán-Việt khó với người chơi quốc tế.** Cần bản dịch nghĩa (vd "Ngưng Tâm Mộc — Heartwood Core"). Localization là chi phí thật.

## 6. Câu hỏi mở
1. Chơi được **loài chim (Vũ Tộc)** lúc ra mắt không, hay chỉ NPC? Bay trong top-down làm vỡ thiết kế vòng ngoài→trong.
2. **Thần cai quản Thần Vực có còn "chơi" như sinh vật** (bị giết, hạ bệ) hay trở thành vai trò quản lý? Tôi nghiêng về: thần vẫn là sinh vật, nhưng sức mạnh gắn với sinh khí Thần Vực. Có thể bị **"Thí Thần"** bởi party.
3. Map **hand-made hay procedural**? Tôi đề xuất: layout vòng và vị trí Linh Nhãn, Linh Mạch cố định (authored); biome trong vòng thì procedural theo seed mỗi Kiếp.
4. Người chơi **có thấy Nhân Tu là người** (chi tiết) hay chỉ bóng dáng? Tôi nghiêng về bóng dáng và dấu vết: rẻ hơn, đáng sợ hơn, giữ bí ẩn hồi 2.
5. Đại Kiếp reset **cả 3 cấp rừng cùng lúc** hay chỉ Cổ Đại? Tôi đề xuất reset cùng lúc để cả server cùng trải qua khoảnh khắc này, nhưng PX cần cân nhắc người chơi mới vào giữa mùa.
