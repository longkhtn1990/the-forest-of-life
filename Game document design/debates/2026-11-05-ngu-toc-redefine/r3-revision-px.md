# R3 Revision — PX

Quy ước: t-n = tuần-người (dự án 1 người nên 1 t-n ≈ 1 tuần lịch). Baseline là v1.0 §16.1: 45,75 t-n + 4,25 đệm = 50 tuần, soft launch tuần 50. Mọi quyết định A–G của người dùng là đã chốt. Phần dưới chỉ xử lý cách làm, số liệu, rủi ro và fallback.

Những điểm tôi coi là đã hội tụ sau R2 và dùng làm đầu vào: Thú = **Lang** (C1–C4), Trùng = **Linh Nghĩ** (Hậu + Lính có chi phí No), Thủy = **Thanh Oa**, Vũ = **Linh Kê**, Mộc = **Linh Mộc**. FTUE giữ **chuột Tiền Thân**. NPC Trung Ấm là **Lão Quy**. Lite = **C1–C3**, đích là Kiếp Viên Mãn C3. Luật ô Q của PROG (khắc cấp tộc là cơ chế, hệ số = max, không nhân). Đạo Lộ thẻ thay Huyết Mạch/Ngộ Đạo (PROG-R2-02). Đường cong nén ×0,5 (PROG-R2-03). Lớp bảo vệ khi chết của SURV (SURV-R2-01…06).

---

## Phản hồi phản biện

| Phản biện (từ ai, ID) | Quyết định | Lý do | Thay đổi cụ thể |
|---|---|---|---|
| PROG, PX-03: "hệ số khắc nằm trong trần 1,32" sai (Blocker) | **Accept** | PROG đúng: 1,32 chưa chứa E. Cộng thêm ×1,15 cho ra 1,90, lớn hơn 1 cảnh (1,77) | PX-03b: khắc cấp tộc **chỉ là cơ chế** (chặn, Ướt, lộ vị, tài nguyên). Hệ số sát thương nằm trong ô Q = max(E, cơ chế) ≤1,25. Tổng ≤1,73 |
| SURV + PROG, PX-04: đơn giá lite 0,5–0,6/loài quá thấp | **Accept** | Bottom-up thực tế ≈0,8–1,0/loài cho C1–C3 | PX-04c: Nghĩ 1,0 · Oa 0,9 · Kê 0,8, cộng cổng C3 0,3 (bảng duy nhất ở dưới) |
| SURV + PROG, PX-01: lite C1–C2 làm ma trận thành trang trí và không đủ mốc cho D | **Accept** | C2 chỉ có 1 đột phá, tức 1 lần chọn thẻ. Không đủ cho D (3–5 lựa chọn mỗi mốc, kế thừa) lẫn F (random 3) | Lite = C1–C3. **Không còn phương án "hạ lite về C2"** trong fallback, vì nó vi phạm D/F. Fallback đúng là hoãn cả loài |
| SURV, PX-02: Thủy không có vai hỗ trợ party, chồng vai Mộc | **Accept** | Thủy = hồi động, Mộc = neo tĩnh | Oa: hồi 0,5% HP/5s cho đồng minh trong 3 ô khi Oa ở nước nông. Dẫn Nước +6 Thủy/phút cho cây là cơ chế phụ (chỉ có ở cấu hình A) |
| SURV + PROG, PX-03: 7 cặp chỉ có hệ số | **Accept** | Hệ số đã bị cấm theo ô Q, nên mỗi cặp cần 1 cơ chế | 10 cặp × 1 cơ chế dạng data (0,4) + cộng sinh thật: 4 cặp (A) hoặc 2 cặp (B/C) |
| WORLD, PX-03: vòng sinh của PX không theo Ngũ Hành | **Partial** | PROG chứng minh mọi cách xếp đều là cùng một vòng 5 được đổi nhãn. WORLD (lore owner) và PROG (số) chọn bản Tứ Tượng (Thú = Kim, Vũ = Hỏa, Trùng = Thổ). Tôi chỉ đòi điều kiện về khả năng đọc | Bỏ thứ tự của PX. Theo bản Tứ Tượng với điều kiện: tooltip viết bằng **vật chất** ("Phân/đất xới nuôi Trùng", luật WORLD), và HN5 đo ≥60% hiểu đúng ≥2 quan hệ. Trượt thì đổi văn bản tooltip, không đổi vòng |
| WORLD, PX-01: Thủy nên là Linh Quy | **Reject** | 3/4 chọn Oa. Rùa trên cạn chậm, nên trong 5 phút đầu không có "wow" (phút 2–6 chỉ thấy rùa lê). Nước sâu dễ thành vùng bất tử (PROG). Huyền Vũ vẫn có mặt qua **Lão Quy** (NPC giữ luân hồi), đúng nơi lore cần nhất | Giữ Oa. Linh Quy chơi được: [Post], cùng sprite gốc với Lão Quy |
| WORLD, PX-07: dời Linh Thảo sang Post và đổi tên chạm thẳng "Mộc gồm cỏ" | **Accept** | WORLD đúng. Bách Thảo dạng **1 trong 3 nhánh Đạo Lộ của Linh Mộc** đưa cỏ vào MVP gần như miễn phí (3 thẻ data) | PX-07b: Bách Thảo = nhánh Đạo Lộ Mộc [MVP]. Vật phẩm giữ tên "Linh Thảo". Bỏ đổi tên "Dược Thảo" |
| WORLD + SURV, PX-04: C2 cắt mất độ kiếp | **Accept** | Đã xử lý bằng C3-lite | — |
| WORLD, PX-10: bánh xe 3 lớn + "Xem thêm" | **Reject** (tôi đã tự rút ở R2) | Ẩn 2 tộc làm 40% lựa chọn mất khả năng khám phá, trong khi hook của game là "Ngũ Tộc". Quá tải được xử lý bằng bố cục, không phải bằng cách giấu | PX-10c: 5 thẻ, 1 thẻ hero + 4 thẻ nhỏ (xem PX-12) |
| SURV, PX-06: "Phi Lược"/"bay" tạo kỳ vọng sai | **Accept** | Review dạng "có bay mà không bay được" | MVP dùng tên **Sải Cánh**. Chữ "bay" chỉ xuất hiện ở Post (Ưng) |
| SURV, Q: chi phí Linh Thử AI + Hạt Quên đã tính chưa? | **Accept** (trước đây thiếu) | — | Dòng riêng 0,25 t-n trong bảng ngân sách |
| SURV, Q: Hóa Hình Mộng sang U1? | **Accept** | Không nằm trong vòng sinh tồn | −0,25 ở mọi cấu hình |
| SURV, Q: mất Đạo Quả meta thì lấy gì làm tiền mềm? | Trả lời | — | PX-09b: Đạo Quả thành **Đạo Hạnh** (thanh cấp tài khoản, không tiêu được). Hoa Lộ là ví kiếm được duy nhất |
| WORLD, Q: Hóa Tích hiện cho cả server ở MVP? | **Partial** | Giá trị cảm xúc cao (bằng chứng xã hội), nhưng tốn 0,3 | Chỉ ở gói tùy chọn A+. B/C dùng Biên Niên + Mộ Linh có sẵn |
| WORLD, Q: lore "Vũ Tộc Giáng Lâm" cho đợt 2? | Trả lời | — | Dùng ở cấu hình C. Đợt 1 vẫn có Quạ Già, Diều hâu, gà rừng AI. Quạ Già báo trước 7 ngày |
| WORLD-13: di sản mất hết khi đời sau chết | **Reject** (với tư cách economy/retention owner) | Mất trắng đã là chi phí. Mất thêm di sản là phạt kép, và chỉ phần thưởng dài hạn này giữ được D30 | Theo PROG: Sổ Di Sản không bao giờ mất. Ô trang bị của đời đó coi như đã dùng xong, đời sau chọn lại. **Ghi vào câu hỏi cho người dùng** |
| PROG, Q: ngưỡng đệm mới? | Trả lời | — | ≥8,5% = vàng (mức v1.0 đã chấp nhận) · 6–8,5% = cam · <6% = **đỏ, không khuyến nghị** |

---

## Đề xuất đã sửa

### PX-04c: Ngân sách MVP, bảng duy nhất

**Đối chiếu các ước tính của team** (vì sao có dải +0,7 đến +4,4):
| Nguồn | Net | Đã tính gì / thiếu gì |
|---|---|---|
| WORLD R1 | +0,7 (≈ +2,0 sau khi bỏ đếm trùng) | Lite C1–C2 rẻ, chưa có D–G |
| PX R1 | +1,45 | Lite 0,55/loài (quá thấp), chưa có D–G |
| SURV R2 | +2,35 → +2,75 | Lite 1,2/loài + G bắt buộc. Chưa tính D, F, lớp bảo vệ E |
| PROG R2 | +3,5 | Lite 1,5/loài, tín dụng "Lang→AI" sai. Sau đó PROG tự hạ đơn giá còn 0,9–1,0 và tính D ≈ ngang v1.0 |
| PX R2 | +1,6 (an toàn) / +2,65 (C3) / +4,4 (đủ D–G) | Gần bảng dưới. Khác ở chỗ D được tín dụng (44 thẻ ≈ 42 node + 18 skill) và lớp bảo vệ E đầy đủ hơn |
| **PX R3 (chốt)** | **A +4,35 · B +1,5 · C +0,5** | Bảng dưới, mỗi dòng chỉ tính một lần |

**Bảng ngân sách (delta so với v1.0)**
| # | Hạng mục | A | B | C | Ghi chú |
|---|---|---|---|---|---|
| **Thêm** | | | | | |
| 1 | Linh Nghĩ lite C1–C3 (Hậu+Lính, Tha, 9 thẻ, sprite) | 1,0 | 1,0 | 1,0 | Dùng lại swarm của Kiến lite |
| 2 | Thanh Oa lite C1–C3 (Dính Lưỡi, ẩn/hồi nước, Ẩm, 9 thẻ) | 0,9 | 0,9 | 0,9 | |
| 3 | Linh Kê lite C1–C3 (Sải Cánh, Báo Tin, Bới, 9 thẻ) | 0,8 | 0,8 | **0** (đợt 2) | |
| 4 | Cổng C3: Kiếp Viên Mãn template × số loài lite | 0,3 | 0,3 | 0,2 | |
| 5 | UI 5 tộc: bánh xe, tên cảnh giới, hint động từ tộc + Director "thắng đầu" mỗi tộc | 0,35 | 0,3 | 0,3 | |
| 6 | Nước: tile/autotile, nông/sâu, bảng địa hình SURV, Hồ Con, cá decor, Ướt | 0,7 | 0,55 | 0,55 | B/C: nước sâu chỉ có ở Hồ Con, Đầm Mục để nông |
| 7 | Ma trận 10 cặp × 1 cơ chế (data) + icon/tooltip | 0,4 | 0,4 | 0,35 | |
| 8 | Cộng sinh thật (Khế ước Kiến có sẵn + mới) | 0,4 (4 cặp) | 0,15 (2) | 0,15 (2) | A: + Tưới, Mở Xác, Báo Tin · B/C: + Tưới |
| 9 | Trung Ấm nước, Lão Quy, pool câu, đổi tên Khuẩn | 0,3 | 0,3 | 0,3 | |
| 10 | D: UI Đạo Lộ (≤5 thẻ, Đặt Trước/Chọn Sau) + pipeline + tái cấu trúc Mộc/Lang (có Bách Thảo) | 0,6 | 0,6 | 0,6 | |
| 11 | E: Trọng Thương C3+, Kiếp thất bại lùi tầng, UI "Ngươi để lại", Trung Ấm 2 biến thể, nén đường cong | 0,6 | 0,5 | 0,5 | B/C: 1 biến thể Trung Ấm |
| 12 | Đạo Hạnh (thanh tài khoản, thay Đạo Quả Bàn) | 0,15 | 0,15 | 0,15 | |
| 13 | F: random 3, Sổ Di Sản, ô 1/2/3, bảng dịch 25 ô | 0,5 | 0,4 | 0,4 | |
| 14 | Linh Thử FTUE + AI (reskin controller, Hạt Quên) | 0,25 | 0,25 | 0,25 | |
| 15 | QA/sim cân bằng 5 tộc, band PvP | 0,45 | 0,4 | 0,35 | |
| | **Tổng thêm** | **7,70** | **7,00** | **6,00** | |
| **Bớt** | | | | | |
| c1 | #4 Linh Thử bản đầy đủ | −1,0 | −1,0 | −1,0 | Thay bằng dòng 14 |
| c2 | #5c Kiến lite: swarm/AI chuyển vào Nghĩ | −0,4 | −0,4 | −0,4 | |
| c3 | #5d Hóa Hình Mộng → U1 | −0,25 | −0,25 | −0,25 | SURV đồng ý |
| c4 | #8 Huyết Mạch + Ngộ Đạo draft → Đạo Lộ | −0,5 | −0,5 | −0,5 | 44 thẻ PROG |
| c4b | #8 phần nội dung của Linh Thử (6 skill, 2 HM) | −0,3 | −0,3 | −0,3 | |
| c5 | #10 Hậu Duệ, Túc Tuệ, Hồi Ức, Đạo Quả Bàn | −0,8 | −0,8 | −0,8 | Hệ quả bắt buộc của E |
| c6 | Pool Trung Ấm 60 → 40 câu | −0,1 | −0,1 | −0,1 | |
| c7 | #5b Linh Thức → chỉ còn do thám | 0 | −0,4 | −0,4 | Cắt sẵn ở cổng 30 của v1.0, nay cắt từ đầu |
| c8 | #6 palette mùa 4 → 2 | 0 | −0,2 | −0,2 | |
| c9 | #18 shop 6 → 4 skin | 0 | −0,1 | −0,1 | |
| c10 | Linh Tức vi mô chỉ ở FTUE/Linh Triều | 0 | −0,1 | −0,1 | |
| c11 | #7b Linh Quỹ động → mật độ tĩnh | 0 | −0,75 | −0,75 | Mất H13 Khô Linh, cá thành decor tĩnh |
| c12 | #12 catch-up solo rút gọn (giữ Bế Quan, Mộng Báo) | 0 | −0,3 | −0,3 | |
| c13 | #17 sự kiện: chỉ Đại Linh Triều + Đại Kiếp lite | 0 | −0,3 | −0,3 | |
| | **Tổng bớt** | **−3,35** | **−5,50** | **−5,50** | |
| | **Net** | **+4,35** | **+1,50** | **+0,50** | |
| | Tổng việc (t-n) | 50,10 | 47,25 | 46,25 | |

**Ba cấu hình cho người dùng chọn**
| | A: Đủ hết, dời ngày | B: Rút gọn trong 50 tuần | C: Ra mắt theo đợt |
|---|---|---|---|
| Soft launch | **Tuần 55** (dời 5 tuần) | Tuần 50 | Tuần 50 (4 tộc) + **đợt 2 Vũ tuần 53–54** |
| Đệm | 4,25 (8,5%), **vàng** | 2,75 (5,5%), **đỏ** | 3,75 (7,5%), **cam** |
| Tộc chơi được ngày 1 | 5 | 5 | 4 (Mộc, Thú, Trùng, Thủy). Kê đợt 2 = 1,1 t-n (0,8 loài + 0,1 Kiếp + 0,1 tích hợp + 0,1 event) |
| Cái bị cắt | Chỉ những gì quyết định A–G đã thay thế, cộng Hóa Hình Mộng | A + Linh Thức chỉ do thám, 2 mùa, 4 skin, Linh Quỹ tĩnh, catch-up gọn, chỉ 1 sự kiện lớn, 2 cộng sinh thật, nước sâu chỉ ở Hồ Con | Như B, cộng việc hoãn Kê |
| Rủi ro chính | Lỡ cửa sổ thời gian, chỉ còn 1 tuần "lùi khẩn cấp" (v1.0 cho tối đa 6) | Lịch sử: đệm 8,5% đã bị cờ rủi ro, 5,5% gần như chắc chắn bị ăn hết vào tuần 40 | Store page và trailer ngày 1 chỉ có "Tứ Tộc". Cần copy "Ngũ Tộc, tộc thứ năm giáng lâm" |
| Gói thêm A+ (tùy chọn) | +0,75: Hóa Tích lite (0,3) + cơ chế phụ mỗi tộc (Đánh Hơi, Tổ, Dẫn Nước, Gáy: 0,45). Cần dời **6 tuần** (đệm 10,1%) | Không | Không |

**Khuyến nghị PX: A (dời 5 tuần).** Lý do: bốn quyết định D, E, F, G đụng cả 4 hệ lõi (progression, cái chết, meta, bản sắc loài). B dồn hết rủi ro vào một khoản đệm chắc chắn bị ăn. Nếu cổng tuần 30 trượt thì A tự rơi về C (đã định nghĩa sẵn bên dưới), không cần quyết định lại. Nếu người dùng không chấp nhận dời ngày, chọn **C**, không chọn B.

**Không có cấu hình nào cho:** lite C1–C2 (vi phạm D/F), hay 5 tộc mà một số tộc chỉ là AI ở ngày 1 (vi phạm C trừ khi người dùng đồng ý ra mắt theo đợt).

**Thứ tự làm (module hóa, để mỗi cổng có một game đóng được):** E (đơn giản hơn Hậu Duệ) → D (Đạo Lộ trên Mộc/Lang) → Oa → Nghĩ → F → Kê → cơ chế phụ G.

### PX-15: Cổng, scope risk và fallback (thay §16.1 fallback)
| Cổng | Đo | Ngưỡng trượt | Hành động |
|---|---|---|---|
| Tuần 2 (spike) | Dính Lưỡi trên 2 client trễ 150 ms | Giật/hit sai >10% | Dính Lưỡi lên người chơi chỉ còn làm chậm (đã là mặc định, xem PX-02b) |
| **Tuần 16 (VS)** | VS = FTUE chuột → Trung Ấm Lão Quy → bánh xe 5 thẻ → Linh Mộc C1–C2 với Đạo Lộ · Lang AI · **Oa prototype** · mất trắng + Trọng Thương · 2 client | VS >13 t-n | A → C (Kê sang đợt 2). Nếu >15 t-n: C + dời 2 tuần |
| Tuần 24 (Nghĩ xong) | Chi phí thực của Nghĩ | >1,3 t-n | Đơn giá lite sai ≥30%: Kê sang đợt 2 ngay |
| **Tuần 30 (alpha)** | Lịch | Trễ >2 t-n | Áp các mục cắt của B (c7–c13) lên cấu hình hiện tại. Trễ >4: C |
| Tuần 38 (beta) | HE1/HE4 (bên dưới) | Rời game sau chết C3+ >35% | Trọng Thương áp cho mọi nguyên nhân chết, Ấu Linh kéo tới hết C2 nếu chưa có |
| **Không bao giờ cắt** | Linh Mộc, Lang, FTUE chuột, mất trắng có lớp bảo vệ, Đạo Lộ 3–5 thẻ, Viên Mãn + Di Sản, độ kiếp C3, Rừng chung PvP, Thiên Đạo L1–L3, **≥4 tộc chơi được ngày 1** | | |

### PX-10c: FTUE mới: chuột Tiền Thân → chết → chọn tộc
Nguyên tắc giữ nguyên: mỗi beat dạy **một** động từ, 100% local, đường cong kịch bản. Hai điểm mới: (1) người chơi phải **hiểu luật mất trắng ngay lần chết đầu**, khi chưa mất gì, để lần chết thật không bất ngờ. (2) Cả 5 tộc phải được **nhìn thấy trước** khi chọn (nhận ra quen hơn là phải đọc).

| Phút | Beat | Học được | Cảm xúc | Phần thưởng / UI | Tộc thấy |
|---|---|---|---|---|---|
| 0:00–0:40 | Mộng Hỏa rơi qua Lão Tùng, nhập vào Linh Thử | Chạm/kéo | Kỳ vĩ | Joystick | Mộc |
| 0:40–3:00 | Ăn hạt Linh Thảo phát sáng. Vignette 5s: kiến khiêng hạt qua đường (WORLD, dùng swarm có sẵn) | Ăn = tu vi | Thỏa mãn | Thanh tu vi, No | Trùng |
| 3:00–5:00 | Bóng diều hâu. Nút Ẩn ở bụi | Có kẻ săn, trốn được | Hồi hộp | HP | Vũ |
| 5:00–7:30 | Tiểu Kiếp C1→C2, rồi **lựa chọn Đạo Lộ đầu tiên: 3 thẻ**, 1 thẻ gắn "Gợi ý" | Đột phá = chọn hướng | Hùng tráng (mốc fun #1) | Vòng gỗ vòng 1 | — |
| 7:30–10:30 | Gai cây non, Lão Tùng thả Linh Quả, chuột ngậm hạt. Gà rừng AI bới lá lộ sâu gần đó (background) | Cây có ý thức | Ngạc nhiên | Icon hạt | Vũ (Kê) |
| 10:30–12:00 | Thọ Nguyên 12'. Quạ Già báo Linh Tức. Ếch AI quăng lưỡi bắt bướm ở Hồ Con (background) | Sinh mệnh có hạn | Khẩn trương nhẹ | Thọ Nguyên | Thủy (Oa) |
| 12:00–14:00 | Sói AI tiến về ổ. (A) dụ sói ra xa: ổ chuột con sống, Biên Niên "Hộ Ổ", Tâm Hướng Sinh/Hợp. (B) về chết già dưới Lão Tùng: **đất nơi xác +30% Dưỡng Chất** (trạng thái thế giới, không phải sức mạnh mang theo) | Cái chết là lựa chọn | Day dứt | — | Thú (Lang) |
| 14:00–15:00 | **Trung Ấm bên mặt nước (45s)**: xác chìm, nước đổi màu. Lão Quy: *"Ngươi đã mang nó cả đời. Giờ nó mang ngươi."* Rồi luật nói một lần: *"Chết giữa đường, ngươi trả lại cho rừng. Đi hết đường, rừng trả lại cho ngươi."* Thẻ "Ngươi để lại": hạt nảy mầm, 38 linh khí, Biên Niên trang 1, +Đạo Hạnh | **Luật E và F** | Xúc động (mốc fun #2) | Thanh Đạo Hạnh nhích lên | Thủy (Lão Quy) |
| 15:00–15:40 | **Chọn tộc: 5 thẻ** (PX-12). Hero: Linh Mộc *"Trở thành hạt giống ngươi đã mang"* | Đổi tộc | Háo hức | — | Cả 5 |
| 15:40–20:00 | Đời 2. Linh Mộc: beat v1.0 (rễ, Vệt Nắng, gai hươu, Manh Nha). Tộc khác: hint động từ tộc 60s + Director cho "thắng đầu" trong ≤3' (Lang: thỏ · Nghĩ: xác cạnh tổ · Oa: bướm ở Hồ Con · Kê: sâu dưới lá). **Lựa chọn đầu của đời 2 ≤5'** (SURV-R2-04, PROG nén đường cong). Không còn Hồi Ức | Lối chơi thứ hai khác hẳn | "Mình là cái cây/sói/kiến…" | Vòng gỗ hiện vòng cuối mờ: *"Viên Mãn: mang theo 1 Đạo Chủng"* (đặt mục tiêu) | — |
| ~20:00 | Mở Rừng chung/riêng. Vé Tự Quy giữ nguyên (P2 sang sói ngay) | — | — | — | — |
| ~25:00 | Gương: Linh Thử AI ăn Linh Quả đầu của cây. Nếu chọn A, đó là **chuột con của ổ** | Vòng tuần hoàn khép lại | Hiểu ra | — | — |

Chi phí: nằm trong #15 FTUE của v1.0 + dòng 5/9/14. Ếch và gà AI là sprite của loài lite, chạy AI decor.

### PX-12 (mới): Chống choice paralysis trên mobile
**(a) Chọn tộc (5 thẻ).** Landscape: thẻ hero bên trái (40% chiều rộng, chọn sẵn), lưới 2×2 bên phải. Mỗi thẻ: tên đại diện + vai ≤6 chữ (vd *Oa: "Rình bên nước, kéo mồi"*) + 1 icon động từ + độ khó ●○○ + ảnh "Ngươi đã thấy" lấy từ FTUE. Không có chỉ số. Nút chính "Chọn" luôn ở cùng chỗ. Chạm vào thẻ thì mở 1 clip 4s. Lần sau (khi chết hoặc Viên Mãn): thẻ hiện thêm "Đời gần nhất: …" và số người tộc đó trong phòng (PX-14).
**(b) Đạo Lộ mỗi mốc (3–5 thẻ, PROG).** Số thẻ: 3 (C1→2) · 4 (C2→3, C3→4) · 5 (hậu kỳ C4). Màn hình 844×390 pt chứa đủ 5 thẻ × ~150 pt nên **không vuốt, không ẩn**. Mỗi thẻ: tên ≤2 từ (WORLD) + 1 dòng ≤12 chữ + icon trục (Sát/Hộ/Động/Hồi/Thức) + nhãn "Kế thừa" nếu nối với thẻ trước + nhãn "Sống sót" (SURV: mỗi bộ có ít nhất 1 thẻ sống sót).
- **Đặt Trước:** vì pool cố định và xem trước được, người chơi đánh dấu thẻ dự định bất cứ lúc nào ngoài giao tranh. Lúc đột phá, thẻ áp tự động với toast 3s "Đổi?". Mục tiêu ≥50% lựa chọn ở C2+ đi qua Đặt Trước.
- **Chọn Sau:** đột phá giữa Rừng chung PvP thì **không bao giờ bật màn hình chặn**. Có huy hiệu "1 lựa chọn đang chờ", chọn được khi ở Hang/Neo/ngoài giao tranh 10s, không giới hạn thời gian. Hiệu ứng tính từ lúc chọn.
- Xác nhận bằng nút riêng (không chọn bằng một chạm vào thẻ), để bấm nhầm <5% (H10).
**(c) Di Sản (random 3).** 3 mảnh sáng (WORLD-10), ≤12 chữ mỗi mảnh, hiện luôn bản "dịch" sang tộc dự định của đời sau.
Chi phí: nằm trong dòng 10 và 13.

### PX-13 (mới): Giảm rủi ro retention của chết mất trắng (UX, không đổi luật)
Mục tiêu đo bằng phút bị mất (SURV): ≤40' ở C1–C2, ≤90' ở C3+, có lớp bảo vệ khi vượt ngưỡng. Với đường cong nén (PROG): lite C3 ≈ 3h, C4 ≈ 5,5–6h. Người chơi casual (~25'/ngày theo KPI 14' × 1,8 phiên) đạt Viên Mãn lite **khoảng ngày 7**, C4 **khoảng ngày 14**. Người chơi core (~90'/ngày) đạt lite ngày 2, C4 ngày 4.

| # | Biện pháp | Phục vụ ai | Chi phí |
|---|---|---|---|
| 1 | **Không bất ngờ**: luật dạy ở FTUE phút 14 khi chưa mất gì. Vòng gỗ luôn hiện "Đời này: 2h10'", chỉ trong menu, không trên HUD | Mọi persona | 0 |
| 2 | **Cái chết đọc được**: Trung Ấm hiện nguồn chết, cảnh `g`, đòn cuối, và "Ngươi để lại" (cây con ở chỗ chết, Dưỡng Chất vùng, trang Biên Niên) | P3 | dòng 11 |
| 3 | **Luôn có một thanh đi lên**: mỗi cảnh đạt được trong đời cộng Đạo Hạnh **ngay lúc đạt**, nên chết không lấy lại. Màn chết hiện "+N Đạo Hạnh, cấp tài khoản 7 → 8" | P1, P3 | dòng 12 |
| 4 | **Khởi động lại nhanh**: ≤20s tới lúc điều khiển. Trung Ấm bỏ qua được từ lần 2. Lựa chọn đầu tiên ≤5'. Không FTUE lần 2 | Mọi persona | 0 |
| 5 | **Điểm dừng an toàn**: thoát game ở Hang/Neo/Hồ Con = ngủ an toàn (§5.9). Thoát ngoài trời = đếm ngược 30s, hiện rõ. Quan trọng nhất cho mobile (cuộc gọi đến, hết pin) | P1 | trong §5.9 v1.0 |
| 6 | **Cảnh báo trước khi nguy**: Thần Thức báo ▲ trong 20 ô (đã có). Kiếp Báo 60s trước Tiểu Kiếp ở Rừng chung. Huy hiệu "đời có giá trị" khi >90' nhắc người chơi về điểm an toàn gần nhất | P1, P3 | 0,05 (trong dòng 11) |
| 7 | **Hook quay lại sau chết**: Mộng Báo ngày hôm sau *"Cây con nơi ngươi ngã đã cao 2 ô"* (WORLD-10). Mộ Linh đặt hoa được (Hoa Lộ sink, PX-09b) | P3 | 0,05 |
| 8 | **Ad an ủi chỉ sau 8s** trên màn Trung Ấm, không bao giờ che nút "Đời mới" | — | 0 |
| 9 | **Gợi ý đổi tộc khi chết**: thẻ hero ở lần chọn sau là tộc người chơi chưa thử (không phải tộc vừa chết). Biến mất mát thành sự mới mẻ (G) | P1, P3 | 0 |

Ngoài domain nhưng tôi ủng hộ và đã tính vào dòng 11: Kiếp thất bại ≠ chết (SURV-R2-01, PROG), Trọng Thương C3+ (SURV-R2-02), CT ×0 khi g≥2 (đã có §8).
**Câu hỏi cho người dùng (không phải đề xuất):** Rừng riêng (solo) có được dùng trục "Hình phạt chết" của v1.0 (§13) để bật "1 lần Hộ Mệnh mỗi đời" không? Mặc định PX: **không**, tôn trọng quyết định E.

### PX-09b: Kinh tế sau khi bỏ meta sức mạnh
```
cảnh đạt (mỗi đời, tính ngay) ~60% ─┐
Viên Mãn ×3 thưởng ~25%            ├─► [Đạo Hạnh] (cấp tài khoản, KHÔNG tiêu) ─► mỗi cấp: 1 phần thưởng ngang
đời đầu mỗi tộc +50% ~10%          │       (Tiền Kiếp Ấn bậc, khung Biên Niên, hậu tố Đạo hiệu). Vô hạn, prestige mỗi 10 cấp
Oán Linh / sự kiện ~5%             ┘
sự kiện/thành tựu/ad ──────────────► [Hoa Lộ] (ví kiếm được duy nhất) ─► skin (~1/10h) · hoa Mộ Linh (5, tiêu hao) · [A+] trang trí Hóa Tích
Viên Mãn ──────────────────────────► [Sổ Di Sản] (không phải tiền) ─► ô trang bị 1 / 2 / 3 ở Viên Mãn lần 1 / 3 / 6
nạp tiền ──────────────────────────► [Ngọc Tinh] ─► skin, Pass. KHÔNG đổi sang ví khác
```
- **Vì sao Đạo Hạnh không tiêu được:** danh mục mở khóa ngang hữu hạn (5 tộc mở sẵn, vài node QoL), nên một ví tiêu được sẽ bão hòa sau ~8–10h và người chơi tích trữ vô nghĩa (HK2 ở R2). Thanh cấp không cần sink, không lạm phát, và là "thanh luôn đi lên" của PX-13. Bỏ một ví nên người chơi chỉ còn 2 thứ phải hiểu: Hoa Lộ và Ngọc Tinh.
- **Chống farm:** Đạo Hạnh tính theo **lần đầu đạt mỗi cảnh trong một đời**, nên tự sát rồi làm lại chỉ farm được C1 (rất ít). Không có Đạo Hạnh từ kill PvP.
- **Di Sản là phần thưởng dài hạn thay Đạo Quả Bàn** (thang PROG): ô 2 ở Viên Mãn lần 3, ô 3 ở lần 6. Với P(hoàn thành) ≈55% và đời lite 3h/full 6h, ô 3 rơi vào khoảng 30–50h chơi, tức hook D30 cho core. Lite Viên Mãn cho di sản bậc 1 (giá trị ×0,6, SURV) nhưng **vẫn tính 1 lần trên thang ô**, để lite không bị coi là "đời không đáng".
- **Tộc:** cả 5 mở sau FTUE. Không bán tộc. Loài thứ hai của mỗi tộc (1.0/Post) mở bằng cấp Đạo Hạnh hoặc Nghiệp Duyên, không bằng tiền.
- **Sửa §14.2:** bỏ ad "Hồi sinh tại chỗ" ở solo (mua cách né mất trắng, vi phạm E). "Đạo Quả +30% khi chết" → "Đạo Hạnh +30% khi chết" (3/ngày), được bật **cả ở PvP** vì nay không còn là sức mạnh. Giúp đạt KPI ad ≥25% DAU. Shop MVP: A 6 skin, B/C 4 skin (Lang, Nghĩ, Oa, Kê, vì Linh Mộc procedural).
- **Pass Kỷ Nguyên [U1]:** spotlight 1 tộc mỗi 28 ngày, xoay vòng 5 tộc. Free: Hoa Lộ + 2 skin. Premium ~4,99 USD: 6 skin của tộc spotlight + hiệu ứng Viên Mãn. **Không bao giờ có Đạo Hạnh, CT, Di Sản.** Spotlight còn là đòn bẩy cân bằng dân số (đẩy tộc thiếu người).

### PX-14 (mới): Phân bố tộc ở CCU 24–40
Giả định mục tiêu: Mộc 30%, Lang 22%, Nghĩ/Oa/Kê 16% mỗi tộc. Kịch bản xấu: một tộc lite chỉ 8%.
| CCU phòng | Số người kỳ vọng mỗi tộc lite (16%) | P(tộc vắng cả phòng) 16% / 8% | P(vắng trong 1 vòng map, ~⅓ phòng) 16% / 8% |
|---|---|---|---|
| 12 (sàn KPI U1) | 1,9 | 12% / 37% | 50% / 72% |
| 24 | 3,8 | 1,5% / 13% | 25% / 51% |
| 40 | 6,4 | 0,1% / 3% | 10% / 33% |
Kết luận: ở cấp phòng, CCU ≥24 đủ đa dạng nếu mọi tộc ≥12%. Ở cấp vòng map (nơi giao tranh thật xảy ra), 25–50% thời gian một tộc lite vắng mặt. Do đó:
1. **Ma trận phải sống bằng AI:** cơ chế khắc/sinh áp cho cả AI cùng tộc (Lang AI, bầy sâu, gà rừng AI, ếch AI, Diều hâu). Chi phí 0 vì là data.
2. **Không vai nào phụ thuộc tộc khác có mặt:** mỗi tộc có một động từ solo (Oa kéo mồi, Kê thấy Linh Hạch, Nghĩ Mở Xác). Cộng sinh dành cho party 2–4 người.
3. **Cân bằng mềm:** bánh xe hiện số người mỗi tộc trong phòng. Tộc <10% trong 30' thì bật ưu ái loài thiếu của v1.0 (§17.1) kèm nhãn "Rừng đang cần". Lobby ưu tiên xếp người chơi vào phòng mà tộc của họ ít nhất (Could, 0,05).
4. **Gộp phòng khi CCU <10** (nâng từ 8) vì có 5 tộc.
5. Telemetry: tỉ lệ tộc theo phòng/giờ, theo vòng map · số lần cặp khắc/sinh gặp nhau mỗi phiên (người–người và người–AI) · tỉ lệ chết/giờ theo tộc.

### Các ID khác đã sửa
- **PX-01b:** đại diện như phần đầu file. Lite = C1–C3, đích Kiếp Viên Mãn C3.
- **PX-02b:** Trùng phá Tâm Rễ: theo PROG (Căn Thương mở từ C3, nhân 0,5^chênh cảnh) cộng SURV/PX (chỉ chạy khi Thú/Vũ đã hạ phòng ngự trong 30s). Thủy: hồi đồng minh. **Dính Lưỡi** của Oa: kéo được AI và vật phẩm, lên người chơi thì chỉ làm chậm 1s (lai giữa PROG và SURV, tránh rủi ro netcode). SURV/PROG chốt số.
- **PX-05b:** Lão Quy, Trung Ấm bên mặt nước, Ao Sương mở Mộng Ấn 1. Tên E7 do WORLD chốt (Triều Mộng là tên lore, cơ chế dùng hệ mưa có sẵn).
- **PX-06b:** Sải Cánh (MVP), Ưng bay [Post].
- **PX-07b:** Bách Thảo = nhánh Đạo Lộ của Linh Mộc [MVP]. Linh Thảo loài riêng → [Won't], trừ khi KPI 1.0 đòi.
- **PX-08b, roadmap:** MVP theo cấu hình đã chọn · **U1:** (C) Kê + event Giáng Lâm · lite → C4 · C5, Pass, Android như v1.0 · Hóa Hình Mộng · **1.0:** loài thứ hai đầu tiên (Linh Thử chơi được, ứng viên khác: Ong) · cộng sinh thật cho đủ 10 cặp · Hóa Tích nếu chưa có · **Post:** Linh Quy, Lý "Vũ Môn", Ưng bay, Bướm.

### PX-11b: Giả thuyết playtest (thay HN1–HN9 và cộng thêm H1–H13 v1.0)
| ID | Giả thuyết | Ngưỡng | GĐ | Nếu trượt |
|---|---|---|---|---|
| HF-1 | FTUE mới vẫn tạo ham muốn chơi đời 2 | ≥70% bắt đầu đời 2 trong 60s | VS | Rút Trung Ấm lần đầu còn 30s, giữ câu Lão Quy |
| HF-2 | Người chơi hiểu luật E/F sau FTUE | ≥80% trả lời đúng "chết thì mất gì, giữ gì" | VS | Thêm 1 dòng luật trên màn chết lần 2 |
| HF-3 | Cả 5 tộc được nhận ra | ≥60% kể được ≥4/5 tộc | VS | Đẩy vignette ếch/gà ra foreground |
| HC-1 | Chọn tộc không gây tê liệt | Trung vị ≤25s, ≤15% mở >2 clip | VS | Bớt chữ trên thẻ, tăng ảnh "Ngươi đã thấy" |
| HC-2 | Lựa chọn Đạo Lộ nhanh trên mobile | Trung vị ≤20s · ≥70% chọn không mở chi tiết · ≥50% ở C2+ dùng Đặt Trước | Alpha | Giảm thẻ C2→3 từ 4 xuống 3 |
| HC-3 | Không thẻ trội/thẻ chết | Không thẻ nào >50% hay <5% lượt chọn khi có mặt | Alpha | PROG chỉnh số |
| HE-1 | Mất trắng chịu được | Chết C3+ do PvP: ≥45% quay lại trong 72h · rời game ≤60s sau chết ≤25% | Alpha/Beta | Cổng tuần 38 (PX-15) |
| HE-2 | Chết sớm không gây bỏ game | Chết trước C3: ≥65% bắt đầu đời mới trong 2' | Alpha | Rút ngắn thời gian tới lựa chọn đầu |
| HE-3 | P1 không bỏ game | P1 (cozy) bỏ game ≤40% trong Phiên 1–6 | Alpha | Ấu Linh tới hết C2 + điểm dừng an toàn rõ hơn |
| HE-4 | Mộc không thành "bến an toàn" độc chiếm | Mộc ≤45% lượt chọn sau 7 ngày | Alpha | Hero card gợi ý tộc chưa thử, Pass spotlight |
| HV-1 | Viên Mãn đạt được | P(hoàn thành) ≥55% · trung vị lite ≤3,5h, full ≤7h | Alpha | PROG nén thêm CT_cảnh |
| HV-2 | Di Sản kéo đời tiếp | ≥70% chọn trong ≤15s và bắt đầu đời mới trong 2' | Alpha | Hiện bản dịch rõ hơn |
| HV-3 | Di Sản không phá PvP | Người có di sản thắng cùng cảnh ≤55% | Alpha | Hạ trần ô Sát |
| HV-4 | Lite không thành đường tắt farm | Lite chiếm ≤60% số Viên Mãn ở người có ≥3 Viên Mãn | Beta | Lite tính ½ trên thang ô |
| HG-1 | "Chất" tộc khác biệt | ≥65% mô tả "tộc X chơi khác chỗ nào" trong 1 câu | Alpha | Tăng độ tương phản động từ, không thêm cơ chế |
| HG-2 | Đổi tộc diễn ra tự nhiên | ≥50% chơi ≥3 tộc trong 5 đời đầu | Beta | Ưu đãi Đạo Hạnh đời đầu mỗi tộc +50% → +100% |
| HD-1 | Phân bố tộc | Mỗi tộc 10–40% trong 7 ngày (thay H7) | Alpha | PX-14 mục 3 |
| HD-2 | Ma trận được cảm nhận | ≥60% giải thích đúng ≥2 quan hệ · ≥3 lần gặp cặp khắc/sinh mỗi phiên (tính cả AI) | Alpha | Tăng mật độ AI theo tộc |
| HW-1 | Nước nông không thành bẫy | Chết trên ô nước ≤1,3× trung bình | Alpha | SURV chỉnh bảng địa hình |
| HW-2 | Nước sâu không thành vùng bất tử | CT/giờ ở nước sâu ≤0,3× ở bờ | Alpha | Giới hạn lặn ≤20s |
| HK-1 | Kê: Sải Cánh không bấm nhầm | Bấm nhầm <5% · tỉ lệ thoát thành công ≤55% | Alpha | Đổi sang giữ để kích hoạt |
| HK-2 | Hoa Lộ không tích trữ vô nghĩa | <30% người chơi 10h+ có Hoa Lộ dư ≥3 skin | Beta | Thêm hàng xoay vòng, tiêu hao Mộ Linh |
KPI go/no-go U1 của v1.0 giữ nguyên. Riêng D30 ≥3% được đánh dấu **rủi ro cao** vì đã mất meta sức mạnh, nên phải đo cohort từ closed alpha tuần 30.

---

## Risk Register (cập nhật, domain PX)
| Rủi ro | KN | TĐ | Giảm thiểu | Owner | Fallback |
|---|---|---|---|---|---|
| Đệm dưới 8,5% (B: 5,5%) | Rất cao (B) / TB (A) | Rất cao | Chọn A hoặc C, cổng 16/24/30 | PX | A → C → áp B-cuts |
| Đơn giá lite sai ≥30% | Cao | Cao | Đo Nghĩ ở tuần 24 | PX | Kê đợt 2 |
| Mất trắng làm sụp D7/D30 | Cao | Rất cao | PX-13, Trọng Thương, Đạo Hạnh, thang Di Sản | PX/SURV | Cổng tuần 38 |
| Choice paralysis mobile | TB | Cao | PX-12 (Đặt Trước, Chọn Sau, ≤12 chữ) | PX | Giảm số thẻ ở C2→3 |
| Ma trận vô hình ở CCU thấp | Cao | TB | Áp lên AI, cộng sinh party | PX/SURV | Tăng mật độ AI |
| Mộc độc chiếm (bến an toàn) | Cao | Cao | Hero card gợi ý tộc mới, Pass spotlight, ưu ái loài thiếu | PX | Hạ ưu tiên Mộc trên bánh xe sau FTUE |
| Lite = đường farm di sản | TB | TB | Lite bậc 1 (×0,6) | PROG/PX | Lite tính ½ trên thang ô |
| Bốn hệ lõi đổi cùng lúc (D, E, F, G) | Cao | Rất cao | Làm theo module E → D → F → G | PX | Cơ chế phụ G chỉ nằm ở A+ |
| Store hứa "Ngũ Tộc" nhưng ra mắt 4 (C) | TB | TB | Copy "tộc thứ năm giáng lâm", ngày công bố cụ thể | PX/WORLD | — |

---

## Những thứ tôi mượn từ người khác
- PX-10c, PX-13 (từ WORLD-10): câu luật *"Chết giữa đường, ngươi trả lại cho rừng…"*, cây con ở chỗ chết, Lão Quy vớt 3 mảnh sáng, vignette kiến khiêng hạt.
- PX-09b (từ PROG-R2-04): thang ô Di Sản 1/2/3, Sổ không mất. (từ SURV) lite bậc 1.
- PX-12 (từ PROG-R2-02): pool cố định xem trước (cơ sở để có Đặt Trước), số thẻ 3/4/4/5. (từ SURV) nhãn "Sống sót". (từ WORLD-11) tên ≤2 từ, vòng gỗ.
- PX-13 (từ SURV-R2-01…06, PROG-R2-03): ngưỡng phút mất, Trọng Thương, Kiếp thất bại ≠ chết, khởi động lại ≤5', nén ×0,5.
- PX-07b (từ PROG-05, SURV): Bách Thảo.
- PX-03b (từ PROG-R2-01): ô Q.

## Lập trường giữ vững (và vì sao)
1. **Oa, không Quy**: wow trong 60s đầu, không có vùng bất tử. Huyền Vũ đã có Lão Quy.
2. **5 thẻ chọn tộc, không ẩn**: hook là Ngũ Tộc. Quá tải giải bằng bố cục và sự quen thuộc từ FTUE, không bằng cách giấu.
3. **Không lite C2** trong bất kỳ fallback nào: thiếu mốc cho D/F. Trượt thì hoãn cả loài.
4. **Không chọn B** dù nó vừa ngân sách: đệm 5,5% là ảo tưởng với một dev solo.
5. **Di Sản không mất khi chết** (ngược WORLD-13): phạt kép giết mất phần thưởng dài hạn duy nhất còn lại. Người dùng chốt.
6. **Không màn hình chọn chặn giữa PvP**: Chọn Sau là bắt buộc, không phải tùy chọn.

## Điều tôi sẵn sàng đánh đổi
- Dời 6 tuần thay vì 5 nếu người dùng muốn A+ (Hóa Tích + cơ chế phụ).
- Gộp Hoa Lộ vào Đạo Hạnh (chỉ còn 1 thứ kiếm được) nếu playtest HK-2 cho thấy người chơi nhầm hai thứ. Cái giá là mất ví cosmetic tiêu được.
- Thẻ C2→3 từ 4 xuống 3 nếu HC-2 trượt (vẫn trong khung 3–5 của người dùng).
- Thứ tự vòng sinh: chấp nhận bất kỳ bản nào WORLD và PROG chốt, miễn HD-2 đạt.
- Linh Quỹ động: đã sẵn sàng cắt ở B/C. Ở A tôi giữ vì nó là chỉ báo sinh thái (H13, cá của SURV-06).

## Câu hỏi cho người dùng (PX gom lại)
1. Chọn **A (dời 5 tuần)**, **B (đúng hạn, đệm 5,5%)** hay **C (đúng hạn, Vũ vào đợt 2 tuần 53–54)**? PX khuyến nghị A, phương án thay thế là C.
2. Di Sản có mất khi đời sau chết giữa chừng không? (PX/PROG/SURV: không · WORLD: có)
3. Rừng riêng (solo) có được tùy chọn "1 lần Hộ Mệnh mỗi đời" không? (PX mặc định: không)
