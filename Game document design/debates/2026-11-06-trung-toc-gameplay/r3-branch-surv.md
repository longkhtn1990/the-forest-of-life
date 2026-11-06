# R3 bổ sung — SURV: phản biện Cây Hướng Nghĩ & nhịp (PROG-R3-01..03)

## 1. Hướng nào đổi vòng sinh tồn thật?
Thang đo: **Có** = đổi ít nhất 1 trong 5 trục (kiếm ăn, Tổ, bầy, đe dọa, Đông). **Combat** = chỉ đổi giao tranh.

| Nút | Đổi gì | Vấn đề | Sửa *(SURV-R3-xx)* |
|---|---|---|---|
| Binh | Bầy (2 Binh, nửa bầy mỗi lần mất 1 con), kiếm ăn (không Gửi Về) | OK. Hậu tự Tha nhiều hơn, rủi ro ngoài trời tăng | Giữ |
| Phu | Kiếm ăn, bầy | Trùng trục với Đại Lộ và Mạch Ngầm/Phu (cả 3 đều là "đường") | Chấp nhận vì đó là bản sắc Phu |
| Huyệt | **Tổ ẩn** (Sào ngầm, không lộ ngoài 6 ô) | (a) Mất tín hiệu "Gò nhìn từ 20 ô", Lang không còn đọc được mục tiêu. (b) "Không đặt ở bùn" sẽ khóa mục tiêu C4 nếu bến tính là bùn | **-01:** ẩn ngoài **12 ô** (không phải 6). Vòng sáng Gò vẫn hiện khi đang có trộm/giao tranh. Bến cạn tính là **đất khô**, Huyệt đặt được |
| Viên | **Nguồn ăn mới** (Mật) | Rệp nuôi = thức ăn không cạn, phá scarcity. Rải lên cây của người chơi Mộc mà không có Khế ước = ký sinh không có phản đòn | **-02:** Mật ≤**25%** No nạp vào mỗi giờ. Đàn rệp bị Nha/Oa ăn thì hết sau 3'. Chỉ rải lên cây AI, cây Khế ước, hoặc lau sậy (để dùng được ở Đầm C4). Rệp trên cây Mộc người chơi lạ hút −1% Thủy/phút **và cây thấy rệp** |
| **Hành Quân** | **Bỏ Sào → Tổ Di** | Phá luật **1 hang an toàn**: một điểm hồi sinh + kho 20 + Nơi Trú mang theo được, CD 5'. Hệ quả: lách Dời Tổ 1 lần/cảnh, Đông "chỉ hồi ở Tổ" thành vô nghĩa, Viên Mãn và Gò Tổ Cổ không có chỗ neo | **BLOCK → -03:** giữ Sào. **Trại Quân** = Ngách di động: dựng 3s, CD 5', chỉ dùng để hồi sinh Lính, **không kho, không Nơi Trú, không Nhập Định**, phá bằng 3 đòn. Thêm +1 lượt Dời Tổ mỗi cảnh. Fantasy du mục nằm ở Tràn Quân + Trại, không nằm ở "không nhà" |
| Toan Độc | Combat, kèm sink No (−4 mỗi lần) | OK | Giữ |
| Phục Địa | Phòng Tổ (bẫy) | Hố ẩn đặt ở đâu cũng được → AFK-grief ở lối kiếm ăn chung | **-04:** hố chỉ đặt trong Sân Tổ, hoặc tồn tại ≤3' nếu đặt ngoài |
| Mạch Ngầm | Tuyến Tha | "Tha trong mạch **không bị bắt**" xóa nỗi sợ cốt lõi của Nghĩ (chuyến Tha bị chặn). Trùng với Hợp Đạo Mạch Tổ | **-05:** Tốc Tha trong mạch ×0,6. Miệng mạch lộ 3s khi có vật đi qua. Phá Ngách thì cắt mạch. Mạch Tổ đổi thành toán tử (PROG đã nêu) |
| Diệp Viên | Hiện tại **chỉ +CT** | Vườn +3% CT không đổi vòng sinh tồn. Cắt Tán đánh cây Mộc **đang sống**: vừa trùng trục Quang hợp của Mộc, vừa phá luật "kiến dọn rừng" và luật khắc (Nghĩ ép được Mộc khỏe mà không cần Lang) | **-06:** đổi thành **Vườn Nấm** (đúng kiến cắt lá ngoài đời): 10 lá → 1 nấm/5', nấm không thối → **nguồn ăn mùa Đông**, trần ≤30% No Đông. Cắt Tán chỉ lấy lá từ cây AI hoặc cây Mộc Tàn. Muốn giữ debuff thì làm Cắt Tán lên cây Mộc Tàn (Căn Thương ×1,2). WORLD duyệt |
| Mục Rệp | Hồi máu từ rệp | Dòng Viên→Mục Rệp→Thánh Viên chồng 3 tầng sustain. Cả dòng chết khi ở Đầm C4 (không có cây) | **-07:** Gọi Mật hồi 6% **tiêu 1 đàn rệp** (đàn ngừng ra mật 60s). Áp -02 cho lau sậy |
| Nghĩ Vương | Combat | OK | Giữ |
| Đại Lộ | Đe dọa (Đường Cái server thấy được = tự lộ mình) | Câu "Không có nhà" mâu thuẫn -03 | Bỏ câu đó, phần còn lại giữ |
| Địa Cung | Tổ | Sân Tổ 12 ô có thể phá mốc Q7 (Lang vẫn thắng ≥40% trong Sân Tổ) | Sim lại Q7 với Huyệt+Địa Cung chồng nhau. Nếu Lang <40% thì giữ 8 ô, chỉ cho thêm sạc Hầm |
| Thánh Viên | Cộng sinh | Gai không trúng bầy = luật Khế ước đã có, nút này chỉ phủ rộng ra 20 ô | Đổi: Khế ước với Thánh Viên **không chiếm slot** của cây |

**Kết luận:** 7/14 nút đổi vòng sinh tồn thật (Binh, Phu, Huyệt, Viên, Mạch Ngầm, Diệp Viên sau khi sửa, Đại Lộ). 4 nút combat (Toan Độc, Phục Địa, Nghĩ Vương, Địa Cung) là chấp nhận được, vì Binh và Huyệt cần một nhánh giao tranh. Nhưng **mỗi Gốc phải có ≥1 Trung đổi vòng sinh tồn**. Hiện Binh chỉ đạt khi đi qua Hành Quân (đã sửa).

## 2. Nhịp chơi
**Đồng ý A + S1 + S3. Không đồng ý B làm mặc định.** B mất 4,5h mỗi lần chết, Mid chỉ 68%. Với luật mất trắng, mức đó vượt ngưỡng "đủ đau để bỏ game". S2: đồng ý không làm.

**Hazard mục tiêu mới (A, ÷√1,5 ≈ ÷1,22):**
| Cảnh | v1.2 | A | Kiểm chứng |
|---|---|---|---|
| C1–C2 | ≤0,15/h | **≤0,12/h** | Chết vì đói >0,04/h → kéo dài warning |
| C3 | ≤0,10/h | **≤0,08/h** | PvP ≤0,05 |
| C4 | ≤0,08/h | **≤0,065/h** | Cá Sấu ≤0,025 |

Kiểm tra độ phơi nhiễm mỗi đời: 1,5 (thời gian) × 0,8 (S3 bỏ 20% thời gian ra khỏi rủi ro) ÷ 1,22 (S1) ≈ **0,98× v1.2**. Khớp với Mid 73% PROG đã sim.

**Điều kiện cho S1:**
- Chỉ giảm **sự kiện gây chết** (Director thưa kẻ săn, Huyết Nguyệt). **Không** giảm mật độ thức ăn và **không** giảm số encounter không gây chết (trộm kho, mất Lính, nước tách bầy). Nếu cắt cả những thứ đó thì 99' của C3 thành buồn tẻ.
- Decay No mỗi phút giữ nguyên. Chuyến Tha ×1,5 là đúng chủ đích, nhưng **Hướng Tích phải thay ≥30% chuyến lặp** (bước công trình có mục tiêu), nếu không sẽ thành grind.
- **Số Đông mỗi đời giữ 2** (C2 Hậu, C4). Nếu mùa chạy theo đồng hồ server thì đời 5,5h có thể gặp 3 Đông. Cần neo mùa vào nhịp cảnh, hoặc sim lại với kho 40.

**Điều kiện cho S3:**
- Chỉ ở **Sào**: không ở Ngách, không ở Trại Quân.
- Rủi ro "thấp", không phải "≈0": trong lúc Nhập Định, trộm online vẫn lấy được kho theo luật Hang, và Hậu bị đánh thức khi có kẻ trong 8 ô.
- Mùa Đông: S3 chồng với No ×0,5 thì Đông thành AFK. Vì vậy trong Đông, trần S3 là ≤15%, và mục tiêu "ra ngoài ≥1 lần/Đông" vẫn giữ.

## 3. BLOCK
- **B-1 (Hành Quân "Bỏ Sào" + Đại Lộ "không có nhà"):** phá luật 1 hang an toàn, luật Đông chỉ hồi sinh ở Tổ, Viên Mãn ở Tổ và Gò Tổ Cổ. Gỡ block bằng **SURV-R3-03**.
- Không block, nhưng **bắt buộc sửa trước R4:** -05 (Mạch Ngầm), -06 (Diệp Viên/Cắt Tán), -02 (trần Mật).
