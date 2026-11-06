# R2 Critique — PX

## Về PROG
### Giữ lại
- PROG-03 (giới hạn hồi Lính 1/8s trong giao tranh): vá exploit đổi No lấy HP vô hạn. PROG-06 (Lính Thứ Tư ×1,52): đúng.
- PROG-04 (sửa tỉ trọng CT thành 60/25/15): vì Căn Thương hiếm nên người chơi solo không được thiếu CT.
### Mượn
- PROG-02 Sai Lính gộp với SURV-05 Lính tự hành thành **một hệ**. Input: khi đang Tha, **giữ Tương Tác = Giao** cho Lính, chạm = Thả. Không thêm nút.
### Phản biện
| ID | Mức | Vấn đề | Tình huống | Thay thế / kiểm chứng |
|---|---|---|---|---|
| PROG-01 | Major | Sào Bến, SURV-02 Dời Tổ và SURV-06 Giữ bến làm cùng một việc là "có tổ ở bến". Thành ra 3 luật cho 1 mục tiêu | Ở phút 142, người chơi phải phân biệt Tổ, Tổ Phụ và Sào Bến | Cắt Sào Bến. Mốc C4 Trung thay bằng **Dời Tổ lên bến** (SURV) cộng **Đại Gò** (WORLD-05). Không tốn thêm t-n |
| PROG-01 | Major | Gác Tổ cần thêm thao tác chọn Lính ở lại và thêm cảnh báo trên HUD | Trên mobile không có chỗ để giao việc cho Lính | Cắt (PROG cũng xếp nó đầu danh sách cắt) |
| PROG-01 | Minor | Dùng việc bỏ "Ăn tại Tổ No ×1,25" để bù chi phí: chỉ số này gần như không tốn chi phí, nhưng lại là lý do để về Tổ | Beat 8:30 của PX-04 dựa vào nó | Giữ ×1,25 |
| PROG-05 | Minor | Đề xuất Hầm Ngầm = "giữ Tha khi tay không" đụng với thao tác giữ 2s để đặt Tổ Phụ | Người chơi muốn chui hầm thì lại cắm Tổ Phụ | Dùng **vuốt né** (PX-01) |
### Câu hỏi
Khi Sai Lính chỉ còn 1 Lính ở C2 thì CT/phút C2 giảm bao nhiêu?

## Về SURV
### Giữ lại
- SURV-02/05: Linh Hạch không Tha được, kho có trần, thịt thối 15'. Sink sạch, chống tích trữ.
- SURV-10/12: mất Lính là lỗi nhỏ, ai cũng có đường thoát từ kit gốc.
### Mượn
- SURV-06 "≥2 Lính đứng bến ≥20s" thành use-case chính của lệnh **Giữ** (PX-02), kiểm bằng HNg-5.
### Phản biện
| ID | Mức | Vấn đề | Tình huống | Thay thế / kiểm chứng |
|---|---|---|---|---|
| SURV-04/05 | Major | Pip có 6 trạng thái (sống, chết, tách, Giữ, Đi lạc, tự hành). Không đọc được trong 2s | Đang giao tranh, người chơi không biết còn mấy Lính đỡ đòn | Gộp Đi lạc vào tách (viền cam), tự hành dùng 1 overlay mũi tên. Còn 4 hình + 1 overlay. Kiểm bằng HNg-4 |
| SURV-05 | Major | Lính tự hành mở ở C3 Sơ chồng lên điểm nóng P1 (A1, Căn Thương, PvP, Trọng Thương cùng lúc) | Phút 50, người chơi có 5 luật mới trong vòng 1' | Theo nhịp PROG: 1 Lính ở C2 Trung, 2 Lính ở C3 Trung |
| SURV-06 | Minor | Cá Sấu AI (0,05) là enemy mới | — | Won't trong MVP. Ếch AI và Oa người chơi đã đủ áp lực ở bến |

## Về WORLD
### Giữ lại
- WORLD-02 Gò Bỏ ×3: dạy chọn chỗ đặt tổ mà không cần chữ. WORLD-05: Lính đặt tên Một/Hai/Ba, chỉ tốn data, cho Hy Sinh thêm sức nặng cảm xúc.
### Mượn
- 3 bậc gò dùng làm **mốc thăng tiến nhìn thấy được** để lấp dry spell C4 (Đại Gò ≈142').
### Phản biện
| ID | Mức | Vấn đề | Tình huống | Thay thế / kiểm chứng |
|---|---|---|---|---|
| WORLD-03 | Major | Bỏ Cột Linh Quang, chỉ dùng mùi. Người đã quen chơi Lang sẽ mất phương hướng | Phút 20, không tìm được đường vào Trung Lâm | Giữ Cột, mùi là lớp thêm. Đo: ≥70% vào Trung Lâm trước phút 25 |
| WORLD-01/03 | Minor | Kiến AI theo đường mùi (~0,05) tốn hiệu năng trên mobile và gây nhiễu PvP | — | Could, chỉ làm sau cổng |
| WORLD-01 | Minor | Ghi "C3 đủ 3 Lính" nhưng 3 Lính đã có từ C2 | — | Đổi thành "bầy tự đi" (Lính tự hành) |

## Trả lời bắt buộc
**(1) Tải điều khiển.** Không hệ nào cần nút thứ 6: Giao gắn vào giữ Tương Tác, Dời Tổ đi qua menu Nơi Trú. Đỉnh giao tranh C4 vẫn ≤45 thao tác/phút, vì người chơi không Sai Lính khi đang đánh (Sai Lính cộng +2–4 thao tác/phút lúc đi gom). Rủi ro thật nằm ở **tải nhận thức**, không ở tải ngón tay. **Giữ:** Tha Bầy, Sai Lính gộp, leash/Đi lạc, Dời Tổ, Hộ Giá (bị động). **Cắt:** Gác Tổ, Sào Bến. **Hoãn:** Tích Sào (Should), Cá Sấu (Won't).

**(2) Chi phí.** Giữ hết thì: nền 1,48 + PX 0,15 + PROG 0,27 + SURV ~0,22 + WORLD ~0,19 ≈ **2,31 t-n, vượt cổng 36%**. Đây là **Blocker scope**. Gói Must đề xuất:
| Hạng mục | t-n |
|---|---|
| Nền + PX net | 1,63 |
| PX-04 rút từ 6 xuống 4 beat (beat Nha dùng Diều hâu của SURV) | −0,03 |
| Tha Bầy (Lính mang vật khi đang Theo) | +0,05 |
| Tổ chính C2 (reskin Hang) | +0,03 |
| 3 bậc gò | +0,03 |
| **Tổng** | **1,71** |
Gói này **sát cổng, không có đệm**. Fallback nếu tuần 24 đo >1,70: Tổ Phụ đặt ở vị trí cố định (−0,02). Sai Lính tự hành (0,10) là hạng mục đầu tiên làm sau cổng. Tạm thời thay bằng bản "lite": Lính chỉ Tha khi đang Theo.

**(3) Lang mạnh gấp đôi.** Ở bãi trống Nghĩ thua 0%, Lang giết trong 4–6s. Ở C3, chết là mất 50–116' chơi. Người chơi sẽ thấy đó là phạt bất công, không phải thất bại vì kỹ năng. Kéo theo: bỏ game sau đời đầu tiên ở C3 và pick rate dồn hết về Lang. Lập trường: **cái lệch là Lang, không phải Nghĩ**. Không buff Nghĩ, **giảm Lang 10–15%**. Nâng KPI thoát lên **≥6s** (4s quá chặt với phản xạ trên mobile, và Hầm Ngầm chỉ nhánh Tồn có). Kit gốc phải tự mua được ≥1,5s. Thêm **HNg-6:** chết vì Lang ≤35% số ca chết của Nghĩ ở C3+, pick rate Lang ≤35% ở Alpha, tỉ lệ bỏ game sau một đời chết vì Lang không cao hơn mức trung bình quá 10 điểm.

**(4) Tha C1/C2.** Đồng thuận 4/4: C1 Hậu Tha 1 vật, C2 Tha Bầy. Tha là động từ của hint đầu đời nên phải xuất hiện trước phút 5. Phản đối PROG mở Lính 1 → 2 ở phút 3,7: beat Hy Sinh ở 6:30 sẽ để Hậu không còn Lính nào, và chất "bầy" mất ngay từ đầu. Lai: **bắt đầu với 1 Lính, Lính thứ 2 nở đúng lúc thắng đầu (≤90s)**. Người chơi học được "ăn thì bầy lớn", tải lúc đầu vẫn nhẹ, chi phí 0.

## Xung đột liên domain
| Xung đột | ID | Lập trường | Gợi ý |
|---|---|---|---|
| Input Hầm Ngầm | PROG-05 / PX-01 | Vuốt né | Chốt PX-01 |
| Có tổ ở bến | PROG-01 Sào Bến / SURV-02 Dời Tổ / SURV-06 Giữ bến | Chỉ giữ Dời Tổ | Cắt Sào Bến |
| Số Lính ở C1 | PROG-01 / SURV-01 / PX-04 | 1, lên 2 khi thắng đầu | Lai như mục (4) |
| No ×1,25 tại Tổ | PROG-01 / SURV-02 | Giữ | Giữ |

## Top 3 phải chốt
1. Gói Must ≤1,70 t-n và danh sách hoãn.
2. Giảm Lang 10–15% cùng KPI thoát ≥6s (cần sim duel toàn cục).
3. Sai Lính gộp với Lính tự hành: bản lite trong MVP, bản đầy đủ làm sau cổng.
