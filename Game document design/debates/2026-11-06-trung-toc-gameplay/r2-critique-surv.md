# R2 Critique — SURV

## Về PROG
### Giữ lại
- PROG-01 (Tha lite C1 / Tha Bầy C2), PROG-03 (CD hồi Lính tại chỗ: kênh 1,5s, 1 Lính/8s trong combat). Tôi bỏ số 1s của SURV-04 và lấy số của PROG.
### Mượn
- PROG-02 Sai Lính = SURV-05 Lính tự hành, gộp lại dưới tên của PROG. Lấy 50% CT, ≤30 ô, không có Hy Sinh khi Lính ở ngoài 6 ô.
### Phản biện
| ID | Mức | Vấn đề | Tình huống | Thay thế / kiểm chứng |
|---|---|---|---|---|
| PROG-01 Sào Bến | Major | Đây là hang an toàn thứ 2 (có Bế Quan) đặt ngay trên nút tranh chấp, phá luật SURV-03 | Nghĩ C4 Bế Quan trong Sào Bến, ngồi giữ bến mà không ai đuổi ra được | Bỏ hệ riêng, gộp vào **Dời Tổ lên bến** (SURV-02, 1 lần/cảnh). 0 t-n, tiết kiệm 0,05 |
| PROG-07 | Major | Sân Tổ hồi 1 Lính/5s, trong khi luật Tổ của tôi là 20s. Hai bộ số không khớp nhau | Nghĩ đứng sát Tổ, có 4 Lính không bao giờ cạn, Lang không có cửa | Sân Tổ = ≤8 ô quanh Tổ chính/Phụ, hồi 1 Lính/10s. Chạy lại sim D với số này |
| PROG-04 | Minor | Hỏi mật độ thức ăn nhưng chưa có mục tiêu cho mùa Đông | — | Xem lập trường (3) |
### Câu hỏi cho PROG
- Nếu Lính tăng 1→2→3 thì beat Hy Sinh ở 6:30 của PX chỉ còn 1 Lính sống. Có chấp nhận không?

## Về WORLD
### Giữ lại
- WORLD-01 (Căn Thương = dọn rừng), WORLD-03 (3 bến có danh tính riêng), WORLD-04 (Hầm Đá chỉ là prop).
### Mượn
- 3 bậc gò dùng làm **tín hiệu đọc được** cho kẻ săn. Đây đúng là áp lực "đọc được".
### Phản biện
| ID | Mức | Vấn đề | Tình huống | Thay thế |
|---|---|---|---|---|
| WORLD-03 Gò Bỏ | Major | Bảng ghi "an toàn", nhưng WORLD-02 lại tả cả 3 gò đều có lý do bị bỏ. Hai chỗ tự mâu thuẫn | Người mới chọn gò C vì "an toàn" rồi mất Lính liên tục vì Diều hâu | Gò Bỏ = dựng nhanh, kèm **1 hazard cố định** cho mỗi gò (luật ở mục 5) |
| WORLD Q1 Gò Tổ Cổ | Minor | Đặt Tổ vào gò cổ có thể thành exploit snowball | Nghĩ đời 2 vào gò cổ bậc Đại Gò ngay từ C2 | Vào gò cổ chỉ được khởi đầu ở bậc Gò, mỗi gò cổ 1 Nghĩ |
| WORLD-03 spawn | Minor | 6 ổ trứng nhưng chưa nói luật dùng chung | 2 Nghĩ sinh cùng một ổ, giành nhau cùng một bãi hạt | 1 ổ/1 Nghĩ, ổ bị chiếm thì sinh ở ổ khác |
### Câu hỏi cho WORLD
- Kiến AI đi theo đường mùi có chặn đường đi của Lính trên đường hẹp (Bến Xương) không?

## Về PX
### Giữ lại
- PX-01 (chạm/giữ), Pip phân biệt bằng hình dạng, PX-05 P1 (hoãn hint Căn Thương).
### Mượn
- Vuốt né làm đường thoát cho **mọi nhánh**. Cách này giải luôn M3 của tôi: Nghĩ không đi Tồn vẫn có đường thoát.
### Phản biện
| ID | Mức | Vấn đề | Tình huống | Thay thế / kiểm chứng |
|---|---|---|---|---|
| PX-02 | Major | Bấm Xung khi không có mục tiêu thì bầy đứng Giữ. Lúc hoảng sẽ bấm nhầm, bầy đứng im | Nha bổ nhào từ 9 ô, người chơi bấm Xung, bầy đứng yên, Hậu mất Lính chắn | Chỉ vào Giữ khi **không có địch trong 12 ô**. Có địch trong 6–12 ô thì Xung lao về địch gần nhất. Đo bằng HNg-4 |
| PX-02 | Major | Sai Lính (C2) và đặt Tổ chính chưa có input | — | Hậu đang Tha mà giữ Tương Tác lên vật thứ 2 thì giao vật đó cho Lính gần nhất. Đặt Tổ: giữ 2s, vòng xanh/đỏ theo luật hợp lệ. Không thêm nút |
| PX-04 | Minor | Beat 0:03 có 2 Lính, xung đột với PROG-01 | — | Theo lập trường (1) |

## Lập trường cuối (owner luật)
**(1) Tha:**
- C1: Hậu Tha 1 vật (≤2 đv) về Ổ (kho 20).
- C2 Sơ: **Tha Bầy**, xác 4 đv cần Hậu + ≥2 Lính, Tốc ×0,6. Đặt Tổ chính (kho 40). Lính Tha khi đi theo Hậu.
- C2 Trung: Sai Lính ×1 (học lúc Ấu Linh còn che). C3: Sai Lính ×2.
- Linh Hạch không Tha được.
- Lính tăng 1→2→3 theo PROG. PX dời beat "2 Lính" sang 3:45.

**(2) Duel:** Chấp nhận, với 4 điều kiện:
- (a) Sân Tổ ≤8 ô, hồi Lính 10s, Lang thắng ở đó ≥40% (cấm rùa tổ).
- (b) Bãi trống: Lang cần ≥4,0s để giết Nghĩ ở **mọi** cảnh.
- (c) Nghĩ chỉ dùng kit gốc (vuốt né + Lính chắn + Toan Dịch chậm), không có Hầm Ngầm, vẫn thoát được ≥50%.
- (d) PvP Nghĩ C3 ≤0,06/h.

Chỉ giảm Lang sau khi sim có kiting. Tổ Phụ 3 đòn là phản đòn hợp lệ của Lang.

**(3) 5 hệ:**
- Tha Bầy và Gác Tổ: OK. Gác Tổ chỉ báo động, không đánh, và vẫn chiếm 1 slot bầy.
- Sai Lính: OK. Lính vẫn tốn −1 No/90s, tối đa 2 Lính.
- **Sào Bến: phá luật** "1 hang an toàn". Gộp vào Dời Tổ.
- Tích Sào: OK nếu Trứng là vật kho 2 đv, **trộm được**, tối đa 2. Tâm Ma chỉ sao Hậu + Lính thường.
- Mật độ thức ăn: ~6 vật trong 15 ô quanh Tổ, respawn 90s. No vào ≈1,3× decay (C1–C2), 1,2× (C3), 1,4× (C4). Đông: 0,8×, buộc phải ăn từ kho.

**(4) Controls PX:** Khớp, kèm các luật sau.
- Giữ nới leash lên **20 ô / 45s**, quá ngưỡng thì Đi lạc về Tổ.
- Gộp "bị tách" và "Đi lạc" thành 1 trạng thái Pip cam. Đứng bờ 15s rồi về Tổ (trả lời P3).
- Giữ không tốn thêm No.
- Đông: chạm Pip hiện khóa (không hồi sinh tại chỗ).
- Hầm Ngầm thay vuốt né (CD 25s). Trong lúc CD thì vuốt né thường. Không chui qua nước, Lính bị bỏ lại thì Đi lạc.

**(5) Luật cho WORLD:**
- **Gò:**
  - Ổ (C1, kho 20) → Gò (đặt Tổ chính C2, kho 40) → Đại Gò (≥120 đv Tha tích lũy và ≥C3, kho 60).
  - Đọc được bậc gò từ 20 ô.
  - Chi phí là data: tôi đổi chỉ số kho, không thêm hệ.
- **Gò Bỏ:** dựng Tổ chính tức thì, sẵn 5 đv trong kho, mỗi gò 1 hazard cố định:
  - A: Mưa làm ngập, mất 10% hạt mỗi lần, không Bế Quan khi mưa.
  - B: Lang AI đi qua 1 lần/5'.
  - C: Diều hâu trong 10 ô có CD 1,5' (thay vì 3').
- **Bến cạn:**
  - Đặt Tổ hợp lệ dù sát nước, tối đa 1 Tổ/bến. Cá Sấu đớp bờ ở cả 3 bến.
  - Bến Xương: lối hẹp 2 ô.
  - Bến Rễ: Nha đậu được, không bị cấm bay.
  - Bến Bùn: Nha/Diều hâu có CD bổ nhào −30%.

## Xung đột liên domain
| Xung đột | ID | Lập trường | Gợi ý |
|---|---|---|---|
| Sào Bến vs 1 hang an toàn | PROG-01, SURV-03 | Gộp | Dời Tổ |
| Số Lính ở C1 | PROG-01, PX-04, WORLD-01 | 1→2 | PX dời beat |
| Lệnh Giữ khi hoảng | PX-02 | Cổng 12 ô | HNg-4 |
| Nerf Lang toàn cục | PROG-07 | Chưa | Sim có kiting trước |

## Top 3 phải chốt
1. Luật Sân Tổ: 10s, ≤8 ô, Lang ≥40%.
2. Sai Lính + Giữ + đặt Tổ, tất cả trong 1 nút Tương Tác.
3. Gò 3 bậc gắn kho 20/40/60, Gò Bỏ có hazard.
