# R7 Patch: WORLD

Phạm vi: W1–W5 theo BỔ SUNG 4. Số liệu để SURV/PROG chốt.

## W1. Đặc tính tộc *(WORLD-R7-01)*
| Tộc | Đặc tính | Lore 1 câu | Gameplay (ý tưởng) |
|---|---|---|---|
| Mộc | **Tự Dưỡng** | *"Cây không săn: nó uống đất và nuốt nắng."* | Tu vi + No sinh từ Dưỡng Chất ô rễ × ánh sáng (Vệt Nắng, mùa, Tán che). Không cần đi kiếm ăn. Đổi lại: không di chuyển, chịu hạn/bóng râm. |
| Thú | **Khứu Tung** (đánh hơi) | *"Thú đọc rừng bằng mũi; máu là chữ viết rõ nhất."* | **Đánh Hơi thành đặc tính tộc** (Linh Thử, Lộc sau này cũng có), không còn là động từ riêng của Lang. Thấy vệt máu/xác/mùi; nước và mưa xóa vệt. Nhân vật Thú khác nhau ở cách *dùng* vệt. |
| Trùng | **Thoát Xác** | *"Trùng chết đi một lần mỗi khi lớn lên, để lại cái vỏ cho rừng."* | Đột phá cảnh = lột vỏ: hồi đầy, xóa debuff. Vỏ cũ rơi tại chỗ thành đồ ăn/Sinh Năng cho tộc khác. Phụ: thân nhỏ, chui được khe/bụi mà tộc khác không vào. Ludonarrative: lớn lên là trả lại cho rừng. |
| Thủy | **Thủy Tức** | *"Với Thủy tộc, mặt nước là trần nhà, không phải bức tường."* | Thở và di chuyển dưới nước sâu (tốc nhanh hơn trên cạn), lên cạn thì có Ẩm. **Chống vùng bất tử:** dưới nước vẫn bị Thủy tộc khác và Quăng Lưỡi đánh. Di chuyển tạo gợn bọt (nhìn thấy được). Hồi máu dưới nước sâu không nhanh hơn ở Nơi Trú. |
| Vũ | **Lăng Không** (bay) | *"Chim là mắt của rừng vì nó đứng ở chỗ không ai đứng được."* | Bay là một **tầng trạng thái** (đổi sprite + bóng đổ, không cần vật lý 3D): vượt địa hình, nhìn rộng hơn, tốn Thể Lực liên tục, **không ăn/đánh khi bay** (trừ Bổ Nhào). **Chống bất tử:** bóng đổ luôn hiện. Diều hâu AI săn trên tầng không. Quăng Lưỡi/Gai bắn được người đang bay. Hết Thể Lực thì rơi. Netcode: chỉ 1 cờ `airborne` + tốc. |

## W2. Đại diện Vũ MVP: đổi sang **Linh Nha (Quạ)** *(WORLD-R7-02)*
Lý do:
1. **Tộc "biết bay" thì đại diện phải bay giỏi.** Gà rừng chỉ bay vụt ngắn nên sẽ dạy sai đặc tính tộc ngay ở đời đầu.
2. **Hợp vai "mắt & miệng của rừng" hơn bất kỳ loài nào.** Quạ ăn xác, tìm xác (ăn khớp Linh Hạch, Mở Xác) và kêu báo bầy.
3. **Khớp với Hỏa:** **Kim Ô** là quạ ba chân trong mặt trời. Như vậy Vũ = Hỏa có gốc thần thoại, không còn gán ghép.
4. **Tái dùng gần hết kit Kê:** Gáy → **Kêu Báo**, Hạ Cánh Đạp → **Bổ Nhào** (đáp từ tầng không), Bới giữ nguyên (quạ bới thật). Sải Cánh được thay bằng đặc tính Lăng Không. Linh Kê lùi về roadmap 1.0, dùng lại thiết kế cũ, chi phí thấp.

So với các loài khác: sẻ yếu vai, khó đọc trên mobile. Cú gắn đêm nên lệch nhịp ngày-rừng.

**Đổi NPC:** Quạ Già → **Bạch Hạc** (Lão NPC Vũ, sứ giả, báo sự kiện 24h). Hạc không có trong roadmap chơi được nên luật đặt tên được đảm bảo vĩnh viễn. Landmark Ao Gương: **hạc đứng trên lưng Lão Quy**, đúng hình tượng hạc–quy trong đền Việt. Người chơi nhìn từ xa là biết đó là nơi luân hồi.

**Lỗi luật trong v1.1 cần sửa:** roadmap Post có "Linh Quy" (rùa) trùng loài với Lão Quy. Đề xuất đổi thành **Miết** (ba ba).

## W3. Nội tại riêng *(WORLD-R7-03)*
| Nhân vật | Nội tại | Flavor | Ý tưởng hiệu ứng |
|---|---|---|---|
| Linh Mộc | **Niên Luân Ký** | *"Mỗi mùa đông qua đi để lại một vòng gỗ."* | Mỗi mùa sống sót +1 vòng (có trần): +Thân HP max nhỏ, hiện trên UI Niên Luân. Thưởng cho việc *sống lâu*, đúng nhịp chậm. |
| Lang | **Truy Huyết** | *"Con mồi chạy, máu nó ở lại."* | Mục tiêu đang chảy máu hoặc HP <50% để lại vệt Khứu Tung đậm, Lang chạy theo vệt +Tốc. Biến đặc tính tộc thành đuổi kết liễu. |
| Linh Nghĩ | **Sào Ký** | *"Tổ nhớ mọi thứ ngươi mang."* | Mỗi vật Tha về Tổ +1 cộng dồn (có trần, mất khi chết): Lính sinh ra +HP/Công nhỏ. Khớp hint FTUE sẵn có. |
| Thanh Oa | **Hô Vũ** | *"Cóc là cậu ông Trời; ếch kêu thì Trời phải nghe."* | Đứng ở nước nông kêu (bị động, tự kích sau vài giây đứng yên): ô đất 3 ô quanh Oa thành "đất ẩm" (+Thủy cho cây). Mưa thì Oa +CT. Thủy → Mộc thành hành vi, không cần nút. |
| Linh Nha | **Ký Diện** | *"Quạ không quên một khuôn mặt, và nó kể cho cả bầy."* | Kẻ đánh Nha bị "Ghi Mặt" vài phút: Nha và party thấy kẻ đó khi trong tầm, Nha gây thêm sát thương lên kẻ đó. Dựa trên hành vi thật của quạ. Đồng thời là công cụ chống bắt nạt tự nhiên (§8). |

## W4. Roadmap loài theo tộc *(WORLD-R7-04)*. **Đậm** = MVP
**Mộc**
- **Linh Mộc**: cây gỗ, neo vùng, toàn năng
- Hương Thảo: hương xua trùng, hồi phục
- Ma Vân Đằng: dây leo quấn trói
- Thiết Mộc: vỏ sắt, chậm, trụ
- Tùng: xanh qua Đông, chịu lạnh
- Bách: trường thọ, rễ sâu
- Nắp Ấm: bẫy nuốt trùng
- Trúc: lớn vọt, rỗng ruột
- Si (Cổ Thụ): rễ phụ lan
- Liên (sen): cây sống trong nước

**Thú**
- **Lang**: săn đuổi, kết liễu
- Linh Thử: nhỏ, đào hang, trữ hạt
- Hồ (cáo): mưu mẹo, giả chết
- Lộc (hươu): chạy xa, gạc húc
- Trư (lợn rừng): ủi đất, lì đòn
- Hầu (khỉ): leo tán, ném quả
- Hùng (gấu): ngủ Đông, đập mạnh
- Báo: ẩn đêm, vồ một đòn

**Trùng**
- **Linh Nghĩ**: bầy đàn, tha về tổ
- Phong (ong): thụ phấn, chích đàn
- Điệp (bướm): rắc phấn, đổi rừng
- Thiền (ve sầu): ngủ đất, Thoát Xác
- Đường Lang: rình, chém kép
- Huỳnh (đom đóm): sáng đêm, dẫn đường
- Tri Chu (nhện): giăng tơ, bẫy chờ
- Ngô Công (rết): độc, chui đất

**Thủy**
- **Thanh Oa**: lưỡng cư, lưỡi kéo
- Linh Cáp (nhái): nhỏ, nhảy xa, độc da
- Linh Lý (cá chép): Vũ Môn → Giao Long
- Giải (cua): càng kẹp, đi ngang bờ
- Miết (ba ba): giáp mềm, cắn giữ
- Thiện (lươn): luồn bùn, trơn thoát
- Ngạc (cá sấu): phục kích bờ, đỉnh xích

**Vũ**
- **Linh Nha (quạ)**: trinh sát, ăn xác, báo
- Linh Kê (gà rừng): bới đất, gáy, bay ngắn
- Tước (sẻ): đàn nhỏ, nhanh nhẹn
- Yến (én): bay nhanh nhất, theo mùa
- Thúy Điểu (bói cá): lao nước, khắc Thủy
- Hiêu (cú): săn đêm, bay im
- Ưng: bay cao, vồ con mồi

## W5. Cảnh giới Linh Nha *(WORLD-R7-05)*
| C | Khung | Linh Nha | Gắn cơ chế |
|---|---|---|---|
| 1 | Khai Linh | **Hoàng Khẩu** (mỏ vàng chim non) | Chưa bay thật, chỉ nhảy và vỗ cánh ngắn. FTUE an toàn, C1 không có vùng bất tử. |
| 2 | Luyện Khí | **Ly Sào** (rời tổ) | Mở Lăng Không. |
| 3 | Trúc Cơ | **Phản Bộ** (quạ mớm mồi nuôi mẹ) | Mở thẻ/động từ mớm mồi đồng minh (+No) thành vai party. |
| 4 | Kết Đan | **Nha Đan** | MVP (H1). |
| 5 | Hóa Hình | Nha Nhân ‖ Yêu Nha | |
| 6 | Nguyên Anh | **Kim Ô Hồn** | Thay Chu Tước Hồn. |
| 7 | Thành Thần | **Kim Ô Thần** | Thay Phượng Thần. |

Glossary: Ngũ Tộc Vũ = "chim muông (quạ, gà, cú…)", Thủy = "loài sống ở nước/gần nước, đầm lầy". Thêm Tự Dưỡng, Khứu Tung, Thoát Xác, Thủy Tức, Lăng Không, Kêu Báo, Bổ Nhào, Bạch Hạc. Bỏ Quạ Già, Sải Cánh, Hạ Cánh Đạp.
