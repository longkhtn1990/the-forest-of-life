# R2 Critique — PROG
Sim: `sim/prog_r2_duel_global.py` → `sim/prog_r2_duel_global_output.md` (duel đứng yên 4 tộc, quét nerf Lang).

## Về SURV
- **Giữ:** SURV-02/04/12, đặc biệt Lính chắn trong kit gốc. Sim R2 cho thấy Lính chắn 40% kéo thời gian Lang giết Nghĩ ở C3 từ 4–6s lên **8,3s**.
- **Mượn:** SURV-05 thay hẳn PROG-02 (xem 2). Dời Tổ (SURV-02) thay Sào Bến.

| ID | Mức | Vấn đề | Đề xuất |
|---|---|---|---|
| SURV-04 | Major | Hồi sinh tại chỗ không có CD: có No là đổi được HP vô hạn | Kênh 1,5s; trong giao tranh CD 8s |
| SURV-08 | Minor | Đông −40% nhưng chưa có số kho | Sim No Đông sau khi chốt mật độ thức ăn |

## Về WORLD
- **Giữ:** WORLD-01/02 (Gò Bỏ dạy chọn đất). Đồng ý đổi tên thành Huyệt Nghĩ.
- **Mượn:** dùng bậc gò làm mốc tiến trình: **Gò = 25 đv Tha** (≈34'), **Đại Gò = 80 đv** (≈142').

| ID | Mức | Vấn đề | Đề xuất |
|---|---|---|---|
| WORLD Q1 | Minor | Người dọn vào Gò Cổ làm chủ cũ mất +Linh Quỹ, cả hai bên đều thiệt | Người dọn vào được kho 20 → 25, chủ cũ giữ Linh Quỹ |

## Về PX
- **Giữ:** PX-01, PX-02, Pip 0–4. PX-04 khớp timeline của tôi (M1 ≈3,7', đột phá ≈14').

| ID | Mức | Vấn đề | Đề xuất |
|---|---|---|---|
| PX-01 | Major | Giữ trên xác dùng cho Mở Xác, đụng với Tha Bầy | Phân theo loại vật: xác nhỏ (nặng 4) + ≥2 Lính trong 3 ô thì giữ = Tha Bầy; xác lớn thì giữ = Mở Xác |
| PX-02 | Minor | Pip có 5 trạng thái | Gộp "tự hành" và "Đi lạc" thành **vắng** (viền nét đứt), còn 4 |
| X4 | Major | Chỉ còn dư 0,07 t-n | Xem (5) |

## Lập trường cuối cùng
**(1) Tha:** C1 chỉ Hậu Tha, 1 vật nhỏ về Ổ, được 0,25 CT. C2 Sơ mở **Tha Bầy** cho Lính: xác nhỏ, cần ≥2 Lính, 0,70 CT, Tốc ×0,6. Tôi **rút** đề xuất 1→2→3 Lính, giữ 2 Lính ở C1. Beat 1:30 của PX cần 2 Lính, và mỗi Lính chỉ tốn 0,67 No/phút.

**(2) Lính tự hành:** gộp SURV-05 với Sai Lính, mở ở **C3 Sơ**. Tối đa 2 Lính, mỗi con mang 1 vật, đi ≤30 ô, được 0,125 CT/chuyến, ở ngoài 6 ô thì không có Hy Sinh. Input: khi đang Tha, giữ Tương Tác lên vật thứ hai thì Lính gần nhất nhận vật đó (0 nút). Phần code tái dùng AI "Đi lạc về Tổ". **Pip 0–3**, ô thứ 4 chỉ hiện khi có thẻ Tứ Binh. Giảm Tứ Binh từ ×1,60 xuống ×1,52 (+5%) để Ω PvE = 1,43.

**(3) Hầm Ngầm:** không thêm nút, dùng vuốt né (PX-01). Tôi rút đề xuất "giữ tay không" vì đụng với thao tác đặt Tổ Phụ. Số: CD 25s, chui 2s, trồi ≤6 ô. Giữ Hầm Ngầm là thẻ, vì Lính chắn đã đạt KPI thoát.

**(4) Lang** (sim R2, đứng yên, block 40%):
| Phương án | Lang thắng Oa / Nha / Nghĩ (C4) | Lang giết Nghĩ C3 |
|---|---|---|
| v1.2 | 100/100/100% | 8,3s |
| Lang −15% Công | 100/100/100% | 10,0s |
| Lang ×0,70 HP+Công | 100/100/84% | 11,2s |
| Lang ×0,65 | 1/100/31% | 11,3s |
| 3 tộc mới ×1,25 | 100/100/100% | — |

Lang phải giảm khoảng 35% cả HP lẫn Công mới về ngang. Mức đó là làm lại Lang, và lỗi nằm ở baseline v1.2 của cả 4 tộc, không riêng Nghĩ. Lập trường:
- (a) Session này không đổi chỉ số Lang hay Nghĩ.
- (b) Chấp nhận "Lang > Nghĩ ở bãi trống" theo luật khắc. KPI là Nghĩ thoát được trong ≥4s, và Lính chắn 40% đã đạt.
- (c) Đánh dấu **Blocker toàn GDD**: cần session cân bằng 4 tộc có mô hình cơ động (bay, lặn), xong trước tuần 24.

**(5) 5 hệ lấp dry spell:**
| Hệ | Khớp PX/SURV | Quyết định | t-n |
|---|---|---|---|
| Sai Lính | Gộp với SURV-05 | Giữ | 0,04 |
| Tha Bầy | Khớp nếu phân theo loại vật | Giữ | 0,05 |
| Sào Bến | Trùng SURV-02/03/06 | Cắt, thay bằng Dời Tổ lên bến | 0 |
| Gác Tổ | Trùng luật Tổ | Cắt | 0 |
| Tích Sào | Luật Kiếp chưa được duyệt | Cắt, đưa vào backlog 1.0 | 0 |

Tổng +0,09 t-n, lố 0,02 so với phần dư; bù bằng mục cắt đầu của PX (Tổ Phụ đặt cố định). Khoảng trống dài nhất còn **29'** (142'→171'). C2 không có khoảng nào quá 20' (14' → bờ nước ~20' → Gò 34').

## Xung đột liên domain
| Xung đột | ID | Lập trường |
|---|---|---|
| Tự hành / Sai Lính | SURV-05, PROG-02 | Gộp một hệ: luật của SURV, số của PROG |
| Giữ xác | PX-01, PROG-01 | Phân theo loại vật |
| Tỉ trọng CT | §6.9, PROG-04 | 60/25/15, chờ SURV chốt mật độ |

## Top 3 phải chốt
1. Blocker cân bằng Lang (4c).
2. Kit gốc Nghĩ: Lính chắn 40% + Hy Sinh + CD hồi sinh 8s.
3. Giữ 2 hệ, cắt 3 hệ.
