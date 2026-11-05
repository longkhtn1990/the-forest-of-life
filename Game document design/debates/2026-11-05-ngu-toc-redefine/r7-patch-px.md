# R7 — Patch PX sau Bổ sung 4 (H1–H5)

Gốc: FINAL v1.1 §16.1 cấu hình A = 50,10 t-n. Đơn vị: t-n (tuần-người). Bay và lặn là công nghệ chưa ai trong team làm, nên các dòng N6–N8 có sai số **±40%**.

## X1. Ngân sách lại

### PX-30 · Các dòng thay đổi và dòng mới (trên nền A)
| # | Hạng mục | A' | Ghi chú |
|---|---|---|---|
| N1 | Linh Nghĩ: từ lite lên C4 (tầng sprite C4, A1 Thăng, 3 thẻ M5/M6, tên cảnh, đường cong) | +0,40 | Dòng #1 cũ giữ 1,0 |
| N2 | Thanh Oa: lên C4 | +0,40 | |
| N3 | Đại diện Vũ: lên C4 | +0,40 | Đổi từ gà sang loài bay giỏi (WORLD chọn) trước khi vẽ sprite thì tốn 0 |
| N4 | Hợp Đạo × 3 loài (9 thẻ) | +0,15 | |
| N5 | Kiếp C4 × 3 (Phi Thăng I dùng lại template C3; Viên Mãn C4 dùng template của Mộc/Lang) | +0,20 | |
| N6 | **Hệ tầng Z dùng chung** cho cả bay lẫn lặn: 3 tầng rời Đất / Trên / Dưới, server tự lọc ai thấy ai theo tầng, ma trận ai đánh trúng ai, camera | +0,70 | Bay và lặn dùng chung một hệ, rẻ hơn khoảng 0,5 so với làm hai hệ riêng |
| N7 | **Bay thật**: cất cánh / lượn / hạ cánh / đậu cành, Thể Lực bay, art 8 hướng + bóng + cất/hạ cánh, Diều hâu AI đánh trên không, prediction phía client | +1,60 | |
| N7b | Gộp Sải Cánh vào bay (bớt phần trùng của dòng #3) | −0,20 | |
| N8 | **Sống dưới nước**: shader lớp nước, tileset đáy, thức ăn và CT dưới nước, 3 AI săn dưới nước (cá lớn, cá sấu AI, rắn nước) | +1,10 | |
| N8b | Bớt phần trùng với dòng #6 (Lặn, autotile nước sâu) | −0,15 | |
| N9 | Nội tại riêng × 5 + đặc tính tộc Thú/Trùng + tooltip | +0,40 | |
| N10 | UI: chỉ báo tầng, nút Cất/Hạ cánh **dùng chung ô BN1** (vẫn ≤5 nút), cập nhật thẻ chọn tộc | +0,15 | |
| N11 | QA/sim: duel giữa các tầng, 5 nhân vật full | +0,40 | Dòng #15 cũ giữ |
| | **Net mới** | **+5,55** | |
| | Xóa dòng cũ | 0 | HV-4 "lite thành đường farm" và luật "lite tính ½" hết hiệu lực, không tốn gì |

### PX-31 · Ba cấu hình mới (người dùng chọn, thay §16.2)
Đệm tính bằng % trên tổng việc. **Luật giữ nguyên: đệm dưới 8,5% thì không bao giờ là khuyến nghị.**

| | **A': Đủ hết** (khuyến nghị PX) | B': Rút gọn | C': Theo đợt |
|---|---|---|---|
| Tổng việc | 55,65 | 52,15 | 49,35 |
| Đệm | 4,75 (8,5%) | 4,45 (8,5%) | 4,20 (8,5%) |
| Soft launch | **Tuần 61** (dùng đệm 10% thì tuần 62) | Tuần 57 | Tuần 54 với 4 tộc + **Vũ đợt 2 ở tuần 58** (3,1 t-n) |
| Bị cắt | Không | c7–c13 của B cũ (−2,15) · bay không có đậu cành, Diều hâu là kẻ săn trên không duy nhất · dưới nước còn 2 AI, chỉ đổi màu bằng shader, không vẽ đáy riêng (−0,6) · Hợp Đạo của 3 loài mới sang 1.0 (−0,15) · **trả lại nước sâu ở Đầm Mục** (+0,1), vì Thủy cần lãnh thổ | Như B', hoãn cả Vũ (−2,8: lite + C4 + phần riêng của bay) |
| Rủi ro chính | Chậm hơn v1.1 6 tuần; bay chưa có số liệu thực | Linh Quỹ tĩnh vi phạm luật theme (§1.2) tới U1 | Hook "bay" (cảnh trailer mạnh nhất) không có ngày 1 |

- Cả ba đều giữ ≥4 tộc chơi được ngày 1. **Không có cấu hình 50 tuần nào giữ được 5 nhân vật full và đệm ≥8,5%.**
- Thứ tự làm (module): E → D → **N6 tầng Z** → Oa + lặn → Nghĩ → F → Vũ + bay → G.
- **Sửa cổng §16.3:**
  - Tuần 2: spike thêm bay trên 2 client trễ 150ms, cộng phần server lọc tầm nhìn theo tầng.
  - **Tuần 8**: prototype bay. Nếu lệch hit giữa các tầng >5% hoặc tụt <30fps trên máy yếu thì chuyển sang **C'**.
  - Tuần 16 (VS): có thêm Oa lặn dưới nước.
  - Tuần 24: một nhân vật full tốn >1,7 t-n thì áp B'.
- **Fallback bay cuối cùng** (không phải cấu hình bán ra): chỉ còn 1 tầng "Tán thấp", mỗi lần bay ≤8s.

## X2. Rủi ro UX/netcode trên mobile

### PX-32 · Rủi ro và cách giảm thiểu
| Rủi ro | Giảm thiểu |
|---|---|
| **Bầu trời thành vùng bất tử** | Bay tốn Thể Lực, 100 → 0 trong ~25s, rồi buộc hạ cánh · trên không CT ×0, không ăn, không Đả Tọa · cất cánh mất 0,6s và bị ngắt được · kẻ bay lộ trên Thần Thức ở tầm ×1,5 · Diều hâu và Vũ khác đánh được trên không · Quăng Lưỡi trúng kẻ bay thấp |
| Bay làm map trở nên tầm thường | Tán Thâm Lâm chặn bay · sét và bão cấm bay · Linh Hạch, Quả Ước, Nơi Trú đều nằm dưới đất |
| Camera và độ dễ đọc ở màn 844×390 | Zoom ra tối đa ×1,25 · luôn có bóng trên đất và vòng chỉ tầng · tầng là trạng thái rời, không phải độ cao liên tục |
| Netcode lệch trạng thái tầng | Server quyết định đổi tầng · thời gian cất cánh che độ trễ · chỉ bù lag cho các đòn cùng tầng · tốc bay ≤1,6× Lang để vùng tầm nhìn không bị xáo trộn liên tục ở 40 CCU |
| **Dưới nước thành vùng bất tử** (luật "CT ×0" đã bị đảo) | CT/giờ dưới nước ≤0,8× ở bờ · có AI săn dưới nước · Linh Hạch và mốc tu nằm trên bờ · Lang chờ được ở bờ |
| Lộ vị trí người đang lặn (cheat) | Server không gửi vị trí người ở tầng Dưới cho người tầng Đất; người tầng Đất chỉ thấy gợn nước |
| Shader nước trên Android/WebGL yếu; bundle ≤20MB | Tùy chọn chỉ đổi màu phẳng · tileset đáy nén chung atlas |
| Vũ hút quá nhiều người chọn (ngược với lo ngại Mộc độc chiếm) | Mở rộng HE-4: **không tộc nào >45%** |

### PX-33 · Giả thuyết playtest mới
| ID | Giả thuyết | Ngưỡng | GĐ | Nếu trượt |
|---|---|---|---|---|
| HB-1 | Bay không phải lối thoát chắc thắng | Vũ thoát khi bị đuổi ≤55% · thời gian ở trên không ≤35% | Alpha | Thể Lực bay cạn nhanh hơn ×1,3 |
| HB-2 | Đọc được tầng trên mobile | ≥80% gọi đúng tầng của 3 mục tiêu trong 3s · cất/hạ cánh nhầm <5% | VS | Đổi sang "giữ để cất cánh", tăng tương phản bóng |
| HB-3 | Netcode giữa các tầng ổn | Lệch hit ≤5% ở trễ 150ms · ≥30fps trên máy yếu ở 40 CCU | Spike tuần 8 | Chuyển C' |
| HN-1 | Dưới nước nguy hiểm thật | CT dưới nước ≤0,8× ở bờ · ≥20% số lần Oa chết xảy ra dưới nước | Alpha | Thêm AI, giảm thức ăn dưới nước |
| HN-2 | Lặn vui và có lý do lên bờ | ≥60% người chơi Oa ở dưới nước 30–70% thời gian · ≥65% nói được vì sao mình lên bờ | Alpha | Dời mốc tu lên bờ |

- Bỏ HV-4. HV-1 đổi thành "trung vị full ≤7h cho mọi tộc".
- Lưu ý cho HG-2: một đời full mất ~4,8h, nên thử đủ 5 tộc tới Viên Mãn mất ~24h. Cảm giác "mới mẻ mỗi đời" giờ dựa vào lúc chết và Tự Quy chứ không còn dựa vào đời lite ngắn. Cần đo.

## X3. FTUE và chọn tộc (PX-34): sửa nhỏ, khoảng 0,05 t-n, đã nằm trong N10
- **7:30:** thay gà rừng bới lá bằng đại diện Vũ mới **bay xuống từ cành rồi cất cánh lại**. Bay là hook, nên phải được nhìn thấy trước lúc chọn tộc.
- **10:30:** ếch AI bắt bướm xong **lặn mất xuống ao**.
- **14:00 Trung Ấm:** xác chìm, camera theo xuống dưới mặt nước 3s. Đây là lần đầu người chơi thấy tầng Dưới, dùng lại shader nên không tốn thêm.
- **Thẻ chọn tộc:** thêm 1 icon đặc tính tộc (Tự dưỡng / Săn / Bầy / Dưới nước / Bay). Không thêm chữ, không thêm chỉ số. Hero card vẫn là Mộc.
- **"Thắng đầu" ở đời 2:** Vũ cất cánh lần đầu trong ≤60s · Oa bắt cá dưới nước đầu tiên trong ≤3'.
- Hook store page / trailer: *"Mọc rễ, săn mồi, dẫn bầy, lặn sâu, cất cánh: năm cách sống trong một khu rừng."*
