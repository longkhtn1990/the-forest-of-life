# 00-brief — Gameplay chi tiết Trùng Tộc (Linh Nghĩ)

## Yêu cầu nguyên văn
> đào sâu vào phát triển gameplay chi tiết cho trùng tộc, người chơi sẽ làm gì thao tác gì? ở từng level từng giai đoạn, các tính năng mở khóa là gì và họ sẽ thao tác thêm gì?

## Bối cảnh
- GDD hiện hành: `Game document design/The-Forest-of-Life-GDD-v1.2.md` (bắt buộc đọc các mục liên quan Trùng/Linh Nghĩ: §2.7, §3, §4.2, §4.5–4.8, §5.1–5.2, §5.10–5.11, §6.2–6.7, §6.9–6.10, §7, §12, §13). Mọi quyết định trong v1.2 là nền, **không làm lại**; chỉ đào sâu và lấp chỗ trống. Nếu thấy mâu thuẫn trong v1.2 thì nêu và đề xuất sửa.
- Nhân vật MVP Trùng Tộc = **Linh Nghĩ** (kiến): Hậu (người chơi) + Lính. Đặc tính tộc **Bầy & Thoát Xác**. Nội tại **Hy Sinh**. Động từ **Tha**, Xung, Mở Xác, Căn Thương (C3, chỉ khi cây Mộc Tàn). Đạo Lộ: Chức Diệp (Tồn) / Toan Nghĩ (Sát) / Công Nghĩ (Vai) + Thiên Phú Hậu Mẫu + 3 Hợp Đạo. Cảnh giới: Ấu Nghĩ → Lập Sào → Thành Quần → Nghĩ Đan. Đầy đủ C1–C4 + Viên Mãn. Mid ~4,9h/đời.
- Ràng buộc cứng: mobile ≤5 nút, HUD 4+1, controller chung; không thêm need mới; không làm phình ngân sách (mọi thứ mới phải ghi chi phí t-n và cái thay thế); trần Ω ≤1,60; PvP luôn bật.

## Deliverable
Một **spec gameplay theo giai đoạn** cho Linh Nghĩ: với **từng cảnh/tầng (C1 Sơ → C4 Hậu → Viên Mãn)** và mốc Đạo Lộ M1–M6: (a) người chơi làm gì (mục tiêu, vòng lặp moment/activity), (b) thao tác gì (mobile & PC, nút nào, cử chỉ nào), (c) mở khóa gì (kỹ năng, động từ, UI, vùng map, cơ chế bầy/tổ), (d) thao tác **thêm** gì so với tầng trước, (e) mối đe dọa & áp lực, (f) số liệu chính. Kèm: đời đầu tiên chơi Nghĩ (onboarding trong đời), session mẫu ở mỗi cảnh, thăng tiến độ phức tạp điều khiển bầy.

## Chế độ
Quick (R1 → R2 → tổng hợp) theo yêu cầu tiết kiệm token của người dùng. Mỗi designer làm đúng phạm vi được giao trong R1, không lan sang domain khác.

## Ngôn ngữ: tiếng Việt, thuật ngữ Hán-Việt như GDD.

---

## GÓP Ý CỦA NGƯỜI DÙNG SAU FINAL (vòng bổ sung R3)
> nhịp độ chơi quá nhanh và không có nhiều rẽ nhánh khác biệt
> ví dụ level 1 sau khi lên level 2 cần phải có 3~5 lựa chọn khác nhau từ đó rẽ ra nhiều phương hướng phát triển thế mạnh, tương tự về sau

Diễn giải (orchestrator):
- **K1. Rẽ nhánh thật:** mỗi lần đột phá **cảnh** (C1→C2, C2→C3, C3→C4, và về sau) đưa ra **3–5 HƯỚNG phát triển khác biệt về thế mạnh/lối chơi** (không phải +% nhỏ). Chọn 1 hướng → cảnh sau mở 3–5 hướng con **kế thừa** từ hướng đó. Mỗi hướng thay đổi rõ cách chơi (động từ, vai, điểm mạnh/yếu, có thể cả hình dạng). Áp dụng cho Linh Nghĩ trước (làm mẫu), sau đó thành template cho cả 5 tộc.
- **K2. Nhịp chậm lại:** một cảnh phải "dày" hơn (v1.2: C1 14', C2 +36', C3 +66', C4 +102', đời ~218' không chết). Team đề xuất 2–3 phương án nhịp cụ thể (phút/giờ mỗi cảnh, số phiên) để người dùng chọn, kèm hệ quả với luật "chết = bắt đầu lại hoàn toàn" (D30/D31: P(Viên Mãn), phút mất mỗi lần chết) và cách giữ an toàn (không tranh luận lại quyết định chết mất trắng).
- Ràng buộc giữ: ≤5 nút, quyết định D/E/F/G vẫn đúng (3–5 lựa chọn mỗi mốc, kế thừa, hiệu quả hết đời; chết mất trắng; Viên Mãn random 3 chọn 1), trần Ω, ngân sách (nêu chi phí nội dung khi số hướng nhân lên — phải có cấu trúc chống bùng nổ tổ hợp).
