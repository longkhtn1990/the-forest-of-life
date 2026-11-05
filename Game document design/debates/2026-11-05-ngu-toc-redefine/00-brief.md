# 00-brief — Định nghĩa lại Ngũ Tộc (revision session)

## Yêu cầu nguyên văn của người dùng (sau khi đọc FINAL.md của GDD v1.0)
> Khái niệm ngũ tộc ok
> Mộc tộc là các cây cối bao gồm cỏ và các loại cây
> Thú tộc là bao gồm các loại thú từ nhỏ đến lớn
> Trùng tộc là bao gồm các loại côn trùng kiến, bướm, ong,...
> Thủy tộc là bao gồm các loại cá và loài nước ngọt sống trong khu rừng (thay thế khuẩn tộc)
> Vũ tộc là tất cả loại chim, gà,...

**Đây là quyết định đã CHỐT của người dùng, không tranh luận lại.** Việc của team: tìm cách thực hiện và xử lý mọi hệ quả cho nhất quán.

## Bối cảnh
- Game: *The Forest of Life*, sinh tồn tu tiên PvP 2D/2.5D top-down, Web/Mobile/PC, studio 1 người + AI. GDD v1.0 ở `Game document design/debates/2026-11-05-forest-of-life-gdd/FINAL.md` (927 dòng, **đọc hết**). Các file khác của session đó (r4-conflicts, r6-signoff...) tham khảo khi cần.
- Ngũ Tộc hiện nay (FINAL §2.7): Mộc, Thú, Trùng, **Khuẩn**, Vũ. Khuẩn Tộc giữ vai "phân giải + **giữ luân hồi**", NPC **Bà Khuẩn** đón Mộng Hỏa ở Trung Ấm. Khuẩn (nấm) là loài chơi được [1.0]; có Bào Tử Triều (E7), vòng nấm tiên (Mộng Ấn 1), "rễ/nấm" trong Sổ Sinh Năng và Linh Quỹ, cộng sinh Nấm của cây. Linh Thảo (cỏ) đang là loài riêng [1.0]. Vũ Tộc: NPC Quạ Già (MVP), chơi được = [Cắt]/[Won't].
- MVP hiện tại: 3 loài (Linh Mộc, Linh Thử, Lang), C1–C4, 1 map 256², ngân sách 45,75 tuần-người + ~4,25 đệm. Đệm đã mỏng (8,5%). **Không được làm phình MVP**: mỗi thêm một thứ phải ghi rõ cắt gì.

## Câu hỏi team phải trả lời (mỗi bản đề xuất phải trả lời cả 5, ưu tiên domain của mình)
1. **Vai trò của Khuẩn Tộc đi đâu?** Phân giải xác, giữ luân hồi/Trung Ấm (Bà Khuẩn), Bào Tử Triều, vòng nấm tiên, cộng sinh nấm, "rễ/nấm" trong Sổ Sinh Năng + Linh Quỹ. Giữ nguyên chức năng gameplay nhưng đổi chủ? Giao cho Thủy Tộc? Nếu nấm vẫn tồn tại trong thế giới thì thuộc tộc nào, hay là yếu tố môi trường không thuộc tộc nào?
2. **Thủy Tộc là gì?** Lore (vì sao nước/cá giữ luân hồi, nếu có), NPC đại diện thay Bà Khuẩn (tên, hình, lời thoại mẫu), địa hình nước (suối, ao, đầm; FINAL hiện có "suối", Đầm Mục, Liễu Chết) trên map 256², loài chơi được đầu tiên (nếu có) và nhãn phạm vi, cơ chế dưới nước (di chuyển, ranh giới nước/cạn, sinh tồn, chiến đấu), tương tác với Mộc/Thú/Trùng/Vũ (chuỗi thức ăn, Thủy need của cây), tên cảnh giới theo loài (bảng §6.2), Hóa Hình.
3. **Mộc Tộc nay gồm cả cỏ và cây**: gộp Linh Thảo vào Mộc thế nào (cùng một loài chơi được? hay hai dạng sống trong cùng tộc?), ảnh hưởng đến Plant Pressure, Thiên Tài Địa Bảo "Linh Thảo", bảng tên cảnh giới.
4. **Vũ Tộc gồm chim, gà...**: có loài chơi được không, ở nhãn nào? Còn là Sứ giả/Quạ Già không? Bay có phá cân bằng top-down 2D không? Ảnh hưởng PvP, Quạ Linh ăn xác (AI), Diều hâu AI.
5. **Phạm vi & cân bằng**: MVP có đổi gì không (nên ít nhất có thể)? 1.0/Post đổi gì? Ngân sách và những gì phải cắt. Roadmap loài mới (bảng §4.1). Cập nhật các chỗ nhắc "Khuẩn/nấm/Bà Khuẩn" trong FINAL.

## Giả định (orchestrator đặt, team được phép phản biện)
- Ngũ Hành/Thần Vị Post (S4) hiện có 5 Thần Vị. Nếu Khuẩn → Thủy Tộc thì ánh xạ Ngũ Hành có thể khớp tự nhiên hơn (Mộc/Thủy...), team nên khai thác nếu hợp lý nhưng không bắt buộc.
- "Loài nước ngọt" = cá, ếch, rùa, tôm, cua... (người dùng nói "các loại cá và loài nước ngọt"). Team tự chọn danh sách.
- Mô tả tộc là về **loài sinh vật**, không còn "chức năng hệ thống" thuần túy như Khuẩn. Chức năng hệ thống (phân giải, luân hồi) phải gắn lại cho khớp tộc mới.
- Giữ nguyên mọi quyết định khác của GDD v1.0 trừ khi bị ảnh hưởng trực tiếp.

## Deliverable
`FINAL.md` của session này = **bản vá (patch) cho GDD v1.0**: danh sách thay đổi theo từng mục FINAL cũ (số mục + nội dung mới), Decision Log, scope delta. Sau đó orchestrator áp patch vào `FINAL.md` của GDD v1.0 (đánh dấu v1.1).

## Chế độ
Quick (R1 → R2 → R5) + R6 sign-off. Vì đây là phản hồi nhắm vào một phần của thiết kế đã có (không chạy lại toàn bộ).

## Ngôn ngữ
Tiếng Việt, giữ thuật ngữ Hán-Việt như GDD v1.0.

## Tham khảo
- `Game document design/debates/2026-11-05-forest-of-life-gdd/FINAL.md` (bắt buộc)
- `.claude/skills/design-debate/protocol.md`

---

## BỔ SUNG CỦA NGƯỜI DÙNG (đã chốt, đến sau khi R1 bắt đầu)
> mỗi loại sẽ nên có một thế mạnh so với các hệ còn lại và có tính tương sinh tương khắc và bổ trợ, cộng sinh lẫn nhau
> và giai đoạn MVP ở mỗi tộc chỉ 1 nhân vật, chưa vội phát triển sâu

Hệ quả bắt buộc team phải xử lý:
- **A. Mỗi tộc có một thế mạnh riêng** so với 4 tộc còn lại (một "vai" không tộc nào thay được).
- **B. Quan hệ giữa các tộc:** tương sinh (A nuôi B), tương khắc (A kiềm chế B), bổ trợ, cộng sinh. Phải thành **ma trận 5×5 cụ thể** (hiệu ứng gameplay đo được, không chỉ lore), nối với Ngũ Hành/vòng linh khí (S2) và ma trận "ai ăn ai" §4.5. Không để một tộc thống trị.
- **C. MVP = 5 tộc × đúng 1 nhân vật chơi được mỗi tộc** (Mộc, Thú, Trùng, Thủy, Vũ), chưa phát triển sâu. Điều này **thay thế** MVP 3 loài (Linh Mộc, Linh Thử, Lang) của GDD v1.0, trong đó Thú Tộc từng có 2 loài. Phải chọn 1 đại diện Thú; cân nhắc Lang/Linh Thử còn lại thành AI. "Chưa sâu" = ví dụ: bản lite, C1–C3 hoặc C4 với ít skill, ít Huyết Mạch. PX phải làm lại ngân sách (hiện 45,75 tuần-người, đệm 8,5%) và gắn cờ scope risk nếu cần, kèm phương án fallback (vd 5 tộc nhưng một số tộc chỉ C1–C2 trong MVP, hoặc ra mắt theo đợt).
- Các câu trả lời cho 5 câu hỏi ở trên giờ phải theo khung "5 tộc × 1 nhân vật".

---

## BỔ SUNG 2 CỦA NGƯỜI DÙNG (đã chốt, đến trong lúc R2)
> mỗi lần phát triển nên có nhiều (3 ~ 5) sự lựa chọn và hướng phát triển thêm ở level đó, các lựa chọn luôn có tính kế thừa và hiệu quả cho đến hết vòng đời của nhân vật
> nếu nhân vật chết giữa chừng thì khi bắt đầu lại sẽ là hoàn toàn mới, nếu nhân vật hoàn thành đến giai đoạn cuối của một nhân vật thì sẽ được chọn 1 hiệu ứng (random 3 trong các hiệu ứng nhân vật hiện có)

Hệ quả bắt buộc:
- **D. Mỗi mốc phát triển (đột phá tầng/cảnh) đưa ra 3–5 lựa chọn** (hướng phát triển/hiệu ứng). Lựa chọn **kế thừa** (lựa chọn sau xây trên lựa chọn trước) và **còn hiệu quả đến hết đời nhân vật** (không có lựa chọn "chết" bị lạc hậu ở cảnh cao). Thay/điều chỉnh hệ skill tree, Huyết Mạch, Keystone, Bản Năng của GDD v1.0 (§6). PROG là owner. Cần quy định: lựa chọn ở mỗi tầng hay mỗi cảnh, pool cố định hay random, tránh choice paralysis trên mobile, phù hợp "MVP chưa phát triển sâu" (mỗi nhân vật MVP cần bao nhiêu lựa chọn tối thiểu).
- **E. Chết giữa chừng = bắt đầu lại hoàn toàn mới** (nhân vật mới ở C1, không mang lựa chọn/sức mạnh). Điều này **thay** cơ chế Hậu Duệ (đầu thai cùng loài, mất ~1 buổi) và phần sức mạnh mang theo của Luân Hồi/Túc Tuệ trong GDD v1.0. Team phải xử lý lại: Trung Ấm, Sổ Sinh Năng (xác vẫn nuôi rừng), chống bắt nạt (mất trắng khi bị gank → Thiên Đạo Luật/Ấu Linh có đủ không?), độ kiếp thất bại có tính là chết không, retention (P3 "Cái chết là hạt giống"), cây offline bất tử, ước tính thời gian một vòng đời.
  - **Giả định của orchestrator (team được phản biện, người dùng sẽ chốt):** "hoàn toàn mới" = không mang theo bất kỳ sức mạnh nào. Thứ không phải sức mạnh (skin, Biên Niên, Mộ Linh, kiến thức, sách sưu tầm) vẫn giữ. Đạo Quả dạng tiền meta mua sức mạnh thì bỏ hoặc chuyển sang chỉ mở khóa ngang (loài, skin), team đề xuất.
- **F. Hoàn thành giai đoạn cuối của nhân vật** → hệ thống random 3 hiệu ứng trong số các hiệu ứng nhân vật đó đang có (các lựa chọn đã nhận trong đời) → người chơi chọn 1 để mang sang nhân vật sau (di sản). Team đề xuất: "giai đoạn cuối" ở MVP là gì (vì MVP lite có thể chỉ tới C2/C3/C4), di sản có cộng dồn qua nhiều đời không (trần?), có áp dụng khi đổi tộc không (hiệu ứng của sói mang sang cây thế nào), di sản có bị mất khi đời sau chết giữa chừng không, sau khi hoàn thành thì nhân vật cũ đi đâu (Phi Thăng, thành Mộ Linh/NPC, Đại Kiếp...).

---

## BỔ SUNG 3 CỦA NGƯỜI DÙNG (đã chốt)
> Game play của mỗi tộc sẽ có phần khác nhau một chút nhỏ để phù hợp với đặc điểm tộc của mình, tạo thêm sự lôi cuốn mới mẻ cho từng lần chơi

Hệ quả:
- **G. Mỗi tộc có một "chất" gameplay riêng, khác nhau một chút** (một cơ chế/động từ đặc trưng + nhịp khác) trên **cùng một khung chung** (HUD 4+1, needs, cảnh giới, lựa chọn 3–5 lựa chọn mỗi mốc). Mục tiêu: mỗi lần đổi tộc sau khi chết hoặc hoàn thành có cảm giác mới. "Khác một chút" nghĩa là không làm 5 game riêng. Phải ghi rõ: phần dùng chung (chiếm phần lớn code/UI) và phần riêng của mỗi tộc (1–2 cơ chế, có ước tính chi phí). Kết hợp với F: di sản mang sang tộc khác thì "dịch" thế nào cho khớp chất của tộc mới.

---

## BỔ SUNG 4 CỦA NGƯỜI DÙNG (đã chốt, đến sau khi FINAL v1.1 được viết)
> 1. Vai trò của Khuẩn Tộc đi đâu? bỏ qua, là yếu tố môi trường
> 2. Thủy Tộc là gì? các loại cá, cua, ếch, nhái, rùa, cá sấu,... các loại sống ở nước hoặc gần nước, đầm lầy
> 3. Mộc Tộc nay gồm cả cỏ và cây? đúng là 1 tộc với nhiều loại cỏ và cây ví dụ hương thảo, ma vân đằng, thiết mộc, tùng, bách, nắp ấm,...
> 4. Vũ tộc là tất cả các loại chim, gà, quạ, cú,...
> 5. Phạm vi & cân bằng: MVP sẽ là mỗi tộc có 1 nhân vật (tổng cộng 5 nhân vật cho 5 tộc) và phát triển đầy đủ các level, gameplay cho nhân vật đó, mỗi nhân vật sẽ có 1 nội tại riêng biệt làm đặc trưng, và con đường phát triển riêng biệt nhưng có đặc tính chung của tộc ví dụ cây thì có thể hấp thụ dinh dưỡng từ đất và ánh sáng để tự tổng hợp dinh dưỡng, kinh nghiệm, chim thì biết bay và di chuyển nhanh, cá thì có thể sống dưới nước,... tự phát triển tiếp

Hệ quả (thay đổi so với FINAL v1.1):
- **H1. Không còn bản lite:** cả 5 nhân vật MVP phát triển **đầy đủ mọi level của MVP (C1–C4 + Viên Mãn C4)** như Linh Mộc/Lang. [Giả định orchestrator: "đầy đủ các level" = đầy đủ trong phạm vi MVP map Hạ Lâm (C1–C4); C5+ theo roadmap U1/1.0/Post như các nhân vật khác.]
- **H2. Hai lớp bản sắc:** (a) **Đặc tính tộc** dùng chung cho mọi loài trong tộc (vd Mộc tự dưỡng từ đất + ánh sáng; Vũ biết bay & di chuyển nhanh; Thủy sống được dưới nước; Thú, Trùng: team đề xuất). (b) **Nội tại riêng** của từng nhân vật (1 passive đặc trưng) + con đường Đạo Lộ riêng.
- **H3. Vũ BAY THẬT** (đảo ngược D22 "không bay"). **Thủy SỐNG DƯỚI NƯỚC** (đảo ngược luật "nước sâu chỉ để lánh, CT ×0"). Phải giữ cân bằng PvP, không vùng bất tử, chạy được trên mobile/netcode top-down 2D.
- **H4. Khuẩn = yếu tố môi trường** (khớp v1.1: nấm không thuộc tộc nào; phân giải là quy trình môi trường).
- **H5. Danh sách loài theo tộc** mở rộng: Mộc (hương thảo, ma vân đằng, thiết mộc, tùng, bách, nắp ấm…), Thủy (cá, cua, ếch, nhái, rùa, cá sấu…), Vũ (chim, gà, quạ, cú…). Chọn lại đại diện MVP nếu cần (đặc biệt Vũ: gà rừng có còn hợp khi tộc "biết bay"?).
