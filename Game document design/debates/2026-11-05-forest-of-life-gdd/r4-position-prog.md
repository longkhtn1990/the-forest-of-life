# R4 Position — PROG

> Sim mới: `sim/prog_r4_c4_sim.py` → `sim/prog_r4_c4_sim_output.md` (C4, 20.000 lần chết/cảnh, vị trí chết phân bố đều trong cảnh, Mid 64 CT/phiên).

## C1: Số cảnh giới và bộ tên cảnh giới
| Phương án | Fun cho người chơi | Hợp chủ đề | Chiều sâu hệ thống | Khả thi sản xuất | Khác biệt thị trường | Tổng |
|---|---|---|---|---|---|---|
| A. 7 cảnh, 3/2/2, tên theo WORLD Bảng B | 4 | 4 | 4 | 5 | 4 | **21** |
| B. 9 cảnh, 3/3/3 | 3 | 5 | 3 | 2 | 4 | 17 |
| C. 7 cảnh, C5–C6 chia 4 tầng | 4 | 4 | 4 | 4 | 4 | 20 |
| D. 7 cảnh, tên khung theo PROG | 4 | 3 | 4 | 5 | 3 | 19 |

- **Lựa chọn của tôi:** **A.**
- **Lập luận mạnh nhất:** Tổng thời gian của 7 cảnh bằng 9 cảnh (1.661 so với 1.671 CT). Ở Đại Kiếp 56 ngày, 78% Mid chạm Thiên Kiếp. Con số "63% so với 29%" mà WORLD dẫn lấy từ sim F/I, và tôi đã rút các sim đó. Nếu chọn 9 cảnh, mọi thứ nhân theo cảnh tốn thêm 29%, trong khi C7–C8 không mở khả năng mới nào. Phần tên thì WORLD là owner. "Nguyên Anh" là cảnh nguyên thần rời được thân, nên khớp với năng lực Xuất Khiếu mở ở C6. Tên cảnh và tên năng lực không cần trùng nhau.
- **Phương án lai đề xuất:** Lấy nguyên **Bảng B**, gồm cả tên theo loài (Tàng Thực, Ngưng Tâm Mộc…). PROG-02b chỉ còn là bảng ánh xạ `n`. Ở R6 tôi sẽ kiểm tra để không cột loài nào có tên trùng nhau giữa C6 và C7. Ví dụ: nếu C6 của Lang là "Thiên Lang" thì C7 phải là tên khác.
- **Điều kiện để tôi đổi ý:** (1) Telemetry hoặc playtest cho thấy một tầng C5–C6 dài ≥3,5 phiên Mid và retention tụt ngay tại tầng đó. Khi đó tôi chuyển sang **C**: tách tầng, giữ nguyên tổng CT, không phải dựng lại đường cong. (2) WORLD chứng minh được 2 khả năng mới về chất cho 2 cảnh thêm vào, với chi phí ≤ +10% scope. Khi đó tôi chuyển sang B.

## C2: Bộ thuật ngữ cốt lõi
| Phương án | Fun | Chủ đề | Chiều sâu | Khả thi | Khác biệt | Tổng |
|---|---|---|---|---|---|---|
| A. Glossary WORLD R3 toàn bộ | 3 | 5 | 4 | 5 | 4 | **21** |
| B. Đạo Tâm (tiền) / Tâm Hướng (la bàn) | 3 | 3 | 4 | 5 | 3 | 18 |
| C. Đạo Quả (tiền) / Tâm Hướng (la bàn) | 3 | 4 | 4 | 5 | 3 | 19 |

- **Lựa chọn của tôi:** **A.** Tôi đổi lập trường so với R3.
- **Lập luận mạnh nhất:** Phương án A khớp câu brief "giữ một phần linh hồn/đạo tâm" theo đúng hai nửa của nó. Nửa "đạo tâm" là **Đạo Tâm**, tức la bàn hành vi, giữ lại 50% qua luân hồi. Nửa "linh hồn" là **Đạo Quả**, tức tiền meta. Chữ "Quả" cũng hợp chủ đề rừng: quả rụng xuống nuôi kiếp sau. Lý do quyết định là bảng PROG-10c của chính tôi đang dùng "Đại Kiếp" cho hai việc, vừa là đột phá C5→6 vừa là reset server. Đó là lỗi đọc thật. Đổi tên lúc này gần như không tốn gì vì chưa có code.
- **Phương án lai đề xuất:** Áp dụng đổi tên vào mọi spec của PROG: Đạo Tâm Bàn → **Đạo Quả Bàn**, Hộ Thể → **Ấu Linh**, Trung Kiếp (C3→4) → **Phi Thăng Kiếp I**, Đại Kiếp (C5→6) → **Phi Thăng Kiếp II**. Còn lại kiếp C4→C5: đây không phải Phi Thăng, giá 45 CT, dùng template của Phi Thăng Kiếp I. Kiếp này cần một tên, nhờ WORLD đặt (tên tạm: "Hóa Hình Kiếp"). Nó thuộc U1 nên không chặn MVP.
- **Điều kiện để tôi đổi ý:** Test bản địa hóa cho thấy người chơi EN/VN nhầm Đạo Quả với Đạo Tâm (hai tên cùng tiền tố). Khi đó vẫn giữ A, nhưng bắt buộc dùng icon và màu khác hẳn nhau, và UI không bao giờ hiện hai tên này cạnh nhau.

## C3: Lịch thời gian
| Phương án | Fun | Chủ đề | Chiều sâu | Khả thi | Khác biệt | Tổng |
|---|---|---|---|---|---|---|
| A. 20' · mùa 42h · năm 7 ngày | 4 | 5 | 4 | 5 | 4 | **22** |
| B. 20' · mùa 48h · năm 8 ngày | 3 | 4 | 4 | 4 | 3 | 18 |
| C. 24' · mùa 42h · năm 7 ngày | 3 | 4 | 4 | 5 | 3 | 19 |

- **Lựa chọn của tôi:** **A.**
- **Lập luận mạnh nhất:** Chỉ A chia hết trên cả chuỗi. Ngày-rừng 20' cho mùa 42h = 126 ngày-rừng. Một năm-rừng = 1 tuần thực, trùng với lịch sống của người chơi. Kỷ Nguyên 28 ngày = 4 năm, Đại Kiếp 56 ngày = 8 năm. Giờ bắt đầu mỗi mùa trôi 18h, nên người chỉ chơi cố định lúc 21h vẫn gặp đủ 4 mùa trong 1 tuần. B có Kỷ 28 = 3,5 năm, tức Kỷ Nguyên reset giữa năm-rừng và lệch với lịch sự kiện. Tôi đã nhượng 24' từ trước.
- **Phương án lai đề xuất:** Không có. SURV chuyển lịch sự kiện sang năm 7 ngày và tính chu kỳ theo ngày-rừng. `k_s` mùa Đông của tôi không đổi (vẫn 1,0 ±10%).
- **Điều kiện để tôi đổi ý:** SURV chỉ ra được một sự kiện cốt lõi bắt buộc phải có chu kỳ 8 ngày và không xếp vào tuần 7 ngày được mà không chồng lên sự kiện khác. Tôi chưa thấy trường hợp nào như vậy.

## C4: Giá của cái chết (Hậu Duệ và Luân Hồi)
**Sim (phiên Mid; TB / tệ nhất; Luân Hồi tính TB kèm số tuần):**

| Cảnh | Hậu Duệ A (đầu tầng) | Hậu Duệ B (Sơ kỳ, ×1) | **Hậu Duệ C (Sơ kỳ, ×1,5)** | Luân Hồi ×4/×2 | Luân Hồi ×3/×1,5 |
|---|---|---|---|---|---|
| C3 | 0,47 / 1,04 | 1,24 / 2,03 | **0,83 / 1,35** | 1,3 (0,26 tuần) | 1,7 (0,34) |
| C4 | 0,73 / 1,62 | 1,50 / 2,03 | **1,00 / 1,35** | 2,5 (0,49) | 3,3 (0,66) |
| C5 | 0,99 / 2,03 | **1,65** / 2,03 ✗ | **1,10 / 1,35** | **4,1 (0,82)** | 5,5 (**1,10** ✗) |
| C6 | 1,26 / 2,03 | **1,74** / 2,03 ✗ | **1,16 / 1,35** | 6,4 (1,28)* | 8,5 (1,70) ✗ |

Trần của PX: Hậu Duệ trung bình ≤1,5 phiên, tệ nhất ≤3 phiên. Luân Hồi ≤1 tuần. \*Ở C6, Luân Hồi chỉ xảy ra khoảng 12,5% số lần chết (Nguyên Thần), nên chi phí kỳ vọng thấp hơn nhiều.

| Phương án | Fun | Chủ đề | Chiều sâu | Khả thi | Khác biệt | Tổng |
|---|---|---|---|---|---|---|
| A. Về đầu tầng · ×4/×2 | 4 | 3 | 3 | 5 | 3 | 18 |
| B. Về Sơ kỳ ×1 · ×3/×1,5 | 3 | 4 | 3 | 5 | 3 | 18 |
| C. Về Sơ kỳ + Hồi Ức ×1,5 · ×4/×2 | 4 | 5 | 4 | 4 | 4 | **21** |

- **Lựa chọn của tôi:** **C.** Tôi nhượng phương án "về đầu tầng" của mình.
- **Lập luận mạnh nhất:** C là phương án duy nhất đạt trần của PX ở mọi cảnh. Giá Hậu Duệ gần như phẳng, 0,83–1,16 phiên, nên dễ đọc: "chết thì mất khoảng một buổi". Theo phương án A, chết ở C3 chỉ tốn 0,47 phiên, rẻ đúng như SURV đã chỉ ra. B vượt trần trung bình ở C5–C6 (1,65/1,74). Luân Hồi ×3/×1,5 vượt 1 tuần ngay từ C5. Về Sơ kỳ cũng khớp lore của WORLD.
- **Phương án lai đề xuất (bắt buộc kèm theo, có lỗi số liệu trong chính spec của tôi):** PROG-17 viết "Hồi Ức tính là +3 vào Gia Trì, trần ×4". Hiểu theo kiểu cộng như vậy thì Hồi Ức ×4 chỉ còn ra 136 CT/phiên (×2,1), không phải 256. Khi đó Luân Hồi ở C5 tốn **1,38 tuần**, vượt trần (xem phần "Cách hiểu G" trong file output). **Sửa:** *Hồi Ức là hệ số nhân riêng, nằm ngoài trần Gia Trì*: `rate = base × min(GiaTrì, 3) × HồiỨc`. Sửa vậy không mở exploit, vì Hồi Ức tự tắt khi chạm đỉnh cũ (sim T). Oán Linh: tôi nhận **+25%**.
- **Điều kiện để tôi đổi ý:** Telemetry cho thấy dưới 30% số lần chết chọn đổi loài vì Hậu Duệ quá rẻ. Khi đó tôi bỏ ×1,5 (về B ở C3–C4) nhưng giữ ×1,5 cho C5+.

## C5: Thời lượng Ấu Linh
| Phương án | Fun | Chủ đề | Chiều sâu | Khả thi | Khác biệt | Tổng |
|---|---|---|---|---|---|---|
| A. 60' hoặc hết C2 (cái nào đến trước) | 3 | 4 | 3 | 5 | 3 | 18 |
| B. 3h hoặc hết C2 (cái nào đến trước) | 4 | 4 | 3 | 5 | 3 | **19** |
| C. 3h **và** chưa vượt C2 | 3 | 3 | 2 | 4 | 2 | 14 |

- **Lựa chọn của tôi:** **B.** Tôi nhượng PX, vì PX là owner.
- **Lập luận mạnh nhất:** Trên đường cong thật, người chơi hết C2 sau khoảng 90–105' trong rừng chung, cả Mid lẫn Casual (Casual đạt 156 CT sau khoảng 3,7 phiên × 25'). Vì vậy B trên thực tế là "hết C2", còn mốc 3h chỉ là lưới an toàn cho người bị kẹt. A cắt khiên khi người chơi mới đi được khoảng 65% C2, đúng lúc lần chết PvP đầu tiên dễ làm họ bỏ game nhất. C để người C3 vẫn có Ẩn Khí, tức mở đường cho smurf.
- **Phương án lai đề xuất:** Không có. Giữ các luật đi kèm của tôi: chủ động tấn công thì mất Ấu Linh, kẻ đánh nhận 0 thưởng và +2 Nghiệp.
- **Điều kiện để tôi đổi ý:** Telemetry cho thấy hơn 10% thời gian Ấu Linh gắn với kill của đồng đội, tức người được khiên đi do thám hoặc làm mồi. Khi đó hạ trần từ 3h xuống 90'.

## C6: Phần thêm vào MVP
| Phương án | Fun | Chủ đề | Chiều sâu | Khả thi | Khác biệt | Tổng |
|---|---|---|---|---|---|---|
| A. Giữ nguyên PX 44+6 | 3 | 3 | 3 | 5 | 2 | 16 |
| B. + Linh Quỹ + Linh Thức + Kiến | 4 | 4 | 4 | 3 | 4 | 19 |
| C. B + Huyết Nguyệt, Mộ Linh… (lùi 3 tuần) | 4 | 5 | 4 | 1 | 4 | 18 |
| D. + Linh Quỹ + Linh Thức (không Kiến) | 4 | 4 | 4 | 4 | 4 | **20** |

- **Lựa chọn của tôi:** **D**, sửa nhỏ thành D′.
- **Lập luận mạnh nhất:** Câu hỏi sống còn của Vertical Slice là "cây có giữ được ≥50% tester chơi ≥10' không". Linh Thức lite phục vụ thẳng câu hỏi đó: cây là loài bất động, và 30 s tách camera khỏi thân là động từ riêng duy nhất của cây đủ sức lên trailer. Linh Quỹ lite biến câu chủ đề "kẻ mạnh ở lâu làm rừng đói" thành luật, với chi phí S (chỉ là một hệ số trong PROG-03b). Kiến thì cần một controller mới, tốn 2 tuần và mang rủi ro AI. Ở MVP, phần cộng sinh đã có Quả Ước (cộng sinh giữa người với người).
- **Phương án lai đề xuất (D′):** Giữ **4 mùa**, vì lịch ở C3 dựng trên 4 × 42h và đổi palette mùa rất rẻ. Bù ngân sách bằng hai việc: Kế Hoạch Sinh Trưởng chỉ còn "Tán mọc lại" (khoảng −1 tuần), và Đạo Quả Bàn giảm từ 6 xuống 4 node (−0,25 tuần). Thêm vào: Linh Thức lite khoảng 1–2 tuần (dùng lại camera Thần Thức), Linh Quỹ lite khoảng 0,5 tuần. Tuần đệm còn khoảng 4,5–5 (≈9%). Kiến là mục đầu tiên của U1. Lưu ý kèm theo: MVP chỉ có C1–C4, nên Mid chạm trần khoảng ngày 15–19 của Kỷ 28 (691 CT). Sau khi chạm trần, vòng chơi là luân hồi đổi loài. Tôi sẽ chạy lại dòng MVP của PROG-16 với trần C4 trước R6.
- **Điều kiện để tôi đổi ý:** (1) Spike cho thấy Linh Thức lite tốn ≥2,5 tuần, hoặc sau closed alpha đệm còn dưới 4 tuần. Khi đó cắt Linh Thức trước, như tôi đã cam kết ở R3. (2) VS cho thấy cây giữ ≥60% tester mà không cần Linh Thức. Khi đó tôi chọn A + Linh Quỹ.

---

## Phản đối / ghi chú với bảng "orchestrator tự giải quyết"
| Điểm | Ý kiến PROG |
|---|---|
| Vệt Nắng theo SURV | **Đồng ý.** Kiểm tra: 8 s × (2,5−1) / 50 s = +24%, nên Vệt Nắng chiếm 19,4% thu nhập, trùng mục tiêu 20%. `k_s` của Linh Mộc không cần chỉnh quá ±10%. |
| Khô Linh 2h theo SURV | **Đồng ý.** Ghi chú: sim U cũ ra 2,8 ngày-rừng × 20' = 56' thực. Tôi sẽ giảm khoảng 50% tải mỗi thú săn lên quỹ trong sim U để khớp mốc 2h, và gửi lại trước R6. |
| Thiên Phạt ở 5 Nghiệp | Đồng ý. |
| Thiên Kiếp thất bại do sét | Đồng ý ghi vào Câu hỏi mở. Đây là tính năng [Post]. |
| Linh Thử chơi được ở MVP | Đồng ý. |
| Thiên Kiếp luôn Công | Đây là lập trường của tôi. Không có dissent. |
| **Bổ sung (số liệu, không phải phản đối):** Hồi Ức nằm ngoài trần Gia Trì (xem C4). FINAL phải ghi đúng công thức này, nếu không mọi con số Luân Hồi trong PROG-10c/16 sẽ sai khoảng 1,7 lần. | **Bắt buộc.** |
