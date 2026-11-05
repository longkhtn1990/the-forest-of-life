# R1 Proposal — SURV (bản 2, đã khớp "BỔ SUNG CỦA NGƯỜI DÙNG")

## 1. Cách tôi hiểu yêu cầu
Ngũ Tộc = 5 nhóm sinh vật, **mỗi tộc có một vai không tộc nào thay được**, nối nhau bằng vòng tương sinh/tương khắc/bổ trợ/cộng sinh. MVP = **5 tộc × 1 nhân vật chơi được**, chưa sâu. Chức năng Khuẩn cũ (phân giải, giữ luân hồi) tách ra: phân giải là **quy trình môi trường**, luân hồi là **lore của nước**. Giả định: không thêm need nào (Thú vẫn không Khát), không thêm AI archetype ở MVP.

## 2. Hook
**Năm vai, một vòng tròn, không ai đứng ngoài.** Mộc nuôi, Thú săn, Trùng chở và dọn, Thủy chữa và chia nước, Vũ thấy xa và vượt địa hình. Nước là nơi rừng nhớ: Linh Mạch là mạch nước của rễ Kiến Mộc.

## 3. Đề xuất

### SURV-01: Năm vai (thế mạnh) và nhân vật MVP
| Tộc | Hành Tượng | **Vai độc nhất** | Điểm yếu | **Nhân vật MVP** | Thay gì |
|---|---|---|---|---|---|
| **Mộc** | Mộc | Lãnh thổ, sản xuất (Dưỡng Chất, Quả, Neo), phòng thủ bất động | Bất động, chậm | **Linh Mộc** (đã có) | Linh Thảo → [1.0], cùng tộc |
| **Thú** | Kim | Sát thương và đuổi bắt trên đất liền | Cần ăn đều, Linh Quỹ hạn chế | **Lang** | **Linh Thử → AI**; xem SURV-02 |
| **Trùng** | Thổ | **Bầy + chuyên chở + chui**: Tha Mầm/thịt/hạt, mở xác, chui lỗ nhỏ | HP thấp, bầy tan thì yếu | **Linh Nghĩ** (kiến) | dùng lại swarm của Kiến lite |
| **Thủy** | Thủy | **Hồi phục + chia nước**: tưới cây, hồi máu đồng đội, chạy xuống nước sâu thì bộ săn đất liền không theo | Chậm trên cạn (3,5 ô/s), cần nước | **Linh Quy** (rùa) | thay chỗ Khuẩn [1.0] |
| **Vũ** | Hỏa | **Cơ động địa hình + tầm nhìn**: lướt qua nước sâu, rễ, bụi gai; lao từ trên xuống | HP thấp, lướt tốn Thể Lực | **Linh Trĩ** (gà rừng linh; lướt 2,5s, CD 10s, 40 Thể Lực, **không đánh/ăn khi lướt**) | [Won't] → MVP lite |
- **Vì sao Trĩ chứ không phải đại bàng:** bay thật phá top-down và "trốn là lựa chọn". Lướt ngắn thì giữ được cả hai. Bay thật là Hóa Hình C5+ [Post].
- **Needs 3 loài mới** (cùng khung No/Thể Lực): No decay Nghĩ −5/phút (warning đầu **8,2'**) · Trĩ −4,5 (**9,1'**) · Quy −3 (**13,7'**). Đều trong mục tiêu 8–15'.
- Một **controller mặt đất chung** (Lang) cho Lang, Nghĩ, Quy, Trĩ; chỉ khác thông số và 2–3 skill. Linh Mộc vẫn riêng.

### SURV-02: Linh Thử → AI + Tiền Thân FTUE
- Linh Thử vẫn là **mồi AI** và **Tiền Thân kịch bản** ở FTUE (C1, 12', ăn hạt, ngậm hạt, né diều, chết). Dùng chung controller Thú, đã cắt Kho Hạt/đào hang, chỉ giữ "ngậm hạt". FTUE giữ nguyên nhịp (D12). Sau FTUE bánh xe loài có 5 loài, **không có Thử**.
- Ghi nhận: đây là chỗ mất lớn nhất của MVP cũ (Độn Thử, Tàng Thử). Căn Thương chuyển sang **Linh Nghĩ** (xem SURV-04).

### SURV-03: Ma trận 5×5 (Sinh → Khắc → Cộng sinh)
Vòng sinh theo Ngũ Hành: **Mộc → Vũ → Trùng → Thú → Thủy → Mộc**. Vòng khắc: **Mộc ⊣ Trùng ⊣ Thủy ⊣ Vũ ⊣ Thú ⊣ Mộc**. Mỗi cặp có 1 quan hệ chính (đo được) và 1 **cộng sinh opt-in**. **Tránh chồng số:** khắc ở cấp tộc là *cơ chế*, không nhân thêm hệ số E (đã có ×1,25/×0,8 ở Huyết Mạch; stress-test chỉ chịu ×1,32).
| Cặp | Chính | Hiệu ứng đo được | Cộng sinh (opt-in) |
|---|---|---|---|
| Mộc → Vũ | Sinh | Quả Ước: Vũ ăn +15 No. Tán là **Neo Hậu Duệ** của Vũ | Vũ rải hạt 20 ô, ăn Sâu trên Tán (bầy sâu −50%) |
| Vũ → Trùng | Sinh | "Phân Vũ" (ô rơi, +Dưỡng Chất 3 ô). Nghĩ ăn Phân +8 No | Nghĩ dọn xác chỗ Vũ nghỉ, giảm bị Quạ cướp Linh Hạch |
| Trùng → Thú | Sinh | Xác đã **Mở Xác** (Nghĩ, 45s) không gây Trúng Độc. Bầy mồi +6 No | Nghĩ tha thịt vào Hang: thối 10' → 15' |
| Thú → Thủy | Sinh | Xác thú ≤3 ô nước: Đất ×1,5, **+3% Linh Quỹ** (ao) | Lang vồ cá khi còn ≥1 bầy: không phạt |
| Thủy → Mộc | Sinh | Ô nước W = 3 (đã có). **Quy Tưới:** +20 Thủy lên cây trong 10 ô, CD 60s | Cây che bóng ao: Thủy bay hơi mùa Hạ ×0,8 |
| Mộc ⊣ Trùng | Khắc | Độc/Gai ×1,5 lên bầy; bầy sâu tự sinh khi Tán >70% | **Khế ước Kiến** (đã có, tối đa 2 tổ) |
| Trùng ⊣ Thủy | Khắc | Bầy Nghĩ cạnh ao: bầy cá hồi ×0,5; Nghĩ đào Căn Thương lên rễ nước (1%/s) | Nghĩ lọc rác ao: ao đục hồi +1 bầy/2' |
| Thủy ⊣ Vũ | Khắc | Vũ hạ cánh ở nước nông: **Ướt** (Tốc −20%, CD lướt ×1,5, 6s). Quy cắn Vũ trong nước ×1,25 | Quy cõng Vũ qua đầm (Vũ đứng trên mai: miễn Ướt) |
| Vũ ⊣ Thú | Khắc | Lao từ trên: choáng 1s, 25% HP Thú nhỏ. Thú không đánh trả khi Vũ lướt | Vũ ping vị trí cho Lang (Thần Thức +4 ô) |
| Thú ⊣ Mộc | Khắc | Cào Thân (×0,5, không cho No) — giữ nguyên §4.5 | Lang không phá Mầm: Cây nuôi Quả cho Lang mồi |
- **Kiểm tra thống trị:** mỗi tộc *khắc 1, bị khắc 1, nuôi 1, được nuôi 1*. Không tộc nào ở 4 hàng "không bị đe dọa". Điểm yếu thực dụng: Lang thắng Mộc bằng số (cần ≥2 Lang); Vũ khắc Thú nhưng chết khi xuống nước.
- **Kết nối S2:** xác → Đất → Linh Mạch thành luồng *Thú → Thủy → Mộc*. Ao là nơi linh khí quay về cây.

### SURV-04: Khuẩn tan vào ba chỗ, nấm thành môi trường
- **Phân giải = quy trình.** Sinh Năng 20 CT (8/4/8) giữ nguyên. Xác trả "Đất" sau **3' trên cạn, 90s ở ô ướt** (≤2 ô cách nước), **45s nếu Nghĩ Mở Xác**. Làm rõ câu "Đầm Mục xác phân giải nhanh hơn".
- **Nấm** không thuộc tộc nào, là **props** (Mục Thổ, nấm trên gốc). Mạng cộng sinh nấm của cây → **Mạng Rễ Ngầm** (thuộc Mộc).
- **Căn Thương** từ Độn Thử (đã AI) chuyển sang **Linh Nghĩ** ("Đào Rễ": 1%/s lên Tâm Rễ khi ≥3 Nghĩ). Vẫn đúng quy tắc "cần phối hợp nhiều loài".

### SURV-05: Lão Quy, Trung Ấm, lore
- **S1 sửa nhẹ:** Linh Mạch là mạch nước của rễ Kiến Mộc; suối là Linh Mạch lộ thiên; mọi dòng nước về Suối Nguồn dưới gốc Kiến Mộc, nên Mộng Hỏa tắt trong nước thì nổi lại.
- **NPC Lão Quy** (rùa già giữa Ao Tịnh) thay Bà Khuẩn, dùng chung art với Linh Quy (tint + scale). Thoại: *"Ngươi đã mang nó cả đời. Giờ nó mang ngươi."* / (đói) *"Nước nhớ mọi thứ chảy qua nó. Kể cả cơn đói của ngươi."*
- **Trung Ấm:** xác chìm vào mặt nước phản chiếu (đổi shader, không cảnh mới). **Mộng Ấn 1** "vòng nấm tiên" → **Vũng Sương** (đứng soi lúc bình minh sau mưa).

### SURV-06: Cơ chế nước (MVP, không thêm need)
| Ô | Vị trí | Với mặt đất | Với cây |
|---|---|---|---|
| **Nước nông** (suối, rìa ao, Đầm Mục) | Bìa: 1 suối + Vũng Sương · Trung: suối chính (Linh Mạch) · Thâm: Đầm Mục | **Lội:** Tốc ×0,75, xóa vệt máu/mùi, **tiếng nước lộ vị trí 8 ô** | Rễ vào được, W = 3/ô |
| **Nước sâu** (lõi ao, hồ **Linh Nhãn**) | 2 vũng ở Đầm Mục, hồ ở tâm | Chặn Lang, Nghĩ. **Quy bơi 8 ô/s**, Trĩ lướt qua | Rễ không vào |
| **Giông** | code sét sẵn | Người lội trong 8 ô điểm sét nhận 10% HP max | Rễ trong nước: sét ×0,8 |
- **Dưới nước:** chỉ Quy vào được; **không oxy, không chết đuối, không combat dưới nước** ở MVP. Ranh giới: cạn ↔ nông ↔ sâu. ~3% ô là nước, ~5% ô ẩm viền (PROG kiểm tra W).
- **Cá (Linh Ngư):** bầy sprite, **không AI**; số bầy = f(Linh Quỹ): Sung Linh 3 · Bình 2 · **Khô Linh 0 (ao đục, cá nổi)**. Lang vồ cá +18 No/cắn. Mỗi ao ≥1 bầy: **+1 sức chứa Linh Quỹ** (trần +3/vùng). Cá thành chỉ báo Khô Linh (H13) mà không cần UI mới.

### SURV-07: Chuỗi thức ăn có Vũ
- **Diều hâu, Quạ Linh, Quạ Già → Vũ.** Diều: Circle (báo 2s) → Dive → Flee, **miễn khi dưới Tán/bụi** (nên Nghĩ/mồi trú dưới cây đồng minh). Chi phí 0.
- **Gà Rừng AI** [U1] (skin archetype Hươu, mồi Bìa, trứng mùa Xuân +10 No cho Thú, tranh hạt Bìa −10%). **Chim Sẻ** [1.0] thay "Cộng sinh Nấm": ăn Quả Ước, rải hạt, ăn Sâu.

### SURV-08: Dây chuyền
- §5.7: "cây và nấm tính 0,5" → "cây tính 0,5"; sức chứa = 6 + 1/cây + 1/ao-sống (trần +3). §5.5: "rễ/nấm" → "rễ". **E7 Bào Tử Triều → Triều Hồi** [1.0] (mưa hồn 10', ao nở thêm 2 ô, không lũ; thắng: Thủy, cây gần nước). E3 Đại Hỏa thắng: "cây tiên phong, cá trong đầm".
- §6.2: cột Khuẩn → Linh Quy; thêm Linh Nghĩ, Linh Trĩ (WORLD đặt tên). Thần Vị 5 khớp 5 tộc (Mộc/Thủy/Thổ=Trùng/Kim=Thú/Hỏa=Vũ), 0 chi phí [Post]. Nhãn Ngũ Hành của Huyết Mạch là của **nhánh**, tách khỏi tộc.

## 4. Scope (đề xuất, PX chốt)
- **Mức "chưa sâu":** Mộc và Lang **giữ C1–C4** (USP và PvP). Nghĩ, Quy, Trĩ **lite: C1–C3**, 1 Huyết Mạch, Bản Năng 1–2 + A1, **không Keystone, không Phi Thăng Kiếp I** ở MVP (tức không vào Thâm Lâm; vẫn Hậu Duệ/Luân Hồi đầy đủ).
- **Ước tính của SURV:** +3 loài lite ~+3,0 (mỗi loài ~1,0 do controller chung và kiến tái dụng swarm) · ma trận + nước +0,5 · Linh Thử→FTUE −0,6 · Kiến lite chuyển thành Nghĩ −0,3. **Net ≈ +2,6 tuần**, vượt đệm 4,25 còn ~1,6.
- **Cắt bù:** Huyết Mạch 6→4 (−0,6), Hóa Hình Mộng (−0,25), Linh Thức giữ chỉ do thám (−0,4), Gà/Ếch/Chim Sẻ lùi sau MVP. Còn đệm ~2,9 (~6%) → **scope risk cao**.
- **Fallback:** ra mắt theo đợt (Mộc + Thú + Trùng ngày 1; Thủy, Vũ vào tuần ~35–44 của beta) hoặc Nghĩ/Quy/Trĩ chỉ C1–C2.

## 5. Kết nối
**PROG:** số Quy/Nghĩ/Trĩ, W, Linh Quỹ có cộng ao, kiểm lại "tận diệt cây cần phối hợp" với Nghĩ thay Độn Thử. **WORLD:** Lão Quy, S1, tên cảnh giới 3 loài, Triều Hồi. **PX:** ngân sách trên, FTUE Linh Thử-lite, art tile nước/shader.

## 6. Rủi ro
1. **5 tộc × lite có thể nông hơn 3 loài sâu.** Kiểm chứng: VS chỉ cần 3 tộc, 2 tộc còn lại vào alpha.
2. **Trĩ + Diều hâu AI** có thể chồng vai nếu Vũ thành "kẻ săn thứ hai". Giữ HP 0,6× và lướt không đánh.
3. **Nghĩ (bầy) khó cân hitbox.** Hitbox gộp 1; Công = base × (0,5 + 0,1k), k = 1–5.
4. Tôi đã giữ 0 need mới và 0 AI archetype mới; scope vẫn phồng.

## 7. Câu hỏi mở
- Q1: Linh Thử chỉ là Tiền Thân FTUE có đủ cho "chuột mang hạt" không, hay giữ 1 Hậu Duệ Thử cho FTUE-only?
- Q2: Vũ MVP là Trĩ (an toàn) hay Tước (bay thật, rủi ro cân bằng)? Tôi chọn Trĩ.
- Q3: Chấp nhận Nghĩ/Quy/Trĩ không vào Thâm Lâm ở MVP?
