# 00 — Brief: GDD đầy đủ cho "The Forest of Life"

> Session: `Game document design/debates/2026-11-05-forest-of-life-gdd/` · Chế độ: standard · Ngày: 2026-11-05
> Ngôn ngữ output: **tiếng Việt** (giữ thuật ngữ chuyên ngành tiếng Anh khi cần).

## 1. Yêu cầu nguyên văn của người dùng
> "tôi có một idea là xây dựng 1 game là một khu rừng giả tưởng tùy mức độ mà sẽ có khu rừng nhỏ -> rất lớn, rừng nguyên sinh rừng cổ đại.
> Trong khu rừng giả tưởng đó mỗi người chơi sẽ là 1 sinh vật, một cây, một ngọn cỏ đều có ý thức sinh mệnh, với những phương thức thu thập điểm kinh nghiệm tùy thuộc vào từng sinh vật ví dụ: cây thì hấp thu dinh dưỡng và nắng, quang hợp, phản vệ các loại ăn cỏ, ăn lá. Là sinh vật thì ăn, săn bắt để có được kinh nghiệm.
> Con đường tiến hóa của từng sinh vật sẽ có nhiều rẽ nhánh với các kỹ năng khác nhau bổ trợ và làm tăng sức mạnh cho sinh vật, tương tự như các câu truyện tiên hiệp giả tưởng.
> Hãy hỏi sâu thêm tôi để mở rộng ý tưởng, sau đó các subagent hãy debate lẫn nhau để hoàn thiện bộ tài liệu GDD đầy đủ."

## 2. Câu trả lời của người dùng khi được hỏi sâu (ràng buộc CỨNG)
| Chủ đề | Người dùng chốt |
|---|---|
| Mô hình chơi | **Solo + co-op, có server tùy chọn** (bắt đầu solo/co-op, có thể mở rộng lên server lớn hơn) |
| Quy mô rừng | **Kết hợp cả ba**: (a) nhiều cấp map/server theo quy mô: Rừng Non (nhỏ) → Rừng Nguyên Sinh → Rừng Cổ Đại (khổng lồ); (b) trong mỗi map có vùng ngoài→trong càng cổ xưa càng nguy hiểm; (c) rừng biến đổi/phát triển theo thời gian và hành động người chơi |
| Cái chết | **Luân hồi chuyển kiếp**: chết mất thân xác nhưng giữ một phần "linh hồn/đạo tâm" (meta-progression), chọn đầu thai thành loài khác; xác trở thành dinh dưỡng cho rừng |
| Tiên hiệp | **Kết hợp**: mỗi loài có **tên gọi cảnh giới riêng**, nhưng các cảnh giới **tương đương nhau về mức level tiến hóa** giữa các loài (vd cảnh giới 3 của cây ≈ cảnh giới 3 của sói). Có linh khí, độ kiếp, hóa hình, bí cảnh… |
| Chơi thực vật | Dùng **tất cả**: mở rộng lãnh thổ bằng rễ/hạt; hóa hình khi đủ cảnh giới; điều khiển sinh vật cộng sinh (nấm, kiến, ong…); linh hồn xuất khiếu (phóng linh thức ra khỏi thân). **Team được yêu cầu nghĩ thêm và phát triển thêm.** |
| PvP | **Luôn PvP tự do** — chuỗi thức ăn thật sự giữa người chơi |
| Nền tảng | **Web, Mobile, PC** |
| Đồ họa | **2D/2.5D top-down stylized** |
| Tone | **Hùng vĩ, huyền huyễn, khắc nghiệt vừa** — rừng đẹp và nguy hiểm, cá lớn nuốt cá bé nhưng có cơ hội vươn lên; độ kiếp là khoảnh khắc hùng tráng |
| Endgame | **Sinh tồn, sống sót và thành thần.** Thường xuyên có **nhiều sự kiện lớn ảnh hưởng cả khu rừng** |
| Session | **Có lưu tiến độ, mỗi lần chơi 15–60 phút, toàn bộ tiến trình kéo dài nhiều tuần** |
| Team & kinh doanh | **Studio 1 người + các AI subagent**. **Free-to-play**, kiếm tiền từ **quảng cáo, thời trang/skin, pass** |

## 3. Giả định của orchestrator (team được phép tranh luận/đổi, nhưng phải nêu lý do)
- **G1 — PvP vs Solo:** "Luôn PvP tự do" áp dụng cho mọi thế giới **online/shared**. Chế độ **solo** (offline hoặc private) đối thủ là AI. Co-op bạn bè trong cùng một rừng vẫn có PvP với người ngoài nhóm. Team cần đề xuất cơ chế chống "ma cũ bắt nạt ma mới" (newbie protection, vùng an toàn, chênh lệch cảnh giới) mà KHÔNG phá tinh thần PvP tự do.
- **G2 — Nền tảng:** cùng một codebase (vd Unity/Godot/web engine) xuất Web + Mobile + PC; input phải chơi được bằng cảm ứng. Team nên đề xuất thứ tự ra mắt (platform nào trước).
- **G3 — Monetization:** không pay-to-win; skin/cosmetic không tăng chỉ số. Quảng cáo nên là rewarded ads tùy chọn. PX cần đánh giá tính đạo đức và tác động tới PvP.
- **G4 — Sản xuất:** 1 người + AI (code, art bằng AI hỗ trợ, nội dung). Mọi tính năng phải được ước lượng chi phí theo thực tế này. MVP phải khả thi trong ~6–12 tháng.
- **G5 — Số loài lúc ra mắt:** chưa chốt; team đề xuất (gợi ý ban đầu: 4–6 loài đại diện các "giới" khác nhau: thực vật thân gỗ, cỏ/thảo mộc, ăn cỏ, ăn thịt, côn trùng/nấm…).
- **G6 — Tên game tạm:** "The Forest of Life". Bối cảnh văn hóa: cảm hứng tiên hiệp/huyền huyễn phương Đông, có thể pha thần thoại rừng toàn cầu.

## 4. Deliverable mong muốn
**Một bộ GDD đầy đủ** (sẽ tổng hợp ở `FINAL.md`), tối thiểu bao gồm:
1. Tầm nhìn, hook, USP, theme, design pillars, đối tượng người chơi
2. Core loops nhiều tầng (moment / session 15–60' / tuần / luân hồi)
3. Hệ thống loài & giới (thực vật / động vật / côn trùng / nấm…), cách chơi riêng và cách nhận "tu vi"/EXP riêng của từng loại
4. Hệ thống cảnh giới & tiến hóa: tên cảnh giới riêng mỗi loài, bảng tương đương, rẽ nhánh tiến hóa, skill tree, độ kiếp, hóa hình
5. Hệ thống sinh tồn: needs, tài nguyên/linh khí, môi trường, chuỗi thức ăn, mối đe dọa
6. Đặc tả cách chơi thực vật (rễ, hạt, cộng sinh, xuất khiếu, hóa hình + ý tưởng mới)
7. Luân hồi & meta-progression
8. Thế giới: các cấp rừng, vùng, biome, bí cảnh, lore, thế lực, rừng biến đổi theo thời gian
9. Sự kiện lớn toàn rừng (world events)
10. PvP, co-op, server, chống bắt nạt người mới
11. FTUE, UI/UX đa nền tảng, accessibility
12. Kinh tế, monetization F2P (ads, skin, pass), live-ops
13. Phạm vi: MVP / vertical slice / roadmap, chi phí cho studio 1 người + AI, kỹ thuật/engine đề xuất
14. Rủi ro, giả thuyết playtest, KPI
15. Decision log, câu hỏi mở

## 5. Tài liệu tham khảo trong repo
Chưa có tài liệu thiết kế nào trước đó. Đây là session đầu tiên.
