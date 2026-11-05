# R1 Proposal — PX (Ngũ Tộc redefine, đã cập nhật theo "BỔ SUNG CỦA NGƯỜI DÙNG")

## 1. Cách tôi hiểu yêu cầu
Tộc = loài sinh vật (Mộc: cỏ+cây · Thú: nhỏ→lớn · Trùng: kiến, bướm, ong · Thủy: cá + loài nước ngọt · Vũ: chim, gà). MVP = **5 tộc × đúng 1 nhân vật chơi được**, "chưa sâu"; mỗi tộc một thế mạnh riêng; ma trận 5×5 tương sinh/khắc/bổ trợ/cộng sinh. Giả định của PX: (a) đệm 4,25 tuần là mức tối thiểu, mọi thứ thêm phải kèm cắt; (b) "chưa sâu" = **C1–C2** cho 3 tộc mới (xem §3 PX-04); (c) chức năng hệ thống của Khuẩn (phân giải, Linh Quỹ, Sổ Sinh Năng) là luật rừng, không cần tộc.

## 2. Hook
*"Năm tộc, năm cách sống, một vòng ăn-và-bị-ăn: nước nuôi cây, cây nuôi thú, thú nuôi bầy, bầy nuôi chim, chim nuôi nước."* Hook store: *"Làm cổ thụ, sói, kiến, ếch hay gà rừng tu tiên."*

## 3. Đề xuất

### PX-01: Năm đại diện MVP
| Tộc | Đại diện | Độ sâu MVP | Chi phí (tuần-người) |
|---|---|---|---|
| Mộc | **Linh Mộc** | Đầy đủ C1–C4 (giữ nguyên v1.0) | đã có |
| Thú | **Lang** | Đầy đủ C1–C4 | đã có |
| Trùng | **Kiến Linh** (kiến + bầy VFX đi theo; dùng chung hạ tầng swarm với Kiến lite) | Lite C1–C2 | 0,5 |
| Thủy | **Thanh Oa** (ếch, tên tạm; lưỡng cư nên không bị nhốt trong nước) | Lite C1–C2 | 0,6 |
| Vũ | **Kê / Trĩ Linh** (gà rừng chạy + **Phi Lược** nhảy/lướt ngắn, không bay thật) | Lite C1–C2 | 0,55 |
- **Chọn Lang cho Thú** vì P2 cần kẻ săn và Thú tộc cần "cơ động + burst". **Linh Thử hạ xuống "Tiền Thân FTUE" + AI** (giữ "chuột mang hạt", mốc fun #2). Giá phải trả: mất Tàng Thử/Độn Thử và đối tác Quả Ước của người chơi cây (Linh Thử AI thay). Căn Thương chuyển cho Trùng (PX-03).
- **Lite C1–C2:** 2 Bản Năng (Bản Năng 1, 2), không Huyết Mạch, không Ngộ Đạo draft riêng, không Phi Thăng. Ngân sách skill vẫn 18 (Linh Mộc 6 + Lang 6 + 3×2). Chạm đỉnh C2 Hậu thì UI: *"Con đường chưa mở. Luân Hồi để đi tiếp"* (Hồi Ức ×4 giữ tốc độ). Đạo Quả từ lite ≤ ~39.

### PX-02: Thế mạnh riêng (không tộc nào thay được)
| Tộc | Vai độc quyền | Đo được |
|---|---|---|
| Mộc | Lãnh thổ, sản xuất, bất tử khi offline | Duy nhất có ô rễ + Mộng Báo |
| Thú | Cơ động + burst săn | Tốc cao nhất, TTK thấp nhất (7,5s Lang vs Lang) |
| Trùng | **Bầy + duy nhất phá Tâm Rễ** (Căn Thương 0,5%/s mỗi Kiến, tối đa 3), thay Độn Thử | Giết thật cây cần Trùng, nên cây không còn "bất khả diệt" nhưng cần đồng minh |
| Thủy | Hồi phục + chủ nước: tốc ×1,3 và hồi 1,5%HP/5s trong nước nông; +10% hồi Linh Quỹ vùng nước | Ở bờ nước khó bị đuổi bắt |
| Vũ | Trinh sát: Thần Thức +50%, Phi Lược vượt bụi/hang 3 ô (CD 12s, tốn Thể Lực), ping cho party | Biết trước mọi sự kiện, thoát hiểm ngắn |

### PX-03: Ma trận 5×5 (skeleton, SURV/PROG chỉnh số)
Vòng **sinh**: Thủy → Mộc → Thú → Trùng → Vũ → Thủy. Vòng **khắc** (cách một): Thủy → Thú, Mộc → Trùng, Thú → Vũ, Trùng → Thủy, Vũ → Mộc. Mỗi cặp 10 cặp không thứ tự rơi đúng 1 vào sinh hoặc khắc, nên mỗi tộc có 1 nguồn nuôi, 1 người được nuôi, 1 con mồi khắc, 1 kẻ khắc mình: **không tộc nào thống trị**.

| Cặp | Chiều xuôi (hiệu ứng) | Chiều ngược (cộng sinh/bổ trợ) |
|---|---|---|
| Thủy→Mộc (sinh) | Cây trong 3 ô Thủy: +2 Thủy/phút | Thủy trong bóng Tán: Thể Lực hồi +15% |
| Mộc→Thú (sinh) | Quả Ước +15 No (đã có) | Thú mang hạt: cây nhận phát tán (đã có) |
| Thú→Trùng (sinh) | Trùng hấp thu xác do Thú để lại +50% phần "Kẻ ăn" | Trùng dọn xác nhanh ×1,5, +1% Linh Quỹ |
| Trùng→Vũ (sinh) | Vũ ăn Trùng +10 No | Vũ trong 6 ô cây giảm đẻ Bầy sâu |
| Vũ→Thủy (sinh) | Thủy trong 6 ô Vũ: +30% Thần Thức | Thủy: ping Vũ thấy xác trong nước |
| Thủy⊣Thú (khắc) | ×1,15 khi cả hai trong nước; Thú lội chậm ×0,8 | Thú ăn cá +12 No ở bờ |
| Mộc⊣Trùng (khắc) | Gai/Độc ×1,15 lên Trùng | **Khế ước cộng sinh Kiến lite** biến khắc thành bổ trợ (đã có trong MVP) |
| Thú⊣Vũ (khắc) | ×1,15 khi Vũ trên đất; Vũ hạ cánh lộ vị trí 2s | — |
| Trùng⊣Thủy (khắc) | ×1,15; bầy trong 4 ô làm Thủy hồi −20% | — |
| Vũ⊣Mộc (khắc) | Mổ Tán ×1,15, Quả Ước bị tha không nhận hạt | Hiện chỉ cây với Quả Ước giữ vai cộng sinh [1.0] |
- Hệ số khắc nằm **trong trần** cộng dồn ×1,32 (stress-test §6.5), không chồng lên Huyết Mạch E.
- Chi phí 0,4 tuần: 10 hệ số dạng data, icon ▲▼ trên vòng dưới chân (mở rộng UX hiện có). Không thêm động từ.
- **Scope risk:** chỉ cặp Mộc–Trùng–Thú có cộng sinh thật ở MVP. 7 cặp còn lại chỉ có hệ số. Khế ước cho các cặp khác: [1.0].

### PX-04: Ngân sách MVP làm lại
**Cộng thêm:** 3 đại diện lite 1,65 · nước nông + cá/ếch AI 0,35 · ma trận 0,4 · tên cảnh giới/lore 5 tộc 0,2 · QA/sim cân bằng 5 loài 0,3 = **+2,9**.
**Cắt bù:** Linh Thử đầy đủ → FTUE+AI −0,5 · 4 palette mùa → 2 −0,2 · Hóa Hình Mộng −0,25 · shop 6 → 4 skin −0,2 · Linh Tức vi mô chỉ ở FTUE/Linh Triều −0,2 · pool Trung Ấm 60→40 câu −0,1 = **−1,45**.
**Ròng +1,45 → 47,2 tuần-người, đệm 2,8 (5,6%).** Dưới ngưỡng 8,5% của v1.0, **SCOPE RISK RẤT CAO**.
Nếu Tier lite lên C1–C3 thì +0,75 (đệm 2,05, 4,1%). **Không khuyến nghị.**

**Fallback có cổng (thay §16.1):**
1. **Cổng tuần 16:** Vertical Slice chỉ gồm Linh Mộc, Linh Thử FTUE, Lang AI + 2 client PvP (không đụng 3 tộc mới). Trễ >1 tuần: hoãn **Kê** sang đợt 2.
2. **Cổng tuần 30:** trễ >2 tuần: **ra mắt theo đợt** (xem 3). Cắt tiếp: Kế hoạch Sinh Trưởng, Linh Quỹ → mật độ tĩnh, Linh Thức chỉ do thám.
3. **Đợt:** soft launch tuần 45 gồm Mộc, Thú, Trùng, Thủy (4 tộc). **Vũ vào đợt 2 (tuần 49–52)** như event "Vũ Tộc Giáng Lâm", tận dụng làm marketing.
4. Phương án cuối: Thủy/Vũ chỉ là AI + NPC ở MVP, playable ở U1 (kế hoạch R1 ban đầu của tôi).
- **Không bao giờ cắt:** Linh Mộc, Lang, luân hồi, độ kiếp C3, PvP Rừng chung, FTUE, **ít nhất 4/5 tộc chơi được**.

### PX-05: Khuẩn đi đâu
Phân giải/Linh Quỹ/Sổ Sinh Năng là luật rừng ("rễ/nấm" → "rễ/cỏ", "cây-nấm" → "cây/cỏ" trong §5.5, §5.7). Nấm = prop môi trường, không tộc, không chơi được. Bỏ loài Khuẩn, cộng sinh Nấm, E7 Bào Tử Triều bản nấm (đổi tên *Mưa Vong* dùng hệ mưa có sẵn, WORLD chốt tên). Luân hồi → **Thủy Tộc**, NPC **Lão Quy** (rùa già) thay Bà Khuẩn: Trung Ấm bên mặt nước, xác chìm, nước đổi màu theo Linh Quỹ, giữ câu *"Ngươi đã mang nó cả đời. Giờ nó mang ngươi."* Vòng nấm tiên → **Ao Sương lúc bình minh** mở Mộng Ấn 1 (chi phí 0). "Luân Hồi Thần" §6.2 thành Thủy Thần, Ngũ Hành Thần Vị Thủy ở Đầm Mục khớp, chỉ khai thác ở [Post].

### PX-06: Vũ và bay
Quạ Già (Sứ giả), Quạ Linh, Diều hâu AI gắn nhãn Vũ, chi phí 0. Kê không bay nên không phá cân bằng. Bay thật (Ưng) **[Post]** với luật: tốn Thể Lực, không ăn/đánh khi bay, hạ cánh CD 2s lộ vị trí, không qua Giới Bia. Rủi ro bay trên mobile (tầm nhìn, hit detection) hoãn tới đó.

### PX-07: Mộc gộp cỏ
Linh Mộc là đại diện MVP. **Linh Thảo vẫn là loài thứ hai của Mộc, dời [1.0] → [Post]** (nhường slot Khuẩn cho việc đào sâu 3 tộc lite). Cỏ nền là tile, không tính tải Linh Quỹ. Đổi tên vật phẩm "Linh Thảo" → **"Dược Thảo"**, FTUE 0:40 "hạt linh thảo" → "hạt phát sáng".

### PX-08: Roadmap loài (thay §4.1)
| Nhãn | Nội dung |
|---|---|
| MVP | Linh Mộc, Lang (C1–C4) · Kiến Linh, Thanh Oa, Kê (C1–C2) |
| U1 | Đào sâu 3 tộc lite lên C3 + 1 Huyết Mạch mỗi loài (thay phần mở rộng Linh Thử) |
| 1.0 | Lite → C4 + 2 Huyết Mạch; Khế ước cộng sinh cho 3 cặp tiếp; Linh Thử trở lại chơi được (**Could**) |
| Post | Linh Thảo (Mộc) · Lý cá chép "Vũ Môn" (Thủy) · Ưng (Vũ bay) · Lộc, Ong/Bướm (Thú, Trùng) · iOS |
**Scope risk U1/1.0:** đào sâu 3 loài ≈ 1,5 tuần/loài cho mỗi lần; thay vào đó giữ Pass/Android. Chốt bằng KPI D7 và khảo sát loài.

### PX-09: Persona, skin, Pass
- Lang → P2. Kiến Linh và Oa → P3 + P1 (co-op, cozy). Kê → P1 (meme "gà tu tiên"). Cá chép/Ưng hứa hẹn là drawcard đợt sau.
- Loài **không bán bằng tiền** (mở bằng Đạo Quả/Duyên). Shop MVP 4 skin (1 mỗi tộc ngoài Mộc); Pass [U1] **spotlight 1 tộc mỗi Kỷ Nguyên**. Skin Thủy/Vũ không đổi độ tương phản trên nền nước/trời. Hoa Lộ vẫn là sink duy nhất.

### PX-10: FTUE
- Trung Ấm: Lão Quy, nước, 45s (giữ).
- Phút 15:30 bánh xe loài **5 loài**, Linh Mộc highlight, 3 loài lite gắn nhãn *"Lữ Khách (C1–C2)"*. Rủi ro: 5 lựa chọn quá tải. Phương án: hiện 3 lớn (Linh Mộc, Lang, 1 ngẫu nhiên) + "Xem thêm".
- Trong 25' người chơi chạm đủ 5 tộc (chuột/sói · diều hâu · Lão Tùng · sâu/kiến · Lão Quy). Không thêm beat.

### PX-11: Giả thuyết
| ID | Giả thuyết | Ngưỡng | GĐ |
|---|---|---|---|
| HN1 | Tester gắn Trung Ấm với nước/rùa và luân hồi | ≥60% | VS |
| HN2 | Kể được ≥4/5 tộc sau FTUE | ≥60% | VS/Alpha |
| HN3 | Mỗi tộc chiếm 8–32% lượt chọn khi luân hồi | đạt | Alpha |
| HN4 | Người chơi chạm trần lite (C2 Hậu) và Luân Hồi trong 60s, không thoát game | ≥60% | Alpha |
| HN5 | Hiểu ma trận: giải thích đúng ≥2/5 quan hệ khắc | ≥60% | Alpha |
| HN6 | Không tộc nào có thắng PvP Mid >35% (cùng cảnh) | đạt | Alpha |
| HN7 | Chọn Linh Mộc ở bánh xe 5 loài | ≥45% (từ 50%) | VS |
| HN8 | Nước nông không thành bẫy: chết trên ô nước ≤1,3× trung bình | đạt | Alpha |
| HN9 | Kê: Phi Lược bấm nhầm <5%; thoát thành công ≤55% | đạt | Alpha |

## 4. Kết nối domain khác
SURV: số ma trận, nước nông (terrain modifier, không nút), Trùng nhận Căn Thương. PROG: sim 5 loài, trần ×1,32, cap C2 Hậu của lite, Đạo Quả lite. WORLD: Lão Quy, tên cảnh giới Oa/Kiến/Kê (cột Khuẩn §6.2 thay bằng 3 cột), lore nước, Mưa Vong.

## 5. Rủi ro
| Rủi ro | KN | TĐ | Giảm thiểu |
|---|---|---|---|
| Đệm còn 5,6% | Rất cao | Rất cao | Cổng 16/30, ra mắt theo đợt |
| Lite chạm trần nhanh (2–3 phiên Mid), cảm giác "demo" | Cao | Cao | Nhãn "Lữ Khách", Hồi Ức ×4, đo HN4 |
| Cân bằng PvP 5 tộc × 5 tộc | Cao | Cao | Chỉ hệ số khắc nhỏ, trần ×1,32 |
| Nhầm Tộc với Hành (Thủy tộc/hành Thủy) | Cao | Thấp | UI khác màu, tộc không có hệ số E |
| Cây mất "bất khả diệt" do Trùng | TB | TB | Cần ≥2 tộc phối hợp (Lang+Kiến) |
| Tôi cắt quá tay Linh Thử, Hóa Hình Mộng | TB | TB | Linh Thử giữ ở FTUE, Hóa Hình Mộng về U1 |
| Hứa hẹn loài sau trên store | Cao | Cao | Chỉ nói "Ngũ Tộc", ghi lộ trình |

## 6. Câu hỏi mở
1. Chấp nhận đệm 5,6% + đợt 2 cho Vũ, hay lùi soft launch 4 tuần?
2. Hóa Hình Mộng (nếm trước Hóa Hình) cắt khỏi MVP có chấp nhận được không (WORLD)?
3. Linh Thử chỉ ở FTUE: SURV có chấp nhận mất Độn Thử/Tàng Thử?

## Mục FINAL bị đổi
§0 (TL;DR 1, 5), §2.4 (vòng nấm tiên), §2.7, §3 (không đổi), §4.1–4.2, §4.3 (Hóa Hình Mộng, Căn Thương), §4.5 (mở rộng ma trận), §5.5, §5.6, §5.7, §5.8, §6.2, §6.4–6.5 (Huyết Mạch Linh Thử), §7.2, §10 (E7), §12 (bánh xe loài, 0:40, 14:00), §14.2, §16.1–16.4, §17.1–17.2, §18, §19 (D6, D12 liên quan), §20.2 (Q2).
