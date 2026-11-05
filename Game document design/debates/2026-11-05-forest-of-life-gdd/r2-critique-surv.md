# R2 Critique — SURV

> Lăng kính: *"Người chơi đang sợ mất điều gì lúc này, và họ có đủ công cụ để chống lại không?"* Đơn vị tu vi dùng **CT của PROG** (Mid = 5×40'/tuần ≈ 64 CT/phiên, 320 CT/tuần).
> Tự cập nhật trước (chống bảo thủ): tôi **chấp nhận** 1 ngày-rừng = 24' (WORLD-08) thay cho 20' của tôi; Nghiệp giảm theo **giờ chơi online** (PROG-12) thay cho theo ngày thực; tu vi offline đi qua **hồ Tĩnh Tu** (PROG-04) thay vì cộng thẳng; Khô Linh (WORLD-03) thay cho mật độ linh khí tĩnh của SURV-08.

---

## Về PROG

### Giữ lại (Keep)
- **PROG-03 (CT chuẩn hóa + phương sai là bản sắc loài):** đúng cách cân bằng cây (ổn định) với thú săn (được ăn cả, ngã về không). Tôi dùng CT làm đơn vị chung cho Sinh Năng (xem xung đột X7).
- **PROG-11 (Tốc không tăng theo cảnh giới, Thần Thức chỉ +5%/cảnh):** đây là công cụ sinh tồn mạnh nhất cho con mồi. Kẻ mạnh không đuổi kịp, không nhìn xa hơn, nên "trốn" vẫn là một lựa chọn thật.
- **PROG-07 (Đánh úp kiếp):** kẻ độ kiếp bị kẹt trong vòng và chỉ còn 50% sát thương ra ngoài. Đây là đỉnh tension có hẹn trước, khớp SURV-16.
- **PROG-09 (Nguyên Thần Bất Diệt):** về bản chất là một **neo hồi sinh** cho C6. Tôi tổng quát hóa nó cho mọi cảnh giới (X5).

### Mượn (Steal)
- **PROG-04 Tĩnh Tu:** làm kênh duy nhất cho phần thưởng tu vi offline (X3).
- **PROG-12 luật 1 (Áp Chế n=9 ở Rừng Non):** thay cho "Thiên Đạo Áp Chế trần R3" của SURV-11. Hai cách cùng ý, nhưng con số của PROG đã được simulate.
- **PROG-12 luật 3 (`m = 0.25^g`, cùng một cặp 1 lần/30'):** dùng làm hệ số nhân cho Sổ Năng Lượng của SURV-09.

### Phản biện (Challenge)
| ID | Mức độ | Vấn đề | Tình huống người chơi | Đề xuất thay thế / cách kiểm chứng |
|---|---|---|---|---|
| PROG-11 | **Blocker** | TTK 4–6s áp lên **cây**. Ví dụ của chính PROG: Huyết Lang C4 hạ Thiết Mộc C4 (519 HP) trong 4 đòn. Cây không chạy được nên TTK 5s nghĩa là cây chết trước khi kịp bấm phòng thủ. | Người chơi cây trên mobile đang tap Vệt Nắng thì một sói cùng cấp đi ngang, 5 giây sau cây chết và mất cả kiếp. Họ gỡ game. | Áp **HP 3 lớp** của SURV-03 lên ngân sách PB của PROG: `HP(n)` của PROG là HP lớp **Thân**. Tán = +30% Thân. **Tâm Rễ** = 50% Thân, đòn thường không chạm tới được, chỉ hạn, lửa lớn, nấm mục, nhánh Đào, rễ đối thủ hoặc kiếp mới đánh vào được (khớp "Đạo Căn ≥3 phút" của PX-03). Quy tắc ngân sách: **Tốc = 0 được quy đổi thành ×3 HP Thân**. Mục tiêu sim: 1 kẻ tấn công cùng cấp mất ≥40s mới làm cây **Đổ**, và Tâm Rễ = 0 trừ khi có nguồn đặc biệt. |
| PROG-10 | **Major** | Chỉ có một đường chết: luân hồi toàn phần. Không có lựa chọn "hậu duệ cùng loài tại neo". Kết quả là chết ở C5 tốn 1.3 tuần, và trong PvP tự do điều đó có thể xảy ra **vì một lần bị gank**. PROG cũng tự nêu rủi ro này. | Mid chơi C5 Hóa Hình bị 3 sói C4 đánh úp lúc đang Bế Quan ở bìa vùng. Mất 6.5 phiên. Xác suất người đó quay lại trong 72h thấp. | Thêm **Đầu Thai Hậu Duệ** (SURV-15) làm tầng chết thứ nhất (xem X5). Với luân hồi toàn phần, nâng catch-up từ ×3 lên ×4 cho C5+, như PROG đã gợi ý, để C5 còn khoảng 1 tuần. |
| PROG-10 / PROG-12 | **Major** | Phần thưởng giết và giá trị xác lệch nhau. Kill cùng cấp cho kẻ giết **8 CT**, nhưng xác cho thực vật/nấm **20% CT tầng cuối**, tức **36 CT** ở C5. Nấm đứng cạnh kiếm gấp 4.5 lần kẻ săn. | Một bầy sói hạ hổ C5. Một người chơi nấm ngồi chờ sẵn hút 36 CT. Kẻ săn tự hỏi đi săn để làm gì. | Đưa cả hai về **một pool Sinh Năng** = 20 CT × `m`, chia 40/20/40 theo SURV-09: kẻ ăn 8 CT (đúng số của PROG), Linh Hạch 4 CT cho ai nhặt trước, đất 8 CT chia cho rễ/nấm trong 3 ô. Phần đất cũng chính là phần trả về quỹ vùng của WORLD-03. |
| PROG-03 | Minor | Quang hợp là 60% nguồn tu của cây và chạy thụ động khi online, chỉ cần không AFK 3'. Cây sẽ thành "chạm màn hình mỗi 3 phút". | Người chơi cây online nhưng chỉ chạm màn hình mỗi 2'50" để giữ ×1.0. | Cho CT quang hợp đi qua Quang Tinh thu được, tức là phụ thuộc Vệt Nắng (SURV-07): cây AFK chỉ còn khoảng 60% thu nhập ban ngày. Đo tỉ lệ "thời gian không có hành động có nghĩa" của cây, mục tiêu <25%. |

**Trả lời câu hỏi của PROG (needs → CT):** Comfort ×1.0 · Warning ×0.85 · Critical ×0.5 · 0 (Lethal) ×0. Sàn xác NPC cho Khuẩn: Director (SURV-13) bảo đảm ≥1 xác NPC/5' mỗi vùng thông qua kẻ săn AI hạ con mồi AI. Thú Triều là "bữa tiệc xác".

### Câu hỏi cho PROG
1. Đầu Thai Hậu Duệ có giữ Huyết Mạch và điểm Đạo Đồ không? Tôi đề xuất giữ, và chỉ mất CT.
2. Với thực vật Nhân Hình (PROG-08), "Bản Thể bị hạ thì chết" nghĩa là Thân = 0 hay Tâm Rễ = 0? Tôi đề xuất Tâm Rễ.
3. Chạy được sim TTK với HP 3 lớp và quy đổi "Tốc 0 → ×3 Thân" không?

---

## Về WORLD

### Giữ lại (Keep)
- **WORLD-02/03 (linh khí bảo toàn, Khô Linh):** biến "đừng tham" thành hậu quả sinh thái. Đúng triết lý "môi trường là đối thủ chính".
- **WORLD-08 lớp 2 (diễn thế theo tile/chunk):** khớp Tro Màu và Mộc Mộ của SURV-14/15. Chu kỳ phá hủy rồi tái sinh nhìn thấy được trên bản đồ.
- **WORLD-14d Quả Ước:** trùng với "quả mời" của SURV-10. Hai người đi tới cùng một ý độc lập, nên đây là tín hiệu mạnh.
- **WORLD-11 Nghiệp Duyên:** mở khóa loài bằng chính chuỗi thức ăn. Bị ăn cũng là tiến bộ.

### Mượn (Steal)
- **WORLD-10 E5 Tu Sĩ Nhập Sơn:** một mối đe dọa **chống snowball** (nhắm vào mục tiêu cảnh giới cao nhất) mà không cần luật PvP. Tôi đưa vào Director như archetype thứ 7, chỉ dùng sprite bóng dáng.
- **WORLD-14i Ký Hồn Mộc:** thành một **loại neo** cho Đầu Thai Hậu Duệ, dùng được cho đồng đội co-op.
- **WORLD-13 trục Sinh↔Sát**, kèm sửa đổi **"Thực Sát / Lạm Sát"** (SURV-20, mới): giết rồi ăn ≥50% phần của kẻ ăn trong 60s thì tính Sát ×0.3. Giết mà không ăn thì ×1.0. Nhờ vậy thú ăn thịt không bị phạt kép chỉ vì sống đúng bản năng (giải quyết rủi ro #3 của WORLD), và needs gắn với đạo tâm.

### Phản biện (Challenge)
| ID | Mức độ | Vấn đề | Tình huống người chơi | Đề xuất thay thế / cách kiểm chứng |
|---|---|---|---|---|
| WORLD-03 | **Major** | Quỹ vùng cạn theo **mật độ dân**. Bìa Rừng là nơi người mới tụ đông nhất, nên sẽ Khô Linh thường trực. Tức là trải nghiệm tệ nhất rơi đúng vào người yếu nhất. | Server 40 người, 25 người mới spawn ở Bìa Rừng, sau 2 ngày-rừng vùng xám màu và tu vi −50% cho đúng nhóm cần tu nhanh nhất. | Bìa Rừng có **sàn quỹ 50%** ("Thiên Đạo hộ mầm"). Khô Linh chỉ xảy ra từ Trung Lâm trở vào. Hệ số hồi quỹ tỉ lệ với số cây/nấm sống trong vùng. Kiểm chứng: sim agent 40 người × 7 ngày, đo % thời gian Bìa Rừng có tu vi < ×0.8, mục tiêu <10%. |
| WORLD-10 E2 | **Major** | Huyết Nguyệt mỗi tuần, cổ thú đi ra **vòng ngoài**, cộng với con mồi rơi ×2 linh khí. Kết quả là một **đêm thảm sát người mới** cố định mỗi tuần, đi ngược mọi luật chống bắt nạt. | Người mới vào game đúng tối thứ 7, chết 3 lần trong 8' vì cổ thú AI. D1 sụp. | Cổ thú chỉ ra tới **Trung Lâm**. Bìa Rừng chỉ có kẻ săn AI +50%. Thưởng ×2 chỉ áp dụng khi giết con mồi cùng cấp hoặc cao hơn. Người có Linh Quang Hộ Thể được cảnh báo trước 1 ngày-rừng. |
| WORLD-14f Mộc Độn | **Major** | Fast-travel qua mạng rễ xóa áp lực "khoảng cách tới Hang". Đó là trục căng chính của thú (SURV-13 tính Áp Lực theo khoảng cách) và là pha "rút về lúc hoàng hôn". | Bầy 3 sói đi săn sâu, trọng thương thì độn về cây đồng đội trong 1 giây. Không bao giờ có chuyến về nhà nguy hiểm. | Chỉ độn giữa các ô **thuộc mạng rễ** của cây (12–48 ô, không xuyên bản đồ). Không độn được khi bị gây sát thương trong 10s gần nhất. CD 3'. Tốn 15 Quang Tinh của cây mỗi lượt, nên cây phải trả giá. |
| WORLD-12 (9 cảnh) | Major | Mỗi đại cảnh giới phải mở ra **một khả năng mới về chất** (luật tech tree), không chỉ +stat. 9 cảnh = 9 khả năng mới × 5 loài. Riêng cảnh 7–8 (Phản Hư/Hợp Đạo) hiện chưa có khả năng gameplay nào gắn vào. | Người chơi lên cảnh 8 và không có gì mới ngoài số. Đó là một dry spell nhiều tuần. | Dùng 7 của PROG. Giữ logic "mỗi cấp rừng có 1 độ kiếp phi thăng" của WORLD bằng cách ánh xạ lại (X1). |
| WORLD-16 | Minor | Thiên Phạt "sét đuổi 1 ngày-rừng" trùng với 3 hệ khác. Ngoài ra không nói rõ có offline để né được không. | Kẻ mang nghiệp thoát game khi mây kiếp tới. | Hợp nhất (X4). Đồng hồ Thiên Phạt **dừng khi offline** và Nghiệp không giảm khi offline. |

### Câu hỏi cho WORLD
1. Server ≤30–40 người có cần 9 Thần Vị không? Tôi đề xuất số Thần Vị = max(3, dân số/15).
2. Tôi có thể giữ quyền sở hữu con số Khô Linh (ngưỡng, hồi phục) và WORLD sở hữu lore cùng hiển thị không?
3. Phi thăng thì cây **bỏ lại** lãnh thổ rễ. Có để lại Mộc Mộ (landmark) ở rừng cũ không? Tôi đề xuất có.

---

## Về PX

### Giữ lại (Keep)
- **PX-03 M1 + "Đạo Căn ≥3 phút":** độc lập trùng với Tâm Rễ của tôi.
- **PX-05.4 (combat power ~1.6–1.8×/cảnh):** khớp ×1.77 của PROG.
- **PX-12 luật 1 (skin không đổi silhouette, không ngụy trang):** sống còn trong một game săn mồi.
- **PX-16 Thiên Đạo cân bằng loài:** giải đúng rủi ro #5 của tôi. Tôi bổ sung: Director bù **AI con mồi** khi tỉ lệ thú ăn thịt vượt 35%.

### Mượn (Steal)
- **PX-05 "Oán Linh" (nạn nhân bị lấn yếu nhận +50% Đạo Tâm):** đây là comeback mechanic, đưa vào X4.
- **PX-04 "Thiên Thư báo mộng":** gộp với Nhật Ký Rễ của tôi thành một màn tóm tắt.
- **PX-04 thời gian nhập định 60s:** dùng cho trường hợp thoát game **khi đang combat** (X3).

### Phản biện (Challenge)
| ID | Mức độ | Vấn đề | Tình huống người chơi | Đề xuất thay thế / cách kiểm chứng |
|---|---|---|---|---|
| PX-04 | **Blocker** | Tu luyện offline 60% với trần 8h nghĩa là 8×60×0.6 = **288 CT/đêm**, trong khi Mid **chơi cả tuần** chỉ được 320 CT. Một đêm ngủ gần bằng một tuần chơi. Game thành idle, và đường cong nhiều tuần của PROG vỡ. | Người chơi cây log in 2', log out, lặp mỗi ngày, rồi đạt C5 nhanh hơn người chơi sói săn thật. | Tách 2 kênh. (1) **Tu vi:** chỉ đi qua hồ Tĩnh Tu của PROG (×2 cho 30' phiên sau, tương đương +30 CT/ngày). (2) **Thân xác/lãnh thổ:** cây đặt sẵn **Kế Hoạch Sinh Trưởng** trước khi thoát (tối đa 3 ô rễ, mọc lại Tán, quả chín), trả bằng Quang Tinh tích trữ, thực hiện khi offline. Như vậy P1 vẫn "tối về thấy rễ lan 3 ô" mà CT không lạm phát. |
| PX-04 | Major | Tự vệ thụ động **cho EXP khi offline** mở đường farm bằng tài khoản phụ. Ngoài ra trần "25% lãnh thổ **mỗi lần** offline" sẽ cộng dồn nếu đăng nhập/thoát liên tục. | Bạn chơi sói AFK cắn gai cây tôi suốt đêm để nuôi tu vi cho tôi. | Sát thương gây ra khi offline chỉ cho **Dưỡng Chất** (vật liệu), không cho CT. Trần tổn thất tính **theo 24h thực**, không theo lần offline (X3). |
| PX-05.1–2 | Major | (a) Linh Quang Hộ Thể "45' đầu" có tính cả FTUE 20' chạy offline, nên trong Rừng chung chỉ còn khoảng 25'. (b) Chênh +1 cảnh đã bị +1 Nghiệp, nghĩa là **phạt chính chuỗi thức ăn**: sói C3 ăn hươu C2 là bản năng, không phải bắt nạt. | Sói C3 bị đánh dấu Nghiệp chỉ vì đi săn đúng cách. Hệ sinh thái ăn thịt chết dần. | Khiên tính **60' trong Rừng chung** hoặc tới C2. Chênh 1 cảnh **không sinh Nghiệp** (PROG đúng ở điểm này) (X4). |
| PX-08 | Major | FTUE ép chết bằng sói scripted ở phút 11–14. Người chơi cảm thấy chết **vô lý**, đi ngược nguyên tắc "chết phải hiểu vì sao". Lần chết đầu cũng là lúc dạy họ rằng PvE bất công. | Người chơi giỏi né mãi, cuối cùng bị script giết. Họ thấy bị lừa. | **Thọ Nguyên:** Linh Thử là loài đời ngắn, có thanh tuổi thọ 12' hiện rõ trên màn hình. Phút 11 cho người chơi chọn cách kết thúc: dụ sói ra xa ổ để cứu bầy (nhận Đạo Tâm ×1.5) hoặc chết già dưới gốc cây (nhận Linh Thổ). Cái chết vẫn chắc chắn xảy ra, nhưng là **lựa chọn đọc được**. Giảm chi phí: dùng Ấu Lộc thay Linh Thử để không thêm 1 loài art. |
| PX-09 | Major | Reset kỷ nguyên 14/28 ngày làm "thành thần" bất khả với gần như mọi người. Theo bảng PROG-04, Mid tới C7 ở 6.5 tuần, Core 3.7 tuần (26 ngày). Với kỷ nguyên 28 ngày, **chỉ Core 7×60' mới thành thần**. Với 14 ngày, không ai thành thần. | Mid chơi 4 tuần, vừa chạm C6 thì bị reset. Đích đến của game không bao giờ tới được. | Tách **reset bản đồ** khỏi **reset nhân vật** (X2). |
| PX-15 | Minor | Linh Khí Triều chốt cứng 12h và 20h là FOMO giờ giấc với P1, và chồng lên Linh Triều của SURV-17 và WORLD-10. | Người chơi ở múi giờ khác không bao giờ có Triều. | Gộp chung một lịch (X8). Linh Triều nhỏ trôi theo chu kỳ mùa 42h, nên giờ diễn ra đổi mỗi ngày. |

### Câu hỏi cho PX
1. Khi reset bản đồ, nhân vật có được giữ không? Tôi đề xuất giữ, xem X2.
2. Linh Thử có là loài chơi được sau FTUE không? Nếu có thì MVP thành 4 loài.
3. Một thú bị đánh thức giữa đồng (mất mạng mobile), 30s có đủ công bằng không?

---

## Xung đột liên domain phát hiện được

| # | Xung đột | Các ID liên quan | Lập trường của tôi | Gợi ý giải quyết |
|---|---|---|---|---|
| X1 | **Số cảnh giới 7 vs 9** | PROG-01, WORLD-12, WORLD-04, SURV-08 | **7.** Lý do: 7 dải trần/upkeep linh khí là đủ, mỗi cảnh có một khả năng mới (C2 Linh Thức, C3 Huyết Mạch, C4 Đạo Đồ, C5 Hóa Hình, C6 Xuất Khiếu, C7 Thần), và đã có simulate. | Ánh xạ 3 cấp rừng: **Rừng Non C1–C2 · Nguyên Sinh C3–C4 · Cổ Đại C5–C6 · Thần C7**. Phi thăng gắn vào kiếp C2→C3 và C4→C5. Hóa Hình rồi bước vào Thần Lâm rất hợp lore. WORLD gộp tên cảnh 7–8 thành tên C6/C7. Upkeep SURV-08: C1–2 L0, C3–4 L1, C5–6 L2, C7 L3. |
| X2 | **Độ dài mùa / reset** | WORLD-08 (~7 tuần), PX-09 (14/28 ngày), PROG-04 (Mid 6.5 tuần, có chết 6–9 tuần) | Tách 2 loại reset. **Đổi 1 mùa = 42h**, nên 1 năm-rừng = **đúng 1 tuần thực** và giờ diễn ra mùa trôi qua mọi múi giờ. | **Kỷ Nguyên (map reset)** = 4 năm = **28 ngày**, khớp pass PX: địa hình, diễn thế, Khô Linh và lãnh thổ reset. Nhân vật **giữ** cảnh giới, cây giữ Tâm Rễ và chọn lại ô gốc trong cùng vòng. Rừng Non có thể 14 ngày. **Đại Kiếp (character reset)** = 2 Kỷ Nguyên = **8 tuần**, mọi người luân hồi, Đạo Tâm tỉ lệ với cảnh giới đạt được. 8 tuần ≥ 6.5 tuần của Mid cộng 1–2 lần chết. Người vào muộn có Thiên Đạo Bù Đắp (PROG) và Đạo Tâm khi Đại Kiếp. |
| X3 | **Offline** | PX-04, PROG-04, SURV-12 | Thân không bao giờ chết khi offline hợp lệ. **Tu vi offline chỉ qua hồ Tĩnh Tu.** | **Luật Bế Quan hợp nhất:** (1) Thoát trong lãnh thổ hoặc Hang thì thân bất tử ngay. Thoát ngoài: 30s nếu không combat, **60s** nếu gây hoặc nhận sát thương trong 30s gần nhất. (2) Trần tổn thất **mỗi 24h thực**: ≤20% Tán và ≤25% ô rễ **ngoài** (không tính các ô trong bán kính 2 quanh Tâm Rễ). Kho Hang có thể bị cướp tối đa 50%. (3) Tự vệ thụ động vẫn chạy, nhưng chỉ cho Dưỡng Chất. (4) Quang hợp offline 25% vào **Quang Tinh** (vật liệu, trần kho 150), không vào CT. (5) Kế Hoạch Sinh Trưởng. (6) Ô rễ của cây offline >48h teo 1 ô/ngày để chống giữ đất ảo. (7) Báo mộng. |
| X4 | **Chống bắt nạt: 4 tên, 4 luật** | SURV-11, PROG-12, WORLD-16, PX-05 | Một hệ thống, gọi là **"Thiên Đạo Ghi Nghiệp"**: đơn vị **Sát Nghiệp**, trạng thái đỉnh **Thiên Phạt**, khiên người mới **Linh Quang Hộ Thể**. | **g = cảnh giới THẬT** của kẻ giết − nạn nhân. Chỉ số combat tính sau Áp Chế, nhưng Thiên Đạo biết cảnh thật, nên C6 bị nén xuống C3 vẫn bị tính g=4 khi giết C2. **g≤0:** thưởng `1+0.5|g|` (Nghịch Thiên). **g=1:** ×0.6, **0 Nghiệp** (chuỗi thức ăn tự nhiên). **g≥2:** ×0.1 Sinh Năng, **+2 Nghiệp**, nạn nhân **Oán Linh +50% Đạo Tâm**. No (satiety) vẫn nhận đủ: ăn là ăn. Làm cây Đổ (không giết) tính +1. **Ngưỡng:** 1–2 aura đỏ trong 20 ô + kiếp +10%/Nghiệp · ≥3 **Huyết Sát** hiện trên bản đồ vùng, thưởng ×3 cho ai hạ · ≥6 **Thiên Phạt**: sét đuổi 1 ngày-rừng, mỗi 60s một sét 10% HP max, dừng khi offline. **Giảm 1/2h chơi online.** **Miễn trừ:** nạn nhân đánh trước (chủ động, không tính gai thụ động) thì không sinh Nghiệp trong 60s. Cùng cặp chỉ tính 1 lần/24h (chống farm Oán Linh bằng tài khoản phụ). **Khiên:** 60' trong Rừng chung hoặc tới C2: −60% sát thương từ g≥2, kẻ đánh không nhận gì, bị đánh dấu Bất Nhân 5'. Cộng thêm Ẩn Khí (C1–C2 không hiện trên radar của g≥2). |
| X5 | **Chi phí chết ở cảnh giới cao** | PROG-10 (C5 1.3 tuần), PROG-09, PX-06, SURV-15, WORLD-14i | Hai tầng chết. Mục tiêu: **chết có neo ≤1.5 phiên ở mọi cảnh**, **mất neo thì C5 ≈ 1 tuần**. | **Tầng 1 — Đầu Thai Hậu Duệ** tại neo (Mầm Con / Huyết Noãn trong Hang / Bào Tử / Ký Hồn Mộc / Nguyên Thần Bất Diệt ở C6): mất **50% CT của tầng hiện tại** (không rơi xuống dưới Sơ kỳ của cảnh hiện tại), mất kho cá nhân, giữ Huyết Mạch và Đạo Đồ. C3 ≈ 0.75 phiên · C5 ≈ 90 CT ≈ 1.4 phiên. **1 lần/24h thực**, mỗi nhân vật 1 neo, neo có HP và phá được (tạo lối chơi "tận diệt"). **Tầng 2 — Luân Hồi** (không có neo, neo đang CD, hoặc chết lần 2 trong 24h): bảng PROG-10, catch-up ×4 cho C5+. Sau khi chết có Hồn Hộ 10'. Thiên Kiếp thất bại = chết thật (giữ nguyên PROG). |
| X6 | **Độ bền cây vs TTK** | PROG-11, SURV-03/10, PX-03 | Blocker. Xem PROG-11. | PROG sim lại với HP 3 lớp. |
| X7 | **Sổ năng lượng: kill vs xác vs quỹ vùng** | PROG-10/12, SURV-09, WORLD-03 | Một pool. | Sinh Năng = 20 CT × `m(g)`, chia 40 kẻ ăn / 20 Linh Hạch / 40 đất. Phần đất đi vào quỹ vùng của WORLD-03. Khuẩn 3 CT/lần lấy từ phần đất. |
| X8 | **Lịch sự kiện bị chồng (7 + 8 + 4 sự kiện)** | SURV-17, WORLD-10, PX-15 | Mỗi tuần (= 1 năm-rừng): 1 sự kiện mùa/mùa, 1 Đại Linh Triều, Huyết Nguyệt vào đêm Đông. Sự kiện emergent có trần 1/ngày. | MVP chỉ làm 3: Linh Triều, Huyết Nguyệt, Đại Hạn/Hỏa (dùng chung lưới tile). Sau đó thêm Tu Sĩ Nhập Sơn và Thú Triều. |
| X9 | **Thời điểm rẽ nhánh tiến hóa** | PX-08 (nhánh ở phút 5–8), PROG-05 (C3, ~0.5 tuần) | Thuộc domain PROG, tôi không quyết. | Gợi ý: FTUE cho chọn một "Bản Năng" (skill đầu), còn Huyết Mạch vẫn ở C3. |

## Top 3 điều team phải chốt
1. **Bộ khung thời gian (X1 + X2):** 7 cảnh giới ánh xạ vào 3 cấp rừng, mùa 42h (1 năm-rừng = 1 tuần), Kỷ Nguyên map 28 ngày và Đại Kiếp nhân vật 8 tuần. Mọi con số khác (decay theo mùa, lịch sự kiện, pass, chi phí chết) đều phụ thuộc vào khung này.
2. **Mô hình hậu quả (X3 + X4 + X5):** luật Bế Quan hợp nhất, một hệ Thiên Đạo Ghi Nghiệp, và hai tầng chết (Hậu Duệ tại neo / Luân Hồi). Đây là trả lời cho câu "tôi sợ mất gì". Hiện có 3–4 phiên bản mâu thuẫn nhau.
3. **Cây sống được trong PvP (X6 + X7):** HP 3 lớp với Tâm Rễ không chạm được bằng đòn thường, TTK để cây Đổ ≥40s, và một sổ Sinh Năng thống nhất. Nếu sai chỗ này, "chơi cây", tức USP của game, chết ngay ở phút đầu tiên gặp sói.
