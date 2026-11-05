# The Forest of Life — Game Design Document v1.0

> Session: `Game document design/debates/2026-11-05-forest-of-life-gdd/` · Chế độ: standard (R1→R6) · Ngày: 2026-11-05
> Tác giả: team 4 Senior Game Designer, gồm **SURV** (sinh tồn), **PROG** (tiến trình & số liệu), **WORLD** (thế giới & câu chuyện), **PX** (trải nghiệm, kinh tế, phạm vi). Orchestrator tổng hợp.
> Nguồn: mỗi mục ghi ID ý tưởng gốc (vd `SURV-03b`). Chỗ đánh dấu **[orch]** là chỗ orchestrator phải tự hài hòa hai bản không khớp nhau. Các chỗ này đã được team duyệt lại ở R6.
> Nhãn phạm vi: **[MVP]** soft launch Web (tháng 0–12) · **[U1]** Update 1 (tháng 13–15) · **[1.0]** (tháng 16–21) · **[Post]** sau 1.0 · **[Cắt]**.
> Đơn vị: **CT (Chu Thiên)** = tu vi của 1 phút chơi tích cực. Người chơi **Mid** chơi 5 phiên × 40'/tuần ≈ 64 CT/phiên ≈ 320 CT/tuần. **Casual** ≈ 130 CT/tuần. **Core** ≈ 2× Mid.

---

## 0. TL;DR

1. **Game là gì:** game sinh tồn tu tiên PvP 2D/2.5D top-down trên Web/Mobile/PC. Mỗi người chơi là một **Mộng Hỏa** (tia mộng của cây thần Kiến Mộc đã ngã) nhập vào một sinh linh trong rừng: cổ thụ, chuột hay sói. Mỗi loài tu luyện theo cách riêng (quang hợp, ăn hạt, săn mồi) qua **7 cảnh giới** có tên riêng theo loài, rẽ nhánh **Huyết Mạch** và **độ kiếp** để đột phá.
2. **Vòng đặc trưng:** chết thì có hai đường. **Hậu Duệ** là đầu thai cùng loài tại một "neo" và mất khoảng một buổi chơi. **Luân Hồi** là đổi sang loài khác, mang theo **Đạo Quả** (tiền meta) và **Túc Tuệ**. Xác của bạn trả linh khí về cho rừng.
3. **PvP luôn bật** ở Rừng chung. Kẻ mạnh không bị cấm ăn kẻ yếu, nhưng **Thiên Đạo Luật** lấy đi phần lời: giết người kém mình ≥2 cảnh không cho tu vi, còn sinh **Sát Nghiệp** khiến kẻ đó thành mục tiêu săn của cả rừng.
4. **Cây chơi được thật:** HP 3 lớp, một sói cùng cấp cần ≥40s mới làm cây Đổ. Cây có lan rễ, Vệt Nắng, gai/độc, cộng sinh kiến, Linh Thức (phóng hồn đi do thám), và được nếm trước Hóa Hình. Khi offline cây bất tử.
5. **Phạm vi:** studio 1 người + AI. MVP gồm 3 loài, C1–C4, 1 map 256² có 3 vòng và PvP người thật. Tổng 45,75 tuần-người + ~4,25 tuần đệm, ra mắt Web trên CrazyGames/itch.io. F2P: skin, rewarded ads, Pass. **Không bán sức mạnh.**

---

## 1. Tầm nhìn, hook, đối tượng — owner: PX · WORLD

### 1.1 Theme & hook *(WORLD-01b, PX-02b)*
- **Theme:** *"Mọi sự sống đều được nuôi bằng một sự sống khác. Kẻ mạnh nhất không phải kẻ ăn nhiều nhất, mà là kẻ nuôi được cả khu rừng."*
- **USP:** *Game sinh tồn tu tiên PvP đầu tiên cho bạn làm bất kỳ sinh mệnh nào trong rừng (chuột, sói, cổ thụ). Mỗi lần chết là một lần luân hồi, và xác bạn nuôi chính khu rừng.*
- **Hook trailer:** *"Kiếp này em là con chuột mang hạt. Kiếp sau em là cổ thụ mọc từ xác chính mình."*
- **Tagline:** *"Sống. Bị ăn. Mọc lại thành rừng."* (EN: *Live. Be eaten. Grow back as the forest.*)

### 1.2 Năm trụ cột *(WORLD-01b)*
| # | Pillar | Người chơi phải cảm thấy | Cơ chế chứng minh | Kiểm chứng |
|---|---|---|---|---|
| P1 | **Ăn và bị ăn** | Mọi sinh linh khác là con mồi hoặc mối đe dọa | PvP tự do, Tốc không tăng theo cảnh, Thiên Đạo Luật | ≥70% kể được "một lần suýt chết" sau phiên 2 |
| P2 | **Chậm mà vĩ đại** | Kiên nhẫn được đền đáp và nhìn thấy được | Lãnh thổ rễ lưu lại, Mộng Báo | ≥50% người thử cây chơi ≥10' |
| P3 | **Cái chết là hạt giống** | Chết đau nhưng có nghĩa | Trung Ấm, Đạo Quả, FTUE chuột → cây | ≥60% quay lại trong 72h sau khi chết PvP ở C≥3 |
| P4 | **Rừng nhớ** | Hành động để lại dấu vết | Mộ Linh, Biên Niên, Khô Linh, Thần Bia | ≥30% chạm Mộ Linh trong tuần 1 |
| P5 | **Trời đất chứng giám** | Độ kiếp và sự kiện là khoảnh khắc chung | Công Kiếp, Đại Linh Triều, Đại Kiếp | ≥40% độ kiếp chọn Công Kiếp |

> **Luật hóa theme:** **Linh Quỹ/Khô Linh** (MVP) và **Công Đức** (U1+) là hai cơ chế duy nhất biến theme thành luật chơi. Không cắt cả hai cùng lúc.

### 1.3 Persona *(PX-01b)*
| Persona | Nền tảng | Session | Động lực | Cần | Sợ |
|---|---|---|---|---|---|
| **P1 "Đạo hữu xe buýt"**, 18–30t, đọc tiên hiệp | Mobile web → Android | 10–20', 2–3 lần/ngày | Completion, Power, Fantasy | Đột phá đều, thấy thứ gì đó lớn lên khi offline | Mất công sức vì bị gank |
| **P2 "Kẻ săn mồi"**, 16–28t, fan The Isle / mope.io | PC web → Steam | 45–90' | Competition, Excitement | Săn người thật, adrenaline | Lớn chậm, không được làm sói |
| **P3 "Người làm vườn"**, 20–40t, cozy/strategy | PC/Mobile | 20–40' | Design, Strategy, Discovery | Lan rễ, cộng sinh, thấy rừng đổi vì mình | Thao tác twitch |

**Quy tắc:** tính năng nào không phục vụ ≥1 persona ở mức "mạnh" thì xuống Could.

### 1.4 Đối thủ & khoảng trống *(PX-02b)*
| Đối thủ | Học được | Khán giả phàn nàn | Bài học |
|---|---|---|---|
| The Isle / Path of Titans | Nỗi sợ thật, PvP chuỗi thức ăn | Lớn 4–6h, người mới bị ăn ngay, map vắng | Lớn nhanh, chết có thưởng, mật độ sự kiện cao |
| mope.io / evowars | Vào game 5 giây, tiến hóa mỗi 1–2' | Không có meta, thể loại bão hòa | Chỉ mượn nhịp đầu game |
| Game tu tiên idle/MMO | Cảm giác đột phá, tên cảnh giới | P2W, VIP, dark pattern | Giữ đột phá, bỏ P2W |
| Tale of Immortal | Tiên hiệp bán được trên Steam | Grind, UI rối | UI phải gọn |
| Game làm cây (Grow The Seed, Tree Simulator) | Có cầu cho fantasy "làm cây" | Single-player hoặc meme | **Khoảng trống:** chưa thấy game nào cho chơi cây trong PvP nhiều người, có luân hồi giữa các loài (search 11/2026) |

---

## 2. Thế giới & lore — owner: WORLD

### 2.1 Bốn sự thật *(WORLD-02b)*
| Sự thật | Nội dung | Người chơi **làm** gì với nó |
|---|---|---|
| **S1. Kiến Mộc đã ngã** | Cây nối trời đất bị chặt ở Đại Kiếp trước. Rễ của nó vẫn sống dưới đất, gọi là **Linh Mạch** | Linh Mạch là các đường sáng mờ trên map. Cây cắm Tâm Rễ trúng mạch được thêm tài nguyên |
| **S2. Linh khí chỉ chuyển chủ** | Linh khí không tự sinh mà đi vòng: nắng → cây → thú ăn cỏ → thú săn → xác → đất → Linh Mạch | Nền của **Linh Quỹ/Khô Linh** và sổ **Sinh Năng** |
| **S3. Ý thức là mộng của Kiến Mộc** | Mộng của Kiến Mộc vỡ thành vô số **Mộng Hỏa**. Người chơi là một Mộng Hỏa. Phần mộng còn lại chính là **Ý Chí Rừng** (Director). Dư ảnh của các Mộng Hỏa khác là **Linh Ảnh** (bot) | Giải thích luân hồi, vì sao các loài nói chuyện được với nhau, vì sao solo vẫn có "người" |
| **S4. Thần Vị là rễ cái của Kiến Mộc mới** [Post] | 5 Thần Vị Ngũ Hành. Thần nuôi vực của mình, Quy Căn thì thần lực đổ vào chồi Kiến Mộc, rồi Đại Kiếp xảy ra | Endgame. Reset được kể như một sự kiện câu chuyện |

**Ba bí mật theo hồi:** (1) **Hạ Lâm**: Rừng Non mọc từ một hạt gió thổi ra từ Thần Lâm, Mảnh Mộng 3 cho thấy bóng người cầm rìu. (2) **Linh Lâm** [Post]: Nhân Tu chính là yêu thú và cây đã hóa Nhân Hình rồi quên gốc ("kẻ ăn nhiều nhất trở thành kẻ chặt cây"). (3) **Thần Lâm** [Post]: thần cũ tự hiến thân làm rễ.
**Chi phí authored:** MVP ~4.000 từ, toàn game ~12.000 từ. Không có cutscene.

### 2.2 Ba cấp rừng = ba giới *(WORLD-04c, PROG-01c, C1)*
| Cấp | Tên lore (tên brief) | Map | Người/phòng | Cảnh giới | Áp Chế (trần tầng n) | Câu hỏi | Nhãn |
|---|---|---|---|---|---|---|---|
| 1 | **Hạ Lâm** (Rừng Non) | 256², 3 vòng + Linh Nhãn | Solo/co-op 1–4; Rừng chung 24–40 CCU | C1–C3. Thâm Lâm (vòng trong) là cửa vào Linh Lâm cho C4 | n=9 (C3 Hậu) ở Bìa và Trung Lâm. **Không** áp ở Thâm Lâm | "Vì sao tôi tỉnh dậy biết nghĩ?" | **MVP** |
| 2 | **Linh Lâm** (Rừng Nguyên Sinh) | 384², 4 vòng | 30–80 | C4–C5 | n=15 (C5 Hậu) | "Vì sao linh khí cạn dần?" | [1.0] |
| 3 | **Thần Lâm** (Rừng Cổ Đại) | 512², 5 Thần Vực quanh gốc Kiến Mộc | 80–200 | C6–C7 | Không trần | "Kiến Mộc có nên mọc lại?" | [Post] |

- **Cấu trúc lồng nhau:** vòng trong của mỗi cấp là rìa ngoài của cấp kế tiếp. Nhờ vậy MVP có một lần "phi thăng" thật mà chỉ cần 1 map. **[orch]** Vòng lõi MVP lấy tên **Thâm Lâm** (theo WORLD). PROG và PX từng gọi vòng này là "Linh Lâm", nhưng tên đó đã dùng cho cấp rừng 2.
- **Phi Thăng:** ở MVP là **Phá Giới**: qua Phi Thăng Kiếp I thì Giới Bia phát sáng, sương rẽ ra, Áp Chế được gỡ. Từ [1.0] là chuyển map: cây kết Phi Thăng Tử bay theo gió (đồng thời là màn loading), thú theo Đại Di Cư, cây rời đi để lại **Phi Thăng Mộc Mộ**.
- **Phân Thân:** người ở cấp cao quay về cấp thấp bị tự động Áp Chế, UI ghi "Phân Thân · C3 Hậu". Sát Nghiệp vẫn tính theo cảnh giới thật.
- Layout vòng, Linh Nhãn và Linh Mạch là **authored**. Biome trong vòng sinh procedural theo seed của mỗi Kỷ Nguyên.

### 2.3 Vòng ngoài → trong (MVP) *(WORLD-05b, SURV-08b)*
| Vòng | Biome MVP | Bonus CT (cộng vào Gia Trì) | Mật độ linh khí · hấp thu khi tĩnh tọa | Linh Quỹ | Nguy hiểm | Màu |
|---|---|---|---|---|---|---|
| **Bìa Rừng** | Đồng Cỏ Ven Rừng | +0 | L0 · +3/phút | Sàn 50%, không Khô Linh | Thấp. Nơi Ấu Linh spawn | #C9D97A |
| **Trung Lâm** | Rừng Lá Rộng | +0,15 | L1–L2 · +6/phút | Bình thường | Trung bình | #6FA35A |
| **Thâm Lâm** | Đầm Mục | +0,3 | L2–L3 · +12/phút | Hồi chậm | Cao. C4 không bị nén | #2F6B5E |
| **Linh Nhãn** (nút ở tâm) | — | +0,5 | L4 · +25/phút (khi Linh Triều) | Giàu, tải cao | Rất cao. Nơi tranh đoạt | #7B6FD6 |

**[orch]** Ba biome MVP được làm như **3 bộ palette và props trên một tileset** để khớp ngân sách "1 biome + biến thể" của PX. **Wayfinding:** Cột Linh Quang ở Linh Nhãn (ra khỏi màn hình thì hiện vệt ở mép), hạt linh khí trôi về tâm, Giới Bia đánh dấu ranh vòng ("Thâm Lâm · Cảnh đề nghị 4"), color grading theo vòng, chế độ accessibility thêm icon. **Không có minimap.**

### 2.4 Biome & bí cảnh *(WORLD-06c, 07c)*
| Biome | Nhãn | Bí mật → hành động |
|---|---|---|
| Đồng Cỏ Ven Rừng | MVP | Sau mưa mọc vòng nấm tiên. Đứng trong vòng lúc bình minh thì mở **Mộng Ấn 1** ("Ngươi là Mộng Hỏa") |
| Rừng Lá Rộng | MVP | Dưới rễ **Lão Tùng** có Thần Bia cũ: mở **Mộng Ấn 2** ("Kiến Mộc đã ngã") và lời chỉ điểm đi tìm Mộng Ấn 3 |
| Đầm Mục | MVP | **Liễu Chết** vào đêm trăng tròn mở **Mộng Ấn 3** (bóng người cầm rìu). Xác phân giải nhanh hơn |
| Rừng Tro | 1.0 | Sinh sau Đại Hỏa, dinh dưỡng ×3. Hoa Phượng Hỏa (Cơ Duyên) |
| Trúc Lâm Gió · Vách Đá Rêu · Hang Rễ | Post | — |

| Bí cảnh | Nhãn | Dạng | Thưởng |
|---|---|---|---|
| **Mộng Ấn ×3** | MVP | Vignette tĩnh toàn màn hình (1 ảnh + ~150 từ), **không phải instance** | Đạo Quả nhỏ, 1 Duyên, 1 Cơ Duyên |
| **Linh Mạch Huyệt** | MVP | Vùng mở trong đỉnh 30' của Linh Triều: 1 ở Trung Lâm (chỉ C≤3), 1 ở Linh Nhãn | Linh khí ×2 (CT vẫn đi qua trần Gia Trì) |
| Mộng Cảnh Cổ Thụ · Lôi Trì | 1.0 | Instance 10–20' / luyện kiếp không mất gì | Mảnh Mộng / giảm độ khó kiếp kế tiếp |
| Trùng Sào · Trại Nhân Tu Bỏ Hoang | Post | Dungeon co-op / chỉ Nhân Hình vào được | — |

### 2.5 Lịch thời gian *(WORLD-19, C3 nhất trí 4/4)*
| Đơn vị | Độ dài thực | Ghi chú |
|---|---|---|
| **Ngày-rừng** | **20'** (ngày 12' · hoàng hôn 2' · đêm 6') | Phiên 15' thấy được ≥1 đêm hoặc 1 bình minh |
| **Mùa** | **42h** (Xuân Sinh · Hạ Trưởng · Thu Thu · Đông Tàng) | Giờ bắt đầu mùa trôi 18h sau mỗi mùa, nên mọi múi giờ đều có lượt |
| **Năm-rừng** | **7 ngày thực** | Mỗi tuần có 1 Đại Linh Triều. Huyết Nguyệt từ [U1] |
| **Kỷ Nguyên** | **28 ngày** (4 năm) | 1 Pass. Từ [1.0]: map Hạ Lâm sinh seed mới, **nhân vật được giữ** |
| **Đại Kiếp** | **56 ngày** (8 năm). **MVP: 28 ngày** | Reset nhân vật: mọi người luân hồi và nhận Đạo Quả |

**Timeline bản đầy đủ (56 ngày):** ngày 1 mọi người vào Hạ Lâm → ngày ~20 Core trung vị chạm Thiên Kiếp → **ngày 22 Thần Vị Khai** → ngày 28 Kỷ Chuyển (phòng Hạ Lâm mới, giữ nhân vật) → ngày 36–42 thần nhiệm kỳ đầu Quy Căn → **ngày 56 Đại Kiếp**. **Rừng Non xoay vòng** *(PROG-16)*: cứ 14 ngày mở một phòng Hạ Lâm mới, mỗi phòng sống 28 ngày, nên người vào muộn luôn có phòng ≤14 ngày tuổi.

### 2.6 Rừng biến đổi *(WORLD-08c, SURV-15c)*
- **Mộ Linh [MVP]:** nơi sinh linh C4+ ngã xuống mọc một Hoa Mộ Linh trong 1 năm-rừng. Chạm vào đọc được 1 dòng, vd *"Nơi đây Lang 'Tro Tàn' (C4) ngã dưới nanh Lang 'Thanh Ảnh', Đông năm 3."*
- **Khô Linh hiển thị [MVP]:** vùng nhạt màu, lá rơi, thú AI bỏ đi (xem §5.7).
- [1.0]: diễn thế 3 giai đoạn Trống → Cỏ → Rừng, cộng Tro (chunk 8×8) · **Mộc Mộ** cho cây C5+ · **Hạt Quên** (Ổ Hạt của Linh Thử không bị ăn trong 1 năm-rừng thì mọc thành cây non AI).
- [Post]: Thần Vực trôi theo Tâm Hướng của thần.

### 2.7 Thế lực: Ngũ Tộc + kẻ ngoài rừng *(WORLD-09c)*
| Thế lực | Vai trò hệ thống | Lão NPC (bất động) | Nhãn |
|---|---|---|---|
| **Mộc Tộc** | Lãnh thổ, hạ tầng, ký ức | **Lão Tùng**: dạy đạo, chỉ Mộng Ấn, chào khác nhau theo Tâm Hướng | Linh Mộc: MVP |
| **Thú Tộc** | Săn, di chuyển, lãnh địa | Bạch Lộc Tàn Hồn [1.0] | Lang, Linh Thử: MVP |
| **Trùng Tộc** | Bầy đàn, cộng sinh | Trùng Hậu Hóa Thạch [1.0] | Kiến cộng sinh + côn trùng AI: MVP |
| **Khuẩn Tộc** | Phân giải, **giữ luân hồi** | **Bà Khuẩn**: đón Mộng Hỏa trong Trung Ấm (text + 1 ảnh) | Bà Khuẩn: MVP · Khuẩn chơi được: 1.0 |
| **Vũ Tộc** | Sứ giả | **Quạ Già**: đậu trên Giới Bia, báo trước sự kiện | NPC: MVP · chơi được: [Cắt] |
| **Nhân Tu** | Mối đe dọa từ ngoài, tấm gương | Không có NPC biết nói, chỉ có dấu vết | Dấu vết tĩnh ở Thâm Lâm: MVP · E5: Post |

**Không làm hệ danh tiếng phe.** Thế giới phản ứng qua Linh Quỹ, Mộ Linh, Thần Bia và lời Lão NPC.

---

## 3. Core Loops — owner: SURV *(SURV-06b, PX-10b)*

| Tầng | Thời gian | Vòng lặp | Căng → Thả |
|---|---|---|---|
| **Moment** | giây | Thú: tìm → ăn/né → chạy. Cây: bắt Vệt Nắng → kéo rễ → bật gai | Kẻ săn xuất hiện → thoát vào bụi/hang |
| **Activity** | 3–10' | Thú: săn mồi, trữ hạt, tranh Linh Mạch. Cây: lan rễ tới ô ẩm, nuôi kiến, treo Quả Ước, Linh Thức do thám | Đi xa Hang/Tâm Rễ → về lãnh thổ |
| **Session** | 15–60' | **Mộng Báo** (≤10s) → 2–3 Cơ Duyên trên map → vòng chính → **điểm dừng tốt** là đột phá tầng, hoặc **Đả Tọa** tại Hang/Tâm Rễ (luyện linh khí đã tích, trần 15% CT phiên) rồi **Bế Quan** | Đêm, sự kiện → Đả Tọa, autosave |
| **Campaign** | tuần | Tầng → Tiểu Kiếp → **Phi Thăng Kiếp I** (sang Thâm Lâm/Linh Lâm) → Trung Kiếp → Phi Thăng Kiếp II → Thiên Kiếp. Luân hồi đổi loài. Đại Linh Triều hằng tuần. Đại Kiếp cuối chu kỳ | Đại Kiếp: nghi lễ, Biên Niên, Thần Bia |

**Tension graph (Ý Chí Rừng):** mỗi 20' có ít nhất 1 đỉnh áp lực >60 và 1 đáy <25 (§5.8).

---

## 4. Loài & cách chơi — owner: SURV (cơ chế) · PROG (số) · WORLD (tên)

### 4.1 Lộ trình loài
| Loài | Giới | Vai trò chuỗi thức ăn | Nhãn |
|---|---|---|---|
| **Linh Mộc** (cây) | Mộc | Sản xuất, lãnh thổ, phòng thủ, neo | **MVP** |
| **Linh Thử** (chuột) | Thú | Con mồi, ăn hạt/quả, mang hạt | **MVP** |
| **Lang** (sói) | Thú | Kẻ săn | **MVP** |
| Khuẩn (nấm) | Khuẩn | Phân giải, mạng ngầm | 1.0 |
| Linh Thảo (cỏ/thảo dược) | Mộc | Lan nhanh, Phản Sinh | 1.0 |
| Lộc (hươu) | Thú | Ăn lá (ở MVP chỉ là AI) | Post |
| Phong (ong) / Trùng | Trùng | Bầy đàn | Post |

### 4.2 Nguồn tu vi theo loài (chuẩn hóa 1,0 CT/phút ±10%) *(PROG-03b)*
| Loài | Nguồn chính | Nguồn phụ | Đặc thù | Phương sai |
|---|---|---|---|---|
| **Linh Mộc** | Quang hợp nền 45%, tỉ lệ với Quang Tinh **thu được** | **Vệt Nắng** 20% · cắm rễ/hấp thu 20% (Linh Mạch, phần "đất" của xác) | Phản vệ thành công 2 CT (1 lần/kẻ tấn công/30'), Quả Ước bị ăn, cộng sinh 15% | Thấp (~16%) |
| **Linh Thử** | Ăn hạt/quả 45% | Trữ/gieo hạt 25% | **Thoát Sinh** 2 CT, đào hang, Linh Tuyền 30% | Trung bình (~22%) |
| **Lang** | Săn 60% (Sinh Năng 8 CT/con mồi cùng cảnh) | Ăn xác, đánh dấu lãnh thổ 25% | PvP theo Thiên Đạo Luật 15% | Cao (~34%) |
| Khuẩn [1.0] | Phân giải xác 50% | Lan tơ 25% | Khế ước cộng sinh 25% | Cao |

**Hệ số áp lên CT** (nhân thẳng, nằm ngoài Gia Trì): vùng thấp hơn cảnh của mình ×0,5^chênh · needs Comfort ×1 / Warning ×0,85 / Critical ×0,5 / Lethal ×0 · Khô Linh: thú ×0,5, cây ×0,8 · mùa Đông với cây: rễ ×1,6 bù quang hợp ×0,4 · AFK (không có quyết định trong 5') ×0,2 · **offline 0**.

### 4.3 Linh Mộc: chơi cây *(SURV-03b, 07b, PROG-11b, WORLD-14c, C6-B′)*
**HP 3 lớp:**
| Lớp | C1 | Ai phá được |
|---|---|---|
| **Tán** (~20% ngân sách) | 60 | Thú ăn lá, sâu, Linh Thử gặm chồi. Chịu đòn trước |
| **Thân** (~50%) | 200 (PROG: 3 × HP tham chiếu, vì Tốc = 0 được quy đổi thành ×3) | Mọi đòn (×0,5 khi Tán còn), sét |
| **Tâm Rễ** (~30%) | 100 | **Chỉ Căn Thương**: Độn Thử đào 1%/s · lửa 2%/s · rễ đối thủ 0,5%/s · hạn (Thủy = 0) · sét kiếp. Khi cây đang Mộc Tàn thì ×2 |

- **Thân = 0 → Đổ** (chưa chết): mất Tán và 25% CT tầng hiện tại, vào **Mộc Tàn** 120s (không quang hợp, Căn Thương ×2), mọc lại nếu Quang Tinh ≥30. **Tâm Rễ = 0 mới là chết.**
- **TTK đã kiểm chứng (sim O, C4 Sơ):**

| Tình huống | Thời gian |
|---|---|
| 1 Lang cùng tầng vs cây phòng thủ | **43–54s**. Nếu sói rút ở HP <35% thì không bao giờ làm cây Đổ |
| Cây AFK | 35s |
| 1 Lang cao hơn 1 cảnh | 36s |
| 3 Lang | 17s |
| 3 Lang + Độn Thử | Đổ ở 17s, chết thêm 50s sau đó |

  Muốn tận diệt cây cần **phối hợp nhiều loài**.

**Động từ của cây (mở theo bậc):**
| Động từ | Mở | Số liệu C1 | Đánh đổi | Nhãn |
|---|---|---|---|---|
| **Bắt Vệt Nắng** (chạm) | Phút đầu | Trung bình 1 vệt/50s, ×2,5 Quang Tinh trong 8s, **báo trước 2s** bằng ánh sáng trên tán. AFK mất ≈19%. Tỉ lệ lỡ trên mobile phải ≤30% | Bỏ qua không chết | MVP |
| **Vươn rễ** (kéo) | Phút đầu | 1 ô/20s, 8 Quang Tinh/ô, tối đa 12 ô. ×1,6 mỗi cảnh: 12 → 19 → 31 → 49 → 79 → 126 → 201. Ô rễ = lãnh thổ, nước, cảm ứng rung | Rễ dài thì nhiều điểm bị cắt | MVP |
| **Gai Bạo** (slot phòng thủ 1) | Phút đầu | Phản 15% sát thương mỗi cắn trong 10s, CD 20s, 10 Quang Tinh | Tiêu cho phòng thủ thì ít để lớn | MVP |
| **Độc Tiết** (slot phòng thủ 2) | C1 Trung | Sau 5 cắn: chậm 30%, −2 HP/s trong 6s, CD 45s, 20 Quang Tinh | như trên | MVP |
| **Gieo hạt / Mầm-Neo** | C1 Hậu | Tầm 6 ô (gió mạnh 20), 25 Quang Tinh + 5 Dưỡng Chất, tối đa 3 Mầm Con, **1 Mầm làm Neo** (30 HP, được bảo vệ nếu nằm trong mạng rễ) | Neo ngoài mạng rễ dễ bị phá | MVP |
| **Quả Ước** | C2 | 15 Quang Tinh/quả. Thú ăn: +15 No, +3 linh khí. Cây nhận hạt phát tán + phân bón | Quả nuôi luôn cả kẻ thù | MVP |
| **Cộng sinh: Kiến lite** | C2 | Tới sau 8s, −3 HP/s lên kẻ đứng trong ô rễ, duy trì −1 Quang Tinh/phút/tổ, tối đa 2 tổ. Làm dạng **swarm VFX + decal theo ô, không rig** | Bỏ đói thì kiến rời đi | **MVP** ⚠️ |
| **Linh Thức lite** (xuất khiếu) | C2 | Mộng Hỏa rời thân **60s**, đi tối đa **30 ô** (sợi mệnh), do thám, ping cho party, đánh dấu. Không tấn công. **CD 3'** **[orch: CD theo PROG]**. Thân chỉ còn phòng thủ thụ động khi hồn ở ngoài | Mỗi lần dùng mất 1 Vệt Nắng | **MVP** |
| **Hóa Hình Mộng** (nếm trước Hóa Hình) | C4, trong đỉnh 30' của Đại Linh Triều | Dạng Bản Thể tạm thời: sprite ×1,3, gai +1 tầm | Teaser cho U1 | **MVP** ⚠️ |
| Đắng Hóa, Trói Rễ (Căn Tỏa), Nắp Ấm | Huyết Mạch C3 | Trong ngân sách 18 skill | — | MVP |
| Kế Hoạch Sinh Trưởng | Trước khi thoát | **MVP chỉ có "Tán mọc lại"** (câu FTUE: *"Tán sẽ tự lành khi ngươi rời đi"*). Bản đầy đủ (≤3 ô rễ, quả chín) ở U1 | — | MVP lite |
| Mộc Độn (chỉ trong mạng rễ, khóa 10s sau sát thương, CD 3', 15 Quang Tinh) · Trận Pháp · Ký Hồn Mộc · Cộng sinh Ong/Nấm · Cầu Viện Hương | — | — | — | 1.0 / U1 |
| **Bản Thể C5** (U1) · **Di Căn** (cây nhổ Tâm Rễ đi chậm ≤3', lúc đi Tâm Rễ bị lộ) | — | — | — | U1 |
| Nhân Hình (sợi mệnh 30 ô) · Xuất Khiếu thật (C6) · Mị Hương · Ký Sinh Đoạt Xá · Truyền Mộng | — | — | — | Post |

> **Bốn cách chơi thực vật của brief đều có trong MVP:** rễ/hạt ✓ · cộng sinh (Kiến lite) ✓ · xuất khiếu (Linh Thức lite) ✓ · hóa hình (Hóa Hình Mộng, bản đầy đủ ở U1) ✓.

**Plant Pressure Map (MVP):**
| Áp lực | Tần suất | Đối phó |
|---|---|---|
| Hươu AI ăn lá (−2 lá/cắn) | 1 đợt/4–7', Director điều chỉnh | Gai, Độc, kiến, hoặc treo Quả Ước để hươu ăn quả thay lá |
| Linh Thử gặm chồi/Mầm | Tùy | Đặt Mầm trong mạng rễ. Hoặc biến chuột thành đồng minh (ăn sâu, mang hạt) |
| Bầy sâu (đẻ khi Tán >70% và không có kiến) | Theo luật | Kiến, Độc, Linh Thử ăn sâu |
| Cây đối thủ | Liên tục | Che bóng −30%. Tranh ô rễ: bên đầu tư Quang Tinh/ô cao hơn thắng sau 30s |
| Hạn và sét | Mùa Hạ, giông | Rễ tới suối, thu Tán trong giông |

**Session mẫu cây 30' (C2):** Mộng Báo ("Tán đã lành, Mộng Tích 100%") → bắt Vệt Nắng và kéo rễ về phía suối → hươu AI tới, bật Gai và treo 1 Quả Ước → nuôi tổ kiến thứ 2 → Linh Thức do thám thấy Lang tiến về Mầm-Neo, ping cho bạn co-op (Linh Thử) → Đả Tọa → đột phá tầng → Bế Quan.

### 4.4 Thú: Linh Thử & Lang *(SURV-02b, PROG-11b)*
- **Điều khiển:** joystick, **vuốt để né**, đẩy joystick ra mép để chạy. Nút Đánh/Ăn theo ngữ cảnh (giữ = ăn liên tục, mỗi 1,5s một cắn).
- **Linh Thử:** Tốc 6,6 ô/s, có hang nhiều cửa. **Kho Hạt**: chôn hạt vào Hang cấp 1 (40 hạt, không thối). Hạt chôn ngoài Hang có 20% bị quên và nảy mầm. Đánh đổi: ăn ngay hay trữ cho Đông.
- **Lang:** Tốc 6,0 ô/s. Thịt trong kho **thối sau 10'**, nên phải săn đều.
- **TTK:** Lang vs Lang cùng tầng 7,5s · Lang vs Linh Thử 5,0s. Con mồi tự vệ bằng phát hiện sớm, tốc độ, hang và Ấu Linh, **không bằng máu dày**.

### 4.5 Ma trận "ai ăn ai" (MVP) *(SURV-10b)*
| Kẻ hành động → đối tượng | Linh Mộc | Linh Thử | Lang | Hươu AI |
|---|---|---|---|---|
| **Linh Mộc** | Che bóng, tranh rễ | Quả Ước (nuôi), Nắp Ấm (bẫy) | Gai/Độc/kiến, hút xác | Gai/Độc, Quả Ước |
| **Linh Thử** | Ăn quả và mang hạt (cộng sinh) **hoặc** gặm chồi/Mầm (gây hại), ăn sâu (giúp cây) | Tranh hạt | Con mồi | — |
| **Lang** | Cào Thân (×0,5, không cho No), chỉ để phá Mầm-Neo | **Săn** | Tranh lãnh thổ | **Săn** |

**Nguyên tắc:** thú ăn cây nhận ít hơn phần cây mất (lá → thú 40%). Cây bị gặm thì chậm lại chứ không chết.

---

## 5. Hệ thống sinh tồn — owner: SURV

### 5.1 HUD 4+1, ≤5 nút *(SURV-01b, PX-11b)*
| Loài | 4 chỉ báo cố định | +1 | Nút (≤5) |
|---|---|---|---|
| **Linh Mộc** | Vòng HP 3 lớp · Thủy · Quang Tinh · Linh Khí | Tu vi | Phòng thủ (bánh xe 2) · Hạt · Quả · Cộng sinh · Linh Thức. Chạm map để bắt Vệt Nắng, kéo để vươn rễ. Đả Tọa/Độ Kiếp/Bế Quan nằm trong menu ngữ cảnh |
| **Linh Thử / Lang** | HP · Linh Khí · No · Thể Lực (vòng quanh joystick) | Tu vi | Đánh/ăn · 3 skill · Thần Thông (ô khóa tới U1, hiển thị như mục tiêu) |

**[orch]** Bộ chỉ báo của thú lấy theo SURV (owner). PX từng ghi "Thủy" cho thú, nhưng Khát của thú đã bị bỏ từ R1. Trạng thái hiện bằng icon 24dp. Dưỡng Chất, Ánh Sáng% và Quỹ Vùng hiện bằng hình ảnh trên map.

### 5.2 Needs: động vật (C1, thời gian thực)
| Need | Linh Thử | Lang | Ngưỡng C / W / Cr / L | Hậu quả |
|---|---|---|---|---|
| **No** decay | −5/phút (chạy ×1,5, Đông ×1,4) | −4/phút | 100–60 / 59–25 / 24–1 / 0 | C: hồi HP 1%/5s · W: ngừng hồi · Cr: Thể Lực max −30% · 0: −1% HP/3s |
| Lần Warning đầu tiên | **8,2'** | **10,2'** | — | Trong mục tiêu 8–15' |
| No hồi | Hạt +8 · quả +15 · sâu +6 · cỏ +3 | Thịt +30/cắn · Linh Thử nguyên con +25 · xác thối +12 (25% Trúng Độc) | — | Ăn khi đã no: phần dư → linh khí ×50% |
| **Thể Lực** | Chạy −10/s · né −20 · hồi +25/s | Chạy −12/s · đòn −15…−25 · hồi +20/s | 100–40 / 39–15 / 14–1 / 0 | <15 không chạy được · 0 choáng 1,5s |
| **HP** | theo PROG | theo PROG | <25% | Để lại vệt máu, đánh hơi được trong 12 ô |

### 5.3 Needs: Linh Mộc
| Need | Decay | Ngưỡng | Hậu quả | Hồi |
|---|---|---|---|---|
| **Thủy** | Ngày −3/phút · đêm −1/phút · +0,5/phút mỗi bậc chiều cao · Hạ ×1,5 | 100–50 / 49–30 / 29–10 / 0 | <30: quang hợp ×0,5 · <10: rụng lá · 0: Tâm Rễ −1%/5s (chết héo sau ~8') | `6×(1−e^(−W/4))`/phút, W = ô ẩm + 3×ô suối · mưa +10/phút · sương bình minh +15 |
| **Quang Tinh** (kho 0–150) | Đêm hô hấp ≈ −4/phút (C1) | 0 vào ban đêm thì tiêu Tán để thở | — | Ngày ≈ +6/phút khi nắng đủ, Vệt Nắng ×2,5 |
| **Linh Khí** | theo skill | — | — | Theo vòng, Linh Quang (1/3', +5) |
| Dưỡng Chất (panel phụ) | không decay | — | Thiếu thì không lớn, không ra hạt | Đất màu, xác, phân thú, hạt bị quên |

- **Ngân sách 1 ngày-rừng (C1):** +72 (ngày) +17 (Vệt Nắng) −24 (đêm) ≈ **+65 Quang Tinh**. Chi tiêu: lá 2 · ô rễ 8 · bậc chiều cao 40 · hạt 25 · quả 15 · phòng thủ 10–20. Không bao giờ đủ cho tất cả, và đó là chỗ có quyết định.
- **Ánh Sáng%:** 100% ở chỗ trống, mỗi tán cao hơn chồng lên trừ 30%, sàn 10%. Cao thì nhiều nắng nhưng tốn Thủy, bị nhìn thấy từ xa và hút sét.

### 5.4 Môi trường × needs *(SURV-05b, C6-B′)*
| Điều kiện | Thú: No | Mộc: Thủy | Mộc: quang hợp | Thức ăn | Ghi chú | Nhãn |
|---|---|---|---|---|---|---|
| Đêm (6') | ×1 | ×0,33 | 0 (hô hấp) | — | Kẻ săn AI +50% | MVP |
| **Xuân** | ×0,9 | ×1 | ×1,2 | Cỏ ×1,3 · con mồi AI ×1,2 | Mùa Linh Triều | MVP |
| **Đông** | ×1,4 | ×0,5 | ×0,4 (rễ ×1,6) | Hạt ×0,3 · cỏ ×0,4 | Mùa đói | MVP |
| Hạ / Thu | ×1 / ×1,1 | ×1,5 / ×1 | ×1,3 / ×0,9 | — / quả ×1,5 | — | U1 (MVP chỉ đổi palette) |
| Mưa | — | +10/phút | ×0,6 | — | Xóa mùi | MVP |
| Giông | — | +10/phút | ×0,4 | — | Mỗi 20s sét đánh vật cao nhất trong 8 ô (30% Thân max). Code dùng chung với sét kiếp | MVP |
| Sương mù, lũ | | | | | | [Cắt] |

### 5.5 Sổ Sinh Năng *(SURV-09b, PROG-17)*
Khi một người chơi chết, **Sinh Năng = 20 CT**, chia như sau:
| Phần | CT | Ai nhận | Hệ số |
|---|---|---|---|
| Kẻ ăn | 8 | Chỉ khi **ăn/hấp thu** (4s, bị ngắt được) | × m(g) của kẻ giết |
| Linh Hạch | 4 | Ai nhặt trước. Quạ AI lấy mất sau 90s, tự tan sau 30' | × m(g) của người nhặt |
| Đất | 8 | Rễ/nấm trong 3 ô + **+2% Linh Quỹ vùng** | Không nhân hệ số |

Con mồi NPC: nhỏ ×0,5, vừa ×1, lớn ×2. **Kill-trading bị lỗ:** kẻ giết +8 CT, nạn nhân mất tới 130 CT, cùng một cặp chỉ cho CT 1 lần/30'.

### 5.6 Item sinks & Thiên Tài Địa Bảo *(SURV-18b, 22)*
- **Sinks:** Linh Hạch tan sau 30' · thịt thối 10' · quả rụng 5' · 20% hạt chôn bị quên · rễ teo khi Thủy <30 · Thiên Tài Địa Bảo tan sau 24h.
- **Thiên Tài Địa Bảo** (Cơ Duyên đột phá): **Linh Thảo** (Trung Lâm, 1/vùng/ngày-rừng) · **Huyết Tinh** (từ kẻ săn AI mạnh) · **Lôi Mộc Tâm** (chỉ có trên cây vừa bị sét đánh). Luyện Hóa [1.0].

| Giai đoạn | Thứ khan hiếm | Thứ dư |
|---|---|---|
| C1–C2 (Bìa) | No, Thủy, an toàn trước kẻ săn AI | Cỏ, hạt |
| C3–C4 (Trung, Thâm Lâm) | Linh khí, Linh Quỹ, Linh Mạch, Mầm-Neo | Thức ăn cơ bản |
| Đông | Thức ăn (thú), ánh sáng (cây) | — |

### 5.7 Linh Quỹ & Khô Linh [MVP lite] *(SURV-08b, WORLD-03c)*
- Mỗi vùng (~64×64 ô) có một **Linh Quỹ Q (0–100%)**.
- **Tải** của người online: C1–C3 = 1 · C4–C5 = 3 · C6 = 5 · Thần = 0. Cây và nấm tính 0,5.
- **Sức chứa** = 6 + 1/cây-nấm người chơi sống trong vùng (cây offline tính 0,5).
- **Tải > sức chứa:** ΔQ = −35%/h × (tải − sức chứa)/sức chứa.
- **Tải ≤ sức chứa:** +4%/h, cộng 1%/h cho mỗi cây/nấm. Mỗi xác +2%.
- **Trạng thái:** Sung Linh >60% · Bình 30–60% · **Khô Linh <30%** (CT kẻ tiêu thụ −50%, cây/nấm −20%, kill PvP chỉ cho Sinh Năng ×0,5, thú ăn cỏ AI rời vùng, vùng ngả xám).
- **Bìa Rừng có sàn 50%** ("Thiên Đạo Hộ Mầm").
- **Mục tiêu:** 4 Lang C4 farm một vùng Trung Lâm sẽ làm vùng Khô Linh sau **~2h có mặt** (≈3 tối chơi). Tổ hợp 2 Lang + 1 cây không bao giờ làm Khô Linh. PROG sim lại theo mốc 2h.
- **Trung Ấm** dùng chính quỹ này để kể lại cái chết: *"Thân xác ngươi trả 412 linh khí về Đầm Mục."*

### 5.8 Mối đe dọa AI & Ý Chí Rừng *(SURV-13b)*
| Archetype | Tên | State machine | Spawn/vùng (ngày / đêm) | Ai sợ | Nhãn |
|---|---|---|---|---|---|
| Ăn cỏ đàn | Hươu Sừng Ngọc | Graze → Alert → Flee theo đàn → Regroup | 2 đàn × 3–5 | Cây | MVP |
| Kẻ săn | Báo Bóng Đêm. **[orch]** Diều hâu và sói AI trong FTUE là skin của cùng archetype | Idle → Curious → Stalk → Attack → Eat / Flee (HP <30%) | Bìa 1/2 · Trung 2/4 · Thâm 3/5 | Linh Thử, Lang yếu | MVP |
| Bầy côn trùng | Sâu Lửa (template này cũng dùng cho Kiến lite) | Spawn → Swarm → Consume → Disperse | Theo luật Tán >70% | Cây | MVP |
| Ăn xác | Quạ Linh | Circle → Wait → Steal Linh Hạch → Flee | Theo xác | Kẻ vừa giết | MVP |
| Ký sinh / Boss Hộ Rừng | Tơ Hồng Yêu / Cổ Hùng Giữ Suối | — | — | Cây / kẻ có Nghiệp | 1.0 |

**Director lite:**
- `Áp Lực = 0,3·(100−HP%) + 0,3·(100−need thấp nhất) + 0,2·min(100, 3·số ô cách Hang/Tâm Rễ) + 0,2·min(100, 25·số kẻ thù trong 10 ô)`.
- Áp Lực <30 kéo dài 5' thì spawn thêm áp lực. Áp Lực >75 thì 3' không spawn gì mới và mở một "cửa thoát" (quả rơi, mưa xóa mùi).
- **Cân bằng sinh thái:** Lang >35% dân số thì con mồi AI +50%. Cây <15% thì đợt hươu −30%.
- Director cũng script FTUE và lấp rừng khi server vắng (Linh Ảnh).

### 5.9 Lãnh thổ, Hang, Bế Quan/offline *(SURV-12b, PX-04b)*
| Luật | Số |
|---|---|
| Thoát game trong Hang/lãnh thổ rễ | **Bế Quan** ngay. Thú rời thế giới, cây thành bất tử |
| Thoát ở chỗ khác hoặc rớt mạng | **Nhập Định** 30s (60s nếu vừa combat). Trong lúc này thú tự chạy vào bụi/hang ≤5 ô (PX-18) |
| Khi offline | **Miễn mọi decay needs và mọi sự kiện môi trường** |
| Trần tổn thất (mỗi 24h thực) | ≤20% Tán · ≤25% ô rễ ngoài (không tính bán kính 2 quanh Tâm Rễ) · kho Hang bị cướp ≤50%. **Tâm Rễ và Thân bất tử** |
| Phòng thủ thụ động khi offline | Chỉ cho Dưỡng Chất, **không cho CT** |
| Tăng trưởng khi offline | Quang hợp 25% vào Quang Tinh (trần 8h, trần kho 150) + Kế Hoạch Sinh Trưởng (MVP: Tán mọc lại) |
| **CT offline** | **0.** Chỉ có Mộng Tích (§6.8) |
| Chống giữ đất ảo | Offline >48h thì rễ teo 1 ô/ngày (không teo vào bán kính 2) |
| Quay lại | **Mộng Báo** ≤10s: *"Tán đã lành · [Hắc Lang] gặm 14% Tán, trúng độc bỏ chạy · Mộng Tích 100% · Đại Linh Triều sau 6h"* |
| Solo | Catch-up mô phỏng tối đa 8h, cùng luật |

**Hang:** mỗi người 1 Hang cấp 1 [MVP] (kho 40, nơi Đả Tọa, nơi đặt Ổ Hậu Duệ). Cấp 2–4 [1.0].

---

## 6. Tiến trình: cảnh giới, tiến hóa, độ kiếp — owner: PROG

### 6.1 Thất Cảnh (7 cảnh giới, 3/2/2) *(PROG-01c, C1 nhất trí 4/4)*
| C | Khung | Cấp rừng | Kiếp khi rời cảnh | Lời hứa mở khóa | Nhãn |
|---|---|---|---|---|---|
| 1 | **Khai Linh** | Hạ Lâm · Bìa | Tiểu Kiếp | 2 Bản Năng, ăn/quang hợp | MVP |
| 2 | **Luyện Khí** | Hạ Lâm · Bìa → Trung | Tiểu Kiếp | Co-op, Linh Thức lite + Kiến (cây), Huyết Mạch Ấn | MVP |
| 3 | **Trúc Cơ** | Hạ Lâm · Trung (Áp Chế n=9) | **Phi Thăng Kiếp I** | **Chọn Huyết Mạch** (đổi sprite), A1 | MVP |
| 4 | **Kết Đan** | Thâm Lâm (MVP) → Linh Lâm (1.0) | **Trung Kiếp** | Keystone 1, A2, Hóa Hình Mộng | MVP |
| 5 | **Hóa Hình** | Linh Lâm | **Phi Thăng Kiếp II** | Bản Thể (U1) ‖ Nhân Hình (Post), Thần Thông | U1 |
| 6 | **Nguyên Anh** | Thần Lâm | **Thiên Kiếp** (cần Thần Cách) | Xuất Khiếu thật, Nguyên Thần Bất Diệt, Keystone 2 | Post |
| 7 | **Thành Thần** | Lõi Thần Lâm | — | Thần Vị / Quy Căn | Post |

Mỗi cảnh C1–C6 có 3 tầng **Sơ / Trung / Hậu kỳ**, tổng 18 tầng. **UI** luôn hiện dạng "**C4 · Ngưng Tâm Mộc · Trung kỳ**", kèm vòng màu dưới chân.

### 6.2 Tên cảnh giới theo loài (tên riêng, cấp tương đương) *(WORLD A′, PROG-02b)*
| C | Khung | **Linh Mộc** | **Linh Thử** | **Lang** | Khuẩn [1.0] | Linh Thảo [1.0] | Lộc [Post] | Trùng [Post] |
|---|---|---|---|---|---|---|---|---|
| 1 | Khai Linh | Manh Nha | Khai Trí | Ấu Lang | Bào Tử | Phá Thổ | Ấu Lộc | Ấu Trùng |
| 2 | Luyện Khí | Trát Căn | Tàng Thực | Lang Nha | Khuẩn Ty | Liên Căn | Linh Lộc | Thoát Xác |
| 3 | Trúc Cơ | Thành Tán | Ẩn Huyệt | Lang Cốt | Khuẩn Võng | Thành Thảm | Lộc Giác | Kết Kén |
| 4 | Kết Đan | Ngưng Tâm Mộc | Thử Đan | Lang Đan | Ngưng Tán | Ngưng Dược Tính | Lộc Đan | Phá Kén |
| 5 | Hóa Hình | Thụ Nhân ‖ **Cổ Mộc Yêu** | Thử Nhân ‖ **Yêu Thử** | Lang Nhân ‖ **Yêu Lang** | Khuẩn Nhân ‖ Khuẩn Yêu | Thảo Tinh ‖ Dược Yêu | Lộc Tiên ‖ Yêu Lộc | Trùng Nhân ‖ Trùng Yêu |
| 6 | Nguyên Anh | Mộc Hồn | Thử Hồn | Nguyệt Lang Hồn | Địa Mạch Hồn | Vạn Diệp Hồn | Bạch Lộc Hồn | Phong Hồn |
| 7 | Thành Thần | Mộc Thần | Thử Thần | Lang Thần | Luân Hồi Thần | Bách Thảo Thần | Lộc Thần | Trùng Thần |

**Quy tắc tên:** Hán-Việt, 2–4 âm tiết. Ở C5 tên tách theo Đạo: **Nhân Hình ‖ Bản Thể** (U1 chỉ có Bản Thể). Tên gắn với cơ chế: Thử C2 *Tàng Thực* là lúc bắt đầu trữ hạt · Trùng C3 *Kết Kén* là kiếp bất động, bầy phải canh · Thảo C4 *Ngưng Dược Tính* là lúc chính bạn thành linh dược Nhân Tu săn. Tầng thứ 4 nếu sau này cần tên là **Viên Mãn**.

### 6.3 Đường cong tu vi *(PROG-04c, sim N)*
Công thức: `CT_tầng = CT_cảnh × (0,30 / 0,33 / 0,37)`. Chi phí Cơ Duyên/kiếp: 5 / 15 / 30 / 45 / 70. Con số hiển thị **TV = CT × 10 × 1,25^(n−1)** (để người chơi thấy số lớn dần).

| C | CT tầng S/T/H | CT cảnh | Kiếp (CT) | Lũy kế | Phiên Mid/cảnh | Tuần Casual | **Tuần Mid** | Tuần Core |
|---|---|---|---|---|---|---|---|---|
| 1 Khai Linh | 11/12/13 | 36 | Tiểu (5) | 41 | 0,6 | 0,3 | 0,1 | 0,1 |
| 2 Luyện Khí | 30/33/37 | 100 | Tiểu (15) | 156 | 1,6 | 1,2 | 0,5 | 0,3 |
| 3 Trúc Cơ | 54/59/67 | 180 | Phi Thăng I (30) | 366 | 2,8 | 2,9 | **1,1** | 0,6 |
| 4 Kết Đan | 84/92/104 | 280 | Trung (45) | 691 | 4,4 | 5,4 | **2,2** | 1,2 |
| 5 Hóa Hình | 114/125/141 | 380 | Phi Thăng II (70) | 1.141 | 5,9 | 8,9 | 3,6 | 2,0 |
| 6 Nguyên Anh | 156/172/192 | 520 | Thiên Kiếp | **1.661** | 8,1 | 13,0 | **5,2** | 2,9 |

(Chưa tính chết và Bù Đắp.) **Dry spell:** mỗi tầng tối đa 3,0 phiên Mid. Ở C4–C5 cứ khoảng 1,5–2 phiên có một Ngộ Đạo hoặc một lần độ kiếp.

**Unlock Timeline (Mid):**
| Thời điểm | Mở khóa |
|---|---|
| Phút 0–16 | FTUE Linh Thử (đường cong kịch bản Tiền Thân ×3): C2 ở phút ~7, chết ở phút 14–16 |
| Phút 16–29 | Linh Mộc (Hồi Ức). **C1 + Tiểu Kiếp lên C2 ở phút ~29** |
| Phiên 2 | Bản Năng 2, co-op, Linh Thức + Kiến (cây), Ngộ Đạo đầu tiên |
| Phiên 3 (0,5 tuần) | **C3: chọn Huyết Mạch**, A1 |
| Phiên 6 (1,1 tuần) | **Phi Thăng Kiếp I → Thâm Lâm**, Keystone 1, A2 |
| Phiên 11 (2,2 tuần) | **Trần MVP (hết C4):** luân hồi đổi loài, Hóa Hình Mộng, tranh Linh Nhãn, Công Đức (U1) |
| Phiên 18 (3,6 tuần) | [U1] Phi Thăng Kiếp II |
| Phiên 26 (5,2 tuần) | [Post] Thiên Kiếp |

### 6.4 Huyết Mạch: 2 nhánh mỗi loài, vòng Ngũ Hành khép kín *(PROG-05b, WORLD-13c)*
| Loài | Nhánh 1 | Nhánh 2 | Nhánh [1.0] |
|---|---|---|---|
| **Lang** | **Huyết Lang** (Hỏa, nghiêng Sát): chảy máu, hút máu. *Ấn:* 20 đòn gây chảy máu / 5 lần ăn xác tươi | **Phong Lang** (Mộc, nghiêng Hợp): lướt, săn bầy. *Ấn:* 5 lần săn cùng đồng minh | Băng Lang (Thủy) |
| **Linh Mộc** | **Thiết Mộc** (Kim, Hộ): gai, giữ Tâm Rễ. *Ấn:* 10 lần phản vệ thành công | **Linh Quả Thụ** (Mộc, nghiêng Sinh): quả buff đồng minh. *Ấn:* quả bị ăn 15 lần | Huyết Đằng (Hỏa) |
| **Linh Thử** | **Tàng Thử** (Thủy, nghiêng Sinh): trữ hạt, gieo Mầm làm neo cho cây đồng minh. *Ấn:* gieo 10 hạt | **Độn Thử** (Thổ, nghiêng Sát): đào hầm, **Căn Thương**, phá neo. *Ấn:* đào 300 ô | Ảnh Thử |

**Vòng khắc:** Huyết Lang → Thiết Mộc → (Phong Lang, Linh Quả Thụ) → Độn Thử → Tàng Thử → Huyết Lang. Hệ số E: khắc ×1,25 · bị khắc ×0,80. Lửa sự kiện là Căn Thương sinh thái, không thuộc Ngũ Hành. **Learn-by-doing:** nhánh có nhiều Ấn nhất luôn được mở. Sau 10h ở MVP có **12 dạng nhân vật** (3 loài × 2 nhánh × 2 Keystone) × 4 loadout, cộng thứ tự Ngộ Đạo và Túc Tuệ.

### 6.5 Ngộ Đạo (thay cho skill tree) *(PROG-06b)*
- **"Mỗi lần đột phá, chọn 1 trong 3 Ngộ."** Mức độ phức tạp này đọc hiểu được trong 30 giây.
- **Kỹ năng chủ động (mở theo cảnh):** Bản Năng 1 (C1), Bản Năng 2 (C2), A1 (C3), A2 (C4), Thần Thông (C5, U1). **Loadout 3 chủ động + 1 Thần Thông trên mọi nền tảng.** Từ C4 có 4 kỹ năng chủ động nên phải bỏ 1.
- **Keystone:** một cặp loại trừ nhau ở C4, một cặp ở C6 [Post].
- **Ngộ Đạo (draft):** ở mỗi tầng Hậu kỳ C3–C5 và mỗi lần độ kiếp thành công. Pool gồm 4 Bản Năng + 6 Huyết Mạch (4 Notable, 2 Minor). Node khớp với hành vi gần đây có trọng số ×2. Mỗi cảnh được đổi lựa chọn 1 lần.
- **Không respec trong kiếp.** Muốn làm lại build thì Luân Hồi.
- **Ngân sách MVP:** 18 kỹ năng chủ động dựng từ 12 template, 42 node có script, 18 Minor. Thần Thông (6) ở U1.

**Ví dụ: Lang → Huyết Lang**
| Loại | Node | Hiệu ứng | Mở |
|---|---|---|---|
| Bản Năng | Lang Nha / Hú Gọi | Lao cắn ×1,5, CD 12s / lộ vị trí con mồi trong 20 ô trong 4s | C1 / C2 |
| A1 / A2 | Huyết Trảo / Huyết Bộc | ×1,6 + chảy máu 4s / kích nổ chảy máu, hồi 30% lượng đó | C3 / C4 |
| Thần Thông [U1] | Huyết Nguyệt Cuồng | 8s: +30% tốc đánh, hút máu ×2, bị mọi người thấy qua Thần Thức | C5 |
| Keystone C4 | **Huyết Cuồng** ‖ **Thực Cốt** | HP <30% thì +20% sát thương và hút máu ×2, nhưng không nhận hồi máu khác ‖ ăn xác cho lớp Cốt (+4% Thủ, tối đa 5 lớp) | C4 |
| Notable | Khứu Huyết (*chuyển được qua Túc Tuệ*) · Ẩn Phong · Răng Cưa · Nuốt Vội · Mùi Sợ Hãi · Kẻ Đơn Độc | — | pool |

**Ví dụ: Linh Mộc → Thiết Mộc:** Vỏ Cứng (−50% sát thương 5s) · Vươn Rễ · A1 Vỏ Gai (gai 10% → 25%) · A2 **Căn Tỏa** (trói 1,5s mọi kẻ địch trên mạng rễ trong 8 ô) · Thần Thông Thiết Lâm Kết Giới [U1] · Keystone **Bàn Căn** (Tâm Rễ +50%) ‖ **Thiết Tán** · Notable: Rễ Cảm (*chuyển được*: báo kẻ đến trong 20 ô), Nhựa Đắng, Vòng Niên Luân, Hộ Pháp Thụ…

**Build Archetype Cards (MVP):**
| Build | Fantasy | Mạnh | Đối trọng |
|---|---|---|---|
| Huyết Lang · Huyết Cuồng | Kẻ săn đơn độc | Burst, tự hồi | Tàng Thử khắc, Sát Nghiệp |
| Phong Lang · Thực Cốt | Bầy săn | Bầy 3 con làm cây Đổ trong 17s | Chia CT theo party chặn bầy ≥4, Thiết Mộc khắc |
| Thiết Mộc · Bàn Căn | Pháo đài cổ thụ | Một sói cùng cấp không thể làm Đổ | Bất động, Huyết Lang khắc, Độn Thử + lửa |
| Linh Quả Thụ + Tàng Thử (co-op) | Vườn cộng sinh | CT ổn định, Hậu Duệ an toàn | Phụ thuộc đồng minh, Độn Thử phá neo |
| Độn Thử · tận diệt | Kẻ phá rễ | Loài duy nhất giết thật được cây | Mỏng (5s trước sói) |

**Stress-test:** cộng dồn tấn công tối đa chỉ được ×1,32, thấp hơn khoảng cách 1 cảnh (×1,77).

### 6.6 Độ Kiếp *(PROG-07b, SURV-16b, C2)*
| Đột phá | Kiếp | Thời lượng | Chế độ | Nội dung | Thất bại | Nhãn |
|---|---|---|---|---|---|---|
| C1→2, C2→3 | **Tiểu Kiếp** | 60–90s | Riêng | Né lôi có báo trước | −10% CT tầng, thử lại ngay | MVP |
| C3→4 | **Phi Thăng Kiếp I** (Phá Giới) | 2' | **Ẩn** (mây chỉ thấy trong 10 ô, khó hơn 20%) hoặc **Công** (thấy trong 30 ô, báo trước 60s, có Hộ Pháp, cho cosmetic Pháp Tướng) | Lôi (3 đợt × 3 sét, 25% HP max, linh khí làm khiên 1:1) + **Tâm Ma** (bản sao 3 kỹ năng của mình; Tâm Hướng chỉ đổi mẫu, độ khó cố định) | −30% CT tầng + **Đạo Cơ Tổn** 20' (−10% chỉ số). **Không có thời gian chờ 24h** | MVP (Công Kiếp/Pháp Tướng: U1) |
| C4→5 | **Trung Kiếp** | 3' | Ẩn / Công | Dùng lại template trên | như trên | U1 |
| C5→6 | **Phi Thăng Kiếp II** | 4' | Ẩn / Công | 3 pha, đổi thời tiết vùng | như trên | U1 |
| C6→7 | **Thiên Kiếp** | 10' | **Luôn Công** (world event) | Cần Thần Cách. Ai cũng có thể giúp hoặc phá | Do sét: xem Câu hỏi mở Q3. **Bị sinh vật khác giết: chết thật**, Đạo Quả ×2 | Post |

- **Độ khó:** sát thương kiếp = gốc × (1 + 0,10 × Sát Nghiệp, trần +50%) × (1 − 0,15 × số lần thất bại liên tiếp, sàn 0,55). Mục tiêu: 60–70% qua ở lần đầu, ≥95% sau 3 lần.
- Kẻ độ kiếp kẹt trong vòng kiếp, gây 50% sát thương ra ngoài. Mọi trạng thái ẩn bị phá khi bước vào vòng. **Hộ Pháp** cho Công Đức. **Đánh Úp Kiếp** cũng tính Sát Nghiệp như giết thường.
- **Cây phải chuẩn bị** vì không chạy được: rễ vào ô ẩm (−20% sát thương sét), Tích Lôi Mộc, Mầm-Neo dự phòng.

### 6.7 Hóa Hình & Linh Thức *(PROG-08b, 09b, WORLD-14c)*
- **Bản Thể** [U1] (chi phí S): sprite +30%, +10% chỉ số, 1 Keystone độc quyền, tên Yêu. Với cây có **Di Căn** (tùy chọn). **MVP chỉ có Hóa Hình Mộng.**
- **Nhân Hình** [Post]: rig humanoid chung, −15% chỉ số chiến đấu, 2 ô Pháp Bảo, đọc khắc đá, vào trại Nhân Tu. Cây ở dạng người đi trong bán kính sợi mệnh 30 ô quanh Bản Thể, chết khi **Tâm Rễ** = 0. Lore hồi 2: *"kẻ ăn nhiều nhất trở thành kẻ chặt cây"*.
- **Linh Thức lite** [MVP] → **Xuất Khiếu** (C6) + **Nguyên Thần Bất Diệt** [Post]: thân chết thì Nguyên Thần thoát ra, về được Linh Huyệt trong 60s thì tính như Hậu Duệ không cần neo.

### 6.8 Thiên Đạo Gia Trì, Mộng Tích, party *(PROG-17, C4)*
- **Gia Trì:** mọi bonus CT **cộng** lại (Mộng Tích +1 · Bù Đắp +0,5 · loài đang thiếu +0,25 · Mộ Linh +0,2 · bonus vòng +0,15/0,3/0,5 · Linh Triều +1), **trần ×3**.
- **Hồi Ức** (catch-up sau chết) là **hệ số nhân riêng, nằm ngoài trần Gia Trì**: `rate = base × min(GiaTrì, 3) × HồiỨc` *(sửa ở R4 của PROG; nếu để trong trần thì Luân Hồi ở C5 tốn 1,38 tuần, vượt trần PX)*. Hồi Ức tự tắt khi chạm đỉnh cũ.
- **Mộng Tích** (rested): đầy sau 8h offline, cho **×2 CT trong 30' chơi đầu**. Đây là bonus hằng ngày duy nhất.
- **Party:** tổng CT nhóm = 1 + 0,6·min(k−1, 2), chia đều. Mỗi người nhận 100 / 80 / 73 / 55% khi k = 1 / 2 / 3 / 4, nên đi nhóm 2–3 có lợi, bầy ≥4 thì không.
- **Thiên Đạo Bù Đắp:** +0,5 khi tiến độ dưới 60% của Mid. Catch-up ×2 sau reset chỉ tới hết C3.

### 6.9 Công thức sức mạnh *(PROG-11b)*
- **Chỉ số theo tầng n (1..18):** `HP, Thân, Tán, Tâm Rễ, Công, Linh Lực = base × 1,10^(n−1)`, tức ×1,33 chỉ số và **×1,77 combat power mỗi cảnh**.
- `Thủ = d × K(n)`, với `K(n) = 100 × 1,10^(n−1)`. `DR = Thủ / (Thủ + K(n_tấn_công))`, trần 75%.
- `Dmg = Công × hệ số kỹ năng × (1 − DR) × E × Crit × Mit`. Crit 5% (trần 40%) ×1,5.
- **Tốc không tăng theo cảnh** (nhánh thay đổi tối đa ±15%). Nhờ vậy "trốn" luôn là một lựa chọn. Thần Thức = base × (1 + 0,05 × (C−1)).
- **Áp Chế:** `n_hiệu_lực = min(n, trần vùng)`. Chỉ áp cho **chỉ số**. Nghiệp và thưởng tính theo cảnh thật.

| Base (n=1) | HP / Thân | Công | d | Tốc (ô/s) | Thần Thức (ô) |
|---|---|---|---|---|---|
| Lang | 420 | 50 | 0,40 | 6,0 | 14 |
| Linh Thử | 300 | 26 | 0,30 | 6,6 | 16 |
| Linh Mộc | Thân 1.260 (Tán và Tâm Rễ mỗi lớp 0,5×) | 30 (rễ quất, gai 10%) | 0,80 | 0 | 10 (+ Rễ Cảm) |

**PvP theo chênh lệch cảnh (sim R):**
| Chênh | 1 người thấp hơn thắng | 2 người thấp hơn | 3 người thấp hơn |
|---|---|---|---|
| 1 cảnh | 15% | 96% | 100% |
| 2 cảnh | 2% | 70% | 99% |
| 3 cảnh | 0% | 26% | 86% |

---

## 7. Cái chết, Luân Hồi & meta — owner: SURV (luật) · PROG (số) · WORLD (nghi thức) *(C4 nhất trí 4/4)*

### 7.1 Các tầng chết
| Đường | Khi nào | Mất | Giữ | Đạo Quả |
|---|---|---|---|---|
| **Cây Đổ** (không phải chết) | Thân = 0 | Tán, 25% CT tầng, Mộc Tàn 120s | Mọi thứ khác | 0 |
| **Hậu Duệ** (tầng 1: dòng dõi) | Neo còn sống (Mầm-Neo · Huyết Noãn trong Hang · Ổ Hạt · [1.0] Ký Hồn Mộc), chưa dùng trong 24h thực | Về **Sơ kỳ 0% của đại cảnh hiện tại**, **mất tối đa 130 CT**, kho cá nhân | Cảnh giới, Huyết Mạch, Ngộ, Keystone, lãnh thổ. **Hồi Ức ×1,5 tới đỉnh cũ** | **0** (không qua Trung Ấm) |
| **Luân Hồi** (tầng 2: khai ngộ) | Tự chọn, **hoặc** neo bị phá, **hoặc** chết lần 2 trong 24h, **hoặc** chết khi đang Thiên Phạt | Cảnh giới, Huyết Mạch, Ngộ, vật phẩm (rơi tại xác), lãnh thổ (thành dinh dưỡng) | Đạo Quả, **Túc Tuệ** (1 Notable), Codex, Tiền Kiếp Ấn. **Hồi Ức ×4** tới đầu cảnh cũ, rồi **×2** tới đỉnh | **25% × CT lũy kế của kiếp** (+25% nếu Oán Linh, +100% nếu chết trong Thiên Kiếp) |
| **Đại Kiếp** (cuối chu kỳ) | Mọi người | Như Luân Hồi | Như Luân Hồi | 25% × CT lũy kế × (1,0 / 1,5 nếu đã Phi Thăng II / 2,0 nếu Thành Thần) |

**Chi phí chết, tính bằng phiên Mid (sim R4-C4):**
| Chết tại | Hậu Duệ (TB / tệ nhất) | Luân Hồi ×4/×2 |
|---|---|---|
| C3 | 0,83 / 1,35 | 1,3 phiên (0,26 tuần) |
| C4 | 1,00 / 1,35 | 2,5 (0,49 tuần) |
| C5 | 1,10 / 1,35 | 4,1 (0,82 tuần) |
| C6 | 1,16 / 1,35 | 6,4 (1,28 tuần)* |

\*Ở C6, Luân Hồi chỉ xảy ra khoảng 12,5% số lần chết (khi Nguyên Thần bị bắt). Trần PX (Hậu Duệ trung bình ≤1,5 phiên, Luân Hồi ≤1 tuần) **đạt ở C2–C5**. Thông điệp cho người chơi: *"chết thì mất khoảng một buổi; đổi loài thì mất vài buổi nhưng được Đạo Quả, loài mới và Túc Tuệ."*

- **Hồn Hộ 10'** sau khi sống lại: kẻ có g≥1 giết lại trong thời gian này nhận 0 CT.
- **Nhịp:** từ lúc chết tới lúc điều khiển kiếp mới ≤20s. Có quyết định thú vị trong ≤90s.
- **KPI:** ≥35% số lần chết đi vào Luân Hồi. Nếu dưới 30% thì giảm Hồi Ức của Hậu Duệ trước, sau đó mới nâng trần lên 160 CT.

### 7.2 Nghi thức (WORLD-11c)
- **Hậu Duệ:** timelapse 3s "mầm/trứng nứt ra".
- **Trung Ấm** [MVP]: lần đầu 45s, từ lần sau 8–12s và bỏ qua được. (1) Camera giữ ở xác, timelapse phân hủy, dòng tóm tắt lấy số từ Linh Quỹ. (2) Bà Khuẩn nói 1 câu chọn từ pool ~60 câu theo cách chết. (3) Chọn loài và điểm sinh.
- **Biên Niên Kiếp** [MVP]: 1 trang tự sinh cho mỗi kiếp, chia sẻ thành ảnh được. Vd: *"Kiếp thứ 4 — Lang 'Khói'. Sống 9 ngày-rừng. Ăn 41 sinh linh. Thất bại ở Phi Thăng Kiếp. Ngã xuống đêm Đông năm 2."*
- **Nghiệp Duyên** [U1]: Duyên với loài X tăng khi ăn X, bị X ăn, hấp thu xác X, cộng sinh với X. **Không khóa loài.** Giá loài thứ 4 trở đi = 300 × (1 − 0,2 × Duyên), sàn 40%.
- **Tiền Kiếp Ấn** [U1]: dấu nhỏ trên sprite kiếp sau (vd sói có vân lá mờ vì từng là cây). Kiếm được, không bán. Skin không được che Ấn.
- **Tâm Hướng** qua luân hồi: lùi 50% về tâm la bàn, nên "tính cách" tồn tại xuyên loài.

### 7.3 Đạo Quả Bàn (meta) *(PROG-10c, C6-B′)*
**100% mở khóa ngang. Không node nào cho chỉ số chiến đấu hay % CT.**
| Node | Hiệu ứng | Giá | Nhãn |
|---|---|---|---|
| Huyết Mạch Thiên Kiến | Thấy điều kiện Ấn từ C1 | 80 | **MVP** [orch] |
| Loadout Preset II | Lưu 2 bộ 3+1 | 120 | **MVP** [orch] |
| Túc Tuệ ô 2 | Mang 2 Notable sang kiếp sau | 400 | **MVP** [orch] |
| Tiền Kiếp Ấn I · Mộ Linh Đầu Thai · Vùng Sinh · Codex Ký Ức · Hào Quang Kiếp | — | 60–500 | U1 |

**[orch]** B′ cắt Đạo Quả Bàn từ 6 xuống 3 node. Orchestrator chọn 3 node có chi phí code thấp nhất và có tác động rõ tới build; PROG xác nhận ở R6. Phần Đạo Quả dư chảy vào **Tiền Kiếp Ấn các bậc** (prestige vô hạn, chỉ để xem). **Ở MVP cả 3 loài mở ngay sau FTUE.** Mid được khoảng 1.000 Đạo Quả mỗi Đại Kiếp đầy đủ.

---

## 8. Thiên Đạo Luật: PvP tự do & chống bắt nạt — owner: PROG/SURV (số) · PX (UX)

**Không có công tắc PvP ở Rừng chung.** `g` = cảnh giới **thật** của kẻ giết − cảnh giới thật của nạn nhân. Chỉ số combat tính **sau** Áp Chế. Thưởng và Nghiệp tính theo **cảnh thật**.

| g | m(g): CT kẻ ăn / Linh Hạch | No | Sát Nghiệp | Nạn nhân |
|---|---|---|---|---|
| ≤0 (**Nghịch Thiên**) | × (1 + 0,5·\|g\|) | 100% | 0 | — |
| 1 | × 0,5 | 100% | **0** (chuỗi thức ăn tự nhiên) | +10% Đạo Quả |
| ≥2 | **× 0** | **100%** (ăn vẫn là ăn) | **+1** (+2 nếu nạn nhân có Ấu Linh) | **Oán Linh** +25% Đạo Quả, 1 lần/24h |
| Làm cây Đổ khi g≥2 | — | — | +1 (trừ khi hai cây tranh ô rễ) | — |

| Bậc Nghiệp | Hậu quả | Nhãn |
|---|---|---|
| ≥1 | Hào quang đỏ thấy trong 20 ô. Kiếp +10% sát thương mỗi Nghiệp (trần +50%) | MVP |
| ≥3 **Huyết Sát** | Hiện trên bản đồ vùng. Ai hạ được nhận thưởng ×3 (+ Công Đức) | MVP |
| ≥5 **Thiên Phạt** | Sét đuổi trong 1 ngày-rừng (20'), mỗi 60s một đòn 10% HP. **Đồng hồ dừng khi offline.** Sống sót thì Nghiệp về 0 nhưng mất 10% CT tầng | U1 |
| Giảm Nghiệp | −1 sau mỗi 2h **online**. Offline không giảm | MVP |
| Miễn trừ | Đánh trả người đã tấn công mình trong 60s (gai thụ động không tính). Cùng một cặp: CT 1 lần/30', Nghiệp và Oán Linh 1 lần/24h | MVP |

- **Ấu Linh** *(C5 nhất trí 4/4)*:
  - Kéo dài **3h trong Rừng chung hoặc tới hết C2, cái nào đến trước**.
  - Sát thương nhận từ g≥2 bị giảm 60%. Người có g≥2 **không thấy Ấu Linh trên Thần Thức** (chỉ thấy bằng mắt trong 5 ô).
  - Kẻ đánh Ấu Linh nhận 0 thưởng và bị đánh dấu **Bất Nhân** 5'.
  - **Mất khiên nếu chủ động tấn công người chơi khác.** Báo trước 10' khi khiên sắp hết.
- **Áp Chế:** n = 9 ở Bìa/Trung Lâm của Hạ Lâm, n = 15 ở Linh Lâm, không trần ở Thâm Lâm và Thần Lâm. Ví dụ: C6 Hậu vào Rừng Non bị nén từ ×11,9 xuống ×2,14, người C2 vẫn thắng được 9%.
- **Thoát Sinh:** gây sát thương lên kẻ săn có g≥1 rồi sống sót, ra khỏi tầm trong 30s thì +2 CT (1 lần/10').
- **UX:** vòng cảnh giới dưới chân dùng **màu + hình** (▲ cao hơn / ● ngang / ▼ thấp hơn). Aura Tâm Hướng chỉ hiện khi soi bằng Thần Thức.
- **Đã bỏ:** −HP vì linh khí loãng (PX R1), Linh Khí Thất Thoát cá nhân (SURV R1), Minh Ước (cờ tắt PvP, trái brief).

---

## 9. Nội tâm & endgame — owner: WORLD · PROG

### 9.1 Tâm Hướng (la bàn hành vi) [MVP dữ liệu + aura; Tâm Ma theo mẫu: U1] *(WORLD-13c, C2)*
- **Hai trục, đo hoàn toàn bằng hành vi:** **Sinh ↔ Sát** và **Hợp ↔ Độc**. Chuẩn hóa theo baseline của loài.
- **Thực Sát / Lạm Sát:** giết rồi ăn ≥50% trong 60s thì trục Sát chỉ nhận ×0,3. *Săn để ăn không phải tội; Sát là một đạo hợp lệ, có Keystone riêng.*
- **Nguồn:** Sinh (quả bị ăn, Linh Hóa Địa, Hộ Pháp, hồi linh) · Sát (Lạm Sát, kill có Nghiệp, phá neo của người khác) · Hợp (co-op, cộng sinh) · Độc (bỏ rơi đồng đội, cướp mồi của party, solo kéo dài).
- **Tâm Hướng đổi:** aura (xanh lá / đỏ sẫm / vàng / xám, chỉ thấy khi soi bằng Thần Thức) · 3 biến thể lời chào của mỗi Lão NPC · mẫu Tâm Ma (cùng ngân sách độ khó).
- **Arc nội tâm theo cấp rừng:** Hạ Lâm *"Ta là gì?"* → Linh Lâm *"Ta muốn gì?"* → Thần Lâm *"Ta để lại gì?"*. Flavor text: *"Đạo Quả kết từ đạo tâm."*

### 9.2 Công Đức [U1 bộ đếm + Thần Bia lite · Post Thần Cách] *(WORLD-22, PROG-13b)*
- **Công Đức** là con số đo **"đã nuôi rừng bao nhiêu"**. Nguồn: Quả Ước bị ăn · Linh Hóa Địa · xác được phân giải vào Linh Quỹ · hồi linh trong vùng Khô Linh · Hộ Pháp (2/phút) · săn đàn ăn cỏ quá đông (tín hiệu **Lộc Tràn**: thú săn cũng là người làm vườn) · hạ kẻ Huyết Sát/Thiên Phạt · trả Linh Hạch Cổ Thú về quỹ (chứ không nuốt).
- **Thần Bia lite** (cuối mỗi Đại Kiếp) có 3 bảng: **Hộ Lâm** (top Công Đức) · **Đỉnh Cảnh** (người đầu tiên đạt cảnh cao nhất của mỗi loài) · **Trường Sinh** (kiếp sống lâu nhất). **Không có bảng số kill.**
- **Thần Cách** = Công Đức ≥250 trong kiếp (PROG chỉnh theo telemetry, thời gian đạt giữa các loài lệch nhau ≤±20%).

### 9.3 Thành Thần, Thần Vị, Quy Căn [Post] *(WORLD-21, PROG-13b)*
1. Qua Thiên Kiếp thì thành **C7 Thành Thần**, chọn một trong hai: **Nhập Vị** (chiếm Thần Vị trống, hoặc thách đấu thần đang Thần Suy) hoặc **Quy Căn ngay** (khắc tên lên Thần Bia, luân hồi với Đạo Quả thưởng và Thần Ấn).
2. Thần **rời chuỗi thức ăn**: không ăn, không nhận thưởng giết. Theo **Thần Quy**, thần không tấn công trực tiếp người dưới C5. **Thần Lực = f(Linh Quỹ vực, số sinh linh, độ phủ thực vật).** Thần ban phước hoặc giáng họa lên vùng.
3. **5 Thần Vị Ngũ Hành**: Mộc (Rừng Lá Rộng), Hỏa (Rừng Tro), Thổ (Đồng Cỏ), Kim (Vách Đá Rêu), Thủy (Đầm Mục). Server nhỏ: số ghế = clamp(⌊dân/15⌋, 3, 5).
4. **Nhiệm kỳ 14 ngày**, rồi thần Quy Căn và ghế mở lại. Mỗi chu kỳ có khoảng 12 thần. Core cũng có thể Quy Căn sớm (khóa Đạo Quả ×2) để chơi loài khác.
5. **Đại Kiếp theo lịch cố định**, không kích hoạt theo số ghế. Kích thước chồi Kiến Mộc = tổng Thần Lực Quy Căn của chu kỳ. Chồi lớn thì chu kỳ sau có thêm 1 Linh Mạch và Đạo Quả +5% cho cả server.
6. **Solo:** 5 thần AI. Thành thần là màn kết.

---

## 10. Sự kiện toàn rừng — owner: WORLD (ý nghĩa) · SURV (số) *(WORLD-10c, SURV-17b, C3)*

**Luật chung:**
1. Quạ Già báo trước 24h ngay trong thế giới game, cảnh báo 10' trước giờ G.
2. Mỗi sự kiện có **pha nền 24h**, **đỉnh lặp lại theo ngày-rừng** và **1 cao trào 30' lúc 20:00 giờ khu vực**. Đại Kiếp lặp cao trào ở 2 khung giờ.
3. **Người đang Bế Quan được miễn.**
4. Mỗi sự kiện có **kẻ thắng và kẻ thua theo giới**.
5. Trần 1 sự kiện emergent/ngày.

**Lịch năm-rừng 7 ngày (SURV R4):** Linh Triều ngày 1 · Đại Hạn ngày 3 · Huyết Nguyệt ngày 6.

| # | Sự kiện | Gameplay | Thắng / thua | Di sản | Nhãn |
|---|---|---|---|---|---|
| E1 | **Đại Linh Triều** (hằng tuần, Xuân) | Nền: Linh Mạch +1 mật độ (+0,15 Gia Trì khi đứng trên mạch), lá/quả mọc nhanh. Mỗi bình minh game: Linh Quang ×3. **Cao trào 30':** Linh Nhãn mở (L4), 2 Linh Mạch Huyệt, **Hóa Hình Mộng** cho cây C4 | Thắng: thực vật (rễ trên mạch hưởng mà không cần đi), kẻ tranh Huyệt. Thua: con mồi gần lõi | — | **MVP** |
| E8 | **Đại Kiếp lite** (ngày 28 ở MVP) | 24h "Kiếp Vân": trời tối dần, Linh Nhãn nở hoa. Cao trào: bóng chồi Kiến Mộc mọc lên, rừng cháy sáng trắng, Thần Bia hiện tên, mọi người luân hồi và nhận Đạo Quả, Biên Niên tổng kết | Không ai thua: đây là nghi lễ | Thần Bia | **MVP** |
| E2 | **Huyết Nguyệt** (Đông) | Kẻ săn AI +50% ở Bìa. Mỗi đêm game có Huyết Báo ở Trung/Thâm Lâm, **không ra Bìa**. Thưởng ×2 chỉ khi mồi cùng hoặc cao cảnh hơn. **Thoát Sinh ×2.** Ấu Linh được báo trước 1 ngày | Thắng: thú săn, con mồi giỏi chạy. Thua: Linh Thử ở Trung Lâm | Linh Hạch yêu thú | U1 |
| E6 | **Đại Hạn** (Hạ) | Thủy decay ×2, suối hẹp lại, thú tụ về suối | Thắng: Lang, rễ sâu. Thua: cây | Cây qua ≥3 đỉnh nhận **Hạn Căn** (−20% Thủy decay cả kiếp) | 1.0 |
| E3 | **Đại Hỏa** (Hạ + sét) | Lửa lan 1 ô/8s trên ô khô, sau đó thành Rừng Tro | Thắng: cây tiên phong, nấm. Thua: cây già | Tro (dinh dưỡng ×3), diễn thế | 1.0 |
| E4 | **Đại Di Cư** (Thu) | Đàn thú AI băng ngang map | Thắng: thú săn, cây có quả. Thua: cây non trên đường | Hạt đi xa | 1.0 |
| E7 | **Bào Tử Triều** (sau một ngày nhiều cái chết) | Sương bào tử, nấm mạnh lên, đầu thai tại Mộ Linh +1 Duyên | Thắng: nấm | — | 1.0 |
| E5 | **Tu Sĩ Nhập Sơn** (khi nhiều C5+ tụ một vùng) | Đoàn Nhân Tu AI săn mục tiêu cảnh cao nhất. Không có cờ đình chiến | Thắng: kẻ phòng thủ. Thua: kẻ mạnh nhất | Công Đức | Post |
| — | **Linh Tức** (vi mô, mỗi ~90' với giờ trôi ngẫu nhiên, kéo dài 10') | Bonus tu vi trong vùng, cộng vào Gia Trì. **[orch]** PROG chốt hệ số; FTUE dùng ×2 | — | — | MVP |
| — | **Kỷ Nguyên modifier** (PX-22) | 1 luật xoay vòng mỗi kỳ dạng data (vd *Kỷ Nguyên Hạn: Thủy decay ×1,3*) | — | — | U1 |

---

## 11. Chế độ chơi, server, co-op — owner: PX *(PX-09b)*

| Bậc | Chế độ | Kỹ thuật | Nhãn |
|---|---|---|---|
| T0 | **Rừng riêng** (solo + AI/Linh Ảnh, độ khó chỉnh theo 3 trục) | Cùng mô-đun sim, room local trên client, cloud save | MVP |
| T1 | **Co-op trong Rừng chung**: party ≤4 qua invite link, PvP với người ngoài nhóm | Colyseus room chung | MVP |
| T1b | Phòng co-op riêng (PvE + PvP nội bộ tùy chọn) | Room private | U1 |
| T2 | **Rừng chung Hạ Lâm**: ≤40 CCU/phòng, ≤150 cư dân, PvP luôn bật | Colyseus server-authoritative, 10–15 Hz, interest management theo chunk | MVP |
| T3 / T4 | Linh Lâm 384² / Thần Lâm 512² + Thần Vị | Zone / có thể cần multi-process | 1.0 / Post |

- **Chế độ ngủ (PX-20):** phòng không có ai online thì sim chạy 1 Hz theo tile, catch-up khi có người vào. Rừng vẫn sống 24/7 gần như miễn phí.
- **Khu vực:** Singapore trước (VN/SEA). EU/US khi DAU ngoài SEA >30%. Gộp phòng khi CCU <8.
- **Moderation cho 1 người:** **không chat tự do** (chỉ emote và câu soạn sẵn), **không tên tự do** (tên là "Đạo hiệu" sinh tự động, vd *Thanh Phong Lão Tùng*), kill-switch T2, công cụ admin tối thiểu. Ops ≤6h/tuần.

**Chi phí (phải benchmark ở tuần 2):**
| DAU | CCU đỉnh | Server + DB/tháng | Doanh thu ad (ARPDAU 0,01–0,03 USD) |
|---|---|---|---|
| 1K | ~100 | ~30 € | 300–900 USD |
| 10K | ~1.000 | ~100–150 € | 3K–9K USD |
| 50K | ~5.000 | ~500–700 € | 15K–45K USD |

---

## 12. FTUE 20 phút: "Chuột mang hạt" — owner: PX · WORLD *(PX-08b, WORLD-20, SURV-21)*

Nguyên tắc: mỗi bước dạy **một** động từ mới. Kiếp đầu dùng đường cong kịch bản Tiền Thân ×3. Cây có tiếng nói từ giây thứ 10. Cái chết là **lựa chọn đọc được**. FTUE chạy 100% local.

| Phút | Beat | Học được | Cảm xúc | UI mở thêm |
|---|---|---|---|---|
| 0:00–0:40 | Mộng Hỏa rơi qua tán **Lão Tùng**: *"Lại một đốm mộng hỏa… Sống đi, nhỏ bé."* Chạm để nhập vào Linh Thử | Chạm/kéo để đi | Kỳ vĩ | Joystick |
| 0:40–3:00 | Ăn hạt linh thảo phát sáng | Ăn = tu vi | Thỏa mãn | Thanh tu vi, No |
| 3:00–5:00 | Bóng diều hâu AI lướt qua. Nút "Ẩn" hiện khi đứng cạnh bụi. Thấy viền Ấu Linh | Có kẻ săn, trốn được | Hồi hộp | HP |
| 5:00–7:30 | **Tiểu Kiếp C1→C2:** 3 tia sét nhỏ, kéo để né | Đột phá là khoảnh khắc lớn | **Hùng tráng** (mốc fun #1) | 1 nút skill (chọn Bản Năng) |
| 7:30–10:30 | Cắn vỏ một cây non thì bị gai đâm. Đi vòng lại thì Lão Tùng thả **Linh Quả**: chuột ăn và **ngậm hạt** | Cây có ý thức: có thể đánh, có thể cho | Ngạc nhiên | Icon hạt trong má |
| 10:30–12:00 | Thanh **Thọ Nguyên** (12', chỉ có ở FTUE). Quạ Già báo Linh Tức | Sinh mệnh có hạn, rừng có sự kiện | Khẩn trương nhẹ | Thọ Nguyên |
| 12:00–14:00 | Sói AI tiến về ổ chuột con. **Chọn:** (A) dụ sói ra xa, Đạo Quả ×1,5 "Hộ Ổ", Tâm Hướng nhích về Sinh/Hợp; hoặc (B) về chết già dưới gốc Lão Tùng, được Linh Thổ +30% đầu kiếp. Né sói tới hết Thọ Nguyên ở A thì được achievement "Nghịch Thiên" | Cái chết là lựa chọn | Day dứt | — |
| 14:00–15:30 | **Trung Ấm (45s):** xác phân hủy, *"Thân xác ngươi trả 38 linh khí về Bìa Rừng."* **Hạt trong má nảy mầm từ xác.** Bà Khuẩn: *"Ngươi đã mang nó cả đời. Giờ nó mang ngươi."* | Chết = tiến trình | **Xúc động** (mốc fun #2) | Đạo Quả |
| 15:30–16:00 | Chọn kiếp: 3 loài đều mở. Lựa chọn được highlight: *"Trở thành hạt giống ngươi đã mang"* | Đổi loài | Háo hức | Bánh xe loài |
| 16:00–20:00 | **Linh Mộc** mọc đúng chỗ chuột chết (Hồi Ức ×3): kéo rễ tới đất ẩm, chạm Vệt Nắng, gai đâm hươu con đang gặm lá (Director script ở phút 4–6 của kiếp cây). Đột phá Manh Nha. *"Tán sẽ tự lành khi ngươi rời đi."* | Gameplay thứ hai khác hẳn, offline an toàn | "Mình là cái cây" | Vòng 3 lớp, Thủy, Quang Tinh, Gai |
| ~20:00 | Mở **Rừng chung** (mặc định) / Rừng riêng. Tặng **1 vé Tự Quy** (luân hồi chủ động không cần chết, để P2 thành sói ngay) | — | — | — |
| ~25:00 | **Gương:** một Linh Thử AI ăn Linh Quả đầu tiên của cây và tha hạt đi | Vòng tuần hoàn khép lại | Hiểu ra | — |

**Đo:** ≥80% đạt Tiểu Kiếp trước phút 8 · ≥70% bắt đầu kiếp 2 trong 60s · ≥55% chơi cây tới phút 20 · phân bố A/B trong khoảng 35–65% · ≥50% chọn Linh Mộc ở phút 15 · A/B test "chuột → hạt" với "chọn loài ngay".

---

## 13. UI/UX đa nền tảng & accessibility — owner: PX *(PX-11b)*
- **Ngân sách cứng:** ≤4 chỉ báo cố định + 1 thanh tu vi · ≤5 nút · **3 skill + 1 Thần Thông trên mọi nền tảng** · nút ≥48dp · HUD ≤18% màn hình · landscape · tôn trọng safe-area.
- **Công bằng cross-play:** skill nhắm mềm (soft-lock 30°). PC không có nhiều nút hơn mobile.
- **Cây chơi một tay:** mọi thao tác làm được bằng ngón cái phải. Mục tiêu ≤6 chạm/phút để đạt 90% thu nhập.
- **Accessibility:** vòng cảnh giới dùng màu + hình · icon hướng cho mọi tín hiệu âm thanh · 3 cỡ chữ · giảm chớp/rung khi độ kiếp · giữ ↔ bật cho mọi nút giữ · remap phím PC · tôn trọng cờ tắt chat của portal. Solo chỉnh độ khó theo 3 trục **Sinh tồn / Chiến đấu / Hình phạt chết**. Rừng chung dùng luật cố định.
- **Đo:** bấm nhầm <5% trên mobile · thời gian ra quyết định chạy/đánh ≤1s.

---

## 14. Kinh tế & monetization F2P — owner: PX *(PX-12b)*

### 14.1 Ví và luồng
```
chơi tích cực ~70% ─┐
Mộng Tích ~20%      ├─► [Tu vi = CT] (thanh tiến độ, không phải ví) ─► cảnh giới
sự kiện ~5–8%       │                                                   chết: Hậu Duệ / Luân Hồi; kiếp thất bại −30% tầng
PvP ≤5%             ┘   mọi bonus → Thiên Đạo Gia Trì (cộng, trần ×3); Hồi Ức nhân riêng
ăn/hấp thu/Linh Hạch/quỹ vùng ──► [Linh Khí] ──► skill, khiên kiếp, Đả Tọa (≤15% CT phiên), hồi thương
quang hợp/xác/đất ──────────────► [Quang Tinh ≤150 · Dưỡng Chất · Thủy] ──► rễ, phòng thủ, quả, hạt, kiến
luân hồi/Oán Linh/Đại Kiếp ─────► [Đạo Quả] (meta) ──► Đạo Quả Bàn (ngang), mở loài 4+, dư → Tiền Kiếp Ấn
sự kiện/thành tựu/ad ───────────► [Hoa Lộ] (cosmetic kiếm được) ──► skin (~1 skin/10h chơi)
nạp tiền ───────────────────────► [Ngọc Tinh] ──► skin, Pass. KHÔNG đổi sang ví khác
```

| Exploit | Chặn bằng |
|---|---|
| Kill-trading giữa 2 tài khoản | Sinh Năng cố định, cùng cặp 1 lần/30', Oán Linh 1 lần/24h, Hậu Duệ mất tới 130 CT |
| Chồng hệ số (×82 ở sim K) | Gia Trì cộng dồn, trần ×3 |
| Cây idle offline | 0 CT offline, Quang Tinh có trần |
| Farm phòng thủ thụ động bằng tài khoản phụ | Offline chỉ cho Dưỡng Chất |
| "Tự sát lấy bonus" | Lỗ 26 CT (sim T) |

### 14.2 Monetization (không P2W)
1. **Skin:** không đổi silhouette, hitbox, vòng cảnh giới hay độ tương phản. **Không có skin ngụy trang.** Không che Tiền Kiếp Ấn. Ở PvP có tùy chọn "đối thủ hiện skin mặc định".
2. **Rewarded ads (luôn opt-in, qua SDK portal):**

| Vị trí | Rừng riêng (solo) | Rừng chung (PvP) |
|---|---|---|
| Hoa Lộ ×2 | ✅ 3 lần/ngày | ✅ 3 lần/ngày |
| Đạo Quả khi chết +30% | ✅ 3 lần/ngày | ❌ |
| +5' Mộng Tích | ✅ 1 lần/ngày | ❌ |
| Hồi sinh tại chỗ | ✅ | ❌ |
| Bất kỳ thứ gì cho CT/chỉ số/thời gian | — | ❌ |

3. **Không có:** interstitial trong lúc chơi, loot box trả tiền, VIP, năng lượng, đồng hồ chờ để bán nút skip.
4. **Pass Kỷ Nguyên** [U1], 28 ngày. Free: Hoa Lộ + 2 skin. Premium ~4,99 USD (VN ~49.000đ): 6 skin, hiệu ứng độ kiếp, khung Biên Niên, hoàn đủ Ngọc Tinh nếu hoàn thành. **Không bao giờ có Đạo Quả hay CT.**
5. **Pháp Tướng Độ Kiếp** [U1]: thiên tượng riêng khi Công Kiếp mà cả phòng thấy. **Gói Người Sáng Lập trên Steam** [1.0]: 9,99 USD, chỉ cosmetic.
6. **Mục tiêu:** ≥25% DAU xem rewarded ad. Thấp hơn 35% vì cấm ad sức mạnh ở PvP; đây là đánh đổi đã chấp nhận.

---

## 15. Tech stack — owner: PX *(PX-13b)*
- **TypeScript toàn bộ:** Phaser 3.x hoặc PixiJS v8 (chốt sau spike tuần 1–2) · **Colyseus từ ngày 1** (solo cũng là room local, nên PvP không phải tính năng gắn vào muộn) · sim dùng chung client/server · Vite.
- **Ràng buộc portal (CrazyGames):** gói tải ban đầu ≤50MB, **≤20MB** nếu muốn lên trang chủ mobile. Tổng ≤250MB, ≤1.500 file. Mục tiêu nội bộ: initial ≤20MB, stream asset theo vòng map.
- **Backend:** Postgres managed · snapshot thế giới mỗi 60s · Cloudflare CDN · PostHog (telemetry) + Sentry (crash).
- **Đóng gói:** Capacitor Android [U1] · Tauri cho Steam [1.0] · iOS [Post]. **Thứ tự nền tảng: Web → Android → Steam → iOS.**
- **Art:** AI-gen + chỉnh tay theo style guide khóa ở tuần 2. Thú dùng cutout rig (DragonBones). **Cây procedural** (L-system/shader), vừa rẻ vừa là lợi thế của việc chơi cây. Kiến và côn trùng là swarm VFX. Hiệu năng ≤300 entity động, sim sinh thái theo tile.

---

## 16. Phạm vi & roadmap — owner: PX *(PX-14b + C6-B′)* ⚠️ SCOPE RISK

**Ngân sách:** 12 tháng ≈ 50 tuần lịch. **MVP = 45,75 tuần-người + ~4,25 tuần đệm (~8,5%)**, dưới mức an toàn 14% của PX nên **gắn cờ scope risk**.

### 16.1 MUST: MVP (soft launch Web)
| # | Tính năng | Tuần-người |
|---|---|---|
| 1 | Tiền sản xuất: spike Phaser + Colyseus trên Safari iOS/Chrome Android (300 entity, ≤20MB), style guide, pipeline sim → JSON | 2 |
| 2 | Core engine: world tile 256², camera/zoom, save, sim dùng chung, netcode server-authoritative | 4 |
| 3 | Controller thú chung + **Lang** (3+1, Hang, neo Huyết Noãn) | 2,5 |
| 4 | **Linh Thử** (trữ hạt, đào hang) | 1 |
| 5 | **Linh Mộc** (rễ, Vệt Nắng, gai/độc, Mầm-Neo, Quả Ước, HP 3 lớp, Tán mọc lại) | 3,25 |
| 5b | **Linh Thức lite** | 1,25 |
| 5c | **Kiến lite** (swarm) | 1 |
| 5d | **Hóa Hình Mộng** | 0,25 |
| 6 | Needs 2+2, ngày/đêm, 4 palette mùa (modifier chỉ ở Xuân/Đông), mưa + giông | 1 |
| 7 | AI 4 archetype + Director lite + bot lấp phòng | 2 |
| 7b | **Linh Quỹ / Khô Linh lite** | 0,75 |
| 8 | Tiến hóa: khung 7 cảnh, nội dung C1–C4 (12 tầng), CT, Mộng Tích, 6 Huyết Mạch, 18 skill, Ngộ Đạo draft, tên cảnh giới | 3 |
| 9 | Tiểu Kiếp + Phi Thăng Kiếp I (Ẩn Kiếp, vẫn bị đánh úp được) | 1,5 |
| 10 | Chết: Hậu Duệ + Luân Hồi + Trung Ấm + Đạo Quả Bàn 3 node + Biên Niên + Mộ Linh | 1,75 |
| 11 | Map 256², 3 vòng + Linh Nhãn, 3 palette biome, wayfinding, 3 Mộng Ấn | 2,5 |
| 12 | Bế Quan / Nhập Định / Mộng Báo / catch-up solo | 1,5 |
| 13 | Thiên Đạo Luật (không Thiên Phạt), Ấu Linh, ưu ái loài thiếu | 1,5 |
| 14 | **Rừng chung T2:** lobby theo khu vực, phòng ≤40 CCU, party ≤4, persistence, reconnect, Đại Kiếp 28 ngày, anti-cheat cơ bản, emote, Đạo hiệu, kill-switch, admin | 4 |
| 15 | FTUE "chuột mang hạt" | 1,5 |
| 16 | UI/HUD 2 chế độ điều khiển + accessibility cơ bản | 2,5 |
| 17 | Sự kiện: Đại Linh Triều + Đại Kiếp lite + Linh Tức | 1 |
| 18 | Rewarded ads + shop 6 skin + Hoa Lộ | 1 |
| 19 | Telemetry + crash + dashboard KPI | 0,5 |
| 20 | Âm thanh, lore ~4k từ, VN/EN | 1 |
| | Tích hợp, QA, closed alpha | 3,5 |
| | **Tổng** | **≈45,75** (+~4,25 đệm) |

**Fallback có cổng kiểm tra:**
- **Cổng tuần 16** (hết Vertical Slice): nếu VS tốn hơn 13 tuần, cắt (1) Hóa Hình Mộng, rồi (2) Kiến lite (cộng sinh chỉ còn Quả Ước).
- **Cổng tuần 30** (closed alpha): nếu trễ hơn 2 tuần, cắt (3) Linh Quỹ (đổi thành mật độ tĩnh theo vòng), rồi (4) Linh Thức chỉ giữ do thám.
- **Danh sách cắt tiếp theo:** mùa 4 → 2 · chỉ giữ Đại Linh Triều · map 3 vòng → 2 · shop còn 2 skin · Huyết Mạch 2 → 1 · Linh Thử chỉ còn AI + FTUE (phương án cuối).
- **Không bao giờ cắt:** cây, Linh Thức (ít nhất bản do thám), luân hồi đổi loài, độ kiếp, Rừng chung PvP, Thiên Đạo L1–L3, FTUE.
- Nếu vẫn trượt: **lùi soft launch tối đa 6 tuần**, không ra mắt thiếu PvP.

### 16.2 Vertical Slice (tuần 3–14, kiểm định tuần 14–16)
**Nội dung:** FTUE đầy đủ · Linh Mộc C1–C2 (kèm Linh Thức) · Linh Thử · Lang AI · 1 vòng map · Tiểu Kiếp · luân hồi · Bế Quan solo · **2 client PvP trong cùng một room**.
**Câu hỏi phải trả lời:** (1) ≥70% tester muốn chơi kiếp tiếp sau luân hồi chuột → cây? (2) Cây giữ ≥50% tester chơi ≥10'? Nếu (2) trượt thì dừng 2 tuần làm lại cây, **không cắt cây**.

### 16.3 Lịch
| Giai đoạn | Tuần | Mốc |
|---|---|---|
| Tiền sản xuất | 1–2 | Spike, style guide, benchmark CCU |
| Vertical Slice | 3–14 | Playtest 15–20 người (H1–H3) |
| Alpha | 15–34 | 3 loài, C1–C4, Thiên Đạo, Rừng chung. **Closed alpha PvP người thật trên Discord từ tuần ~30** (100–300 người) |
| Beta | 35–44 | UI/accessibility, ads/shop, telemetry. Open beta itch.io qua 1 chu kỳ 28 ngày |
| Đệm + soft launch | 45–50 | Web: CrazyGames + itch.io + site riêng (Poki nếu được duyệt) |

### 16.4 Sau MVP
- **[U1] "Linh Lâm Khai Môn"** (tháng 13–15, ~11,5 tuần):
  - C5 Bản Thể + Di Căn, Trung Kiếp + Phi Thăng Kiếp II, Công Kiếp/Pháp Tướng
  - Pass Kỷ Nguyên, Android
  - Huyết Nguyệt, biome thứ 2, phòng co-op riêng, Thiên Phạt
  - Kế Hoạch Sinh Trưởng đầy đủ, Đạo Quả Bàn đủ node, Nghiệp Duyên, Tiền Kiếp Ấn
  - Công Đức + Thần Bia lite, Kỷ Nguyên modifier
- **[1.0]** (tháng 16–21, ~24 tuần):
  - Khuẩn (loài thứ 4), Linh Thảo
  - Đạo Đồ chung + nhánh Huyết Mạch thứ 3, Mộc Độn, Ký Hồn Mộc, Trận Pháp
  - Đại Hỏa + Rừng Tro + diễn thế, Đại Hạn, Đại Di Cư, Bào Tử Triều
  - Mộng Cảnh + Lôi Trì
  - Map Linh Lâm 384², tách reset map 28 / nhân vật 56 ngày
  - Steam Early Access
- **[Post]** (chỉ khi KPI 1.0 đạt): Thần Lâm 512², C6–C7, Thiên Kiếp, Thần Vị/Quy Căn · Nhân Hình + Pháp Bảo · Xuất Khiếu thật, Mộng Giới, Lĩnh Vực · Tu Sĩ Nhập Sơn · Lộc, Trùng · iOS · tông môn.
- **[Won't]:** chat/tên tự do · mọi công tắc tắt PvP ở Rừng chung · loot box trả tiền, VIP, năng lượng, mọi thứ P2W · lũ, sương mù · Cửu Cảnh · Vũ Tộc chơi được.

---

## 17. Rủi ro & giả thuyết playtest — owner: PX

### 17.1 Risk Register
| Rủi ro | Khả năng | Tác động | Giảm thiểu |
|---|---|---|---|
| Scope creep (đệm chỉ còn 8,5%) | **Rất cao** | Rất cao | MoSCoW chốt, cổng tuần 16/30, mỗi ý tưởng mới phải ghi rõ thay cái gì |
| PvP người thật bị đẩy lùi | Trung bình | Rất cao (vi phạm brief) | Netcode từ ngày 1, PvP trong VS, closed alpha tuần 30 |
| Cây không vui / quá nhiều thao tác | Cao | Rất cao (USP) | Gate VS cho H3, ≤6 chạm/phút, mở UI dần |
| Người mới bị grief, D1 sụp | Cao | Rất cao | Ấu Linh 3h, Áp Chế, Sát Nghiệp theo cảnh thật, FTUE local |
| Core chạm trần C4 sau ~1,2 tuần rồi hết nội dung dọc | Cao | Trung bình | Luân hồi đổi loài, Huyết Sát bounty, Linh Nhãn, U1 ở tháng 13 |
| Rừng vắng | Cao | Cao | Phòng ≤40, bot Director/Linh Ảnh, gộp phòng khi CCU <8 |
| Lệch loài (ai cũng chọn sói) | Cao | Cao | Ưu ái loài thiếu (+0,25, có aura), Director tăng con mồi |
| Doanh thu ad thấp | Trung bình | Cao | Pass, Pháp Tướng, Founders, server rẻ |
| Cheat trên web | Trung bình | Cao | Server-authoritative, rate-limit |
| Kiệt sức solo dev | Cao | Rất cao | Ops ≤6h/tuần, sự kiện tự động, không chat/tên tự do |
| Bundle mobile >20MB / hiệu năng | Trung bình | Trung bình | Spike tuần 1–2, ≤300 entity, stream asset |
| Art AI thiếu nhất quán | Trung bình | Trung bình | Style guide khóa tuần 2, cây procedural |
| Khán giả nhỏ tuổi + PvP | Trung bình | Trung bình | Không chat/tên tự do, bạo lực stylized |

### 17.2 Giả thuyết playtest
| ID | Giả thuyết | Ngưỡng | Giai đoạn |
|---|---|---|---|
| H1 | Tiền Thân ×3 đưa tới khoảnh khắc lớn đầu tiên | ≥80% đạt Tiểu Kiếp trước phút 8 | VS |
| H2 | "Chuột mang hạt" tạo ham muốn chơi kiếp tiếp | ≥70% bắt đầu kiếp 2 trong 60s | VS |
| H3 | Cây đủ vui (có Linh Thức trong build) | ≥50% chơi cây ≥10' · ≤6 chạm/phút | VS |
| H3b | Linh Thức và Kiến được dùng | ≥50% cây C2+ dùng Linh Thức mỗi phiên · ≥40% nuôi ≥1 tổ kiến | Alpha |
| H4 | Bế Quan xóa nỗi sợ offline | Khảo sát ≤2,5/5 | Alpha |
| H5 | Thiên Đạo Luật giảm bắt nạt | ≤10% kill PvP có g≥2 | Alpha |
| H6 | Mộng Báo kéo người chơi quay lại | D1 +5 điểm % (A/B) | Beta |
| H7 | Cân bằng loài tự nhiên | Không loài nào >40% dân số suốt 7 ngày | Alpha |
| H8 | Đổi loài vẫn hấp dẫn khi có Hậu Duệ | ≥35% số lần chết chọn Luân Hồi | Alpha |
| H9 | Chi phí cái chết chịu được | ≥60% quay lại trong 72h sau chết PvP ở C≥3 | Alpha/Beta |
| H10 | Ngân sách UI đủ | Bấm nhầm <5% | VS/Beta |
| H11 | Lựa chọn cách chết trong FTUE có nghĩa | Phân bố A/B 35–65% | VS |
| H12 | P2 không bị khóa khỏi sói | ≥70% P2 dùng vé Tự Quy hoặc chơi sói trước phút 40 | Beta |
| H13 | Khô Linh đọc được | ≥60% người làm vùng Khô Linh hiểu nguyên nhân (khảo sát) | Alpha |

**KPI go/no-go cho U1:** D1 ≥25% (portal) / ≥30% (organic) · D7 ≥8% · D30 ≥3% · session ≥14' · ≥1,8 phiên/DAU · ad ≥25% DAU · crash <1% · CCU đỉnh/phòng ≥12. **Gate 1.0:** D30 ≥4% và doanh thu ≥2× chi phí vận hành trong 2 chu kỳ liên tiếp.
**Telemetry bắt buộc:** time-to-first-breakthrough, phút bỏ game trong FTUE, lựa chọn A/B ở FTUE, nguyên nhân chết (AI/PvP, g thật), Hậu Duệ hay Luân Hồi, loài được chọn khi luân hồi, thời lượng offline và tổn thất, phân bố Nghiệp, số chạm/phút của cây, tỉ trọng nguồn CT, lượt dùng Linh Thức và Kiến, ad view theo vị trí, CCU theo phòng, thời gian vùng ở trạng thái Khô Linh.

---

## 18. Glossary rút gọn — owner: WORLD *(WORLD-18, C2)*
| Thuật ngữ | Nghĩa |
|---|---|
| **Mộng Hỏa** | Người chơi: tia mộng của Kiến Mộc |
| **CT (Chu Thiên)** / **Tu Vi** | Đơn vị kế toán (1 phút chơi tích cực) / thanh tiến độ cảnh giới |
| **Linh Khí** | Ví trong kiếp (skill, khiên, Đả Tọa) và dòng sống chảy trong rừng |
| **Linh Quỹ / Khô Linh** | Quỹ linh khí của vùng / vùng cạn (<30%) |
| **Sinh Năng** | Năng lượng của xác = 20 CT, chia 8 / 4 / 8 |
| **Đạo Quả** | **Tiền meta** giữ qua luân hồi (25% CT lũy kế). Flavor: *"Đạo Quả kết từ đạo tâm"* |
| **Đạo Quả Bàn** | Cây meta chỉ có mở khóa ngang |
| **Tâm Hướng** | **La bàn hành vi** 2 trục: Sinh↔Sát, Hợp↔Độc |
| **Thiên Đạo Gia Trì** | Tổng các bonus CT, trần ×3 |
| **Hồi Ức** | Hệ số catch-up sau chết, nằm ngoài trần Gia Trì |
| **Mộng Tích** | Hồ rested: ×2 CT trong 30' đầu phiên |
| **Áp Chế** / **Phân Thân** | Level-sync theo vùng / tên UI của người cấp cao đang bị nén |
| **Huyết Mạch** / **Ấn** | Nhánh tiến hóa ở C3 / bộ đếm learn-by-doing |
| **Ngộ Đạo** / **Keystone** / **Túc Tuệ** | Draft chọn 1 trong 3 / node đỉnh / Notable mang sang kiếp sau |
| **Thần Thông** / **Thần Thức** | Kỹ năng tối thượng / tầm cảm nhận |
| **Tiểu Kiếp · Phi Thăng Kiếp I · Trung Kiếp · Phi Thăng Kiếp II · Thiên Kiếp** | Các kiếp đột phá C1→2, C2→3 / C3→4 / C4→5 / C5→6 / C6→7 |
| **Đại Kiếp** | **Chỉ** dùng cho sự kiện reset cuối chu kỳ (56 ngày; MVP 28) |
| **Kỷ Nguyên** | Chu kỳ 28 ngày (map, Pass) |
| **Ẩn Kiếp / Công Kiếp** · **Hộ Pháp** · **Tâm Ma** · **Đạo Cơ Tổn** | Kiếp riêng tư / công khai · bảo vệ người độ kiếp · bản sao của chính mình trong kiếp · debuff 20' khi thất bại |
| **Phi Thăng** | **Chỉ** dùng cho chuyển cấp rừng. MVP: Phá Giới qua Giới Bia |
| **Hậu Duệ** / **Neo** / **Luân Hồi** / **Trung Ấm** | Tầng chết 1 / Mầm-Neo, Huyết Noãn, Ổ Hạt / tầng chết 2 / màn chuyển tiếp |
| **Hồn Hộ** | Bảo vệ 10' sau khi sống lại |
| **Thiên Đạo Luật** · **Sát Nghiệp** · **Huyết Sát** · **Thiên Phạt** · **Nghịch Thiên** · **Oán Linh** · **Ấu Linh** · **Bất Nhân** · **Thoát Sinh** | Hệ chống bắt nạt · đơn vị nghiệp · bounty từ ≥3 Nghiệp · sét đuổi từ ≥5 Nghiệp · thưởng khi hạ kẻ cao cảnh hơn · đền bù cho nạn nhân · khiên người mới · dấu 5' cho kẻ đánh Ấu Linh · thưởng khi con mồi thoát |
| **Bế Quan** / **Nhập Định** / **Đả Tọa** / **Mộng Báo** | Thoát an toàn / cửa sổ 30–60s khi thoát sai chỗ / luyện linh khí → CT / tóm tắt khi quay lại |
| **Tán / Thân / Tâm Rễ / Đổ / Mộc Tàn / Căn Thương** | 3 lớp HP của cây / bị hạ (chưa chết) / trạng thái yếu sau khi Đổ / đòn duy nhất trừ được Tâm Rễ |
| **Vệt Nắng · Quả Ước · Linh Thức · Hóa Hình Mộng** | Cửa sổ bonus quang hợp · hợp đồng ăn quả mang hạt · phóng hồn do thám · Bản Thể tạm thời trong Linh Triều |
| **Hạ Lâm / Linh Lâm / Thần Lâm** | Rừng Non / Nguyên Sinh / Cổ Đại |
| **Bìa Rừng / Trung Lâm / Thâm Lâm / Linh Nhãn** | Các vòng từ ngoài vào trong |
| **Công Đức · Thần Cách · Thần Vị · Quy Căn · Thần Bia** | Điểm "đã nuôi rừng" · điều kiện Thiên Kiếp · 5 ghế thần · trở về gốc · bia khắc tên |
| **Ý Chí Rừng** / **Linh Ảnh** | Director / bot (dư ảnh Mộng Hỏa) |

**Bị loại:** Đạo Tâm (thuật ngữ hệ thống), Đạo Tâm Bàn, Hộ Thể, Linh Quang Hộ Thể, Nghiệp Lực, Thiên Phạt Lấn Yếu, Hồn Thoát, Trùng Tu, Mộng Ảnh, Linh giới, Cửu Cảnh, Tụ Linh (tên cảnh), Xuất Khiếu (tên cảnh), "Đại Kiếp" khi dùng cho đột phá.

---

## 19. Decision Log

| # | Quyết định | Phương án bị loại | Ai ủng hộ / phản đối | Lý do |
|---|---|---|---|---|
| D1 | **7 cảnh giới, ánh xạ 3/2/2**, khung Khai Linh · Luyện Khí · Trúc Cơ · Kết Đan · Hóa Hình · Nguyên Anh · Thành Thần (C1 phương án A′) | 9 cảnh (Cửu Cảnh); khung Tụ Linh/Xuất Khiếu; 4 tầng ở C5–C6 | 4/4 ở R4. WORLD đổi từ 9 sang 7 sau khi PROG rút sim; PROG từng đổi 7 → 9 → 7 | C7–C8 của Cửu Cảnh không có khả năng mới về chất; 9 cảnh tốn thêm ~29% chi phí theo cảnh; đường cong v2 cho 78% Mid chạm Thiên Kiếp trong 56 ngày; "Nguyên Anh" tránh trùng với kỹ năng Xuất Khiếu |
| D2 | **Đạo Quả = tiền meta, Tâm Hướng = la bàn**, kiếp đột phá Tiểu / Phi Thăng I / Trung / Phi Thăng II / Thiên, "Đại Kiếp" chỉ cho reset, **Ấu Linh** (C2-C) | A (Đạo Tâm = la bàn), B (Đạo Tâm = tiền) | C: WORLD (owner ×1,5) + SURV = 2,5 · B: PX = 1 · A: PROG = 1 | Loại hẳn "Đạo Tâm" khỏi thuật ngữ hệ thống để hết nhầm nghĩa. "Đạo Quả" khớp P3 |
| D3 | **Ngày 20' · mùa 42h · năm 7 ngày · Kỷ Nguyên 28 · Đại Kiếp 56 (MVP 28)** (C3-A) | Mùa 48h / năm 8 ngày; ngày 24' | 4/4. SURV đổi lập trường | Năm-rừng = 1 tuần thực nên mỗi tuần có đủ sự kiện; 56 = 2 × 28 khớp Pass; giờ mùa trôi phủ mọi múi giờ |
| D4 | **Hậu Duệ về Sơ kỳ đại cảnh, trần 130 CT, Hồi Ức ×1,5; Luân Hồi ×4/×2; Oán Linh +25%; Hồi Ức nằm ngoài trần Gia Trì** (C4-C + sửa của PROG) | A (về đầu tầng), B (×3/×1,5) | 4/4. PROG nhượng "đầu tầng", SURV nhượng ×3/×1,5 | Phương án duy nhất đạt trần PX ở mọi cảnh (Hậu Duệ 0,83–1,16 phiên); khớp lore "dòng dõi" |
| D5 | **Ấu Linh 3h hoặc hết C2, cái nào đến trước**, mất khiên khi chủ động tấn công, báo trước 10' (C5-B) | 60' (A); "và" (C) | 4/4. PROG nhượng PX | C cho phép tài khoản phụ đứng mãi ở C2 để giữ khiên và tàng hình |
| D6 | **MVP thêm Linh Quỹ lite + Linh Thức lite + Kiến lite + Hóa Hình Mộng**, bù bằng cắt Kế Hoạch Sinh Trưởng, giảm modifier mùa, Đạo Quả Bàn còn 3 node (C6-B′) ⚠️ scope risk | A (giữ 44+6), C (+Huyết Nguyệt, Mộ Linh…, lùi 3 tuần), D (không có Kiến) | B/B′: PX (owner ×1,5) + SURV = 2,5 · D/D′: WORLD + PROG = 2 | Brief yêu cầu cứng cả 4 cách chơi thực vật; MVP phải kiểm chứng đúng USP. Fallback về D ở cổng tuần 16 |
| D7 | **Offline = 0 CT**, chỉ có Mộng Tích; thân bất tử và miễn needs/sự kiện khi Bế Quan | Offline 60% (PX R1) | Blocker của SURV và PROG ở R2, PX chấp nhận | 288 CT/đêm > cả tuần chơi của Mid, game sẽ thành idle |
| D8 | **HP cây 3 lớp, Đổ ≥40s, Tâm Rễ chỉ nhận Căn Thương** | TTK 4–6s (PROG R1) | Blocker của SURV ở R2, PROG chấp nhận và sim lại | PvP tự do + cây bất động chỉ chạy được khi cây có thời gian phản ứng |
| D9 | **Thiên Đạo Luật hợp nhất, g theo cảnh thật** | 3 hệ riêng (Sát Nghiệp / Nghiệp Lực / Thiên Phạt Lấn Yếu); g tính sau Áp Chế | Hội tụ ở R2–R3 (4/4) | Tính sau Áp Chế để hở đúng chỗ người mới đông nhất |
| D10 | **Thần Cách = Công Đức, không phải số kill**; Thần Bia không có bảng kill | Lên thần bằng hạ Cổ Thú (PROG R1) | WORLD audit ở R2, PROG chấp nhận | Nếu không, kẻ ăn nhiều nhất thành thần, ngược với theme |
| D11 | **Đại Kiếp theo lịch cố định** | Kích hoạt khi đủ ghế Thần Vị (WORLD R1) | Blocker của PROG, WORLD chấp nhận | Core có thể kích hoạt reset khi Mid còn ở C5 |
| D12 | **FTUE "chuột mang hạt"**, người chơi chọn cách chết | Thú nhỏ chết theo script (PX R1); bắt đầu bằng cây | WORLD + SURV + PX | Cây là cao trào của FTUE chứ không phải giải an ủi; chết theo script là bất công |
| D13 | **Ngộ Đạo draft thay cho đồ thị skill tree**; MVP 3 loài / 6 Huyết Mạch / 18 skill | 33 skill, 7 lớp hệ thống (PROG R1) | PX phản biện, PROG tự cắt sâu hơn đề xuất | Đọc hiểu trong 30s, UI rẻ, vừa ngân sách ≤5 nút |
| D14 | **Ad ở Rừng chung = 0 CT**; skin không ngụy trang; Pass không có Đạo Quả/CT | Ad +% CT, ad tăng thời gian bế quan | 4/4 | Mọi % tu vi mua được bằng ad trong PvP đều là P2W |
| D15 | **Không chat tự do, không tên tự do** | Chat mở | PX | 1 người không moderate nổi; khán giả portal nhỏ tuổi |
| D16 | **Minh Ước bị cắt** | Cờ tắt PvP trong sự kiện | WORLD tự cắt | Trái brief "luôn PvP tự do" |
| D17 | **Vòng lõi MVP tên Thâm Lâm** [orch] | "Linh Lâm vòng lõi" | WORLD owner tên | "Linh Lâm" là tên của cấp rừng 2 |
| D18 | **Vệt Nắng theo SURV** (8s/50s ×2,5, báo trước 2s) · Khô Linh 2h · Thiên Phạt ở 5 Nghiệp · Linh Thử chơi được | — | Orchestrator chốt theo owner; không ai phản đối ở R4 | — |
| D19 | **Thiên Kiếp luôn Công, bị giết là chết thật** [Post], kèm các điều kiện bắt buộc: người chơi tự chọn thời điểm khởi kiếp; mây báo trước ≥60s, thấy trong 30 ô, cảnh báo toàn phòng; có slot Hộ Pháp; kẻ giết người độ kiếp nhận Sát Nghiệp; Luân Hồi từ C6 lấy lại cảnh cũ ≤1,5 tuần Mid | Thiên Kiếp có Ẩn | PROG giữ. SURV và PX dissent nhẹ có điều kiện | Đỉnh "hùng tráng + tàn khốc" của brief |

---

## 20. Dissent & Câu hỏi mở

### 20.1 Dissent ghi nhận
- **PX (D2):** brief viết "giữ một phần linh hồn/**đạo tâm** (meta-progression)", nên PX muốn tiền meta tên là Đạo Tâm. Team giữ Đạo Quả, và đặt câu flavor *"Đạo Quả kết từ đạo tâm"* để giữ chữ của brief. **Người dùng chốt** (Q1).
- **SURV (D6):** muốn mùa 4 → 2 (Sinh/Tàn, 84h) thay cho "4 palette, chỉ Xuân/Đông có modifier". PX (owner scope) chọn cách sau để giữ lịch của D3.
- **WORLD + PROG (D6):** chọn D (không có Kiến) vì lo đệm. Đã có fallback về D ở cổng tuần 16.
- **SURV, PX (D19):** dissent nhẹ có điều kiện. Thiếu điều kiện nào thì phải sửa thiết kế trước khi làm Thiên Kiếp.

### 20.2 Câu hỏi mở cho người dùng
| # | Câu hỏi | Mặc định của team |
|---|---|---|
| Q1 | Tên tiền meta: **Đạo Quả** hay **Đạo Tâm**? | Đạo Quả |
| Q2 | Chấp nhận MVP đệm chỉ ~8,5% (đủ 4/4 cách chơi thực vật), hay giữ đệm 14% và để Kiến/Hóa Hình Mộng sang U1? | Chấp nhận, có cổng tuần 16 |
| Q3 | Thiên Kiếp thất bại vì sét: −50% CT tầng Hậu (PROG) hay rơi 1 tầng (SURV)? | Chốt khi làm [Post] |
| Q4 | Nhân vật tạo trong 7 ngày cuối chu kỳ có được miễn reset không (WORLD đề xuất)? | Chưa chốt, PX quyết ở beta |
| Q5 | Slot phòng thủ 2 của cây: **Độc Tiết** hay **Cầu Viện Hương** (gọi thiên địch, tạo hợp tác cây–sói)? | Độc Tiết ở MVP, A/B ở alpha |
| Q6 | Portal ra mắt: CrazyGames + itch.io, hay muốn thử Poki/Google Play sớm hơn? | CrazyGames + itch.io |
| Q7 | Làm full-time hay part-time? Lịch 50 tuần giả định full-time | Full-time |

---

## Phụ lục: tài liệu nguồn trong session
- `00-brief.md`: brief và ràng buộc cứng của người dùng
- `r1-proposal-*.md` → `r2-critique-*.md` → `r3-revision-*.md` → `r4-conflicts.md` → `r4-position-*.md` → `r6-signoff-*.md`
- `sim/`: mô phỏng của PROG (`prog_sim.py`, `prog_r2_sim.py`, `prog_r3_sim.py`, `prog_r4_c4_sim.py` và output)
