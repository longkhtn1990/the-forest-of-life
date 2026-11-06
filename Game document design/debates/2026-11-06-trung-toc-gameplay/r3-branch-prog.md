# R3 bổ sung — PROG: Cây Hướng theo cảnh & nhịp chơi

> K1 + K2 của người dùng. Sim: `sim/prog_r3_pacing.py` (+`_output.md`), mô hình vòng đời sim B v1.2 (×1 hiệu chuẩn: Mid 73%/5,0h ≈ v1.2).

## B1. Template: Cây Hướng lưới K4 *(PROG-R3-01)*

**Luật chung, áp cho cả 5 tộc:**
| Đột phá | Chọn | Pool / tộc | Ô được đổi | Kế thừa |
|---|---|---|---|---|
| C1→C2 | **Hướng Gốc**: 1 trong 4 | 4 | Lính/thân + **BN2** + 1 bị động + 1 điểm yếu + hình dạng | — |
| C2→C3 | **Hướng Trung**: 1 trong 3 | 6 | **A1** + 1 bị động | Mỗi Trung là **ghép của 2 Gốc** (6 cạnh của K4). Gốc X chỉ thấy 3 Trung có chứa X. A1 Trung có 1 dòng "nếu Gốc là X/Y" |
| C3→C4 | **Hướng Đỉnh**: 1 trong 3 | 4 + 6 Thuần | **A1 Thăng** = toán tử lên A1 Trung + hình Đan | Trung(X,Y) chào Đỉnh X, Đỉnh Y hoặc **Thuần** (đào sâu chính Trung) |

- **36 dòng** (4×3×3) từ **14 nút hành vi + 6 Thuần (data)**; cây thường cần 4+12+36. C4→C5 [U1]: Nhân ‖ Yêu là toán tử lên cả cây.
- **Chống bùng nổ tổ hợp:**
  1. Trung = cặp Gốc → kế thừa nằm sẵn trong cấu trúc.
  2. **Đỉnh là toán tử** (vd *"Xung mang 50% hiệu ứng A1"*), chạy với mọi A1 Trung.
  3. Mọi kỹ năng dựng trên **6 primitive chung 5 tộc**: nón, vũng, lao, bẫy, hào quang, kênh.
- **Quan hệ với Đạo Lộ: gộp.**
  - Đột phá cảnh = mốc **Hướng** (thay M2/M3/M5). Thẻ Đạo Lộ (khung giữ nguyên) dời vào **mốc trong cảnh**, làm vai **chỉnh nhỏ**; thẻ **cấp động từ** chuyển lên Hướng (4 thẻ Nghĩ viết lại, §B2).
  - D/E/F/G giữ: 3–5 lựa chọn, kế thừa, hiệu quả hết đời, không respec. Viên Mãn rút 3 từ thẻ **và** Hướng (Hướng dịch theo trục chính).
- **Mốc mỗi đời: 3 Hướng + 7 thẻ + Viên Mãn = 11 quyết định** (v1.2 có 7).

**Chi phí 1 tộc** (ước PROG; PX chốt; giả định kỹ năng trên primitive 0,02 t-n, sprite ghép phần rời 0,015, UI lưới 0,06 một lần):
| | Kỹ năng mới | Sprite thân | Data (cạnh / Hướng Tích / Thuần) | Thẻ viết lại | t-n |
|---|---|---|---|---|---|
| **K4** (Nghĩ, 36 dòng) | +10 | 8 + 4 palette Lính | 12 / 42 / 6 | 4 | **≈0,40** |
| **K3 lite** (3 Gốc/3 Trung/3 Đỉnh, 27 dòng) | +5 | 6 | 6 / 27 / 3 | 2–4 | ≈0,21 |

⚠️ **Scope:** K4 cả 5 tộc ≈2 t-n; Nghĩ K4 + 4 tộc K3 ≈1,24 t-n — đều vượt cổng tuần 24. Đề xuất MVP: **Nghĩ K4 + Lang K3**, Oa/Nha/Mộc chỉ tầng Gốc (Trung/Đỉnh sang 1.0). PX quyết.

## B2. Cây Hướng Linh Nghĩ *(PROG-R3-02; tên tạm, WORLD đặt lại)*

Kit chung giữ: Xung, Tha, Khiêng, Mở Xác, Lính chắn, Hy Sinh; **Căn Thương luôn là ngữ cảnh của A1** (luật Mộc Tàn). Toan Dịch chỉ còn ở Binh; Gốc khác đáp kẻ bay bằng Lính chắn + Hy Sinh (điểm yếu khai rõ).

### Hướng Gốc (C1→C2)
| Gốc | Fantasy | Đổi lối chơi (BN2 + động từ) | Mạnh | Yếu |
|---|---|---|---|---|
| **Binh Nghĩ** | Kiến lính, hàm kìm | 3 Lính → **2 Binh** (HP 24%, Công 0,24× mỗi con). BN2 **Phun Toan**: nón axit, Thủ −15% 4s, trúng kẻ bay. Xung = Binh **kẹp giữ** 0,8s | Giao tranh, chịu AoE | Không Gửi Về, CT ×0,96, mất 1 Binh = nửa bầy |
| **Phu Nghĩ** | Kiến thợ, đường kiến | Lính **tự Tha** khi Theo. Gửi Về ×2 ngay C2. BN2 **Vạch Mùi**: vệt 8 ô, bầy/đồng minh +15% Tốc, kẻ trên vệt bị lộ | Kinh tế, party, đọc đường | HP Lính −15%, dps 0,93 |
| **Huyệt Nghĩ** | Kiến đào, sống dưới đất | Vuốt né → **Hầm Ngầm** (CD 25s). Sào **ngầm**: không lộ ngoài 6 ô. BN2 **Ụ Đất**: chặn đường/LOS 3 ô 6s | Thoát, phòng tổ | Không đặt Sào ở bùn (khó ở C4 Đầm); chui là bỏ Lính |
| **Viên Nghĩ** | Kiến chăn, nông dân | BN2 **Rải Rệp**: đặt rệp lên cây/bụi (≤3 đàn), 60s sau giữ Tương Tác lấy **Mật** (+No, +CT); Khế ước với Mộc không chiếm slot | Bền, cộng sinh Mộc | dps 0,93; rệp bị Nha/Oa ăn; phụ thuộc cây |

### Hướng Trung (C2→C3), thay A1 Đục Rễ
| Trung (cặp Gốc) | A1 / luật mới | Từ Gốc A / Gốc B |
|---|---|---|
| **Hành Quân** (Binh+Phu) | **Bỏ Sào → Tổ Di** (giữ 3s dựng tạm, CD 5', kho 20, không Đại Gò). +1 Lính. A1 **Tràn Quân**: dòng bầy 6 ô, kẻ trên đường −20% Tốc | Binh: Tràn kẹp 0,5s / Phu: Tràn nhặt vật trên đường |
| **Toan Độc** (Binh+Viên) | A1 **Vũng Toan** 3×3 6s: Thủ −20%, hồi máu −30% (khắc Mộc/Oa), −4 No/lần | Binh: Lính để vết axit / Viên: vũng ×1,3 cạnh cây có rệp |
| **Phục Địa** (Binh+Huyệt) | A1 **Hố Bẫy**: tối đa 2 hố ẩn, kẻ dẫm vào bị giữ 1,2s, Lính trồi lên Xung miễn phí. | Binh: giữ 1,5s / Huyệt: chui vào hố = Hầm Ngầm hồi ngay |
| **Mạch Ngầm** (Huyệt+Phu) | A1 **Đào Mạch**: nối Sào ↔ ≤2 Ngách. Chui qua mạch kênh 2s. **Tha trong mạch không bị bắt** | Huyệt: +1 Ngách / Phu: Gửi Về đi trong mạch |
| **Diệp Viên** (Viên+Huyệt) | Tha **lá** nuôi **Vườn Lá** (10 lá/bậc, ≤3 bậc): ≤12 ô quanh Sào CT +3%/bậc (online, trong kẹp CT). A1 **Cắt Tán**: Lính cắt Tán, mục tiêu −30% Quang hợp 20s | Viên: rệp trong vườn / Huyệt: vườn ngầm, không trộm được |
| **Mục Rệp** (Viên+Phu) | A1 **Gọi Mật**: hút mật từ mọi đàn rệp trong 15 ô → hồi 6% HP bầy và đồng minh 12 ô (healer) | Viên: 4 đàn / Phu: mật đi theo vệt mùi |

### Hướng Đỉnh (C3→C4) = A1 Thăng dạng toán tử + hình Nghĩ Đan
| Đỉnh | Toán tử lên A1 Trung | Luật bầy/tổ |
|---|---|---|
| **Nghĩ Vương** (Binh) | Xung mang 50% hiệu ứng A1 | Hậu đứng tiền tuyến: Lính chắn 40% → 55% |
| **Đại Lộ** (Phu) | A1 dùng từ bất kỳ điểm nào trên vệt mùi ≤20 ô | Vệt Gửi Về thành **Đường Cái** (server thấy), Tốc +15% trong trần |
| **Địa Cung** (Huyệt) | A1 trong Sân Tổ ×1,3 | Sân Tổ 8 → 12 ô, Hầm Ngầm 2 sạc |
| **Thánh Viên** (Viên) | A1 cạnh cây cộng sinh hồi 3% HP bầy | Cây đồng minh ≤20 ô: Gai không trúng bầy, cây +5% Thủy |
| **Thuần ×6** | A1 Trung Thăng (data) | — |

**Thẻ Đạo Lộ phải viết lại:**
| Thẻ cũ | Chuyển vào | Thẻ mới |
|---|---|---|
| Hầm Ngầm | Huyệt | **Vỏ Dày** (−6% sát thương nhận khi ≥2 Lính sống) |
| Ngách | Mạch Ngầm | **Lối Lui** (Lính chết → Hậu +12% Tốc 2s) |
| Tứ Binh | Hành Quân | **Binh Kỷ** (Lính +8% HP, +5% Công) |
| Vác Đôi | Phu | **Chân Chắc** (Tốc khi Tha −30% → −18%) |

Hợp Đạo Hầm Phục/Mạch Tổ viết lại thành toán tử theo tag.

**Sau 10 giờ:** Hành Quân→Đại Lộ không có nhà; Huyệt→Mạch Ngầm→Địa Cung giữ mê cung; Viên→Mục Rệp→Thánh Viên là healer sống nhờ cây Mộc — khác thao tác, không chỉ khác số.

## B3. Nhịp chơi *(PROG-R3-03)*

**Phút Mid mỗi cảnh, không chết:**
| Phương án | C1 | C2 | C3 | C4 | Đời | Phiên Mid 40' | Phiên P1 15' |
|---|---|---|---|---|---|---|---|
| v1.2 | 14' | 36' | 66' | 102' | 218' (3,6h) | 5,5 | 14,5 |
| **A ×1,5 đều** | 21' | 54' | 99' | 153' | 327' (5,5h) | 8,2 | 22 |
| **B ×2 lệch** (C1 ×1,4 → C4 ×2,2) | 20' | 68' | 132' | 224' | 444' (7,4h) | 11 | 30 |
| C ×3 đều | 42' | 108' | 198' | 306' | 654' (10,9h) | 16 | 44 |

**Ba lớp an toàn** (không đổi luật chết mất trắng):
- **S1 Mật độ:** cảnh dài ×k → hazard/giờ mục tiêu ÷√k (C3 0,10 → 0,08/h ở A). SURV tune (Director, Sân Tổ, Hồn Hộ).
- **S2 Dư Âm:** đời sau CT ×1,5 ở cảnh đời trước đã qua (trừ C4); chạm luật E → cần người dùng duyệt.
- **S3 Tu ở Tổ:** ≤20% CT mỗi cảnh từ Nhập Định bán chủ động ở Nơi Trú (chạm ~10s/lần; AFK vẫn ×0,2), rủi ro ≈0.

**Kết quả sim** (P đời đầu Viên Mãn · giờ/1 Viên Mãn · phút mất TB mỗi lần chết · phút mất kỳ vọng mỗi Viên Mãn):
| Phương án | P1 xe buýt | Mid | P2 kẻ săn |
|---|---|---|---|
| v1.2 | 81% · 4,7h · 138' · 34' | 73% · 5,0h · 136' · 52' | 58% · 5,7h · 134' · 95' |
| A, không lớp | 71% · 7,6h · 205' · 83' | 62% · 8,3h · 197' · 127' | 46% · 10,0h · 188' · 233' |
| **A + S1 + S3** | 81% · 7,0h · 200' · 48' | **73% · 7,5h · 201' · 78'** | 59% · 8,4h · 199' · 138' |
| B, không lớp | 63% · 11,0h · 268' · 158' | 52% · 12,5h · 258' · 246' | 32% · 16,9h · 244' · 514' |
| **B + S1 + S3** | 77% · 9,7h · 269' · 79' | **68% · 10,5h · 268' · 127'** | 54% · 12,0h · 259' · 217' |

**Đọc kết quả:**
- Kéo dài không có lớp an toàn: P(Viên Mãn) rơi 10–20 điểm, mỗi lần chết mất thêm 1–4h.
- S2 cho rất ít (B: +1 điểm Mid, −17' kỳ vọng) → PROG **không** khuyến nghị.
- **Khuyến nghị PROG: A + S1 + S3** (5,5h/đời, Mid 73%, ~2,2 tuần).
  "Dày" đến từ **11 quyết định/đời** (v1.2: 7) + Hướng Tích, không chỉ từ thời gian. KPI phút mất kỳ vọng ≤60' nới thành **≤80'**.
- **B** nếu muốn đời ~7,5h: Mid 68%, mất **4,5h mỗi lần chết**, KPI ≤130'. **C loại:** kể cả S1+S3 vẫn mất 6,5h/lần chết, Mid 63%.

**Nhịp trong cảnh (A):** 3 tầng/cảnh; thẻ ở Trung và Hậu, Hướng khi đột phá; thêm **Hướng Tích**: mỗi Hướng có 3 bước công trình/cảnh (vd Binh hạ 3 mồi lớn; Viên giữ 3 đàn rệp 10'), thưởng hình dạng / kho +5 / leash +2, **ngoài Ω**.

| Cảnh (phút) | Beat mới theo phút | Khoảng dài nhất |
|---|---|---|
| C1 (0–21) | M1 thẻ 6' · Mở Xác 12' · **Gốc 21'** | 9' |
| C2 (21–75) | HT 30' · thẻ 38' · HT 47' · thẻ 56' · Đông/HT 65' · **Trung 75'** | 10' |
| C3 (75–174) | Căn Thương ~85' · HT 95' · thẻ 105' · Dời Tổ/HT 120' · thẻ 138' · HT 155' · **Đỉnh 174'** | 19' |
| C4 (174–327) | Bến 190' · HT 205' · thẻ 220' · Đại Gò 240' · HT 255' · Hợp Đạo 272' · HT 295' · **Viên Mãn 327'** | 23' |

Mọi khoảng ≤25'.

## B4. Cân bằng *(PROG-R3-04)*
- **Ngân sách Hướng:** mỗi nút dps ≤×1,02 (Đỉnh ×1,00), cả dòng **H_dps ≤1,05**; thế mạnh ehp/CT/party phải trả bằng một trục yếu.
  - **Ω template = M_thẻ ≤1,30 × 1,02 × 1,10 × 1,035 × H 1,05 = 1,585 ≤1,60.** Kẹp M_thẻ ≤1,30 (đã chốt cho U1) được áp ngay từ MVP.
  - Ω Nghĩ max = 1,25 × 1,10 × 1,035 × 1,04 = **1,48**.
- **Sim 36 dòng** (sau 3 vòng nén số):

| Kết quả | Giá trị |
|---|---|
| Điểm tổng (trọng số dps 35 / sống sót 25 / CT 25 / party 15) | 1,037 – 0,988 → **chênh 1,05** |
| Mạnh nhất / yếu nhất | Binh→Phục Địa→Thuần / Phu→Mục Rệp→Phu |
| Chênh theo trục, có chủ đích | dps 1,23 · CT 1,23 · ehp 1,30 · party 1,32 |

- **Kẹp đã áp:** CT dòng ∈ [0,92; 1,14] (bản đầu 0,87–1,25: thời gian tới Viên Mãn lệch 43%); ehp ≤1,22 (Huyệt chồng 3 tầng ra 1,31 = "không bắt được").
- **Đường sống:** ehp min 0,94 → Lang C3 cần 7,8s (KPI ≥6s); CT min 0,92.
- **Rủi ro cộng dồn:** chênh build thẻ 1,21 × chênh Hướng 1,05 = **1,27 >1,25**. Thẻ động từ đã lên Hướng nên pool thẻ đều hơn: mục tiêu ≤1,18 → tổng ≤1,24. **Cần sim lại pool thẻ** (R4).
- **Playtest:** mỗi Gốc pick-rate 15–40% (Binh hơi đứng đầu → nén trước nếu >40%); ≥60% người chơi nói được "Hướng của tôi làm gì khác" sau 1 đời.

## Câu hỏi cho người dùng
| # | Câu hỏi | Mặc định PROG |
|---|---|---|
| R3-Q1 | Nhịp A (5,5h/đời) hay B (7,4h/đời)? | A + S1 + S3 |
| R3-Q2 | Duyệt S2 Dư Âm? | Không cần |
| R3-Q3 | Phạm vi MVP: Nghĩ K4 + Lang K3, ba tộc còn lại chỉ có Gốc? | Có |
