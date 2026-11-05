# R1 Proposal — PROG

> Domain: cảnh giới & tiến hóa, nguồn tu vi, skill tree, độ kiếp, hóa hình, luân hồi/meta, công thức sức mạnh, PvP giữa các cảnh giới, unlock pacing.
> Mô phỏng: `sim/prog_sim.py` (chạy: `python3 <SESSION>/sim/prog_sim.py`), kết quả đầy đủ ở `sim/prog_sim_output.md`. Mọi bảng số dưới đây lấy từ script, trừ khi ghi "thiết kế tay".

## 1. Cách tôi hiểu yêu cầu

Người dùng muốn một hệ tiến trình kiểu tiên hiệp: mỗi loài có tên cảnh giới riêng nhưng thang level dùng chung, mỗi loài nhận tu vi bằng một động từ khác nhau (quang hợp, gặm, săn, phân giải…), con đường tiến hóa rẽ nhánh, độ kiếp hùng tráng, hóa hình, và cái chết là luân hồi chứ không phải game over. Tất cả phải chạy trong khung **PvP tự do**, **phiên 15–60 phút**, **hành trình nhiều tuần**, **F2P không pay-to-win**, và **một người làm cùng AI**.

Giả định của tôi:
- **A1.** "Thành thần" là đích của *một kiếp* (một nhân vật). Luân hồi là vòng lặp dài hơn: nhiều kiếp, mỗi kiếp 3–10 tuần.
- **A2.** Mốc chuẩn là người chơi "Mid": 5 phiên/tuần × 40 phút. Kiếp đầu tới Thành Thần mất **6–9 tuần** (tính cả 1–2 lần chết). Core 3–5 tuần, Casual 12–18 tuần.
- **A3.** Sức mạnh dọc phải đủ rõ để thỏa trope "cảnh giới áp đảo", nhưng bị nén lại và đi kèm luật PvP, để người cảnh giới thấp vẫn có ba lựa chọn: **trốn, hợp lực, hoặc đánh úp người đang độ kiếp**.
- **A4.** Ra mắt với 5 loài, MVP 3 loài (cây – ăn cỏ – ăn thịt = chuỗi thức ăn tối thiểu). Mọi nội dung phải sinh được từ **template**, nhờ vậy loài mới chủ yếu là dữ liệu + art.

## 2. Ý tưởng cốt lõi (hook)

**"Mọi sinh linh cùng một Thiên Đạo."** Sói, cây và nấm cùng leo một thang 7 cảnh giới đo bằng một đơn vị chung là **Chu Thiên (CT)**. Thứ khác nhau là *cách* chúng tu: con đường tiến hóa của bạn được viết từ những gì bạn đã ăn, đã sống sót và đã giết. Khi chết, bạn mang theo một mảnh của kiếp trước sang kiếp sau.

## 3. Đề xuất chi tiết

### PROG-01: Thất Cảnh — khung cảnh giới chung (7 cảnh giới × 3 tầng)
- **Mô tả:** Có 6 cảnh giới để "cày", mỗi cảnh giới chia 3 tầng **Sơ / Trung / Hậu kỳ**, tổng cộng 18 tầng (chỉ số `n = 1..18`). Cảnh giới 7 **Thành Thần** không cày bằng tu vi mà đạt qua Thiên Kiếp và Thần Cách (PROG-13). UI hiển thị dạng "Trúc Cơ · Trung kỳ" kèm số cảnh giới nhỏ "C3" để người chơi so được giữa các loài.
- **Số liệu / quy tắc:**

| C | Tên chung (dùng cho UI so sánh) | Ý nghĩa gameplay | Vùng phù hợp |
|---|---|---|---|
| 1 | Khai Linh | Thức tỉnh ý thức; tutorial, 2 kỹ năng | Rừng Non |
| 2 | Tụ Linh | Hấp thụ linh khí; mở co-op, Linh Thức (thực vật) | Rừng Non |
| 3 | Trúc Cơ | **Chọn Huyết Mạch** (rẽ nhánh tiến hóa) | Rừng Non trong → Nguyên Sinh ngoài |
| 4 | Kết Đan | Mở **Đạo Đồ** (cây Đạo chung), bí cảnh cấp 1 | Rừng Nguyên Sinh |
| 5 | Hóa Hình | **Hóa hình** hoặc Bản Thể; pháp bảo | Nguyên Sinh trong → Cổ Đại ngoài |
| 6 | Xuất Khiếu | **Nguyên Thần xuất khiếu**, Nguyên Thần Bất Diệt | Rừng Cổ Đại |
| 7 | Thành Thần | Thần vị, Thần Lực, Phi Thăng | Lõi Rừng Cổ Đại / toàn server |

- **Tình huống:** Một người chơi sói thấy cây cổ thụ hiện "Niên Luân Kết Tâm · Sơ kỳ (C4)". Họ biết ngay cây đó cao hơn mình một cảnh giới mà không cần thuộc tên cảnh giới của loài cây.
- **Vì sao tốt:** 7 bậc là đủ để cảm nhận "leo núi" mà vẫn nằm gọn trong đầu người chơi casual (bảng 9 cảnh giới × 9 tầng của truyện thì quá dày). Ba tầng mỗi cảnh giới tạo mốc nhỏ khoảng mỗi 1–3 phiên.

### PROG-02: Bảng tên cảnh giới riêng theo loài (tương đương tuyệt đối về level)
- **Mô tả:** Mỗi loài có một bộ 7 tên. Tên chỉ là lớp vỏ: chỉ số, ngân sách sức mạnh và CT cần đều lấy từ `n`, không đọc tên. Viết tên cho một loài mới chỉ tốn một bảng 7 dòng, AI có thể đề xuất và người làm duyệt.

| C | Linh Mộc (cây thân gỗ) | Linh Thảo (cỏ/thảo mộc) | Lộc (hươu – ăn cỏ) | Lang (sói – ăn thịt) | Khuẩn (nấm) | Phong (ong – côn trùng, post-launch) |
|---|---|---|---|---|---|---|
| 1 | Mầm Linh | Hạt Thức | Ấu Lộc | Ấu Lang | Bào Tử | Ấu Trùng |
| 2 | Chồi Tụ Quang | Diệp Tụ Linh | Lộc Nhung | Lang Nha | Tơ Khuẩn | Kén Linh |
| 3 | Thân Mộc Trúc Cơ | Thảo Căn | Linh Giác | Lang Cốt | Khuẩn Võng | Phá Kén |
| 4 | Niên Luân Kết Tâm | Hoa Đan | Giác Đan | Huyết Đan / Lang Đan | Tán Đan | Phong Đan |
| 5 | Thụ Nhân | Thảo Tiên | Lộc Tiên | Lang Nhân | Khuẩn Nhân | Trùng Nhân |
| 6 | Mộc Hồn Xuất Khiếu | Vạn Diệp Hồn | Bạch Lộc Hồn | Nguyệt Lang Hồn | Vạn Tơ Hồn | Phong Hồn |
| 7 | Thần Mộc | Thảo Mẫu | Thần Lộc | Thiên Lang | Mẫu Khuẩn | Vạn Phong Mẫu |

- **Quy tắc tương đương:** Tại cùng `n`, mọi loài có cùng **Ngân sách Sức mạnh** `PB(n) = 100 × 1.10^(n−1)`. Mỗi loài phân bổ ngân sách đó theo vai trò (cây: Sinh Lực/Thủ cao, Tốc = 0; sói: Công/Tốc cao). Không có loài nào "mạnh hơn", chỉ có loài **khác hình dạng**.
- **Tình huống:** Một người chơi cây C4 và một người chơi sói C4 đánh nhau tại rễ cây. Cây có lợi thế vì đứng trên lãnh thổ của mình. Nếu sói lôi được trận đấu ra ngoài tầm rễ thì sói có lợi thế. Kết quả phụ thuộc vào vị trí và lựa chọn, không phụ thuộc vào loài.

### PROG-03: Chu Thiên (CT) — đơn vị chuẩn hóa tu vi và nguồn tu vi theo loài
- **Mô tả:** **1 CT = lượng tu vi chuẩn của 1 phút chơi tích cực ở cảnh giới hiện tại.** Mọi hành động sinh tu vi được định giá bằng CT, không phụ thuộc cảnh giới. Ví dụ "săn hạ con mồi cùng cảnh giới = 4.4 CT". Con số tu vi hiển thị (TV) tăng dần cho sướng mắt, `TV/phút = 10 × 1.25^(n−1)`, nhưng việc cân bằng chỉ làm trên CT. Đây là công cụ quan trọng nhất của tôi cho một studio 1 người: thêm loài mới chỉ cần bảng hành động định giá CT, sau đó chạy Monte Carlo để chỉnh hệ số `k_s` về **1.0 CT/phút ±10%**.
- **Nguồn tu vi (thiết kế tay, kèm giá trị trong sim):**

| Loài | Nguồn chính (~60%) | Nguồn phụ (~25%) | Nguồn đặc thù (~15%) |
|---|---|---|---|
| Linh Mộc | **Quang hợp** khi online: 0.45 CT/phút × ánh sáng (0.6–1.0, giảm khi bị tán cây lớn che, ban đêm) | **Cắm rễ** vào Linh Mạch / xác chết / suối: 1.2 CT mỗi lần, khoảng 1 lần/4 phút | **Phản vệ** đẩy lui kẻ ăn lá: 2.0 CT; **quả bị ăn**: 0.08 CT/phút (cộng sinh) |
| Linh Thảo | **Lan hạt** chiếm ô đất: 0.9 CT/lần, khoảng 1 lần/3 phút | Quang hợp nhẹ 0.35 CT/phút | **Phản Sinh**: bị gặm nhưng mọc lại, 0.8 CT |
| Lộc | **Gặm Linh Thảo**: 0.55 CT/phút × chất lượng ô cỏ (0.6–1.4) | Uống **Linh Tuyền**: 2.0 CT | **Kinh Hồn Ngộ Đạo**: thoát truy sát được 2.5 CT |
| Lang | **Săn** (tìm + đuổi khoảng 3 phút, thành công 55%): 4.4 CT trung bình | Ăn xác, đánh dấu lãnh thổ | Hạ người chơi cùng cảnh giới: 8 CT (PROG-12) |
| Khuẩn | **Phân giải xác** (phụ thuộc số cái chết trên server): 3.0 CT | Lan mạng tơ 0.30 CT/phút | **Khế ước cộng sinh** với cây 0.15 CT/phút (cả hai cùng nhận) |

- **Kết quả Monte Carlo** (phiên 40', 4000 lần chạy):

| Loài | CT/phút thô | k_s | Sau hiệu chỉnh | P10 | P90 | Biến thiên |
|---|---|---|---|---|---|---|
| Linh Mộc | 0.92 | 1.09 | 1.00 | 0.81 | 1.21 | 16% |
| Linh Thảo | 0.73 | 1.37 | 1.00 | 0.82 | 1.19 | 14% |
| Lộc | 0.92 | 1.09 | 1.00 | 0.73 | 1.27 | 21% |
| Lang | 0.85 | 1.17 | 1.00 | 0.59 | 1.46 | 34% |
| Khuẩn | 1.04 | 0.96 | 1.00 | 0.59 | 1.49 | 34% |

- **Đọc kết quả:** Tốc độ trung bình bằng nhau, nhưng **phương sai là bản sắc của loài**. Thực vật ổn định ("tu chậm mà chắc"), thú săn được ăn cả ngã về không. Đây là cách cân bằng mà vẫn giữ cảm giác khác biệt. Khuẩn có rủi ro cấu trúc: nếu server vắng thì không có xác để phân giải, nên cần một **sàn xác NPC** (SURV/WORLD đảm bảo mỗi vùng có khoảng ≥1 xác/5 phút).
- **Luật bổ sung:**
  - **Linh khí phù hợp vùng:** vùng có cảnh giới khuyến nghị thấp hơn bạn cho CT × 0.5^(chênh lệch). Vùng cao hơn cho CT × (1 + 0.25 × chênh lệch), tối đa +50%. Luật này đẩy người chơi vào sâu trong rừng và không cho người mạnh ở lại farm Rừng Non.
  - **Chống AFK cho thực vật:** quang hợp chỉ chạy khi online. Nếu không có tương tác trong 3 phút thì rơi vào "Linh Thức Tán Loạn", tốc độ ×0.2.
  - **Cộng sinh là trò chơi dương:** khế ước cây–nấm, ong–hoa thì **mỗi bên nhận 60%** giá trị chứ không chia đôi 50/50. Hợp tác vì vậy có lợi thật nhưng có trần (tối đa 25% CT/phút đến từ cộng sinh).

### PROG-04: Đường cong tu vi và lịch tuần
- **Công thức:** `CT_cần(n) = min(180, 4 × n^1.45)`. Đầu game là đường đa thức để tầng đầu chỉ mất vài phút, sau đó có **trần 180 CT/tầng** từ C5 trở đi để mỗi tầng muộn không vượt khoảng 3 phiên của người chơi Mid. Ngoài ra mỗi lần rời một cảnh giới tốn thêm chi phí "Cơ Duyên + Độ Kiếp" (10/25/45/60/90 CT-tương-đương).

| n | Cảnh giới · Tầng | CT cần | Lũy kế | TV hiển thị cần |
|---|---|---|---|---|
| 1 | C1 Khai Linh · Sơ | 4 | 4 | 40 |
| 2 | C1 · Trung | 11 | 15 | 137 |
| 3 | C1 · Hậu | 20 | 35 | 307 |
| 4 | C2 Tụ Linh · Sơ | 30 | 64 | 583 |
| 6 | C2 · Hậu | 54 | 159 | 1,640 |
| 7 | C3 Trúc Cơ · Sơ | 67 | 227 | 2,564 |
| 9 | C3 · Hậu | 97 | 405 | 5,768 |
| 10 | C4 Kết Đan · Sơ | 113 | 518 | 8,399 |
| 12 | C4 · Hậu | 147 | 794 | 17,096 |
| 13 | C5 Hóa Hình · Sơ | 165 | 959 | 23,999 |
| 14–15 | C5 · Trung/Hậu | 180 | 1,319 | 40,927 |
| 16–18 | C6 Xuất Khiếu | 180 | 1,859 | 79,936 |

Tổng: **1,859 CT** cho các tầng, cộng 230 CT cho Cơ Duyên/Độ Kiếp, tức **2,089 CT**. Chia theo cảnh giới: C1 35 · C2 125 · C3 246 · C4 389 · C5 525 · C6 540.

- **Tĩnh Tu Tích Lũy (rested bonus):** khi offline, hồ chứa đầy dần, đầy sau 8 giờ. Hồ đầy cho **30 phút đầu của phiên kế tiếp được ×2 CT**. Cơ chế này thay cho "tu vi thụ động khi offline", vì tu vi thụ động sẽ biến thực vật thành game AFK. Nó cũng khiến phiên 15 phút có giá trị gấp đôi: phù hợp brief.
- **Lịch thời gian thực** (hiệu suất thời gian tích cực 85%, có rested, **không tính chết**), đơn vị là tuần:

| Hồ sơ | CT/tuần | →C2 | →C3 | →C4 | →C5 | →C6 | →C7 (Thiên Kiếp) |
|---|---|---|---|---|---|---|---|
| Casual 3×25' | 128 | 0.3 | 1.3 | 3.5 | 6.9 | 11.4 | 16.4 |
| **Mid 5×40'** | 320 | 0.1 | 0.5 | 1.4 | 2.7 | 4.6 | **6.5** |
| Core 7×60' | 567 | 0.1 | 0.3 | 0.8 | 1.5 | 2.6 | 3.7 |

Người chơi Mid cần khoảng **21.8 giờ chơi thực** để chạm Thiên Kiếp. **Phiên đầu tiên** (người mới có hồ rested đầy): tầng 1 xong ở phút 3, tầng 2 ở phút 9, hết C1 ở phút 21, sau đó độ Tiểu Kiếp lên **C2 trước khi phiên 25–30 phút kết thúc**. Đây là "lời hứa" đầu tiên.
- **Bù đắp cho Casual:** nếu cảnh giới của bạn thấp hơn trung vị server từ 2 bậc trở lên, bạn nhận **Thiên Đạo Bù Đắp +25% CT**. Ước tính kéo Casual từ 16.4 xuống còn khoảng 13–14 tuần; cần sim lại khi có telemetry.

### PROG-05: Huyết Mạch — tiến hóa rẽ nhánh viết bằng hành động
- **Mô tả:** Khi đột phá lên **C3 Trúc Cơ**, mỗi loài chọn **1 trong 3 Huyết Mạch**. Lựa chọn này đổi hình dạng (sprite variant), bộ kỹ năng và Ngũ hành. Điểm mấu chốt là **learn-by-doing**: trong C1–C2, hành vi của bạn tích lũy *Huyết Mạch Ấn* cho từng nhánh. Nhánh nào đủ ấn thì được mở. Nhánh có nhiều ấn nhất luôn mở, để không ai bị khóa hết lựa chọn. Mỗi điều kiện làm được trong 1–2 phiên.

| Loài | Nhánh A | Nhánh B | Nhánh C |
|---|---|---|---|
| Lang | **Huyết Lang** (Hỏa) — chảy máu, hút máu, cuồng hóa khi máu thấp. *Ấn:* 20 đòn gây chảy máu hoặc 5 lần ăn xác tươi | **Phong Lang** (Mộc/Phong) — lướt, săn theo đàn, buff tốc độ cho đồng đội. *Ấn:* 3 km chạy nước rút, 5 lần săn thành công khi đang tăng tốc | **Băng Lang** (Thủy) — làm chậm, đóng băng, chịu đòn. *Ấn:* 20 phút ở vùng Hàn hoặc ăn 5 Băng Tâm Thảo |
| Lộc | **Linh Giác Lộc** — hồi máu đàn, kết giới | **Thiết Giác Lộc** — xung phong húc, tank | **Ảnh Lộc** — ẩn thân, phân thân ảo ảnh, chuyên thoát thân |
| Linh Mộc | **Thiết Mộc** — vỏ gai, phản sát thương, bất động mà cứng | **Linh Quả Thụ** — kết linh quả buff đồng minh, kinh tế cộng sinh | **Huyết Đằng** — dây leo ăn thịt, bẫy, kéo con mồi lại gần |
| Linh Thảo | **Dược Thảo** — kẻ ăn mình là đồng minh thì được hồi máu | **Độc Thảo** — kẻ thù ăn mình thì trúng độc, phản phệ | **Phong Thảo** — hạt bay, "đa thân", nhảy giữa các bụi cỏ |
| Khuẩn | **Mục Khuẩn** — phân giải xác, dựng xác thành con rối | **Huyễn Khuẩn** — bào tử gây ảo giác, đảo điều khiển | **Tâm Võng** — mạng tơ chia sẻ tầm nhìn, nối cây đồng minh |
| Phong | **Chiến Phong** | **Mật Phong** (kinh tế mật/thụ phấn) | **Hậu Phong** (triệu hồi đàn) |

- **Tình huống:** Minh chơi sói, hay lẩn vào vùng tuyết để trốn đàn Huyết Lang khác. Đến lúc đột phá Trúc Cơ, cậu thấy cả Phong Lang lẫn Băng Lang đã mở, trong đó Băng Lang sáng nhất vì nhiều ấn nhất. Cậu nhận ra con đường của mình đã thành hình từ chính cách mình sống sót.
- **Vì sao tốt:** Câu trả lời cho câu hỏi "sau 10 giờ khác nhau ở đâu?" là: 5 loài × 3 nhánh = **15 dạng sinh linh khác nhau** ngay từ tuần 1. Chi phí art cũng có kiểm soát: mỗi loài cần 1 base + 3 variant, tổng **20 bộ sprite** khi ra mắt với 5 loài.

### PROG-06: Đạo Đồ — kiến trúc skill tree (chi phí sản xuất được tính sẵn)
- **Cấu trúc 3 lớp:**
  1. **Bản Năng** (riêng mỗi loài): 6 node, trong đó có 2 kỹ năng chủ động. Mở từ C1.
  2. **Huyết Mạch** (riêng mỗi nhánh): 10 node, gồm 3 chủ động (A1 ở C3, A2 ở C4, **Thần Thông** tối thượng ở C5), **2 cặp Keystone loại trừ nhau** (chọn 1 trong 2 ở C4, chọn 1 trong 2 ở C6), 3 Notable, 1 Minor.
  3. **Đạo Đồ chung** (dùng cho mọi loài, mở ở C4 Kết Đan): 4 Đạo × 6 node. **Sát Đạo** (tấn công), **Hộ Đạo** (bảo vệ/co-op), **Sinh Đạo** (cộng sinh/kinh tế), **Ẩn Đạo** (ẩn/thoát). Mỗi kiếp đầu tư tối đa vào 2 Đạo.
- **Điểm:** 1 điểm mỗi tầng (18) + 1 điểm mỗi lần độ kiếp thành công trước C7 (5), tổng **23 điểm cho 40 node khả dụng (~57%)**, nên người chơi buộc phải chọn. **Khóa kép:** điểm đến từ tu vi, còn quyền lấy Notable/Keystone đến từ **Đạo Ngộ** (thử thách hành động, ví dụ "kết liễu 3 con mồi bằng chảy máu"). Nhờ vậy giữa những tầng dài 180 CT vẫn liên tục có thứ mới để mở.
- **Loadout thân thiện cảm ứng:** 4 ô kỹ năng chủ động + 1 ô Thần Thông + tấn công cơ bản.
- **Respec:** tẩy điểm miễn phí trong cùng Huyết Mạch tại Linh Huyệt, 1 lần/ngày. **Huyết Mạch thì cố định cho cả kiếp**, chỉ luân hồi mới đổi được. Cái chết vì vậy đồng thời là cơ hội làm lại build, đúng với chủ đề.
- **Chi phí sản xuất:** mỗi loài có 2 + 3×3 = **11 kỹ năng chủ động**. 5 loài ra mắt là 55 kỹ năng, nhưng chỉ dựng từ **khoảng 12 template** (lướt, nón, vòng AoE, đạn, vùng DoT, khiên, triệu hồi, ẩn thân, trói/làm chậm, hào quang, biến hình, kênh niệm). Mỗi kỹ năng là một bộ tham số cộng VFX tô lại màu. Đạo Đồ chung có 24 node, viết một lần dùng cho mọi loài. MVP: 3 loài × 11 = 33 kỹ năng. Vertical slice: 1 loài, 2 Huyết Mạch.
- **Tỉ lệ node:** Keystone 15% · Notable 45% · Minor 10% · Chủ động 30%. Tôi cố ý giữ rất ít node "+x%".

### PROG-07: Độ Kiếp — đột phá là một màn chơi, không phải một nút bấm
- **Điều kiện:** đầy CT tầng Hậu kỳ + **Cơ Duyên** của cảnh giới (ví dụ: lên Kết Đan cần một Linh Hạch từ bí cảnh hoặc một bữa ăn/hấp thu từ nguồn cảnh giới ≥ của mình). Sau đó kích hoạt kiếp tại một địa điểm do người chơi chọn.

| Đột phá | Loại kiếp | Thời lượng | Công khai | Nội dung | Thất bại |
|---|---|---|---|---|---|
| C1→C2, C2→C3 | Tiểu Kiếp | 60–90s | Không | Né lôi có báo trước | Mất 10% CT tầng, thử lại ngay |
| C3→C4 | Trung Kiếp | 2 phút | Hiện trong vùng | Lôi + **Tâm Ma** (đánh bản sao dùng kỹ năng của chính mình) | Mất 30% CT tầng, debuff "Đạo Cơ Tổn" 20' |
| C4→C5 (Hóa Hình) | Trung Kiếp | 3 phút | Hiện trong vùng | Lôi + Tâm Ma + đợt yêu thú | như trên |
| C5→C6 | Đại Kiếp | 4 phút | **Thông báo cả server** | 3 pha, thời tiết vùng đổi | như trên + rơi 1 tầng nếu thua 3 lần liên tiếp |
| C6→C7 | **Thiên Kiếp** | 10 phút | World event | xem PROG-13 | **Chết** (luân hồi, Đạo Tâm ×2) |

- **Điều chỉnh độ khó:** sát thương kiếp = gốc × (1 + 0.10 × **Sát Nghiệp**) × (1 − 0.15 × số lần thất bại trước đó, sàn 0.55). Mục tiêu tỉ lệ thành công lần đầu là 60–70%, sau 3 lần là ≥95%.
- **Hộ Pháp:** bạn bè đứng trong vòng kiếp có thể chặn người chơi khác vào phá. Ngược lại, người ngoài có thể **đánh úp người đang độ kiếp**: kẻ độ kiếp bị kẹt trong vòng và chỉ còn 50% sát thương ra ngoài. Đây là cơ hội hợp lệ để người cảnh giới thấp hơn hạ người cao hơn, và là khoảnh khắc "hùng tráng + tàn khốc" đúng tone.
- **Tình huống:** Một Thiết Mộc C4 Hậu kích hoạt kiếp lên Hóa Hình ở bìa Rừng Nguyên Sinh. Cả vùng thấy cột mây sét. Hai sói C3 lao tới định đánh úp. Đàn ong bạn của cây giữ vòng ngoài. Sau 3 phút, cây hóa hình trong tiếng sét.

### PROG-08: Hóa Hình (C5) — một lựa chọn ngang, không phải nâng cấp bắt buộc
- **Hai đạo, chọn khi đột phá C5 (đổi lại được bằng kiếp):**
  - **Nhân Hình Đạo:** có dạng người (dùng **một rig humanoid chung** cho mọi loài, chỉ thay bộ phận như tai, sừng, lá, vảy). Đổi dạng mất 2s, hồi chiêu 60s. Ở dạng người: chỉ số chiến đấu −15%, đổi lại mở **2 ô Pháp Bảo**, chế tác, nói chuyện với phe NPC, vào bí cảnh "Nhân giới". **Với thực vật:** dạng người rời khỏi Bản Thể (cây gốc vẫn đứng nguyên). Nếu Bản Thể bị hạ thì bạn chết. Thực vật đổi được khả năng di chuyển, đánh cược bằng gốc rễ.
  - **Bản Thể Đạo:** từ chối hóa hình. Nhận **+10% chỉ số vĩnh viễn**, kích thước "Yêu Thân" (to hơn 30%, áp đảo vùng), cùng 1 Keystone độc quyền. Bị mất pháp bảo và chế tác.
- **Vì sao tốt:** người dùng muốn có hóa hình, nhưng nếu nó là nâng cấp thuần thì mọi người đều trông giống nhau. Biến nó thành ngã rẽ (giao lưu/công cụ đối lại sức mạnh thô) tạo thêm một chiều build. Chi phí chỉ là 1 rig chung.

### PROG-09: Xuất Khiếu (C6) và Nguyên Thần Bất Diệt
- **Xuất Khiếu chủ động:** phóng Nguyên Thần ra khỏi thân trong 90s (hồi chiêu 5'). Nguyên Thần đi xuyên địa hình, do thám, **đoạt xá tạm** một sinh vật NPC thấp hơn ≥2 cảnh giới, hoặc đánh nhau trên "Linh giới" với Nguyên Thần khác. Trong lúc đó thân xác bất động. **Thực vật có bản lite từ C2** gọi là *Linh Thức* (chỉ do thám, 30s), vì phần này thuộc fantasy cốt lõi của chơi cây theo brief.
- **Nguyên Thần Bất Diệt:** khi thân xác C6 chết, Nguyên Thần thoát ra. Nếu về tới Linh Huyệt (nhà) trong 60s mà không bị bắt (kỹ năng Thần Thức/Ẩn Đạo có thể săn hồn), bạn **trùng sinh tại chỗ, chỉ rơi 1 tầng** thay vì luân hồi. Luật này giải bài toán "chết ở C6 mất gần 2 tuần" (xem PROG-10) và cho Xuất Khiếu một vai trò sinh tử.

### PROG-10: Luân Hồi — meta-progression giữ gì, mất gì

| **Giữ** | **Mất** |
|---|---|
| **Đạo Tâm** (tiền tệ meta, = 10 × C_đỉnh² + thành tựu) | Cảnh giới, CT, Huyết Mạch, điểm Đạo Đồ |
| **Tiền Kiếp Hồi Ức**: ×3 CT đến hết cảnh giới (đỉnh − 1), ×1.5 đến lại đỉnh cũ | Pháp bảo/vật phẩm mang theo (rơi tại xác) |
| **1 Túc Tuệ**: mang 1 node Notable của kiếp trước sang loài mới (2 ô khi Đạo Tâm cao) | Lãnh thổ/rễ (biến thành dinh dưỡng cho rừng) |
| Codex (loài/thảo dược/quái đã biết), danh tiếng clan, cosmetic | |

- **Xác thành dinh dưỡng:** xác của bạn trở thành một điểm Linh Mạch tạm thời (30'). Giá trị bằng 20% CT tầng cuối của bạn, chia cho thực vật/nấm hấp thu. Cái chết của người này nuôi sự sống của người khác, và đây cũng là nguồn chính của loài Khuẩn.
- **Chi phí leo lại (sim, chết ở tầng Trung):**

| Chết tại | CT mất nếu không có catch-up | CT leo lại có catch-up | Tuần (Mid) | Phiên 40' | Đạo Tâm nhận |
|---|---|---|---|---|---|
| C2 Tụ Linh | 64 | 31 | 0.10 | 0.5 | 40 |
| C3 Trúc Cơ | 237 | 103 | 0.32 | 1.6 | 90 |
| C4 Kết Đan | 553 | 228 | 0.71 | 3.6 | 160 |
| C5 Hóa Hình | 1,039 | 415 | 1.30 | 6.5 | 250 |
| C6 Xuất Khiếu | 1,639 | 630 | 1.97 | 9.8 | 360 (hoặc chỉ rơi 1 tầng nhờ Nguyên Thần Bất Diệt) |

  Đánh giá: từ C2 đến C4 là "khắc nghiệt vừa" (dưới 1 tuần). C5 khá đau (1.3 tuần), cố ý như vậy để mỗi trận PvP ở Rừng Cổ Đại có sức nặng. Tôi chấp nhận để SURV/PX tranh luận điều chỉnh hệ số ×3 (×4 sẽ đưa C5 về khoảng 1 tuần).
- **Đạo Tâm Bàn (20 node, chủ yếu ngang):** mở loài mới, Huyết Mạch "biết trước" (thấy điều kiện ấn từ C1), thêm preset loadout, ô Túc Tuệ thứ 2, hào quang cosmetic, điểm xuất phát (vùng sinh). **Luật cứng: không node nào tăng chỉ số chiến đấu. Trần tổng là +10% tốc độ CT.** Người chơi lâu năm được nhiều lựa chọn hơn chứ không mạnh hơn khi gặp người mới cùng cảnh giới.
- **Tình huống:** Lan chết ở C4 khi là Huyết Lang. Cô đầu thai thành Linh Mộc và mang Túc Tuệ "Lang Khứu" (đánh hơi kẻ săn trong 25m). Kết quả là một cây "biết ngửi thấy sói", build lai giữa hai kiếp mà chưa ai có. Cô lên lại C3 sau khoảng 3 phiên.

### PROG-11: Formula Sheet — 6 chỉ số hiển thị
- **Chỉ số:** Sinh Lực (HP), Linh Lực (năng lượng kỹ năng), Công, Thủ, Tốc, Thần Thức (phát hiện/ẩn).
- **Scaling dọc:** `HP(n), Công(n) = base_s × 1.10^(n−1)`, tương đương ×1.33 mỗi cảnh giới. **Tốc không tăng theo cảnh giới** (chỉ thay đổi theo loài/nhánh, tối đa ±15%). **Thần Thức** chỉ được +5% mỗi cảnh giới. Đây là đòn bẩy chống bắt nạt quan trọng nhất: kẻ mạnh không chạy nhanh hơn và không nhìn xa hơn nhiều.
- **Sát thương:** `Dmg = Công × Hệ_số_kỹ_năng × (1 − DR) × E × C`
  - `DR = Thủ / (Thủ + K(n_tấn_công))`, với `K(n) = 100 × 1.10^(n−1)` và `Thủ = d_build × K(n)`. Cùng tầng thì `DR = d/(1+d)`. Ví dụ d = 0.5 cho DR 33%, trần DR 75%.
  - `E` (Ngũ hành): khắc ×1.25, bị khắc ×0.80, trung tính ×1.0.
  - `C` (Hội tâm): tỉ lệ cơ bản 5%, trần 40%, ×1.5.
- **Ví dụ:** Huyết Lang C4 Sơ (n=10) có Công 50 × 1.1⁹ = 118. Dùng "Huyết Trảo" (hệ số 1.6) lên Thiết Mộc C4 Sơ (d=0.8, tức DR 44%, Mộc bị Hỏa khắc nên ×1.25): 118 × 1.6 × 0.56 × 1.25 ≈ **132**. HP của cây C4 Sơ khoảng 220 × 1.1⁹ = 519, tức cần khoảng 4 đòn khi khắc hệ, 3 đòn nếu có hội tâm, hoặc 5 đòn nếu không khắc hệ (TTK khoảng 4–6 giây, đủ thời gian để phản ứng trên mobile).

### PROG-12: PvP giữa các cảnh giới — dọc rõ ràng, không vô vọng
- **Mô phỏng** (sức mạnh = HP × DPS, nhiễu log-normal σ = 0.40 đại diện cho kỹ năng tay, build, địa hình, đánh úp):

| Chênh lệch | Hệ số chỉ số | Tỉ lệ sức mạnh | TTK so với cùng cấp | P(thấp thắng 1v1) | P(2 thấp thắng 1 cao) |
|---|---|---|---|---|---|
| 1 tầng | ×1.10 | ×1.21 | 83% | **37%** | 99% |
| 2 tầng | ×1.21 | ×1.46 | 68% | 25% | 98% |
| 1 cảnh giới | ×1.33 | ×1.77 | 56% | **15%** | 96% |
| 2 cảnh giới | ×1.77 | ×3.14 | 32% | 2% | **70%** |
| 3 cảnh giới | ×2.36 | ×5.56 | 18% | 0% | 27% (cần 3 người) |
| 4 cảnh giới | ×3.14 | ×9.85 | 10% | 0% | 4% (cần 4) |
| 6 cảnh giới | ×5.56 | ×30.9 | 3% | 0% | 0% (cần 6) |

  Kết quả: **"vượt một cảnh giới mà thắng" xảy ra khoảng 1/7 trận** (đủ hiếm để thành giai thoại, đúng trope thiên tài). Chênh 2 cảnh giới thì phải hợp lực. Chênh từ 3 cảnh giới trở lên thì phải trốn. Trốn khả thi vì Tốc không tăng theo cảnh giới.
- **Bốn luật giữ PvP tự do mà không vô vọng:**
  1. **Thiên Đạo Áp Chế (level-sync xuống):** trong Rừng Non mọi chỉ số bị kéo về trần n = 9 (C3 Hậu). Ở vùng ngoài của Nguyên Sinh trần là n = 15. Một C6 Hậu vào Rừng Non với một C2 Trung có tỉ lệ sức mạnh giảm từ ×11.9 xuống còn ×2.1 (P thấp thắng ≈ 9%). Người mạnh vẫn mạnh hơn và vẫn giữ kỹ năng, nhưng bị nén lại, nên không có chuyện "ai cũng bị one-shot".
  2. **Sát Nghiệp:** giết người chơi thấp hơn bạn ≥2 cảnh giới (sau khi đã áp chế) cho **+1 Nghiệp**. Mỗi Nghiệp tăng 10% sát thương kiếp kế tiếp. Từ 3 Nghiệp trở lên bạn bị đánh dấu **Huyết Sát** trên bản đồ, và ai hạ được bạn nhận ×3 thưởng. Nghiệp giảm 1 sau mỗi 2 giờ chơi. Chuỗi thức ăn tự nhiên (chênh <2) không sinh Nghiệp. Tự do vẫn giữ nguyên, chỉ là bắt nạt có giá phải trả ở đúng khoảnh khắc người chơi quý nhất là độ kiếp.
  3. **Thưởng theo chênh lệch:** hạ người chơi được `8 CT × m`. Nếu nạn nhân thấp hơn `g` cảnh giới thì `m = 0.25^g`. Nếu nạn nhân cao hơn thì `m = 1 + 0.5g` (danh hiệu **Nghịch Thiên**). Cùng một cặp người chơi chỉ cho thưởng đầy đủ 1 lần mỗi 30 phút (chống farm/đổi mạng).
  4. **Đánh úp kiếp** (PROG-07) và **Thần Quy** (PROG-13): kẻ yếu có cửa sổ hợp lệ để lật kèo, còn kẻ mạnh nhất có giới hạn với kẻ yếu nhất.

### PROG-13: Thành Thần (C7) — endgame có vòng quay
- **Điều kiện Thiên Kiếp:** C6 Hậu viên mãn + **Thần Cách** (một trong ba: bảo vệ rừng trong một world event, nhận Tín Ngưỡng từ ≥10 người chơi khác, hoặc hạ một Cổ Thú). Thiên Kiếp là world event 10 phút, cả server thấy, ai cũng có thể giúp hoặc phá.
- **Thần vị có hạn:** đề xuất **5 Thần vị/server theo Ngũ hành** (WORLD quyết định lore). Thần nhận Thần Lực từ sức khỏe khu rừng và tín đồ, được ban phước/giáng họa lên vùng và kích hoạt sự kiện nhỏ. **Thần Quy:** Thần không tấn công trực tiếp người chơi dưới C5, chỉ tác động qua sự kiện. Thần có thể bị thách đấu bởi một C6 Hậu đang có Thần Cách.
- **Phi Thăng:** sau 14 ngày hoặc khi hết mùa, Thần phi thăng, được khắc tên lên **Thần Mộc Bia**, nhận cosmetic vĩnh viễn và Đạo Tâm lớn, rồi luân hồi (bắt đầu kiếp mới). Thần vị luôn quay vòng nên server không bị một người chiếm vĩnh viễn. Ở chế độ solo: thành Thần là màn kết thúc, sau đó Phi Thăng sang một khu rừng mới và giữ Đạo Tâm.

### PROG-14: Unlock Timeline (người chơi Mid, thời gian thực)

| Thời điểm | Mở khóa | Loại gate |
|---|---|---|
| 0–5' | Di chuyển, ăn/quang hợp, tầng 1, kỹ năng Bản Năng 1 | Hướng dẫn |
| ~20' | **Tiểu Kiếp đầu tiên → C2**, kỹ năng 2 | Tu vi |
| Phiên 2 | Co-op mời bạn, Linh Thức (thực vật), Huyết Mạch Ấn hiển thị | Tu vi |
| Phiên 3–4 (~0.5 tuần) | **C3: chọn Huyết Mạch** (đổi hình), A1 | Tu vi + hành động |
| ~1 tuần | Bí cảnh đầu tiên (Cơ Duyên Kết Đan), vào Rừng Nguyên Sinh | Vật phẩm |
| 1.4 tuần | **C4: Đạo Đồ**, Keystone 1, Trung Kiếp đầu tiên có Tâm Ma | Tu vi + Cơ Duyên |
| 2.7 tuần | **C5: Hóa Hình / Bản Thể**, Thần Thông, pháp bảo | Kiếp |
| 4.6 tuần | **C6: Xuất Khiếu**, Keystone 2, Rừng Cổ Đại | Đại Kiếp |
| ~6.5 tuần | Thiên Kiếp, tranh Thần vị | Thần Cách + world event |
| Lần chết đầu (bất kỳ lúc nào) | Đạo Tâm Bàn, Túc Tuệ, chọn loài mới | Sự kiện |

  Kiểm tra dry spell: từ C5 trở đi mỗi tầng tốn khoảng 2.8 phiên Mid. Khoảng giữa các tầng được lấp bằng Đạo Ngộ (mở quyền node), bí cảnh và world event, nên mục tiêu là không có quá 1 phiên trôi qua mà không có thứ mới.

### PROG-15: Build Archetype Cards (chứng minh có đa dạng build)

| Build | Fantasy | Lõi | Mạnh | Yếu / đối trọng |
|---|---|---|---|---|
| **Huyết Lang + Sát Đạo** | Kẻ săn đơn độc | Chảy máu, hút máu, Keystone "Huyết Cuồng" | Burst, tự hồi máu | Băng Lang làm chậm; bị Sát Nghiệp nếu săn kẻ yếu |
| **Thiết Mộc + Hộ Đạo + Bản Thể** | Pháo đài cổ thụ | Gai phản sát thương, kết giới | Giữ lãnh thổ, hộ pháp kiếp cho clan | Bất động, bị Huyễn Khuẩn và lửa khắc |
| **Linh Quả Thụ + Khuẩn Tâm Võng (2 người)** | Rừng cộng sinh | Quả buff + mạng tơ chia tầm nhìn | Kinh tế co-op, CT ổn định | Phụ thuộc đồng minh |
| **Ảnh Lộc + Ẩn Đạo** | Kẻ sống sót bất tử | Ẩn thân, ảo ảnh, Kinh Hồn Ngộ | Gần như không bắt được | Sát thương thấp, Thần Thức cao khắc |
| **Phong Thảo + Nhân Hình** | Linh hồn lang bạt | Đa thân, nhảy bụi cỏ, pháp bảo | Cơ động/do thám | Mỏng, mỗi thân dễ bị gặm |

  **Stress-test dồn một hướng:** dồn Sát Đạo + Huyết Lang + Bản Thể cho DPS cao nhất. Bản Thể +10% và Huyết Cuồng +20% khi máu dưới 30% chỉ cộng tối đa khoảng ×1.32, tức thấp hơn khoảng cách một cảnh giới (×1.77 sức mạnh). Combo xấu nhất là "Ảnh Lộc ẩn + Thần Thông AoE" để đánh úp người đang độ kiếp. Cách chặn: phá ẩn khi bước vào vòng kiếp. Cần playtest.

## 4. Kết nối với các domain khác
- **SURV:** cần tần suất chết dự kiến theo cảnh giới (để sim lại thời gian nhiều tuần), sàn xác NPC cho Khuẩn, đói/khát tác động lên CT như thế nào (tôi đề xuất needs thấp thì CT ×0.5, không thì ×0). Độ căng của luân hồi phải phù hợp bảng PROG-10.
- **WORLD:** tên/lore 7 cảnh giới và 5 Thần vị, vùng Hàn/Hỏa để làm điều kiện Huyết Mạch, bí cảnh làm Cơ Duyên, độ sâu vùng (Non/Nguyên Sinh/Cổ Đại) khớp với trần Áp Chế n = 9/15/không trần.
- **PX:** duyệt Tĩnh Tu ×2 trong 30 phút, rewarded ads (tôi đề xuất **chỉ nạp thêm tối đa 5 phút hồ Tĩnh Tu, 1 lần/ngày**, tương đương +5 CT/ngày, khoảng +8% CT/tuần với Mid. Không bao giờ cho CT trực tiếp, Đạo Tâm hay vật phẩm Cơ Duyên). Pass cosmetic: hào quang độ kiếp, skin Huyết Mạch. Ước lượng chi phí cho 12 template kỹ năng và 20 bộ sprite.
- **Mọi người:** chốt danh sách loài ra mắt. Tôi đề xuất MVP Linh Mộc/Lộc/Lang, ra mắt thêm Linh Thảo + Khuẩn, mùa 1 thêm Phong.

## 5. Rủi ro tự nhận diện
1. **Quá nhiều tầng hệ thống** (Huyết Mạch + Đạo Đồ + Keystone + Túc Tuệ + Đạo Tâm Bàn). Biện pháp: FTUE chỉ hiện Bản Năng cho tới C3. Đạo Đồ chỉ xuất hiện ở C4. Đạo Tâm Bàn chỉ xuất hiện sau lần chết đầu tiên. Mỗi lớp được giới thiệu cách nhau ít nhất 1 tuần.
2. **CT chuẩn 1.0/phút là lý thuyết.** Thực tế thực vật có thể nhàm, thú săn có thể bị "cướp" mồi. Cần telemetry CT/phút theo loài từ alpha, và chỉnh `k_s` mỗi tuần.
3. **Cái chết ở C5 tốn 1.3 tuần** có thể khiến người chơi bỏ game sau một lần bị gank. Cần playtest giả thuyết "người chơi chết ở C5 có quay lại trong 72 giờ không ≥60%".
4. **Thiên Đạo Áp Chế** có thể làm người chơi lâu năm cảm thấy bị "nerf". Nên giữ nguyên kỹ năng và cosmetic, chỉ nén chỉ số, rồi kiểm chứng bằng khảo sát.
5. **Server vắng:** Khuẩn và Thần Cách (Tín Ngưỡng ≥10 người) phụ thuộc mật độ người chơi. Cần phương án NPC/AI thay thế ở server nhỏ và chế độ solo.
6. **Rewarded ads tăng tốc độ:** mức 15'/ngày sẽ cho +75 CT/tuần (+23% với Mid), quá lớn. Mức 5'/ngày cho khoảng +8%, nhưng vẫn là vùng xám về P2W. PX quyết; phương án an toàn nhất là ads chỉ cho cosmetic.

## 6. Câu hỏi mở
1. Chết khi độ Thiên Kiếp có nên giữ lại Thần Cách cho kiếp sau không (để lần thử thứ hai nhanh hơn)?
2. Mỗi mùa có reset server không? Nếu có, Thần vị và Phi Thăng nên gắn với mùa.
3. Đổi giữa Hóa Hình và Bản Thể có nên cần một kiếp phụ, hay chỉ cho đổi bằng luân hồi?
4. Co-op/party có chia CT hay mỗi người nhận đủ? (Tôi đề xuất mỗi người nhận 85% CT của hành động chung, cộng 10%/người tối đa 3 người, để khuyến khích đi nhóm mà không thành farm.)
5. Ở chế độ solo/offline có được tua nhanh (×1.5 CT) vì không có PvP không? Nếu có, cần chặn chuyển nhân vật từ solo lên server online.
