# R3 bổ sung: PX phản biện cây Hướng & nhịp *(PX-R3-01…05)*

> Đọc: brief K1/K2, `r3-branch-prog.md`, FINAL §2/§13, GDD v1.2 §16.2–16.3. Chỉ trong domain PX.

## 1. K4 có đúng ý "3–5 lựa chọn khác biệt" không? *(PX-R3-01)*

**Đếm số lựa chọn thật** (thật = đổi động từ/vai, không chỉ đổi số):
| Đột phá | Thẻ hiện | Lựa chọn thật | Nhận xét |
|---|---|---|---|
| C1→C2 Gốc | 4 | **4** | Đạt. Cả 4 Gốc đều đổi BN2 và 1 động từ |
| C2→C3 Trung | 3 | **3** | Đạt ở mức sàn. Cả 6 Trung đều đổi A1 |
| C3→C4 Đỉnh | 3 | **≈1,5** | **Chưa đạt.** Thuần là data. Địa Cung (×1,3, 8→12 ô, 2 sạc) và Thánh Viên (+3% hồi, +5% Thủy) chủ yếu là số. Chỉ Nghĩ Vương và Đại Lộ đổi cách chơi |

**Sửa:**
- (a) Mỗi Đỉnh có **1 luật động từ**. Ví dụ: Địa Cung cho Lính trồi lên từ Hầm Ngầm; Thánh Viên cho rệp trên cây đồng minh tự Gửi Về mật.
- (b) Mỗi Thuần có **1 twist luật** thay vì chỉ cộng số. Ví dụ: Thuần Hố Bẫy cho phép đặt hố khi đang Tha.
- Chi phí thêm ≈ +0,06 t-n.
- Nhận xét phụ: **K4 chỉ hơn K3 ở tầng Gốc (4 so với 3 lựa chọn)**, nhưng tốn gần gấp đôi (0,40 so với 0,21). Người chơi chỉ thấy hơn đúng 1 thẻ.

**UI chọn Hướng trên mobile:**
- **Tối đa 4 thẻ** (Gốc). Mỗi thẻ gồm: silhouette mới, icon động từ, **1 dòng "Mạnh / Yếu"**, và nút "xem 10s" (clip lặp). Không có đoạn mô tả dài.
- **Hiện trước được:** có nút "Cây" luôn mở xem được. Tầng kế tiếp hiện đầy đủ. Tầng Đỉnh chỉ hiện tên + silhouette, giữ tò mò mà vẫn cho người chơi lập kế hoạch. Từ đời thứ 2, các nhánh đã đi qua hiện đầy đủ (Hướng Tích làm "sổ sưu tập").
- **Chọn Sau (PvP):**
  - Đột phá **không mở modal**. Có chấm vàng trên nút A1/BN2. Người chơi mở bảng chọn khi ra khỏi giao tranh 5s hoặc khi ở Nơi Trú.
  - Bảng chọn chiếm ≤40% màn hình dưới, game vẫn chạy.
  - Trong lúc chờ, người chơi giữ kit cũ. Hướng **không có hạn giờ chọn**, nhưng chỉ cộng Hướng Tích sau khi đã chọn. Đây là động lực mềm, không phạt.

**≤5 nút: giữ được.** Các thay đổi đều nằm trên BN2/A1/vuốt né/Tương Tác. Có 3 rủi ro:
1. **Đại Lộ** "A1 từ bất kỳ điểm nào trên vệt" cần ngắm, trái luật MVP chỉ auto-target. → Luật: A1 tự phát từ điểm trên vệt gần mục tiêu đang khóa nhất.
2. **Bảng Tương Tác ngữ cảnh tăng từ 9 lên ≈13 dòng** (Tổ Di, hái Mật, Tha lá, chui mạch). Rủi ro là **mơ hồ ngữ cảnh**, không phải số nút. → Bắt buộc có bảng ưu tiên và icon nút đổi theo đối tượng. Đo bằng HR3-4.
3. **Hành Quân bỏ Sào**: Tổ Di (giữ 3s) dùng lại slot Đặt Sào. OK.

## 2. Nhịp & retention *(PX-R3-02)*

**Lập trường: A + S1 + S3, nhưng đổi thành "A-sớm".**
- Ở A, Gốc mở ở phút 21. Phiên P1 dài 15' nên **người chơi casual không gặp rẽ nhánh trong phiên đầu**, mà đây lại là hook D1 mạnh nhất ("mai thử Huyệt").
- A-sớm: C1 ≈15' (×1,1), C2–C4 ×1,6 (58'/106'/158'). Tổng ≈337' (5,6h). Ω và Mid giữ như A (PROG sim lại để xác nhận).
- **B bị loại khỏi MVP**:
  - Mất 4,5h mỗi lần chết. Với P1 (15'/ngày) là ≈18 ngày chơi.
  - Viên Mãn đầu tiên rơi sau D30, trong khi Viên Mãn là hook D30.
  - B có thể là tùy chọn server "Trường Sinh" ở [1.0].
- **Điểm cộng cho luật chết:** cây Hướng biến cái chết thành "đời sau thử nhánh khác" (logic roguelite). Phải đo, không được giả định.

| KPI | Ngưỡng |
|---|---|
| Đạt Gốc trong phiên 1 | ≥80% |
| Rời game sau khi chết ở C2 / C3+ | ≤25% / ≤35% (cổng tuần 38) |
| Phút mất kỳ vọng mỗi Viên Mãn (Mid) | ≤80' |
| Viên Mãn đầu trước D14 (trong nhóm còn chơi ở D7) | ≥50% |
| Đời sau chọn **Gốc khác** | ≥40% |
| Khoảng không có beat | ≤25', người chơi trả lời "lặp/chán" ở C3–C4 ≤20% |

**Rủi ro bị bỏ sót:** đời dài thêm 55% trên **cùng map 256²**. Chi phí thật của K2 là **nội dung chống lặp** (sự kiện, Hướng Tích), không phải con số phút. SURV/WORLD cần liệt kê beat C3–C4.

## 3. Scope *(PX-R3-03)*

**Vấn đề gốc:** gói Must của Nghĩ đã là **1,71 t-n**, sát cổng tuần 24 (>1,70 thì áp B'). Thêm K4 (0,40) sẽ **tự động kích hoạt B'**.
→ **Tách cổng:**
- Nhân vật Nghĩ ≤1,70.
- Hệ cây ≤0,50, tính riêng, vì UI lưới và thư viện primitive là chi phí chung.

**Phương án PX chốt (MVP-H):**
| Tộc | Cây | t-n |
|---|---|---|
| Nghĩ | K4 + sửa Đỉnh/Thuần | 0,46 |
| **Mộc** | K3 lite (là nhân vật FTUE/VS, nên ấn tượng rẽ nhánh đầu tiên đến từ Mộc chứ không phải Nghĩ) | 0,21 |
| Lang | K3 lite (pick cao, phản diện PvP) | 0,21 |
| Oa, Nha | 3 Gốc; Trung/Đỉnh **[U1]** (không phải 1.0) | 2×0,10 |
| **Tổng** | | **≈1,08** |

- Áp vào A' (đệm 4,75): đệm còn 3,67 (6,6%), **vi phạm luật đệm ≥8,5%**.
- → Giữ đệm thì soft launch **lùi ≈1 tuần (tuần 62)**. Ước theo ~4 FTE, cần xác nhận lại.
- PROG đề xuất Mộc chỉ có Gốc, PX không chọn: Mộc là bản demo của game.
- Giả định 0,02 t-n mỗi kỹ năng là lạc quan. Spike tuần 12 đo trên 3 kỹ năng Nghĩ. Nếu thực tế ×1,5, áp ngay F1.

**Fallback (cắt theo thứ tự):**
- F1. Nghĩ K4 → K3 (bỏ Viên hoặc Huyệt): −0,19.
- F2. Lang → chỉ Gốc: −0,11.
- F3. Đỉnh của mọi tộc chỉ còn toán tử, bỏ hình Đan riêng: −0,08.
- **Không bao giờ cắt:** tầng Gốc của cả 5 tộc (hook D1) và Chọn Sau.

## 4. Giả thuyết playtest *(PX-R3-04)*
| ID | Giả thuyết | Ngưỡng | Nếu trượt |
|---|---|---|---|
| HR3-1 | Hướng khác biệt thật | Xem clip 30s, ≥65% đoán đúng Gốc · mỗi Gốc pick 15–40% · Thuần ≤30% | Thêm động từ cho Hướng yếu; Thuần >30% = bẫy an toàn, giảm số |
| HR3-2 | Chết thành "thử nhánh khác" | ≥40% đổi Gốc ở đời sau · tỉ lệ rời game sau chết không cao hơn v1.2 quá 5 điểm | Dư Âm S2 (cần duyệt E) |
| HR3-3 | Nhịp A-sớm không nhạt | ≥80% đạt Gốc trong phiên 1 · phiên Mid trung vị ≥25' · "chán" ở C3–C4 ≤20% | Thêm beat Hướng Tích; rút C4 về ×1,4 |
| HR3-4 | UI chọn & ngữ cảnh rõ | Thời gian quyết định trung vị Gốc ≤25s, Trung ≤40s · chết trong 10s sau khi mở bảng ≤2% · Tương Tác nhầm ngữ cảnh ≤5% | Ẩn bảng khi có địch trong 12 ô; tách Tha lá/hái Mật sang BN2 |
