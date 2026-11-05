# R2 Critique — SURV

Phán quyết nhanh theo 6 điểm lệch (chi tiết ở các mục dưới).

| Điểm lệch | Bản tốt nhất | Vì sao (góc sinh tồn) |
|---|---|---|
| (a) Thú | **Lang** (WORLD/PX) | Năm vai phải tách nhau. "Cơ động + trữ" của Linh Thử chồng lên kho của Mộc và cơ động của Vũ. Lang là vai duy nhất "săn + burst" nên tạo áp lực. |
| (a) Thủy | **Oa, bắt đầu từ Nòng Nọc** (WORLD/PX). Lý (PROG) là Post | Cá thuần túy bị nhốt trong 6–8% map. Nòng Nọc (C1, cá-giống, ở nước) chuyển thành Ếch (C2, lên bờ) vẫn thỏa "cá và loài nước ngọt". |
| (a) Vũ | **Kê/gà rừng** (WORLD) có điều kiện | Chim sẻ cần Vỗ Cánh 5 ô, CD 10s, miễn phí, nên gần như một nút thoát thân. Sải Cánh của Kê (60 Thể Lực, CD 20s, không né) có chi phí thật. |
| (a) Trùng | **Kiến, mô hình Hậu + Lính** (PROG), có trần | Lính là đơn vị đọc được. "Bầy VFX" của PX không có luật tiêu hao. |
| (b) Thứ tự vòng | **Thủy→Mộc→Thú→Trùng→Vũ→Thủy** (WORLD = PX) | Khớp Quả Ước, chuỗi xác→Trùng, chim ăn sâu. Hành: Thú = Hỏa, Trùng = Thổ (WORLD). Chi tiết ở §D. |
| (c) NPC | Chưa chốt. Lão Quy hợp mẫu "Lão Tùng" hơn | "Ngao" trong tiếng Việt thường chỉ con ngao (nhuyễn thể), không chỉ rùa. WORLD cần xem lại. |
| (d) FTUE | **Chuột Tiền Thân** (PX) | Đã thiết kế sẵn (diều hâu, đói, mang hạt). Kiến mang hạt buộc làm lại một mạch 25 phút. |
| (e) Độ sâu | C2 kỹ năng + cổng C3 dùng chung template Kiếp (xem §E) | Giữ nhịp đỉnh của vòng sống còn mà không tốn thêm +0,75. |
| (f) Ngân sách | Không bản nào chuẩn. Ước của tôi +2,0 đến +3,0 (xem §F) | Đơn giá mỗi loài lệch nhau 2–3 lần. |

---

## Về PROG
### Giữ lại (Keep)
- PROG-03: vòng Hành ghép đúng Ngũ Hành, kèm số liệu đo được cho mỗi cặp. Đây là bản chặt nhất về mặt cấu trúc.
- PROG-06: bảng nước nông/sâu cùng con số diện tích (6–8% map = 3.900–5.200 ô). Ranh giới nước/cạn có số cụ thể.
- PROG-05: cổng cuối bản lite, đổi CT dư thành Đạo Quả. Tránh cảm giác "cụt" khi chạm trần.
- PROG-02: mô phỏng nguồn tu vi (CV 19–28%) chứng minh nguồn CT cho tộc lite không lệch.
### Mượn (Steal)
- Mô hình Hậu + Lính cho Trùng (PROG-01), kèm công thức công hiệu dụng 22 × (1 + 0,25·Lính). Tôi thêm trần ở bên dưới.
- Bách Thảo (Mộc, Huyết Mạch) thay Linh Thảo. Rẻ nhất trong 3 cách xử lý cỏ: WORLD giữ loài riêng [1.0], PX dời sang [Post]. Cỏ thành một nhánh của Linh Mộc, không cần loài mới.
### Phản biện (Challenge)
| ID | Mức | Vấn đề | Tình huống | Đề xuất / kiểm chứng |
|---|---|---|---|---|
| PROG-01 (Nghĩ) | **Major** | Công ×(1+0,25×3) = **×1,75**, gần bằng một cảnh (×1,77) cho Hậu có 3 Lính. Lính 40 HP là máu đệm thêm 120. Trùng gần như "thăng một cảnh miễn phí". | Nghĩ C3 gặp Lang C3: 22×1,75 = 38,5 Công, tổng HP 420 so với 360. Nghĩ thắng ngay nếu không có AoE. | Lính cần chi phí sống: mỗi Lính tốn −1 No/90s hoặc hồi sinh 20s với 8 No. Công thức mới: ×(1 + 0,25×Lính) nhưng trần ×1,5 khi chỉ có Lính. Kiểm chứng bằng sim 1v1 trên 5 tộc, mục tiêu thắng 40–60%. |
| PROG-01 (Lý) | **Major** | Thủy vào nước sâu thì miễn nhiễm cả Thú (PROG-06) và nguồn chính 45% (tảo, ấu trùng, xác chìm) cũng nằm ở nước. Lý có thể ở trong đó cả phiên, an toàn và vẫn đủ ăn. | Lý C3 ngồi giữa Đầm. Lang không vào được, bầy không vào được. Chỉ Tước còn mổ được. Người kia phải bỏ cuộc, không phải thua. | Nước sâu chỉ là **bể ẩn**, không phải lãnh thổ: trong nước sâu nguồn CT chính chỉ 60% (hết dư), Tước và Diều hâu AI tấn công được. Thêm 1 điểm hỏng: nước mưa mùa Hạ cạn ô rìa (PROG-03 đã có "ao trong 6 ô rễ không cạn"). |
| PROG-01 (Lý) | **Major** | Lý (cá) bị nhốt trong 6–8% map. Spawn C1 ở Bìa Rừng là vũng nông, nơi Thú săn ×1,25. | Người chơi Thủy mới sinh ra, đứng trong vũng cạn 3×3, Lang AI ập vào, không có chỗ ẩn. Dễ bỏ game. | Dùng Oa (đã là fallback của PROG). Thủy C1 = Nòng Nọc có 1 hồ con sâu 3×3 ở Bìa (Hang tương đương). Lý để lại Post với lore Vũ Môn. |
| PROG-03 | **Major** | E dùng Hành của Huyết Mạch sau C3, nên Lý chọn Kim Lân thì không còn "Thủy". Ma trận tộc đổi theo nhánh. | Người chơi đọc ma trận "Thủy khắc Trùng", đến C3 chọn Huyết Mạch Kim thì quan hệ biến mất mà không báo. | Tách hai tầng: **ma trận tộc** cố định (hệ số 1,15, mục WORLD) và **E Huyết Mạch** (1,25). Lấy giá trị lớn hơn, không cộng. Giữ trần ×1,32. |
| PROG-01 (Thú) | **Minor** | Linh Thử không có vai sát thương. Sau khi Lang thành AI, tộc "kẻ săn" duy nhất là AI. | Người chơi thích PvP không có nhân vật tộc Thú để chọn. | Xem điểm (a): chọn Lang. Linh Thử vẫn có mặt như AI + FTUE. |
### Câu hỏi cho PROG
1. Lính có dùng chung bảng Thể Lực/No của Hậu hay có bảng riêng (HUD 4+1 PROG nhắc)?
2. Nghĩ lite C3 có được thành hai Hậu (Yêu Nghĩ) trước khi cổng đóng, hay chỉ ở C4?

---

## Về WORLD
### Giữ lại (Keep)
- WORLD-01: nước là bể chứa nhớ, và S2 sửa thành "đất/nước". Là lời giải lore tốt nhất cho câu "vì sao Thủy giữ luân hồi".
- WORLD-03: dòng Linh Tuyền từ Linh Nhãn ra Bìa; "ngược dòng = vào trong". Làm breadcrumb, thay cho minimap. Ba bến cạn là điểm nghẽn PvP có chủ đích.
- WORLD-04: nấm là "da của Linh Mạch", không có Mộng Hỏa. Giải quyết trọn vẹn câu hỏi 1 của brief.
- WORLD-06: luật cân bằng "tộc-khắc ≤×1,15, lấy giá trị lớn hơn, không cộng". Luật tốt nhất trong 3 bản. Khắc chủ yếu là **cơ chế** (chặn, đục, kéo).
### Mượn (Steal)
- Vòng sinh/khắc theo thứ tự của WORLD, và Hành Thú = Hỏa, Trùng = Thổ. Cả hai đều đúng Ngũ Hành, và hợp với Huyết Lang (Hỏa) cùng "đất của xác" của Trùng.
- Tên cảnh giới Nòng Nọc, Rụng Đuôi, Thượng Ngạn. Vòng đời lột xác sẵn có là cơ chế "lên bờ" tự nhiên.
- Kê ghé ao thì cá +1/ngày, "Dẫn Nước" của Oa. Đây là cộng sinh có chi phí thật cho người chơi.
### Phản biện (Challenge)
| ID | Mức | Vấn đề | Tình huống | Đề xuất / kiểm chứng |
|---|---|---|---|---|
| WORLD-03 | **Major** | Nước sâu duy nhất ở Đầm Mục, nằm Thâm Lâm, vòng nguy hiểm nhất. Người chơi Thủy mới sinh ở đâu? | Oa C1 spawn ở Bìa Rừng, không có nước sâu; hoặc spawn ở Thâm Lâm và bị thú dữ nuốt. | Thêm 1 **Hồ Con** (3×3 sâu) ở cửa suối Bìa Rừng làm điểm ẩn C1–C2. Ngân sách: tile, không asset. |
| WORLD-03 | **Major** | Tốc nước nông: WORLD ×0,75 cho mọi tộc; PROG ×0,6 cho loài cạn; PX ×0,8 cho Thú và ×1,3 cho Thủy. Ba con số cho một luật địa hình. | Cùng một suối, tester Lang thấy chậm kiểu này, tester Oa thấy nhanh kiểu kia. Không đọc được vì sao chết. | **Bảng địa hình do SURV chốt** (xem cuối file). |
| WORLD-05 | **Major** | Oa "Quăng Lưỡi" (kéo/chậm 1s, CD 12s) là một động từ mới. PX cũng cam kết "không thêm động từ". Kéo trong PvP top-down trên mobile còn gây vấn đề hit detection. | Oa kéo Lang vào nước sâu 1s; client trễ 150ms hiển thị kéo giật. Lang chết hoặc người chơi chê lag. | Đổi sang **làm chậm 1s + đục bờ** (tái dùng cơ chế "đục"), không kéo. Kéo hoãn tới U1 sau khi có netcode test. |
| WORLD-06 (Kê) | **Minor** | Kê chỉ C2 với Sải Cánh 60 Thể Lực là số tốt, nhưng thế mạnh "Mắt" +30% Thần Thức không đủ khác Lang (burst) về cảm giác. | Người chơi chạm Kê 10 phút chỉ thấy "gà chạy chậm, nhìn xa hơn". | Thế mạnh phải chơi được từ C1: ping 1 chạm lên party (có số: 20 ô, 8s). Test HN9 của PX. |
| WORLD-05 (FTUE) | **Major** | Kiến mang hạt thay chuột: toàn bộ mạch FTUE (diều hâu ↔ chuột 300 HP, đói đầu tiên ~10 phút) đã tinh chỉnh cho chuột. Đổi sang kiến buộc đo lại TTK, đói, kịch bản chết. | Kiến 1 HP-thấp bị diều hâu một đòn: FTUE kết thúc nhanh hoặc cần nới mạch. | Giữ chuột (fallback B của chính WORLD). Chi phí +0,5 là có thật nhưng thấp hơn làm lại mạch. |
### Câu hỏi cho WORLD
1. Tên "Cụ Ngao": người đọc Việt hiểu "ngao" là con nghêu/ngao. Muốn là rùa thì "Lão Quy" gọn hơn (cùng mẫu "Lão Tùng"). Nếu ngại trùng "Quy Căn", đổi Quy Căn? Hoặc chấp nhận Cụ Ngao là **ngao có ngọc**, ngọc là ký ức, và ý này còn mạnh hơn rùa. Chọn cái nào?
2. Triều Mộng (WORLD) hay Mưa Vong (PX) cho E7? Tôi nghiêng Mưa Vong về cơ chế (dùng hệ mưa có sẵn) và tên Triều Mộng về lore.

---

## Về PX
### Giữ lại (Keep)
- PX-04: fallback có cổng (tuần 16 / 30) và nguyên tắc "không bao giờ cắt ≥4/5 tộc chơi được". Đúng kỷ luật.
- PX-11 HN3, HN6, HN8: ngưỡng thắng PvP ≤35%, tử vong trên ô nước ≤1,3× trung bình. Ba giả thuyết kiểm chứng đúng điểm yếu của hệ này.
- PX-05: Ao Sương lúc bình minh mở Mộng Ấn 1 thay vòng nấm tiên, chi phí 0.
- PX-02: vai độc quyền của Trùng (duy nhất phá Tâm Rễ) tạo nhu cầu phối hợp thật giữa các tộc.
### Mượn (Steal)
- Căn Thương chuyển cho Trùng: 0,5%/s mỗi Nghĩ, tối đa 3 (1,5%/s). Cần thiết vì Độn Thử bị cắt, nếu không Tâm Rễ không còn đòn nào để chết ngoài lửa/hạn/sét.
- Luật "Linh Thử AI thay vai đối tác Quả Ước". Giữ nguyên phần Mộc/Thú cộng sinh.
### Phản biện (Challenge)
| ID | Mức | Vấn đề | Tình huống | Đề xuất / kiểm chứng |
|---|---|---|---|---|
| PX-04 | **Major** | Ngân sách thiếu nhất quán đơn vị. PROG đã nêu Lang đầy đủ ≈ −2,0 tuần-người (6 kỹ năng, 14 node, 1 sprite) = khoảng 0,33 mỗi kỹ năng. PX cho 3 tộc lite **cả loài** chỉ 0,5–0,6 mỗi loài (2 kỹ năng + sprite + HUD) = thấp hơn đơn giá đó. | Cuối tuần 30 trễ 2 tuần vì 3 loài lite thực tế 1,0–1,2/loài. | Dùng đơn giá chung: lite C2 ≈ 1,2/loài (2×0,33 + sprite 0,3 + HUD/AI 0,2). Xem §F. |
| PX-01 | **Major** | Lite C1–C2 + "Con đường chưa mở" ở C2 Hậu: người chơi chạm trần sau ~2–3 phiên, sống phần còn lại như khách. Ma trận tộc (hệ số 1,15) chỉ có ý nghĩa trong cùng cảnh (cảnh khác nhau ×1,77), nên nếu Thủy/Vũ/Trùng luôn ở C1–C2 thì ma trận hầu như không bao giờ hiện ra trong PvP. | Oa C2 gặp Lang C4: 1,15 không cứu được ×1,77. Cả ma trận trở thành trang trí. | Cổng C3 (xem §E) và **band PvP theo cảnh** (đã có trong FINAL) đảm bảo lite gặp lite. Đặt HN5/HN6 đo trong cùng band. |
| PX-02 | **Major** | Oa "tốc ×1,3 và hồi 1,5% HP/5s trong nước nông" làm Thủy tự cân bằng trong 6–8% map, nhưng không có vai **hỗ trợ party**. Mộc cũng có "ở lại chỗ và hồi". Thủy chồng vai Mộc. | Hai người Mộc + Oa ở suối: Oa hồi bản thân, chẳng cho ai. | Thêm 1 hiệu ứng cho đồng minh: Dẫn Nước +6 Thủy/phút (WORLD), cộng hồi 0,5%HP/5s cho đồng minh trong 3 ô. Thủy = **hồi động**, Mộc = **neo tĩnh**. |
| PX-03 | **Minor** | Chỉ 3 cặp có cộng sinh thật, 7 cặp "chỉ hệ số". Ma trận trông giàu hơn thực tế. | Người chơi đọc 5×5 rồi không thấy khác biệt ở 7 cặp. | Mỗi tộc đủ 1 hiệu ứng **cơ chế** (không phải hệ số) ở MVP: 5 cặp sinh có hiệu ứng nuôi (No/Thủy/Thể Lực), 5 cặp khắc chỉ cần 1 cơ chế nhỏ. Dạng data, +0,1. |
| PX-06 | **Minor** | Kê "không bay" nhưng PX-02 cho Phi Lược vượt bụi/hang 3 ô và PX-06 hứa Ưng bay thật. Hai thứ cùng tên "Phi/bay" dễ gây kỳ vọng sai trên store. | Review "game có bay mà không bay được". | Gọi "Nhảy" / "Sải Cánh" ở MVP, "bay" chỉ trong Post. |
### Câu hỏi cho PX
1. Với Lang đầy đủ + Linh Thử FTUE/AI: chi phí "Linh Thử AI + Hạt Quên" đã tính chưa?
2. Có chấp nhận chuyển Hóa Hình Mộng sang U1 không? Đây là chỗ tôi không phản đối: nó không nằm trong vòng sinh tồn.

---

## A. Ma trận nào còn tộc thống trị / tộc không có thế mạnh
Cả ba bản đều có cấu trúc vòng đối xứng (mỗi tộc có 1 nguồn sinh, 1 đích sinh, 1 con mồi khắc, 1 kẻ khắc). Đối xứng cấu trúc không đủ. Thống trị đến từ vai (role), không từ vòng.

| Bản | Nguy cơ thống trị | Tộc yếu vai |
|---|---|---|
| PROG | **Trùng**: ×1,75 Công, Mộc nuôi, khắc Vũ, chỉ bị Thủy khắc ở ven bờ. **Thủy**: nước sâu miễn nhiễm. | **Thú (Linh Thử)**: không burst, bị Mộc khắc, chỉ khắc Thủy ở nước nông (nơi Lý hiếm khi ở). Vai "trữ + cơ động" trùng Mộc và Vũ. |
| WORLD | **Thủy (Oa)**: nước sâu chặn Lang, kéo, ẩn/hồi, tưới +6 Thủy/phút cho cây. Khắc cả Thú lẫn nuôi Mộc. | **Mộc** (nếu Thủy lấy mất "nuôi/Linh Quỹ"). Mộc cần 1 vai không ai chạm: ô rễ + Mộng Báo + bất tử offline. |
| PX | Không bản nào thống trị, vì mọi hệ số ≤1,15. | **Thủy** thiếu vai hỗ trợ đồng minh; **Vũ** chủ yếu thông tin, không có cơ chế đòn riêng. |

Ghi chú: ma trận PROG chặt về cấu trúc nhưng đặt Thú = Thổ, Trùng = Hỏa. Nếu Lang là đại diện (Huyết Lang = Hỏa trong FINAL §6.4) thì ánh xạ Hành của WORLD khớp dữ liệu có sẵn hơn.

## B. Bảng địa hình nước (SURV chốt, thay 3 con số lệch nhau)
| Ô | Thủy tộc | Loài cạn | Vũ | Ghi chú |
|---|---|---|---|---|
| Cạn | Oa Tốc ×1,0 (Ẩm giảm, xem dưới) | ×1,0 | ×1,0 | Hồ Con và Đầm là ngoại lệ |
| Nước nông | Tốc ×1,2, hồi 1%HP/5s | **×0,8** | ×1,0 | Xóa mùi/vệt máu (WORLD). Thủy của cây tính 3× (FINAL §5.4) |
| Nước sâu | Ẩn (như Hang), hồi 1%HP/5s | **Chặn** | Bay qua bằng Sải Cánh/Nhảy, không dừng | CT chính 60% khi ở sâu, Diều hâu AI vẫn tấn công |
| Hồ Con (3×3 sâu, Bìa) | Hang C1–C2 | Chặn | Như trên | Chống spawn-camp |

**Ẩm** (chỉ hiện khi Oa ở trên cạn): 100 → 0 trong **10 phút** (−1/6s); 0 thì −1% HP/5s. Tái dùng slot thanh Thủy của cây. Không thêm thanh mới. Nếu playtest thấy phiền, bỏ Ẩm và giữ ràng buộc bằng Tốc, không bằng thanh.

## C. Vai nhân vật và Needs của tộc lite (tối đa 3 thanh, không thêm)
| Tộc | Thanh hiển thị | Ghi chú |
|---|---|---|
| Nghĩ | HP, No, Thể Lực (+ số Lính) | Lính tốn No (xem Major ở PROG) |
| Oa | HP, No, Thể Lực (+ Ẩm khi trên cạn) | Ẩm thay Thủy của cây |
| Kê | HP, No, Thể Lực | Sải Cánh tốn 60 Thể Lực làm đường cong rủi ro |

## D. Về thứ tự vòng tương sinh (b), chọn WORLD/PX
Lý do: (1) Mộc→Thú giữ Quả Ước làm "sinh" thay vì ngoại lệ; (2) Thú→Trùng khớp chuỗi xác → dọn xác (Trùng giữ vai phân giải của Khuẩn cũ); (3) Trùng→Vũ khớp "chim ăn sâu"; (4) Mộc⊣Trùng biến thành **quyết định** (nuôi kiến khế ước hay đuổi bầy), một lựa chọn cộng sinh/khắc thật. Khuyết điểm: Vũ→Thủy yếu về logic ở cả hai bản. Gợi ý: Vũ→Thủy là "mưa/sương" (Kê gáy bình minh +15 Thủy trong 8 ô, WORLD-06) thay vì ping.
Việc còn thiếu: không bản nào ghi **ma trận "ai ăn ai" §4.5** cho Nghĩ/Oa/Kê (chỉ PROG nhắc). Cần thêm 3 hàng, chiều ăn khác với chiều sinh/khắc.

## E. Độ sâu 3 tộc mới (e)
Tôi chọn **kỹ năng C2 (2 Bản Năng + 1 nét "vai" ở C1) + cổng C3 qua template Kiếp dùng chung**. Lý do: vòng sống còn có ba đỉnh: đói (C1), lãnh thổ/đêm (C2), độ kiếp (C3). Dừng ở C2 thì tộc lite không bao giờ thấy đỉnh thứ ba, trong khi "độ kiếp C3" nằm trong danh sách không-cắt của PX. Giá: skin Kiếp (PROG đã tính cho Lý), không thêm kỹ năng. Nếu Vertical Slice trễ >1 tuần: hạ về C2 thuần (PX).

## F. Ngân sách (f)
Đơn vị chung (từ −2,0 của PROG cho Lang đầy đủ): lite C2 ≈ **1,2/loài**; ×3 = 3,6. Cộng nước 0,5 (tile + luật, không asset), ma trận 0,4, QA/sim 0,3 = **4,8**. Bù: Lang giữ (0), Linh Thử full → FTUE+AI −1,2, Hóa Hình Mộng −0,25, palette/shop −0,4, pool Trung Ấm −0,1, Huyết Mạch tộc lite 1 nhánh −0,5 = **−2,45**. Ròng ≈ **+2,35**, đệm còn ~1,9 (≈4%). Giữa ước của WORLD (+0,7) và PROG (+3,5). Đây là ước lượng của tôi, không phải số đã kiểm; PX chốt.

## Xung đột liên domain phát hiện được
| Xung đột | ID | Lập trường của tôi | Gợi ý |
|---|---|---|---|
| Đại diện Thú / Thủy | PROG-01, WORLD-05, PX-01 | Lang + Oa (Nòng Nọc). Thử và Lý là Post/AI | Giữ chuột FTUE-only |
| Hệ số tộc vs E Huyết Mạch | PROG-03, WORLD-06, PX-03 | Hai tầng, lấy giá trị lớn, trần ×1,32 | Ma trận tộc cố định |
| Tốc nước nông | PROG-06, WORLD-03, PX-02 | Một bảng (§B) | SURV chốt |
| Căn Thương thuộc ai | PX-02, FINAL §5.4 | Trùng (0,5%/s/Nghĩ, max 3) + lửa/hạn/sét/rễ | Lang chỉ đưa Tán/Thân đến Đổ |
| Độ sâu lite và ngân sách | PROG-05, PX-04, WORLD §5 | C2 kỹ năng + cổng C3 chung template; ròng +2,35 | Cổng tuần 16/30 của PX |
| Cỏ trong Mộc | PROG-05, WORLD-07, PX-07 | Bách Thảo là Huyết Mạch [1.0] | Linh Thảo item giữ nguyên tên nếu chưa nhầm |
| NPC và E7 | WORLD-02, PX-05, WORLD-04 | Lão Quy hoặc Cụ Ngao-ngọc; Mưa Vong cơ chế | WORLD chốt |

## Top 3 điều team phải chốt
1. **Thú = Lang, Thủy = Oa (Nòng Nọc→Ếch), Trùng = Kiến Hậu+Lính có chi phí No, Vũ = Kê**; vòng sinh theo WORLD/PX, ma trận hai tầng.
2. **Bảng địa hình nước + Hồ Con + nước sâu không phải lãnh thổ** (§B), và Căn Thương chuyển cho Trùng.
3. **Độ sâu lite và ngân sách**: C2 kỹ năng + cổng C3; ước +2,35, đệm ~4%; cổng tuần 16/30 và "đợt 2" cho Vũ.
(Sau Bổ sung 2 và 3, danh sách chốt đầy đủ ở cuối mục dưới: thêm "chết = mất trắng" và "chất riêng mỗi tộc".)

---

## Hệ quả của Bổ sung 2 với domain của tôi (SURV)

Các mục trên (B, E, F) viết trước Bổ sung 2. Chỗ nào xung đột thì mục này thắng. Hai chỗ phải sửa: "quy đổi CT dư thành Đạo Quả" (PROG-05) và "Hồi Ức ×4" (PX-01) không còn hợp lệ khi Đạo Quả/Túc Tuệ không mua sức mạnh. Cổng cuối của tộc lite nay là **điểm hoàn thành (F)**, không phải ngõ cụt.

### E. Chết = mất trắng: thiết kế để "đủ đau, không đủ đau để bỏ game"
Nguyên tắc: chi phí chết đo bằng **phút chơi bị mất**. Bản chưa có số về độ dài một đời nên tôi đặt ngưỡng, PROG đo lại: tại bất kỳ thời điểm nào, chi phí chết kỳ vọng **≤ 40 phút** ở C1–C2, **≤ 90 phút** ở C3+ (nếu đời dài hơn, phải có lớp bảo vệ dưới đây). Không có lớp bảo vệ thì C3 trở đi là Frostpunk: một lần xui mất 3 giờ.

| ID | Quy tắc | Số liệu | Lý do |
|---|---|---|---|
| SURV-R2-01 | **Độ kiếp thất bại không phải chết.** Thất bại = lùi về đầu cảnh, mất lựa chọn của mốc đó, CD thử lại 10'. Chỉ HP/Tâm Rễ = 0 mới là chết | Kiếp lặp tối đa 3 lần/đời, lần 3 thất bại thì Hấp Hối (SURV-R2-02) | Kiếp là đỉnh căng báo trước, không phải cái bẫy. Người chơi phải hiểu vì sao thất bại |
| SURV-R2-02 | **Trọng Thương** (C3+): đòn kết liễu do **người chơi** gây ra đưa nhân vật vào Trọng Thương 30s thay vì chết ngay, tương tự Mộc Tàn của cây. Đồng minh cứu (giữ 3s) hoặc kẻ địch bồi thêm 1 đòn mới chết. AI/đói/thời tiết giết thẳng | Mỗi nhân vật 1 lần Trọng Thương/5 phút | Giảm gank "một nhát mất 3 giờ". Kẻ gank vẫn phải bồi đòn, có lộ vị |
| SURV-R2-03 | **Chống bắt nạt theo cảnh**: kẻ cảnh cao hơn ≥2 cảnh giết người cảnh thấp bị 0 CT từ xác, hiện cờ Sát Nghiệp (đã có Nghiệp trong Trung Ấm). Ấu Linh giữ C1–C2 | CT từ xác kẻ thấp hơn 2 cảnh: ×0, hơn 1 cảnh: ×0,5 | Đền bù cho "không còn Hậu Duệ". Thiên Đạo Luật một mình là chưa đủ |
| SURV-R2-04 | **Tốc độ khởi động lại**: đời mới có lựa chọn đầu tiên trong **≤5 phút** (không FTUE lần 2). Chọn lại tộc (kể cả cùng tộc), spawn ở rìa an toàn | Mốc 1 ≤5', mốc 2 ≤20' | Chết phải dẫn tới một vòng "tension→release" mới nhanh, tránh death spiral |
| SURV-R2-05 | **Cây offline bất tử giữ nguyên** (Thân/Tâm Rễ bất tử, tổn thất ≤20% Tán/24h). Chết chỉ xảy ra khi online. Chết do đói/hạn chỉ khi cây ở trạng thái hoạt động | — | Cây offline bất tử + mất trắng online: nếu không giữ, Mộc không dám tắt máy |
| SURV-R2-06 | **Sinh Năng và Trung Ấm** giữ: xác vẫn nuôi rừng (Sổ Sinh Năng), Trung Ấm 45s hiện **cái chết đọc được** (nguồn, vì sao, 1 câu NPC) và **tên lựa chọn đã bỏ lại** (Biên Niên/Mộ Linh). Cái chết trả lại cho rừng, không cho người | Cộng Sinh Năng Đất theo cảnh | Giữ ý "cái chết là hạt giống" (P3) mà không mang sức mạnh |

Ba cảnh báo: (1) Vũ (240 HP) và Oa chết nhiều nhất trong PvP. Chấp nhận khác nhau, nhưng mục tiêu **tỉ lệ chết/giờ chênh ≤25% giữa các tộc** (đo ở HN6). (2) Nếu Đạo Quả không còn mua sức mạnh, mục tiêu retention chuyển sang di sản (F) và mở khóa ngang (loài, skin, Biên Niên). (3) Cổng tuần 16: đo "tỉ lệ bỏ game sau lần chết đầu ≥C3" ≤15%; nếu cao hơn thì nâng SURV-R2-02 thành mọi nguyên nhân.

### D. 3–5 lựa chọn mỗi mốc, kế thừa, còn hiệu quả đến hết đời
Góc sinh tồn của tôi:
- **Mỗi bộ lựa chọn có ít nhất 1 lựa chọn "sống sót"** (thoát thân, hồi, chịu đói/khát, ẩn) và 1 lựa chọn "vai" (khuếch đại thế mạnh tộc). Không có bộ toàn sát thương: người chơi "đang sợ mất gì" phải có đáp án ở mọi mốc.
- **Còn hiệu quả đến hết đời** = hiệu ứng dạng **% theo trục sống còn** (No tiêu hao, hồi, Tốc, tầm nhìn, số Lính, mật độ rễ), không phải số cứng. PROG chốt công thức.
- **MVP tối thiểu mỗi nhân vật:** Mộc/Lang 4 mốc × 3–4 lựa chọn; tộc lite 2 mốc × 3 lựa chọn = 6 (khớp ngân sách 2 Bản Năng). Hiển thị 3 thẻ ở C1–C2, 4–5 ở C3+ để tránh choice paralysis trên mobile.
- Bất đồng với đề xuất "random 3 từ pool lớn": ở mốc đột phá, pool **cố định theo tộc + nhánh đã chọn** (đọc được), chỉ random ở F (di sản).

### F. Di sản
| Câu hỏi | Đề xuất SURV |
|---|---|
| "Giai đoạn cuối" MVP | Tộc lite: chạm cổng C3 Hậu (xem §E trên). Mộc/Lang: C4 Hậu. Hoàn thành = Phi Thăng nhẹ: nhân vật thành **Mộ Linh/NPC** trên map (kỷ niệm), không còn điều khiển |
| Slot | **1 slot, thay thế** (không cộng dồn). Chọn mới thì bỏ cũ. Tránh snowball khi đã "bắt đầu hoàn toàn mới" |
| Độ mạnh | Theo cảnh hoàn thành: lite (C3) = bậc 1 (≤+5% hoặc side-grade tiện ích), C4 = bậc 2 (≤+8%). Chống farm tộc lite để lấy di sản cho Mộc |
| Đổi tộc | Dịch theo **tag trục sống còn**: Hộ / Sát / Sinh / Hợp (đã có ở Huyết Mạch). Ví dụ "Sinh": Mộc → hồi Thủy; Lang → hồi sau ăn xác; Oa → hồi nước nông. Mỗi tộc có 1 dòng dịch cho mỗi tag (4 dòng × 5 tộc = 20 dòng data) |
| Chết giữa chừng | **Di sản không mất.** Chỉ được chọn khi hoàn thành, nếu mất thì phạt kép sau khi đã mất trắng |
| Mô hình PvP | Di sản ≤ trần ×1,32 chung (không cộng với Hành) |

### Câu hỏi cho team
1. PROG: một đời C1→C4 dài bao nhiêu phút trung vị? Không có con số, ngưỡng "40/90 phút" của tôi không kiểm chứng được.
2. WORLD: Mộ Linh có thể là điểm tương tác (đặt hoa, đọc Biên Niên) thay cho Hậu Duệ?
3. PX: mất Đạo Quả meta nghĩa là mất "tiền mềm" cho Pass/loài; nguồn nào thay?

---

## Hệ quả của Bổ sung 3 (G): chất riêng của mỗi tộc

Khung chung (chiếm đại đa số code/UI): HUD 4+1, needs (HP, No, Thể Lực, +1 theo tộc), cảnh giới, thẻ lựa chọn mỗi mốc, Trung Ấm, Sinh Năng. Phần riêng: 1 cơ chế bắt buộc + 1 tùy chọn, mỗi tộc có **nhịp** khác nhau. Ràng buộc: thuần dữ liệu và tái dùng hệ thống sẵn có.

| Tộc | Cơ chế riêng (bắt buộc) | Cơ chế riêng (tùy chọn, hoãn nếu hết ngân sách) | Nhịp một phiên | Chi phí ước |
|---|---|---|---|---|
| Mộc | **Lan Rễ + Quả Ước** (đã có) | — | Chậm, lập kế hoạch, đêm là hạn | 0 |
| Thú (Lang) | **Đánh Hơi**: thấy vệt máu/xác trong 12 ô, nước xóa vệt (WORLD-03) | Tha Mồi: ăn xác tươi trong 5s đầu cho +No | Rình rồi lao, nghỉ dài | 0,15 |
| Trùng (Nghĩ) | **Bầy**: quản lý Lính (tiêu hao No, sửa trần ×1,5 ở Major trên) | Tổ: điểm hồi mini, dọn xác ×1,5 | Quay về tổ liên tục (hub–spoke) | 0,25 |
| Thủy (Oa) | **Dòng + Ẩm**: xuôi dòng Tốc +20%, ngược −10%, nước sâu ẩn | Dẫn Nước cho cây (+6 Thủy/phút) | Bám bờ, vòng quanh nguồn nước | 0,2 |
| Vũ (Kê) | **Báo Tin**: ping party 20 ô/8s + Sải Cánh | Gáy Bình Minh: sương +15 Thủy | Đi xa trinh sát rồi về báo | 0,2 |

Tổng ≈ +0,8 nếu làm đủ phần bắt buộc ở 4 tộc mới (Mộc là 0). **Phần này nằm trong hạng mục "đơn giá lite 1,2/loài"** ở §F: tôi đã tính HUD/AI 0,2, nên tăng thực tế khoảng +0,4 (còn lại là phần tôi gán sẵn). Ngân sách nay ròng ≈ **+2,75**, đệm ≈ 1,5 (≈3%). Đó là mức dưới ngưỡng an toàn: bắt buộc áp cổng tuần 16 và "đợt 2".

Quan hệ với F: tag di sản (Hộ/Sát/Sinh/Hợp) được dịch qua động từ riêng của tộc (xem bảng F), nên mỗi lần đổi tộc thấy một "giọng" khác của cùng hiệu ứng. Đây là cách rẻ nhất để đáp ứng "mỗi lần chơi có cảm giác mới".

### Top 3 điều team phải chốt (cập nhật)
1. **Chết = mất trắng có lớp bảo vệ**: Kiếp thất bại ≠ chết, Trọng Thương C3+, chống gank theo cảnh, khởi động lại ≤5'. Thiếu các lớp này, tôi sẽ BLOCK ở R6.
2. **Năm đại diện và ma trận hai tầng** (Lang, Oa, Kiến Hậu+Lính có chi phí, Kê; Căn Thương cho Trùng), cộng bảng địa hình nước.
3. **Ngân sách +2,75 (đệm ~3%)** kèm cổng tuần 16/30, và lựa chọn mỗi mốc phải gồm 1 lựa chọn sống sót.
