# R1 Proposal — SURV (phạm vi hẹp: S1–S4)

## 1. Cách tôi hiểu yêu cầu
Tôi đào sâu Linh Nghĩ trên nền v1.2 (không làm lại): phút chơi ở từng cảnh, luật Tổ/bầy, cái chết, và tương tác liên tộc. Mọi số mới đều đánh dấu **[đề xuất]**; số v1.2 giữ nguyên. Giả định: Tốc Hậu 5,0 ô/s (PROG xác nhận), Tha ×0,7 Tốc (v1.2).

**Mâu thuẫn v1.2 cần sửa:**
- (M1) §4.2 nói "Tha + Xung, 2 Lính ở C1", còn §6.2 nói "*Lập Sào* bắt đầu Tha". → **SURV-01** sửa: C1 Hậu tự Tha, C2 Lính mới Tha.
- (M2) §6.2 "*Thành Quần* có đủ bầy" nhưng §4.2 đã cho 3 Lính ở C2. → "đủ bầy" ở C3 = **Lính tự hành** (SURV-05), không phải thêm Lính.
- (M3) Hầm Ngầm là thẻ Chức Diệp, không phải kit gốc. → Nghĩ không đi Tồn vẫn phải có đường thoát (SURV-12).

## 2. Hook
**"Tổ là não, bầy là tay, Hậu là tim."** Mỗi chuyến đi là một câu hỏi: mang thêm 1 hạt hay về trước khi bầy bị cắt.

## 3. Đề xuất chi tiết

### SURV-01: Moment/Activity loop theo cảnh (S1)
| Cảnh (Mid) | Moment (giây) | Activity (phút) | Mục tiêu ngắn hạn | Áp lực chính · ai săn · khi nào |
|---|---|---|---|---|
| **C1 Ấu Nghĩ** (0–14') · Bìa · 2 Lính | Nhặt hạt/sâu, Xung sâu AI, né bóng Diều hâu | Chuyến 45–60s quanh Ổ trứng (≤15 ô): Hậu Tha 1 vật, ăn tại Ổ (No ×1,25) | No ≥60, gom 10 đơn vị vào Ổ, đột phá C2 | Diều hâu AI bổ xuống Lính lẻ (từ phút 4, 1 lần/3'); ếch AI ở mép nước ăn Lính; Gai cây AI AoE. Lính chết rẻ (6 No) → dạy Hy Sinh |
| **C2 Lập Sào** (14–50') · Bìa→Trung Lâm · 3 Lính | Ra lệnh Xung, chỉ vật cho Lính Tha, đọc bờ nước | Chọn chỗ **Tổ chính** (SURV-02), chuyến Tha 60–120s ra 15–25 ô, trữ trước Đông | Tổ có ≥25 đơn vị trước Đông đầu; chọn M2–M3 | Nha người chơi (Ấu Linh vẫn bật) mổ Lính; suối chia bầy; Đông đầu: thức ăn ngoài −40% **[đề xuất, nếu v1.0 chưa có]** |
| **C3 Thành Quần** (50–116') · Trung Lâm · 3 Lính (4 nếu Toan) | Mở Xác 6s trong khi Lính canh; gửi Lính tự Tha | Theo vệt chiến: tới xác → Mở → Tha thịt về Tổ/Hang Lang; tham gia hạ cây (Căn Thương) | Kinh tế xác (30% CT); qua Kiếp C3 | **PvP mở** (hết Ấu Linh): Lang săn Hậu, Nha bắt Lính tự hành, Mộc Gai AoE. Huyết Nguyệt. Trọng Thương bắt đầu |
| **C4 Nghĩ Đan** (116–218') · Thâm Lâm/Đầm Mục | Giữ ≥2 Lính đứng bến, Toan Dịch Nha đang bay, Đục Rễ Thăng | **Giữ bến** (SURV-06): xác Đầm tan 2'15", Mở → 45s → Tha cực ngắn; độ kiếp Viên Mãn ở Tổ | 1 bến trong ≥60% thời gian online; Viên Mãn | Cá Sấu AI đớp mép bến; Oa người chơi; Nha Bổ Nhào; Tán dày chặn Nha nhưng Đầm trống tán; 2 bến còn lại = đối thủ |

Tension graph: mỗi chuyến Tha là 1 đỉnh nhỏ (đi xa Tổ), mỗi lần về Tổ là 1 đáy. Mục tiêu: đáy <25 cứ mỗi 3–5'.

### SURV-02: Tổ chính (S2)
- **C1:** Ổ trứng ở Bìa = Tổ tạm (Nơi Trú, kho **20**). **C2 Lập Sào:** đặt **Tổ chính** 1 lần miễn phí (kho 40, reskin Hang v1.2).
- **Vị trí hợp lệ [đề xuất]:** ô cạn, ≥4 ô từ nước nông, ≥12 ô từ Hang/Tổ của người khác, không trong lãnh thổ rễ **đối địch** (trong rễ đồng minh = Khế ước, SURV-13). Ngoại lệ: **bến cạn Đầm Mục** hợp lệ dù sát nước.
- **Dời Tổ:** 1 lần/cảnh (C3, C4), kho mang theo 50%, phần còn lại rơi thành loot 30'. Lý do: tránh "Tổ du mục" nhưng cho phép tiến vào trong.
- **Bị phá:** Tổ chính **không phá được** (dùng luật Hang, 0 t-n). Kho theo trần tổn thất offline v1.2 (≤50%). Online: kẻ khác ăn trộm kho theo luật Hang v1.0, không thêm luật.
- **Kho:** hạt và vỏ không thối; thịt thối 15' (đã có). Ăn tại Tổ No ×1,25; Đông ở Tổ No ×0,5.

### SURV-03: Tổ Phụ (thẻ Chức Diệp)
- Đặt 15–30 ô từ Tổ chính; tối đa 1 (2 nếu PROG cho Hợp Đạo Mạch Tổ cộng).
- Chức năng: hồi sinh Lính (20s), điểm chui Hầm Ngầm/Mạch Tổ. **Không** kho, **không** Nơi Trú/Bế Quan (tránh 2 hang an toàn).
- **Phá được:** 3 đòn bất kỳ (hoặc 1 Gai AoE) → sập, dựng lại sau 3'. Rẻ để phá = đối thủ có lý do đi săn Tổ Phụ, tạo đỉnh căng ở C3–C4.

### SURV-04: Lính (S2)
| Luật | Số |
|---|---|
| HP / No | 12% HP Hậu; mỗi Lính thêm −1 No/90s lên Hậu (v1.2) |
| Dây (leash) **[đề xuất]** | Bám Hậu ≤8 ô. >8 ô trong 5s → **Đi lạc**: pip xám, Lính tự về Tổ gần nhất (không chết), tới nơi thì trở lại sẵn sàng |
| Nước nông | Lính không vào; đứng bờ chờ 15s, sau đó về Tổ. Hậu qua nông = bỏ bầy (đây là Trùng ⊣ Thủy ngược chiều: nước tách bầy) |
| Hồi sinh | Tổ 20s miễn phí · tại chỗ kênh 1s, −6 No (Hậu Mẫu: miễn khi No >70%) |
| Lính chết | Rơi xác nhỏ +2 No cho kẻ ăn, **0 CT, 0 Linh Hạch** (không farm Lính) |
| Ra lệnh ngoài tầm | Xung tầm 6 ô; lệnh ngoài 8 ô không nhận. Duy nhất ngoại lệ: Lính tự hành (SURV-05) |

### SURV-05: Tha (S2)
| Vật | Trọng lượng (đv kho) | Ai mang |
|---|---|---|
| Hạt, sâu | 1 | Hậu hoặc 1 Lính |
| Miếng thịt (từ xác Mở) | 2 | Hậu hoặc 1 Lính |
| Vỏ Thoát Xác | 2 | Hậu hoặc 1 Lính |
| Xác thú nhỏ nguyên con | 4 | Hậu + ≥2 Lính, Tốc ×0,6 |
| Linh Hạch | **không Tha** (ăn ngay; chống tích trữ CT) | — |
- Tốc: Hậu Tha ×0,7 (Vai Rộng −10%), Lính Tha ×0,8. Hậu mang 1 vật (Vai Rộng 2).
- **C2:** Lính Tha khi đi theo Hậu. **C3 "đủ bầy" [đề xuất]:** **Lính tự hành** — chỉ 1 vật, Lính tự mang về Tổ theo đường thẳng ≤30 ô, tối đa 2 Lính cùng lúc. Lính tự hành bị tấn công không có Hy Sinh (ngoài 6 ô). Đây là thao tác thêm của C3: đánh đổi tốc gom vs Lính lẻ làm mồi Nha.

### SURV-06: Giữ bến C4
- 3 bến cạn, mỗi bến ~6×6 ô. "Giữ" = Tổ (chính hoặc Phụ) đặt trên bến **hoặc** ≥2 Lính đứng bến ≥20s.
- Lợi ích: xác Đầm tan 2'15" → Mở Xác 45s → Tha ≤6 ô về Tổ; Trùng ⊣ Thủy (Thủy trong 6 ô không hồi HP, hiện trên Thần Thức).
- Áp lực: **Cá Sấu AI đớp mép bến** (reskin Báo, tấn công ô cạn sát nước 1 ô, 1 lần/90s, ưu tiên Lính); Oa kéo Lính trước Hậu; Nha Bổ Nhào trống tán.
- Kiếp Viên Mãn ở Tổ: Tổ trên bến = CT nhanh nhưng lộ; dời về Tổ cũ = an toàn nhưng mất 1 lượt dời. Lựa chọn có chủ ý.

### SURV-07: Thoát Xác (S2)
- Khi: mỗi lần đột phá cảnh thành công (C1→C2, C2→C3, C3→C4, Viên Mãn): hồi 100% HP, xóa debuff, miễn 1,5s (v1.2).
- Vỏ: tồn tại 60s **[đề xuất]**, Nghĩ Tha về Tổ = +10 No vào kho; kẻ khác ăn +8 No. Quạ AI tới sau 20s.
- Rủi ro: vỏ là mồi kéo kẻ ăn xác về chỗ vừa độ kiếp. Không thêm debuff "vỏ mềm" (giữ v1.2).
- Khuyến nghị cho onboarding: đột phá ở Tổ → vỏ rơi trong kho luôn.

### SURV-08: Mùa Đông với kiến
- Ở Tổ No ×0,5 (v1.2). Ngoài trời: Lính **không hồi sinh tại chỗ** trong Đông **[đề xuất]**, chỉ ở Tổ → bầy ra ngoài ít hơn.
- Vòng chơi Đông: trữ trước (Thu) → ở Tổ tu + chuyến ngắn ≤10 ô. Đây là "release" lớn của Nghĩ, khác Lang (Đông = đói nhất).
- Kiểm chứng: sim No Đông, kho 40 phải đủ 1 Đông mà vẫn phải ra ngoài ≥1 lần.

### SURV-09: Trọng Thương với Hậu + Lính (S3)
- Hậu Trọng Thương (C3+, đòn kết liễu do người chơi): Lính chuyển **Hộ Giá**, đánh kẻ trong 3 ô; mỗi Lính trúng kẻ đang Kết Liễu làm kênh **+0,5s (trần +1,5s → 3s)**. Không ngắt hẳn, không tự cứu.
- Hy Sinh không hồi khi Trọng Thương. Lính không cứu được Hậu (giữ "đồng minh cứu" cho người chơi).

### SURV-10: Mất Lính vs mất Hậu
- Mất Lính = −6 No hoặc 20s về Tổ: lỗi nhỏ, đọc được, chơi thường xuyên.
- Mất Hậu = hết đời (Lính tan theo). Lính đang ngoài trời rơi xác nhỏ; kho Tổ thành loot 30'.
- Cost of death ở C3 ≈ 50–116' chơi; vì vậy Nghĩ cần đường thoát rõ (SURV-12).

### SURV-11: Hazard mục tiêu Nghĩ (tách nguồn)
| Cảnh | Tổng (v1.2) | Nguồn chính được phép | Tín hiệu cần nerf |
|---|---|---|---|
| C1–C2 | ≤0,15/h | AI (Diều hâu, ếch) ≥70% | Đói >0,05/h → kéo dài warning |
| C3 | ≤0,10/h | PvP ≤0,06 | Chết do Nha >30% → siết Bổ Nhào lên Hậu |
| C4 | ≤0,08/h | Cá Sấu + PvP bến | Cá Sấu >0,03/h → tăng CD đớp bờ |

### SURV-12: Đường thoát
- **Kit gốc (mọi nhánh):** Lính chắn (Lính đứng giữa Hậu và kẻ địch nhận đòn cận chiến đầu tiên) + Hy Sinh + Tổ gần. Toan Dịch chậm 20% để kéo khoảng cách.
- **Hầm Ngầm (Chức Diệp):** chui 2s, không bị chọn mục tiêu, trồi ≤6 ô theo hướng joystick **[đề xuất]**; không chui qua nước. **Lính bị bỏ lại → Đi lạc về Tổ.** Thoát = trả giá bầy.
- Mạch Tổ (Hợp Đạo): nhảy về Tổ/Tổ Phụ ≤20 ô, kênh 2s (ngắt được) — chỉ là đường về, không phải nút bất tử.

### SURV-13: Tương tác liên tộc (S4)
| Cặp | Tình huống thực chơi |
|---|---|
| **Khế ước Kiến (Mộc)** | Nghĩ đặt Tổ trong lãnh thổ rễ cây đồng minh (chiếm 1 trong 2 slot của cây): Gai/Độc cây **không trúng Lính của Nghĩ đó**; Nghĩ ăn mật Quả Ước; Lính đuổi bầy sâu AI trên Tán. Cây có bảo vệ, Nghĩ có tổ an toàn khỏi khắc. |
| **Mở Xác cho Lang** | Lang hạ Hươu, Nghĩ Mở 6s (Lang canh), Lang ăn không Trúng Độc; Nghĩ Tha 2 miếng vào Hang Lang (thối 15'). Ngược lại: Lang solo có thể ăn Hậu (+10 No) — lý do Nghĩ luôn giữ Lính chắn. |
| **Trùng ⊣ Thủy giữ bờ** | 2 Lính đứng bờ suối: Oa không hồi HP trong 6 ô và hiện trên Thần Thức Hậu → Oa phải lặn Đáy (CT ×0,3) hoặc đổi ao. Oa phản đòn: Quăng Lưỡi bắt Lính trước. |
| **Nha Bổ Nhào** | Nha bổ vào cụm Lính tự hành (Lính lẻ = mồi). Phản ứng: Toan Dịch trúng Nha đang bay; Bổ Nhào hạ cánh = cửa sổ 0,4s để Xung. Ở bến C4 trống tán, Nha là mối đe dọa số 1 với Lính. |
| **Căn Thương** | Lang phá Thân → Mộc Tàn → Nghĩ đào 50s. Nghĩ không có Lang thì không giết được cây cùng cảnh (giữ v1.2). |

## 4. Kết nối với các domain khác
- **PX:** nút Tha (ngữ cảnh trên nút Đánh/ăn?), cử chỉ chỉ vật cho Lính, lệnh Lính tự hành, đặt/dời Tổ — tất cả trong ≤5 nút. Pip Lính cần trạng thái "Đi lạc"/"tự hành". Chi phí t-n: Lính tự hành, Cá Sấu đớp bờ, Tổ Phụ phá được.
- **PROG:** Tốc Hậu, CT mỗi đơn vị Tha, giá trị vỏ, kho 20/40 có đủ cho Đông; Lính chắn có vượt +10% ehp không.
- **WORLD:** tên Tổ tạm/Tổ Phụ/bến, câu Trung Ấm "Lính đi lạc".

## 5. Rủi ro tự nhận diện
- Lính tự hành có thể quá vi mô trên mobile → fallback: bỏ, C3 "đủ bầy" = Lính Tha 2 vật.
- Leash 8 ô + Đi lạc có thể gây cảm giác "mất bầy vô lý" → playtest: % Lính đi lạc ngoài ý muốn ≤10%.
- Giữ bến có thể bị 1 Nghĩ chiếm cả phiên → luật: Tổ chiếm bến, đối thủ phá được Tổ Phụ.

## 6. Câu hỏi mở
1. Ăn trộm kho Tổ online theo luật Hang v1.0 có đúng không, hay Tổ cần luật riêng?
2. Đông v1.0 đã giảm thức ăn ngoài chưa? Nếu có, bỏ số −40% của tôi.
3. Lính có tính là "đồng minh" trong Hy Sinh/Đường Mùi ở party không?
