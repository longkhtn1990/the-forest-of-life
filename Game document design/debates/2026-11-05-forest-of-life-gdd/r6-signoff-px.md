# R6 Sign-off — PX
**Verdict:** BLOCK (3 blocker nhỏ, mỗi cái có đoạn thay thế viết sẵn, sửa xong là APPROVE-WITH-NOTES. Không cần debate lại.)

Phần lớn FINAL đã đúng với R3/R4 của tôi: persona, USP, hook, đối thủ, server, offline 0 CT, ví và exploit, monetization, tech, B′, cổng tuần 16/30, risk register, H1–H13, KPI. HUD thú [orch] cũng đúng theo SURV-01b (HP · Linh Khí · No · Thể Lực quanh joystick, không có Thủy).

---

## Blockers

| # | Vị trí trong FINAL | Vấn đề | Sửa cụ thể (đoạn thay thế viết sẵn) |
|---|---|---|---|
| B1 | §5.9 bảng Bế Quan, dòng 1 (và D8) | **Lỗ combat-log làm hỏng PvP với cây.** Luật hiện tại cho "Bế Quan ngay" khi thoát trong Hang hoặc lãnh thổ rễ, kể cả khi đang bị đánh. Cây thì *luôn* đứng trong lãnh thổ của mình. Tình huống: 3 Lang + Độn Thử phối hợp (đúng như §4.3 yêu cầu), tới giây 15 người chơi cây tắt tab, cây thành bất tử. TTK 17s/50s, vai trò "loài duy nhất giết thật được cây" của Độn Thử và Sinh Năng từ xác cây đều mất tác dụng. Thú bị đuổi chạy vào Hang rồi thoát cũng vậy. Lỗ này có từ R3 của tôi và SURV. Tôi nhận phần lỗi | Thay dòng 1–2 của bảng §5.9 bằng: <br>`| Thoát trong Hang/lãnh thổ rễ **và** không gây/nhận sát thương, không có kẻ địch người chơi trong ô rễ/Hang trong 30s gần nhất | **Bế Quan** ngay. Thú rời thế giới, cây thành bất tử |` <br>`| Mọi trường hợp khác (đang combat, ngoài lãnh thổ, rớt mạng) | **Nhập Định** 30s (60s nếu vừa combat). Thân vẫn bị tấn công được. Thú tự chạy vào bụi/hang ≤5 ô (PX-18). Cây chạy phòng thủ thụ động như khi AFK (Gai, kiến). **Không Bế Quan được khi đang độ kiếp hoặc đang Mộc Tàn** |` <br>Thêm vào D8, cột Lý do: *"…và chỉ được Bế Quan khi đã 30s không combat (chống combat-log)."* Hệ quả cho cây rớt mạng giữa trận: tệ nhất là **Đổ** (TTK AFK 35s), không chết, vì Tâm Rễ chỉ nhận Căn Thương. Mức giá đó chấp nhận được |
| B2 | §5.1 hàng Linh Mộc, so với §6.5 và §13 | **Ngân sách nút của cây mâu thuẫn với chính FINAL.** §13 và §6.5 ghi "3 skill + 1 Thần Thông trên mọi nền tảng", "Từ C4 có 4 kỹ năng chủ động nên phải bỏ 1". Nhưng §5.1 đã dùng hết 5 nút của cây cho Phòng thủ (bánh xe) · Hạt · Quả · Cộng sinh · Linh Thức, không còn ô cho A1/A2 (vd Vỏ Gai, Căn Tỏa của Thiết Mộc) và cũng không còn ô Thần Thông ở U1. Nguyên nhân: B′ đưa Linh Thức vào chỗ của Thần Thông trong SURV-01b. Nếu tính đủ động từ, cây cần khoảng 9–10 nút, vượt trần ≤5 | Thay ô "Nút (≤5)" của hàng Linh Mộc ở §5.1 bằng: <br>*"**3 ô chủ động** (loadout: Bản Năng 1–2 của cây là Gai Bạo / Độc Tiết / Vỏ Cứng, A1–A2 từ Huyết Mạch thay vào) · **Sinh Trưởng** (1 bánh xe: Hạt · Quả · Cộng sinh · Linh Thức) · **Thần Thông** (ô khóa tới U1, hiển thị như mục tiêu). Chạm map để bắt Vệt Nắng, kéo để vươn rễ (là cử chỉ, không chiếm nút). Đả Tọa/Độ Kiếp/Bế Quan nằm trong menu ngữ cảnh."* <br>Ở §4.3 đổi "slot phòng thủ 1/2" thành "Bản Năng (ô chủ động)". Lý do UX: động tác cần phản xạ (phòng thủ) có nút riêng, động tác chậm và có chủ đích (gieo, kiến, Linh Thức CD 3') đi qua bánh xe, mất thêm 1 chạm. PROG xác nhận pool 4 Bản Năng của cây |
| B3 | §16.3 Lịch | **Lịch vẫn dùng bản R3 (44 tuần + 6 tuần đệm)**, không khớp §16.1 (45,75 + 4,25). Beta kết thúc ở tuần 44, trong khi khối lượng việc kéo tới giữa tuần 46. Bảng lịch đang hiện đệm 6 tuần, còn phần chữ ghi 4,25 | Thay 2 dòng cuối bảng §16.3: <br>`| Beta | 35–46 | UI/accessibility, ads/shop, telemetry. Open beta itch.io qua 1 chu kỳ 28 ngày (tuần 42–46) |` <br>`| Đệm + soft launch | giữa 46–50 (~4,25 tuần) | Web: CrazyGames + itch.io + site riêng (Poki nếu được duyệt) |` |

---

## Notes (không chặn)

**N1. Ấu Linh thiếu 2 ràng buộc của PX R4 C5 (nên sửa cùng đợt).** FINAL chưa nói khiên gắn với tài khoản hay với kiếp. Lập trình viên làm một mình gần như chắc chắn sẽ lưu trạng thái theo nhân vật. Khi đó một alt Luân Hồi liên tục sẽ có lại khiên và thoát khỏi Thần Thức ở mỗi kiếp, tức đúng exploit mà D5 viện ra để loại phương án C. Thêm vào §8 bullet Ấu Linh: *"Khiên gắn với **tài khoản**: đồng hồ 3h chỉ đếm thời gian online trong Rừng chung (FTUE và Rừng riêng không trừ). Hậu Duệ, Luân Hồi và vé Tự Quy **không** nạp lại khiên. Mốc 'hết C2' là lần đầu tài khoản chạm C3."*

**N2. Scope bị lọt mà chưa tính giờ.** Các mục sau có nhãn MVP nhưng không có dòng chi phí: Quạ Linh (archetype thứ 4, #7 vẫn giữ 2 tuần như khi có 3 archetype), Linh Tức (#17 vẫn 1 tuần như khi có 2 sự kiện), 2 Linh Mạch Huyệt, 3 Thiên Tài Địa Bảo, bot "Linh Ảnh". Tôi ước khoảng +0,5–1 tuần, nên đệm thực tế còn ~3,25–3,75 tuần (6,5–7,5%). Đề xuất: (a) ghi vào §16.1 #7: *"Linh Ảnh MVP = reskin archetype AI với Đạo hiệu và aura Mộng Hỏa, không có hành vi giả người chơi"*; (b) Thiên Tài Địa Bảo MVP chỉ giữ **Linh Thảo**, đưa Huyết Tinh và Lôi Mộc Tâm sang U1; (c) Risk register ghi "đệm thực ~7%".

**N3. Tỉ trọng nguồn CT ở §14.1 sai theo chính công thức của FINAL.** Mid chơi 40'/phiên, Mộng Tích cộng +1 trong 30' đầu → 30/(40+30) ≈ **43%** CT đến từ Mộng Tích, không phải ~20%. P1 chơi phiên 10–20' thì tỉ trọng ≈50%. Sửa sơ đồ thành: *"chơi tích cực ~50% · Mộng Tích ~40% · sự kiện ~5–8% · PvP ≤5%"*. Không cần đổi thiết kế: con số này cho thấy P1 được nâng đỡ tốt. Nhưng telemetry "tỉ trọng nguồn CT" phải dùng ngưỡng mới, nếu không sẽ báo động giả.

**N4. Kinh tế Đạo Quả trong MVP.**
- (a) Ba node chỉ hút tổng 600 Đạo Quả. Mid ở MVP kiếm khoảng 300–400 mỗi chu kỳ 28 ngày, Core khoảng 600. Phần dư "chảy vào Tiền Kiếp Ấn", nhưng Tiền Kiếp Ấn là [U1], nên trong MVP Core sẽ tích Đạo Quả không có chỗ tiêu sau khoảng 1 chu kỳ. Thêm vào §7.3: *"MVP: Đạo Quả dư được giữ lại cho loài thứ 4 và Tiền Kiếp Ấn ở U1. Trung Ấm hiện 'X Đạo Quả đang chờ hạt giống mới'."*
- (b) Ad "Đạo Quả +30%" ở solo dẫn tới Túc Tuệ ô 2, tức mang 2 Notable vào PvP. Đây là một đường từ ad tới sức mạnh, dù nhỏ. Thêm điều kiện cho Túc Tuệ ô 2: *"cần ≥3 lần Luân Hồi"*. Ad không tăng tốc được điều kiện này.

**N5. Fallback §16.1.**
- (a) Thiếu **cổng tuần 2** (điều kiện đổi ý ở R4 của tôi): *"Spike Colyseus/Phaser tốn hơn kế hoạch >1 tuần thì về phương án D ngay, Kiến lên U1."*
- (b) "Map 3 vòng → 2" sẽ làm Phi Thăng Kiếp I không còn chỗ để tới. Sửa thành *"…→ 2 vòng, **Thâm Lâm thu thành enclave ~64×64 quanh Linh Nhãn**"*.
- (c) Sau "chỉ giữ Đại Linh Triều" cần ghi rõ: *"reset ngày 28 vẫn chạy, chỉ bỏ nghi lễ. Vẫn trả Đạo Quả và Biên Niên dạng chữ"*.
- (d) Ghi số tuần tiết kiệm cho từng mục cắt: HHM 0,25 · Kiến 1 · Linh Quỹ ~0,5 · mùa ~0,25 · sự kiện 0,5 · map 1 · shop 0,5 · Huyết Mạch 1 · Linh Thử 1.
- (e) Lùi 6 tuần nghĩa là tổng 56 tuần ≈ 13 tháng, vượt G4 1 tháng. Ghi điều này vào Q2/Q7 để người dùng biết.

**N6. Retention/live-ops (deliverable #12 của brief) đang mỏng.** Bảng hook D1/D7/D30 và nhịp nội dung của PX-15b không có trong FINAL. Đề xuất thêm §14.3:
> | Mốc | Hook MVP |
> |---|---|
> | D1 | Mộng Báo "Tán đã lành", Mộng Tích đầy, Giới Bia Thâm Lâm hiện mục tiêu |
> | D7 | Đại Linh Triều đầu tiên, Mid qua Phi Thăng Kiếp I (1,1 tuần), Huyết Sát bounty |
> | D30 | Đại Kiếp lite, Biên Niên tổng kết, Thần Bia, chu kỳ mới |
>
> Nhịp vận hành: 1 bộ skin mỗi Kỷ Nguyên, 1 update lớn mỗi 2 Kỷ Nguyên, ops ≤6h/tuần, mọi sự kiện tự động.

**N7. Thêm giả thuyết H14** (điều kiện đổi ý C5 của tôi): *"Lang ở Bìa/Trung Lâm có ≥1 cuộc săn PvP hợp lệ mỗi 20'. Ấu Linh chiếm ≤50% số con mồi người chơi ở Bìa. Alpha."* Nếu trượt thì P2 không có mồi.

---

## Nhất quán số liệu (PX tự kiểm)
| Kiểm tra | Kết quả |
|---|---|
| Tổng §16.1 | 2+4+2,5+1+3,25+1,25+1+0,25+1+2+0,75+3+1,5+1,75+2,5+1,5+1,5+4+1,5+2,5+1+1+0,5+1+3,5 = **45,75 ✓** |
| B′ so với R3 | 44 + (0,75+1,25+1+0,25) − (0,75 KHST + 0,5 mùa + 0,25 Bàn) = **45,75 ✓**. Đệm 4,25/50 = **8,5% ✓** |
| Nội dung B′ | Linh Quỹ (sàn Bìa 50%, 2h) ✓ · Linh Thức 60s/30 ô, mất 1 Vệt Nắng ✓ · Kiến 2 tổ, −3 HP/s, −1 QT/phút ✓ · HHM ×1,3, gai +1 ✓ · "Tán sẽ tự lành" ở FTUE, Mộng Báo và session mẫu ✓ · 4 palette, modifier Xuân/Đông ✓ · 3 node ✓ |
| Cổng 16/30 | Khớp R4 ✓. VS 3–14 + kiểm định 14–16 ✓. Closed alpha tuần ~30 ✓ |
| Lịch §16.3 | ✗ (B3) |
| Unlock §6.3 | 156/64 = 2,4 → phiên 3 ✓ · 366/64 = 5,7 → phiên 6 ✓ · 691/64 = 10,8 → phiên 11 ✓ |
| Trần chi phí chết | Hậu Duệ 0,83–1,16 (tệ nhất 1,35) ≤1,5/≤3 ✓ · Luân Hồi C5 0,82 tuần ≤1 ✓ · C6 1,28 ≤1,5 (D19) ✓ |
| Tỉ trọng nguồn CT §14.1 | ✗ (N3) |
| Ràng buộc cứng brief §2 | Solo/co-op/server ✓ · 3 cấp rừng + vòng + rừng biến đổi ✓ · luân hồi đổi loài, giữ meta, xác thành dinh dưỡng ✓ · tên cảnh theo loài, cấp tương đương ✓ · 4/4 cách chơi thực vật trong MVP ✓ (fallback cổng 16 có thể còn 2/4 ở MVP, cả game vẫn đủ, Q2 đã hỏi người dùng) · PvP luôn bật ở Rừng chung ✓ (hiện bị B1 làm thủng với cây) · Web/Mobile/PC ✓ · 2D/2.5D ✓ · session 15–60', nhiều tuần ✓ · 1 người + AI, F2P ads/skin/pass ✓ (Pass ở U1) |

## Dissent ghi nhận
- **Hồi Ức nằm ngoài trần Gia Trì (D4):** tôi **rút** phương án lai ở R4. Lập luận của PROG đúng: để Hồi Ức trong trần thì Luân Hồi ở C5 mất 1,38 tuần, vượt chính trần của tôi. Không dissent.
- **D2 Đạo Quả/Đạo Tâm:** giữ dissent như §20.1. Người dùng chốt ở Q1. Tôi vẫn khuyến nghị làm test 5 giây (0,1 tuần) trong VS.
- **D19:** giữ dissent nhẹ như §20.1, không đổi.
