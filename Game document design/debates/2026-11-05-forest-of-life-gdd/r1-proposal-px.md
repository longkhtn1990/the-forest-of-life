# R1 Proposal — PX

> Domain: player persona, USP & thị trường, FTUE, UI/UX đa nền tảng, PvP & bảo vệ người mới, mô hình server, kinh tế & monetization, retention/live-ops, session & offline, tech stack, scope/MVP, rủi ro, playtest.
> Vai trò: red team. Tôi sẽ nói thẳng chỗ nào trong brief đang tự mâu thuẫn, nhưng mỗi lần chỉ ra đều kèm cách giữ tinh thần ý tưởng.

## 1. Cách tôi hiểu yêu cầu

Người dùng muốn một game **sinh tồn – tiến hóa – tu tiên** đặt trong một khu rừng sống. Người chơi là *bất kỳ* sinh mệnh nào (cây, cỏ, nấm, côn trùng, thú). Mỗi loài lên "tu vi" theo cách riêng, cảnh giới có tên riêng nhưng mạnh ngang nhau. Chết là **luân hồi**, tức là một phần của tiến trình chứ không phải kết thúc. Thế giới **luôn PvP tự do** và có sự kiện toàn rừng, chạy trên **Web/Mobile/PC**, mỗi lần chơi **15–60 phút**, kéo dài nhiều tuần. Game **F2P**, do **1 người + AI** làm.

Các giả định tôi đặt ra (có thể tranh luận):
- **A1:** Thị trường chính là người đọc/xem tiên hiệp (VN, SEA, Trung Quốc, cộng đồng webnovel toàn cầu) và người chơi `.io`/survival casual trên web/mobile. Fan hardcore kiểu The Isle không phải thị trường chính.
- **A2:** "PvP luôn bật" nghĩa là **không có công tắc PvP** ở thế giới chung. Nó không có nghĩa là "không có luật". Thiên Đạo (luật thế giới) được phép điều tiết hậu quả của PvP.
- **A3:** Với 1 người làm và F2P bằng ads, **chi phí server trên mỗi người chơi phải gần 0** cho đến khi game chứng minh được retention. Vì vậy server lớn là giai đoạn sau, đúng với cụm "server tùy chọn" của người dùng.
- **A4:** Rừng Cổ Đại "khổng lồ" là **cảm giác** hùng vĩ (camera, âm thanh, quy mô sinh vật, lore). Nó không nhất thiết là một map liền mạch 100 km².

## 2. Ý tưởng cốt lõi (hook)

**USP (1 câu):** *Game tu tiên duy nhất mà bạn không chỉ là tu sĩ, bạn có thể là một cái cây, một cây nấm hay một con sói. Mỗi kiếp sống là một con đường đạo khác nhau, và cái chết chỉ là bước luân hồi sang kiếp kế tiếp.*

**Hook trailer/store (1 câu):** *"Kiếp này em là ngọn cỏ bị dẫm nát. Kiếp sau em là cổ thụ nuốt trọn cả bầy sói."*

## 3. Đề xuất chi tiết

### PX-01: Ba persona mục tiêu
- **Mô tả & số liệu:**

| Persona | Nền tảng | Session | Động lực (Quantic Foundry) | Họ cần gì | Họ sợ gì |
|---|---|---|---|---|---|
| **P1 "Đạo hữu xe buýt"**, 18–30t, đọc truyện tiên hiệp, chơi game tu tiên mobile idle | Mobile/Web | 10–20', 2–3 lần/ngày | Completion, Power, Fantasy | Cảm giác "đột phá" đều đặn, tiến trình vẫn chạy khi offline, tên cảnh giới đậm chất | Mất tiến độ, bị người khác cướp công sức |
| **P2 "Kẻ săn mồi"**, 16–28t, fan The Isle/Path of Titans/mope.io | PC/Web | 45–90' | Competition, Destruction, Excitement | Săn người thật, nỗi sợ và adrenaline của chuỗi thức ăn | Bị grief vô nghĩa, lớn lên chậm như The Isle (4–6 giờ mới thành thể apex) |
| **P3 "Người làm vườn"**, 20–40t, thích cozy/strategy/Don't Starve | PC/Mobile | 20–40' | Design, Strategy, Discovery | Mọc rễ, lan rộng, xây hệ sinh thái cộng sinh, thấy rừng thay đổi vì mình | Hành động nhanh, PvP twitch |

- **Quy tắc:** mỗi hệ thống trong GDD phải ghi rõ nó phục vụ persona nào. Thực vật phục vụ P3 + P1 (vì có offline progress). Thú phục vụ P2 + P1.
- **Tình huống:** P1 chơi Linh Mộc trên mobile 12 phút lúc ăn trưa, rồi bế quan. Tối về, P1 thấy rễ đã lan thêm 3 ô và có 1 con sói (P2) bị gai độc của cây làm trọng thương trong đêm.
- **Vì sao tốt:** Brief đang ôm 3 audience trái ngược nhau. Gọi tên chúng ra thì team mới thấy được xung đột (PvP twitch đối đầu với cozy) và thiết kế sự **bất đối xứng có chủ đích** giữa các giới.

### PX-02: Bản đồ đối thủ và khoảng trống thị trường

| Game | Điểm mạnh nên học | Điểm cộng đồng phàn nàn | Bài học cho chúng ta |
|---|---|---|---|
| **The Isle** | Nỗi sợ thật, chuỗi thức ăn người-với-người | Growth 4–6 giờ cho apex, KOS (kill on sight), toxic, người mới bị ăn ngay | Thời gian lớn phải **ngắn & có ý nghĩa**, chết phải **có thưởng** |
| **Path of Titans** | Cross-platform kể cả mobile, quest đi kèm growth thụ động | Map mobile vắng, tìm thức ăn lâu | Phải có **mật độ sự kiện**. Rừng vắng 5 phút = người chơi bỏ |
| **Spore** | Fantasy "tiến hóa từ nhỏ đến lớn" | Mỗi giai đoạn nông, chơi xong 1 lần là hết | Tiến hóa cần **build có ý nghĩa** và replay qua luân hồi |
| **Eco** | Hệ sinh thái thật, hành động người chơi làm thay đổi thế giới | Chậm, phức tạp, server tốn | Rừng biến đổi phải **đọc được bằng mắt**, không chỉ là con số |
| **Don't Starve / Rain World** | Không khí, thế giới thù địch đẹp, học qua thất bại | Khó vào, khá trừng phạt | Học qua cái chết được, nhưng **5 phút đầu phải vui** |
| **mope.io / evowars / flyordie** | Vào game trong 5 giây, tiến hóa mỗi 1–2 phút, PvP tự do vẫn vui | Không có tiến trình dài, chết là mất hết | Mượn **nhịp tiến hóa nhanh của .io** cho đầu game, rồi gắn với meta dài hạn |
| **Game tu tiên mobile (idle/MMO Trung Quốc)** | Tên cảnh giới, đột phá, offline progress, nghiện ngắn hạn | Pay-to-win, VIP, dark pattern, gameplay chỉ là bấm nút | Giữ **cảm giác đột phá**, bỏ **P2W**, thêm gameplay thật |

- **Khoảng trống:** chưa game nào kết hợp được **(1) chơi được thực vật** + **(2) luân hồi giữa các loài** + **(3) khung tu tiên** + **(4) vào game nhanh như .io trên web/mobile**. Ghi chú trung thực: tôi không tìm được số retention công khai đáng tin cho mope.io/evowars (search 2026 chỉ ra dữ liệu traffic rời rạc, iOS mope.io chỉ khoảng 7,5K MAU). Thể loại .io thuần đã bão hòa, nên **chúng ta không được bán như một game .io**. Chỉ mượn nhịp đầu game của nó.

### PX-03: Ba mâu thuẫn trong brief và cách gỡ
Tôi nói thẳng: nếu làm đúng nguyên văn brief, game sẽ có các khoảnh khắc khiến người chơi gỡ game.

| # | Mâu thuẫn | Tình huống tệ nhất | Cách gỡ (giữ tinh thần) |
|---|---|---|---|
| M1 | **PvP tự do + cây bất động** | Cây của tôi cày 2 tuần, bị 1 con gấu cấp cao ăn hết trong 40 giây lúc tôi đi ngủ | PX-04 (Bế Quan) + đề xuất cho SURV/PROG: cây có **Đạo Căn** dưới đất. Ăn lá không giết được cây. Muốn giết cây phải đào/vây Đạo Căn ≥3 phút khi chủ online, và **không thể giết khi chủ đang bế quan** |
| M2 | **Session 15' + tiến trình nhiều tuần + PvP luôn bật** | P1 mất 3 tuần tu vi vì bị gank 10 giây | Luân hồi biến cái chết thành **thu hoạch meta** (PX-06). Chênh lệch sức mạnh giữa các cảnh giới bị **nén** trong thế giới PvP (PX-05) |
| M3 | **"Thành thần" endgame + PvP + server lâu dài** | Sau 2 tháng, server có 5 "thần" chiếm cả rừng và người mới không còn chỗ thở | **Thành thần = Phi thăng rời khỏi chuỗi thức ăn** (PX-07). Thần trở thành một thực thể trong world event, không còn đi săn người mới |
| M4 | **F2P bằng ads + server real-time + 3 nền tảng + 1 người** | Hết tiền server trước khi có đủ DAU, hoặc kiệt sức vì port 3 nơi | Web-first, 1 codebase TypeScript, server chỉ dành cho chế độ chia sẻ có opt-in (PX-09, PX-13) |
| M5 | **Rừng Cổ Đại khổng lồ + 2D + 1 người** | Map to nhưng rỗng | Cảm giác "khổng lồ" đến từ sinh vật khổng lồ, camera zoom-out khi đột phá và vùng đóng/mở theo sự kiện. Không phải từ diện tích (A4) |

### PX-04: "Bế Quan" giải quyết câu hỏi "cây của tôi ra sao khi tôi tắt máy?"
- **Mô tả:** Thoát game ở thế giới chung = **bế quan**, một trope tiên hiệp có sẵn nên người chơi hiểu ngay. Thân thể nhập vào **Kén Bế Quan**: thực vật thu Đạo Căn xuống đất, thú về hang ổ, côn trùng/nấm vào kén.
- **Quy tắc (con số ban đầu, PROG cân lại):**
  - Chỉ bế quan an toàn được trong **lãnh địa của mình** (cây) hoặc **hang ổ đã đánh dấu** (thú). Nếu thoát giữa đồng, thân thể mất **60 giây "nhập định"**: hiện rõ trên map và vẫn bị tấn công được. Đây là luật chống combat-log.
  - Khi bế quan: **thân không thể bị giết**, nhưng **lãnh thổ ngoài thì có**. Rễ ngoài, hạt giống, tổ ong cộng sinh vẫn bị ăn/phá được. Người chơi mất tối đa **25% lãnh thổ ngoài cho mỗi lần offline**. Tự vệ thụ động (gai, độc, ong) vẫn hoạt động và **cho EXP khi gây sát thương**.
  - Offline cultivation: được **60% tốc độ tu luyện thụ động**, trần **8 giờ**. Không bao giờ được đột phá cảnh giới khi offline. Đột phá luôn là khoảnh khắc người chơi tự trải qua.
  - Khi quay lại: **"Thiên Thư báo mộng"**, một màn tóm tắt 10 giây theo dạng tin tức (rừng đã xảy ra gì, ai đã xâm phạm, bạn thu được gì, có sự kiện nào sắp tới).
- **Tình huống:** 23h, P3 đóng app. Đêm đó sói P2 gặm 18% rễ ngoài, bị gai độc làm trúng độc nên phải bỏ đi. 7h sáng, P3 nhận báo mộng: "Rễ ngoài bị xâm phạm 18%. Gai độc đã khiến [Hắc Lang] trọng thương. +340 tu vi bế quan." P3 có lý do để vào game: mọc lại rễ và nâng cấp gai.
- **Vì sao tốt:** Thế giới PvP vẫn chạy thật (P2 vẫn có mồi, lãnh thổ vẫn biến động), nhưng nỗi sợ "mất tất cả khi ngủ" thì bị loại bỏ. Báo mộng chính là **D1 hook**.
- **Solo/offline:** thế giới **giả lập catch-up** khi mở lại (mô phỏng tóm lược N giờ, tối đa 8 giờ), không cần server.

### PX-05: PvP tự do có Thiên Đạo, tức là chống "ma cũ bắt nạt ma mới" mà không tắt PvP
Không có công tắc PvP. Thay vào đó, **Thiên Đạo trả giá cho hành vi bắt nạt**:
1. **Linh Quang Hộ Thể (người mới):** áp dụng trong **45 phút chơi đầu tiên hoặc đến hết cảnh giới 1** (cái nào đến trước). Người chơi khác **có thể** tấn công, nhưng sát thương lên người mới **bị giảm 70%** và **không nhận EXP/thức ăn** từ họ. Kẻ nào tấn công sẽ bị đánh dấu "Bất Nhân" trên map trong 5 phút. Vậy là không cấm, nhưng không có lợi.
2. **Luật chênh cảnh giới (Nghiệp Lực):**

| Chênh lệch cảnh giới (kẻ giết – nạn nhân) | EXP kẻ giết nhận | Nghiệp lực | Nạn nhân nhận khi luân hồi |
|---|---|---|---|
| ≤0 (giết người mạnh hơn/bằng) | 150% / 100% | 0 | Đạo tâm bình thường |
| +1 | 60% | +1 | +20% Đạo tâm |
| ≥+2 | 0% | +3 | **+50% Đạo tâm ("Oán linh")** |

   Nghiệp lực ≥5 khiến **Thiên Kiếp lần sau khó hơn** (thêm 1 đợt sét) và **hiện vị trí trên map** cho mọi người chơi. Như vậy kẻ cày newbie tự biến mình thành **mục tiêu săn thưởng**, và nội dung này do chính PvP tạo ra.
3. **Vùng theo độ sâu:** vùng ngoài (Rừng Non) **giới hạn cảnh giới tối đa** người chơi được lưu lại. Người vượt trần sẽ bị "linh khí loãng" (–2% HP/phút). Lý do trong lore: linh khí vùng ngoài quá mỏng với đại năng. Đây là vùng an toàn **mềm**: không cấm vào, chỉ không đáng để ở lại.
4. **Nén sức mạnh trong PvP (đề xuất cho PROG):** tiểu thuyết tiên hiệp có chênh lệch 100 lần giữa cảnh giới, nhưng game PvP thì không chịu nổi. Đề xuất **mỗi cảnh giới mạnh hơn khoảng 1,6–1,8 lần cảnh giới dưới về "combat power"**, để 3 người cảnh giới N vẫn hạ được 1 người cảnh giới N+1. Cảm giác "vượt cấp" vẫn còn qua visual, skill mới và độ kiếp. Mô típ "nghịch thiên vượt cấp giết địch" là trope được yêu thích, nên phải để nó **có thể xảy ra**.
- **Tình huống:** Sói cảnh giới 4 (P2) gặp thỏ cảnh giới 1 (P1). Ăn thỏ được 0 EXP, +3 nghiệp, vị trí bị lộ. P2 sẽ học được rằng đi săn cùng cấp hoặc săn AI mới có lời. P1 nếu có bị ăn thì vẫn nhận +50% Đạo tâm và luân hồi nhanh hơn.
- **Vì sao tốt:** PvP vẫn tự do và chuỗi thức ăn vẫn thật, nhưng **động cơ kinh tế của griefing bị đảo ngược**.

### PX-06: Cái chết là thu hoạch, mất mát có trần
- **Quy tắc (PROG cân lại):** Khi chết, chuyển **20–35% tổng tu vi kiếp này thành Đạo Tâm** (meta). Tỉ lệ cao hơn nếu chết trong độ kiếp hoặc chết vì oán linh. Mất toàn bộ chỉ số thân xác. Giữ lại: Đạo Tâm, các "Ký Ức Huyết Mạch" đã mở (unlock loài/nhánh) và cosmetic. Xác chết biến thành **Linh Thổ**: ô đất màu mỡ trong 10 phút, ai trồng/ăn ở đó được buff. Nếu người chơi đầu thai làm cây ngay chỗ đó thì được +30% tốc độ đầu kiếp.
- **Thời gian quay lại game sau khi chết:** **≤20 giây** từ lúc chết đến khi điều khiển kiếp mới (màn luân hồi bỏ qua được sau lần đầu). Kiếp mới đạt "trạng thái có quyết định thú vị" trong **≤90 giây**.
- **Vì sao tốt:** Đây là điểm xoay của M2. Theo SDT: chết không làm mất **Competence** (đạo tâm vẫn tăng), mà còn tăng **Autonomy** (được chọn loài mới).

### PX-07: "Phi Thăng" là endgame thành thần mà không phá server
- **Mô tả:** Khi đạt cảnh giới cuối và vượt Đại Thiên Kiếp, người chơi **phi thăng**: rời khỏi chuỗi thức ăn của server hiện tại và trở thành **Thần Rừng** của rừng đó. Danh hiệu, tượng/cây thần mang tên họ tồn tại vĩnh viễn trên map, và có một world event mang tên họ (vd "Thần Ân của [tên]": 1 lần/kỷ nguyên, hạ phàm một pháp thân 15 phút làm boss/thần hộ mệnh).
- **Quy tắc:** người phi thăng bắt đầu kiếp mới ở **cấp rừng lớn hơn** (Rừng Non → Nguyên Sinh → Cổ Đại) với một bộ ưu thế meta. Đây chính là thang **"nhiều cấp map/server theo quy mô"** trong brief, giờ có ý nghĩa tiến trình.
- **Vì sao tốt:** Giải quyết M3 (người mạnh nhất tự rời bàn chơi), cho P1/P2 một **mục tiêu dài hạn có tên và có mặt trong thế giới**, và cho live-ops nội dung do người chơi sinh ra.

### PX-08: FTUE 20 phút đầu
**Nguyên tắc:** kiếp đầu tiên **bị khóa là một con thú nhỏ** (đề xuất: Linh Thử, chuột linh). Lý do: hành động trực tiếp thì vui ngay trong 30 giây đầu. Thực vật cần hiểu hệ thống trước rồi mới vui được. **Luân hồi phải xảy ra trong FTUE** vì đó là USP. Nếu người chơi bỏ game trước khi chết lần đầu, họ chưa hề thấy game của chúng ta.

| Phút | Hành động | Học được | Cảm xúc | Phần thưởng |
|---|---|---|---|---|
| 0:00–0:30 | Màn mở: một linh hồn rơi xuống rừng, chạm vào để "thức tỉnh". Không có menu, không có text dài | Chạm/kéo để di chuyển | Tò mò, đẹp | Thức tỉnh: tên cảnh giới "Linh Thử – Khai Trí" hiện lên |
| 0:30–3:00 | Ăn hạt linh thảo phát sáng, thanh tu vi đầy dần | Ăn = tu vi | Thỏa mãn nhỏ liên tục | Lên tiểu cảnh mỗi khoảng 60 giây (nhịp .io) |
| 3:00–5:00 | Bóng diều hâu AI lướt qua. Trốn vào bụi cây | Có kẻ săn mồi, trốn/chạy | Hồi hộp lần đầu | Sống sót: +tu vi "Cảnh Giác" |
| 5:00–8:00 | **Đột phá cảnh giới 1** (mini độ kiếp: 3 tia sét nhỏ, né bằng kéo) | Đột phá = khoảnh khắc lớn | **Hùng tráng** (mốc fun #1) | Chọn **nhánh tiến hóa đầu tiên** (2 lựa chọn: Tốc / Độc) |
| 8:00–11:00 | Dùng skill mới, săn côn trùng AI, gặp **1 cái cây biết phản kích** (AI Linh Mộc bắn gai) | Thực vật là sinh mệnh có ý thức, có thể nguy hiểm | Ngạc nhiên ("cây cũng đánh mình?") | Hạt giống bí ẩn rơi ra |
| 11:00–14:00 | Linh khí triều dâng (mini world event), đối thủ mạnh xuất hiện (sói AI scripted) | Sự kiện rừng | Căng thẳng | Chết là **gần như chắc chắn** (có thể thoát nếu chơi rất giỏi, khi đó được achievement) |
| 14:00–16:00 | **Luân hồi lần đầu:** xác hóa linh thổ, nhìn thấy hoa mọc lên từ chính xác mình. Đạo tâm +. Bánh xe luân hồi mở 2 lựa chọn: Linh Thử (lại) hoặc **Hạt Linh Mộc** | Chết = tiến trình, có thể đổi loài | **Xúc động** (mốc fun #2), "à, game này là vậy" | Mở loài thứ 2 |
| 16:00–20:00 | Chơi cây: mọc rễ bằng chạm-kéo trên map, quang hợp theo nắng, gai đầu tiên đâm con thỏ AI | Gameplay thứ hai hoàn toàn khác | Khám phá, quyền lực chậm | Tiểu cảnh "Mộc – Manh Nha". Gợi ý bế quan: "Cây sẽ tiếp tục lớn khi bạn rời đi" → **D1 hook** |

- **Mục tiêu đo:** ≥80% người chơi đạt phút 5 (đột phá 1). ≥60% đạt luân hồi lần đầu. ≥40% thử loài thứ 2.
- FTUE chạy **100% offline/solo với AI**. Sau khi xong FTUE mới mở "Rừng chung".

### PX-09: Mô hình server theo bậc, khả thi cho 1 người
| Bậc | Chế độ | Kỹ thuật | Chi phí/ước lượng | Khi nào |
|---|---|---|---|---|
| T0 | **Solo** (offline, AI) | Sim local, lưu local + cloud save đơn giản | ≈0 | MVP |
| T1 | **Co-op bạn bè 2–4 người** (private, PvP với AI, có thể bật PvP nội bộ) | Phòng relay/host trên cùng server game (room nhỏ) | Rất thấp | MVP |
| T2 | **Rừng Non chung**: 24–40 người/phòng, PvP luôn bật, kỷ nguyên 14 ngày rồi reset bản đồ (meta giữ) | Server authoritative (Colyseus/Node), tick 10–15 Hz, state 2D gọn | 1 VPS ~2 vCPU (~5–10 €/tháng) ước chứa khoảng 150–250 CCU (**phải benchmark**). Với CCU/DAU ≈ 1:12, 10K DAU cần khoảng 4–6 VPS ≈ 50 €/tháng | Soft launch |
| T3 | **Rừng Nguyên Sinh**: 80–120 người, kỷ nguyên 28 ngày, vào được sau khi phi thăng Rừng Non hoặc đủ Đạo Tâm | Như T2, thêm interest management/zone | ×2–3 chi phí/người | Sau launch 3–6 tháng nếu D30 ≥8% |
| T4 | **Rừng Cổ Đại** (Won't cho giai đoạn này) | Có thể cần multi-process | Không ước lượng | Chỉ khi có doanh thu ổn định |

- **Kinh tế server:** chi phí phần cứng không phải rủi ro lớn nhất. Rủi ro lớn nhất là **vận hành**: anti-cheat, moderation chat, uptime khi chỉ có 1 người. Vì vậy: **không có chat tự do ở MVP** (chỉ emote + câu soạn sẵn kiểu tiên hiệp như "Đạo hữu xin dừng bước!"), server authoritative để giảm cheat, và một kill-switch tắt bậc T2 mà không ảnh hưởng T0/T1.
- **"Kỷ nguyên" có reset:** server lâu dài sẽ tích lũy power creep. Reset 14/28 ngày (giống "wipe" của Rust) kết hợp với meta giữ nguyên, giúp người mới luôn có điểm xuất phát công bằng.
- **Linh Ảnh (async PvP cho solo):** trong solo, một số sinh vật AI dùng **build thật của người chơi khác** (tên + nhánh tiến hóa + skin) được tải từ một API rẻ. Nhờ vậy solo vẫn có cảm giác "chuỗi thức ăn của người thật", với chi phí gần như bằng 0 (JSON tĩnh trên CDN).

### PX-10: Kiến trúc session 15–60 phút
- **Một session = "Một nhịp tu":** vào game (báo mộng 10s) → mục tiêu ngắn (2–3 "cơ duyên" hiện trên map) → vòng lặp chính → **điểm dừng tốt** là đột phá tiểu cảnh hoặc bế quan.
- **Số liệu mục tiêu:** cứ **8–12 phút** người chơi đạt 1 mốc tiến bộ cảm nhận được (tiểu cảnh, skill, vùng mới). Đại cảnh giới đầu cách nhau 1 session, sau đó giãn dần thành 2–4 session/cảnh giới ở mid-game, ~1 tuần/cảnh giới ở cuối game. Cả đời một kiếp đến phi thăng (người chơi giỏi, không chết): ~25–35 giờ, tức 3–5 tuần với 1 giờ/ngày. Nhiều kiếp hơn nếu chết.
- **Không dùng FOMO năng lượng/stamina.** Thay vào đó là **"Linh khí dồi dào"**: 30 phút chơi đầu mỗi ngày được ×1,5 tu vi. Nó thưởng cho việc quay lại chứ không phạt việc chơi lâu.

### PX-11: UI/UX đa nền tảng và điều khiển cảm ứng
- **Hai chế độ điều khiển, một HUD:**
  - **"Hành" (thú, côn trùng, hóa hình):** mobile dùng joystick ảo tay trái, 3 nút skill + 1 nút tuyệt kỹ (giữ để nhắm) tay phải. PC dùng WASD/chuột hoặc click-to-move. Tối đa **4 skill chủ động** trên HUD cho mọi loài.
  - **"Thần Thức" (thực vật, nấm, xuất khiếu):** không có joystick, chỉ **chạm–kéo trên map** (mọc rễ theo đường kéo, chạm để ra lệnh cộng sinh), kiểu RTS-lite. Pinch để zoom. Đây là lý do thực vật hợp với mobile.
- **Màn hình:** landscape bắt buộc trên mobile. UI an toàn cho notch. Nút ≥ 48dp. HUD che ≤18% màn hình.
- **Đọc được trong PvP:** silhouette loài + vòng màu cảnh giới dưới chân (xanh = thấp hơn bạn, vàng = ngang, đỏ = cao hơn). Mục đích là người chơi quyết định chạy hay đánh trong **≤1 giây**.
- **Accessibility:** chế độ màu cho mù màu (không mã hóa chỉ bằng đỏ/xanh). Phụ đề/biểu tượng cho mọi tín hiệu âm thanh (tiếng gầm kẻ săn mồi ⇒ icon hướng). Chế độ một tay cho Thần Thức. Cỡ chữ 3 mức. Giảm rung/chớp khi độ kiếp (sét!). Trong solo: độ khó theo trục **sinh tồn / chiến đấu / hình phạt chết** thay vì Easy/Hard.

### PX-12: Kinh tế (source/sink) và monetization có đạo đức

**Tiền tệ (đề xuất tối giản 4 loại):**
```
SOURCES                              KHO                        SINKS
ăn/săn/quang hợp/sự kiện  ──► [Linh Khí] (trong kiếp) ──► đột phá, skill, độ kiếp, hồi máu
chết/độ kiếp/phi thăng    ──► [Đạo Tâm] (meta, vĩnh viễn) ──► mở loài, nhánh huyết mạch, ưu thế đầu kiếp (có trần)
sự kiện/thành tựu/pass free ─► [Hoa Lộ] (cosmetic, kiếm được) ─► skin, hiệu ứng
nạp tiền                  ──► [Ngọc Tinh] (premium)     ──► skin, pass premium (KHÔNG mua được gì khác)
```
- **Trần chống lạm phát meta:** ưu thế đầu kiếp mua bằng Đạo Tâm **tối đa +25% tốc độ tu luyện cảnh giới 1–2**. Sink dài hạn là **mở rộng chiều ngang** (loài, nhánh, huyết mạch lai), không cộng chỉ số dọc vô hạn.
- **Hoa Lộ kiếm được ≈ 1 skin thường / 10 giờ chơi** để người không nạp vẫn sưu tầm được.

**Monetization (G3), quy tắc cứng PX đề xuất:**
1. **Skin không đổi silhouette, hitbox, màu vòng cảnh giới, độ tương phản với nền.** Không có skin ngụy trang. Trong game PvP săn mồi, skin "lá rụng" giúp tàng hình **chính là pay-to-win**. Ở chế độ PvP, có thể bật "hiển thị skin mặc định cho đối thủ".
2. **Rewarded ads chỉ dành cho tiện lợi, không cho sức mạnh ở thế giới PvP:**

| Vị trí ad | Solo/Co-op | Rừng chung (PvP) |
|---|---|---|
| Nhân đôi Đạo Tâm khi chết | ✅ (trần 3 lần/ngày) | ✅ nhưng chỉ +30%, trần 3 lần/ngày (meta, không ảnh hưởng trận đang đánh) |
| Hồi sinh tại chỗ | ✅ | ❌ (phá chuỗi thức ăn) |
| Tăng tốc bế quan (+2h offline) | ✅ | ✅ trần 1 lần/ngày |
| Nhân đôi Hoa Lộ | ✅ | ✅ |
| Buff chiến đấu | ❌ | ❌ |

3. **Không có interstitial ads khi đang chơi, không loot box trả tiền** (gacha skin thì thể hiện tỉ lệ + có pity, hoặc tốt nhất là không có). Không có "VIP level".
4. **Pass "Kỷ Nguyên"** khớp chu kỳ server 28 ngày: track free (Hoa Lộ, 2 skin) + premium (~4,99 USD: 6 skin, hiệu ứng độ kiếp, khung tên). Có **hoàn trả Ngọc Tinh** đủ mua pass kế tiếp nếu hoàn thành (mô hình Fortnite). Pass **không bao giờ** có Đạo Tâm.
5. **Sản phẩm cao cấp nhất = "Pháp Tướng Độ Kiếp"**: hiệu ứng tia sét/thiên tượng riêng khi độ kiếp, cả server nhìn thấy. Đây là khoảnh khắc khoe tự nhiên nhất của game và không ảnh hưởng combat.
- **Kỳ vọng doanh thu (thận trọng):** ARPDAU khoảng 0,01–0,03 USD (ad eCPM ở VN/SEA thấp hơn nhiều so với Tier-1). 10K DAU ≈ 100–300 USD/ngày, đủ trả server + công cụ AI, nhưng **chưa thành doanh nghiệp**. Muốn sống được thì cần thêm Steam (có thể bán "Gói Người Sáng Lập" cosmetic 9,99 USD) và thị trường Tier-1.

### PX-13: Tech stack và thứ tự nền tảng
- **Đề xuất: TypeScript toàn bộ.** Client dùng **Phaser 3/PixiJS** (2D, web nhẹ). Server dùng **Colyseus** (Node, cùng ngôn ngữ, chia sẻ logic sim giữa client và server, nên solo và online chạy **cùng một mô-đun sim**). Mobile bọc bằng **Capacitor**. PC/Steam bọc bằng **Electron/Tauri**.
- **Vì sao không Unity/Godot:** build web của Unity nặng (thường hàng chục MB, thời gian tải lâu, kém với web portal). Godot 4 web đã cải thiện nhưng vẫn kém ổn định trên Safari iOS. Quan trọng hơn: **AI coding assistant mạnh nhất ở TypeScript/web**, và 1 người cần chia sẻ code client/server. Điểm yếu: hiệu năng mobile thấp với hàng nghìn entity. Giải pháp là giới hạn ≤300 entity động trên màn hình, sim ecosystem chạy ở mức "ô lưới" (tile) chứ không theo từng cá thể.
- **Thứ tự ra mắt:** (1) **Web** trên CrazyGames/Poki + itch.io: audience sẵn, có SDK rewarded ads, playtest rẻ, đo D1 nhanh. (2) **Android**. (3) **Steam PC** (Early Access, cosmetic pack). (4) **iOS** (review khắt khe, chi phí cao nhất cho 1 người).
- **Art bằng AI:** top-down 2.5D stylized hợp với sprite sinh từ AI + chỉnh tay. Nhưng **animation là nút thắt**. Đề xuất skeletal 2D (Spine/DragonBones) hoặc "rig mảnh" đơn giản cho thú. Thực vật thì procedural (rễ, cành mọc bằng L-system/shader), vừa rẻ vừa đẹp. Đây là lợi thế sản xuất của việc **chơi cây**.

### PX-14: Phạm vi MoSCoW và chi phí (1 người + AI)
Đơn vị: S ≈ ≤1 tuần, M ≈ 2–3 tuần, L ≈ 4–6 tuần, XL ≈ 8+ tuần (đã tính AI hỗ trợ code/art).

| Tính năng | MoSCoW | Chi phí | Ghi chú |
|---|---|---|---|
| Core sim + di chuyển + ăn + combat cơ bản | Must | L | Nền móng |
| 3 loài: **Linh Thử** (ăn cỏ nhỏ), **Linh Mộc** (cây), **Huyết Lang** (ăn thịt) | Must | L | Chuỗi thức ăn tối thiểu đầy đủ |
| Cảnh giới 1–5 (tên riêng mỗi loài) + 2 nhánh tiến hóa/cảnh giới | Must | M | Tên nhiều, nhưng số liệu dùng chung |
| Độ kiếp (3 dạng) + luân hồi + Đạo Tâm | Must | M | USP, không được cắt |
| FTUE scripted | Must | M | |
| Rừng Non: 1 map, 3 vùng ngoài→trong | Must | L | |
| Solo + AI, lưu local/cloud | Must | M | |
| Bế quan + offline catch-up + báo mộng | Must | M | |
| 1 world event (Linh Khí Triều) | Must | S | |
| Rừng chung T2 (24–40 người) + Thiên Đạo/nghiệp lực | Should | L | Soft launch, có thể lùi 2 tháng |
| Co-op 2–4 người | Should | M | |
| Loài 4: **Nấm/Kiến cộng sinh** | Should | M | Gameplay "Thần Thức" thứ hai |
| Shop skin + rewarded ads + pass | Should | M | Phải có trước soft launch để đo |
| Linh Ảnh async | Could | S | Rẻ, hiệu quả |
| Xuất khiếu (linh hồn rời thân cây) | Could | M | Hay, nhưng thêm chế độ điều khiển thứ 3 |
| Hóa hình (cây → người/thú) | Could | L | Cần bộ animation mới, đắt |
| Phi thăng + Rừng Nguyên Sinh | Could (post-launch) | XL | |
| Bí cảnh (dungeon instanced) | Could | L | |
| Rừng Cổ Đại, chat tự do, guild/tông môn, iOS ngày đầu | Won't (giai đoạn này) | — | |

- **Vertical slice (tháng 3–4):** 1 vùng Rừng Non, Linh Thử + Linh Mộc + AI sói, cảnh giới 1–3, 1 độ kiếp, luân hồi, bế quan solo. **Câu hỏi duy nhất cần trả lời: "Luân hồi đổi loài có tạo ra cảm giác muốn chơi kiếp tiếp không?"**
- **MVP/soft launch Web (tháng 9–11):** toàn bộ Must + Should. Tổng ước lượng khoảng 40–48 tuần-người. Khớp với G4 nếu **giữ kỷ luật cắt Could**.
- **Tự kiểm tra điểm mù "cắt quá tay":** nếu cắt thêm, tôi **không cắt** thực vật, luân hồi, độ kiếp hay PvP chung. Bốn thứ đó chính là khác biệt. Thứ nên hy sinh trước là số loài (3 vẫn đủ chuỗi thức ăn) và hóa hình.

### PX-15: Retention và live-ops quanh sự kiện toàn rừng
| Mốc | Hook |
|---|---|
| D1 | Báo mộng + cây đã lớn khi offline. Đại cảnh giới 2 đạt được trong session 2 |
| D7 | Kỷ nguyên server đang ở nửa chặng, có world event lớn đầu tiên. Mở loài thứ 3 bằng Đạo Tâm. Pass tier ~10 |
| D30 | Chu kỳ phi thăng/kỷ nguyên kết thúc. Bảng "Thần Rừng" của kỷ nguyên. Pass mới |

- **Lịch sự kiện (1 người vận hành được, tất cả là sự kiện tự động theo lịch, không cần GM):**
  - **Hằng ngày:** Linh Khí Triều 2 lần/ngày (12h & 20h giờ server, 15 phút). Linh khí ×2 ở vùng trong, kéo người chơi vào vùng nguy hiểm, nên PvP tăng tự nhiên.
  - **Hằng tuần:** 1 sự kiện lớn xoay vòng: *Hạn Hán* (cây yếu, thú khát → tranh nguồn nước), *Bầy Châu Chấu Ma* (PvE chung, mọi giới phải hợp tác), *Thú Triều*, *Mưa Linh Vũ*.
  - **Kỷ nguyên (28 ngày):** sự kiện kết "Thiên Địa Đại Kiếp" 30 phút, rừng thay đổi vĩnh viễn trong kỷ nguyên sau (một vùng bị cháy thành tro, dễ mọc cây hơn) theo kết quả của người chơi.
- **Nguyên tắc:** mọi sự kiện phải **ảnh hưởng khác nhau lên từng giới** (hạn hán tốt cho nấm, xấu cho cây), để đổi loài qua luân hồi có lý do chiến lược.

### PX-16 (ngoài domain, gửi PROG/SURV): Thiên Đạo cân bằng loài
- **Vấn đề:** ở server PvP, 70% người sẽ chọn loài ăn thịt (bài học từ The Isle với carnivore), dẫn tới không còn mồi và cả server sụp.
- **Quy tắc:** bánh xe luân hồi hiển thị **"Thiên Đạo ưu ái"**: loài nào chiếm <15% dân số server thì nhận +25% tu vi và skin aura đặc biệt. Loài nào >35% thì luân hồi vào loài đó mất thêm 1 lượt chờ 60 giây. Hệ sinh thái tự cân bằng bằng **động cơ**, không cần cấm.

## 4. Kết nối với các domain khác
- **SURV:** cần (1) "Đạo Căn" của thực vật: giết được nhưng phải tốn ≥3 phút và chủ được báo. (2) Tự vệ thụ động hoạt động khi offline. (3) Needs cho mỗi loài ≤3 thanh, đọc được trên mobile. (4) Tuyệt đối không có need nào **trôi khi offline** đến mức gây chết.
- **PROG:** cần (1) đường cong combat power ~1,6–1,8×/cảnh giới trong PvP. (2) Lịch đột phá khớp PX-10 (8–12 phút/mốc đầu game). (3) Công thức chuyển tu vi→Đạo Tâm có trần. (4) Skill tree ≤4 skill chủ động cùng lúc. (5) Bảng số dùng chung giữa các loài để tiết kiệm sản xuất.
- **WORLD:** cần (1) Lore cho Bế Quan, Thiên Đạo, Nghiệp Lực, Phi Thăng, Linh Ảnh. (2) Tên cảnh giới mỗi loài, **ngắn ≤4 chữ** để vừa màn hình mobile. (3) Rừng Non có 3 vùng với tín hiệu thị giác rõ về mức nguy hiểm. (4) Mô tả cảm giác của 4 world event hằng tuần.
- **Mọi người:** mỗi đề xuất nên ghi chi phí S/M/L/XL và persona phục vụ.

## 5. Rủi ro tự nhận diện (Risk Register)
| Rủi ro | Khả năng | Tác động | Giảm thiểu | Phụ trách |
|---|---|---|---|---|
| Người mới bị grief, D1 sụp | Cao | Rất cao | PX-05, FTUE offline, Rừng Non có trần cảnh giới | PX/PROG |
| Gameplay thực vật nhàm (chờ đợi thụ động) | Cao | Cao | Vertical slice phải chứng minh cây có ≥1 quyết định/30 giây khi online | SURV/PX |
| Scope creep (hóa hình, xuất khiếu, 10 loài, Cổ Đại) | Rất cao | Rất cao | MoSCoW cứng. Mỗi tính năng Could cần D7 ≥15% mới mở | PX |
| Dân số server thấp → rừng vắng | Cao | Cao | Phòng nhỏ 24–40, bot AI lấp chỗ, Linh Ảnh, ghép phòng theo khu vực | PX |
| Lệch cân bằng loài (ai cũng chọn sói) | Cao | Cao | PX-16 | PROG |
| Doanh thu ads không đủ | Trung bình | Cao | Steam cosmetic pack, pass, chi phí server tối thiểu | PX |
| Cheat (speedhack, teleport) trên web | Trung bình | Cao | Server authoritative cho T2, không tin client | PX |
| Kiệt sức solo dev / vận hành 24/7 | Cao | Rất cao | Sự kiện tự động theo lịch, không chat tự do, kill-switch T2, ra mắt từng nền tảng | PX |
| Hiệu năng web/mobile thấp | Trung bình | Trung bình | ≤300 entity động, ecosystem sim theo tile | PX |
| Nội dung AI-art kém nhất quán | Trung bình | Trung bình | Style guide khóa sớm. Thực vật procedural | WORLD |

## 6. Giả thuyết playtest và KPI
| ID | Giả thuyết | Đo | Ngưỡng đạt |
|---|---|---|---|
| H1 | Nhịp tiến bộ kiểu .io khiến người chơi đạt đột phá 1 | % đạt phút 5 | ≥80% |
| H2 | Luân hồi lần đầu tạo cảm giác "muốn thêm 1 kiếp" | % bắt đầu kiếp 2 trong 60s sau khi chết | ≥70% |
| H3 | Thực vật đủ vui cho P3 | % người thử cây chơi ≥10 phút ở kiếp cây | ≥50% |
| H4 | Bế quan giảm nỗi sợ PvP | Khảo sát "tôi lo mất tiến độ khi offline" (1–5) | trung bình ≤2,5 |
| H5 | Nghiệp lực giảm grief | % kill ở chênh lệch ≥2 cảnh giới | ≤10% tổng kill PvP |
| H6 | Báo mộng kéo người chơi quay lại | D1 có/không có báo mộng (A/B) | +5 điểm % |
| H7 | Cân bằng loài tự nhiên | Không loài nào >40% dân số server suốt 7 ngày | đạt |

**KPI soft launch Web (mục tiêu go/no-go cho Android/Steam):** D1 ≥30%, D7 ≥10%, D30 ≥4%, session trung bình ≥14 phút, ≥2 session/DAU/ngày, tỉ lệ xem rewarded ad ≥35% DAU, crash <1%.
**Telemetry bắt buộc:** time-to-first-breakthrough, time-to-first-death, nguyên nhân chết (AI/PvP, chênh cảnh giới), tỉ lệ chọn loài khi luân hồi, phút bỏ game trong FTUE, thời lượng offline và lãnh thổ mất.

## 7. Câu hỏi mở
1. Người dùng có chấp nhận **reset bản đồ theo kỷ nguyên 14/28 ngày** ở server chung không? Tôi cho rằng đây là cách duy nhất giữ PvP công bằng lâu dài.
2. **Kiếp đầu bị khóa là thú nhỏ** (không phải cây) có trái với hình dung của người dùng không? Tôi đề xuất vậy vì 5 phút đầu phải vui. Cây đến ở phút 15.
3. Thị trường đầu tiên là **VN/SEA (tiếng Việt)** hay **toàn cầu (tiếng Anh)**? Chọn thế nào thì ad eCPM, tên cảnh giới và tone lore đều thay đổi theo.
4. Có chấp nhận **không có chat tự do** ở MVP (chỉ emote/câu soạn sẵn) để giảm gánh moderation không?
5. Mức "khắc nghiệt vừa" đã đủ chưa? Liệu trần mất 25% lãnh thổ khi offline có quá mềm với P2 (fan PvP), làm mất chuỗi thức ăn "thật"? Cần SURV góp ý.
