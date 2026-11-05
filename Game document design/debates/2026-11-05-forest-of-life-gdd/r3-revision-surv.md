# R3 Revision — SURV

> Domain: core survival loop, needs, tài nguyên & linh khí, chuỗi thức ăn, mối đe dọa, lãnh thổ/hang, cái chết.
> Đơn vị tu vi: **CT** (PROG-03). Người chơi Mid chơi 5 phiên × 40'/tuần, tức ≈ 64 CT/phiên và 320 CT/tuần.
> Nhãn scope: **[MVP-A]** (tháng 0–11), **[MVP-B]** (soft launch, tháng 12–15), **[1.0]**, **[Post]** (sau 1.0), **[Cắt]**. Mọi mục [MVP] mới đều ghi rõ nó **thay thế** cái gì.
> Thuật ngữ theo glossary WORLD: **Bế Quan** = thoát an toàn · **Nhập Định** = cửa sổ dễ tổn thương khi thoát sai chỗ · **Đả Tọa** = luyện linh khí thành CT trong phiên · **Mộng Tích** = hồ rested · **Linh Thức** = skill hồn của cây (lên C6 thành Xuất Khiếu) · **Đạo Quả** = tiền meta · **Tâm Hướng** = la bàn hành vi.

---

## 0. Ba lập trường chốt nhanh (theo yêu cầu orchestrator)

| Chủ đề | Lập trường cuối của SURV |
|---|---|
| **7 hay 9 cảnh giới** | **Giữ 7**, ánh xạ **3/2/2** (Rừng Non C1–3 · Nguyên Sinh C4–5 · Cổ Đại C6–7), bỏ phương án 2/2/2+1 tôi đưa ở R2 vì WORLD và PX đã đồng thuận 3/2/2. Lý do và điều kiện đổi ý: xem mục 4. |
| **Gói đơn vị của PROG/PX** | **Chấp nhận** CT là đơn vị gốc · Sinh Năng = 20 CT · Gia Trì cộng dồn kiểu cộng, trần ×3 (×4 trong 30' đầu sau luân hồi) · offline 0 CT · Thiên Đạo Luật hợp nhất. **Điều chỉnh 4 điểm:** (1) g tính theo **cảnh giới thật**, không phải sau Áp Chế; (2) Linh Hạch dùng cùng hệ số m(g) với người nhặt; (3) làm cây Đổ khi g≥2 cũng sinh Nghiệp; (4) đồng hồ Thiên Phạt dừng khi offline. Bảng đầy đủ: SURV-11c. |
| **Mobile** | Mọi loài đều theo **4 thanh + 1 thanh tu vi, ≤5 nút** (SURV-01b). Cây mở khóa động từ theo bậc. Tôi tự bỏ **Ngủ Đông, Linh Khí Thất Thoát cá nhân, sương mù, lũ, Tơ Hồng ở MVP**. |

**Lịch dùng chung cho mọi bảng dưới đây:** 1 ngày-rừng = **20' thực** (Ngày 12' · Hoàng hôn 2' · Đêm 6'), quay lại con số của SURV-19 vì PROG và WORLD đều đã chốt 20'. 1 mùa = **48h thực**, 1 năm-rừng = 8 ngày, Kiếp = 48 ngày = 6 năm-rừng (PROG). Tôi bỏ đề xuất mùa 42h ở R2, vì 48h chia hết vào Kiếp 48 ngày. Vấn đề múi giờ được giải bằng cấu trúc sự kiện (SURV-17b), không cần cho mùa trôi giờ.

---

## 1. Phản hồi phản biện

| Phản biện (từ ai, ID) | Quyết định | Lý do | Thay đổi cụ thể |
|---|---|---|---|
| PROG · SURV-15 Blocker: cost-of-death tự mâu thuẫn, Hậu Duệ quá rẻ làm USP đổi loài chết | **Partial** | Đúng ở hai điểm: số giờ đầu tư của tôi lệch đường cong, và Hậu Duệ mất 1 tiểu cảnh thì quá rẻ. Tôi **không** nhận "rơi 1 cảnh giới": ở C5 cách đó mất ~0.47 tuần, chạm trần retention của PX | SURV-15c: Hậu Duệ **rơi về Sơ kỳ 0% của cảnh hiện tại (WORLD), trần mất 130 CT (PX)**, 0 Đạo Quả, 1 lần/24h, neo phá được. Đổi loài: ×3 tới đầu cảnh cũ, rồi ×1.5 tới đỉnh cũ, cộng Đạo Quả. Bảng giờ đầu tư neo theo tổng 1.670 CT |
| PROG · SURV-09/02 Major: 5 đơn vị năng lượng, Sinh Năng chưa định nghĩa, kill-trading | **Accept** | Sim M thuyết phục: với Sinh Năng = tu vi lũy kế, kill-trading lãi +188 CT/h | Sinh Năng = 20 CT chuẩn hóa, chia **8 / 4 / 8**. Ăn khi đã no thì phần dư chuyển thành linh khí với hiệu suất 50%. Kill-trading tại neo lỗ (SURV-09b) |
| PROG · SURV-06/08 Major: Bế Quan ×1.5 tạo chiến lược AFK | **Accept** | Ngồi im an toàn mà được ×1.5 là chiến lược trội. Tôi sai | Đổi tên thành **Đả Tọa**: chỉ luyện linh khí **đã tích**, không sinh mới. CT từ Đả Tọa có trần **15% CT của phiên** (PX). Tĩnh tọa ngoài thì theo luật chống AFK của PROG |
| PROG · SURV-16 Major: kiếp thất bại phải chờ 24h | **Accept** | Casual mất gần 1 tuần chỉ vì RNG | Thất bại = **Đạo Cơ Tổn** 20' + mất 30% CT tầng (PROG-07). Thử lại được ngay ở phiên sau |
| PROG · SURV-03 Minor: Thủy từ rễ quá hào phóng | **Accept** | 3 ô rễ là xóa được need Thủy, nên need này không có thật | Hấp thu = `6 × (1 − e^(−W/4))`/phút, trong đó W = ô ẩm + 3×ô suối (SURV-03b) |
| PROG · SURV-07 Minor: rễ ×2/cảnh nổ hiệu năng | **Accept** | — | Rễ ×1.6/cảnh: 12 → 19 → 31 → 49 → 79 → 126 → 201 ô |
| PROG · SURV-12 Minor: quang hợp offline ra CT | **Accept** (đã sửa ở R2) | — | Offline chỉ ra Quang Tinh (trần kho 150), 0 CT |
| PROG · ngày 20' hay 24' | **Accept 20'** | Ở R2 tôi đã nhượng 24' cho WORLD, nhưng giờ WORLD và PROG đều chốt 20' và tension graph dựng trên 20' | SURV-19 giữ nguyên |
| PX · SURV-07 Major: Vệt Nắng thành game chạm liên tục | **Accept** | Mâu thuẫn với chơi một tay, đúng là lỗi. Tôi từng đặt mục tiêu "AFK mất 40%", con số đó là phạt chứ không phải thưởng | Vệt Nắng thành **cửa sổ thưởng**: trung bình 1 vệt/50s, chạm thì ×2.5 trong 8s. AFK mất ≈19% thu nhập. Cần ≈1.5 lần chạm/phút để đạt 100% |
| PX · SURV-03/07 Major: cây có 13 chỉ báo, 13 nút | **Accept** | Ngân sách 4+1 hợp lý. Tôi có điểm mù "quá nhiều thanh" | SURV-01b: vòng HP 3 lớp, Thủy, Quang Tinh, Linh Khí, cộng thanh tu vi. Dưỡng Chất vào panel phụ. Ánh Sáng% hiện bằng hình trên tán. Động từ mở theo bậc (SURV-07b) |
| PX · SURV-15 vs PROG-10 Blocker | **Partial** (lai) | Xem dòng đầu. Tôi nhận trần chi phí 130 CT của PX và mốc đo ≥30–35% số lần chết chọn đổi loài | SURV-15c |
| PX · SURV-17+12 Major: Đại Hạn giết cây đang offline | **Accept, luật cứng** | Mất 2 tuần vì một sự kiện mình không thể tham gia là kiểu chết người chơi không đọc được | Thân đang offline **miễn mọi decay needs và mọi sự kiện môi trường**. Sự kiện kéo dài 24h và có nhiều đỉnh (SURV-17b) |
| PX · SURV-08/11 Minor: 3 cơ chế cùng đẩy người mạnh khỏi vùng ngoài | **Partial** | Đúng là thừa ở tầng **cá nhân**, nên tôi bỏ Linh Khí Thất Thoát. Nhưng WORLD cần upkeep để biến "kẻ mạnh ở lâu làm rừng đói" thành luật | Upkeep cảnh giới chuyển thành **tải lên Quỹ Linh Vùng** (SURV-08b), không trừ gì trực tiếp vào người chơi. Phía cá nhân chỉ còn Áp Chế và CT ×0.5^chênh (PROG) |
| PX · SURV-13/14 Minor scope | **Accept** | — | MVP: 4 archetype AI, 2 kiểu thời tiết (mưa, giông). Ký sinh và boss sang [1.0]. Sương mù, lũ [Cắt] |
| PX · Q1: ăn bằng giữ nút hay chạm từng cắn? | Trả lời | — | **Giữ nút** đánh/ăn theo ngữ cảnh thì tự cắn mỗi 1.5s, chạm thì 1 cắn. Khoảng 1 lần giữ mỗi 6–8' |
| PX · Q2: mùa Đông cây có ngừng tu không? | **Accept** (không ngừng) | 25% năm-rừng không có CT là phạt quá nặng | **Cắt Ngủ Đông.** Thay bằng Đông Tàng: CT từ rễ ×1.6 để bù quang hợp ×0.4. Đông Tàng Mộng Du (Linh Thức ×2) để [1.0] |
| WORLD · SURV-09 Major: ledger bảo toàn hoàn hảo, săn sạch không tốn gì | **Accept** | Đây là phản biện hay nhất tôi nhận được. Một sổ cái cân hoàn hảo thì không có sinh thái | Phần đất của xác cộng vào **Quỹ Linh Vùng**. Tải tu luyện rút từ quỹ. Quỹ <30% thì Khô Linh (SURV-08b), có sàn ở Bìa Rừng |
| WORLD · SURV-15 Major: Hậu Duệ vô giá | **Accept** | Gộp với PX như dòng đầu. "Dòng dõi hay khai ngộ" là đánh đổi đẹp | Hậu Duệ: 0 Đạo Quả, giữ Huyết Mạch. Đổi loài: có Đạo Quả |
| WORLD · từ vựng Bế Quan/Xuất Khiếu | **Accept** | — | Skill cây đổi thành **Linh Thức** [1.0]. Bế Quan, Nhập Định, Đả Tọa dùng theo glossary |
| WORLD · Linh Triều có 3 nhịp | **Partial** | Một sự kiện, một nhịp. Tôi **không** nhận Linh Tức 2 lần/ngày × 15', vì PX đã tự bỏ bản đó do là hẹn giờ kiểu FOMO | Linh Triều: 24h mỗi 4 ngày, đỉnh vào mỗi bình minh game, cao trào 30' (SURV-17b) |
| WORLD · Q: mùa 3.5 ngày? | **Reject** | Mùa 3.5 ngày làm mỗi mùa kéo quá nửa tuần: người chơi 3 phiên/tuần có thể chỉ gặp 1 mùa. Mùa 48h thì mỗi tuần có 3–4 lần đổi mùa và chia hết vào Kiếp 48 ngày | Mùa 48h, năm-rừng 8 ngày. Sự kiện "1/mùa" đổi thành "1/năm-rừng" |
| WORLD · Q: upkeep rút từ quỹ vùng? | **Accept** | — | SURV-08b |
| PROG-12b · g tính sau Áp Chế | **Reject** (giữ R2, cùng PX) | Một C6 bị nén về C3 giết C2 sẽ không bị tính Nghiệp, tức là lỗ hổng cho đúng loại "ma cũ" mà ta muốn chặn | Chỉ số combat tính sau Áp Chế. **Thưởng và Nghiệp tính theo cảnh thật** |
| PROG-07 · Thiên Kiếp thất bại = chết | **Partial**, theo hướng PX | Tôi là owner của "cái chết". Chết vì sét sau ~5 tuần đầu tư, khi chỉ còn ~12 ngày tới cuối Kiếp, là chết không hồi được trong mùa | Sét làm HP về 0 thì **Kiếp Thương + rơi 1 tầng** (PX đề xuất 2 tầng; tôi giảm còn 1 vì đã có Đạo Cơ Tổn). **Chết thật chỉ khi bị sinh vật khác giết** trong lúc độ kiếp |

---

## 2. Đề xuất đã sửa (bản cuối cho GDD)

**Giữ nguyên:** SURV-19 (tension graph, ngày 20'). **Đã cắt:** Ngủ Đông, Linh Khí Thất Thoát cá nhân, mật độ linh khí động trên từng ô, sương mù, lũ, Hang cấp 2–4 trong MVP, crafting Luyện Hóa.

### SURV-01b: HUD 4+1, ≤5 nút [MVP-A]

| Loài | 4 chỉ báo cố định | +1 | Nút (≤5) + cử chỉ |
|---|---|---|---|
| **Linh Mộc** | ① Vòng HP 3 lớp (Tán ngoài / Thân giữa / Tâm Rễ lõi) ② Thủy ③ Quang Tinh ④ Linh Khí | Tu vi | Phòng thủ (bánh xe 2) · Hạt · Quả · Cộng sinh · Thần Thông. **Chạm** map để bắt Vệt Nắng, **kéo** để vươn rễ. Đả Tọa, Độ Kiếp, Linh Hóa Địa nằm trong menu ngữ cảnh |
| **Linh Thử / Lang** | ① HP ② Linh Khí ③ No ④ Thể Lực (vòng quanh joystick) | Tu vi | Đánh/ăn theo ngữ cảnh (giữ = ăn liên tục) · 3 skill · Thần Thông. **Vuốt** để né, đẩy joystick ra mép để chạy |
| **Khuẩn** [1.0] | HP · Linh Khí · Ẩm · Mục Chất | Tu vi | như cây |

- Trạng thái (Trúng Độc, Ấu Linh, Nghiệp >0, Kiếp Thương) là **icon 24dp**, không phải thanh. Dưỡng Chất, Ánh Sáng% và Quỹ Vùng hiện bằng hình ảnh trên map (tán sáng/tối, màu vùng).
- **Bỏ 1 need thì game có tệ đi không?** Đã kiểm: Khát của thú và Thân nhiệt đã bị bỏ từ R1. Dưỡng Chất bị hạ xuống panel phụ. Thể Lực được giữ vì nó là trục của mọi cuộc rượt đuổi, nhưng hiện dưới dạng vòng quanh joystick, không chiếm chỗ thanh.

### SURV-02b: Needs Table — Động vật [MVP-A]
Thang 0–100, giá trị cho C1, thời gian thực. **Hệ số needs → CT:** Comfort ×1.0 · Warning ×0.85 · Critical ×0.5 · Lethal ×0.

| Need | Linh Thử (ăn hạt, con mồi) | Lang (ăn thịt) | Ngưỡng C / W / Cr / L | Hậu quả theo ngưỡng |
|---|---|---|---|---|
| **No** decay | −1/12s (−5/phút). Chạy ×1.5. Đông ×1.4 | −1/15s (−4/phút). Chạy ×1.5. Đông ×1.4 | 100–60 / 59–25 / 24–1 / 0 | C: hồi HP 1%/5s · W: ngừng hồi HP · Cr: Thể Lực max −30% · 0: −1% HP/3s |
| Lần **Warning đầu tiên** | **8.2'** | **10.2'** | — | Cả hai nằm trong mục tiêu 8–15' |
| **No** hồi | Hạt +8/cắn (1s) · quả +15 · sâu +6 (đồng thời diệt ổ sâu trên cây) · cỏ/chồi +3 | Thịt +30/cắn (2s) · Linh Thử nguyên con +25 · xác thối +12, 25% Trúng Độc (−1 HP/2s trong 20s) | — | Ăn khi đã no: phần dư → linh khí ×50% |
| **Thể Lực** | Chạy −10/s (10s) · né −20 · hồi +25/s đứng, +12/s đi | Chạy −12/s (8.3s) · đòn −15 đến −25 · né −20 · hồi +20/s đứng, +10/s đi | 100–40 / 39–15 / 14–1 / 0 | <15: không chạy được · 0: choáng 1.5s · No Critical: hồi ×0.6 |
| **HP** | theo PROG `HP(n)` | theo PROG | 100–50 / 49–25 / 24–1 / 0 | <25%: để lại vệt máu, kẻ săn đánh hơi được trong 12 ô |

- **Linh Thử – Kho Hạt** [MVP-A, S; thay cho "kho thịt" riêng của Lang, dùng chung code kho Hang]: giữ nút ở ô có hạt thì **chôn**. Kho Hang cấp 1 chứa 40 hạt, không thối. Hạt chôn ngoài Hang có 20% bị "quên" sau 1 ngày-rừng và nảy mầm, cho cây người chơi trong 3 ô +5 Dưỡng Chất. **Đánh đổi:** ăn ngay hay trữ cho mùa Đông (hạt mọc ×0.3 trong Đông). Đây là "gỗ để sưởi hay để xây tường" của chuột.
- **Lang:** thịt trong kho Hang **thối sau 10'**, nên Lang phải săn đều chứ không tích trữ được.

### SURV-03b: Needs — Linh Mộc và 3 lớp thân [MVP-A]

| Lớp | C1 | Tỉ lệ ngân sách PB (khớp PROG-11b) | Ai phá được |
|---|---|---|---|
| **Tán** | 60 | ~20% | Thú ăn lá (Hươu AI), sâu, mưa đá, Linh Thử (chồi non) |
| **Thân** | 200 | ~50% · HP(n) của PROG là HP lớp này · Tốc = 0 được quy đổi ×3 HP Thân | Mọi đòn đánh (×0.5 khi Tán còn), sét, cây khác |
| **Tâm Rễ** | 100 | ~30% · **đòn thường không chạm tới** | Hạn (Thủy = 0), kiếp, rễ đối thủ, [1.0] lửa lớn, nấm mục, nhánh Đào |

- **Tán = 0:** đòn tiếp theo lột vỏ Thân. **Thân = 0 → Đổ:** cây vào trạng thái Rễ Ngủ, mọc lại sau 3' nếu Quang Tinh ≥30, mất 1 bậc chiều cao (≈15–20 CT tiến độ hình thể, **không** mất CT). **Mục tiêu sim (PROG):** 1 kẻ tấn công cùng cảnh cần ≥40s để làm cây Đổ khi cây dùng phòng thủ, và ≥25s nếu cây không làm gì.

| Need | Decay | Ngưỡng C / W / Cr / L | Hậu quả | Cách hồi |
|---|---|---|---|---|
| **Thủy** | Ngày −3/phút · đêm −1/phút · +0.5/phút mỗi bậc chiều cao · Hạ ×1.5 · Đại Hạn ×2 (cao trào ×2.5) | 100–50 / 49–30 / 29–10 / 0 | <30: quang hợp ×0.5 · <10: rụng 1 lá/10s · 0: Tâm Rễ −1%/5s (chết héo sau ~8') | Hấp thu `6×(1−e^(−W/4))`/phút, W = ô ẩm + 3×ô suối (3 ô ẩm → +3.2; 1 ô suối + 5 ô ẩm → +5.3; trần +6) · mưa +10/phút · sương bình minh +15 một lần |
| **Quang Tinh** (tiền tệ, kho 0–150) | Đêm hô hấp −0.05×(Tán + Thân/10)/phút (C1 ≈ −4/phút) | 0 vào ban đêm thì tiêu Tán để thở (−1 lá/15s) | — | Ngày: Tán × Ánh Sáng% × hệ số Thủy × 0.1/phút (C1 nắng đủ ≈ +6/phút) · Vệt Nắng ×2.5 trong 8s, trung bình 1 vệt/50s |
| **Linh Khí** | theo skill | — | — | Hấp thu theo vòng (SURV-08b), Linh Quang (vệt vàng, 1/3', +5) |
| **Dưỡng Chất** (panel phụ, không decay) | — | — | Thiếu thì không lớn, không ra hạt | Đất màu, xác, phân thú trong lãnh thổ rễ, Hạt Thử bị quên |

- **Ngân sách 1 ngày-rừng của cây C1:** +72 (ngày) +~17 (Vệt Nắng) −24 (đêm) ≈ **+65 Quang Tinh**. Chi tiêu: lá 2 · ô rễ 8 · bậc chiều cao 40 · hạt 25 + 5 Dưỡng Chất · quả 15 · phòng thủ 10–20. Một ngày đủ cho khoảng 1 bậc chiều cao, hoặc 2 quả + 1 hạt + 2 lần phòng thủ. **Không bao giờ đủ cho tất cả**, và đó là chỗ có quyết định.
- **CT của cây:** phần CT quang hợp tỉ lệ với Quang Tinh **thu được**, không tỉ lệ với thời gian online. **Đông Tàng:** trong mùa Đông, CT từ rễ ×1.6 để bù quang hợp ×0.4. PROG cần sim để giữ parity ±15% với thú.
- **Ánh Sáng%:** 100% ở chỗ trống, mỗi tán cao hơn chồng lên trừ 30%, tối thiểu 10%. Cao thì nhiều nắng hơn nhưng tốn Thủy hơn, bị nhìn thấy từ xa hơn và hút sét.

### SURV-04b: Khuẩn [1.0] và Trùng [Post]
- **Khuẩn** giữ số liệu R1: Ẩm −4/phút dưới nắng, −1/phút trong bóng, +2/phút ban đêm hoặc khi mưa. Nắng trực tiếp >60s thì −2% HP/s. Mục Chất lấy từ xác, gỗ mục, lá rụng. Sợi nấm 5 Mục Chất/ô. Phần đất của xác sang quỹ vùng ×3 nếu nấm hấp thu. **Sàn xác:** Director bảo đảm ≥1 xác NPC mỗi 5' mỗi vùng.
- **Trùng-đàn** [Post]. Ở MVP, kiến là cộng sinh do cây điều khiển.

### SURV-05b: Ma trận môi trường × needs [MVP-A]

| Điều kiện | Thú: No | Thú: Thể Lực hồi | Mộc: Thủy | Mộc: quang hợp | Thức ăn sẵn có | Ghi chú |
|---|---|---|---|---|---|---|
| Đêm (6') | ×1.0 | ×1.0 | ×0.33 | 0 (hô hấp) | — | Kẻ săn AI +50%, kẻ săn người chơi +30% tầm nhìn |
| Xuân | ×0.9 | — | ×1.0 | ×1.2 | Cỏ ×1.3 · hạt/quả ×0.8 · con mồi AI ×1.2 | Mùa sinh sản |
| Hạ | ×1.0 | ×0.8 | ×1.5 | ×1.3 | ×1.0 | Mùa Đại Hạn |
| Thu | ×1.1 | — | ×1.0 | ×0.9 | Hạt/quả ×1.5 · cỏ ×0.8 | Mùa tích trữ (Kho Hạt) |
| Đông | ×1.4 | ×0.8 | ×0.5 | ×0.4 (CT rễ ×1.6) | Hạt ×0.3 · cỏ ×0.4 · con mồi ×0.8 | Mùa Huyết Nguyệt |
| Mưa | ×1.0 | — | +10/phút | ×0.6 | — | Xóa mùi, con mồi dễ trốn hơn |
| Giông | ×1.0 | — | +10/phút | ×0.4 | — | Mỗi 20s sét đánh vật cao nhất trong 8 ô, 30% Thân max. Thú đứng dưới cây bị đánh lan 20 HP |
| ~~Sương mù, Lũ~~ | | | | | | [Cắt] |

### SURV-06b: Core loop 4 tầng [MVP-A]
Giữ cấu trúc R1, sửa hai điểm: (1) **Release cuối phiên là Đả Tọa tại Hang hoặc Tâm Rễ**: luyện linh khí đã tích thành CT (trần 15% CT phiên), autosave, rồi Bế Quan. Đả Tọa **không** sinh linh khí mới. (2) Tầng Campaign theo Kiếp 48 ngày: Tiểu Kiếp (tầng) → Trung Kiếp C3→C4 (phi thăng Non→Nguyên Sinh) → Đại Kiếp C5→C6 → Thiên Kiếp C6→C7.

### SURV-07b: Cây — động từ theo bậc mở khóa

| Động từ | Mở ở | Số liệu C1 | Đánh đổi | Nhãn |
|---|---|---|---|---|
| **Bắt Vệt Nắng** | Phút đầu làm cây | 1 vệt/50s, ×2.5 trong 8s. Linh Quang 1/3' +5 linh khí. AFK mất ≈19% | Bỏ qua cũng không chết | [MVP-A] |
| **Vươn rễ** (kéo) | Phút đầu | 1 ô/20s · 8 Quang Tinh/ô · tối đa 12 ô, ×1.6 mỗi cảnh · ô rễ = lãnh thổ, nước, cảm ứng rung | Rễ dài thì nhiều điểm bị cắt | [MVP-A] |
| **Gai Bạo** | Phút đầu | Phản 15% sát thương mỗi cắn, trong 10s · CD 20s · 10 Quang Tinh | Tiêu cho phòng thủ thì ít Quang Tinh để lớn | [MVP-A] |
| **Độc Tiết** | C1 Trung | Sau 5 cắn: chậm −30%, −2 HP/s trong 6s · CD 45s · 20 Quang Tinh | như trên | [MVP-A] |
| **Gieo hạt / Neo** | C1 Hậu | Tầm 6 ô (gió mạnh 20) · 25 Quang Tinh + 5 Dưỡng Chất · tối đa 3 Mầm Con, **1 Mầm được chỉ định làm Neo** | Mầm 30 HP. Mầm trong mạng rễ được hưởng phòng thủ của cây, ngoài mạng thì không | [MVP-A] |
| **Quả Ước** (= WORLD-14d) | C1 Hậu | 15 Quang Tinh/quả · thú ăn được +15 No, +3 linh khí · cây nhận 1 hạt phát tán + phân bón tại chỗ thú đi qua | Quả nuôi luôn cả kẻ thù | [MVP-A] |
| **Cộng sinh: Kiến** | C2 | Tới sau 8s, −3 HP/s lên kẻ đứng trong ô rễ · duy trì −1 Quang Tinh/phút/tổ · tối đa 2 tổ | Bỏ đói thì kiến rời đi | [MVP-A] |
| Đắng Hóa, Trói Rễ, Nắp Ấm/Bẫy Kẹp | Huyết Mạch C3 (PROG) | số liệu R1 | — | [MVP-A] nằm trong ngân sách 24 skill của PROG/PX |
| **Linh Thức** (hồn rời thân) | C2 | 90s, CD 5' · thân bị bỏ trống thì phòng thủ tự động 50% | — | [1.0] |
| Cộng sinh Ong/Nấm, Mộc Độn | — | Mộc Độn: chỉ trong mạng rễ, CD 3', 15 Quang Tinh/lượt, không dùng được nếu bị đánh trong 10s gần nhất | — | [1.0] |
| Hóa Hình sợi mệnh 30 ô | — | — | — | [Post] (Nhân Hình). MVP-B chỉ có Bản Thể C5 |

**Plant Pressure Map (MVP):**

| Áp lực | Tần suất | Tác động | Đối phó |
|---|---|---|---|
| Hươu AI ăn lá | 1 đợt/4–7' ở Bìa và Trung Lâm (Director điều chỉnh) | −2 lá/cắn | Gai, Độc, kiến, hoặc treo Quả Ước để hươu ăn quả thay lá |
| Linh Thử (người chơi/AI) | Tùy | Gặm chồi −1 lá/2s, gặm Mầm Con 5 HP/s | Mầm đặt trong mạng rễ, Gai. Hoặc biến chuột thành đồng minh: chuột ăn sâu và mang hạt |
| Bầy sâu | Đẻ trứng khi Tán >70% và không có kiến, nở sau 2' | −1 lá/5s mỗi ổ | Kiến, Độc Tiết, Linh Thử ăn sâu |
| Cây đối thủ | Liên tục | Che bóng −30%, tranh ô rễ (bên đầu tư Quang Tinh/ô cao hơn chiếm được sau 30s) | Vươn cao hơn, chiếm ô trước |
| Hạn và sét | Đại Hạn, giông | Thủy, Thân | Rễ tới suối, thu Tán trong giông |
| ~~Tơ Hồng Yêu~~ | — | — | [1.0] |

FTUE: phút 16–20 làm cây chỉ có Vệt Nắng, rễ và Gai. Director script **một đợt hươu ăn lá ở phút 4–6** của kiếp cây.

### SURV-08b: Linh khí và Quỹ Linh Vùng [MVP-A lite] *(từ WORLD-03b; thay cho mật độ L0–L5 trên từng ô và Linh Khí Thất Thoát của R1)*

**Mật độ tĩnh theo vòng** (MVP: 1 map, 3 vòng):

| Vòng | Mật độ | Cảnh giới mục tiêu | Hấp thu linh khí khi tĩnh tọa | Bonus CT vòng (PROG, cộng vào Gia Trì) |
|---|---|---|---|---|
| Bìa Rừng | L0 | C1–C2 | +3/phút | +0 |
| Trung Lâm | L1–L2 | C2–C4 | +6/phút | +0.15 |
| Linh Lâm (lõi) | L2–L3 | C4–C6 | +12/phút | +0.3 |
| Linh Nhãn (cao trào Linh Triều) | L4 | — | +25/phút | +0.5 |

**Quỹ Linh Vùng Q (0–100%), mỗi vùng 1 số thực:**
- **Tải** của người chơi đang online trong vùng: C1–C3 = 1, C4–C5 = 3, C6 = 5, Thần = 0 (thần nuôi rừng). Cây = 0.5 (vừa tiêu vừa sản xuất), Khuẩn = 0.5.
- **Sức chứa** = 6 + 1 cho mỗi cây/nấm người chơi còn sống trong vùng (cây offline tính 0.5) + 2 cho mỗi Linh Hóa Địa đang hoạt động.
- **Khi tải > sức chứa:** ΔQ = −35%/h × (tải − sức chứa)/sức chứa.
- **Khi tải ≤ sức chứa:** ΔQ = +4%/h, cộng 1%/h cho mỗi cây/nấm. Mỗi xác phân rã trong vùng +2% (+6% nếu nấm hấp thu).
- **Q <30% thì Khô Linh:** CT của kẻ tiêu thụ −50%, của cây và nấm −20% (PROG). Vùng ngả xám (WORLD lo phần hiển thị).
- **Bìa Rừng có sàn Q = 50%** ("Thiên Đạo hộ mầm"), nên không bao giờ bị Khô Linh.
- **Kiểm chứng (giao PROG sim):** 4 Lang C4 (tải 12, sức chứa 6) farm cùng một vùng Trung Lâm sẽ đưa Q từ 100% xuống 30% sau **2 giờ có mặt**, tức khoảng 3 tối chơi (khớp kịch bản của WORLD). 2 Lang C4 + 1 cây + 1 nấm (tải 7, sức chứa 8) thì không bao giờ bị Khô Linh. Mục tiêu agent sim 40 người × 7 ngày: Bìa Rừng có tu vi < ×0.8 trong <10% thời gian.
- **Cách dùng linh khí (giữ nguyên R1):** skill, hồi thương (10 linh khí = 10% HP), khiên kiếp (1:1 HP), Đả Tọa thành CT, Linh Hóa Địa. **Linh Hóa Địa** [MVP-B, S, nằm trong menu ngữ cảnh]: cây C4+ tiêu 200 linh khí để lãnh thổ rễ được +1 mật độ và vùng được +2 sức chứa trong 24h thực. WORLD dùng hành động này làm trụ của Thần Cách.

### SURV-09b: Sổ Sinh Năng [MVP-A]
Khi một **người chơi** chết, Sinh Năng = **20 CT chuẩn hóa** (UI hiển thị phóng to theo cảnh giới). Phần thưởng giết AI do PROG quy định (≈4.4 CT).

| Phần | CT | Ai nhận | Hệ số |
|---|---|---|---|
| Kẻ ăn | 8 | Chỉ nhận qua hành động **ăn hoặc hấp thu**: 4s, bị ngắt được | × m(g) của kẻ giết (SURV-11c) |
| Linh Hạch | 4 | Ai nhặt trước. Quạ AI lấy mất sau 90s nếu không ai nhặt. Tự tan sau 30' | × m(g) của **người nhặt** so với nạn nhân |
| Đất | 8 | Rễ và sợi nấm trong 3 ô hấp thu trong thời gian xác phân rã, đồng thời +2% Q vùng | Không nhân hệ số: sinh thái luôn được phần của mình |

- **Kill-trading tại neo bị lỗ:** hai người C4 thay nhau giết. Mỗi vòng kẻ giết nhận +8 CT, nạn nhân mất tối đa 130 CT (Hậu Duệ). Lần chết thứ hai trong 24h buộc Luân Hồi. Ngoài ra Hồn Hộ 10' và luật cùng một cặp chỉ cho CT 1 lần/30'.
- **Ăn khi đã no:** phần No dư đổi thành linh khí với hiệu suất 50%.

### SURV-10b: Kinh tế gặm và ma trận "ai ăn ai" (MVP: 3 loài + AI)

| Kẻ hành động → đối tượng | Linh Mộc | Linh Thử | Lang | Hươu AI |
|---|---|---|---|---|
| **Linh Mộc** | Che bóng, tranh rễ | Quả Ước (nuôi), Nắp Ấm (bẫy, Huyết Mạch C3) | Gai/Độc/kiến. Hút xác Lang để lại | Gai/Độc, Quả Ước |
| **Linh Thử** | Ăn quả và mang hạt (cộng sinh) **hoặc** gặm chồi/Mầm (gây hại). Ăn sâu trên tán (giúp cây) | Tranh hạt | Con mồi. Thoát bằng hang nhiều cửa | — |
| **Lang** | Cào Thân (×0.5, không cho No). Lý do duy nhất để làm vậy là phá Mầm-Neo ("tận diệt") | **Săn**, nguồn chính | Tranh lãnh thổ | **Săn** |

- **Nguyên tắc giữ nguyên:** thú ăn cây thì nhận được ít hơn phần cây mất (lá → thú 40%). Cây không chết vì bị gặm, chỉ chậm lại. Hạ cây (Thân về 0) cần kẻ cao hơn ≥1 cảnh, hoặc 3+ kẻ phối hợp ≥2', hoặc sét.
- **Mục tiêu sim:** thú gặm 60s một cây có phòng thủ nhận ≈1.5× giá trị của 60s ăn cỏ dại nhưng mất ~25% HP. Cây mất 8–10' quang hợp, Tâm Rễ không mất gì.

### SURV-11c: Thiên Đạo Luật hợp nhất [MVP-B, cùng Rừng chung] *(PROG-12b với 4 điều chỉnh của SURV)*

**g = cảnh giới THẬT của kẻ giết − cảnh giới thật của nạn nhân.** Chỉ số combat tính **sau** Áp Chế. Thưởng và Nghiệp tính theo cảnh thật.

| g | m(g): CT kẻ ăn / Linh Hạch | No | Nghiệp | Nạn nhân nhận |
|---|---|---|---|---|
| ≤0 (Nghịch Thiên) | × (1 + 0.5·\|g\|) | 100% | 0 | — |
| 1 | × 0.5 | 100% | 0 (chuỗi thức ăn tự nhiên) | +10% Đạo Quả |
| ≥2 | **× 0** | 100% (sinh tồn vẫn là thật) | +1, hoặc +2 nếu nạn nhân đang có Ấu Linh | **Oán Linh** +25% Đạo Quả, tối đa 1 lần/ngày |
| Làm cây Đổ khi g≥2 *(SURV)* | — | — | +1 (không tính khi hai cây đang tranh ô rễ) | — |

| Bậc Nghiệp | Hậu quả |
|---|---|
| ≥1 | Hào quang đỏ thấy được trong 20 ô. Kiếp +10% sát thương mỗi Nghiệp, trần +50% |
| ≥3 **Huyết Sát** | Hiện trên bản đồ vùng. Ai hạ được nhận thưởng ×3 |
| ≥5 **Thiên Phạt** | Sét đuổi trong 1 ngày-rừng (20'), mỗi 60s một sét 10% HP max. **Đồng hồ dừng khi offline** *(SURV)*. Sống sót thì Nghiệp về 0 nhưng mất 10% CT tầng (WORLD) |
| Giảm Nghiệp | −1 sau mỗi 2h **online**. Không giảm khi offline |
| Miễn trừ | Nạn nhân chủ động tấn công trước (gai thụ động không tính) thì không sinh Nghiệp trong 60s. Cùng một cặp: CT 1 lần/30', Nghiệp và Oán Linh 1 lần/24h |

- **Ấu Linh:** áp dụng trong 3h đầu ở Rừng chung hoặc tới hết C2. Kẻ có g≥2 không thấy người có Ấu Linh trên Thần Thức (radar), chỉ thấy bằng mắt trong 5 ô, và gây −60% sát thương lên họ. Mất Ấu Linh nếu chủ động tấn công người chơi.
- **Áp Chế:** trần C3 Hậu trong Rừng Non. Vòng Linh Lâm không bị Áp Chế.
- **Thoát Sinh:** gây sát thương lên kẻ săn có g≥1 rồi sống sót, ra khỏi tầm trong 30s thì +2 CT, 1 lần/10'.
- **Hồn Hộ:** trong 10' sau Hậu Duệ, kẻ có g≥1 giết lại thì nhận 0 CT.
- **Đã bỏ:** Linh Khí Thất Thoát cá nhân (SURV) và −HP vì linh khí loãng (PX).

### SURV-12b: Lãnh thổ, Hang, luật Bế Quan/offline [MVP-A]
- **Cây:** ô rễ là lãnh thổ. Hai mạng rễ giáp nhau thì tranh ô: bên có Quang Tinh đầu tư/ô cao hơn chiếm sau 30s.
- **Hang** [MVP-A chỉ cấp 1, cấp 2–4 để 1.0]: mỗi người chơi 1 hang. Kho 40 đơn vị. Nơi Đả Tọa và nơi đặt **Ổ Hậu Duệ** (neo). Thú làm hang trong hốc cây người chơi (một nút bật "Mở Hốc") để [1.0].

| Luật Bế Quan (hợp nhất) | Số |
|---|---|
| Thoát trong Hang hoặc lãnh thổ rễ của mình | Bế Quan ngay. Thú rời thế giới, cây thành bất tử |
| Thoát ở chỗ khác hoặc rớt mạng | **Nhập Định** 30s (60s nếu gây hoặc nhận sát thương trong 30s gần nhất). Kết nối lại trong thời gian này thì chơi tiếp |
| Khi offline | **Miễn mọi decay needs và mọi sự kiện môi trường.** Thủy và No đóng băng |
| Trần tổn thất của cây và Hang | Tính **mỗi 24h thực**: ≤20% Tán, ≤25% ô rễ ngoài (không tính bán kính 2 ô quanh Tâm Rễ), kho Hang bị cướp ≤50%. Tâm Rễ và Thân bất tử |
| Phòng thủ thụ động khi offline | Vẫn chạy, nhưng chỉ cho **Dưỡng Chất**, không cho CT |
| Tăng trưởng khi offline | Quang hợp 25% vào Quang Tinh, trần 8h, trần kho 150. **Kế Hoạch Sinh Trưởng** đặt trước khi thoát: ≤3 ô rễ, mọc lại Tán hoặc chín quả, trả bằng Quang Tinh |
| CT offline | **0.** Chỉ có Mộng Tích (PROG-04) |
| Chống giữ đất ảo | Ô rễ của cây offline >48h teo 1 ô/ngày, không teo vào bán kính 2 |
| Tóm tắt khi quay lại | **Mộng Báo** (gộp Nhật Ký Rễ và báo mộng), xem trong ≤20s |

### SURV-13b: Mối đe dọa AI và Ý Chí Rừng [MVP-A: 4 archetype + Director lite]

| Archetype | Tên (WORLD sẽ đặt lại) | State machine | Spawn mỗi vùng (ngày / đêm) | Ai sợ nó | Nhãn |
|---|---|---|---|---|---|
| Ăn cỏ đàn | Hươu Sừng Ngọc | Graze → Alert (thấy kẻ săn trong 8 ô) → Flee theo đàn → Regroup | 2 đàn × 3–5 con | Cây | [MVP-A] |
| Kẻ săn | Báo Bóng Đêm (biến thể **Huyết Báo**: đổi palette, scale 1.5×) | Idle → Curious → Stalk → Attack → Eat / Flee (khi HP <30%) | Bìa 1/2 · Trung 2/4 · Linh Lâm 3/5. Cảnh giới ≤ mức của vòng | Linh Thử, Lang yếu | [MVP-A] |
| Bầy côn trùng | Sâu Lửa | Spawn → Swarm → Consume → Disperse | Theo luật Tán >70% | Cây | [MVP-A] |
| Ăn xác | Quạ Linh | Circle (sau 60s) → Wait → Steal Linh Hạch (sau 90s) → Flee | Theo xác | Kẻ vừa giết | [MVP-A] |
| Ký sinh tĩnh | Tơ Hồng Yêu | Dormant → Attach → Drain (−20% Quang Tinh) | 1/ngày-rừng ở vùng ẩm | Cây | [1.0] |
| Hộ Rừng (boss) | Cổ Hùng Giữ Suối | Guard → Warn → Attack → Return | 1 ở Linh Lâm | Kẻ mang Nghiệp | [1.0] |
| Chống snowball | Tu Sĩ Nhập Sơn (từ WORLD-10) | nhắm vào kẻ có cảnh giới cao nhất | Theo sự kiện | Kẻ mạnh | [Post] |

**Ý Chí Rừng (Director lite):**
- Áp Lực (0–100) = 0.3×(100 − HP%) + 0.3×(100 − need A thấp nhất) + 0.2×min(100, 3×số ô cách Hang/Tâm Rễ) + 0.2×min(100, 25×số kẻ thù trong 10 ô).
- Áp Lực <30 kéo dài 5' thì spawn thêm áp lực (đàn hươu, sâu, báo). Áp Lực >75 thì 3' không spawn gì mới quanh người đó và mở một "cửa thoát" (quả rơi, mưa xóa mùi).
- Mỗi 20' có ít nhất 1 đỉnh >60 và 1 đáy <25.
- **Cân bằng sinh thái:** nếu người chơi Lang >35% thì con mồi AI +50%. Nếu cây <15% thì đợt hươu −30%.
- Director cũng script FTUE và lấp rừng khi server vắng (Mộng Ảnh/Linh Ảnh).

### SURV-14b: Đe dọa môi trường
- **Đêm, Mưa, Giông/Sét** [MVP-A]: số liệu như SURV-05b. Code sét dùng chung với sét Độ Kiếp.
- **Lửa và Tro Màu** [1.0, cùng Đại Hỏa]: lửa lan 1 ô/8s trên ô khô, 1 ô/30s trên ô ẩm, không qua suối. Tán −10/s, Thân −5 HP/s. Tro cho Dưỡng Chất ×3 trong 2 ngày thực. Diễn thế 3 giai đoạn (theo PX).
- **Lũ** [Cắt].

### SURV-15c: Cái chết → Xác → Luân Hồi [MVP-A]

**Phân rã xác** (giữ R1): nhỏ 3' · vừa 6' (quạ tới sau 60s) · lớn/C4+ 12'. **Mộ Linh** (WORLD) cho mọi sinh linh C4+. **Mộc Mộ** [MVP-B] cho cây C5+: tồn tại 2 ngày thực, +2 mật độ trong 5 ô; đầu thai tại Mộc Mộ được +0.2 Gia Trì cho C1–C2.

**Hai tầng chết:**

| | **Tầng 1: Hậu Duệ** (dòng dõi) | **Tầng 2: Luân Hồi** (khai ngộ) |
|---|---|---|
| Điều kiện | Neo còn sống và chưa dùng Hậu Duệ trong 24h thực | Chọn tự nguyện, **hoặc** neo bị phá, **hoặc** chết lần 2 trong 24h, **hoặc** chết khi đang có Thiên Phạt |
| Neo | Mầm-Neo (cây) · Ổ Hậu Duệ trong Hang (thú, HP = 20% HP chủ) · [1.0] Ký Hồn Mộc (neo đặt trên cây của bạn co-op) · Bào Tử · C6: Nguyên Thần Bất Diệt (neo không phá được, vẫn 1 lần/24h) | — |
| Tiến trình | Về **Sơ kỳ 0% của đại cảnh hiện tại**, **mất tối đa 130 CT** (≈2 phiên Mid) | Về C1 của loài mới (hoặc cùng loài). **Tiền Kiếp Gia Tốc ×3** cho tới đầu cảnh giới cũ, sau đó ×1.5 tới đỉnh cũ (nằm trong trần Gia Trì) |
| Giữ | Huyết Mạch, Đạo Đồ, lãnh thổ còn lại | Túc Tuệ, Tiền Kiếp Ấn |
| Mất | Kho cá nhân | Thân, lãnh thổ, kho |
| Đạo Quả | **0** (không đi qua Trung Ấm) | 25% CT lũy kế của kiếp (+10% nếu chết trong kiếp, +25% nếu chết thành Oán Linh) |
| Sau khi chết | Hồn Hộ 10' | Trung Ấm 45s lần đầu, 8–12s và bỏ qua được từ lần sau (PX) |

**Cost of death** *(đường cong 7 cảnh là **giả định** của SURV để tính, tổng 1.670 CT giống Cửu Cảnh của PROG; PROG chốt lại)*:

| C | CT cả cảnh (giả định) | Lũy kế | Mid tới hết cảnh | Hậu Duệ mất (trung bình / tối đa) | Luân Hồi: thời gian quay lại đầu cảnh cũ (×3) |
|---|---|---|---|---|---|
| 1 | 50 | 50 | 0.16 tuần | 25 / 50 CT (0.4 / 0.8 phiên) | ≈0 |
| 2 | 130 | 180 | 0.56 tuần | 65 / 130 (1.0 / 2.0) | 0.05 tuần |
| 3 | 230 | 410 | 1.28 tuần | 115 / 130 (1.8 / 2.0) | 0.19 tuần |
| 4 | 330 | 740 | 2.31 tuần | 130 / 130 (2.0) | 0.43 tuần |
| 5 | 430 | 1.170 | 3.66 tuần | 130 / 130 (2.0) | 0.77 tuần |
| 6 | 500 | 1.670 | 5.22 tuần | 130 / 130 (2.0), luôn có Nguyên Thần | 1.22 tuần (chỉ khi bị ép Luân Hồi) |

- **Kiểm tra USP:** ở C5, Hậu Duệ tốn ≈0.4 tuần còn đổi loài tốn ≈0.77 tuần nhưng đổi lại có Đạo Quả, loài mới và Túc Tuệ (tỉ lệ ≈1:1.9, gần với 1:1.5 của PROG). Ước tính 15–20% số lần chết bị **ép** Luân Hồi (neo bị phá, chết 2 lần/24h), cộng 15–20% tự chọn, ra ≈35%. **Telemetry:** ≥35% số lần chết đi vào Luân Hồi (PROG ≥35%, PX ≥30%). Nếu thấp hơn, tăng trần Hậu Duệ lên 160 CT trước khi đụng tới những thứ khác.
- **Retention:** người chết vì PvP ở C≥4 quay lại trong 72h ≥60% (PX).

### SURV-16b: Độ Kiếp như thử thách sinh tồn công khai
- **Công Kiếp** (mặc định): mây kiếp xuất hiện 60s trước và thấy được trong 30 ô. Có Hộ Pháp, có cosmetic Pháp Tướng (PX). **Ẩn Kiếp** [MVP-A, S]: mây chỉ thấy trong 10 ô, độ khó +20%. Không cần instance.
- Tiểu Kiếp và Trung Kiếp [MVP-A]. Ví dụ Trung Kiếp: 3 đợt × 3 sét, mỗi sét 25% HP max, linh khí làm khiên theo tỉ lệ 1:1, +10%/Nghiệp. Thiên Tài Địa Bảo dùng làm Cơ Duyên. Đại Kiếp [MVP-B nếu nội dung tới C6]. Thiên Kiếp [Post].
- **Cây không chạy được nên phải chuẩn bị:** đặt rễ vào ô ẩm (−20% sát thương sét), Tích Lôi Mộc (Huyết Mạch), Mầm-Neo dự phòng.
- **Thất bại:** Đạo Cơ Tổn 20' + mất 30% CT tầng. Riêng Thiên Kiếp: Kiếp Thương + rơi 1 tầng. **Chết thật chỉ khi bị sinh vật khác giết.**

### SURV-17b: Sự kiện toàn rừng
**Quy tắc chung:** (1) Quạ Già báo trước 24h, cảnh báo 10' trước khi bắt đầu. (2) Mỗi sự kiện có **pha nền 24h** (modifier nhẹ), **đỉnh lặp lại theo chu kỳ ngày-rừng** (ai online lúc nào cũng gặp) và **1 cao trào 30' lúc 20h giờ server** (gộp PROG và PX). (3) **Offline thì miễn.** (4) Mỗi sự kiện có kẻ thắng và kẻ thua theo giới.

**Lịch năm-rừng 8 ngày:** Xuân ngày 0–2 · Hạ 2–4 · Thu 4–6 · Đông 6–8.

| Sự kiện | Khi nào | Pha nền 24h | Đỉnh lặp | Cao trào 30' | Ai khổ | Ai lợi | Di sản | Nhãn |
|---|---|---|---|---|---|---|---|---|
| **Linh Triều** | Ngày 1 và ngày 5 mỗi năm (12 lần/Kiếp) | Linh Mạch +1 mật độ (+0.15 Gia Trì khi đứng trên mạch) | Mỗi bình minh game (3'): +2 mật độ, Linh Quang ×3 | Linh Nhãn mở ở Linh Lâm (L4) | Không ai, nhưng PvP dồn về một chỗ | Ai chiếm Linh Mạch. Cây có rễ trên mạch hưởng mà không cần đi | — | [MVP-A] |
| **Đại Hạn** | Ngày 3 (Hạ) | Thủy decay ×2 ban ngày, ô ẩm chỉ tính ×0.5 trong W, suối hẹp lại | Mỗi trưa game (4'): thú tụ về suối | Hỏa Nhật: Thủy ×2.5 | Cây | Lang (suối thành bãi săn), Thử (quả rụng sớm) | Cây online qua ≥3 đỉnh: **Hạn Căn** −20% Thủy decay cho cả kiếp | [MVP-A] (chỉ là modifier và palette, trong ngân sách S của PX) |
| **Huyết Nguyệt** | Ngày 7 (Đông) | Kẻ săn AI +50% ở Bìa | Mỗi đêm game (6'): Huyết Báo ở Trung Lâm/Linh Lâm, **không ra Bìa**. Con mồi ×2 linh khí khi g≤0 | Huyết Báo Vương ở Linh Lâm, Linh Hạch ×1.5 | Linh Thử | Lang, Quạ. Cây nhận xác thành Dưỡng Chất | Linh Hạch yêu thú. Người có Ấu Linh được báo trước 1 ngày-rừng | [MVP-A] |
| Sâm Lâm Hỏa Kiếp | Hạ/Thu, do sét | | | | Cây, ổ trên mặt đất | Nấm, cây non sau đó | Tro, diễn thế, lối vào bí cảnh | [1.0] |
| Thú Triều | 2 lần/Kiếp | | | | Thú nhỏ | Cây, kẻ ăn xác | | [1.0] |
| Trùng Tai | Xuân | | | | Tán cây | Thử, cây có kiến | | [1.0] |
| Đại Di Cư · Khô Mục Xâm Lấn · Tu Sĩ Nhập Sơn | | | | | | | | [Post] |

Độ phủ: 4 ngày có sự kiện trong mỗi 8 ngày. Người chơi Mid (5 phiên/tuần) gặp sự kiện ở khoảng 2–3 phiên mỗi tuần, vượt mục tiêu 85% số tuần của PROG.

### SURV-18b: Item sinks [MVP-A] và Thiên Tài Địa Bảo [MVP-A lite]
- **Sinks:** Linh Hạch tự tan sau 30' (quạ lấy sau 90s nếu bị bỏ) · thịt trong kho thối sau 10' · quả rụng mất sau 5' · 20% hạt chôn ngoài Hang bị quên · ô rễ teo khi Thủy <30 (−1 ô/ngày-rừng) · Thiên Tài Địa Bảo không dùng thì tan sau 24h thực.
- **Thiên Tài Địa Bảo** (thay cho lớp Luyện Hóa của R1): 3 loại, dùng làm Cơ Duyên cho đột phá (PROG-07). Linh Thảo ở Trung Lâm, 1/vùng/ngày-rừng. Huyết Tinh rơi từ Huyết Báo. Lôi Mộc Tâm chỉ có trên cây vừa bị sét đánh. Dùng Luyện Hóa để lấy kháng tính hoặc vật liệu Hang là [1.0].

### SURV-20: Thực Sát / Lạm Sát [MVP-A, chỉ là luật dữ liệu, S]
Giết rồi ăn ≥50% phần của kẻ ăn trong 60s thì trục Sát của Tâm Hướng chỉ nhận ×0.3. Giết mà không ăn thì ×1.0. Khớp với ý của PROG "Sát đo so với baseline của loài": sói đi săn bình thường không bị phạt kép.

### SURV-21: Cái chết đầu tiên đọc được (FTUE) *(gộp WORLD-PX-08 với Thọ Nguyên của SURV; PX sở hữu)*
Linh Thử FTUE có thanh **Thọ Nguyên 12'** hiện rõ, và mang một hạt trong bụng từ lần ăn Linh Quả của cây Lão Tùng. Ở phút 11, người chơi chọn: **dụ Lang AI ra xa ổ** để cứu bầy (nhận Đạo Quả ×1.5), hoặc **chết già dưới gốc cây**. Cả hai đường đều kết thúc bằng việc hạt nảy mầm từ xác, và lựa chọn đầu thai mặc định là "trở thành hạt giống ngươi đã mang". Cái chết vẫn chắc chắn xảy ra, nhưng là **lựa chọn có lý do**, không phải bị script giết.

### SURV-22: Resource Table và scarcity curve [MVP-A]

| Tài nguyên | Vòng | Tier | Dùng cho (≥2 cách) | Respawn | Sink / đánh đổi |
|---|---|---|---|---|---|
| Cỏ dại | Bìa, Trung | 0 | No của Thử (+3), mồi cho Hươu AI | 60s/ô. Gặm trụi thì ô trống 3' | Hươu AI tranh ăn |
| Hạt | Bìa, Trung | 0 | Thử ăn (+8) **hoặc** chôn vào kho | Mỗi cây AI rơi 1 hạt/2'. Đông ×0.3 | Bị quên thì nảy mầm |
| Quả / Linh Quả | Cây AI và cây người chơi | 1 | No +15, linh khí +3 (Linh Quả từ cây C3+ cho +10). Phát tán hạt cho cây | Cây AI 1 quả/3' | Rụng mất sau 5'. Cây người chơi trả 15 Quang Tinh mỗi quả |
| Sâu | Trên tán | 0 | Thử +6 No, đồng thời giúp cây | Theo luật Tán | — |
| Thịt / xác | Mọi nơi | 1 | Lang No. Đất (Dưỡng Chất + Q vùng). Quạ | Từ kẻ săn AI, Director bảo đảm sàn | Thối sau 10'. Xác phân rã 3/6/12' |
| Nước | Suối, ô ẩm, mưa | 0 | Thủy của cây. Suối là điểm tụ của thú khi Đại Hạn | — | Đại Hạn làm suối hẹp |
| Ánh sáng / Vệt Nắng / Linh Quang | Tán | 0 | Quang Tinh, linh khí | 1 vệt/50s, Linh Quang 1/3' | Bị cây cao hơn che |
| Dưỡng Chất | Đất màu (20% ô ở Trung Lâm), xác, phân, hạt bị quên | 1 | Lớn cây, ra hạt | — | Tiêu khi lớn |
| Linh khí môi trường | L0 → L4 theo vòng, Linh Mạch, Linh Tuyền (2–3 điểm/map, +20/lần hút, CD 5') | 1–3 | Skill, khiên kiếp, Đả Tọa, hồi thương, Linh Hóa Địa | Q vùng | Tải vùng |
| Linh Hạch | Xác người chơi và AI từ C2 trở lên | 2 | 4 CT × m(g), hoặc Cơ Duyên phụ | — | Tan sau 30', quạ lấy |
| Thiên Tài Địa Bảo | Trung, Linh Lâm | 3 | Cơ Duyên đột phá, [1.0] kháng tính | Xem SURV-18b | Tan sau 24h |

| Giai đoạn | Thứ khan hiếm (người chơi sợ mất) | Thứ dư |
|---|---|---|
| C1–C2 (Bìa) | No, Thủy, sự an toàn trước kẻ săn AI | Cỏ, hạt |
| C3–C4 (Trung) | Linh khí, Q vùng, Linh Mạch, Mầm-Neo | Thức ăn cơ bản |
| C5–C6 (Linh Lâm) | Thiên Tài Địa Bảo, Linh Nhãn, Linh Hạch | Thức ăn, lãnh thổ ngoài |
| Đông, mọi giai đoạn | Thức ăn (Thử, Lang), ánh sáng (cây) | — |

---

## 3. Những thứ tôi mượn từ người khác
- **PROG:** CT là đơn vị gốc, Sinh Năng = 20 CT, Gia Trì trần ×3, offline 0 CT, Thiên Đạo Luật (PROG-12b), Đạo Cơ Tổn, rễ ×1.6, công thức Thủy hàm mũ, Đả Tọa 1:1, Áp Chế, mốc ≥35% chọn đổi loài.
- **PX:** ngân sách UI 4+1 và 5 nút, trần 130 CT, miễn sự kiện khi offline, Vệt Nắng thành cửa sổ thưởng, Công Kiếp/Ẩn Kiếp, Trung Ấm rút ngắn, cắt 4 archetype và 2 thời tiết, Linh Thử là loài MVP, Ngủ Đông chỉ khi offline (tôi cắt hẳn).
- **WORLD:** Quỹ Linh Vùng (WORLD-03b), Hậu Duệ về đầu cảnh hiện tại và 0 Đạo Quả ("dòng dõi hay khai ngộ"), glossary, FTUE "chuột mang hạt → cây mọc từ xác", Mộ Linh, Ý Chí Rừng là giấc mộng của Kiến Mộc, Quả Ước, ánh xạ 3/2/2.

## 4. Lập trường giữ vững (và vì sao)
1. **7 cảnh giới, không phải 9.**
   - (a) Luật tech tree: mỗi đại cảnh giới phải mở một khả năng mới về chất. C7 Phản Hư và C8 Hợp Đạo của Cửu Cảnh hứa Linh giới và Lĩnh Vực, cả hai đều là tính năng XL thuộc [Post]. Hai cảnh đó sẽ là "cảnh chỉ có số" ở bản ra mắt.
   - (b) Ba vòng Q vùng/mật độ và ba cấp rừng ánh xạ 3/2/2 sạch sẽ.
   - (c) Lập luận nhịp của PROG (2.5–4.4 phiên/cảnh) vẫn đạt được với 7 cảnh × 3 tầng: ở C5–C6 mỗi **tầng** là 2.2–2.6 phiên, và tầng có Tiểu Kiếp làm mốc.
   - **Điều kiện để tôi đổi ý:** sim hoặc playtest cho thấy D7/D14 sụt quanh C5–C6 vì "dry spell", hoặc PROG chứng minh khoảng cách giữa các tầng >3 phiên Mid. Phương án lai tôi chấp nhận: giữ 7 tên đại cảnh, cho C5–C6 có **4 tầng**.
2. **Hậu Duệ phải tồn tại và có trần.** Rơi cả 1 cảnh giới như PROG đề xuất là phạt retention. USP luân hồi được bảo vệ bằng phần thưởng (Đạo Quả, loài mới) và giới hạn (1 lần/24h, neo phá được), không bằng cách làm Hậu Duệ đau.
3. **g theo cảnh giới thật.** Nếu tính sau Áp Chế, Thiên Đạo Luật bị lách đúng ở nơi người mới đông nhất.
4. **Tâm Rễ không bị đòn thường chạm tới, và cây Đổ cần ≥40s.** Đây là điều kiện sống còn của USP "chơi cây".
5. **Mỗi sự kiện có kẻ thắng và kẻ thua theo giới**, và cổ thú/Huyết Báo **không bao giờ ra Bìa Rừng**.
6. **No vẫn nhận đủ khi g≥2.** Sinh tồn là thật, chỉ có tu vi bị Thiên Đạo cắt. Như vậy "cá lớn nuốt cá bé" vẫn tồn tại, nhưng không còn sinh lời.
7. **Thiên Kiếp thất bại vì sét không giết người chơi.** Chỉ sinh vật khác mới giết được người đang độ kiếp.

## 5. Điều tôi sẵn sàng đánh đổi
- **Scope domain SURV ở MVP-A ≈ 15 tuần-người** (PX ước tính bản đầy đủ là 45): cây lite L, needs cho 3 loài + mùa + 2 thời tiết M, 4 AI + Director M, 3 sự kiện S+, sổ Sinh Năng + xác + Q vùng S, luật offline S, Hang cấp 1 + Kho Hạt S. Nếu vượt ngân sách, thứ tự cắt là: **Đại Hạn sang 1.0** → **Q vùng chuyển thành mật độ tĩnh theo vòng** (mất lớp theme, giữ được gameplay) → **Ẩn Kiếp**.
- **PvP người thật lùi sang MVP-B** (PX). Tôi chấp nhận, với điều kiện MVP-A dùng Director + Mộng Ảnh để mô phỏng chuỗi thức ăn, và MVP-B phải kiểm chứng được H5 (≤10% số kill ở chênh ≥2).
- **Trần Hậu Duệ** có thể tăng từ 130 lên 160 CT nếu tỉ lệ chọn đổi loài <35%.
- **Đường cong 7 cảnh** trong SURV-15c là giả định. PROG được tự do phân bổ lại 1.670 CT. Tôi chỉ cần giữ ba ràng buộc: Hậu Duệ ≤2 phiên, Luân Hồi tới C5 ≤1 tuần, 1v1 vượt 1 cảnh thắng ≤25%.
- **Cách gọi tên** neo, sự kiện, archetype: giao toàn bộ cho WORLD.
