# R1 Proposal — PROG

## 1. Cách tôi hiểu yêu cầu
Tôi lo phần khung số của spec Linh Nghĩ: tầng nào mở cái gì, mỗi tầng chỉ số bao nhiêu, CT đến từ đâu, Đạo Lộ đổi thao tác ra sao, và cân bằng có đứng vững không. Giả định: nhịp Mid giữ v1.2 (218' tới Viên Mãn, ~1,6 CT/phút), chỉ số ×1,10/tầng, không thêm need. Sim: `sim/prog_r1_nghi_sim.py` → `sim/prog_r1_nghi_sim_output.md`.

## 2. Hook
**"Bầy lớn dần theo đường mòn của ngươi":** cứ mỗi 10–30', người chơi có thêm một con Lính, một lệnh mới hoặc một cái tổ mới, chứ không chỉ có thêm số.

## 3. Đề xuất chi tiết

### PROG-01: Unlock Timeline 12 tầng (Mid, không chết)
| Tầng | Phút | CT tầng | Mở khóa (**mới** = đề xuất R1) |
|---|---|---|---|
| C1 Sơ | 0 | 6 | Hậu + **1 Lính**, Tha (Hậu tha 1 vật nhỏ), BN1 Xung, Hy Sinh, Tổ |
| C1 Trung | 3,7 | 7 | **Lính thứ 2 nở** · M1 (Bậc I) |
| C1 Hậu | 7,9 | 7 | **Mở Xác** (động từ solo) |
| Kiếp C1→2 | 12,2–14 | 3 | Tiểu Kiếp · **Thoát Xác #1** (lần đầu thấy luật "lột vỏ = hồi đầy, vỏ thành mồi") · M2 (+Hậu Mẫu) |
| C2 Sơ | 14 | 15 | BN2 Toan Dịch · **Lính thứ 3** · **Tha Bầy** (xác/vật lớn, ≥2 Lính khiêng) · co-op |
| C2 Trung | 23,5 | 16 | **Sai Lính** (PROG-02) ×1 |
| C2 Hậu | 33,6 | 18 | **Gác Tổ**: để 1 Lính ở lại Tổ, báo khi có kẻ vào 8 ô; Lính đó không tính vào Công |
| Kiếp C2→3 | 44,9–50 | 8 | Tiểu Kiếp · **Thoát Xác #2** · M3 |
| C3 Sơ | 50 | 27 | A1 Đục Rễ + **Căn Thương**, hết Ấu Linh, Trọng Thương |
| C3 Trung | 67 | 30 | **Sai Lính ×2** |
| C3 Hậu | 85,8 | 33 | M4 |
| Kiếp C3→4 | 106,6–116 | 15 | Phi Thăng Kiếp I · **Thoát Xác #3** · M5 |
| C4 Sơ | 116 | 42 | Đục Rễ Thăng, Thâm Lâm / Đầm Mục, Giữ bến |
| C4 Trung | 142 | 46 | **Sào Bến**: Tha 20 vật tới một bến cạn để dựng tổ tạm (hồi sinh Lính, Bế Quan). Mỗi đời 1 cái, mất khi bị phá |
| C4 Hậu | 171 | 52 | M6 (+Hợp Đạo) · **Tích Sào**: mỗi 10 vật Tha vào Tổ = 1 **Trứng Hộ Kiếp** (tối đa 2), nở thành Lính tạm chỉ trong Kiếp Viên Mãn |
| Kiếp Viên Mãn | 203,6–218 | 23 | Ở Tổ. Vỏ cuối = Hóa Tích |

- **Dry spell:** v1.2 chỉ có M2→M3 (36' ở C2, trong đó chỉ có BN2) và C4 (116→171, 55'). Sau khi lấp, khoảng dài nhất là 29' (142→171). Đoạn 171→204 (33') là giai đoạn chuẩn bị kiếp nên đã có mục tiêu (Tích Sào).
- **Mâu thuẫn v1.2:** §6.2 ghi *"Lập Sào bắt đầu Tha"* nhưng §4.2/§6.3 lại mở Tha ở C1. Cách sửa: C1 là Hậu tha 1 vật, C2 Lập Sào là **Tha Bầy**.
- Lính đi 1 → 2 → 3, khác v1.2 (C1 có 2 Lính ngay) để giảm tải lúc onboarding và giảm No ở đoạn khó nhất (§5.11).
- **Chi phí:** Sai Lính 0,10 t-n (dùng lại AI swarm Kiến) · Tha Bầy 0,05 · Sào Bến 0,05 (dùng lại entity Tổ/Tổ Phụ) · Tích Sào 0,04 · Gác Tổ 0,03 · đổi số Lính 0 (data). **Tổng ≈0,27 t-n.** Cắt theo thứ tự nếu thiếu: Gác Tổ → Tích Sào → Sào Bến. Bù lại: bỏ dòng Phụ "Ăn tại Tổ No ×1,25". PX chốt.

### PROG-02: Sai Lính, núm vặn kinh tế ↔ chiến đấu
- Giao 1 vật cho Lính, Lính tự tha về Tổ và quay lại. Mỗi chuyến cho **50% CT** của Hậu tha (0,125 CT).
- Trong lúc đi, Lính không cộng Công (−0,15×) và đi lẻ nên dễ bị Nha Bổ Nhào hoặc Oa Quăng Lưỡi.
- Đây là quyết định thật mỗi phút: muốn tu nhanh thì yếu khi bị đánh. Nó cũng là vòng hub–spoke mà §4.2 hứa nhưng v1.2 chưa có thao tác. Input do PX làm.

### PROG-03: Số liệu theo tầng (sim A/B)
| Tầng | HP Hậu | HP Lính | Công Hậu | Lính | Công hiệu dụng | DPS chuẩn* |
|---|---|---|---|---|---|---|
| C1 Sơ | 300 | 36 | 22,0 | 1 | 25,3 | 26 |
| C1 Hậu | 363 | 44 | 26,6 | 2 | 34,6 | 36 |
| C2 Sơ | 399 | 48 | 29,3 | 3 | 42,5 | 48 |
| C2 Hậu | 483 | 58 | 35,4 | 3 | 51,4 | 58 |
| C3 Sơ | 531 | 64 | 39,0 | 3 | 56,5 | 69 |
| C3 Hậu | 643 | 77 | 47,2 | 3 | 68,4 | 83 |
| C4 Sơ | 707 | 85 | 51,9 | 3 | 75,2 | 93 |
| C4 Hậu | 856 | 103 | 62,8 | 3 (4 nếu có Lính Thứ Tư) | 91,0 | 113 |
*Đánh thường + Xung (4/10s) + Toan Dịch + Đục Rễ/Thăng, đánh mục tiêu đứng yên.

- **CD cố định** (không đổi theo tầng): Xung 10s (chạy 4s) · Toan Dịch 12s · Đục Rễ 14s · Hầm Ngầm 25s · Mạch Tổ 90s.
- Hy Sinh hồi 2% (C1 Sơ) lên 4% (C4 Hậu), nội suy theo n.
- **Lỗ hổng:** v1.2 cho hồi Lính "tại chỗ mất 6 No" mà không có CD, nên chỉ cần có No là có thể đổi No lấy HP vô hạn. Đề xuất: kênh 1,5s, trong giao tranh tối đa 1 Lính/8s, ngoài giao tranh không giới hạn.

### PROG-04: Nguồn CT theo giai đoạn (sim C, đã hiệu chỉnh ±12% quanh 1,6 CT/phút)
| Cảnh | CT/phút | Tha + ăn | Mở Xác | Căn Thương + săn | Thay đổi chính |
|---|---|---|---|---|---|
| C1 | 1,50 | 77% | 16% | 8% | Ăn tại chỗ, tha 8 ô |
| C2 | 1,68 | 72% | 21% | 8% | Tha Bầy, Sai Lính, tha 14 ô |
| C3 | 1,77 | 64% | 20% | 16% | Căn Thương, săn bằng Xung |
| C4 | 1,72 | 55% | 28% | 17% | Đầm: xác tan nhanh nên Mở Xác lên cao nhất |
| **Cả đời** | | **61%** | **24%** | **15%** | v1.2 ghi 45/30/25 |

- CT mỗi lần: ăn 0,10 · Hậu tha 0,25 · Tha Bầy 0,70 · Mở Xác 0,60 · săn 0,20 · Căn Thương 3,0/lượt 50s.
- **Đề xuất sửa §6.9 thành ~60/25/15.** Căn Thương cần cây đang Mộc Tàn, mà sự kiện này hiếm, và Đất Xới thì cần có Nha. Giữ 25% thì người chơi solo bị thiếu CT.
- **No:** thời gian không giới hạn được No (vào 19–38/phút so với decay 5–6). Vậy áp lực phải đến từ **mật độ thức ăn**. Tôi cần SURV chốt mật độ để No vào ≈1,2–1,5× decay. Phần dư vào Kho cho mùa Đông.

### PROG-05: Bốn archetype Đạo Lộ
| Build | Fantasy | Đường thẻ (M1→M6) | Thao tác thay đổi | Mạnh / yếu |
|---|---|---|---|---|
| **Vạn Quân** | Bầy nghiền nát | Hàm Thép → Lính Thứ Tư → Hậu Mẫu → Vạn Nghĩ Xung → Hầm Ngầm → Đoàn Quân | Canh Xung 6s, giữ 4 Lính sống, quản No để hồi Lính | DPS cao nhất (×1,25) / tốn No nhất (−6,7/phút), sợ Gai AoE |
| **Hầm Sư** | Mạng hầm dưới đất | Hầm Ngầm → Tổ Phụ → Lính Đỡ → Hàm Thép → Lính Thứ Tư → **Mạch Tổ** | Chọn chỗ đặt tổ phụ, chui né đòn, dịch chuyển giữa các tổ | Gần như không thể bị bắt / DPS thấp, phải ở gần tổ |
| **Đoàn Tha** | Hậu cần, nuôi rừng | Vai Rộng → Đường Mùi → Kho Tổ → Hậu Mẫu → Hàm Thép → Đoàn Quân | Tha 2 vật, vạch đường mùi, Sai Lính liên tục | CT cao nhất (Tha ×1,2 ≈ +7% tổng CT), mạnh khi đi party / yếu khi solo PvP |
| **Phục Kích** | Trồi lên từ lòng đất | Hầm Ngầm → Hàm Thép → Lính Thứ Tư → Tổ Phụ → Vạn Nghĩ Xung → **Hầm Phục** | Chui xuống, áp sát, trồi lên Xung miễn phí 2s | Burst mở màn / lộ bài khi Hầm Ngầm đang CD |

- **M1** quyết định động từ thứ 4 của người chơi: chui hầm, đánh mạnh hơn, hay tha 2 vật.
- **M2** là lúc chọn: lấy Lính Thứ Tư (đánh), Tổ Phụ (lãnh thổ) hay Hậu Mẫu (kinh tế No).
- **M6** chọn Hợp Đạo, nối 2 nhánh thành một lối chơi mang tên riêng.
- Cần PX: Hầm Ngầm (M1, 4') là một **active mới chưa có nút**. Đề xuất làm thành "giữ nút Tha khi tay không".

### PROG-06: Sửa Lính Thứ Tư
- v1.2 ghi ×1,45 → ×1,60, tính ra là **+11,5% DPS** (sim E), tức hơn 2 lần ngân sách Bậc II (+5%). Sim A ở R7 tính thẻ này thấp quá.
- Đề xuất: khi có 4 Lính thì mỗi Lính chỉ cộng 0,13 Công → ×1,52 (≈+5%). Giữ phần HP Lính −15%.
- Sau khi sửa, Ω Nghĩ (PvE) = 1,25 × 1,10 × 1,035 = **1,43 ≤ 1,60**. Chênh build solo cần chạy lại, hiện là 1,21, gần trần 1,25.

### PROG-07: Duel cùng cảnh (sim D) — **cảnh báo hệ thống**
| Cảnh | vs Lang | vs Oa | vs Nha |
|---|---|---|---|
| C2 | 0% (Nghĩ chết sau 6–10s) | 100% | 100% |
| C4 | 0% (4,5–9s) | 66% | 100%* |
*Đứng yên đánh nhau; không mô phỏng bay hay lặn.

- Đo power index (EHP × DPS): **Lang 40k · Nghĩ 20k · Oa 17k · Nha 11k**. Lang mạnh gấp khoảng 2 lần cả ba nhân vật mới.
- Buff Nghĩ (Công lên 30, Lính lên 25%, HP ×1,2) thì Nghĩ thắng Lang được 13%, nhưng lại thắng Oa và Nha 100%. Vậy **không nên buff Nghĩ**.
- Ngay cả khi Lang bị giảm xuống 380/36, Nghĩ vẫn thua 0% ở bãi trống. Chỉ ở **Sân Tổ** (hồi Lính mỗi 5s) Nghĩ mới thắng 66%.
- Đề xuất:
  - (a) Mục tiêu duel 40–60% của §4.6 chỉ áp cho đánh nhau ở **địa hình nhà**. Ở bãi trống, KPI là **thoát được**: Lang cần ≥4s để giết Nghĩ, đủ cho 2s Hầm Ngầm cộng phản xạ. Hiện là 4,0–6,0s, đạt sát nút ở C3.
  - (b) Orchestrator mở sim duel toàn cục ở R2, có tính địa hình. Nhiều khả năng phải giảm Lang khoảng 10–15%.

## 4. Kết nối với domain khác
- **SURV:** chốt mật độ thức ăn và xác theo vùng (PROG-04). Cho biết Tâm Ma ở Phi Thăng Kiếp sao chép bầy hay chỉ sao chép Hậu. Cho biết luật Trứng Hộ Kiếp có chấp nhận được không.
- **PX:** làm input cho Sai Lính, Hầm Ngầm, Gác Tổ. Chốt ngân sách 0,27 t-n.
- **WORLD:** đặt tên cho Sai Lính, Sào Bến, Tích Sào. Viết beat Thoát Xác #1–3, và cho Lính đổi sprite theo cảnh nếu ngân sách art cho phép.

## 5. Rủi ro tự nhận diện
- Sim duel là mô hình đứng yên, không có kiting, Toan Dịch làm chậm hay Cắn Giữ, nên xu hướng đáng tin hơn con số %.
- Tôi đang thêm 5 hệ nhỏ. Cần kiểm tra lại câu hỏi "casual hiểu được trong 30 giây không".
- Sai Lính có thể biến game thành idle quản lý.

## 6. Câu hỏi mở
1. Có chấp nhận nguyên tắc "bãi trống thì Lang > Nghĩ" như một phần của Trùng → Thú (Lang ăn Hậu) không?
2. Sửa tỉ trọng CT thành 60/25/15 hay giữ 45/30/25 và tăng Căn Thương?
