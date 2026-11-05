# R6 Sign-off — WORLD
**Verdict:** BLOCK (3 blocker, cả ba chỉ cần sửa chữ, chi phí sản xuất 0 tuần. Sửa xong là APPROVE-WITH-NOTES)

> Phạm vi rà soát: §1.1–1.2, §2, §5.8 (tên archetype), §6.1–6.2, §7.2, §9, §10, §12, §18, §19 (D2, D3, D11, D17), đối chiếu với r3-revision-world.md và r4-position-world.md. Đã grep toàn bộ FINAL tìm "Đạo Tâm", "Đại Kiếp", "Linh Lâm", "Trung Kiếp", "Cửu Cảnh", "Hộ Thể".
> Kết luận chung: phần lớn domain WORLD được tổng hợp đúng. Bộ tên 7 cảnh A′, Tâm Hướng/Đạo Quả, lịch C3-A, Thâm Lâm, Công Đức = Thần Cách, không có bảng kill, Đại Kiếp theo lịch cố định đều đúng ý. Ba blocker dưới đây là mâu thuẫn logic nội tại. Cả ba đều sinh ra khi gộp nhãn scope (MVP/U1/1.0), không phải do bất đồng thiết kế.

---

## Blockers

| # | Vị trí trong FINAL | Vấn đề | Sửa cụ thể (đoạn thay thế viết sẵn) |
|---|---|---|---|
| **B1** | §9.2 gạch đầu dòng "Thần Bia lite" · §10 E8 · §1.2 P4 · §16.4 U1 | **Thần Bia vừa là MVP vừa là U1.** E8 (MVP) ghi "Thần Bia hiện tên", P4 dùng Thần Bia làm cơ chế MVP. Nhưng §9.2 xếp "Thần Bia lite" vào U1, và bảng Hộ Lâm cần Công Đức, mà Công Đức là U1. Dev làm MVP sẽ không biết cao trào Đại Kiếp lite khắc tên ai. **Thêm một lỗ logic:** bảng Trường Sinh ("kiếp sống lâu nhất") đang tính theo thời gian thực. Cây khi offline bất tử và Tâm Rễ không bao giờ teo (§5.9), nên một cây đăng nhập 1 lần rồi Bế Quan 28 ngày sẽ thắng Trường Sinh mặc định. Bảng này thưởng cho việc *không chơi* | **Thay gạch đầu dòng Thần Bia ở §9.2 bằng:** "**Thần Bia** khắc tên ở cao trào mỗi Đại Kiếp. **[MVP]** 2 bảng, dùng dữ liệu Biên Niên đã có, không cần hệ mới: **Đỉnh Cảnh** (3 người đầu tiên của mỗi loài đạt C4 Hậu trong phòng) · **Trường Sinh** (kiếp có **thời gian online sống sót** dài nhất. Giờ AFK ×0, giờ offline/Bế Quan không tính). **[U1]** thêm bảng **Hộ Lâm** (top Công Đức). **Không có bảng số kill.**" · **§16.4 U1:** "Công Đức + Thần Bia lite" → "Công Đức + bảng Hộ Lâm trên Thần Bia". · Chi phí: nằm trong mục #17 (Đại Kiếp lite) |
| **B2** | §2.5 đoạn "Timeline bản đầy đủ" + "Rừng Non xoay vòng" · §16.1 #14 | **Hai luật lịch đá nhau.** (a) Timeline ghi một ngày "ngày 28 Kỷ Chuyển" chung, nhưng PROG-16 mở phòng Hạ Lâm mới mỗi 14 ngày và mỗi phòng sống 28 ngày, nên không có một ngày Kỷ Chuyển chung. (b) Phòng mở ngày 43 sẽ sống tới ngày 71, vượt qua Đại Kiếp "theo lịch cố định" ở ngày 56 (D11). (c) Ở MVP (Đại Kiếp = 28 ngày), FINAL không nói việc xoay vòng có áp dụng không, và Đại Kiếp là của từng phòng hay toàn server. Hai cách hiểu cho ra hai kiến trúc khác nhau cho mục #14 (4 tuần-người). Nếu hiểu là toàn server mà không xoay vòng, người vào ngày 20 bị reset sau 8 ngày, đúng lỗi Casual mà PX đã bác ở R3 | **Thay đoạn "Rừng Non xoay vòng" ở §2.5 bằng:** "**Luật phòng Hạ Lâm** *(PROG-16, WORLD R6)*: **[MVP/U1]** (Đại Kiếp = 28 ngày) mỗi phòng Hạ Lâm có **đồng hồ Đại Kiếp riêng**, tính từ ngày mở phòng. Cứ 14 ngày mở một phòng mới. Phòng sống đúng 28 ngày rồi kết thúc bằng Đại Kiếp lite của chính nó (Thần Bia và Biên Niên theo phòng). Người mới luôn vào phòng ≤14 ngày tuổi. Lịch năm-rừng (mùa, sự kiện tuần) là đồng hồ chung của khu vực, không theo phòng. Pass [U1] tính theo tài khoản. Khi CCU khu vực dưới ngưỡng thì không mở phòng mới (PX chốt ngưỡng). **[1.0+]** (Đại Kiếp = 56 ngày, toàn server, lịch cố định) phòng Hạ Lâm mở ở ngày 1 / 15 / 29 / 43 của chu kỳ. **Tuổi thọ phòng = min(28 ngày, số ngày còn tới Đại Kiếp).** Khi một phòng đóng (**Kỷ Chuyển của phòng**), cư dân C≤3 sang phòng mới nhất và giữ nhân vật, còn C4+ đã ở Linh Lâm. Ngày 56, Đại Kiếp đóng mọi phòng." · **Trong timeline:** "ngày 28 Kỷ Chuyển (phòng Hạ Lâm mới, giữ nhân vật)" → "ngày 28 Kỷ Chuyển của phòng đầu tiên (cư dân C≤3 sang phòng ngày 29, giữ nhân vật)". · **Q4 (miễn reset 7 ngày cuối):** đóng ở MVP, vì luật phòng đã bảo đảm ≥14 ngày sống |
| **B3** | §6.1 hàng C5 · §6.3 "Phiên 18 [U1] Phi Thăng Kiếp II" · §6.6 · §16.4 U1 · §18 "Phi Thăng" | **Phi Thăng Kiếp II ra ở U1 nhưng đích đến không tồn tại.** Glossary: Phi Thăng **chỉ** dùng để chuyển cấp rừng, và Phi Thăng Kiếp II = C5→C6. C6 và Thần Lâm đều là [Post]. Qua kiếp ở U1 thì người chơi lên một cảnh giới không có nội dung, không có map, không có Áp Chế. Ngoài ra hàng C5 ghi cấp rừng "Linh Lâm" kèm nhãn U1, trong khi map Linh Lâm là [1.0]: ở U1, C5 sống ở Thâm Lâm | **Thay ô "Cấp rừng" của hàng C5 (§6.1) bằng:** "Thâm Lâm (U1) → Linh Lâm (1.0)". **Thêm dưới bảng §6.6:** "**Phi Thăng Kiếp II trước khi có Thần Lâm** [U1–1.0]: qua kiếp thì nhân vật đạt **C5 · Viên Mãn** (tên tầng thứ 4 đã dự phòng ở §6.2). Đây là cờ trạng thái: **không thêm chỉ số** (n giữ 15), sprite có Phi Thăng Tử treo trên tán/lưng, Biên Niên ghi "Đã kết Phi Thăng Tử, chờ gió Thần Lâm". Đại Kiếp vẫn nhân Đạo Quả ×1,5 như §7.1. Khi [Post] mở Thần Lâm, nhân vật Viên Mãn vào thẳng C6 Sơ kỳ mà không phải độ kiếp lại." · **§18 dòng Phi Thăng:** thêm "Trước [Post], Phi Thăng Kiếp II dừng ở C5 · Viên Mãn" |

---

## Notes (không chặn)

### N-A. Các chỗ [orch] liên quan đến WORLD

| [orch] | Đánh giá | Ghi chú / đoạn bổ sung |
|---|---|---|
| §2.2 / D17: vòng lõi tên **Thâm Lâm** | **Đồng ý.** Đã kiểm: mọi chỗ còn lại (§2.3, §3, §5.6, §5.8, §6.1, §8) đều dùng Thâm Lâm cho vòng lõi và Linh Lâm cho cấp rừng 2. Không còn sót | Nên làm rõ Giới Bia là **ranh mềm hay cửa cứng**. §2.2 ghi "sương rẽ ra" khi Phá Giới, nghe như C≤3 không vào được, nhưng Mộng Ấn 3 (Đầm Mục) và dấu vết Nhân Tu nằm ở Thâm Lâm. Đề xuất: "Giới Bia là **ranh mềm**: C≤3 đi qua được, nhưng sương che tầm nhìn còn 50% Thần Thức và không có Áp Chế bảo vệ. Phá Giới xóa sương vĩnh viễn cho người đó." Như vậy Mộng Ấn 3 vẫn tới được trước C4 (một mục tiêu liều lĩnh có chủ đích), còn Phá Giới vẫn là phần thưởng thấy được |
| §2.3: 3 biome là **palette + props trên 1 tileset** | **Đồng ý, kèm 3 điều kiện** để biome vẫn có danh tính *gameplay* chứ không chỉ là màu: (1) mỗi biome có một **tham số mật độ che phủ** (bụi/cỏ cao) và **tỉ lệ ô ẩm** riêng, tái dùng hệ ô sẵn có. Đầm Mục ẩm dày nên dễ nuôi Thủy nhưng khó trốn. (2) Tile mang **biome tag** (Đầm Mục cần nó cho luật "xác phân giải nhanh hơn", Thần Vực [Post] cũng cần). (3) Ba prop authored độc nhất phải nằm trong ngân sách #11: **vòng nấm tiên, Lão Tùng, Liễu Chết** (+ bộ dấu vết Nhân Tu). Thêm nữa: §2.2 ghi "biome trong vòng sinh procedural theo seed" mâu thuẫn nhẹ với §2.3 (1 biome cố định/vòng). Đề xuất: "MVP: biome cố định theo vòng, chỉ bố trí props/ô ẩm là procedural. Trộn biome theo seed từ [1.0] khi có ≥4 biome." **Lão Tùng đặt cố định** ở ranh Bìa–Trung Lâm, cùng vị trí với FTUE: người chơi bước vào Rừng chung và *nhận ra* cái cây đã gọi mình dậy (show, don't tell, chi phí 0) |
| §5.8: diều hâu và sói AI là **skin của archetype kẻ săn** | **Đồng ý.** Ở FTUE, diều hâu chỉ là bóng lướt qua theo script, nên không cần state machine bay. Cần 1 luật để không lẫn với người chơi: "Skin sói AI **chỉ dùng trong FTUE local**. Ở Rừng chung, mọi con sói đều là người chơi Lang hoặc Linh Ảnh (có vòng cảnh giới dưới chân). Kẻ săn AI ở Rừng chung chỉ dùng skin Báo Bóng Đêm / Huyết Báo." Như vậy vòng cảnh giới vẫn là tín hiệu đọc PvP tin được (§8 UX) |

### N-B. Nhất quán thuật ngữ (D2 và luật "một khái niệm, một tên")
**Đã đạt:** "Đạo Tâm" chỉ còn xuất hiện trong flavor (chữ thường), mục Bị loại, Dissent và Q1. "Đại Kiếp" không còn dùng cho đột phá (S1 "chặt ở Đại Kiếp trước" là đúng nghĩa reset). Chuỗi kiếp Tiểu / Phi Thăng I / Trung (C4→5) / Phi Thăng II / Thiên nhất quán ở §3, §6.1, §6.6, §18. Tâm Hướng nhất quán ở §2.7, §6.6, §7.2, §9.1. Không còn "Cửu Cảnh", "Hộ Thể", "Linh giới".

**Còn va chạm, nên sửa trước khi khóa tài liệu:**

| Va chạm | Vị trí | Sửa |
|---|---|---|
| **"Linh Thảo"** đang mang 3 nghĩa: loài [1.0] (§4.1), Thiên Tài Địa Bảo (§5.6), "hạt linh thảo" trong FTUE (§12) | §5.6, §12 | Thiên Tài Địa Bảo → **Linh Chi** (Trung Lâm, 1/vùng/ngày-rừng). FTUE → "ăn **hạt linh cốc** phát sáng". Linh Thảo chỉ còn là tên loài |
| **"Nghịch Thiên"** vừa là luật Thiên Đạo (g≤0) vừa là achievement FTUE | §12 phút 12–14 | Đổi tên achievement thành **"Thoát Nanh"** |
| **"Linh Quang"** vừa là vật nhặt (§5.3, E1) vừa là Cột Linh Quang (wayfinding), lại gần tên đã bị loại "Linh Quang Hộ Thể" | §5.3, §10 E1 | Vật nhặt → **Linh Châu**. "Linh Quang" chỉ dùng cho Cột Linh Quang |
| **"Mảnh Mộng"** và **"Mộng Ấn"** | §2.1 bí mật (1) ghi "Mảnh Mộng 3", §2.4 ghi "Mộng Ấn 3" | §2.1 → "**Mộng Ấn 3**". Mảnh Mộng là phần thưởng của Mộng Cảnh [1.0], thêm vào glossary |
| **"Linh Triều"** và **"Đại Linh Triều"** dùng lẫn | §2.3, §2.4, §6.8 Gia Trì | Thống nhất là **Đại Linh Triều** (sự kiện tuần). Glossary ghi "Linh Triều = cách gọi tắt trên UI" nếu cần |
| **"Linh Thổ"** (FTUE lựa chọn B) chưa có định nghĩa | §12 | → "**Dưỡng Chất +30%** khi bắt đầu kiếp cây" |
| Đạo hiệu mẫu **"Thanh Phong Lão Tùng"** trùng tên Lão NPC | §11 | Generator loại trừ tên NPC (Lão Tùng, Bà Khuẩn, Quạ Già). Đổi ví dụ thành *Thanh Phong Tán Nhân* |
| "Hươu AI" / "Hươu Sừng Ngọc" và loài "Lộc" | §4.1, §5.8 | Glossary: "Hươu Sừng Ngọc = Lộc (AI ở MVP)" |
| Glossary §18 **thiếu các thuật ngữ người chơi gặp trong MVP** | §18 | Thêm các dòng: **Mộng Ấn** (vignette tĩnh mở bằng hiểu biết, 3 cái ở MVP) · **Linh Mạch / Linh Nhãn** (rễ cũ của Kiến Mộc / nút tâm map) · **Giới Bia / Cột Linh Quang** · **Mộ Linh · Biên Niên Kiếp · Tiền Kiếp Ấn** · **Linh Hạch** · **Quang Tinh / Dưỡng Chất** · **Cơ Duyên / Thiên Tài Địa Bảo** · **Đại Linh Triều / Linh Tức** · **Thọ Nguyên** (chỉ có ở FTUE) · **Tự Quy** (vé luân hồi chủ động) · **Phá Giới** · **Cổ Thú** (kẻ săn AI cấp boss: Huyết Báo, Cổ Hùng) · **Linh Hóa Địa** (đánh dấu [1.0] nếu chưa có ở MVP) |
| *Rủi ro đọc nhầm:* **Linh Thức** (skill) và **Linh Thử** (loài) chỉ khác dấu | toàn văn | Không đổi ngay. Đưa cặp này vào playtest đọc tên (điều kiện C2 của tôi ở R4). Nếu ≥30% nhầm thì đổi skill thành "Linh Thức Xuất" hoặc dùng icon cố định |

### N-C. Lịch và câu chuyện: các chỗ chưa định nghĩa (domain WORLD)

| Vấn đề | Đoạn thay thế đề xuất |
|---|---|
| Ngày-rừng "12' · hoàng hôn 2' · đêm 6'" **không có bình minh**, trong khi Mộng Ấn 1, sương bình minh (+15 Thủy), E1 "mỗi bình minh" và §2.5 "1 bình minh" đều cần nó | §2.5: "**Ngày-rừng 20'** = bình minh 1' · ngày 11' · hoàng hôn 2' · đêm 6'" |
| Mộng Ấn 3 cần **"đêm trăng tròn"** nhưng lịch không có chu kỳ trăng | Thêm vào §2.5: "**Tuần trăng = 4 ngày-rừng (80')**: non → bán → gần tròn → tròn. Trăng hiện trên bầu trời đêm, không có UI. Phiên 40' có khoảng 50% cơ hội gặp trăng tròn. Huyết Nguyệt [U1] = trăng tròn nhuộm đỏ trong pha Đông." Chi phí: 4 sprite trăng |
| Huyết Nguyệt "ngày 6" chạy 00:00–24:00 thì 6h đầu rơi vào Thu (Đông bắt đầu ở giờ 126 = 06:00 ngày 6) | §10: "Huyết Nguyệt: pha nền **06:00 ngày 6 → 06:00 ngày 7** (trọn trong Đông), cao trào 20:00 ngày 6" |
| Bí mật hồi 1 ("Rừng Non mọc từ một hạt gió từ Thần Lâm, Lão Tùng là cây đầu tiên") **không có kênh truyền tải**: Mộng Ấn 1–3 không chứa nó | Gộp vào văn bản Mộng Ấn 2 (vẫn ~150 từ): *"Kiến Mộc đã ngã. Hạt cuối cùng nó thả bay theo gió tới đây, và ta là cái cây đầu tiên mọc lên."* Chi phí 0 |
| Luật sự kiện số 4 ("mỗi sự kiện có kẻ thắng và kẻ thua") đá với E8 ("không ai thua") | Luật 4: thêm "(trừ E8 Đại Kiếp, là nghi lễ)" |
| §16.4 U1 ghi "biome thứ 2" mơ hồ, vì MVP đã có 3 biome dạng palette | Đề xuất: "U1: **tileset riêng cho Đầm Mục**" (nước, sậy, gỗ mục). Ở U1, Thâm Lâm là nhà của C4–C5 nên người chơi ở đây lâu nhất |

### N-D. Số liệu và nhịp trong domain câu chuyện
- **§7.1 "chết → điều khiển kiếp mới ≤20s"** đá với **Trung Ấm lần đầu 45s** (§7.2, §12). Sửa: "≤20s (trừ Trung Ấm lần đầu 45s, là beat cảm xúc của FTUE)".
- **§12 phút 16–20 "Đột phá Manh Nha"**, trong khi §6.3 ghi C2 ở phút ~29. Manh Nha là tên C1. Sửa: "Đột phá tầng: **Manh Nha · Trung kỳ**".
- **FTUE lựa chọn B** cho chuột chết dưới gốc Lão Tùng, nên cây mọc trong bóng tán Lão Tùng (Ánh Sáng −30% mỗi tán chồng lên, §5.3). Phần thưởng B (+30% Dưỡng Chất) bị phạt ngược ngay ở kiếp cây. Sửa: "Ở FTUE, hạt nảy mầm ở **mép tán** Lão Tùng (Ánh Sáng 100%)". Đề nghị PROG kiểm thêm: FTUE ghi Hồi Ức ×3, còn luật §7.1 là ×4 tới đầu cảnh cũ.
- **§6.1 C1 "2 Bản Năng"** đá với §6.5 / §6.3 (Bản Năng 2 mở ở C2). Đây là việc của PROG, tôi chỉ ghi nhận.
- **§9.1 Tâm Ma:** §6.6 đã đưa Tâm Ma vào Phi Thăng Kiếp I của MVP. Nên ghi rõ "MVP: 1 mẫu chung · mẫu theo Tâm Hướng: U1" để khớp với tiêu đề §9.1.

---

## Ludonarrative audit cuối
Câu hỏi kiểm tra: *cơ chế này nói gì về thế giới, và nó có cùng thông điệp "kẻ mạnh nhất là kẻ nuôi được cả khu rừng" không?*

| Hệ thống | Thông điệp cơ chế | Khớp? | Ghi chú / đề xuất |
|---|---|---|---|
| Sinh Năng 8/4/8, xác trả Linh Quỹ | Cái chết nuôi rừng | ✅ | Lõi P3. Trung Ấm đọc số từ quỹ thật nên lời thoại không nói dối |
| Linh Quỹ / Khô Linh, Bìa có sàn | Tham thì rừng cạn, và hậu quả rơi vào kẻ tham chứ không rơi vào người mới | ✅ | Ở MVP đây là cơ chế **duy nhất** biến theme thành luật. Nhắc lại: cổng tuần 30 có quyền cắt nó (§16.1 fallback 3). Nếu cắt thì MVP không còn luật nào chứng minh theme. Đề nghị cắt nó **sau** Linh Thức-chỉ-do-thám, không phải trước |
| Thiên Đạo Luật: g=1 không Nghiệp, g≥2 không tu vi nhưng ăn vẫn no | Săn để ăn là tự nhiên, bắt nạt là vô ích | ✅ | Rất khớp với cụm "Thực Sát / Lạm Sát" |
| Vòng khắc Ngũ Hành của Huyết Mạch | Tàng Thử (con mồi, nghiêng Sinh) khắc Huyết Lang (kẻ săn, nghiêng Sát). Kẻ giết bị kẻ nuôi khắc chế | ✅ | Đã kiểm vòng tương khắc Hỏa→Kim→Mộc→Thổ→Thủy→Hỏa: đúng |
| Quả Ước, hươu ăn quả thay lá | Cho đi có lợi hơn bị cướp | ✅ | Có cả trong FTUE ở hai góc nhìn (chuột ăn quả, rồi cây bị ăn quả) |
| Thưởng cho loài đang thiếu (+0,25) | Ý Chí Rừng gọi Mộng Hỏa về chỗ rừng thiếu | ✅ | Nên đưa 1 câu này vào pool thoại Bà Khuẩn trong Trung Ấm, chi phí 0 |
| Thần Bia không có bảng kill | Danh tiếng đến từ nuôi rừng | ⚠️ ở MVP | Ở MVP chưa có Hộ Lâm (B1), nên **không bảng nào thưởng cho việc nuôi rừng**. Chấp nhận tới U1, với điều kiện có điểm dưới đây |
| **Biên Niên Kiếp** ("Ăn 41 sinh linh") | Tự động khoe số mồi đã ăn | ⚠️ | Bản chia sẻ ra mạng xã hội đang chỉ đếm "ăn". Luật template (chi phí 0): **mỗi chỉ số "ăn" phải đi kèm một chỉ số "nuôi"** lấy từ sổ Sinh Năng/Linh Quỹ. Ví dụ: *"Ăn 41 sinh linh. Trả 1.280 linh khí về Trung Lâm. 3 hạt ngươi mang đã thành cây."* Đây là chỗ duy nhất ở MVP mà theme "nuôi" được kể ra cho người ngoài game |
| Rewarded ad "Hồi sinh tại chỗ" (Rừng riêng) | Trả tiền (bằng sự chú ý) để **né cái chết**, tức né đúng vòng lặp chủ đề | ⚠️ | Không trái brief, PX là owner. Đề xuất thay bằng **"Mầm Ban"**: 1 lần/ngày, ad cho một Hậu Duệ không cần neo. Người chơi vẫn chết, vẫn xem timelapse "mầm nứt", xác vẫn nuôi rừng, nhưng giữ được tiến độ như hồi sinh. Code dùng chung đường Hậu Duệ |
| Trục **Độc** của Tâm Hướng tăng khi "solo kéo dài" | Ở Rừng riêng (solo), ai cũng bị kéo về Độc, nên la bàn mất nghĩa | ⚠️ | "Solo kéo dài" chỉ tính ở Rừng chung. Ở Rừng riêng, trục Hợp/Độc chỉ đọc từ hành vi với Linh Ảnh đồng hành |
| Bảng Trường Sinh tính theo thời gian thực | Thưởng cho việc không chơi | ❌ | Đã đưa vào B1 |
| Đỉnh Cảnh (người đầu tiên đạt C4) | Thưởng cho tốc độ | Trung tính | Chấp nhận, vì đó là fantasy tiên hiệp "đột phá trước thiên hạ" |
| Hóa Hình Mộng trong Đại Linh Triều | Cây "mơ" thành hình, đúng S3 (ý thức là mộng) | ✅ | — |

---

## Nhất quán số liệu (tùy chọn, chỉ trong domain lịch và thế giới)
- 4 × 42h = 168h = 7 ngày ✓ · 42h = 126 ngày-rừng ✓ · Kỷ Nguyên 28 = 4 năm ✓ · Đại Kiếp 56 = 8 năm = 2 Kỷ ✓ · 42 mod 24 = 18h trôi mỗi mùa ✓.
- Ngày-rừng 20' và Thiên Phạt "1 ngày-rừng (20')" ✓ · Mộ Linh 1 năm-rừng = 7 ngày ✓.
- Lịch tuần: Đại Linh Triều ngày 1 nằm trong Xuân (giờ 0–42) ✓ · Đại Hạn ngày 3 (giờ 48–72) nằm trong Hạ (42–84) ✓ · Huyết Nguyệt ngày 6 lệch 6h sang Thu (xem N-C).
- Thần Vị: mở ngày 22, nhiệm kỳ 14 ngày, đến ngày 56 được khoảng 2,4 nhiệm kỳ × 5 ghế ≈ 12 thần ✓.
- Áp Chế n=9 = C3 Hậu ✓, n=15 = C5 Hậu ✓. Map 256²/384²/512² ✓. Bonus vòng +0/+0,15/+0,3/+0,5 khớp giữa §2.3 và §6.8 ✓.
- Chi phí lore: MVP 4.000 từ ở §2.1 khớp với mục #20 ở §16.1 ✓.

---

## Dissent ghi nhận
- **D6 (giữ nguyên dissent R4):** tôi vẫn nghiêng về D (bỏ Kiến). Chấp nhận B′ vì đã có cổng tuần 16 để quay về D.
- **Thứ tự cắt ở cổng tuần 30** (§16.1): tôi không đồng ý cắt Linh Quỹ (3) trước Linh Thức-chỉ-do-thám (4). Lý do: Linh Quỹ là luật theme duy nhất của MVP, còn Linh Thức lúc đó vẫn được giữ bản do thám. Đề xuất đảo thứ tự (4) và (3). Không BLOCK vì đây là quyền của owner scope (PX).
- **Rewarded ad hồi sinh ở Rừng riêng:** dissent nhẹ, đã có phương án thay thế "Mầm Ban" ở bảng audit. PX quyết.
