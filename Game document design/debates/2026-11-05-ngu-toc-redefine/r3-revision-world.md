# R3 Revision — WORLD

Phạm vi: toàn bộ domain WORLD sau Bổ sung 1–3 (A–G). Số liệu cơ chế (hệ số, CD, HP) vẫn do SURV/PROG chốt. Ở đây tôi chỉ đưa con số khi đó là con số bố cục map hoặc con số lore. Ngân sách theo bảng bottom-up của PX.

## Phản hồi phản biện

| Phản biện (từ ai, ID) | Quyết định | Lý do | Thay đổi cụ thể |
|---|---|---|---|
| PROG: WORLD-06 "≤×1,15 nằm trong trần 1,32" (**Blocker**) | **Accept** | Tôi hiểu sai trần: 1,32 chưa chứa E, nên 1,32×1,25×1,15 = 1,90 > 1,77 | Bỏ mọi hệ số sát thương cấp tộc. Khắc chỉ là **cơ chế** (PROG-R2-01). WORLD-06b chỉ còn tên, lore và cơ chế |
| PX, SURV: FTUE kiến (Major) | **Accept** | Mạch FTUE đã được tinh chỉnh cho chuột. Một con chuột chết thì người chơi đọc ra ngay, một con kiến lẻ thì không | FTUE giữ **chuột Tiền Thân**. Kiến chỉ xuất hiện trong vignette 0:40 (kiến khiêng hạt qua đường, dùng swarm VFX sẵn có) |
| PX, SURV, PROG: "Cụ Ngao" (Minor) | **Accept** | Người Việt đọc "ngao" thành con nghêu. Con ngao cũng không phải loài nước ngọt | NPC tên **Lão Quy**. Chữ 龜 (rùa) khác chữ 歸 trong *Quy Căn* (Post), nên ít khả năng nhầm. Giữ nguyên Quy Căn |
| PX, SURV, PROG: Thủy = Oa, không phải Quy | **Accept** (rút lại lập trường R2 của tôi) | Quy chậm trên cạn, nước chỉ chiếm ~5% map, và nước sâu dễ thành vùng bất tử. Oa lưỡng cư nên có động từ chủ động ngay từ giây đầu. Tôi R2 lo Oa "lấn vai Trùng" nhưng nỗi lo đó thành quan hệ ăn: Oa ăn kiến lẻ, còn bầy kiến khắc Oa | **Thanh Oa** là nhân vật MVP. Rùa = Huyền Vũ nằm trọn ở **Lão Quy** (NPC), nên NPC trông khác hẳn loài chơi được |
| SURV: nước sâu chỉ có ở Thâm Lâm, Thủy spawn ở đâu (Major) | **Accept** | Oa mới sinh không có chỗ trốn | Thêm **3 Hồ Con** (3×3 sâu) ở Bìa Rừng, mỗi Hồ Con nằm ở một cửa suối. Đây là điểm sinh của Oa (WORLD-03b) |
| SURV: 3 con số Tốc nước nông khác nhau (Major) | **Accept** | Luật địa hình chỉ được có một bộ số | Bỏ ×0,75 của tôi, dùng bảng địa hình §B của SURV. WORLD chỉ đặt chỗ nước và đặt tên |
| SURV: Quăng Lưỡi kéo người chơi gây lỗi netcode (Major) | **Partial** | Kéo là chất của ếch, bỏ đi thì Oa mất động từ. Nhưng kéo vị trí người chơi ở 10–15 Hz quả thật rủi ro | Đề xuất lai: Quăng Lưỡi **kéo AI và con mồi nhỏ** (sâu, kiến lẻ, mồi AI). Trúng **người chơi** thì không kéo mà gây chậm 1s + **Ướt**. SURV/PROG chốt số |
| SURV: thế mạnh "Mắt" của Kê không đọc được khi chơi solo (Minor) | **Accept** | Lời góp ý đúng. PX cũng yêu cầu mỗi tộc có một động từ solo | Động từ riêng của Vũ là **Gáy** từ C1: ping cho party, và khi solo thì làm lộ Linh Hạch/xác trong tầm (PX) |
| PROG: lite C2 không đủ mốc chọn cho D | **Accept** (tầng lore) | D cần ≥3 mốc chọn, Căn Thương cũng cần C3 | Đặt tên cảnh giới C1–C4 cho cả 3 loài lite. Nếu PX hạ về C2 ở cổng tuần 30 thì vẫn dùng bộ tên này |
| PROG: Mộc→Thú "Thể Lực +20%" chồng lên Quả Ước | **Accept** | Vòng sinh đã đổi (WORLD-06b) nên hiệu ứng này không còn | — |
| PROG: Vũ⊣Mộc phá Mầm-Neo ×2 | **Accept** | Cặp khắc này không còn tồn tại | — |
| PX: lite fallback "C1 + 1 skill" | **Accept** | 1 động từ không làm ra một vai | Fallback đúng là **hoãn cả loài**. Ra mắt theo đợt thì dùng sự kiện "Vũ/Thủy Tộc Giáng Lâm" (Quạ Già báo trước) |
| PX: scope delta +0,7 của tôi bị đếm trùng | **Accept** | Có ba khoản tôi đếm sai | Dùng bảng của PX. Phần WORLD ở §"đánh đổi" |
| PX (b), SURV R2: vòng sinh Mộc→Thú→Trùng→Vũ→Thủy | **Reject** | Lý do ở "Lập trường giữ vững" #1 | Giữ vòng Ngũ Hành + Tứ Tượng (SURV-03 R1 = PROG R2 = WORLD R2) |
| PX-07: đổi vật phẩm Linh Thảo thành "Dược Thảo" | **Reject** | Đổi tên kéo theo việc sửa FTUE (0:40) và §5.6. Người chơi chưa từng nhầm hai thứ này | Vật phẩm giữ tên **Linh Thảo** |
| PX Q: "Mắt" của Vũ có chạm lore của Quạ Già không | Trả lời | Không chồng nhau: **Vũ Tộc là mắt và miệng của rừng**. Quạ Già báo cho cả rừng (sự kiện, 24h). Kê báo cho bầy (Gáy, vài giây) | Một câu lore ở §2.7 |
| Tự sửa R2 (sau khi đọc SURV/PROG/PX R2) | — | — | (1) **Kiếp thất bại không phải chết** (rút lại "Kiếp thất bại = chết"). (2) **Đạo Chủng không mất khi chết** (rút lại "mất hết"). (3) **Bỏ thuật ngữ Nghiệp Ấn**, gộp vào Sát Nghiệp đã có (v1.0 tính Đánh Úp Kiếp là Sát Nghiệp). (4) Bánh xe chọn tộc: bỏ phương án "3 lớn + Xem thêm", theo PX hiện 5 thẻ |

---

## Đề xuất đã sửa

### WORLD-05b: Bảng Ngũ Tộc chuẩn (thay §2.7, §4.1)

| Tộc | Hành | Thế mạnh độc quyền (A) | Thẻ bánh xe (≤6 chữ) | Lão NPC | Nhân vật MVP | Động từ riêng (G) | Nhịp |
|---|---|---|---|---|---|---|---|
| **Mộc** | Mộc | **Nuôi**: lãnh thổ rễ, hạ tầng, bất tử khi offline, nâng Linh Quỹ | *Bén rễ, nuôi cả vùng* | **Lão Tùng** (MVP) | **Linh Mộc** C1–C4 | **Bén Rễ** (+ Quả Ước, có sẵn) | Chậm, theo mùa |
| **Thú** | **Kim** | **Săn**: burst, áp lực, kết liễu | *Săn nhanh, cắn quyết định* | Bạch Lộc Tàn Hồn [1.0] | **Lang** C1–C4 | **Đánh Hơi** (thấy vệt máu/mùi; nước xóa vệt) | Rình, lao, nghỉ |
| **Trùng** | **Thổ** | **Số đông + dọn xác**: bầy Lính, Mở Xác, **Căn Thương** (chỉ chạy khi có phối hợp) | *Một mình mà thành bầy* | **Nghĩ Hậu Hóa Thạch** [1.0] (đổi tên từ "Trùng Hậu") | **Linh Nghĩ** lite | **Tha** (khiêng hạt/xác/Mầm về tổ) + bầy | Đi rồi về tổ (hub–spoke) |
| **Thủy** | Thủy | **Dòng**: ẩn và hồi trong nước, tưới cây, **giữ luân hồi** (Trung Ấm, Đạo Chủng) | *Nước là nhà và đường* | **Lão Quy** (MVP) | **Thanh Oa** lite | **Quăng Lưỡi** + Lặn (nước sâu = Hang) | Bám bờ, rình |
| **Vũ** | **Hỏa** | **Mắt và miệng**: báo tin, trinh sát, vượt địa hình ngắn | *Thấy trước, gáy trước* | **Quạ Già** (MVP, Sứ giả) | **Linh Kê** lite (gà rừng) | **Gáy** (ping/Thần Thức) + Sải Cánh | Đi xa, dừng, báo |

- **Không có loài chơi được thứ hai ở MVP.** Linh Thử thành **Tiền Thân FTUE + AI** (con mồi, Hạt Quên [1.0]). Diều hâu, Quạ Linh và Diệc AI (nếu có) mang nhãn Vũ Tộc. Kiến AI và Sâu Lửa mang nhãn Trùng Tộc. Cá và tôm là decor/swarm mang nhãn Thủy Tộc.
- **Lộ trình loài thứ hai (tên giữ chỗ, PX xếp nhãn):** Mộc: Linh Thảo [1.0] · Thú: Linh Thử (chơi lại) [1.0], Lộc [Post] · Trùng: Phong (ong), Điệp (bướm) [Post] · Thủy: **Linh Lý** (cá chép, Vũ Môn → Giao Long) [Post], Giải (cua) [Post] · Vũ: **Ưng** (bay thật) [Post].
- **Luật đặt tên:** NPC không bao giờ trùng loài chơi được của tộc mình (Lão Quy là rùa, Oa là ếch; Quạ Già là quạ, Kê là gà).

### WORLD-06b: Vòng Hành, đọc bằng vật chất (thay WORLD-06)

**Hành:** Mộc = Mộc · **Vũ = Hỏa** (Chu Tước) · **Trùng = Thổ** · **Thú = Kim** (Bạch Hổ) · Thủy = Thủy (Huyền Vũ, chính là Lão Quy).
**Sinh:** Mộc → Vũ → Trùng → Thú → Thủy → Mộc. **Khắc:** Mộc ⊣ Trùng ⊣ Thủy ⊣ Vũ ⊣ Thú ⊣ Mộc.
**Luật một Hành:** Hành thuộc về **tộc (thân)**, không thuộc về nhánh. Các nhánh Đạo Lộ (WORLD-11b) mang **kênh** (Sát/Hộ/Động/Hồi/Thức), không mang Hành. Vì vậy "Huyết Lang (Hỏa)" của v1.0 không còn nhãn Hỏa. Không có trường hợp một con mang hai Hành (đúng PROG-R2-01 mục 3).

| Cặp | Tooltip (tên vật chất, ≤5 chữ) | Hình ảnh người chơi thấy | Gợi ý cơ chế (SURV/PROG chốt, **không có hệ số sát thương**) |
|---|---|---|---|
| Mộc → Vũ | *Hạt rụng nuôi chim* | Kê mổ quả/hạt dưới Tán | Kê ăn Quả Ước/hạt +No. Kê mới **nở dưới Tán đồng minh** (chọn điểm sinh) |
| Vũ → Trùng | *Đất bới nuôi bầy* | Ô đất Kê vừa bới bị xới tung | Ô Kê vừa ăn/bới thành **Đất Xới** 60s, Nghĩ Tha/đào nhanh hơn trên ô đó |
| Trùng → Thú | *Xác mở nuôi thú* | Kiến khoét xác, sói ăn | **Mở Xác** (cộng sinh thật #3 của PX): Lang ăn xác nhanh hơn |
| Thú → Thủy | *Xác chìm nuôi nước* | Xác bên bờ, đàn cá tụ lại | Xác nằm trong ≤1 ô của nước thì phần Đất của Sinh Năng chảy vào nước: đàn cá +1, Oa ăn +No |
| Thủy → Mộc | *Nước dẫn nuôi cây* | Oa ngồi trong vũng giữa ô rễ | **Dẫn Nước** (cộng sinh thật #2 của PX): +Thủy cho cây trong 4 ô |
| Mộc ⊣ Trùng | *Nhựa đắng đuổi bầy* | Bầy dạt khỏi ô rễ | Bầy <3 Lính bị đẩy khỏi ô rễ, **trừ khi có Khế ước Kiến** (cộng sinh thật #1). Cây chọn: nuôi bầy hay đuổi bầy |
| Trùng ⊣ Thủy | *Bầy đắp bờ, nước đục* | Bờ nước sẫm màu, có gò đất | Bầy ≥3 Lính trên bờ làm ô nước "đục" 20s: Oa mất ẩn và hồi ở ô đó |
| Thủy ⊣ Vũ | *Nước ướt cánh* | Lông Kê sũng nước | Quăng Lưỡi trúng hoặc đứng trong nước nông thì **Ướt**: Sải Cánh hồi chậm hơn |
| Vũ ⊣ Thú | *Tiếng gáy phá rình* | Kê gáy, vệt đỏ hiện quanh sói | **Gáy** làm lộ Thú đang ẩn và hủy bonus Vồ-từ-ẩn. Diều hâu AI săn thú nhỏ (FTUE) |
| Thú ⊣ Mộc | *Nanh vuốt phá thân* | Vết cào trên Thân cây | Lang vốn là mối đe dọa chính của cây trong v1.0 (Đổ ≥40s). Cơ chế thêm nếu cần: Vết Cào làm Tán hồi chậm hơn |

- **Luật "ăn khác khắc"** viết vào Codex: *"Lẻ thì là mồi, bầy thì là đất."* Oa ăn kiến lẻ, nhưng bầy kiến khắc Oa. *"Gà một mình là mồi của sói. Tiếng gáy là kẻ thù của sói."*
- Cộng sinh thật #4 của PX (Vũ ping cho Thú) nằm trên một **cặp khắc**. Theo lore đây là điểm hay chứ không phải lỗi: *kẻ khắc ngươi, nếu thành đồng đội, sẽ là mắt của ngươi.*

### WORLD-16 (mới): "Ai ăn ai" cho 3 loài mới (bổ sung §4.5, SURV đã chỉ ra thiếu)
| Loài | Ăn | Bị ăn bởi | Ghi chú lore |
|---|---|---|---|
| Linh Nghĩ | xác (Mở Xác), hạt, mật Quả Ước, sâu | Kê, Oa (khi Nghĩ đi lẻ) | Lang không ăn kiến: quá nhỏ, không đáng một miếng |
| Thanh Oa | C1 (Khoa Đẩu): tảo, xác chìm · từ C2: kiến lẻ, sâu, côn trùng AI | Lang (khi Oa ở cạn), Kê (khi Oa ở C1), Diều hâu AI | Đổi thức ăn ở C2 là chuyện sinh học thật (nòng nọc ăn tảo/xác, ếch ăn côn trùng) và **đổi nguồn tu vi** đúng lúc rụng đuôi |
| Linh Kê | hạt/quả, sâu, Nghĩ lẻ, Oa C1 | Lang, Báo AI, Diều hâu AI | Gà rừng ăn tạp, vì thế là mắt xích mở đầu của vòng sinh |

### WORLD-01b: Lore nước giữ luân hồi (thay §2.1 S1–S3)
- **S1 (sửa):** Rễ của Kiến Mộc là **Linh Mạch**, và Linh Mạch cũng là **mạch nước ngầm**. Chỗ mạch trồi lên mặt đất là **Linh Tuyền**. *Người chơi làm gì:* đi ngược dòng là đi vào trong rừng (wayfinding), cắm rễ cạnh suối là cắm gần mạch.
- **S2 (sửa):** *nắng → cây → (chim, thú ăn cỏ) → thú săn → xác → **đất hoặc nước** → Linh Mạch.* Trên cạn, xác được **Trùng** phân giải. Dưới nước, xác được **Thủy** phân giải. Nấm chỉ là bề mặt của quá trình đó (WORLD-04b).
- **S3 (viết lại theo E):** Mộng Hỏa là **ngọn lửa ý chí**, không phải kho sức mạnh. Sức mạnh nằm trong **thân**, và khi chết thân trả hết sức mạnh cho rừng. **Nước là thứ duy nhất nhớ mà không giữ hình.** Mộng Hỏa tắt trong nước rồi nổi lên lại thành một đốm mới, nhỏ, không mang theo gì. Chỉ khi một đời **đi hết đường** thì phần mộng đã chín mới **kết thành hạt** (Đạo Chủng). Nước giữ hạt đó hộ người chơi.
- **Vì sao Thủy Tộc giữ luân hồi:** mọi dòng nước đều chảy về **Suối Nguồn** dưới gốc Kiến Mộc (SURV-05). Huyền Vũ (Lão Quy) là kẻ ngồi canh dòng đó. *Người chơi làm gì:* Trung Ấm diễn ra trên mặt nước. Đạo Chủng hiện lên từ nước. Cá tụ hoặc tản theo Linh Quỹ (SURV-06), nên chỉ cần nhìn mặt ao là biết vùng đang Khô Linh hay không, không cần UI.
- Chi phí: chỉ là chữ (~300 từ thay thế), không có asset mới.

### WORLD-02b: Lão Quy (thay Bà Khuẩn)
- **Hình:** rùa già, mai phủ rêu, có một con rắn nước cuộn trên mai (biểu tượng Huyền Vũ). Lão ngồi bất động trên một tảng đá giữa **Ao Gương** (Trung Lâm). Một sprite tĩnh (+0,1 theo PX), mặt nước phản chiếu dùng shader.
- **Ngoài thế giới:** 3 lời chào theo Tâm Hướng, dùng chung template Lão Tùng. **Sinh:** *"Nước trong khi ngươi tới. Ngồi đi."* · **Trung tính:** *"Ừ. Lại một đốm lửa biết bơi."* · **Sát:** *"Nước đục theo bước ngươi. Ta vẫn nhìn."* Nếu người chơi là Oa: *"Lại một đứa còn đuôi. Bơi đi, ta không cõng đâu."*
- **Giọng:** chậm, câu ngắn, hay lặp "ừ". Chỉ dùng từ thuộc trường nghĩa nước (*nước, dòng, gương, chìm, trôi, đục, trong*). Không dùng *nấm, bào tử, ủ, mục*.
- **Pool Trung Ấm 40 câu** (PX cắt từ 60 xuống 40), khoảng 10 nhóm × 4. Câu mẫu:

| Tình huống | Câu |
|---|---|
| FTUE (Tiền Thân chuột) | *"Ngươi đã mang nó cả đời. Giờ nó mang ngươi."* (giữ nguyên) |
| Bị Lang ăn | *"Răng nó nhớ ngươi lâu hơn ngươi nhớ nó. Ừ."* |
| Bị Diều hâu/Vũ giết | *"Trời cũng biết đói. Lần sau, nhìn lên."* |
| Đói | *"Bụng rỗng thì nước cũng lạnh."* |
| Cây chết vì hạn | *"Rễ ngươi khát từ lâu. Nước không giận ai."* |
| Oa chết vì cạn Ẩm | *"Ngươi đi xa nước quá. Nước vẫn chờ."* |
| Nghĩ chết khi bầy đã tan | *"Một con kiến không chết. Chỉ là tổ quên nó."* |
| Bị bồi đòn khi Trọng Thương | *"Kẻ bồi đòn đó… nước nhớ mặt nó."* |
| Chết khi đang mang Sát Nghiệp | *"Nước rửa được máu. Không rửa được tên."* |
| Lần đầu mất trắng ở C≥3 | *"Đừng tìm lại. Nhìn chỗ ngươi ngã đi: có gì đang mọc kìa."* |
| Chết khi đang mang Đạo Chủng | *"Thân ngươi ta trả cho rừng. Hạt kia, ta giữ hộ."* |
| **Viên Mãn** | *"Ngươi đi hết đường rồi. Ta vớt cho ngươi ba hạt. Chọn đi. Ừ."* |

### WORLD-03b: Nước trên map 256²
Có một dòng chính **Linh Tuyền** chảy từ Linh Nhãn ra Bìa Rừng, và hai suối nhánh tỏa ra hai phía còn lại. Nhờ vậy cả bốn góc map đều có nước, Oa không bị nhốt ở một góc. Quy tắc định hướng: **ngược dòng = vào trong**.

| Vòng | Điểm nước | Kích thước (ô) | Sâu? | Ghi chú |
|---|---|---|---|---|
| Linh Nhãn | **Mắt Suối** (đầu nguồn) | 8×8 | không | Điểm Linh Triều. Từ đây nhìn thấy Cột Linh Quang phản chiếu trên mặt nước |
| Thâm Lâm | **Đầm Mục** | ~40×40, lõi sâu ~600 | lõi sâu | **3 bến cạn** là điểm nghẽn PvP. **Liễu Chết** ở ven đầm. Xác phân giải nhanh hơn |
| Trung Lâm | Suối chính (bậc đá) + **Ao Gương** | dòng rộng 3 · ao 12×12 (tâm sâu 4×4) | tâm ao | Lão Quy ngồi ở tâm ao. Đây là nơi người chơi tự tới gặp Lão trong phiên 1–2 |
| Bìa Rừng | 3 cửa suối + **3 Hồ Con** + vũng mưa | Hồ Con 3×3 · ~20 vũng | Hồ Con | **Điểm sinh của Oa** (chống spawn-camp). **Ao Sương** (Mộng Ấn 1) nằm ở một cửa suối |
| **Tổng** | | **≈3.100 ô ≈ 4,7% map** | sâu ≈ 650 ô (1%) | PROG kiểm tra lại nguồn No/CT của Oa với diện tích này |

- Luật ô (Tốc, Ướt, Ẩm, nước sâu chặn loài cạn) theo **bảng địa hình §B của SURV**. Nước sâu là **chỗ lánh, không phải lãnh thổ**: nguồn tu vi ở đó thấp (SURV/PROG).
- Đại Hạn (E6, [1.0]): vũng mưa cạn trước, Hồ Con không cạn. Người chơi thấy nước rút trên map nên biết trước Oa sẽ khó khăn.

### WORLD-04b: Số phận của nấm, Mộng Ấn, E7
- **Nấm là "da của Linh Mạch"**: nó mọc ở chỗ mạch trồi lên hoặc chỗ có xác đang tan. Nấm **không có Mộng Hỏa và không thuộc tộc nào**. Codex: *"Nấm không mộng nên không nhớ. Nó chỉ làm sạch."* Trong game nấm là prop và đồ ăn môi trường: nấm ăn được (No nhỏ), **Tơ Nấm** là nền cho cộng sinh của cây [1.0]. *Người chơi làm gì:* thấy vòng nấm tức là chỗ đó gần Linh Mạch hoặc có xác vừa chết, đây là breadcrumb miễn phí.
- **Mộng Ấn 1:** đổi tên thành **Ao Sương** (theo PX). Vòng nấm tiên vẫn còn nhưng thành prop mọc quanh vũng (giữ lại asset cũ). Đứng soi vũng lúc bình minh sau mưa thì người chơi thấy bóng mình là **một đốm lửa**, không phải hình con vật: *"Ngươi là Mộng Hỏa."*
- **Mộng Ấn 2:** giữ nguyên (Lão Tùng, Thần Bia).
- **Mộng Ấn 3:** bóng người cầm rìu hiện trên **mặt nước Đầm Mục** dưới Liễu Chết, vào đêm trăng tròn. Vẫn là chủ đề *nước nhớ*.
- **E7 Bào Tử Triều → Mưa Vong** [1.0] (tôi bỏ cái tên Triều Mộng của mình). Lý do: tên này nói đúng cơ chế (dùng lại hệ mưa có sẵn), và tránh trùng chữ "Triều" với Đại Linh Triều. Diễn biến: đêm sau một ngày có nhiều cái chết thì mưa 10', ao lan rộng thêm 2 ô, không có lũ. Thắng: Thủy, cây gần nước. Flavor: *"Nước trên trời trả lại những gì nước dưới đất đã nhận."* Bỏ cơ chế "+1 Duyên tại Mộ Linh" vì nó dựa vào đầu thai.
- **E3 Đại Hỏa:** bên thắng đổi từ "nấm" thành "cây tiên phong, cá trong đầm".

### WORLD-07b: Mộc gồm cỏ, Vũ, Thần Vị
- **Cỏ ở MVP có hai dạng, đều không phải loài mới:** (1) cỏ nền là tile (PX-07). (2) **Bách Thảo** là một trong 3 nhánh Đạo Lộ của Linh Mộc (WORLD-11b): cây chọn mọc thấp và lan thành thảm. Linh Thảo là loài thứ hai của Mộc [1.0] và giữ cột tên cảnh giới cũ.
- **Vũ:** Quạ Già vẫn là Sứ giả. Nhãn "Vũ chơi được [Cắt]" đổi thành **Linh Kê [MVP lite]**. MVP chỉ có Sải Cánh (nhảy/lướt ngắn), không dùng chữ "bay" ở MVP (theo SURV). Bay thật chỉ có ở Ưng [Post].
- **Thần Vị (S4, Post), khớp với biome v1.0 mà không phải sửa gì:** Mộc = Rừng Lá Rộng · **Hỏa = Rừng Tro** (Vũ: Hoa Phượng Hỏa đã có sẵn) · **Thổ = Đồng Cỏ** (Trùng: gò kiến) · **Kim = Vách Đá Rêu** (Thú) · **Thủy = Đầm Mục** (Thủy). Mỗi ghế có một "tổ" là vị thần đầu tiên của tộc đó, nhưng **tộc nào cũng nhập vị được**.

### WORLD-10b: Hai cách kết thúc một đời, một luật duy nhất
Câu luật, in trong Biên Niên và đọc bởi Lão Quy: **"Chết giữa đường, ngươi trả lại cho rừng. Đi hết đường, rừng trả lại cho ngươi."**

| | **Chết giữa đường** (E) | **Kiếp thất bại** | **Viên Mãn** (F) |
|---|---|---|---|
| Luật (SURV/PROG chốt) | Đời mới ở C1, không mang theo sức mạnh nào | **Không phải chết.** Lùi tầng/cảnh, giữ thẻ đã chọn | Hoàn thành cảnh cuối của loài |
| Lore | Thân trả sức cho rừng. Mộng Hỏa tắt trong nước rồi nổi lên mới | *"Sét đánh gãy, không đánh tắt."* Thiên Đạo chỉ hỏi, kẻ giết là sinh vật khác. Sét không giết, sinh vật khác giết thì chết thật (đúng Thiên Kiếp v1.0) | Phần mộng đã chín kết thành **Đạo Chủng** |
| Người chơi thấy | Trung Ấm: xác chìm, đốm sáng tản ra. Màn **"Ngươi để lại"**: chỗ Mộ Linh, cây/cỏ mọc ở chỗ ngã, Linh Quỹ +x% | Mây kiếp tan, biểu tượng Đạo Cơ Tổn | Trung Ấm biến thể **"Vớt Chủng"**: Lão Quy vớt 3 hạt sáng lên. Người chơi chọn 1, hai hạt kia chìm xuống |
| Thế giới nhận | Sổ Sinh Năng không đổi. P3 vẫn đúng: cái chết vẫn là hạt giống, chỉ là **của rừng** | — | **Hóa Tích** (WORLD-12b) |

- **Tiền Thân FTUE không tính là một đời** (lore: *giấc mộng đầu*). Vì thế cái chết của chuột ở FTUE không đi qua màn "mất trắng".
- **Đại Kiếp** (E8): mọi đời đều kết thúc, nhưng tôi **không** tính đó là "chết giữa đường". Lore: *"Rừng cùng chết, nên không ai chết một mình."* Không có câu "ngươi trả lại", không mất Đạo Chủng đã có. Người chưa Viên Mãn có được thêm Đạo Chủng hay không: **câu hỏi mở cho PROG và người dùng**. Tôi đề xuất là không, để Viên Mãn giữ được giá trị.
- Chi phí: 2 biến thể shader Trung Ấm + ~12 câu thoại, đã nằm trong khoản +0,3 của PX.

### WORLD-13b: Đạo Chủng
- **Không mất khi chết** (tôi đổi lập trường, theo SURV, PROG và PX). Lore giải thích: Đạo Chủng không nằm trong Mộng Hỏa mà **chìm trong Ao Gương, Lão Quy giữ hộ**. Thứ ngươi tự lớn lên thì trả lại cho rừng. Thứ rừng đã trả cho ngươi thì nước giữ. Câu này nhất quán với E: đời sau vẫn là "hoàn toàn mới" về những gì đời đó tự kiếm được.
- **Trần:** *"Một Mộng Hỏa chỉ ôm được ba hạt."* Lore này khớp với mô hình ô của PROG (1 ô khi Viên Mãn lần 1, 2 ô ở lần 3, 3 ô ở lần 6). Số do PROG/PX chốt.
- **Bậc theo cảnh hoàn thành** (theo SURV/PX, chống farm loài lite): Viên Mãn ở loài lite cho **Đạo Chủng Xanh**. Viên Mãn ở C4 cho **Đạo Chủng Vàng**. Hai bậc chỉ khác màu hạt, không cần asset mới.
- **Qua tộc khác:** Đạo Chủng giữ tên và **kênh Dư Âm** (PROG: Sát/Hộ/Động/Hồi/Thức), rồi **bám vào động từ riêng của tộc mới**. Tooltip có dạng: *"Ý của Truy Huyết, trong thân Oa: Quăng Lưỡi trúng kẻ đang chảy máu…"*. Kênh nào không dịch được sang tộc mới thì **không vào bộ 3 random**, nên không bao giờ có hạt vô dụng.

### WORLD-12b: Hóa Tích (nơi Viên Mãn)
| Tộc | Hóa Tích (1 sprite tĩnh, tint từ art của loài) | Môi trường |
|---|---|---|
| Mộc | Cổ thụ hóa đá | Đứng dưới gốc thì đọc được tên và 1 dòng Biên Niên |
| Thú | **Đá Tru** trên gò | Đêm trăng có tiếng tru ambient |
| Trùng | **Gò Tổ Cổ** | Kiến AI ra vào (swarm có sẵn). Đây cũng là chỗ của Nghĩ Hậu Hóa Thạch [1.0] |
| Thủy | **Mai đá** giữa ao | Cá tụ quanh |
| Vũ | **Lông Đá** trên vách | Có tiếng gió |

- Mọi người trên server đều thấy Hóa Tích. Mỗi vùng tối đa 8 cái, cái cũ nhất mờ dần thành sương (*rừng cũng quên*). Tôi nhận đề xuất của PROG: mỗi Hóa Tích cho **+Linh Quỹ vùng** (PROG đặt số). Đây là thưởng cho cả vùng chứ không cho riêng ai, đúng theme "kẻ nuôi được cả khu rừng".
- **Mộ Linh** (nơi chết, v1.0) và **Hóa Tích** (nơi Viên Mãn) là hai dấu vết khác nhau. Trả lời câu hỏi của SURV: Mộ Linh là điểm tương tác có sẵn (chạm vào đọc 1 dòng). Ngưỡng hiện Mộ Linh nên hạ từ C4+ xuống **C3+** để người chơi loài lite cũng được thấy. SURV/PX chốt.
- Chi phí ~0,3. **Fallback 0,05:** Hóa Tích dùng lại Hoa Mộ Linh với màu vàng.

### WORLD-11b: Tên và flavor của lựa chọn đột phá (D), theo khung Đạo Lộ của PROG
- Hệ thống tên **Đạo Lộ** (PROG). UI vẽ dạng **Niên Luân**: các vòng gỗ đồng tâm, mỗi lần đột phá thêm một vòng, ô ở vòng sau nối vào ô ở vòng trước. Notable cũ "Vòng Niên Luân" bị bỏ cùng hệ Notable nên không trùng tên.
- **Quy tắc tên:** mỗi tên ≤2 từ (vừa màn hình mobile), lấy từ sinh thái thật của loài, và người chơi đoán được tác dụng chỉ từ cái tên. Thẻ Bậc 1 khi lên C4 tự đổi sang tên "dạng mạnh". Tên **Hợp Đạo** = chữ đầu của hai nhánh + tên loài (ví dụ *Huyết Ảnh Lang*).

| Loài | Nhánh (kênh) | Bậc 1 · 2 · 3 | Flavor 1 dòng |
|---|---|---|---|
| Linh Mộc | **Thiết Mộc** (Hộ) | Vỏ Cứng · Gai Ngược · Bàn Căn | *"Ta không đi đâu. Ngươi phải tự đi."* |
| | **Linh Quả Thụ** (Hồi) | Quả Ngọt · Hương Dụ · Vạn Quả | *"Ai ăn quả ta đều mang ta đi xa."* |
| | **Bách Thảo** (Động) | Lan Thảm · Liên Căn · Thảo Hải | *"Cắt một ngọn, mọc trăm ngọn."* |
| Lang | **Huyết Lang** (Sát) | Răng Cưa · Truy Huyết · Huyết Cuồng | *"Máu chỉ đường."* |
| | **Phong Lang** (Động) | Lướt Gió · Vây Bắt · Đầu Đàn | *"Một con sói là răng. Một bầy là bão."* |
| | **Ảnh Lang** (Thức) | Lặng Bước · Khứu Phong · Ảnh Phục | *"Thứ ngươi không thấy là thứ ăn ngươi."* |
| Linh Nghĩ | **Toan Nghĩ** (Sát) | Toan Tiễn · Cắn Bám · Toan Vũ | *"Nhỏ, nhưng đốt."* (kiến tiết axit formic) |
| | **Công Nghĩ** (Hồi) | Vác Nặng · Đường Mùi · Kho Tổ | *"Không gì quá nặng nếu đủ vai."* |
| | **Chức Diệp** (Hộ) | Dệt Lá · Khế Ước · Tổ Treo | *"Cây cho ta nhà. Ta giữ nhà cho cây."* (kiến dệt lá giữ cây) |
| Thanh Oa | **Độc Oa** (Sát) | Da Độc · Lưỡi Tê · Kịch Độc | *"Màu càng đẹp, càng đừng chạm."* |
| | **Thiềm Bì** (Hộ) | Da Sần · Phồng Mình · Kim Thiềm | *"Xấu mà sống lâu."* |
| | **Cáo Thiên** (Hồi) | Gọi Mưa · Dẫn Dòng · Kiện Trời | *"Con cóc là cậu ông Trời."* (truyện Cóc kiện Trời) |
| Linh Kê | **Đấu Kê** (Sát) | Cựa Sắc · Hạ Cánh Đạp · Chọi Lửa | *"Nhỏ con, lớn gan."* |
| | **Viễn Mục** (Thức) | Mắt Ngọn · Dò Gió · Thiên Nhãn | *"Kẻ thấy trước không cần chạy nhanh."* |
| | **Mẫu Dực** (Hộ) | Xòe Cánh · Gọi Bầy · Cánh Che | *"Dưới cánh mẹ, diều hâu không thấy gì."* |

- **Thiên Phú Tộc** (thẻ thứ 4 của PROG, nâng cấp động từ riêng): Mộc **Thâm Căn** · Lang **Linh Tị** · Nghĩ **Vạn Túc** · Oa **Trường Thiệt** · Kê **Báo Hiểu**.
- Mỗi tộc có ít nhất một nhánh sống sót (Hộ hoặc Hồi), đáp ứng luật của SURV.
- Tổng **45 tên bậc + 15 nhánh + 5 Thiên Phú**. Chỉ là chữ, chi phí 0. Hiệu ứng và số do PROG viết.

### WORLD-14b: Động từ riêng theo phía lore (G)
| Tộc | Động từ | Vignette mở đầu đời (≤3s, dùng lại sprite) | Hint lần đầu luân hồi vào tộc (1 câu) |
|---|---|---|---|
| Mộc | Bén Rễ | Hạt nứt, mầm nhú lên | *"Kéo rễ về chỗ đất ẩm."* |
| Thú | Đánh Hơi | Mở mắt trong hang | *"Giữ để ngửi. Máu để lại vệt, nước xóa vệt."* |
| Trùng | Tha | Nở từ trứng trong tổ, Lính bò ra | *"Mang về tổ. Tổ nhớ mọi thứ ngươi mang."* |
| Thủy | Quăng Lưỡi / Lặn | Trứng nở trong Hồ Con | *"Ở cạn da ngươi khô. Nước là nhà, là đường."* |
| Vũ | Gáy | Phá vỏ trứng dưới Tán | *"Gáy một tiếng: bầy ngươi thấy, kẻ rình cũng lộ."* |
- Lore cho khung chung: *"Cùng một Mộng Hỏa, khác thân thể."* Vì vậy HUD, needs, cảnh giới và Niên Luân là một bộ dùng chung, chỉ có động từ là khác. Fallback: bỏ vignette, chỉ hiện dòng hint.

### WORLD-15 (mới): Tên cảnh giới (thay §6.2, theo quy tắc Hán-Việt 2–4 âm tiết)
| C | Khung | Linh Mộc | Lang | **Linh Nghĩ** | **Thanh Oa** | **Linh Kê** | Linh Thử [1.0] | Linh Thảo [1.0] |
|---|---|---|---|---|---|---|---|---|
| 1 | Khai Linh | Manh Nha | Ấu Lang | **Ấu Nghĩ** | **Khoa Đẩu** | **Sồ Kê** | Khai Trí | Phá Thổ |
| 2 | Luyện Khí | Trát Căn | Lang Nha | **Lập Sào** | **Thoát Vĩ** | **Đề Minh** | Tàng Thực | Liên Căn |
| 3 | Trúc Cơ | Thành Tán | Lang Cốt | **Thành Quần** | **Đăng Ngạn** | **Triển Dực** | Ẩn Huyệt | Thành Thảm |
| 4 | Kết Đan | Ngưng Tâm Mộc | Lang Đan | **Nghĩ Đan** | **Oa Đan** | **Kê Đan** | Thử Đan | Ngưng Dược Tính |
| 5 | Hóa Hình | (giữ) | (giữ) | Nghĩ Nhân ‖ **Yêu Nghĩ** | Oa Nhân ‖ **Thiềm Yêu** | Kê Nhân ‖ **Yêu Kê** | (giữ) | (giữ) |
| 6 | Nguyên Anh | Mộc Hồn | Nguyệt Lang Hồn | Địa Sào Hồn | Huyền Thủy Hồn | **Chu Tước Hồn** | Thử Hồn | Vạn Diệp Hồn |
| 7 | Thành Thần | Mộc Thần | Lang Thần | Nghĩ Thần | Oa Thần | **Phượng Thần** | Thử Thần | Bách Thảo Thần |

- **Tên khớp với cơ chế:** Oa *Khoa Đẩu* (蝌蚪, nòng nọc): ếch con còn cuống đuôi, lên cạn được nhưng Ẩm cạn nhanh, ăn tảo và xác chìm. *Thoát Vĩ* là lúc rụng đuôi: đổi sang ăn côn trùng, Ẩm cạn chậm hơn. *Đăng Ngạn* là lên bờ hẳn. Nghĩ *Lập Sào* là lập tổ, bắt đầu Tha. *Thành Quần* là có bầy, mở Căn Thương (song song với *Thành Tán* của Mộc). Kê *Đề Minh* là tiếng gáy đầu tiên. *Triển Dực* là sải cánh xa hơn. *Chu Tước Hồn* khớp Vũ = Hỏa.
- **Xóa** cột Khuẩn, cột Trùng [Post] (thay bằng Linh Nghĩ) và câu "Tầng thứ 4 … là Viên Mãn". **Viên Mãn** từ nay chỉ có một nghĩa: hoàn thành cảnh cuối của một đời.
- **Kiếp cuối** của đời được hiển thị trên UI là **Viên Mãn Kiếp**, dù bên dưới là template nào (Tiểu Kiếp cho loài lite, Trung Kiếp cho C4). PROG chốt template.

### WORLD-17 (mới): Chỗ chữ trong FINAL v1.0 cần sửa (phần lore và tên)
| Mục | Cũ | Mới |
|---|---|---|
| §0 #1, §1.1 USP | "cổ thụ, chuột hay sói" | "cổ thụ, sói, kiến, ếch hay gà rừng". Hook trailer về chuột giữ nguyên (chuột là FTUE) |
| §0 #2 | Hậu Duệ / Luân Hồi / Túc Tuệ | "Chết giữa đường thì trả lại cho rừng và bắt đầu mới. Đi hết đường (Viên Mãn) thì mang 1 Đạo Chủng sang đời sau." |
| §1.2 P3 / P4 | "Trung Ấm, Đạo Quả, FTUE chuột → cây" | "Trung Ấm, Sổ Sinh Năng (cây mọc ở chỗ ngã), Viên Mãn/Đạo Chủng, FTUE chuột → cây". P4 thêm **Hóa Tích** |
| §2.1 S1–S3, S4 | — | Theo WORLD-01b và WORLD-07b |
| §2.3, §2.4 | vòng nấm tiên; Đầm Mục | Thêm cột Nước theo WORLD-03b. Mộng Ấn 1 → Ao Sương. Mộng Ấn 3 bóng hiện trên mặt đầm |
| §2.6 | Mộ Linh C4+ | Mộ Linh C3+, thêm Hóa Tích (WORLD-12b) |
| §2.7 | bảng 6 thế lực có **Khuẩn Tộc / Bà Khuẩn** | Bảng WORLD-05b. Thêm dòng: *"Vũ Tộc là mắt và miệng của rừng."* |
| §4.1 | Khuẩn [1.0]; Trùng [Post]; Linh Thử MVP | Theo WORLD-05b |
| §4.2 | dòng Khuẩn | Xóa. PROG thêm 3 dòng cho loài lite |
| §4.3 | "Linh Thử gặm chồi" · "Độn Thử đào" · "Cộng sinh Ong/Nấm" | "Thử AI gặm chồi" · Căn Thương do Linh Nghĩ (số theo SURV/PROG) · "Cộng sinh Ong/Tơ Nấm" |
| §5.5 | "Rễ/nấm trong 3 ô" | "Rễ (cả Bách Thảo) trong 3 ô. Xác sát nước thì phần này chảy vào nước" (SURV chốt) |
| §5.7 | "cây và nấm", "cây-nấm", "cây/nấm" | "cây" |
| §5.8 | Quạ Linh, Diều hâu | Gắn nhãn Vũ Tộc. Sâu Lửa và Kiến AI gắn nhãn Trùng Tộc |
| §6.2 | bảng cũ | WORLD-15 |
| §6.4–6.5 | Huyết Mạch có Hành; Notable "chuyển qua Túc Tuệ" | Đạo Lộ (PROG) + tên WORLD-11b. Bỏ nhãn Hành ở cấp nhánh |
| §6.7 | Nguyên Thần Bất Diệt "tính như Hậu Duệ" | "thoát ra, về Linh Huyệt trong 60s thì không chết" [Post], PROG chốt |
| §7.1–7.2 | Bà Khuẩn; timelapse Hậu Duệ; Hậu Duệ/Túc Tuệ | Lão Quy; bỏ timelapse; thêm WORLD-10b (màn "Ngươi để lại", màn Vớt Chủng). Tiền Kiếp Ấn giữ (cosmetic) |
| §9.1 | "Ta để lại gì?" | Giữ. Đây chính là câu hỏi của Đạo Chủng và Hóa Tích |
| §10 | E7 Bào Tử Triều; E3 "nấm"; E2 "Thua: Linh Thử ở Trung Lâm" | **Mưa Vong**; "cá trong đầm"; "Thua: con mồi nhỏ (Kê, Oa ở cạn)". E6 Đại Hạn thêm "Thua: Oa" |
| §12 FTUE | 0:40; 14:00 Bà Khuẩn; 15:30 "3 loài"; 16:00 "Hồi Ức ×3"; ~20:00 Tự Quy | 0:40 có thêm vignette kiến khiêng hạt (tùy chọn) · 14:00 **Lão Quy** nói nguyên câu cũ · 15:30 bánh xe **5 tộc** · 16:00 "đường cong Tiền Thân" (PROG) · Tự Quy = "kết thúc đời này, đi đời khác" |
| §19 Thuật ngữ | — | **Thêm:** Lão Quy, Ao Gương, Linh Tuyền, Hồ Con, Ẩm, Ướt, Đạo Lộ, Niên Luân, Dư Âm, Đạo Chủng, Viên Mãn, Viên Mãn Kiếp, Hóa Tích, Mưa Vong, Trọng Thương. **Bị loại:** Khuẩn Tộc, Bà Khuẩn, Bào Tử Triều, Cụ Ngao, Triều Mộng, Nghiệp Ấn, Hậu Duệ, Túc Tuệ, Ổ Hậu Duệ |

---

## Những thứ tôi mượn từ người khác
- **SURV-03 (R1):** vòng Hành Thú = Kim, Vũ = Hỏa, Trùng = Thổ. **SURV-05:** Suối Nguồn, Lão Quy. **SURV-06:** cá là chỉ báo Linh Quỹ. **SURV §B:** bảng địa hình, Hồ Con, Ẩm. **SURV-R2-01/02/03:** kiếp thất bại không phải chết, Trọng Thương, Sát Nghiệp theo cảnh.
- **PROG-R2-01:** khắc là cơ chế, ô Q. **PROG-R2-02:** khung Đạo Lộ (3 nhánh × 3 bậc + Thiên Phú + Hợp Đạo). **PROG-R2-04:** kênh Dư Âm, ô di sản 1/2/3, Hóa Tích cho +Linh Quỹ vùng. **PROG-05:** Bách Thảo.
- **PX-05:** Ao Sương, Mưa Vong. **PX:** 4 cộng sinh thật, thẻ bánh xe ≤6 chữ, màn "Ngươi để lại", fallback hoãn cả loài, sự kiện "Giáng Lâm".

## Lập trường giữ vững (và vì sao)
1. **Vòng Hành Ngũ Hành + Tứ Tượng, không dùng vòng Mộc→Thú→Trùng→Vũ→Thủy (PX, SURV R2).** PROG đã chứng minh hai cách xếp có cùng cấu trúc, nên chỉ cần chọn theo chủ đề. Năm lý do:
   - (a) **10/10 cặp có hình ảnh vật chất** (bảng WORLD-06b). Vòng của PX có Vũ→Thủy và Vũ⊣Mộc yếu.
   - (b) **Thú ⊣ Mộc** đúng với trục PvP chính của v1.0 (sói làm cây Đổ). Vòng của PX gọi quan hệ đó là "Mộc sinh Thú".
   - (c) **Vũ ⊣ Thú** đúng với cái chết đầu tiên của game (diều hâu săn chuột ở FTUE).
   - (d) Thần Vị S4 khớp với biome v1.0 mà không phải sửa (Rừng Tro + Hoa Phượng Hỏa = Hỏa = Vũ).
   - (e) Người chơi tu tiên tự đoán ra được nhờ Bạch Hổ và Chu Tước.
   - Điểm yếu thật của vòng này là Vũ→Trùng và Trùng→Thú. Tôi xử lý bằng tooltip vật chất ("Đất bới nuôi bầy", "Xác mở nuôi thú") và một cơ chế data cho mỗi cặp.
   - **Điều kiện đổi ý:** playtest HN2' cho thấy <50% tester giải thích được một cặp sinh/khắc bất kỳ sau khi đọc tooltip, trong khi vòng của PX đạt cao hơn.
2. **Luật một Hành mỗi tộc** (Hành là thân, Đạo là ý). Nếu nhánh cũng mang Hành thì ma trận đổi theo build mà người chơi không được báo (SURV đã nêu ở PROG-03).
3. **NPC luôn khác loài chơi được**, và **Hóa Tích tách khỏi Mộ Linh**. Hai thứ đó kể hai cái kết khác nhau.

## Điều tôi sẵn sàng đánh đổi
- **Hóa Tích** có thể xuống fallback Hoa Mộ Linh màu vàng (−0,25).
- **Vignette mở đầu đời** có thể thay bằng 1 dòng chữ (khoảng −0,1).
- **Rắn trên mai Lão Quy** có thể bỏ nếu sprite trễ.
- **Tên C5–C7** của 3 loài mới để [Post], chỉ khóa C1–C4.
- Quăng Lưỡi có thể bỏ hẳn kéo (theo SURV), **miễn là tên và động từ "lưỡi" vẫn còn** (chậm + Ướt).
- Không đánh đổi: Lão Quy giữ luân hồi bằng nước, câu luật "trả lại cho rừng / rừng trả lại cho ngươi", Đạo Chủng hiện lên từ nước, và nấm không thuộc tộc nào.
