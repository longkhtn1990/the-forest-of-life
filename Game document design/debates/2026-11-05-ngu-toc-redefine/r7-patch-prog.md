# R7 — Patch PROG (H1–H3)
Sim: `sim/prog_r7_sim.py` → `sim/prog_r7_sim_output.md`. Tên là tên tạm, WORLD đặt lại.

## P1. Nghĩ, Oa, Vũ lên đủ C1–C4

**PROG-R7-01.** Khung giống Lang: M1–M6 (4' / 14' / 50' / 86' / 116' / 171'), Viên Mãn ở đỉnh C4 Hậu (218'). Mỗi nhân vật: 6 lần chọn, 9 thẻ, 1 Thiên Phú, 3 Hợp Đạo (ở M6, cần Bậc II cả hai nhánh). Giữ 9 thẻ §6.6, **trừ Lính Đỡ: 25% → 12%** (ở 25% thẻ cho +33% ehp, gấp 4 lần ngân sách Bậc III).

**A1 → A1 Thăng (C4):**
- **Nghĩ — Đục Rễ.** Trên cây đang Mộc Tàn: Căn Thương (§4.8). Trên đất (bổ sung): đường hầm tới mục tiêu ≤4 ô, sau 1s nổ 1,2×Công, AoE 1,5 ô, chậm 30%/2s, CD 14s. **Thăng:** 1,5×Công, chậm 40%; có ≥3 Lính thì trói 0,5s. Tốc độ Căn Thương giữ nguyên (≈50s).
- **Oa — Lưỡi Độc.** Lưỡi 5 ô, 1,3×Công + độc 30%/3s, CD 10s. **Thăng:** 1,5×Công, độc 45%/4s; dùng trong 1,5s sau khi trồi lên thì tầm +1 ô.
- **Vũ — Mổ Liên Hoàn** (3 × 0,6). **Thăng = Bổ Nhào:** khi đang bay, lao xuống 5 ô, 1,6×Công, kích Hạ Cánh Đạp ngay. Dưới đất thì thành 4 mổ. Đây là đòn duy nhất đánh được từ trên trời.

**Hợp Đạo (Tồn×Sát · Tồn×Vai · Sát×Vai):**
- **Nghĩ:** **Hầm Phục** (chui lên từ Hầm Ngầm: Xung miễn phí 2s) · **Mạch Tổ** (Hầm Ngầm nối tổ/tổ phụ ≤20 ô, kênh 2s, CD 90s) · **Đoàn Quân** (Tha về tổ: Lính +8% sát thương 30s, tối đa 2 lần).
- **Oa:** **Phục Bùn** (lưỡi đầu sau Ngụy Bùn/trồi lên ×1,3 + độc) · **Ao Hộ** (Ngủ Bùn hồi cả đồng minh 3 ô 1,5%/s) · **Mưa Độc** (vũng Mưa Rào 10% Công/s, không cộng với Lưỡi Độc).
- **Vũ:** **Cựa Mẹ** (HP <40%: Hạ Cánh Đạp trúng hồi 6% HP) · **Canh Gác** (Diều Hâu! báo cả party; Gáy trong Ổ không lộ mình) · **Gáy Chiến** (3s sau Gáy, Hạ Cánh Đạp lên mục tiêu bị ping choáng 1,0s).

**Sim A.** Mỗi nhân vật 43 build, mốc nào cũng ≥3 thẻ. Chênh mạnh/yếu (solo / party), ngưỡng ≤1,25: Nghĩ 1,21 / 1,15 · Oa 1,14 / 1,08 · Vũ 1,16 / 1,08. M_thẻ max 1,31 / 1,26 / 1,26, đều ≤1,34 (trần của Lang).

**PROG-R7-02. Bỏ phẩm Sơ/Thâm của Đạo Chủng.** Chỉ còn một mức, bằng giá trị Thâm cũ; bảng dịch còn 25 ô. Mọi Viên Mãn rút 3 trong 6 thẻ đã nhận. Win-rate Sổ ô 1–2 vẫn ≈56% (giữ dự phòng Sát 3,5% → 3%). Nếu đến 1.0 có loài lite thì dùng lại phẩm Sơ cho loài đó.

## P2. Nội tại riêng (PROG-R7-03)
Tách khỏi đặc tính tộc và động từ riêng: 1 dòng tooltip, luôn bật. Luật: không cộng CT; tấn công ≤+2% dps, phòng thủ ≤+10% ehp ở C4 Hậu; nội suy tuyến tính theo 12 tầng.

| Nhân vật | Nội tại | Hiệu ứng | C1 Sơ → C4 Hậu |
|---|---|---|---|
| Linh Mộc | **Niên Luân** | Mỗi ngày-rừng (có ≥20' online) không bị Đổ: +1 vòng, mỗi vòng +1% Thân max. Bị Đổ mất ½ số vòng | tối đa 3 → 10% |
| Lang | **Cắn Giữ** | Đòn thường làm mục tiêu chậm 1,5s. Các hiệu ứng chậm lấy giá trị lớn nhất, không cộng | 4 → 10% |
| Nghĩ | **Hy Sinh** | Lính chết trong 6 ô: Hậu hồi % HP (CD 3s mỗi Lính) | 2 → 4% |
| Oa | **Nhựa Da** | Kẻ đánh cận chiến trúng Oa nhận độc theo % Công của Oa trong 2s | 4 → 10% |
| Vũ | **Giật Mình** | Đòn từ kẻ chưa hiện trên Thần Thức bị giảm sát thương | −15% (CD 30s) → −30% (CD 20s) |

Giật Mình C4 đưa đòn Ẩn Phong của Lang ×1,3 → ×0,91 (đúng Vũ ⊣ Thú). Hy Sinh + Lính Đỡ 12% ≈ +20% ehp, bù HP Hậu 0,71× Lang. Đặc tính tộc đề xuất (SURV chốt): **Thú = Đánh Hơi** (nâng từ Lang lên tộc, chi phí 0) · **Trùng = Thân Nhỏ** (bị phát hiện ở ×0,8 tầm, bụi không làm chậm).

## P3. Giới hạn số SURV cần tôn trọng (PROG-R7-04)

**Vũ bay.** Bay là cờ lớp `air` + bóng đổ, vẫn 2D.
- **Cất cánh** 0,6s, trúng đòn thì bị ngắt. **Thể Lực** −8/s khi bay, không hồi.
- **Bay tối đa:** C1 6s · C2 9s · C3 12s · C4 **15s (trần cứng MVP)** = 42 / 63 / 84 / 106 ô. Đáp xong phải đứng đất ≥3s.
- **Tốc bay** 7,0 ô/s (×1,10, trong trần ±15%). Khi bay không ăn, không đánh thường, không ẩn; tầm bị phát hiện ×1,5.
- **Rớt:** trúng đòn ≥6% HP max thì hạ cánh, choáng 0,4s, −30 Thể Lực.
- **Đánh được kẻ bay:** đòn tầm xa (Lưỡi, Toan Dịch), Gai Bạo trong bán kính Tán, Diều hâu AI, Vũ khác. Cận chiến chỉ trúng lúc cất cánh.
- Mưa: Thể Lực bay ×1,5; Ướt thì không cất cánh.
- **Cấm** hệ số "×X sát thương lên kẻ bay": với ×1,25, Ω = 1,95, vượt trần 1,60.

Sim D: thấy Lang từ ≥8 ô thì thoát; Lang ở ≤6 ô (Ẩn Phong) thì Lang Nha ngắt được. Bay là công cụ thoát cần đọc tình huống, không phải nút thoát chắc chắn.

**Thủy dưới nước.** Bỏ luật "nước sâu CT ×0" và bỏ Thể Lực −5/s dưới nước đối với Thủy.
- **CT:** nước sâu **×0,5**, bờ/nông **×1,15**. Ở sâu ≤38% thời gian thì CT trong ±10% (sim C). Ở hẳn dưới nước: 435' tới Viên Mãn thay vì 218' (chậm, không cấm).
- **Lớp `submerged`:** ẩn với loài cạn; bơi >×0,8 Tốc để gợn nước thấy được trong 6 ô.
- **Đánh:** phải trồi lên, hiện ≥0,5s. Không đánh xuyên lớp. PvP dưới nước chỉ giữa các nhân vật cùng lớp (Thủy, cá AI).
- **Lặn khi giao tranh:** kênh 1,5s (vẫn bị chọn làm mục tiêu), vệt nước đục 4s, 3s sau khi lặn không đánh.
- **Trọng Thương / bị Kết Liễu:** không lặn được.
- Không hệ số nào tăng khi ở nước; ô Q giữ nguyên.

**Ω (sim B):** 1,34 (M_thẻ) × 1,02 (nội tại) × 1,10 (Q) × 1,035 (Đạo Chủng) = **1,556**, trong trần ≤1,60. U1 thêm Bản Thể ×1,04 thì lên 1,618, vượt trần → **chốt kẹp M_thẻ ≤1,30 ở U1** (ra 1,570).

## P4. Thời lượng & khối lượng (PROG-R7-05)

Mid, P(đời đầu Viên Mãn) / giờ tới 1 Viên Mãn: Mộc 81% / 4,6h · Lang 75% / 4,8h · Nghĩ 74% / 4,9h · Oa 75% / 5,2h · Vũ 73% / 4,9h.

- **Viên Mãn lần đầu cả 5 tộc: 24,5h ≈ 7 tuần** (v1.1: 16,5h).
- **Thẻ: 66** (13 × 5 + Thâm Hóa; v1.1: 57). **Kỹ năng: 20** (15 + 5 Thăng). Mới: 5 nội tại, 3 tên C4, 3 Phi Thăng Kiếp I + 3 Kiếp Viên Mãn C4. Đạo Chủng 25 dòng.
- PX tính t-n, gồm lớp bay và lớp dưới nước.

Rủi ro: Viên Mãn thứ 2 tăng 2,3h → 4,6–5,2h; theo dõi tỉ lệ bỏ game ở đời 2.
