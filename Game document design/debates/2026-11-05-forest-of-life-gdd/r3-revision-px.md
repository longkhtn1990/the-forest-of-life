# R3 Revision — PX

> Domain: persona, USP và thị trường, FTUE, UI/UX đa nền tảng, accessibility, server, offline/Bế Quan, kinh tế, monetization, retention/live-ops, tech stack, **scope/MVP/roadmap (bản chốt)**, rủi ro, playtest/KPI.
> Đơn vị: **CT** = tu vi chuẩn của 1 phút chơi tích cực (PROG-03). **Mid** = 5 phiên × 40'/tuần ≈ 320 CT/tuần ≈ 64 CT/phiên. **Casual** ≈ 130 CT/tuần. Chi phí tính bằng **tuần-người** (1 người full-time + AI hỗ trợ code/art/test).
> Tên gọi theo glossary của WORLD (R2 #5): **Bế Quan** = thoát an toàn · **Nhập Định** = trạng thái dễ bị tấn công khi thoát sai chỗ · **Mộng Tích** = hồ rested · **Đạo Tâm** = tiền meta · **Tâm Hướng** = la bàn hành vi · **Phi Thăng** = chuyển cấp rừng · **Thành Thần / Quy Căn** = endgame.

---

## Phản hồi phản biện

| Phản biện (từ ai, ID) | Quyết định | Lý do | Thay đổi cụ thể |
|---|---|---|---|
| SURV PX-04 **Blocker**: offline 60% × 8h = 288 CT/đêm, gần bằng 320 CT của cả tuần chơi | **Accept** | Số của SURV đúng, và sim H của PROG xác nhận: CT/tuần ×7,3, chạm Thiên Kiếp sau 0,7 tuần. Game biến thành idle. | **PX-04b: offline = 0 CT.** Chỉ nạp Mộng Tích (PROG-04). Cây tích Quang Tinh và làm Kế Hoạch Sinh Trưởng (SURV) |
| PROG PX-04/12 **Blocker**: offline 60% + ad +2h bế quan = ×8,9 | **Accept** | Như trên. Ad tăng thời gian bế quan là P2W bằng thời gian xem quảng cáo | Bỏ ad bế quan ở mọi chế độ |
| PROG: ad "+5' Mộng Tích, 1/ngày" (~+8% CT) | **Partial** | Ở solo thì được. Ở Rừng chung thì +8% CT nhờ xem ad vẫn là lợi thế PvP mua bằng ad | Rừng chung: ad = **0 CT**. Solo: +5' Mộng Tích 1/ngày |
| SURV PX-04 Major: tự vệ offline cho EXP (farm bằng tài khoản phụ); trần 25% "mỗi lần offline" bị cộng dồn | **Accept** | Lỗ hổng thật | Sát thương thụ động khi offline chỉ cho **Dưỡng Chất**. Trần tổn thất tính **theo 24h thực** |
| SURV PX-05 Major: khiên 45' gồm cả FTUE; +1 Nghiệp khi chênh 1 cảnh phạt chính chuỗi thức ăn | **Accept** | Sói C3 ăn hươu C2 là bản năng, không phải bắt nạt | Theo Thiên Đạo Luật hợp nhất (PX-05b) |
| PROG PX-05 Major: khiên hết ngay trong FTUE | **Accept** | Đúng. Với khiên cũ, người chơi vào Rừng chung với 0 phút bảo vệ | Ấu Linh: **3h trong Rừng chung hoặc tới hết C2** |
| SURV PX-08 Major: cái chết bị script ép là bất công | **Accept** | Đây là bài học sai đầu tiên game dạy người chơi | Thọ Nguyên (SURV) + chọn cách chết (PX-08b) |
| WORLD PX-08 Major: cây chỉ là giải an ủi; rừng "bất công" chứ không "tuần hoàn" | **Accept** | Ý của WORLD tốt hơn bản của tôi. Nó giữ chuột (vui trong 30s đầu) và biến cái chết thành bài học theme | FTUE "chuột mang hạt → cây mọc từ xác" (PX-08b) |
| SURV PX-09 Major: reset 14/28 ngày khiến không ai thành thần được | **Accept** | Sim I của PROG: kỷ nguyên 28 ngày thì 0% Mid chạm Thiên Kiếp | Tách reset bản đồ và reset nhân vật (từ bản 1.0). MVP chưa có Thiên Kiếp nên dùng 1 loại reset 28 ngày (PX-09b) |
| PROG PX-09 Major: chu kỳ phải 48 ngày | **Partial** | Đồng ý chu kỳ nhân vật ≥48 ngày. Tôi chọn **56 ngày = 2 Kỷ Nguyên × 28** để khớp nhịp tuần và pass 28 ngày | Bản 1.0: map 28 ngày / nhân vật 56 ngày |
| PROG Q2: pass 24 ngày? | **Reject** | Chu kỳ 24 ngày trôi so với ngày trong tuần, nên sự kiện cuối tuần và hạn pass rơi vào thứ khác nhau mỗi kỳ. Người chơi tính "tháng" dễ hơn | Pass **28 ngày**, 2 pass/Đại Kiếp |
| WORLD PX-09/15: Rừng Non 14 ngày | **Reject (phần 14 ngày)** | Casual cần ~3 tuần mới tới C4 (đã có Bù Đắp). 14 ngày nghĩa là Casual bị wipe trước cột mốc đầu tiên. Thêm vào đó, 1 người không làm kịp nội dung cho chu kỳ 14 ngày | Rừng Non cũng **28 ngày**. Lore "lịch lồng nhau" của WORLD giữ nguyên ở cấp Nguyên Sinh/Cổ Đại |
| PROG PX-14 Major: MVP chỉ ~1 tuần tiến trình dọc | **Accept** | Đúng | Thêm vòng lõi **Linh Lâm** (C4, không Áp Chế). Trung Kiếp C3→C4 là Phi Thăng đầu tiên |
| PROG PX-10 Major: "Linh khí dồi dào ×1,5" trùng Tĩnh Tu | **Accept** | Đã tự sửa ở R2 | Chỉ còn **một hồ: Mộng Tích** |
| PROG PX-12 Minor: tu vi không phải ví; trùng tên Đạo Tâm | **Accept / Partial** | Tu vi là thanh tiến độ. WORLD đã đổi la bàn thành Tâm Hướng nên "Đạo Tâm" được giữ cho tiền meta | Ví gồm: Linh Khí, Đạo Tâm, Hoa Lộ, Ngọc Tinh (PX-12b) |
| PROG PX-10 Minor: 25–35h tới phi thăng → 17h | **Accept** | Đây là điều kiện để Mid về đích trong chu kỳ | Tổng ≈1.671 CT (số PROG), áp lên khung 7 cảnh |
| WORLD PX-07 Major: "Phi Thăng" dùng cho 2 nghĩa | **Accept** | Glossary | Phi Thăng = chuyển cấp rừng. Thành Thần = ở lại thế giới như một vùng sống, cuối chu kỳ thì Quy Căn |
| WORLD PX-04 Minor: 1 luật, 1 tên | **Accept** | — | "Nhập Định". SURV chốt số |
| WORLD PX-01 Minor: hook "ngọn cỏ" mà MVP không có cỏ | **Accept** | Marketing không được hứa thứ chưa có | Hook mới (PX-02b) |
| SURV Q2: Linh Thử chơi được sau FTUE? | **Trả lời: có** | Cần một loài ăn cỏ *do người chơi điều khiển* để chuỗi thức ăn giữa người chơi đủ 3 bậc (ràng buộc cứng của brief) | MVP = 3 loài chơi được: Linh Mộc, Linh Thử, Huyết Lang. Lộc chỉ là AI |
| SURV Q3: Nhập Định 30s khi mất mạng có công bằng? | **Partial** | 30s ổn nếu thân không đứng giữa đồng | **PX-18:** khi Nhập Định, thú tự "ẩn bản năng" vào bụi/hang gần nhất trong ≤5 ô |
| WORLD Q1: Mộc Độn & Ký Hồn Mộc vào Should? | **Partial** | Ký Hồn Mộc rẻ, là neo co-op nên vào 1.0. Mộc Độn phá trục áp lực khoảng cách của SURV, chỉ vào 1.0 kèm ràng buộc của SURV | Xem MoSCoW |
| WORLD Q2: Tiền Kiếp Ấn làm giảm giá trị skin? | **Reject lo ngại** | Ấn (kiếm được) và skin (mua) là hai trục khác nhau. Ấn tạo nhu cầu "phối" skin đẹp với Ấn | Luật render: skin không được che Ấn |
| PROG đổi sang 9 cảnh giới | **Reject** (có điều kiện đổi ý) | Xem mục "Lập trường giữ vững" #1 | Giữ 7. Quyết định này **không chặn MVP** vì C1–C4 giống nhau ở cả hai phương án |

---

## Đề xuất đã sửa

Các ID giữ nguyên: **PX-03** (bảng mâu thuẫn, chỉ cập nhật trạng thái gỡ ở PX-03b) và **PX-13** (lõi tech, chỉ bổ sung ở PX-13b). Mọi mục khác dưới đây là bản viết lại đầy đủ để orchestrator tổng hợp GDD.

### PX-01b: Persona mục tiêu và bản đồ hệ thống → persona

| Persona | Nền tảng | Session | Động lực (Quantic Foundry) | Cần | Sợ |
|---|---|---|---|---|---|
| **P1 "Đạo hữu xe buýt"**, 18–30t, đọc tiên hiệp, từng chơi game tu tiên idle | Mobile web → Android | 10–20', 2–3 lần/ngày | Completion, Power, Fantasy | Đột phá đều đặn, thấy thứ gì đó lớn lên khi offline, tên cảnh giới đậm chất | Mất công sức vì một pha gank |
| **P2 "Kẻ săn mồi"**, 16–28t, fan The Isle / Path of Titans / mope.io | PC web → Steam | 45–90' | Competition, Excitement, Destruction | Săn người thật, adrenaline của chuỗi thức ăn | Lớn chậm, bị khóa khỏi loài săn mồi |
| **P3 "Người làm vườn"**, 20–40t, thích cozy/strategy/Don't Starve | PC/Mobile | 20–40' | Design, Strategy, Discovery | Lan rễ, cộng sinh, thấy rừng đổi vì mình | Thao tác twitch, phải chạm liên tục |

| Hệ thống | P1 | P2 | P3 |
|---|---|---|---|
| Linh Mộc (Thần Thức, Kế Hoạch Sinh Trưởng) | ●● | ○ | ●●● |
| Huyết Lang (săn, Huyết Sát bounty) | ● | ●●● | ○ |
| Linh Thử (ăn, trữ hạt, chạy trốn) | ●● | ● | ● |
| Độ kiếp, tên cảnh giới | ●●● | ●● | ● |
| Luân hồi đổi loài, Biên niên | ●● | ●● | ●● |
| Mộng Báo, Mộng Tích | ●●● | ○ | ●● |
| Thiên Đạo Luật (Ấu Linh, Sát Nghiệp) | ●●● (được bảo vệ) | ●● (bounty) | ●● |

**Quy tắc:** mọi tính năng mới trong GDD phải ghi persona chính. Tính năng không phục vụ ít nhất 1 persona ở mức ●● thì xuống Could.

### PX-02b: USP, hook, đối thủ

- **USP (1 câu):** *Game sinh tồn tu tiên PvP đầu tiên mà bạn có thể là bất kỳ sinh mệnh nào trong rừng (chuột, sói hay cổ thụ). Mỗi lần chết là một lần luân hồi sang kiếp khác, và xác bạn nuôi chính khu rừng.*
- **Hook trailer (WORLD sửa):** *"Kiếp này em là con chuột mang hạt. Kiếp sau em là cổ thụ mọc lên từ xác chính mình."*
- **Tagline store (ngắn, dùng cho thumbnail portal):** *"Sống. Bị ăn. Mọc lại thành rừng."* (EN: *Live. Be eaten. Grow back as the forest.*)

| Đối thủ | Học | Khán giả phàn nàn | Bài học |
|---|---|---|---|
| The Isle / Path of Titans / Beasts of Bermuda | Nỗi sợ thật, PvP chuỗi thức ăn | Lớn 4–6h, KOS, người mới bị ăn ngay, map vắng trên mobile | Lớn nhanh và có nghĩa. Chết phải có thưởng. Mật độ sự kiện cao |
| mope.io / evowars | Vào game 5 giây, tiến hóa mỗi 1–2 phút | Không có meta, thể loại đã bão hòa | Chỉ mượn nhịp đầu game, không định vị là game .io |
| Game tu tiên idle/MMO (Trung Quốc) | Cảm giác đột phá, tên cảnh giới | P2W, VIP, dark pattern | Giữ đột phá, bỏ P2W |
| Tale of Immortal / Amazing Cultivation Simulator | Sandbox tu tiên trên PC đã chứng minh có thị trường | Grind, UI rối, dịch kém | Tiên hiệp bán được trên Steam, nhưng UI phải gọn |
| Game sinh tồn làm cây (Grow The Seed 2025, các run-based plant survival 2026, Tree Simulator) | Có cầu cho fantasy "làm cây" | Toàn bộ là single-player hoặc meme | **Khoảng trống:** chưa thấy game nào cho chơi cây trong PvP nhiều người chơi, có luân hồi giữa các loài (search 11/2026, kết quả không xác nhận multiplayer cho game cây nào) |
| Don't Starve / Rain World | Thế giới thù địch đẹp | Khó vào | 5 phút đầu phải vui |

### PX-03b: Trạng thái các mâu thuẫn trong brief
| # | Mâu thuẫn | Đã gỡ bằng |
|---|---|---|
| M1 | PvP tự do + cây bất động | HP 3 lớp, Tâm Rễ không chạm được bằng đòn thường, cây Đổ ≥40s (SURV-03, PROG-11b). Thân bất tử khi Bế Quan (PX-04b) |
| M2 | Session 15' + nhiều tuần + PvP | Trần chi phí cái chết (PX-06b), Thiên Đạo Luật (PX-05b) |
| M3 | Thành thần + server lâu dài | Thành Thần rời chuỗi thức ăn, Quy Căn cuối chu kỳ (WORLD), reset theo Kỷ Nguyên |
| M4 | Ads + server + 3 nền tảng + 1 người | Web trước, TS 1 codebase, phòng nhỏ, chế độ ngủ (PX-09b, PX-13b) |
| M5 | Rừng khổng lồ + 2D + 1 người | Cảm giác khổng lồ đến từ camera, scale và vòng khóa, không từ diện tích (giữ A4) |

### PX-04b: Bế Quan, bộ luật offline hợp nhất (thay toàn bộ PX-04)
Gộp SURV X3, PROG-04 và WORLD #3. SURV chốt các con số sinh tồn, PROG chốt số CT.

1. **Thoát game:** trong lãnh thổ hoặc Hang thì **Bế Quan ngay**. Ngoài đó phải qua **Nhập Định 30s**, hoặc **60s** nếu đã gây/nhận sát thương trong 30s gần nhất. Kết nối lại trong thời gian Nhập Định thì chơi tiếp bình thường. **PX-18 (mới):** trong lúc Nhập Định, thú tự chạy vào bụi/hang gần nhất trong ≤5 ô (AI "ẩn bản năng", chi phí S). Mất sóng trên xe buýt không còn là án tử.
2. **Khi Bế Quan:** thân **bất tử**, **miễn decay needs và mọi sự kiện môi trường** (Đại Hạn không giết được cây đang ngủ).
3. **Tu vi offline = 0 CT.** Offline chỉ nạp **Mộng Tích**: đầy sau 8h, cho **×2 CT trong 30' chơi kế tiếp** (số PROG-04, đã nằm trong đường cong Mid). Đây là bonus hằng ngày duy nhất. "Linh khí dồi dào" bị bỏ.
4. **Cây khi offline:** quang hợp 25% vào **Quang Tinh** (vật liệu, kho trần 150), không vào CT. **Kế Hoạch Sinh Trưởng** (SURV): trước khi thoát, người chơi đặt tối đa 3 ô rễ, mọc lại Tán, chín quả, trả bằng Quang Tinh. Kế hoạch được thực hiện khi offline.
5. **Tổn thất khi offline có trần, tính theo 24h thực:** ≤20% Tán, ≤25% ô rễ ngoài (không tính các ô trong bán kính 2 quanh Tâm Rễ), kho Hang bị cướp ≤50%. Tự vệ thụ động vẫn chạy nhưng chỉ cho **Dưỡng Chất**.
6. **Chống giữ đất ảo:** offline >48h thì rễ teo 1 ô/ngày.
7. **Mộng Báo ≤10s khi quay lại:** "Rễ mọc thêm 3 ô · 2 quả chín · [Hắc Lang] gặm 14% Tán, trúng độc bỏ chạy · Mộng Tích 100% · Đại Linh Triều sau 6h". **Không hiện số tu vi offline** vì nó bằng 0. Thứ người chơi thấy là *tăng trưởng nhìn được*.
8. **Solo:** catch-up mô phỏng tối đa 8h khi mở lại, cùng luật như trên.

> Kiểm tra lại câu hỏi của SURV: người chơi cây log in 2', log out, lặp mỗi ngày thì được bao nhiêu? Được 0 CT offline, 30' Mộng Tích chỉ dùng được nếu *chơi* 30'. Kế Hoạch Sinh Trưởng tốn Quang Tinh, mà Quang Tinh lại cần Vệt Nắng khi online. Không còn vòng idle.

### PX-05b: PvP tự do, Thiên Đạo Luật (PX nhận bản hợp nhất SURV X4 + PROG-12b)
Không có công tắc PvP ở Rừng chung. Lập trường PX là các ràng buộc UX sau, số liệu do PROG/SURV chốt:
- **L1 Ấu Linh** (người mới): 3h trong Rừng chung hoặc tới hết C2. Sát thương nhận từ người cao hơn ≥2 cảnh bị giảm 60%. Người chơi cao hơn không thấy Ấu Linh bằng Thần Thức. Mất khiên nếu chủ động tấn công người chơi khác.
- **L2 Áp Chế** ở Bìa Rừng và Trung Lâm (trần C3 Hậu) + CT ×0.5^chênh. **Bỏ** −HP/phút của tôi và cơ chế thất thoát của SURV.
- **L3 Sát Nghiệp:** g tính theo **cảnh giới thật**. g=1: 0 Nghiệp. g≥2: thưởng ≈0, +1 Nghiệp (+2 nếu nạn nhân là Ấu Linh). Từ 1 Nghiệp: aura đỏ, kiếp +10%/Nghiệp. Từ 3 Nghiệp: **Huyết Sát** hiện trên map, ai hạ được nhận thưởng ×3. Thiên Phạt từ 5 Nghiệp vào bản U1. Giảm 1 Nghiệp/2h chơi online. Đánh trả kẻ tấn công trước thì không tính.
- **L4 Đền bù:** Thoát Sinh +2 CT. Oán Linh +25% Đạo Tâm, 1 lần/24h, mỗi cặp chỉ tính 1 lần/24h.
- **UX bắt buộc:** vòng cảnh giới dưới chân dùng **màu + hình** (▲ cao hơn / ● ngang / ▼ thấp hơn). Aura Tâm Hướng chỉ hiện khi soi bằng Thần Thức, để mỗi lúc chỉ có 1 vòng dưới chân.

### PX-06b: Trần chi phí cái chết (ràng buộc retention; PROG chốt công thức)
- **Hậu Duệ** (neo còn sống, 1 lần/24h, neo phá được): rơi về **Sơ kỳ của đại cảnh hiện tại** (WORLD), giữ Huyết Mạch và lãnh thổ, cày lại ×1,5 tới đỉnh cũ (PROG), không nhận Đạo Tâm. **Trần PX:** trung bình ≤1,5 phiên Mid, tệ nhất ≤3 phiên.
- **Luân Hồi** (đổi loài, mất neo, hoặc chết lần 2 trong 24h): Đạo Tâm = 25% CT lũy kế (+10% nếu chết trong kiếp), Tiền Kiếp catch-up ×3 (×4 từ C5). **Trần PX:** lấy lại cảnh cũ ≤1 tuần Mid.
- **Nhịp:** từ lúc chết đến lúc điều khiển kiếp mới ≤20s (Trung Ấm 45s chỉ ở lần đầu, sau đó 8–12s, bỏ qua được). Có quyết định thú vị trong ≤90s. Hồn Hộ 10' (SURV).
- **Đo:** ≥35% số lần chết chọn đổi loài. Người chết vì PvP ở C≥3 quay lại trong 72h ≥60%.

### PX-07b: Phi Thăng và Thành Thần (từ vựng WORLD)
- **Phi Thăng** = qua kiếp lớn để vào cấp rừng sâu hơn. Ở MVP, Trung Kiếp C3→C4 là Phi Thăng vào vòng lõi **Linh Lâm** của cùng map, bên trong một Kết Giới.
- **Thành Thần** (post-launch, Cổ Đại): rời chuỗi thức ăn nhưng **ở lại** như một vùng sống. Cuối chu kỳ thì **Quy Căn**: tên khắc lên Thần Bia, rồi luân hồi.

### PX-08b: FTUE 20 phút, "Chuột mang hạt" (WORLD + SURV Thọ Nguyên + PROG Tiền Thân ×3)
Nguyên tắc: mỗi bước dạy **một** động từ mới. Kiếp đầu (Linh Thử) dùng đường cong **Tiền Thân ×3** scripted, không tính vào sim. Cây có tiếng nói từ giây thứ 10. Cái chết là **lựa chọn đọc được**. FTUE chạy 100% local.

| Phút | Hành động | Học được | Cảm xúc | Phần thưởng | UI mở thêm |
|---|---|---|---|---|---|
| 0:00–0:40 | Mộng Hỏa rơi qua tán cổ thụ **Lão Tùng**. Lão Tùng nói 1 câu: *"Lại một đốm mộng hỏa… Sống đi, nhỏ bé."* Chạm để nhập vào Linh Thử | Chạm/kéo để đi | Choáng ngợp, tò mò | "Linh Thử – Khai Trí" | Joystick |
| 0:40–3:00 | Ăn hạt linh thảo phát sáng | Ăn = tu vi | Thỏa mãn liên tục | Tầng 1 ở ~1:30, tầng 2 ở ~2:45 | Thanh tu vi, No |
| 3:00–5:00 | Bóng diều hâu AI lướt qua. Nút "Ẩn" hiện theo ngữ cảnh khi đứng cạnh bụi | Có kẻ săn mồi, trốn được | Hồi hộp lần đầu | Thoát Sinh +2 CT | Widget HP |
| 5:00–7:30 | **Tiểu Kiếp C1→C2:** 3 tia sét nhỏ, vòng cảnh báo trên đất, kéo để né | Đột phá là khoảnh khắc lớn | **Hùng tráng** (mốc fun #1) | Chọn **Bản Năng** (Tốc Túc / Độc Nha) | 1 nút skill |
| 7:30–10:30 | Cắn lá một cây non thì bị gai đâm. Lão Tùng thả **Linh Quả**, chuột ăn và **ngậm hạt** | Cây có ý thức: có thể đánh, có thể cho | Ngạc nhiên | +tu vi. Icon hạt trong má | Icon hạt |
| 10:30–12:00 | Thanh **Thọ Nguyên** hiện ra (loài đời ngắn, khoảng 12'). Quạ Già báo Linh Tức sắp tới | Sinh mệnh có hạn, rừng có sự kiện | Khẩn trương nhẹ | Tu vi ×2 trong Linh Tức | Thọ Nguyên (chỉ có ở FTUE) |
| 12:00–14:00 | Sói AI xuất hiện gần ổ chuột con. **Lựa chọn:** (A) dụ sói ra xa ổ, nhận Đạo Tâm ×1,5 "Hộ Ổ", hoặc (B) chạy về gốc Lão Tùng và chết già, được Linh Thổ +30% đầu kiếp. Cái chết chắc chắn xảy ra, nhưng do người chơi chọn. Né sói tới hết Thọ Nguyên ở lựa chọn A thì nhận thêm achievement "Nghịch Thiên" | Cái chết là lựa chọn | Quyết tâm | Tùy lựa chọn | — |
| 14:00–15:30 | **Trung Ấm lần đầu (45s):** xác hóa Linh Thổ, **hạt trong bụng nảy mầm từ xác**, 1 dòng Biên niên. Bánh xe luân hồi mặc định: *"Trở thành hạt giống ngươi đã mang"* (1 chạm) | Chết = tiến trình, đổi loài được | **Xúc động** (mốc fun #2) | Đạo Tâm đầu tiên | Bộ đếm Đạo Tâm |
| 15:30–20:00 | Chơi **Linh Mộc** (Hồi Ức ×3): kéo rễ tới đất ẩm, chạm Vệt Nắng, gai đâm hươu con AI đang gặm lá. Đột phá "Manh Nha" ở khoảng 18:00. Đặt Kế Hoạch Sinh Trưởng đầu tiên: *"Cây sẽ mọc 2 ô rễ khi ngươi rời đi."* | Gameplay thứ hai khác hẳn. Offline an toàn | Quyền lực chậm, khám phá | Mở **Rừng chung** + **PX-19: 1 vé Tự Quy miễn phí** (luân hồi chủ động, để P2 thành sói ngay mà không phải chết) | Vòng 3 lớp, Thủy, Quang Tinh, nút Gai |

- **Sau FTUE:** cây giữ nguyên cảnh giới (C1) và được "gió mang" vào Rừng chung, người chơi chọn ô gieo ở Bìa Rừng. Menu có 2 lựa chọn: **Rừng chung (PvP, mặc định)** và **Rừng riêng (solo + AI)**. Cả 3 loài mở ngay. Nghiệp Duyên chỉ giảm giá biến thể/loài 5+ (WORLD #6).
- **Cây mở dần:** phút 16–20 chỉ có rễ, Vệt Nắng, 1 gai. Hạt/neo Mầm Con mở ở C1 Hậu (phiên 2). Quả Ước mở ở C2. Độc mở theo Huyết Mạch C3.
- **Đo:** ≥80% đạt Tiểu Kiếp trước phút 8 · ≥65% tới luân hồi lần đầu · ≥55% chơi cây tới phút 20 · tỉ lệ chọn A/B nằm trong khoảng 35–65% (lựa chọn có nghĩa) · A/B test "chuột→hạt" với "chọn loài ngay" (WORLD).

### PX-09b: Mô hình server và chi phí

| Bậc | Chế độ | Kỹ thuật | Khi nào |
|---|---|---|---|
| T0 | **Rừng riêng** (solo + AI, bot) | Cùng mô-đun sim, chạy room local trên client, cloud save | MVP |
| T1 | **Co-op trong Rừng chung**: party ≤4 qua invite link, PvP với người ngoài nhóm | Colyseus room chung | MVP |
| T1b | Phòng co-op riêng (PvE + PvP nội bộ tùy chọn) | Room private | U1 |
| T2 | **Rừng Non chung**: ≤40 CCU/phòng, ≤150 cư dân, PvP luôn bật, **Kỷ Nguyên 28 ngày** | Colyseus server-authoritative, 10–15 Hz, interest management theo chunk | MVP |
| T3 | Nguyên Sinh 384², map 28 / nhân vật 56 ngày | Như T2, thêm zone | 1.0 |
| T4 | Cổ Đại 512², Thần Vị | Có thể cần multi-process | Post-launch |

- **PX-20 (mới), chế độ ngủ:** phòng có 0 người online thì sim chạy 1 Hz (tile-level), và catch-up khi có người vào. Rừng vẫn sống 24/7 mà gần như không tốn CPU.
- **Chu kỳ:** MVP có một loại reset là **Kỷ Nguyên 28 ngày**. Map reset, nhân vật luân hồi với Đạo Tâm theo cảnh giới đã đạt, sự kiện kết thúc là **Đại Kiếp** (lore của WORLD). Từ bản 1.0: map 28 ngày / nhân vật 56 ngày (SURV X2), đáp ứng mức ≥48 ngày của PROG. Đại Kiếp theo **lịch cố định**, không kích hoạt theo số Thần Vị (PROG đã chỉ ra blocker này).
- **Khu vực:** Singapore trước (VN/SEA), EU/US khi DAU ngoài SEA vượt 30%.

**Chi phí ước lượng (phải benchmark ở tuần 2):** VPS 2 vCPU ≈ 5–10 €/tháng, giả định chứa ~150–250 CCU. CCU/DAU ≈ 1:10. Băng thông ~3–5 KB/s/client.

| DAU | CCU đỉnh | Phòng | VPS | Server + DB + backup/tháng | Doanh thu ad (ARPDAU 0,01–0,03 USD) |
|---|---|---|---|---|---|
| 1K | ~100 | ~7 | 1 + 1 dự phòng | ~30 € | 300–900 USD |
| 10K | ~1.000 | ~70 | 6–8 | ~100–150 € | 3K–9K USD |
| 50K | ~5.000 | ~350 | 30–35 | ~500–700 € | 15K–45K USD |

Chi phí lớn nhất là **vận hành của 1 người**, không phải phần cứng. Giảm thiểu: không chat tự do (chỉ emote và câu soạn sẵn), **PX-17 (mới): không tên tự do**, chỉ "Đạo hiệu" sinh tự động (vd *Thanh Phong Lão Tùng*), đỡ cả gánh moderation tên lẫn vấn đề độ tuổi trên portal. Có kill-switch T2 và công cụ admin tối thiểu. Ngân sách vận hành ≤6h/tuần.

### PX-10b: Session 15–60 phút
- **Một phiên = một nhịp tu:** Mộng Báo (10s) → 2–3 Cơ Duyên trên map → vòng lặp chính → **điểm dừng tốt** là đột phá tầng hoặc Bế Quan kèm đặt Kế Hoạch Sinh Trưởng.
- **Mục tiêu nhịp:** kiếp đầu có mốc mới cứ 8–12'. Ở đường cong chuẩn, mỗi tầng ≈80 CT ≈ 1,2 phiên Mid, mỗi đại cảnh ≈3–4,5 phiên Mid.
- **Ước lượng MVP (PROG chốt):** C4 Hậu ≈ 600 CT lũy kế → Mid ~2 tuần, Core ~1 tuần, Casual ~3 tuần khi có Bù Đắp. Trong 28 ngày, Mid xong kiếp 1 rồi luân hồi sang loài thứ 2 có Tiền Kiếp. Đây chính là USP được chơi thật.
- Không có năng lượng/stamina, không có FOMO theo giờ cố định duy nhất.

### PX-11b: UI/UX đa nền tảng (ngân sách cứng)
- **Luật:** ≤4 chỉ báo cố định + 1 thanh tu vi · ≤5 nút hành động · **3 skill chủ động + 1 Thần Thông trên mọi nền tảng** · nút ≥48dp · HUD ≤18% màn hình · landscape · tôn trọng safe-area/notch.

| | Chỉ báo | Nút |
|---|---|---|
| **Thú (Hành)** | Vòng HP (Thể Lực là viền quanh joystick), No, Linh Khí, Thủy (theo SURV 2+2) + tu vi. Nghiệp chỉ hiện khi >0 | Joystick · Đánh/Ăn/Tương tác theo ngữ cảnh · 3 skill · Thần Thông (ô khóa đến U1, hiển thị như mục tiêu). Né = vuốt. Chạy = đẩy joystick ra mép |
| **Cây (Thần Thức)** | Vòng 3 lớp (Tán/Thân/Tâm Rễ), Thủy, Quang Tinh, Linh Khí + tu vi. Ánh sáng thể hiện bằng hình ảnh trên tán. Dưỡng Chất nằm ở panel phụ | Kéo trên map (rễ) · Phòng thủ (bánh xe 2) · Hạt · Quả · Cộng sinh (U1) · Thần Thông (U1). Bế Quan/Độ Kiếp ở menu ngữ cảnh |

- **Công bằng giữa nền tảng:** skill nhắm mềm (soft-lock 30°) để cảm ứng không thua chuột. Cùng 3+1 skill trên mọi máy.
- **Cây chơi một tay:** mọi thao tác Thần Thức làm được bằng ngón cái phải. Vệt Nắng là **cửa sổ bonus** (cứ 45–60s xuất hiện 1 vệt, kéo dài 15s), AFK chỉ mất ≤20%. Mục tiêu ≤6 chạm/phút để đạt 90% thu nhập.
- **Accessibility:** vòng cảnh giới dùng màu + hình · icon hướng cho mọi tín hiệu âm thanh · 3 cỡ chữ · giảm chớp/rung khi độ kiếp · giữ↔bật cho mọi nút giữ · remap phím PC · tôn trọng cờ tắt chat của portal. Solo chỉnh độ khó theo 3 trục: **Sinh tồn / Chiến đấu / Hình phạt chết**. Rừng chung dùng luật cố định.
- **Đo:** bấm nhầm <5% trên mobile · thời gian ra quyết định chạy/đánh ≤1s (đo bằng playtest có quay màn hình).

### PX-12b: Kinh tế (đơn vị CT) và monetization F2P

**Ví và luồng:**
```
SOURCES                                   KHO                         SINKS
chơi tích cực (ăn/quang hợp/săn) ~70%  ┐
Mộng Tích (×2, 30'/ngày)          ~20%  ├─► [Tu vi = CT] (thanh,     ─► cảnh giới (không tiêu được)
sự kiện (Linh Triều)              ~5–8% │    không phải ví)            chết: Hậu Duệ rơi về Sơ kỳ / Luân Hồi
PvP Sinh Năng 20 CT×m(g)          ≤5%   ┘                              kiếp thất bại −30% CT tầng
   └─ mọi hệ số nhân gộp CỘNG trong "Thiên Đạo Gia Trì", TRẦN ×3 (×4 trong 30' đầu sau luân hồi)

ăn/hấp thu/Linh Hạch/quỹ vùng ──► [Linh Khí] (trong kiếp) ──► skill, khiên, Đả Tọa (≤15% CT phiên), upkeep cảnh (SURV/WORLD)
quang hợp/xác/đất ─────────────► [Quang Tinh ≤150, Dưỡng Chất, Thủy] ─► rễ, Kế Hoạch Sinh Trưởng, phòng thủ (SURV)
luân hồi 25% CT lũy kế, Oán Linh, cuối Kỷ Nguyên ─► [Đạo Tâm] (meta) ─► mở loài (giảm giá theo Duyên, sàn 40%),
                                                                       Đạo Tâm Bàn 6 node (sức mạnh tổng ≤+10% CT),
                                                                       DƯ → Tiền Kiếp Ấn các bậc (prestige vô hạn, không bán)
sự kiện/thành tựu/ad ×2 ─────────► [Hoa Lộ] (cosmetic kiếm được) ─► skin (~1 skin thường/10h chơi)
nạp tiền ────────────────────────► [Ngọc Tinh] ───────────────────► skin, pass. KHÔNG đổi sang ví nào khác
```
(Tỉ trọng nguồn CT là ước lượng của PX. PROG chốt bằng sim.)

**Kiểm tra exploit:**
| Exploit | Chặn bằng |
|---|---|
| Kill-trading giữa 2 tài khoản | Sinh Năng cố định 20 CT × m(g), cùng cặp 1 lần/30', Oán Linh 1 lần/24h |
| Chồng hệ số (sim K của PROG: ×82) | Gia Trì cộng dồn kiểu cộng, trần ×3 |
| Cây idle offline | 0 CT offline, Quang Tinh có trần |
| Farm tự vệ thụ động bằng tài khoản phụ | Offline chỉ cho Dưỡng Chất |
| Đạo Tâm lạm phát | Node sức mạnh có trần thấp. Phần dư chảy vào Ấn (sink vô hạn, chỉ để xem) |
| Farm Đạo Tâm bằng ad ở solo | Ad Đạo Tâm chỉ có ở solo, node sức mạnh ≤+10%, F2P đạt trần sau ~3 kiếp. Rủi ro còn lại nhỏ, theo dõi bằng telemetry |

**Monetization (đạo đức, không P2W):**
1. **Skin:** không đổi silhouette, hitbox, vòng cảnh giới, độ tương phản với nền. Không có skin ngụy trang. Không che Tiền Kiếp Ấn. Ở PvP có tùy chọn "đối thủ hiện skin mặc định".
2. **Rewarded ads (luôn opt-in, đúng yêu cầu SDK của portal):**

| Vị trí | Rừng riêng (solo) | Rừng chung (PvP) |
|---|---|---|
| Hoa Lộ ×2 | ✅ 3 lần/ngày | ✅ 3 lần/ngày |
| Đạo Tâm khi chết +30% | ✅ 3 lần/ngày | ❌ |
| +5' Mộng Tích | ✅ 1 lần/ngày | ❌ |
| Hồi sinh tại chỗ | ✅ | ❌ |
| Bất kỳ thứ gì cho CT/chỉ số/thời gian | — | ❌ |

3. **Không có** interstitial trong lúc chơi, loot box trả tiền, VIP, năng lượng, hay đồng hồ chờ để bán nút skip. (Could, mặc định tắt: một midgame ad ở màn Trung Ấm, chỉ trong solo, ≥15'/lần, không bao giờ trong phiên đầu. Chỉ A/B nếu doanh thu dưới mục tiêu.)
4. **Pass Kỷ Nguyên (U1):** 28 ngày. Track free có Hoa Lộ + 2 skin. Track premium ~4,99 USD (giá địa phương VN ~49.000đ) có 6 skin, hiệu ứng độ kiếp, khung Biên niên, hoàn đủ Ngọc Tinh để mua pass kế tiếp nếu hoàn thành. Không bao giờ có Đạo Tâm hay CT.
5. **Sản phẩm cao cấp (U1):** **Pháp Tướng Độ Kiếp**, thiên tượng riêng khi Công Kiếp mà cả phòng nhìn thấy.
6. **Steam (1.0):** Gói Người Sáng Lập cosmetic 9,99 USD.
- **Đánh đổi đã chấp nhận:** cấm ad sức mạnh ở Rừng chung sẽ làm tỉ lệ xem ad thấp hơn. Mục tiêu ad giảm từ 35% xuống **≥25% DAU**.

### PX-13b: Tech stack (bổ sung)
- **TypeScript toàn bộ:** Phaser 3.x hoặc PixiJS v8 (chốt sau spike tuần 1–2) · **Colyseus từ ngày 1** (solo = room local, nên PvP không phải tính năng gắn vào muộn) · sim dùng chung client/server · Vite.
- **Ràng buộc portal (CrazyGames docs):** gói tải ban đầu ≤50MB, và **≤20MB** nếu muốn lên trang chủ mobile. Tổng ≤250MB, ≤1.500 file. Rewarded ad chỉ qua SDK. Mục tiêu nội bộ: **initial ≤20MB**, stream asset theo vòng map.
- **Backend:** Postgres managed cho hồ sơ và meta · snapshot thế giới mỗi 60s · Cloudflare CDN · PostHog (telemetry) + Sentry (crash).
- **Đóng gói:** Capacitor Android (U1) · Tauri cho Steam (1.0) · iOS post-launch.
- **Art:** AI-gen + chỉnh tay theo style guide khóa ở tuần 2. Thú dùng cutout rig (DragonBones, hoặc Spine nếu cần). **Cây procedural** (L-system/shader), vừa rẻ vừa là lợi thế của việc chơi cây. Hiệu năng: ≤300 entity động, sim sinh thái theo tile.

### PX-14b: Scope chốt — MoSCoW, Vertical Slice, MVP, Roadmap
(Tổng hợp từ đề xuất của cả 4 người. Ước lượng theo tuần-người, đã gồm AI hỗ trợ code/art/test.)

**Ngân sách G4:** 12 tháng ≈ 50 tuần lịch = **44 tuần-người làm tính năng/QA + 6 tuần đệm (~14%)**. Nghỉ lễ, Discord/marketing và bệnh đều nằm trong đệm. Nếu làm part-time thì nhân lịch theo tỉ lệ.

**So với R2:** MVP-A (~44 tuần, chưa có PvP người thật) + MVP-B (+13 tuần) = 57 tuần. Bản chốt dưới đây **đưa PvP người thật vào MVP** và vẫn chỉ ~44 tuần, nhờ cắt C5/Đại Kiếp, Kiến, Linh Ảnh, Pass, Android, Huyết Nguyệt, biome thứ 2, Công Kiếp, Thiên Phạt ra khỏi MVP (−13,5 tuần).

#### MUST: MVP (soft launch Web)
| # | Tính năng | Nguồn | Tuần-người |
|---|---|---|---|
| 1 | Tiền sản xuất: spike Phaser+Colyseus trên Safari iOS/Chrome Android (300 entity, ≤20MB), style guide, pipeline sim PROG → JSON | PX/PROG | 2 |
| 2 | Core engine: world tile 256², camera/zoom, save, sim dùng chung, netcode server-authoritative | PX | 4 |
| 3 | Controller thú chung + **Huyết Lang** (3+1, Hang/neo Huyết Noãn) | SURV/PROG | 2,5 |
| 4 | **Linh Thử** (dùng chung controller, trữ hạt, đào hang) | PX/WORLD | 1 |
| 5 | **Linh Mộc lite** (Thần Thức: kéo rễ, Vệt Nắng, gai + bánh xe phòng thủ, Mầm Con neo, Quả Ước, HP 3 lớp, Kế Hoạch Sinh Trưởng) | SURV-03/07, WORLD-14d/i | 4 |
| 6 | Needs 2+2, ngày/đêm, 4 mùa (palette + modifier), mưa + giông (dùng lại cho kiếp) | SURV | 1,5 |
| 7 | AI 3 archetype (Lộc đàn ăn lá, Diều Hâu săn, bầy côn trùng) + Director lite + bot lấp phòng | SURV-13 | 2 |
| 8 | Tiến hóa: khung 7 cảnh, **nội dung C1–C4** (12 tầng), CT, Mộng Tích, Bản Năng + **2 Huyết Mạch/loài** (~21 skill từ ~9 template), tên cảnh WORLD | PROG/WORLD | 3 |
| 9 | Tiểu Kiếp + **Trung Kiếp C3→C4 = Phi Thăng vào Linh Lâm** (Ẩn Kiếp, vẫn bị đánh úp được) | PROG-07 | 1,5 |
| 10 | Chết: Hậu Duệ + Luân Hồi đổi loài + Trung Ấm + Đạo Tâm Bàn 6 node + Tiền Kiếp + Biên niên (text) + Mộ Linh | SURV/PROG/WORLD | 2 |
| 11 | Map 256², 3 vòng (Bìa Rừng / Trung Lâm / Linh Lâm sau Kết Giới), 1 biome + biến thể, wayfinding không minimap | WORLD-05 | 2,5 |
| 12 | Bế Quan / Nhập Định / Mộng Báo / catch-up solo | PX-04b | 1,5 |
| 13 | Thiên Đạo Luật L1–L4 (không Thiên Phạt), Thiên Đạo ưu ái loài thiếu | PX-05b/16b | 1,5 |
| 14 | **Rừng chung T2:** lobby theo khu vực, phòng ≤40 CCU, party invite ≤4, persistence, reconnect, Kỷ Nguyên 28 ngày, anti-cheat cơ bản, emote, Đạo hiệu, kill-switch, admin | PX-09b | 4 |
| 15 | FTUE "chuột mang hạt" | PX-08b | 1,5 |
| 16 | UI/HUD 2 chế độ điều khiển + accessibility cơ bản | PX-11b | 2,5 |
| 17 | 2 sự kiện: **Đại Linh Triều** (24h, đỉnh 30') + **Đại Kiếp** cuối Kỷ Nguyên | SURV/PROG/WORLD | 1 |
| 18 | Rewarded ads (SDK portal) + shop 6 skin + Hoa Lộ | PX-12b | 1 |
| 19 | Telemetry + crash + dashboard KPI | PX | 0,5 |
| 20 | Âm thanh (asset + AI), lore ~4k từ, VN/EN | WORLD | 1 |
| | Tích hợp, QA, sửa lỗi closed alpha | — | 3,5 |
| | **Tổng** | | **44** (+6 đệm = 50 tuần lịch) |

#### SHOULD: Update 1 "Linh Lâm Khai Môn" (tháng 13–15, ~11,5 tuần)
C5 Bản Thể (scale +30%) + Đại Kiếp C5→C6 + Công Kiếp/Pháp Tướng (2) · Pass Kỷ Nguyên (1,5) · Android Capacitor (2) · Kiến cộng sinh (2) · Huyết Nguyệt (0,5) · biome thứ 2 (1,5) · phòng co-op riêng (0,5) · Thiên Phạt (0,5) · Biên niên dạng ảnh chia sẻ (0,5) · framework Kỷ Nguyên modifier (0,5).

#### COULD: Bản 1.0 (tháng 16–21, ~24 tuần)
Khuẩn, loài thứ 4 (5) · Linh Thức cho cây (2) · Đạo Đồ chung + Keystone (3) · Mộc Độn kèm ràng buộc SURV (1) · Ký Hồn Mộc (0,5) · Đại Hỏa + Rừng Tro + diễn thế 3 giai đoạn (3) · 2 bí cảnh: Lôi Trì, Mộng Cảnh (4) · map Nguyên Sinh 384² + tách reset map 28 / nhân vật 56 (4) · Steam Early Access qua Tauri (2).

#### POST-LAUNCH (XL, chỉ khi KPI 1.0 đạt)
Cổ Đại 512², C6–C7, Thiên Kiếp, Thần Vị/Quy Căn · Nhân Hình + Pháp Bảo · Xuất Khiếu/Linh giới · Mộng Ảnh (async) · Tu Sĩ Nhập Sơn · iOS · tông môn.

#### WON'T (giai đoạn này)
Chat tự do, tên tự do · Minh Ước hay bất kỳ công tắc tắt PvP nào ở Rừng chung · loot box trả tiền, VIP, năng lượng, mọi thứ P2W · thời tiết lũ/sương mù · 9 cảnh giới (trừ khi đạt điều kiện ở mục Lập trường #1).

#### Vertical Slice (tuần 3–14, kiểm định ở tuần 14–16)
FTUE đầy đủ · Linh Mộc lite C1–C2 · Linh Thử · Lang AI · 1 vòng map · Tiểu Kiếp · luân hồi · Bế Quan solo · **2 client PvP cùng một room Colyseus** (bằng chứng PvP chạy từ ngày 1).
**Câu hỏi phải trả lời:** (1) Luân hồi chuột→cây có khiến ≥70% tester muốn chơi kiếp tiếp không? (2) Cây có giữ ≥50% tester chơi ≥10' không? Nếu (2) trượt: dừng 2 tuần để làm lại cây trước khi đi tiếp. Không cắt cây.

#### Lịch MVP
| Giai đoạn | Tuần | Mốc |
|---|---|---|
| Tiền sản xuất | 1–2 | Spike, style guide, benchmark CCU |
| Vertical Slice | 3–14 | Playtest 15–20 người (H1–H3) |
| Alpha | 15–34 | 3 loài, C1–C4, Thiên Đạo, Rừng chung. **Closed alpha PvP người thật trên Discord từ tuần ~30** (100–300 người) |
| Beta | 35–44 | UI/accessibility, ads/shop, telemetry. Open beta itch.io với 1 Kỷ Nguyên 28 ngày trọn vẹn |
| Đệm + Soft launch | 45–50 | Web: CrazyGames + itch.io + site riêng (Poki nếu được duyệt). Kỷ Nguyên 1 chính thức |

#### Giữ "PvP tự do" dù lịch trượt
1. Netcode server-authoritative từ ngày 1, solo chỉ là room local, nên PvP **không thể bị dời** thành một tính năng riêng.
2. PvP người thật có mặt ở VS (nội bộ), closed alpha (tháng 7–8) và soft launch (Rừng chung là chế độ mặc định).
3. **Thứ tự cắt nếu trượt** (tổng tiết kiệm −5,5 tuần): Kế Hoạch Sinh Trưởng chỉ còn "Tán mọc lại" (−0,5) → mùa 4→2 (−0,5) → Đạo Tâm Bàn 6→3 node (−0,5) → chỉ giữ Đại Linh Triều (−0,5) → map 3 vòng→2 + Linh Lâm thành enclave nhỏ (−1) → shop chỉ còn 2 skin (−0,5) → Huyết Mạch 2→1 + nhánh mặc định (−1) → Linh Thử chỉ còn AI + FTUE (−1, phương án cuối).
4. **Không bao giờ cắt:** cây, luân hồi đổi loài, độ kiếp, Rừng chung PvP, Thiên Đạo L1–L3, FTUE.
5. Nếu cắt hết danh sách mà vẫn trượt: **lùi soft launch tối đa 6 tuần (tháng 13–14)**, chứ không ra mắt thiếu PvP vì như thế vi phạm ràng buộc cứng.

### PX-15b: Retention và live-ops (một người vận hành được)
| Mốc (premium tương đương) | Hook ở MVP |
|---|---|
| D1 (1h) | Mộng Báo: rễ đã lan, quả chín · Mộng Tích đầy · mục tiêu Trung Kiếp đã hiện trên Kết Giới Linh Lâm |
| D7 (10h) | Đại Linh Triều đầu tiên · Mid gần C4 · lần đổi loài đầu tiên với Tiền Kiếp · Huyết Sát bounty |
| D30 (30–50h) | Đại Kiếp cuối Kỷ Nguyên, Biên niên tổng kết, Bảng Phi Thăng · Kỷ Nguyên mới mang modifier mới · Đạo Tâm mở Huyết Mạch biến thể |

**Lịch sự kiện (tự động, không cần GM):**
- **Linh Tức** (vi mô): 10', khoảng mỗi 90' với giờ trôi ngẫu nhiên. Phiên 40' gần như luôn gặp một lần.
- **Đại Linh Triều** (tuần): kéo dài 24h thực, có **đỉnh 30' vào 20:00 giờ khu vực** (PROG, sim L: phủ ~85% số tuần của Mid). Trôi ngày trong tuần theo mùa-rừng.
- **Đại Kiếp** (28 ngày): sự kiện kết Kỷ Nguyên 30', lặp lại 2 khung giờ để mọi múi giờ đều xem được.
- Huyết Nguyệt (U1), Đại Hạn/Hỏa (1.0). Luật SURV: mỗi sự kiện có kẻ thắng và kẻ thua theo giới, và người đang Bế Quan không bị ảnh hưởng.
- **PX-22 (mới), Kỷ Nguyên modifier:** mỗi kỳ 1 luật xoay vòng dạng data (vd "Kỷ Nguyên Hạn: Thủy decay ×1,3, nấm/cây chịu hạn được ưu ái"). Chi phí S mỗi cái, tạo cảm giác rừng mới mà không cần nội dung mới.
- **Nhịp nội dung:** 1 bộ skin mỗi Kỷ Nguyên, 1 update lớn mỗi 2 Kỷ Nguyên. Ops ≤6h/tuần.

### PX-16b: Cân bằng loài
Giữ bonus "Thiên Đạo ưu ái" (+25%, nằm trong trần ×3, có aura) cho loài chiếm <15% dân số. **Bỏ** thời gian chờ 60s với loài >35% (vì nó tạo ra thứ để bán nút bỏ qua). Thay bằng Director tăng AI con mồi khi thú ăn thịt vượt 35% (SURV).

### PX-21 (mới): Tách quyết định 7/9 cảnh giới khỏi MVP
C1–C4 trùng tên và vai trò ở cả hai phương án (Khai Linh, Tụ/Luyện Khí, Trúc Cơ, Kết Đan), nên MVP **sản xuất được ngay**. Quyết định cuối chỉ ảnh hưởng nội dung U1 trở đi. PROG chỉ cần cung cấp đường cong C1–C4 và hệ số combat power mỗi cảnh trong khoảng 1,6–1,8× để chốt PvP MVP.

### Playtest hypotheses
| ID | Giả thuyết | Đo | Ngưỡng | Giai đoạn |
|---|---|---|---|---|
| H1 | Tiền Thân ×3 đưa người chơi tới khoảnh khắc lớn đầu tiên | % đạt Tiểu Kiếp trước phút 8 | ≥80% | VS |
| H2 | "Chuột mang hạt" tạo ham muốn chơi kiếp tiếp | % bắt đầu kiếp 2 trong 60s sau khi chết | ≥70% | VS |
| H3 | Cây đủ vui | % chơi cây ≥10' · chạm/phút để đạt 90% thu nhập | ≥50% · ≤6 | VS |
| H4 | Bế Quan xóa nỗi sợ offline | Khảo sát "lo mất tiến độ khi offline" (1–5) | ≤2,5 | Alpha |
| H5 | Sát Nghiệp giảm bắt nạt | % kill PvP có g≥2 (cảnh thật) | ≤10% | Alpha |
| H6 | Mộng Báo kéo người chơi quay lại | D1 có/không có Mộng Báo (A/B) | +5 điểm % | Beta |
| H7 | Cân bằng loài tự nhiên | Có loài nào >40% dân số suốt 7 ngày không | Không | Alpha |
| H8 | Đổi loài vẫn hấp dẫn khi có Hậu Duệ | % lần chết chọn đổi loài | ≥35% | Alpha |
| H9 | Chi phí cái chết chịu được | Chết vì PvP ở C≥3 rồi quay lại trong 72h | ≥60% | Alpha/Beta |
| H10 | Ngân sách UI đủ | Bấm nhầm trên mobile | <5% | VS/Beta |
| H11 | Lựa chọn cách chết trong FTUE có nghĩa | Phân bố A/B | 35–65% | VS |
| H12 | P2 không bị khóa khỏi sói | % P2 (tự khai) dùng vé Tự Quy hoặc chơi sói trước phút 40 | ≥70% | Beta |

**KPI go/no-go soft launch (cho U1/Android):** D1 ≥25% (traffic portal) / ≥30% (organic, Discord) · D7 ≥8% · D30 ≥3% · session trung bình ≥14' · ≥1,8 phiên/DAU/ngày · xem rewarded ad ≥25% DAU · crash <1% · CCU/phòng đỉnh ≥12 (rừng không vắng). **Gate 1.0/Steam:** D30 ≥4% và doanh thu ≥2× chi phí vận hành trong 2 Kỷ Nguyên liên tiếp.
**Telemetry bắt buộc:** time-to-first-breakthrough, phút bỏ game trong FTUE, lựa chọn A/B khi chết ở FTUE, nguyên nhân chết (AI/PvP, g thật), Hậu Duệ hay đổi loài, loài được chọn khi luân hồi, thời lượng offline và tổn thất, Nghiệp phân bố, số chạm/phút của cây, nguồn CT theo tỉ trọng, ad view theo vị trí, CCU theo phòng.

### Risk Register (cập nhật)
| Rủi ro | Khả năng | Tác động | Giảm thiểu | Phụ trách |
|---|---|---|---|---|
| Scope creep vượt 50 tuần | Rất cao | Rất cao | MoSCoW chốt. Mỗi ý tưởng mới phải ghi rõ thay cái gì. Danh sách cắt có thứ tự | PX |
| PvP người thật bị đẩy lùi | Trung bình | Rất cao (vi phạm brief) | Netcode từ ngày 1, PvP trong VS, closed alpha tuần 30, chỉ cho lùi tối đa 6 tuần | PX |
| Cây không vui / quá nhiều thao tác | Cao | Rất cao (USP) | Gate VS cho H3, ngân sách ≤6 chạm/phút, mở dần UI | SURV/PX |
| Người mới bị grief, D1 sụp | Cao | Rất cao | Ấu Linh 3h, Áp Chế, Sát Nghiệp theo cảnh thật, FTUE local | PX/PROG |
| Core chạm trần C4 sau ~1 tuần rồi hết nội dung dọc | Cao | Trung bình | Vòng luân hồi đổi loài, Huyết Sát bounty, U1 thêm C5 ở tháng 13–14 | PX/PROG |
| Rừng vắng (dân số thấp) | Cao | Cao | Phòng ≤40, bot Director, ghép theo khu vực, gộp phòng khi CCU <8 | PX |
| Lệch loài (ai cũng chọn sói) | Cao | Cao | PX-16b + Director tăng AI con mồi | PROG/SURV |
| Doanh thu ad thấp (do không bán sức mạnh ở PvP) | Trung bình | Cao | Pass U1, Pháp Tướng, Steam Founders, chi phí server thấp | PX |
| Cheat trên web | Trung bình | Cao | Server-authoritative, rate-limit, không tin client | PX |
| Kiệt sức solo dev | Cao | Rất cao | Ops ≤6h/tuần, sự kiện tự động, không chat/tên tự do, đệm 14% | PX |
| Hiệu năng mobile web, bundle >20MB | Trung bình | Trung bình | Spike tuần 1–2, ≤300 entity, stream asset | PX |
| Art AI thiếu nhất quán | Trung bình | Trung bình | Style guide khóa tuần 2, cây procedural | WORLD |
| Quyết định 7/9 cảnh kéo dài | Trung bình | Thấp (nhờ PX-21) | Chốt trước U1. MVP không phụ thuộc | PROG/PX |
| Khán giả nhỏ tuổi trên portal + PvP | Trung bình | Trung bình | Không chat/tên tự do, bạo lực stylized, tôn trọng cờ tắt chat | PX |

---

## Những thứ tôi mượn từ người khác
- **SURV:** HUD 2+2 (SURV-01) · HP 3 lớp + Tâm Rễ (SURV-03) · 6 động từ cây (SURV-07) · Ấu Thể Ẩn Khí, Thoát Sinh (SURV-11) · Hồn Thoát 30s, Nhập Định offline (SURV-12) · Director (SURV-13) · Hồn Hộ 10' (SURV-15) · Kế Hoạch Sinh Trưởng, trần tổn thất 24h, teo rễ sau 48h (X3) · Thọ Nguyên trong FTUE · "sự kiện có kẻ thắng/kẻ thua theo giới" (SURV-17).
- **PROG:** CT làm đơn vị kế toán (PROG-03) · Mộng Tích (PROG-04) · Tốc không scale (PROG-11) · Thiên Đạo Luật hợp nhất (PROG-12b) · Gia Trì cộng dồn, trần ×3/×4 · offline 0 CT · sự kiện theo ngày thực có đỉnh 30' · vòng Linh Lâm cho MVP · Tiền Thân ×3 · Đại Kiếp theo lịch cố định · tổng ~1.671 CT.
- **WORLD:** FTUE "chuột mang hạt → cây mọc từ xác" và giọng Lão Tùng (WORLD R2) · glossary (Mộng Báo, Mộng Tích, Nhập Định, Tâm Hướng) · Phi Thăng/Thành Thần/Quy Căn · Đại Kiếp làm lore cho reset · Quạ Già báo sự kiện · Tiền Kiếp Ấn · hook mới · Duyên giảm giá thay vì khóa loài · tên cảnh giới hợp nhất · Hậu Duệ rơi về Sơ kỳ.

## Lập trường giữ vững (và vì sao)
1. **7 cảnh giới, không 9.** Từ góc UX/FTUE/pacing:
   - Nhịp *cảm nhận* nằm ở tầng chứ không ở đại cảnh. Cùng tổng 1.671 CT, 7×3 cho ~80 CT/tầng (1,2 phiên Mid), 8×3 cho ~70 CT/tầng (1,1 phiên). Hai con số chênh ~10%, người chơi không cảm nhận được.
   - Nhịp FTUE (phút 7/14/22) do đường cong Tiền Thân ×3 quyết định, nên không phụ thuộc 7 hay 9.
   - Với 7 cảnh, mỗi đại cảnh ≈240 CT ≈ 3,7 phiên Mid, vẫn nằm trong mục tiêu 2,5–4,4 phiên của chính PROG.
   - 9 cảnh đẻ ra C7–C8 chưa có khả năng mới về chất (SURV), tức nhiều tuần mid-late game chỉ có số tăng.
   - Thêm 2 cảnh là thêm 2 cột tên × mỗi loài để bản địa hóa, và chữ trên mobile dài hơn.
   - 3 trong 4 designer đã hội tụ về ánh xạ 3/2/2, khớp 3 kiếp lớn.
   - **Điều kiện để tôi đổi ý:** sim của PROG trên khung 7 cho thấy có đại cảnh nào >5 phiên Mid mà không sửa được bằng cách phân bổ lại CT, **hoặc** WORLD/PROG đưa ra được khả năng mới về chất cho C7–C8 với chi phí ≤M. Nhờ PX-21, cuộc tranh luận này không chặn MVP.
2. **Ad ở Rừng chung = 0 CT.** Bất kỳ phần trăm tu vi nào mua được bằng ad trong thế giới PvP đều sẽ bị review gọi là P2W, dù chỉ +8%.
3. **Ngân sách UI 4+1 chỉ báo / ≤5 nút / 3+1 skill trên mọi nền tảng.** Cross-play PvP không chịu được việc PC có nhiều nút hơn mobile.
4. **Kiếp đầu là Linh Thử, không phải cây.** Cây vẫn có mặt và có tiếng nói ngay từ giây 10, nhờ đề xuất của WORLD.
5. **Không chat tự do, không tên tự do ở MVP.** Một người không moderate nổi.
6. **Pass và Kỷ Nguyên 28 ngày** (không dùng 24 hay 14), vì khớp nhịp tuần, khả năng sản xuất của 1 người và thời gian Casual cần để tới C4.
7. **Sát Nghiệp tính theo cảnh giới thật**, không tính sau Áp Chế. Nếu tính sau Áp Chế, C4 bị nén về C3 Hậu sẽ giết C2 với g=1, không sinh Nghiệp.

## Điều tôi sẵn sàng đánh đổi
- Đưa C5/Đại Kiếp ra khỏi MVP, và chấp nhận rủi ro người chơi Core hết nội dung dọc sau ~1 tuần (đã ghi trong risk register).
- Đổi sang 9 cảnh nếu đạt điều kiện ở mục 1.
- Tăng trần Hậu Duệ tệ nhất từ 2 lên 3 phiên Mid, để giữ được mô hình "rơi về Sơ kỳ" của WORLD.
- Mục tiêu xem ad giảm từ 35% xuống 25% DAU, đổi lấy kinh tế PvP sạch.
- Chỉ 1 biome và 2 sự kiện ở MVP.
- Biến Linh Thử thành AI-only nếu lịch trượt tới phương án cuối, dù việc đó làm chuỗi thức ăn giữa người chơi mỏng đi.
- Lùi soft launch tối đa 6 tuần, chứ **không** cắt cây, luân hồi, độ kiếp hay PvP Rừng chung.

---
*Nguồn tra cứu (11/2026): [CrazyGames technical requirements](https://docs.crazygames.com/requirements/technical) · [CrazyGames requirements intro](https://docs.crazygames.com/requirements/intro/) · [Grow The Seed (Gaming Nexus)](https://www.gamingnexus.com/News/67543/Grow-The-Seed---A-Deck-Building-Survival-Game2c-Sprouting-May-2025) · [Steam plant-survival 2026](https://store.steampowered.com/app/4789970) · [Tree Simulator 2022 (Steam)](https://store.steampowered.com/app/1591290/Tree_Simulator_2022/)*
