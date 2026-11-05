# The Forest of Life — Game Design Document v1.2

> Thay thế v1.0 (`debates/2026-11-05-forest-of-life-gdd/FINAL.md`). Session sửa đổi: `debates/2026-11-05-ngu-toc-redefine/` · R1 → R2 → R3 → orchestrator phân xử → v1.1 → **R7 patch theo Bổ sung 4** → v1.2 · Ngày 2026-11-05.
> Tác giả: **SURV** (sinh tồn) · **PROG** (tiến trình & số) · **WORLD** (thế giới) · **PX** (trải nghiệm, kinh tế, phạm vi). Orchestrator tổng hợp. ID nguồn ghi ở mỗi mục (vd `PROG-08`). **[orch]** = orchestrator tự hài hòa khi hai bản lệch nhau.
> Nhãn: **[MVP]** soft launch Web · **[U1]** Update 1 · **[1.0]** · **[Post]** · **[Cắt]/[Won't]**. Nhãn **[A']/[B']/[C']** = phụ thuộc cấu hình phạm vi người dùng chọn (§16).
> Đơn vị: **CT** = tu vi của 1 phút chơi tích cực. Mid = 5 phiên × 40'/tuần ≈ 64 CT/phiên. Thời lượng trong bản này tính bằng **giờ chơi tích cực**.

---

## 0. TL;DR

1. **Game:** sinh tồn tu tiên PvP 2D/2.5D top-down (Web/Mobile/PC). Người chơi là **Mộng Hỏa** nhập vào một sinh linh của **Ngũ Tộc**: **Mộc** (mọi loài cây, cỏ) · **Thú** (thú nhỏ → lớn) · **Trùng** (côn trùng) · **Thủy** (cá, cua, ếch, nhái, rùa, cá sấu… sống ở nước, gần nước, đầm lầy) · **Vũ** (chim, gà, quạ, cú…). Mỗi tộc có **một đặc tính tộc** chung cho mọi loài (Mộc **tự dưỡng**, Thú **đánh hơi**, Trùng **bầy & lột xác**, Thủy **sống dưới nước**, Vũ **bay**), quan hệ **sinh / khắc / cộng sinh** theo Ngũ Hành, và mỗi nhân vật có **nội tại riêng** + con đường phát triển riêng.
2. **MVP = 5 tộc × 1 nhân vật, mỗi nhân vật phát triển đầy đủ C1–C4 + Viên Mãn:** Linh Mộc (cây), Lang (sói), Linh Nghĩ (kiến), Thanh Oa (ếch), **Linh Nha (quạ)**.
3. **Tiến trình "Đạo Lộ":** mỗi mốc đột phá chọn **1 trong 3–5 thẻ**. Thẻ **kế thừa** nhau (bậc sau sửa bậc trước) và **còn hiệu quả tới hết đời**.
4. **Cái chết:** **chết giữa đường = đời mới hoàn toàn từ C1**, không mang sức mạnh nào. **Viên Mãn** (hoàn thành C4) → random **3 hiệu ứng** trong số đã nhận → chọn **1 Đạo Chủng** mang sang mọi đời sau. *"Chết giữa đường, ngươi trả lại cho rừng. Đi hết đường, rừng trả lại cho ngươi."* Có 6 lớp đệm chống mất trắng vô lý (kiếp thất bại ≠ chết, Trọng Thương, rớt mạng không chết…).
5. **Phạm vi (giữ đệm 8,5% ở mọi cấu hình):** **A' đủ 5 tộc, ra mắt tuần 61 (khuyến nghị)** · B' rút gọn, tuần 57 · C' 4 tộc ở tuần 54, Vũ đợt 2 tuần 58. Không có cấu hình 50 tuần nào giữ được 5 nhân vật đầy đủ. Không bán sức mạnh.

### 0.1 Phạm vi thay đổi so với v1.0 (các hạng mục đã trao đổi)
| Hạng mục (quyết định chốt của người dùng) | Nội dung | Mục bị đổi | Owner |
|---|---|---|---|
| **Ngũ Tộc định nghĩa lại** | Mộc = mọi cây cỏ · Thú · Trùng · **Thủy thay Khuẩn** (loài sống ở/gần nước, đầm lầy) · Vũ = chim, gà, quạ, cú… · **Khuẩn = yếu tố môi trường** | §2.1, 2.4, 2.7, 4.1, 5.5, 5.7, 10, 18 | WORLD |
| **A. Thế mạnh riêng mỗi tộc** | 1 vai độc quyền / tộc | §2.7, 4.1 | WORLD · SURV |
| **B. Sinh / khắc / bổ trợ / cộng sinh** | Ma trận 5×5 đo được, khắc là **cơ chế** | §4.5, 4.6, 6.9 | SURV (cơ chế) · PROG (số) |
| **C. MVP: mỗi tộc 1 nhân vật** | 5 nhân vật | §4, 16 | PX |
| **H. (Bổ sung 4) Mỗi nhân vật phát triển đầy đủ** | Cả 5 đủ C1–C4 + Viên Mãn (bỏ bản lite) | §4.5, 6, 16 | PROG · PX |
| **I. (Bổ sung 4) Đặc tính tộc + nội tại riêng** | Đặc tính dùng chung mọi loài trong tộc; mỗi nhân vật 1 nội tại đặc trưng | §4.2, 6.6b | SURV (đặc tính) · PROG (nội tại) · WORLD (tên) |
| **J. (Bổ sung 4) Vũ bay thật · Thủy sống dưới nước** | Hệ **tầng Z** (Đất / Không / Đáy nước) | §4.2a, 5.8, 15 | SURV · PROG · PX |
| **D. 3–5 lựa chọn mỗi mốc, kế thừa, hiệu quả hết đời** | Đạo Lộ thay Huyết Mạch/Ngộ Đạo/Keystone | §6.4–6.5 | PROG |
| **E. Chết giữa chừng = bắt đầu mới hoàn toàn** | Bỏ Hậu Duệ, Hồi Ức, Túc Tuệ, Đạo Quả meta | §7, 8, 14 | SURV (luật) · PROG (số) |
| **F. Hoàn thành → random 3, chọn 1 mang sang** | Viên Mãn, Đạo Chủng, Sổ Di Sản | §6.10, 7 | PROG · WORLD |
| **G. Gameplay mỗi tộc khác nhau một chút** | Khung chung + 1–2 động từ riêng / tộc | §4.2, 4.7 | SURV · PROG |

---

## 1. Tầm nhìn, hook, đối tượng — owner: PX · WORLD

### 1.1 Theme & hook
- **Theme:** *"Mọi sự sống đều được nuôi bằng một sự sống khác. Kẻ mạnh nhất không phải kẻ ăn nhiều nhất, mà là kẻ nuôi được cả khu rừng."*
- **USP:** *Game sinh tồn tu tiên PvP cho bạn làm bất kỳ sinh mệnh nào trong rừng (cổ thụ, sói, kiến, ếch, gà rừng). Năm tộc nuôi nhau và khắc nhau theo Ngũ Hành. Chết thì trả mình về cho rừng; đi hết đường thì rừng trả lại cho bạn một hạt Đạo.*
- **Hook trailer:** *"Kiếp này em là con chuột mang hạt. Kiếp sau em là cổ thụ mọc từ xác chính mình."* (giữ: chuột là FTUE)
- **Tagline:** *"Sống. Bị ăn. Mọc lại thành rừng."*

### 1.2 Năm trụ cột
| # | Pillar | Người chơi phải cảm thấy | Cơ chế chứng minh | Kiểm chứng |
|---|---|---|---|---|
| P1 | **Ăn và bị ăn** | Mọi sinh linh là mồi hoặc mối đe dọa | PvP tự do, ma trận Ngũ Tộc, Thiên Đạo Luật | ≥70% kể được "một lần suýt chết" sau phiên 2 |
| P2 | **Chậm mà vĩ đại** | Kiên nhẫn được đền đáp | Lãnh thổ rễ, Niên Luân, Viên Mãn | ≥50% người thử cây chơi ≥10' |
| P3 | **Cái chết là hạt giống** | Chết đau nhưng có nghĩa — hạt giống **của rừng** | Trung Ấm, Sổ Sinh Năng, "Ngươi để lại", Viên Mãn/Đạo Chủng | Chết trước C3: ≥65% bắt đầu đời mới trong 2' · chết PvP C3+: ≥45% quay lại trong 72h |
| P4 | **Rừng nhớ** | Hành động để lại dấu vết | Mộ Linh, **Hóa Tích**, Biên Niên, Khô Linh, Thần Bia | ≥30% chạm Mộ Linh/Hóa Tích trong tuần 1 |
| P5 | **Trời đất chứng giám** | Độ kiếp, sự kiện là khoảnh khắc chung | Kiếp Viên Mãn, Đại Linh Triều, Đại Kiếp | ≥40% độ kiếp chọn Công Kiếp (U1) |

> **Luật hóa theme:** **Linh Quỹ/Khô Linh** (MVP) và **Công Đức** (U1+) là hai cơ chế duy nhất biến theme thành luật. Không cắt cả hai cùng lúc. *(Hệ quả: cấu hình B cắt Linh Quỹ động ở MVP → vi phạm luật này tới khi U1 có Công Đức; thêm một lý do không chọn B.)* [orch]

### 1.3 Persona *(PX-01b)*
| Persona | Nền tảng | Session | Động lực | Cần | Sợ |
|---|---|---|---|---|---|
| **P1 "Đạo hữu xe buýt"**, 18–30t, đọc tiên hiệp | Mobile web → Android | 10–20', 2–3 lần/ngày | Completion, Power, Fantasy | Đột phá đều, thấy thứ gì đó lớn lên | Mất công sức vì bị gank |
| **P2 "Kẻ săn mồi"**, 16–28t, fan The Isle / mope.io | PC web → Steam | 45–90' | Competition, Excitement | Săn người thật, adrenaline | Lớn chậm, không được làm sói |
| **P3 "Người làm vườn"**, 20–40t, cozy/strategy | PC/Mobile | 20–40' | Design, Strategy, Discovery | Lan rễ, cộng sinh, thấy rừng đổi vì mình | Thao tác twitch |

**Vòng đời theo persona (sim B, PROG-11/R7):** một đời đầy đủ (C1–C4): P1 ~7–8 ngày · P3 ~1,9 tuần · Mid ~7 phiên (4,6–5,2h tùy tộc) · P2 ~1 tuần. **Tổng nội dung lần đầu (Mid):** Viên Mãn cả 5 tộc ≈ **24,5h (~7 tuần)**.

### 1.4 Đối thủ & khoảng trống
| Đối thủ | Học được | Khán giả phàn nàn | Bài học |
|---|---|---|---|
| The Isle / Path of Titans | Nỗi sợ thật, PvP chuỗi thức ăn | Lớn 4–6h, người mới bị ăn ngay | Lớn nhanh, chết có ý nghĩa, mật độ sự kiện cao |
| mope.io / evowars | Vào game 5 giây, tiến hóa mỗi 1–2' | Không có meta | Chỉ mượn nhịp đầu game |
| Hades / roguelite | Lựa chọn mỗi mốc, chết = run mới, meta nhỏ | — | **Đạo Lộ + Đạo Chủng** là cấu trúc roguelite đặt trong thế giới PvP bền |
| Game tu tiên idle/MMO | Cảm giác đột phá, tên cảnh giới | P2W, VIP | Giữ đột phá, bỏ P2W |
| Tale of Immortal | Tiên hiệp bán được trên Steam | Grind, UI rối | UI phải gọn |
| Game làm cây | Có cầu cho fantasy "làm cây" | Single-player | Khoảng trống: PvP nhiều người, luân hồi giữa các loài |

---

## 2. Thế giới & lore — owner: WORLD

### 2.1 Bốn sự thật *(WORLD-01b)*
| Sự thật | Nội dung | Người chơi **làm** gì với nó |
|---|---|---|
| **S1. Kiến Mộc đã ngã** | Rễ của nó vẫn sống: **Linh Mạch**, đồng thời là **mạch nước ngầm**. Chỗ mạch trồi lên là **Linh Tuyền** | Đi **ngược dòng = vào trong rừng** (wayfinding). Cắm rễ cạnh suối là cắm gần mạch |
| **S2. Linh khí chỉ chuyển chủ** | *nắng → cây → (chim, thú ăn cỏ) → thú săn → xác → **đất hoặc nước** → Linh Mạch.* Phân giải là **quy trình của rừng** (nấm, vi khuẩn — yếu tố môi trường, không thuộc tộc nào). Trùng (Mở Xác) và Thủy (xác chìm) chỉ **tăng tốc hoặc chuyển hướng** dòng chảy đó | Nền của Linh Quỹ/Khô Linh và Sổ Sinh Năng |
| **S3. Ý thức là mộng của Kiến Mộc** | Mộng Hỏa là **ngọn lửa ý chí**, không phải kho sức mạnh; sức mạnh nằm trong thân, chết thì thân trả hết cho rừng. **Nước là thứ duy nhất nhớ mà không giữ hình**: Mộng Hỏa tắt trong nước rồi nổi lên thành một đốm mới, không mang gì. Chỉ đời **đi hết đường** mới kết phần mộng đã chín thành **Đạo Chủng**, nước giữ hộ | Giải thích chết = mới hoàn toàn, Viên Mãn = Đạo Chủng. Ý Chí Rừng (Director), Linh Ảnh (bot) giữ như v1.0 |
| **S4. Thần Vị là rễ cái của Kiến Mộc mới** [Post] | 5 Thần Vị Ngũ Hành, khớp 5 tộc (§9.3) | Endgame |

**Vì sao Thủy Tộc giữ luân hồi:** mọi dòng nước chảy về **Suối Nguồn** dưới gốc Kiến Mộc. **Huyền Vũ — Lão Quy** ngồi canh dòng đó, **Bạch Hạc** (sứ giả Vũ Tộc) đứng trên lưng Lão — hình tượng hạc–quy của đền Việt, nhìn từ xa là biết nơi luân hồi. Trung Ấm diễn ra trên mặt nước; Đạo Chủng hiện lên từ nước; cá tụ hay tản theo Linh Quỹ.
**Ba bí mật theo hồi** giữ nguyên v1.0 (Mảnh Mộng 3: bóng người cầm rìu — nay hiện **trên mặt nước Đầm Mục**). Authored MVP ~4.000 từ (+~300 từ thay thế lore nước).

### 2.2 Ba cấp rừng = ba giới *(giữ v1.0)*
| Cấp | Tên | Map | Người/phòng | Cảnh giới | Áp Chế | Nhãn |
|---|---|---|---|---|---|---|
| 1 | **Hạ Lâm** (Rừng Non) | 256², 3 vòng + Linh Nhãn | Solo/co-op 1–4; Rừng chung 24–40 CCU | C1–C3; Thâm Lâm là cửa vào cho C4 | n=9 (C3 Hậu) ở Bìa và Trung Lâm; không áp ở Thâm Lâm | **MVP** |
| 2 | **Linh Lâm** | 384², 4 vòng | 30–80 | C4–C5 | n=15 | [1.0] |
| 3 | **Thần Lâm** | 512², 5 Thần Vực | 80–200 | C6–C7 | Không trần | [Post] |

Cấu trúc lồng nhau, Phá Giới ở MVP, Phân Thân: giữ v1.0. Cả 5 nhân vật qua Phi Thăng Kiếp I để vào Thâm Lâm (C4) và Viên Mãn ở đỉnh C4 Hậu.

### 2.3 Vòng ngoài → trong (MVP)
| Vòng | Biome | Bonus CT | Mật độ linh khí | Linh Quỹ | Nguy hiểm | **Nước** *(WORLD-03b)* |
|---|---|---|---|---|---|---|
| **Bìa Rừng** | Đồng Cỏ Ven Rừng | +0 | L0 · +3/phút | Sàn 50% | Thấp. Nơi sinh đời mới | 3 cửa suối + **3 Hồ Con** (3×3 sâu, điểm sinh của Oa) + ~20 vũng mưa + **Ao Sương** (Mộng Ấn 1) |
| **Trung Lâm** | Rừng Lá Rộng | +0,15 | L1–L2 · +6/phút | Bình thường | Trung bình | Suối chính (rộng 3, bậc đá) + **Ao Gương** 12×12 (tâm sâu 4×4) — nơi **Lão Quy** ngồi |
| **Thâm Lâm** | Đầm Mục | +0,3 | L2–L3 · +12/phút | Hồi chậm | Cao | **Đầm Mục** ~40×40, lõi sâu ~600 ô (có **Cá Sấu AI**), **3 bến cạn** (điểm nghẽn PvP), Liễu Chết. Tán Thâm Lâm dày **chặn bay** từng đoạn |
| **Linh Nhãn** | — | +0,5 | L4 (Linh Triều) | Giàu | Rất cao | **Mắt Suối** 8×8 (đầu nguồn) |

- Một dòng **Linh Tuyền** chảy từ Linh Nhãn ra Bìa, hai suối nhánh tỏa sang hai phía còn lại → cả 4 góc map có nước. **Tổng ≈3.100 ô ≈ 4,7% map, sâu ≈650 ô (1%)**. Bìa có ≥250 ô nước (sàn SURV để Nòng Nọc sống được C1).
- Ba biome = 3 palette trên 1 tileset (giữ v1.0). Wayfinding: Cột Linh Quang, hạt linh khí trôi về tâm, Giới Bia, **ngược dòng = vào trong**. Không minimap.

### 2.4 Biome & bí cảnh
| Biome | Nhãn | Bí mật → hành động |
|---|---|---|
| Đồng Cỏ Ven Rừng | MVP | **Ao Sương:** vũng có vòng nấm (prop) quanh mép. Soi vũng lúc bình minh sau mưa → bóng mình là **một đốm lửa**: Mộng Ấn 1 *"Ngươi là Mộng Hỏa."* |
| Rừng Lá Rộng | MVP | Dưới rễ Lão Tùng có Thần Bia cũ: Mộng Ấn 2 (giữ) |
| Đầm Mục | MVP | Đêm trăng tròn, bóng người cầm rìu hiện **trên mặt đầm** dưới Liễu Chết: Mộng Ấn 3. Xác phân giải nhanh hơn |
| Rừng Tro | 1.0 | Sau Đại Hỏa, dinh dưỡng ×3, Hoa Phượng Hỏa |
| Trúc Lâm Gió · Vách Đá Rêu · Hang Rễ | Post | — |

Bí cảnh (Mộng Ấn ×3 dạng vignette, Linh Mạch Huyệt, Mộng Cảnh, Lôi Trì, Trùng Sào, Trại Nhân Tu): giữ v1.0.

### 2.5 Lịch thời gian *(giữ v1.0)*
Ngày-rừng 20' (12/2/6) · Mùa 42h · Năm-rừng 7 ngày · Kỷ Nguyên 28 ngày · Đại Kiếp 56 ngày (**MVP 28**). Rừng Non xoay vòng mỗi 14 ngày.

### 2.6 Rừng biến đổi
- **Mộ Linh [MVP]:** nơi sinh linh **C3+** (hạ từ C4+) ngã xuống mọc Hoa Mộ Linh 1 năm-rừng; chạm đọc 1 dòng. Ngoài ra **mọi** xác đã phân giải hết thì chỗ chết mọc prop cỏ/cây con (+1 Dưỡng Chất ô, tối đa 8/vùng, cái cũ tan) *(SURV-04b)*.
- **Hóa Tích** (nơi Viên Mãn) *(WORLD-12b)*: Mộc = cổ thụ hóa đá · Thú = Đá Tru · Trùng = Gò Tổ Cổ · Thủy = Mai đá giữa ao · Vũ = Lông Đá. Mọi người trên server thấy, tối đa 8/vùng, mỗi cái +Linh Quỹ vùng (PROG đặt số). **[A'+]** bản đầy đủ (0,3 t-n); **[A'/B'/C']** fallback: Hoa Mộ Linh **màu vàng** (0,05) [orch].
- Khô Linh hiển thị: vùng nhạt màu, **ao đục, cá nổi** (§5.7).
- [1.0] diễn thế, Mộc Mộ, Hạt Quên · [Post] Thần Vực trôi.

### 2.7 Ngũ Tộc + kẻ ngoài rừng *(WORLD-05b, WORLD-R7-01/02, SURV-30…34)*
| Tộc | Hành | Thế mạnh độc quyền | **Đặc tính tộc** (mọi loài) | Thẻ chọn tộc (≤6 chữ) | Lão NPC | Nhân vật MVP | Động từ riêng | Nhịp |
|---|---|---|---|---|---|---|---|---|
| **Mộc** (mọi cây, cỏ) | Mộc | **Neo & nuôi:** lãnh thổ rễ, hạ tầng, bất tử khi offline, nâng Linh Quỹ | **Tự Dưỡng** | *Bén rễ, nuôi cả vùng* | **Lão Tùng** | **Linh Mộc** | **Bén Rễ** + Vệt Nắng | Chậm, theo mùa |
| **Thú** (thú nhỏ → lớn) | **Kim** (Bạch Hổ) | **Săn:** burst, đuổi, kết liễu | **Khứu Tung** (đánh hơi & bền sức) | *Săn nhanh, cắn quyết định* | Bạch Lộc Tàn Hồn [1.0] | **Lang** | Lang Nha (lao cắn) + đọc vệt | Rình, lao, nghỉ |
| **Trùng** (kiến, bướm, ong…) | **Thổ** | **Số đông & chuyên chở:** bầy Lính, Tha, Mở Xác, **Căn Thương** | **Bầy & Thoát Xác** | *Một mình mà thành bầy* | Nghĩ Hậu Hóa Thạch [1.0] | **Linh Nghĩ** | **Tha** + Xung | Đi rồi về tổ |
| **Thủy** (cá, cua, ếch, nhái, rùa, cá sấu… ở nước, gần nước, đầm lầy) | Thủy (Huyền Vũ) | **Dòng:** ẩn & hồi trong nước, tưới cây, **giữ luân hồi** | **Thủy Tức** (sống dưới nước) | *Nước là nhà và đường* | **Lão Quy** | **Thanh Oa** | **Quăng Lưỡi** + Lặn | Bám bờ, rình |
| **Vũ** (chim, gà, quạ, cú…) | **Hỏa** (Kim Ô) | **Mắt & miệng của rừng:** báo tin, trinh sát, vượt mọi địa hình | **Lăng Không** (bay & nhanh) | *Thấy trước, kêu trước* | **Bạch Hạc** (Sứ giả, đứng trên lưng Lão Quy) | **Linh Nha** (quạ) | **Kêu Báo** + Bổ Nhào + Bới | Bay xa, đậu, báo |
| **Nhân Tu** | — | Mối đe dọa ngoài, tấm gương | — | — | Không có, chỉ dấu vết | — | — | Dấu vết MVP · E5 Post |

- **Khuẩn Tộc bị loại; Khuẩn là yếu tố môi trường.** Phân giải là timer của rừng (§5.5), "giữ luân hồi" thuộc **Thủy/Lão Quy**. **Nấm không thuộc tộc nào**: *"da của Linh Mạch"*, mọc ở chỗ mạch trồi hoặc xác đang tan; prop + đồ ăn môi trường (No nhỏ); **Tơ Nấm** là nền cộng sinh của cây [1.0]. Codex: *"Nấm không mộng nên không nhớ. Nó chỉ làm sạch."* Thấy vòng nấm = gần Linh Mạch hoặc có xác vừa chết.
- **Linh Thử** = Tiền Thân FTUE + AI (con mồi, Hạt Quên [1.0]). AI mang nhãn tộc: Diều hâu, Quạ Linh → Vũ · Sâu Lửa, kiến AI → Trùng · cá, **Cá Lóc Linh, Cá Sấu** → Thủy · Báo Bóng Đêm, Hươu → Thú.
- **Luật đặt tên:** NPC không trùng loài chơi được của tộc mình (Lão Quy là rùa ≠ Oa ếch; **Bạch Hạc** ≠ Nha quạ — hạc không có trong roadmap chơi được). **Một Hành mỗi tộc:** Hành thuộc về thân, không thuộc nhánh Đạo Lộ. **Vũ = Hỏa qua Kim Ô** (quạ ba chân trong mặt trời).
- **Vũ Tộc là mắt và miệng của rừng:** Bạch Hạc báo cho cả rừng (sự kiện, 24h); Nha báo cho bầy (Kêu Báo, vài giây).
- Không làm hệ danh tiếng phe.

---

## 3. Core Loops — owner: SURV
| Tầng | Thời gian | Vòng lặp | Căng → Thả |
|---|---|---|---|
| **Moment** | giây | Theo **động từ tộc**: Mộc bắt Vệt Nắng/kéo rễ · Lang đọc vệt → lao · Nghĩ ra lệnh Xung/Tha · Oa Quăng Lưỡi → Lặn · Nha cất cánh → Kêu Báo → Bổ Nhào | Kẻ săn xuất hiện → thoát vào Nơi Trú/nước/trời/bụi |
| **Activity** | 3–10' | Săn, trữ, tha về tổ, tưới cây, trinh sát, tranh Linh Mạch | Đi xa Nơi Trú → về |
| **Session** | 15–60' | Mộng Báo → 2–3 Cơ Duyên → vòng chính → **mốc Đạo Lộ** hoặc Đả Tọa → Bế Quan | Đêm, sự kiện → Đả Tọa |
| **Đời** (mới) | ~4,6–5,2h (Mid) | C1 → mốc chọn M1…M6 → **Kiếp Viên Mãn** C4 → chọn Đạo Chủng → đời mới, gợi ý tộc chưa thử | Chết giữa đường → Trung Ấm → đời mới ≤20s |
| **Campaign** | tuần | Viên Mãn nhiều tộc → mở ô Đạo Chủng 2/3 · Đại Linh Triều hằng tuần · Đại Kiếp cuối chu kỳ | Đại Kiếp: nghi lễ, Biên Niên, Thần Bia |

Tension graph: mỗi 20' có ≥1 đỉnh áp lực >60 và 1 đáy <25.

---

## 4. Ngũ Tộc: nhân vật & cách chơi — owner: SURV (cơ chế) · PROG (số) · WORLD (tên)

### 4.1 Lộ trình loài *(WORLD-R7-04, PX-08b)*
**MVP (cả 5 đầy đủ C1–C4 + Viên Mãn):** Linh Mộc · Lang · Linh Nghĩ · Thanh Oa · **Linh Nha** (**[C']** Nha ra đợt 2 tuần 58). U1: C5 cho cả 5. 1.0: loài thứ 2 đầu tiên (**Linh Thử** chơi được; ứng viên: Linh Kê, Phong). Thứ tự các loài sau do PX xếp theo KPI.

| Tộc | Roadmap loài (tên trong game: "chất") |
|---|---|
| **Mộc** | **Linh Mộc** (cây gỗ, neo vùng, toàn năng) · Hương Thảo (hương xua trùng, hồi phục) · Ma Vân Đằng (dây leo quấn trói) · Thiết Mộc (vỏ sắt, chậm, trụ) · Tùng (xanh qua Đông, chịu lạnh) · Bách (trường thọ, rễ sâu) · Nắp Ấm (bẫy nuốt trùng — ăn chủ động là nội tại riêng) · Trúc (lớn vọt, rỗng ruột) · Si (rễ phụ lan) · Liên/sen (cây sống trong nước) |
| **Thú** | **Lang** (săn đuổi, kết liễu) · Linh Thử (nhỏ, đào hang, trữ hạt) · Hồ/cáo (mưu mẹo, giả chết) · Lộc (chạy xa, gạc húc) · Trư/lợn rừng (ủi đất, lì đòn) · Hầu/khỉ (leo tán, ném quả) · Hùng/gấu (ngủ Đông, đập mạnh) · Báo (ẩn đêm, vồ một đòn) |
| **Trùng** | **Linh Nghĩ** (bầy đàn, tha về tổ) · Phong/ong (thụ phấn, chích đàn) · Điệp/bướm (rắc phấn, đổi rừng) · Thiền/ve sầu (ngủ đất, Thoát Xác) · Đường Lang (rình, chém kép) · Huỳnh/đom đóm (sáng đêm, dẫn đường) · Tri Chu/nhện (giăng tơ, bẫy chờ) · Ngô Công/rết (độc, chui đất) |
| **Thủy** | **Thanh Oa** (lưỡng cư, lưỡi kéo) · Linh Cáp/nhái (nhỏ, nhảy xa, độc da) · Linh Lý/cá chép (Vũ Môn → Giao Long) · Giải/cua (càng kẹp, đi ngang bờ) · **Miết**/ba ba (giáp mềm, cắn giữ — thay "Linh Quy" để không trùng Lão Quy) · Thiện/lươn (luồn bùn, trơn thoát) · Ngạc/cá sấu (phục kích bờ, đỉnh xích) |
| **Vũ** | **Linh Nha**/quạ (trinh sát, ăn xác, báo) · Linh Kê/gà rừng (bới đất, gáy, bay ngắn) · Tước/sẻ (đàn nhỏ, nhanh nhẹn) · Yến/én (bay nhanh nhất, theo mùa) · Thúy Điểu/bói cá (lao nước, khắc Thủy) · Hiêu/cú (săn đêm, bay im) · Ưng (bay cao, vồ con mồi) |

### 4.2 Ba lớp bản sắc: khung chung → đặc tính tộc → nội tại & động từ nhân vật *(SURV-12b, SURV-30…34, PROG-R7-03, WORLD-R7-01/03)*
**Khung chung (phần lớn code/UI):** controller mặt đất (trừ Mộc), HUD 4+1, No/Thể Lực, Director, **Nơi Trú**, Trung Ấm, Sinh Năng, Trọng Thương, cảnh giới, UI Niên Luân/Đạo Lộ, 3 nút kỹ năng (BN1, BN2, A1 → A1 Thăng ở C4), **hệ tầng Z** (Đất / Không / Đáy nước). Lore: *"Cùng một Mộng Hỏa, khác thân thể."*

**Đặc tính tộc** (áp cho **mọi loài** trong tộc, kể cả loài sau MVP):
| Tộc | Đặc tính | Lore | Luật (số theo SURV, giới hạn theo PROG) |
|---|---|---|---|
| Mộc | **Tự Dưỡng** | *"Cây không săn: nó uống đất và nuốt nắng."* | Không có No. Dinh dưỡng = Thủy + Quang Tinh + Dưỡng Chất (§5.3); tu vi từ quang hợp + hút đất. CT thụ động chỉ khi online, Ánh Sáng ≥40% và Thủy ≥30. Đổi lại: bất động, chịu hạn/bóng râm |
| Thú | **Khứu Tung** | *"Thú đọc rừng bằng mũi; máu là chữ viết rõ nhất."* | **Đánh Hơi** (giữ 1s, thấy vệt máu/xác/mùi trong tầm theo loài — Lang 12 ô, Thử 8, Lộc 6 — trong 10s, CD 20s; nước/mưa xóa vệt) · Thể Lực hồi ×1,25 khi No ≥60 · Kết Liễu kẻ Trọng Thương nhanh ×1,5. Đổi lại: No decay cao nhất trong nhóm cùng cỡ |
| Trùng | **Bầy & Thoát Xác** | *"Trùng chết đi một lần mỗi khi lớn lên, để lại cái vỏ cho rừng."* | **Bầy + Tha** (số Lính theo loài) · **Thoát Xác**: mỗi lần đột phá cảnh thành công hồi 100% HP, xóa debuff, miễn sát thương 1,5s; vỏ cũ rơi tại chỗ thành đồ ăn (+No) cho tộc khác · Đông: ở Tổ No ×0,5 |
| Thủy | **Thủy Tức** | *"Với Thủy tộc, mặt nước là trần nhà, không phải bức tường."* | Thở, ăn, tu được dưới nước sâu (§5.8). Lên cạn có **Ẩm** theo loài (cá 0 — chỉ quẫy ≤2s · ếch/nhái 10' · cua/rùa/cá sấu 20'). Không oxy, không chết đuối |
| Vũ | **Lăng Không** | *"Chim là mắt của rừng vì nó đứng ở chỗ không ai đứng được."* | **Bay thật** trên tầng Không (§4.2a) + tốc bay nhanh nhất game (7,0 ô/s) |

**"Chất" của từng nhân vật MVP** (nội tại = 1 passive luôn bật; luật PROG: **không cộng CT; tấn công ≤+2% dps, phòng thủ ≤+10% ehp ở C4 Hậu**; nội suy theo 12 tầng):
| Nhân vật | **Nội tại riêng** | Động từ riêng | Phụ (cắt trước nếu thiếu ngân sách) | Nhịp | Nỗi sợ chính | Công cụ chống |
|---|---|---|---|---|---|---|
| Linh Mộc | **Niên Luân Ký** *"Mỗi mùa đông qua đi để lại một vòng gỗ."* — mỗi ngày-rừng (≥20' online) không bị Đổ: +1 vòng, mỗi vòng +1% Thân max (trần 3 → 10% từ C1 Sơ → C4 Hậu). Bị Đổ mất ½ số vòng | Bén Rễ, Vệt Nắng | — | Chậm, theo mùa, cả khi offline | Hạn, sét, bị Đổ | Gai/Độc AoE, Khế ước Kiến, Tưới của Oa |
| Lang | **Cắn Giữ** — đòn thường làm chậm mục tiêu 1,5s (4 → 10%); các hiệu ứng chậm lấy giá trị lớn nhất, không cộng | Lang Nha + đọc vệt Khứu Tung | — | Đói → rình → lao → nghỉ | Hết No giữa Đông, bị Nha làm lộ, mồi bay mất | Hang, ăn xác Mở |
| Linh Nghĩ | **Hy Sinh** — Lính chết trong 6 ô: Hậu hồi 2 → 4% HP (CD 3s mỗi Lính) | **Tha** + Xung (2 Lính ở C1, 3 ở C2; Lính tốn No) | Ăn tại Tổ No ×1,25 | Hub–spoke | Gai AoE, nước tách bầy, Nha Bổ Nhào vào Lính | Tổ, Mở Xác, Căn Thương (C3), Thoát Xác |
| Thanh Oa | **Nhựa Da** — kẻ cận chiến trúng Oa nhận độc 4 → 10% Công của Oa trong 2s | **Quăng Lưỡi** + Lặn (C1 Nòng Nọc chỉ ở nước; C2 rụng đuôi lên bờ) | Tưới (tiêu Ẩm) | Bám nước, ra cạn có tính giờ | Khô (Ẩm), Cá Lóc/Cá Sấu AI, bầy Nghĩ giữ bờ | Đáy nước cắt đuôi, Hồ Con |
| Linh Nha | **Ký Diện** *"Quạ không quên một khuôn mặt, và nó kể cho cả bầy."* — kẻ gây sát thương lên Nha bị **Ghi Mặt** 3': Nha và party thấy kẻ đó trên Thần Thức khi trong 20 ô. Chỉ tiện ích, không cộng sát thương [orch] | **Kêu Báo** + Bổ Nhào + **Bới** | Bới | Bay xa, đậu cành, báo tin | HP mỏng, Diều hâu, Oa ở bờ, giông | Bay, Đậu trên Tán đồng minh, Thần Thức |

- Không nhân vật nào có quá 3 thanh động (HP/No/Thể Lực + tối đa 1). Mỗi nhân vật có **một động từ solo** (Oa kéo mồi, Nha thấy Linh Hạch, Nghĩ Mở Xác) để vai không phụ thuộc tộc khác có mặt.
- **Vignette mở đầu đời** ≤3s + 1 câu hint lần đầu vào tộc: Mộc *"Kéo rễ về chỗ đất ẩm."* · Lang *"Giữ để ngửi. Máu để lại vệt, nước xóa vệt."* · Nghĩ *"Mang về tổ. Tổ nhớ mọi thứ ngươi mang."* · Oa *"Ở cạn da ngươi khô. Nước là nhà, là đường."* · Nha *"Kêu một tiếng: bầy ngươi thấy, kẻ rình cũng lộ."*

### 4.2a Lăng Không: luật bay trong top-down 2D *(SURV-31, PROG-R7-04, PX-30/32)*
| Luật | Số |
|---|---|
| Tầng | **Đất / Không** là trạng thái rời (1 bit netcode, không có độ cao liên tục). Khi bay sprite ×1,15, **bóng dưới đất luôn hiện với mọi người**, vòng chỉ tầng |
| Mở khóa (Linh Nha) | C1 *Hoàng Khẩu*: chỉ nhảy/vỗ cánh ngắn (lướt 4 ô, 60 Thể Lực, CD 20s) · **từ C2 *Ly Sào*: bay thật** |
| Cất cánh | 0,6s, −20 Thể Lực, **trúng đòn thì bị ngắt**. Hạ cánh 0,4s, vòng báo trước tại điểm đáp. Đáp xong phải đứng đất ≥3s mới cất cánh lại |
| Thể Lực khi bay | −8/s, **không hồi**. Bay tối đa (trần cứng MVP): C2 9s · C3 12s · **C4 15s** (63 / 84 / 106 ô). Thể Lực về 0 → **Rơi**: choáng 1s, −5% HP max |
| Tốc bay | 7,0 ô/s (×1,10, trong trần ±15%), bỏ qua địa hình (bụi, nước, rễ), **không qua Giới Bia, bị chặn bởi Tán dày Thâm Lâm** |
| Khi bay | **Không ăn, không hồi HP, CT ×0, không đánh thường, không ẩn, không vào Nơi Trú/Bế Quan**. Tầm bị phát hiện ×1,5. Kêu Báo khi bay ping cả hai chiều |
| Đánh từ trên không | Chỉ **Bổ Nhào** = hạ cánh lên mục tiêu (×1,4 Công, choáng 0,8s, kháng choáng 6s). C4 A1 Thăng: lao 5 ô, 1,6×Công. Muốn gây sát thương phải xuống đất |
| Đậu | Ở node **Cành** (cây lớn, Tán người chơi Mộc, Liễu Chết): hồi Thể Lực +15/s (×1,5 trên Tán đồng minh), ăn quả/sâu trên Tán, CT ×0,5. Lính Nghĩ leo Cành được; Gai Bạo của cây đối địch trúng chim đang đậu. **[B']** bỏ đậu cành |
| Ai đánh được kẻ đang bay | Diều hâu AI (ở tầng Không, ưu tiên mục tiêu bay ×2) · Vũ khác đang bay · đòn tầm xa (Quăng Lưỡi → Ướt, Toan Dịch) · Gai/Độc AoE khi bay qua Tán đối địch. Cận chiến (Lang) chỉ trúng lúc cất/hạ cánh. Trúng đòn ≥6% HP max khi bay → buộc hạ cánh, choáng 0,4s, −30 Thể Lực |
| Cấm | Mọi hệ số "×X sát thương lên kẻ bay" (với ×1,25 thì Ω = 1,95 > 1,60) [orch: bỏ đề xuất "+30% khi cất/hạ cánh"; thay bằng cửa sổ ngắt + cận chiến chỉ trúng lúc đó] |
| Thời tiết | Mưa: Thể Lực bay ×1,5; Ướt thì không cất cánh. Giông: Thể Lực ×2, **sét ưu tiên mục tiêu bay** trong 8 ô (−15% HP max) |
| Chống "trời bất tử" | Director: Vũ ở trên không >50% thời gian trong 3' → thêm 1 Diều hâu (trần 2/người). Linh Hạch, Quả Ước, Nơi Trú, mốc tu đều ở dưới đất |
| Fallback (cổng tuần 8) | "Bay" = lướt dài 10 ô + Đậu; fallback cuối: 1 tầng "Tán thấp", ≤8s mỗi lần |

Sim D (PROG): thấy Lang từ ≥8 ô thì thoát; Lang ở ≤6 ô (Ẩn Phong) thì Lang Nha ngắt được cất cánh. **Bay là công cụ thoát cần đọc tình huống, không phải nút thoát chắc chắn.**

### 4.3 Linh Mộc: chơi cây *(giữ v1.0, sửa những chỗ dưới)*
- HP 3 lớp (Tán/Thân/Tâm Rễ), Đổ, Mộc Tàn 120s, TTK (1 Lang cùng tầng 43–54s…), Plant Pressure Map, session mẫu: **giữ v1.0**.
- **Tâm Rễ chỉ nhận Căn Thương**: nay từ **Linh Nghĩ** (thay Độn Thử), lửa, rễ đối thủ, hạn, sét kiếp (§4.8).
- **Động từ:** Bắt Vệt Nắng · Vươn rễ · Gai Bạo · Độc Tiết · **Gieo hạt / Mầm Con** (bỏ vai "Neo" vì Hậu Duệ đã bỏ; Mầm Con vẫn là cây non AI mở lãnh thổ) · Quả Ước · **Khế ước Kiến** (C2, tối đa 2 tổ; swarm dùng chung với Linh Nghĩ) · **Linh Thức lite** (C2; **[B'/C']** chỉ do thám) · A1 **Vỏ Cứng** (C3) → **Thiết Bì** (C4). Hóa Hình Mộng → **[U1]**.
- **Mộc gồm cỏ:** cỏ nền là tile; **Bách Thảo** là 1 trong 3 nhánh Đạo Lộ (§6.4): cây chọn mọc thấp, lan thành thảm. Vật phẩm **Linh Thảo** (Thiên Tài Địa Bảo) giữ tên.
- Plant Pressure: "Linh Thử gặm chồi" → **Thử AI gặm chồi/Mầm**; "Rễ tới suối" → rễ tới suối hoặc nhờ **Oa Tưới**.

### 4.4 Lang *(giữ v1.0)*
Joystick, vuốt để né. Tốc 6,0 ô/s. Thịt trong kho thối sau 10' (15' nếu Nghĩ Tha vào). TTK Lang vs Lang 7,5s. Đặc tính **Khứu Tung** + nội tại **Cắn Giữ** (§4.2). Hang = Nơi Trú. Lang không chạm được kẻ đang bay — phải canh cửa sổ cất/hạ cánh.

### 4.5 Ba nhân vật mới (đầy đủ C1–C4) *(PROG-10, PROG-R7-01, SURV-01b, 06b, 12b, R7)*
**Linh Nghĩ (Trùng).** Hậu (nhân vật người chơi) + Lính. Lính 12% HP Hậu, hồi sinh ở Tổ 20s hoặc tại chỗ mất 6 No; Lính không vào nước nông. Công hiệu dụng = Công Hậu × (1 + 0,15 × Lính sống) → ×1,45 với 3 Lính. Kit: BN1 **Xung** (bầy đánh 1 mục tiêu 4s, Lính ×1,5, CD 10s) · BN2 **Toan Dịch** (nón 3 ô, 0,8×Công, chậm 20%, CD 12s; trúng được kẻ đang bay) · A1 **Đục Rễ** (C3: trên cây đang Mộc Tàn = Căn Thương §4.8; trên đất = đường hầm tới mục tiêu ≤4 ô, sau 1s nổ 1,2×Công AoE 1,5 ô, chậm 30%/2s, CD 14s) → **Đục Rễ Thăng** (C4: 1,5×Công, chậm 40%; có ≥3 Lính thì trói 0,5s). Thêm **Mở Xác** (kênh 6s: xác phân giải trong 45s, Lang ăn không Trúng Độc). **C4 — Giữ bến:** chiếm 1 trong 3 bến cạn Đầm Mục; xác ở Đầm tan nhanh nên Mở Xác + Tha cho CT cao nhất. Độ kiếp Viên Mãn ở Tổ.

**Thanh Oa (Thủy).** C1 **Khoa Đẩu** (nòng nọc) chỉ sống ở nước, ăn tảo/xác chìm; C2 rụng đuôi lên bờ, đổi sang ăn côn trùng. Kit: BN1 **Quăng Lưỡi** (4 ô, 1,0×Công; **kéo** mồi AI/thức ăn/Linh Hạch; trúng người chơi: **chậm 40% trong 1s, không kéo** — kéo người để U1 sau khi test netcode; trúng kẻ đang bay → Ướt) · BN2 **Nhảy Vọt** (4 ô; đáp xuống nước thì đục nước 3 ô 4s, kẻ trong vùng mất dấu Oa; CD 12s) · A1 **Lưỡi Độc** (C3: lưỡi 5 ô, 1,3×Công + độc 30%/3s, CD 10s) → **Lưỡi Độc Thăng** (C4: 1,5×Công, độc 45%/4s; dùng trong 1,5s sau khi trồi lên thì tầm +1 ô). Vai party: ở nước nông, đồng minh trong 3 ô hồi 0,5% HP/5s. **C4 — Chủ Đầm:** tu ở mặt nước lõi Đầm Mục, săn cá; áp lực Cá Sấu AI và bầy Nghĩ giữ bến. Độ kiếp phải lên bến/nông (sét ×1,25 dưới nước) nên bị lộ.
- **Ẩm** (Oa trên cạn): 100 → 0 trong 10' (−1/6s); đêm ×0,5, mưa ×0, Hạ ×1,25. Ngưỡng 100–40 / 39–15 / 14–1 / 0. Cr: Thể Lực max −30%. 0: −1% HP/5s, Tốc ×0,85 (chết sau ~500s). Nước nông +10 Ẩm/s. Fallback nếu phiền: bỏ thanh, Tốc ×0,85 sau 5' trên cạn.

**Linh Nha — quạ (Vũ).** *(thay Linh Kê; Kê lùi về roadmap 1.0, dùng lại thiết kế cũ)* Kit: BN1 **Lăng Không** (nút cất/hạ cánh, §4.2a; C1 chỉ vỗ cánh lướt 4 ô) + **Bổ Nhào** khi hạ cánh lên mục tiêu (×1,4, choáng 0,8s, kháng choáng 6s) · BN2 **Kêu Báo** (ping 20 ô 8s cho party; solo: thấy Linh Hạch trên xác trong 20 ô; làm lộ Thú đang ẩn) · A1 **Mổ Liên Hoàn** (C3: 3 mổ × 0,6 Công) → **Bổ Nhào Thăng** (C4: khi đang bay, lao xuống 5 ô, 1,6×Công, kích choáng ngay; dưới đất thành 4 mổ). Động từ **Bới** (giữ 2s: 40% sâu +6 · 30% hạt +8 · 30% không có gì; ô xới thành **Đất Xới** 60s, +1 Dưỡng Chất, CD 3'/ô). Quạ ăn xác: xác tươi +12 No. Nở trong ổ trên **Cành/Tán đồng minh**. Từ C3 *Phản Bộ*: mớm mồi cho đồng minh (+No). **C4 — Mắt của Đầm:** trinh sát Linh Mạch/Linh Hạch, Bổ Nhào kết liễu; Đầm trống tán nên bay bị lộ, Diều hâu C4, sét giông. Độ kiếp Viên Mãn ở đất dưới Tán (độ kiếp khi đang bay: sét ×1,5).

### 4.6 Ma trận Ngũ Tộc: sinh, khắc, cộng sinh *(SURV-03b, WORLD-06b, PROG-12)*
**Hành:** Mộc · Vũ = Hỏa · Trùng = Thổ · Thú = Kim · Thủy.
**Sinh:** Mộc → Vũ → Trùng → Thú → Thủy → Mộc. **Khắc:** Mộc ⊣ Trùng ⊣ Thủy ⊣ Vũ ⊣ Thú ⊣ Mộc.
**Mỗi tộc:** nuôi 1, được nuôi 1, khắc 1, bị khắc 1 → không tộc nào thống trị. Khắc là **cơ chế tình huống** (phải gần nước, phải có Lính, phải đang lướt), không phải hệ số luôn bật. Tooltip "sinh" viết bằng **vật chất**.

| Cặp | Loại | Tooltip | Cơ chế đo được (MVP) | Cộng sinh | Mức |
|---|---|---|---|---|---|
| Mộc → Vũ | Sinh | *Hạt rụng nuôi chim* | Quả Ước: Nha +15 No. Nha nở và **đậu trên Tán đồng minh** (hồi Thể Lực ×1,5) | Nha ăn sâu trên Tán: bầy sâu AI −50% | data |
| Vũ → Trùng | Sinh | *Đất bới nuôi bầy* | **Bới** → Đất Xới 60s: lộ sâu/hạt, Nghĩ ăn ở ô đó +6 No, Tha nhanh hơn | — | data |
| Trùng → Thú | Sinh | *Xác mở nuôi thú* | **Mở Xác**: xác phân giải 45s, Lang ăn không Trúng Độc | Nghĩ Tha thịt vào Hang Lang: thối 10' → 15' | **thật [A']** |
| Thú → Thủy | Sinh | *Xác chìm nuôi nước* | Xác ≤2 ô từ nước: phần Đất +3% Linh Quỹ (thay 2%) và +1 bầy cá (trần 3/ao). Xác chìm là thức ăn của Thủy ở mặt nước (+8 No) | — | data |
| Thủy → Mộc | Sinh | *Nước dẫn nuôi cây* | Ô nước W = 3 (có sẵn). **Tưới**: Oa tiêu 20 Ẩm, cây đích +15 Thủy, CD 30s | Tán che ao: ao không cạn mùa Hạ | **thật [mọi cấu hình]** |
| Mộc ⊣ Trùng | Khắc | *Nhựa đắng đuổi bầy* | Gai/Độc của cây là **AoE trúng mọi Lính** (với tộc khác chỉ 1 mục tiêu). Bầy sâu AI tự sinh khi Tán >70% | **Khế ước Kiến** (có sẵn) | **thật [mọi cấu hình]** |
| Trùng ⊣ Thủy | Khắc | *Bầy đắp bờ, nước đục* | Quăng Lưỡi trúng Lính trước Hậu. Bầy ≥2 Lính đứng ở bờ: Thủy ở nước nông/mặt nước trong 6 ô **không hồi HP** và hiện trên Thần Thức của Hậu | — | data |
| Thủy ⊣ Vũ | Khắc | *Nước ướt cánh* | Quăng Lưỡi/đòn tầm xa của Thủy trúng Vũ đang bay → **Ướt** (bay tốn Thể Lực ×2 trong 5s; không cộng dồn, miễn 10s sau đó). Vũ rơi xuống nước sâu thì **Đắm**: Tốc ×0,4, −2% HP/s, không cất cánh được 3s. Bổ Nhào hụt mục tiêu ở mặt nước → Ướt | — | data |
| Vũ ⊣ Thú | Khắc | *Tiếng kêu phá rình* | Tầng Không: Lang không chạm được. **Kêu Báo** từ trên không làm lộ Thú đang ẩn, hủy bonus đòn-từ-ẩn. Bổ Nhào choáng 0,8s. Lang phản đòn bằng cách canh cửa sổ cất/hạ cánh | **Kêu Báo ping cho Lang** (party) | **thật [A']** |
| Thú ⊣ Mộc | Khắc | *Nanh vuốt phá thân* | Cào Thân ×0,5, không cho No; Lang là mối đe dọa chính làm cây Đổ (≥40s) | Lang không giẫm Mầm → cây nuôi Quả Ước cho Lang | data |

- **Hệ số sát thương quan hệ (ô Q)** [orch, §6.9]: **PvP ×1** (chỉ có cơ chế) · **PvE (người chơi ↔ AI cùng tộc) khắc ×1,10 / bị khắc ×0,91**. Mục tiêu duel PvP cùng cảnh: mọi cặp thắng 40–60%, bên khắc ≤60%.
- **Ma trận phải sống bằng AI** ở phòng vắng: cơ chế khắc/sinh áp cho cả AI cùng tộc (Lang AI, Diều hâu, bầy sâu, quạ AI, ếch AI, cá, Cá Lóc, Cá Sấu). Chi phí 0 (data).
- Codex: *"Lẻ thì là mồi, bầy thì là đất."* · *"Kẻ khắc ngươi, nếu thành đồng đội, sẽ là mắt của ngươi."*
- **[A']** 4 cộng sinh thật + 6 data · **[B'/C']** 2 cộng sinh thật (Khế ước Kiến, Tưới) + 8 data.

### 4.7 Ai ăn ai (MVP) *(SURV-03b, WORLD-16)*
| Kẻ ăn | Thức ăn (No) | Bị ai ăn |
|---|---|---|
| Linh Mộc | Rễ: xác, Dưỡng Chất; Nắp Ấm bẫy sâu | Hươu AI, Thử AI (gặm), sâu; Lang cào Thân |
| Lang | Thịt +30/cắn · thú nhỏ nguyên con +25 · xác thối +12 (25% Trúng Độc, 0% nếu đã Mở Xác) · Nghĩ Hậu +10 · cá +10–18 | Lang khác, Báo AI |
| Linh Nghĩ | Hạt +8 · sâu +6 · thịt cắn +10 · ô Đất Xới +6 · xác đã Mở +12 · mật Quả Ước · vỏ Thoát Xác | Nha, Oa (Nghĩ lẻ), Lang (Hậu, ít No) |
| Thanh Oa | Nòng Nọc: tảo/ấu trùng +4, xác chìm · Oa: sâu/Nghĩ AI +6 · cá con +10 · Thử AI +18 | Lang (Oa ở cạn/nông), Diều hâu, Cá Lóc/Cá Sấu AI, Nha (Nòng Nọc ở nông) |
| Linh Nha | Hạt +8 · sâu +6 · Quả Ước +15 · **xác tươi +12** · trứng/ấu trùng +6 · Nghĩ lẻ · Nòng Nọc | Lang (khi ở đất), Báo AI, Diều hâu, Oa (Nha non ở bờ) |

**Nguyên tắc:** thú ăn cây nhận ít hơn phần cây mất (lá → thú 40%). Ăn đồng loại được, No ×0,5. Chiều "ăn" độc lập với sinh/khắc.

### 4.8 Căn Thương (thay Độn Thử) *(PROG-16, SURV-04b)*
- Chủ: **Linh Nghĩ**, mở ở **C3** (A1 Đục Rễ).
- **Chỉ chạy khi cây đang Mộc Tàn** (Thân = 0, tức đã có kẻ làm cây Đổ).
- Tốc độ: 0,33% Tâm Rễ/s mỗi Lính (tối đa 3 → 1%/s), Mộc Tàn ×2 → **2%/s ≈ 50s**, khớp mốc v1.0 "3 Lang + Độn Thử, chết thêm 50s". × 0,5^(cảnh cây − cảnh Nghĩ) nếu cây cao hơn. [orch: dùng số PROG; SURV đề xuất Hậu cũng đào 0,35%/s → 77s.]
- Muốn giết cây cùng cảnh cần **≥1 kẻ phá Thân + Nghĩ đào**. Cây offline bất tử, nên không có kịch bản "kiến giết cây lúc offline".

---

## 5. Hệ thống sinh tồn — owner: SURV

### 5.1 HUD 4+1, ≤5 nút
| Nhân vật | 4 chỉ báo cố định | Ngữ cảnh | +1 | Nút |
|---|---|---|---|---|
| Linh Mộc | Vòng HP 3 lớp · Thủy · Quang Tinh · Linh Khí | — | Tu vi | Phòng thủ (bánh xe 2) · Hạt · Quả · Cộng sinh · Linh Thức |
| Lang | HP · Linh Khí · No · Thể Lực | — | Tu vi | Đánh/ăn · 3 skill · (ô Thần Thông khóa tới U1) |
| Linh Nha | như trên | **Chỉ báo tầng** (Đất/Không) + thời gian bay còn lại trên vòng Thể Lực | Tu vi | như trên; **Cất/Hạ cánh dùng ô BN1** (vẫn ≤5 nút) |
| Linh Nghĩ | như trên | **Pip Lính 0–3** quanh HP | Tu vi | như trên |
| Thanh Oa | như trên | **Ẩm** (chỉ hiện khi lên cạn; dùng lại code thanh Thủy của cây) · chỉ báo tầng khi ở Đáy | Tu vi | như trên |

### 5.2 Needs: động vật (C1)
| Nhân vật | HP gốc (n=1) | No decay | Warning đầu |
|---|---|---|---|
| Lang | 420 | −4/phút | 10,2' |
| Linh Nghĩ | Hậu 300 · Lính 36 | −4/phút, mỗi Lính thêm −1/90s | 8,6' (đủ 3 Lính) |
| Thanh Oa | 330 | Nòng Nọc −3 · Oa −4 | 13,7' · 10,2' |
| Linh Nha | 260 | −4,5/phút (bay không ăn được) | 9,1' |
| Linh Thử (FTUE/AI) | 300 | −5/phút | 8,2' |

[orch] Số Nha lấy theo khung Vũ cũ (Kê) của PROG; SURV đã tính sẵn phương án sẻ (HP 220, −5/phút) và cú (HP 280, −4/phút) nếu đổi loài sau này.

Ngưỡng No 100–60 / 59–25 / 24–1 / 0 và hậu quả, Thể Lực, vệt máu <25% HP: giữ v1.0. Mọi warning đầu nằm trong 8–15'. **0 need mới** (Ẩm là thanh ngữ cảnh của riêng Oa).

### 5.3 Needs: Linh Mộc *(giữ v1.0)*
Thủy, Quang Tinh (kho 0–150), Linh Khí, Dưỡng Chất; ngân sách 1 ngày-rừng ≈ +65 Quang Tinh; Ánh Sáng%. Công thức hồi Thủy `6×(1−e^(−W/4))`/phút, W = ô ẩm + 3×ô suối/ao **+ Tưới của Oa (+15/lần)**.

### 5.4 Môi trường × needs *(giữ v1.0, thêm)*
Đêm, Xuân, Đông, Hạ/Thu, Mưa, Giông như v1.0. Thêm: **Giông — người đứng trong nước trong 8 ô quanh điểm sét −10% HP max; rễ trong nước sét ×0,8.** Mưa: Ẩm ×0. Sương mù, lũ: [Cắt].

### 5.5 Sổ Sinh Năng & phân giải *(SURV-04b)*
Khi một người chơi chết, **Sinh Năng = 20 CT** (không đổi theo cảnh, để kill-trading luôn lỗ):
| Phần | CT | Ai nhận | Hệ số |
|---|---|---|---|
| Kẻ ăn | 8 | Chỉ khi ăn/hấp thu (4s, ngắt được) | × m(g) |
| Linh Hạch | 4 | Ai nhặt trước. Quạ AI lấy sau 90s, tự tan sau 30' | × m(g) |
| Đất | 8 | **Rễ (cả thảm Bách Thảo) trong 3 ô** + 2% Linh Quỹ vùng. **Xác ≤2 ô từ nước: chảy vào nước** (+3% Linh Quỹ, +1 bầy cá) | Không nhân |

- **Phân giải = timer môi trường thuần** (Khuẩn là yếu tố môi trường, không tộc nào sở hữu; nấm/vi khuẩn chỉ là prop và chỉ báo). Trùng và Thủy chỉ tăng tốc hoặc chuyển hướng dòng Đất. **Thời gian:** cạn 3' · ô ướt 90s · **Đầm Mục ×0,75** (2'15" / 68s) · đã Mở Xác 45s. Hết thời gian: prop cỏ/cây con mọc tại chỗ (+1 Dưỡng Chất ô).
- **Xác ở nước sâu trôi vào ô nông gần nhất sau 5s**, nên Linh Hạch không bị giấu dưới đáy.
- Con mồi NPC: nhỏ ×0,5, vừa ×1, lớn ×2. Cùng cặp chỉ cho CT 1 lần/30'.

### 5.6 Item sinks & Thiên Tài Địa Bảo *(giữ v1.0)*
Linh Hạch tan 30' · thịt thối 10' · quả rụng 5' · 20% hạt chôn bị quên · rễ teo khi Thủy <30 · TTĐB tan sau 24h. TTĐB: **Linh Thảo**, Huyết Tinh, Lôi Mộc Tâm.

### 5.7 Linh Quỹ & Khô Linh [MVP lite; **[B'/C']** đổi thành mật độ tĩnh]
- Mỗi vùng ~64×64 ô có Linh Quỹ Q (0–100%).
- **Tải** người online: C1–C3 = 1 · C4–C5 = 3 · C6 = 5 · Thần = 0. **Cây** tính 0,5.
- **Sức chứa** = 6 + 1/cây người chơi sống trong vùng (offline 0,5) **+1 mỗi ao sống (≥1 bầy cá), trần +3/vùng**.
- Tải > sức chứa: ΔQ = −35%/h × (tải − sức chứa)/sức chứa. Tải ≤ sức chứa: +4%/h, +1%/h mỗi cây. Mỗi xác +2% (+3% nếu vào nước).
- Sung Linh >60% · Bình 30–60% · **Khô Linh <30%** (CT kẻ tiêu thụ −50%, cây −20%, kill PvP Sinh Năng ×0,5, thú ăn cỏ AI rời vùng, vùng ngả xám, **cá: Sung 3 bầy / Bình 2 / Khô 0 — ao đục, cá nổi**: chỉ báo không cần UI). Bìa sàn 50%.
- Mục tiêu: 4 Lang C4 farm một vùng Trung Lâm → Khô Linh sau ~2h; 2 Lang + 1 cây không bao giờ Khô Linh.

### 5.8 Nước & Thủy Tức: bảng địa hình (bản chốt duy nhất) *(SURV-32, PROG-R7-04)* [orch: hợp nhất]
| Ô | Thủy (Oa…) | Loài cạn (Lang, Nghĩ) | Vũ | Mộc |
|---|---|---|---|---|
| Cạn | Ẩm giảm (hệ số theo loài) · cá **không lên** · Khoa Đẩu không vào | ×1,0 | ×1,0 | — |
| Nước nông | Tốc ×1,2, hồi 1% HP/5s, Ẩm +10/s, không phát tiếng, **CT ×1,15** | ×0,8, tiếng nước lộ vị trí trong 8 ô · Lính Nghĩ không vào · xóa vệt máu/mùi | đi ×0,8, đáp xuống thì Ướt | Rễ vào được, W = 3/ô |
| Nước sâu — **Mặt** (tầng Đất) | Thở, ăn (cá con +10, tảo +4, xác chìm +8), **CT ×0,8**, không tốn Thể Lực. Gợn nước lộ vị trí với kẻ trên bờ trong 6 ô | **Chặn** | Bay qua được, **Bổ Nhào được** | — |
| Nước sâu — **Đáy** (tầng Đáy, nút Lặn) | **Ẩn với mọi tộc khác**, nhưng **không hồi HP, CT ×0,3, Thần Thức 4 ô** | Chặn | Không chạm được | — |
| Hồ Con (Bìa) | Khoa Đẩu C1 ở Đáy không bị Cá Lóc tuần tra (nơi trú C1, chống spawn-camp) | Chặn | như trên | — |

**Luật Lặn / tầng Đáy:** lặn khi giao tranh là kênh 1,5s (vẫn bị chọn làm mục tiêu), để vệt nước đục 4s; 3s sau khi lặn không đánh được. Muốn đánh phải trồi lên Mặt và hiện ≥0,5s; không đánh xuyên tầng. Đang Trọng Thương hoặc bị Kết Liễu: không lặn được. Server **không gửi vị trí người ở tầng Đáy cho người tầng Đất** (chống cheat), chỉ gửi gợn nước khi bơi >×0,8 Tốc.

**Chống "nước bất tử"** (B-SURV-8):
1. **Kẻ săn dưới nước (AI):** **Cá Lóc Linh** ở mọi khối sâu ≥16 ô (1 con/khối, tuần tra Đáy) · **Cá Sấu AI** chỉ ở lõi Đầm Mục (2 con, cảnh C4, đánh cả Mặt lẫn nông) · **[A']** thêm Rắn Nước. Ở nước sâu >4' liên tục thì Cá Lóc chuyển sang Stalking.
2. **Thủy đánh Thủy** dưới nước như bình thường (cùng tầng). Mỗi ao có ≥2 người chơi Thủy thì −1 bầy cá.
3. Nước có đáy: sâu ≈650 ô (1% map). Linh Hạch, mốc tu, Thiên Tài Địa Bảo nằm trên bờ.
4. Độ kiếp dưới nước: sét kiếp ×1,25 → Thủy phải lên bờ/nông để độ kiếp.
5. **Mục tiêu đo:** CT/giờ dưới nước ≤0,8× ở bờ; ở sâu ≤38% thời gian thì CT trong ±10% (sim PROG); ở hẳn dưới nước tới Viên Mãn mất ~435' thay vì 218' (chậm, không cấm).
- Bỏ luật cũ "không combat dưới nước" và "nước sâu CT ×0" của v1.1. Giữ "không oxy, không chết đuối" cho Thủy.
- **[B']** tầng Đáy chỉ đổi màu bằng shader (không vẽ tileset đáy riêng), 2 AI dưới nước; **nước sâu Đầm Mục vẫn giữ** vì Thủy cần lãnh thổ.

### 5.9 Mối đe dọa AI & Ý Chí Rừng *(giữ v1.0, gắn nhãn tộc)*
Hươu Sừng Ngọc (Thú) · Báo Bóng Đêm (Thú; **Diều hâu** là skin cùng archetype, nhãn **Vũ**, nay hoạt động ở **tầng Không**, ưu tiên mục tiêu bay ×2) · Sâu Lửa (Trùng, template cũng dùng cho bầy Lính) · Quạ Linh (Vũ) · **Cá Lóc Linh, Cá Sấu** (Thủy; reskin template Báo, tuần tra tầng Đáy/Mặt) · ếch AI, quạ AI, cá dùng sprite của nhân vật MVP chạy AI decor. Director lite, công thức Áp Lực giữ v1.0, chỉ đổi `số ô cách Hang/Tâm Rễ` → **`số ô cách Nơi Trú`**. Cân bằng sinh thái: thêm *tộc <10% dân số trong 30' → bật ưu ái loài thiếu*.

### 5.10 Nơi Trú, Bế Quan, offline *(SURV-13, giữ §5.9 v1.0)*
| Tộc | Nơi Trú (1 hệ, 5 skin) | Kho | Điểm sinh đời mới |
|---|---|---|---|
| Mộc | Lãnh thổ rễ | Quang Tinh | Ô đất ẩm ở Bìa |
| Lang | Hang | 40 | Hang ở Bìa |
| Nghĩ | Tổ (reskin Hang) | 40 | Ổ trứng ở Bìa |
| Oa | Hồ Con / khối nước sâu (thoát khi đang ở Đáy) | 20 | Hồ Con ở Bìa |
| Nha | Ổ trên Cành / Tán đồng minh (thoát khi đang đậu) | 20 | Ổ trên Tán đồng minh nếu có, không thì cây lớn ở Bìa |

Bế Quan / Nhập Định 30s (60s nếu vừa combat) / miễn decay khi offline / trần tổn thất 24h (≤20% Tán, ≤25% ô rễ ngoài, kho ≤50%; **Tâm Rễ và Thân bất tử**) / **CT offline = 0** / rễ teo khi offline >48h / Mộng Báo ≤10s / catch-up solo 8h (**[B'/C']** rút gọn): **giữ v1.0**.

### 5.11 Survival Pressure Map một đời *(SURV-14)*
| Thời điểm (Mid) | Áp lực | Ai nặng nhất | Đối phó |
|---|---|---|---|
| 0–14' (C1) | No đầu, Diều hâu, đêm đầu | Nghĩ, Nha | Thức ăn dồi dào ở Bìa, Ấu Linh, Nơi Trú gần |
| 14–50' (C2) | Lãnh thổ, Đông, đi Trung Lâm, **bay lần đầu** | Oa (Ẩm khi rời Bìa), Mộc (Thủy), Nha (Diều hâu tầng Không) | Suối chính, Tưới, co-op, đậu Tán |
| 50–116' (C3) | PvP hết Ấu Linh, Kiếp, Huyết Nguyệt | Nha, Oa (HP mỏng) | Trọng Thương, Kêu Báo, Lặn, kiếp ≠ chết |
| 116–218' (C4, **cả 5 tộc**) | Thâm Lâm, Đầm Mục, Kiếp Viên Mãn | Lang (đói), Mộc (Căn Thương), Nghĩ (nước tách bầy), Oa (Cá Sấu AI), Nha (Đầm trống tán, sét) | Hang, phối hợp, giữ bến, Đáy nước, đậu Liễu Chết, chọn thời điểm kiếp |

---

## 6. Tiến trình: cảnh giới, Đạo Lộ, độ kiếp, Viên Mãn — owner: PROG

### 6.1 Thất Cảnh *(giữ v1.0)*
Khai Linh · Luyện Khí · Trúc Cơ · Kết Đan · Hóa Hình · Nguyên Anh · Thành Thần; mỗi cảnh C1–C6 có Sơ/Trung/Hậu. UI "**C3 · Thành Quần · Hậu kỳ**". **Viên Mãn** từ nay chỉ có một nghĩa: hoàn thành cảnh cuối của một đời (không còn là tên tầng thứ 4).

### 6.2 Tên cảnh giới theo loài *(WORLD-15)*
| C | Khung | Linh Mộc | Lang | **Linh Nghĩ** | **Thanh Oa** | **Linh Nha** | Linh Thử [1.0] |
|---|---|---|---|---|---|---|---|
| 1 | Khai Linh | Manh Nha | Ấu Lang | Ấu Nghĩ | **Khoa Đẩu** (nòng nọc) | **Hoàng Khẩu** (mỏ vàng chim non) | Khai Trí |
| 2 | Luyện Khí | Trát Căn | Lang Nha | Lập Sào | **Thoát Vĩ** (rụng đuôi) | **Ly Sào** (rời tổ) | Tàng Thực |
| 3 | Trúc Cơ | Thành Tán | Lang Cốt | Thành Quần | Đăng Ngạn | **Phản Bộ** (quạ mớm mồi nuôi mẹ) | Ẩn Huyệt |
| 4 | Kết Đan | Ngưng Tâm Mộc | Lang Đan | Nghĩ Đan | Oa Đan | Nha Đan | Thử Đan |
| 5 | Hóa Hình | Thụ Nhân ‖ Cổ Mộc Yêu | Lang Nhân ‖ Yêu Lang | Nghĩ Nhân ‖ Yêu Nghĩ | Oa Nhân ‖ Thiềm Yêu | Nha Nhân ‖ Yêu Nha | Thử Nhân ‖ Yêu Thử |
| 6 | Nguyên Anh | Mộc Hồn | Nguyệt Lang Hồn | Địa Sào Hồn | Huyền Thủy Hồn | **Kim Ô Hồn** | Thử Hồn |
| 7 | Thành Thần | Mộc Thần | Lang Thần | Nghĩ Thần | Oa Thần | **Kim Ô Thần** | Thử Thần |

Tên gắn cơ chế: Oa *Khoa Đẩu* sống trong nước, ăn tảo; *Thoát Vĩ* lên bờ được, Ẩm bắt đầu, đổi nguồn tu vi; Nghĩ *Lập Sào* bắt đầu Tha, *Thành Quần* có đủ bầy và mở Căn Thương; Nha *Hoàng Khẩu* chưa bay thật (FTUE an toàn, C1 không có "trời bất tử"), *Ly Sào* mở Lăng Không, *Phản Bộ* mở mớm mồi đồng minh (vai party). Cột Khuẩn, Linh Thảo, Lộc, Trùng [Post] cũ bị xóa (C5–C7 của 3 loài mới chỉ khóa tên ở [Post]).

### 6.3 Đường cong tu vi (nén ×0,5 vì chết = mất trắng) *(PROG-11)*
Công thức giữ: `CT_tầng = CT_cảnh × (0,30/0,33/0,37)`, chỉ số ×1,10/tầng (×1,77/cảnh). Chỉ đổi hằng số CT_cảnh.
| C | CT tầng S/T/H | CT cảnh | Kiếp (CT) | Lũy kế | v1.0 lũy kế | Phút Mid (không chết) | Mở khóa |
|---|---|---|---|---|---|---|---|
| 1 | 6/7/7 | 20 | 3 | 23 | 41 | 14' | BN1, động từ tộc, M1 |
| 2 | 15/16/18 | 50 | 8 | 80 | 156 | 50' | BN2, co-op, Linh Thức + Kiến (cây), M2 |
| 3 | 27/30/33 | 90 | 15 | 185 | 366 | 116' | A1, Căn Thương (Nghĩ), M3–M4 |
| 4 | 42/46/52 | 140 | 23 | 348 | 691 | 218' | Thâm Lâm, A1 Thăng, M5–M6. **Viên Mãn (cả 5 nhân vật)** |
| 5 [U1] | 57/63/70 | 190 | 35 | 573 | 1.141 | — | |
| 6 [Post] | 78/86/96 | 260 | — | 833 | 1.661 | — | |

Ấu Linh "3h hoặc hết C2" thực tế kết thúc ở phút ~50. Hiển thị TV = CT × 10 × 1,25^(n−1) giữ v1.0.

**Vòng đời (sim B, R7: kiếp ≠ chết + Ấu Linh + Trọng Thương C3+):**
| Persona (Lang làm mẫu) | P(đời đầu Viên Mãn) | Giờ / 1 Viên Mãn | Mất TB mỗi lần chết |
|---|---|---|---|
| P1 xe buýt | 83% | 4,6h (~7–8 ngày) | 131' |
| P3 làm vườn | 78% | 4,7h (~1,9 tuần) | 129' |
| Mid | 75% | 4,8h (~1,4 tuần) | 132' |
| P2 kẻ săn | 63% | 5,3h (~1 tuần) | 126' |

**Theo tộc (Mid):** Mộc 81% / 4,6h · Lang 75% / 4,8h · Nghĩ 74% / 4,9h · Oa 75% / 5,2h · Nha 73% / 4,9h. **Viên Mãn lần đầu cả 5 tộc ≈ 24,5h (~7 tuần).**
So sánh núm vặn (Mid, Lang): v1.0 + kiếp = chết → 9%, 25,4h · nén + kiếp = chết → 13%, 10,4h · **nén + kiếp ≠ chết + bảo vệ → 75%, 4,8h**. KPI: **phút mất kỳ vọng mỗi lần Viên Mãn ≤60'** (Mid 44', P2 74' → theo dõi). Rủi ro: không còn đời lite ngắn, nên theo dõi tỉ lệ bỏ game ở đời 2.

### 6.4 Đạo Lộ: 3–5 lựa chọn mỗi mốc (D) *(PROG-08, WORLD-11b, PX-12)*
**Thay** Huyết Mạch, Ấn, Ngộ Đạo draft, Keystone, Notable/Minor, Túc Tuệ của v1.0. **Một template, một UI cho cả 5 tộc.**
- **3 nhánh × 3 Bậc = 9 thẻ / tộc:** mỗi tộc có đúng 1 nhánh **Tồn** (sống sót), 1 nhánh **Sát**, 1 nhánh **Vai** (khuếch đại thế mạnh tộc / hỗ trợ party).
- **1 Thiên Phú tộc** (khuếch đại động từ riêng), có từ mốc 2.
- **Hợp Đạo** (mốc 6, cả 5 nhân vật): 3 thẻ, mỗi cặp nhánh 1 thẻ, cần Bậc II ở cả hai nhánh. (**[B']** Hợp Đạo của Nghĩ/Oa/Nha sang 1.0.)
- **Thâm Hóa** (thẻ đệm chung): chỉ hiện khi bộ thẻ có <3 lựa chọn, tăng thẻ vừa nhận ×1,3 → **mọi mốc luôn có ≥3 thẻ**.
- **Kế thừa:** Bậc k chỉ hiện khi đã có Bậc k−1 cùng nhánh. **Bậc III sửa hành vi của Bậc I** (vd Huyết Bộc kích nổ chảy máu mà Răng Cưa tạo ra). Hợp Đạo nối hai nhánh.
- **Hiệu quả tới hết đời:** (1) không số cố định — mọi giá trị là % Công/HP/CD/tầm hoặc nhân theo tầng; (2) thẻ chỉ bám vào kỹ năng đã mở ở mốc sớm nhất nó có thể xuất hiện (Bậc I: BN1/bị động · Bậc II: BN2 · Bậc III: A1); (3) **A2 là A1 Thăng** (cùng nút), nên không thẻ nào chết vì kỹ năng bị rút khỏi loadout; (4) kiểm tra Lão Hóa: giá trị tương đối của thẻ ở Viên Mãn ≥0,8× lúc nhận.
- **Mỗi bộ thẻ có ≥1 lựa chọn sống sót**: nhánh Tồn luôn được chào ở mốc kế tiếp tới khi đầy Bậc III.
- **Pool cố định, xem trước trong Codex.** Random chỉ ở F. **★ Gợi ý:** nhánh khớp hành vi 10' gần nhất. **Không respec trong đời.**
- Ngân sách mỗi thẻ: Bậc I ≈ +4% · II ≈ +5% · III ≈ +6–8% (dps, ehp hoặc tiện ích tương đương).

**Mốc chọn (Mid):**
| Mốc | Khi nào | Phút | Thẻ hiện |
|---|---|---|---|
| M1 | Vào C1 Trung | 4' | 3 (Bậc I) |
| M2 | Đột phá C1→2 | 14' | 3–4 (+Thiên Phú) |
| M3 | Đột phá C2→3 | 50' | 3–4 |
| M4 | Vào C3 Hậu | 86' | 3–4 |
| M5 | Đột phá C3→4 | 116' | 3–4 |
| M6 | Vào C4 Hậu | 171' | 3–5 (+Hợp Đạo) |
| Viên Mãn | Qua Kiếp Viên Mãn C4 | 218' | (F) |

Áp dụng **cho cả 5 nhân vật**. Khoảng dài nhất giữa hai mốc 55'. Mỗi đời chọn 6 lần. **Số thẻ phải viết: 66** (13 × 5 + Thâm Hóa). Kỹ năng: 3 nút/loài = 15 + 5 bản Thăng = 20 (phần lớn data). Thêm 5 nội tại (§4.2). Tên nhánh theo WORLD, hiệu ứng theo PROG; tên thẻ là tên tạm của PROG, WORLD đặt lại khi viết data (≤2 từ, đoán được tác dụng) [orch].

**UI (PX-12):** vẽ dạng **Niên Luân** (vòng gỗ đồng tâm, mỗi mốc một vòng). Hiện đủ 3–5 thẻ, không vuốt (844×390 pt chứa 5 thẻ × ~150 pt). Mỗi thẻ: tên ≤2 từ + mô tả ≤12 chữ + icon trục + nhãn "Kế thừa"/"Sống sót". **Đặt Trước** (đánh dấu thẻ dự định bất cứ lúc nào, đột phá thì áp tự động, toast 3s "Đổi?") · **Chọn Sau** (đột phá giữa PvP **không bao giờ** bật màn hình chặn; huy hiệu "1 lựa chọn đang chờ") · xác nhận bằng nút riêng (bấm nhầm <5%).

### 6.5 Đạo Lộ: mẫu chi tiết — Lang *(PROG-09)*
**Kit:** BN1 **Lang Nha** (lao cắn 4 ô, ×1,5 Công, CD 12s) · BN2 **Hú** (lộ vị con mồi 20 ô 4s, CD 30s) · A1 **Xé** (C3: ×1,6 + chảy máu 4s = 40% Công, CD 10s) → **Xé Thăng** (C4: ×1,8, chảy máu 6s) · bị động **Đánh Hơi**.
| Nhánh (trục) | Bậc I (từ M1) | Bậc II (từ M2) | Bậc III (từ M3) |
|---|---|---|---|
| **Huyết Lang** (Sát) | **Răng Cưa**: Lang Nha gây chảy máu 45% Công/3s | **Khứu Huyết**: mục tiêu chảy máu hiện trên Đánh Hơi tới 20 ô; đòn lên nó +10% | **Huyết Bộc**: Xé kích nổ phần chảy máu còn lại ×1,5, hồi 30% lượng đó *(kế thừa Răng Cưa)* |
| **Phong Lang** (Vai) | **Dẫn Đàn**: party thấy vệt Đánh Hơi của bạn; đi theo vệt +5% Tốc | **Hú Bầy**: Hú cho đồng minh 12 ô +8% Tốc 4s · solo: mục tiêu lộ chậm 15% 3s | **Lang Vương**: Hú gắn Dấu Săn 5s — party đánh +6%, mục tiêu không vào Hang/Ẩn · solo: Lang Nha −30% CD lên mục tiêu có Dấu |
| **Ảnh Lang** (Tồn) | **Ẩn Phong**: đứng yên/đi chậm 2s ngoài giao tranh thì ẩn khỏi Thần Thức ngoài 6 ô; đòn đầu ×1,3 | **Nuốt Vội**: ăn xác ×2 tốc, mỗi cắn hồi 2% HP | **Kẻ Đơn Độc**: HP <35% → +15% Tốc 4s, xóa đánh dấu, kích Ẩn Phong ngay; CD 60s *(kế thừa Ẩn Phong)* |
| Thiên Phú | **Mũi Sói**: Đánh Hơi (Khứu Tung) 12 → 18 ô, ngửi được vệt của kẻ vừa vào Hang trong 5s | | |
| Hợp Đạo (M6) | Huyết × Phong **Huyết Nguyệt** (chảy máu do đồng minh gây cũng bị Huyết Bộc kích nổ) · Huyết × Ảnh **Bóng Máu** (đòn đầu từ Ẩn Phong gây chảy máu ×2) · Phong × Ảnh **Ảnh Dẫn** (khi bạn ẩn, đồng minh trong 8 ô ẩn ngoài 10 ô) | | |

**Kiểm chứng (sim C):** 43 build khác nhau · mỗi mốc ≥3 thẻ · chênh mạnh/yếu **1,17 solo / 1,11 party** (ngưỡng ≤1,25) · party không có thẻ bắt buộc.
**Build Archetype (Lang):** Huyết Ảnh (Ẩn Phong → Răng Cưa → Bóng Máu; bị Nha Kêu Báo làm lộ, Oa đục nước xóa vệt) · Huyết Bộc (Huyết Lang I–III; thiếu đường thoát) · Sói Cô (Ảnh Lang I–III + Mũi Sói; sát thương thấp nhất) · Đầu Đàn (Phong Lang + Huyết Nguyệt; party ×1,30 dps, solo yếu hơn 8% → thẻ gắn nhãn "Bầy" kèm giá trị solo, đo pick-rate solo).

### 6.6 Đạo Lộ: khung 4 nhân vật còn lại *(PROG-10, tên nhánh WORLD-11b)*
| Nhân vật | Nhánh Tồn | Nhánh Sát | Nhánh Vai | Thiên Phú |
|---|---|---|---|---|
| **Linh Mộc** (full) | **Thiết Mộc**: Vỏ Gai (Gai Bạo phản 15 → 22%) · Nhựa Đắng (Độc Tiết −30% hồi máu đối thủ 6s) · Bàn Căn (Tâm Rễ +40%, Căn Thương lên mình −25%) | **Linh Quả Thụ**: Quả Ngọt (−20% giá, +25% No cho kẻ ăn) · Quả Linh (đồng minh ăn quả +10% Tốc 20s hoặc hồi 8% HP) · Khế Ước Kiến (+1 tổ = 3, kiến gây 0,1 × Công cây/s) | **Bách Thảo** (**cỏ trong Mộc tộc**): Thảm Cỏ (ô rễ mới mọc cỏ, Vươn rễ 20 → 14s/ô, giá −25%) · Cỏ Gai (kẻ địch trên thảm −10% Tốc) · Phản Sinh (Đổ thì Mộc Tàn 120 → 80s, Tán mọc lại từ thảm ×2) | **Rễ Cảm** (báo kẻ đến trong 20 ô). Hợp Đạo: Thảm Gai · Quả Đắng · Vườn Hoang |
| **Linh Nghĩ** | **Chức Diệp**: Hầm Ngầm (chui đất 2s, không bị chọn làm mục tiêu, CD 25s) · Tổ Phụ (+1 tổ phụ: hồi sinh Lính, điểm chui) · Lính Đỡ (**12%** sát thương lên Hậu chuyển sang Lính gần nhất — sửa từ 25% vì cho +33% ehp, gấp 4 ngân sách) | **Toan Nghĩ**: Hàm Thép (Lính +15% sát thương) · Lính Thứ Tư (+1 Lính → ×1,60, HP Lính −15%) · Vạn Nghĩ Xung (Xung 6s, Lính chết trong Xung hồi sinh ngay 1 lần) | **Công Nghĩ**: Vai Rộng (Tha 2 vật, Tốc khi Tha −30% → −10%) · Đường Mùi (vệt mùi +15% Tốc cho đồng minh/Lính, CT từ Tha ×1,2) · Kho Tổ (Lính hồi sinh 20 → 10s, quanh tổ hồi 1% HP/3s) | **Hậu Mẫu** (Lính hồi sinh không tốn No khi No >70%) |
| **Thanh Oa** | **Thiềm Bì**: Da Dày (Ẩm cạn chậm 30%: 10' → 13') · Ngụy Bùn (đứng yên 1,5s ở nông/bùn thì ẩn ngoài 4 ô) · Ngủ Bùn (HP <30% trong nước sâu/bùn: hồi 3% HP/s 4s, CD 90s) | **Độc Oa**: Lưỡi Dài (4 → 5,5 ô) · Nuốt Chửng (Lưỡi lên mồi AI <30% HP thì nuốt luôn; lên người chơi +20%) · Lưỡi Kép (Quăng Lưỡi 2 lần sạc) | **Cáo Thiên**: Dẫn Nước (cây đồng minh trong 3 ô +6 Thủy/phút) · Suối Lành (đồng minh trong 3 ô ở nông hồi 0,5% HP/5s) · Mưa Rào (Nhảy Vọt mang vũng nông 3×3 trong 15s, CD 45s) | **Rung Nước** (cá/ếch AI trong 12 ô báo khi có kẻ đến) |
| **Linh Nha** | **Hộ Sào**: Bới Nhanh (Bới ×1,5, No từ sâu ×1,5) · Diều Hâu! (kẻ cảnh cao hơn/Diều hâu vào 14 ô thì cảnh báo 2s, lần cất cánh kế −50% CD) · Ổ Cành (Bới/đậu 3s tạo Ổ: ẩn tại chỗ, hồi 1% HP/3s) | **Mỏ Sắt**: Mỏ Nhọn (Bổ Nhào ×1,4 → ×1,6 + chảy máu 2s) · Mổ Mắt (đòn thường thứ 3 liên tiếp: mục tiêu −50% Thần Thức 2s, CD 15s) · Liên Hoàn Mổ (Mổ Liên Hoàn ngay sau khi hạ cánh = 4 mổ) | **Viễn Mục**: Mắt Quạ (Thần Thức +15%) · Kêu Xa (20 → 28 ô, ping 8 → 12s) · Kêu Bình Minh (Kêu Báo đầu ngày-rừng: cây trong 8 ô +15 Thủy, đồng minh +10 Thể Lực) | **Lẩn Bụi** (hạ cánh vào bụi thì ẩn 2s) |

[orch] Thẻ Vũ giữ nguyên hiệu ứng PROG viết cho khung Vũ, chỉ đổi tên/động từ sang quạ (Hạ Cánh Đạp → Bổ Nhào, Gáy → Kêu Báo, Sải Cánh → cất cánh); tên nhánh tạm, WORLD đặt lại.

**A1 Thăng & Hợp Đạo (C4, M6) của 3 nhân vật mới** *(PROG-R7-01)* — thứ tự Tồn×Sát · Tồn×Vai · Sát×Vai:
| Nhân vật | A1 → Thăng | Hợp Đạo |
|---|---|---|
| Linh Nghĩ | Đục Rễ → Đục Rễ Thăng (§4.5) | **Hầm Phục** (chui lên từ Hầm Ngầm: Xung miễn phí 2s) · **Mạch Tổ** (Hầm Ngầm nối tổ/tổ phụ ≤20 ô, kênh 2s, CD 90s) · **Đoàn Quân** (Tha về tổ: Lính +8% sát thương 30s, tối đa 2 lần) |
| Thanh Oa | Lưỡi Độc → Lưỡi Độc Thăng (§4.5) | **Phục Bùn** (lưỡi đầu sau Ngụy Bùn/trồi lên ×1,3 + độc) · **Ao Hộ** (Ngủ Bùn hồi cả đồng minh 3 ô 1,5%/s) · **Mưa Độc** (vũng Mưa Rào 10% Công/s, không cộng với Lưỡi Độc) |
| Linh Nha | Mổ Liên Hoàn → **Bổ Nhào Thăng** (§4.5) | **Cánh Che** (HP <40%: Bổ Nhào trúng hồi 6% HP) · **Canh Gác** (Diều Hâu! báo cả party; Kêu Báo trong Ổ không lộ mình) · **Kêu Chiến** (3s sau Kêu Báo, Bổ Nhào lên mục tiêu bị ping choáng 1,0s) |

**Sim A (R7):** mỗi nhân vật 43 build, mốc nào cũng ≥3 thẻ. Chênh mạnh/yếu (solo / party), ngưỡng ≤1,25: Nghĩ 1,21 / 1,15 · Oa 1,14 / 1,08 · Nha 1,16 / 1,08. M_thẻ max 1,31 / 1,26 / 1,26 (≤1,34 của Lang).

→ Yêu cầu "Mộc gồm cỏ" có trong MVP với chi phí 0 loài mới (một cây đi nhánh Bách Thảo chơi như thảm cỏ lan nhanh); các loài cây/cỏ khác (Hương Thảo, Ma Vân Đằng, Thiết Mộc, Tùng, Bách, Nắp Ấm…) theo roadmap §4.1, cùng đặc tính Tự Dưỡng.

### 6.7 Độ Kiếp *(giữ v1.0, sửa)*
| Đột phá | Kiếp | Thời lượng | Thất bại | Nhãn |
|---|---|---|---|---|
| C1→2, C2→3 | Tiểu Kiếp (né lôi) | 60–90s | −10% CT tầng, thử lại ngay | MVP |
| C3→4 | **Phi Thăng Kiếp I** — template lôi + Tâm Ma sao chép 3 nút (BN1/BN2/A1) | 2' | −30% CT tầng + Đạo Cơ Tổn 20' | MVP (cả 5) |
| **Đỉnh C4 Hậu** | **Kiếp Viên Mãn** (template Trung Kiếp) | 2' | như trên | MVP (cả 5) |
| C4→5 · C5→6 | Trung Kiếp · Phi Thăng Kiếp II | 3' · 4' | như trên | U1 |
| C6→7 | Thiên Kiếp (luôn Công, bị sinh vật giết = chết thật, D19) | 10' | — | Post |

- UI gọi kiếp cuối của đời là **Viên Mãn Kiếp**. Ẩn Kiếp/Công Kiếp, Hộ Pháp, công thức độ khó, mục tiêu 60–70% qua lần đầu / ≥95% sau 3 lần: giữ v1.0. **Địa điểm độ kiếp:** độ kiếp dưới nước sét ×1,25, khi đang bay sét ×1,5 → Thủy và Vũ phải xuống bờ/đất để độ kiếp (bị lộ, đúng chủ đích).
- **Kiếp thất bại ≠ chết** (§7.2 L4): sét kiếp và Tâm Ma không đưa HP dưới 10%; thẻ Đạo Lộ đã nhận giữ nguyên. *"Sét đánh gãy, không đánh tắt."* [orch: giữ mức phạt v1.0; PROG đề xuất "lùi về đầu tầng Hậu, CD 10', 3 lần liên tiếp → Đạo Cơ Tổn" làm phương án chỉnh nếu telemetry cần.]

### 6.8 Hóa Hình & Linh Thức *(giữ v1.0)*
Bản Thể [U1] (+10% chỉ số → **phải giảm còn ×1,04** để giữ trần Ω, §6.9) · Nhân Hình [Post] · Linh Thức lite [MVP] → Xuất Khiếu C6 [Post] · Nguyên Thần Bất Diệt [Post]: thoát ra, về Linh Huyệt trong 60s thì không chết (không còn "tính như Hậu Duệ"). Hóa Hình Mộng → **[U1]**.

### 6.9 Công thức sức mạnh & trần hệ số *(giữ v1.0 §6.9, thêm PROG-12)*
- Chỉ số theo tầng, Thủ/DR, `Dmg = Công × hệ số kỹ năng × (1 − DR) × Q × Crit × Mit`, Tốc không tăng theo cảnh (mọi nguồn ±15%), Áp Chế: giữ v1.0 (E cũ của Huyết Mạch được thay bằng **Q**).
- **Ô Q (quan hệ tộc), một hệ số duy nhất** [orch]: PvP **×1** · PvE với AI cùng tộc: khắc ×1,10 / bị khắc ×0,91. Không thẻ, Đạo Chủng hay sự kiện nào nhân thêm vào Q.
- **%HP bỏ qua Áp Chế bị cấm:** mọi hiệu ứng %HP (Căn Thương…) × 0,5^(chênh cảnh) khi người đánh thấp cảnh hơn.
- **Trần tổng Ω** (mọi nguồn ngoài cảnh giới, tấn công): `Ω = M_thẻ × Nội tại × Q × (1 + ĐạoChủng_Sát) × [Bản Thể U1] ≤ 1,60`. MVP max ≈ 1,34 × 1,02 × 1,10 × 1,035 = **1,556** (PvE). **U1: chốt kẹp M_thẻ ≤1,30** khi thêm Bản Thể ×1,04 (ra 1,570).
- **Cấm** mọi hệ số sát thương theo tầng (lên kẻ bay, lên kẻ dưới nước). Không hệ số nào tăng khi ở nước; ô Q giữ nguyên.

| Base (n=1) | HP / Thân | Công | d | Tốc (ô/s) | Thần Thức |
|---|---|---|---|---|---|
| Lang | 420 | 50 | 0,40 | 6,0 | 14 |
| Linh Mộc | Thân 1.260 (Tán, Tâm Rễ 0,5×) | 30 | 0,80 | 0 | 10 (+Rễ Cảm) |
| Linh Nghĩ | Hậu 300 · Lính 36 | 22 (+0,15×/Lính, tối đa 3) | 0,25 | 5,4 | 12 |
| Thanh Oa | 330 | 30 | 0,30 | 5,6 cạn · ×1,2 nông | 14 |
| Linh Nha | 260 | 26 | 0,25 | 6,4 đất · 7,0 bay | 18 (×1,5 tầm bị phát hiện khi bay) |
| Linh Thử (FTUE/AI) | 300 | 26 | 0,30 | 6,6 | 16 |

**Nguồn tu vi (chuẩn 1,0 CT/phút ±10%):**
| Loài | Nguồn chính | Nguồn phụ | Đặc thù | Phương sai |
|---|---|---|---|---|
| Linh Mộc | Quang hợp 45% | Vệt Nắng 20% · rễ/hấp thu 20% | Phản vệ, Quả Ước, cộng sinh 15% | ~16% |
| Lang | Săn 60% | Ăn xác, lãnh thổ 25% | PvP 15% | ~34% |
| Linh Nghĩ | Tha về tổ, ăn hạt/sâu 45% | Mở Xác, phân giải 30% | Căn Thương, Đất Xới 25% | ~23% |
| Thanh Oa | Lưỡi bắt côn trùng/mồi nhỏ, cá dưới nước 45% | Tưới, cộng sinh ven nước 25% | Thoát Sinh, nuốt mồi AI 30% | ~21% |
| Linh Nha | Bới hạt/sâu, ăn xác 40% | Kêu Báo cho đồng minh, thấy Linh Hạch 25% | Thoát Sinh, Bổ Nhào 35% | ~27% |

Hệ số áp lên CT: vùng thấp hơn cảnh ×0,5^chênh, needs, Khô Linh, Đông, AFK ×0,2, **offline 0** (giữ v1.0) · **tầng:** bay ×0 · đậu cành ×0,5 · Thủy ở nông ×1,15 · mặt nước sâu ×0,8 · Đáy ×0,3 · loài cạn không vào nước sâu. PvP theo chênh cảnh (sim R: 1 cảnh — 1 người thấp hơn thắng 15%): giữ v1.0.

### 6.10 Viên Mãn & Đạo Chủng (F) *(PROG-13, WORLD-10b/13b)*
- **Giai đoạn cuối:** cả 5 nhân vật = đỉnh C4 Hậu (~218' Mid không chết). Qua **Viên Mãn Kiếp** = Viên Mãn. *(U1 có C5: Viên Mãn dời theo cảnh cuối của bản đó; Đạo Chủng đã có giữ nguyên.)*
- **Random 3:** pool = mọi thẻ Đạo Lộ đã nhận trong đời (trừ Thâm Hóa); rút **3 trong 6, không lặp, trọng số đều**. Người chơi chọn 1 → **Đạo Chủng**, giữ tên và **trục** của thẻ gốc. Nghi thức **Vớt Chủng**: Lão Quy vớt 3 hạt sáng lên từ nước, chọn 1, hai hạt kia chìm. *"Ngươi đi hết đường rồi. Ta vớt cho ngươi ba hạt. Chọn đi. Ừ."*
- **Đạo Chủng không phải bản sao thẻ** (nếu không, đời mới khởi đầu bằng Bậc III). Nó là **hiệu ứng nhỏ theo trục, dịch theo động từ của tộc đang chơi**:

| Trục | Giá trị (một mức) | Mộc | Lang | Nghĩ | Oa | Nha |
|---|---|---|---|---|---|---|
| **Sát** | +3,5% sát thương | gai, rễ quất | Lang Nha, Xé | Lính | Quăng Lưỡi | Bổ Nhào, mổ |
| **Hộ** | −5% sát thương nhận | Thân, Tâm Rễ | thân | Hậu + Lính | thân | 2s sau khi đáp: ×2 |
| **Sinh** | +8% hồi | hồi Tán, Thủy | hồi khi ăn xác | Lính hồi sinh nhanh | hồi ở nước nông | No từ Bới/xác |
| **Hành** | +5% (trong trần Tốc ±15%) | thời gian Vươn rễ/ô | Tốc chạy | Tốc khi Tha | CD Nhảy Vọt | **thời gian bay** (trong trần 15s) |
| **Thức** | +12% | Rễ Cảm/Thần Thức | tầm Đánh Hơi | Thần Thức | tầm Rung Nước | tầm Kêu Báo |

  25 dòng data, ô nào cũng dịch được; cùng tộc hay khác tộc như nhau. **Bỏ phẩm Sơ/Thâm** vì không còn bản lite (dự phòng: dùng lại phẩm Sơ nếu 1.0 có loài lite). Không bao giờ có hạt nào chỉ làm "chịu đói lâu hơn >15%" (giữ áp lực đầu đời). Tooltip: *"Ý của Truy Huyết, trong thân Oa: Quăng Lưỡi trúng kẻ đang chảy máu…"*
- **Sổ Đạo Chủng (S2)** — vĩnh viễn, sưu tập: ô trang bị **1** (Viên Mãn lần 1) → **2** (sau 3 lần Viên Mãn ở ≥2 tộc) → **3** (sau 6 lần ở ≥3 tộc; **ô 3 chỉ nhận Hành/Thức**). Tối đa 1 Đạo Chủng/trục. Win-rate người có ô 1–2 so với người mới cùng cảnh ≈56% (ngưỡng ≤55%: nếu vượt thì Thâm Sát 3,5% → 3%). Ô 3 không thêm sức chiến đấu. Lore: *"Một Mộng Hỏa chỉ ôm được ba hạt."*
- **Đạo Chủng không mất khi đời sau chết (L1)** — 4/4 đồng thuận ở R3. Lore: Đạo Chủng **chìm trong Ao Gương, Lão Quy giữ hộ**, không nằm trong Mộng Hỏa. *"Thứ ngươi tự lớn lên thì trả lại cho rừng. Thứ rừng đã trả cho ngươi thì nước giữ."* Đời sau vẫn "hoàn toàn mới" về những gì đời đó tự kiếm.
- **Đại Kiếp** kết thúc mọi đời nhưng **không** tính là chết giữa đường (*"Rừng cùng chết, nên không ai chết một mình."*): không mất Đạo Chủng, người chưa Viên Mãn **không** nhận thêm.
- **Nhân vật Viên Mãn:** thành **Hóa Tích** (§2.6) + trang Biên Niên. Không chơi tiếp; chọn tộc mới ngay (≤20s tới khi điều khiển), thẻ hero gợi ý **tộc chưa thử**.

---

## 7. Cái chết: hai cách kết thúc một đời — owner: SURV (luật) · PROG (số) · WORLD (nghi thức)

### 7.1 Một luật duy nhất *(WORLD-10b)*
**"Chết giữa đường, ngươi trả lại cho rừng. Đi hết đường, rừng trả lại cho ngươi."**
| | **Chết giữa đường** (E) | **Kiếp thất bại** | **Cây Đổ** | **Viên Mãn** (F) |
|---|---|---|---|---|
| Luật | Đời mới ở **C1**, không mang sức mạnh nào (cảnh, thẻ, kho, lãnh thổ) | **Không phải chết.** −CT tầng, giữ thẻ | Không phải chết (Thân = 0, Mộc Tàn 120s) | Hoàn thành cảnh cuối |
| Giữ | Sổ Đạo Chủng, Đạo Hạnh, skin, Biên Niên, Codex, Tiền Kiếp Ấn, kiến thức | Mọi thứ | Mọi thứ trừ Tán, 25% CT tầng | + 1 Đạo Chủng mới |
| Thế giới nhận | Sinh Năng 20 CT; kho Hang rơi thành loot 30'; lãnh thổ rễ → Dưỡng Chất; Hang → Mộ Linh; cây/cỏ mọc ở chỗ ngã | — | — | **Hóa Tích** |
| Người chơi thấy | Trung Ấm trên mặt nước, màn **"Ngươi để lại"** | Mây kiếp tan, Đạo Cơ Tổn | — | Trung Ấm biến thể **Vớt Chủng** |

**Bỏ hẳn:** Hậu Duệ, Neo (Mầm-Neo, Huyết Noãn, Ổ Hạt), Ổ Hậu Duệ, Hồi Ức, Túc Tuệ, Đạo Quả meta, Đạo Quả Bàn. **Tiền Thân FTUE không tính là một đời** (*"giấc mộng đầu"*).

### 7.2 Sáu lớp đệm chống mất trắng vô lý *(SURV-09b)*
| Lớp | Luật | Chi phí |
|---|---|---|
| **L0 Ấu Linh** | 3h hoặc hết C2 (thực tế ~50'), cái nào tới trước (D5 giữ) | 0 |
| **L1 Hồn Hộ** | 10' sau mỗi lần sinh mới: kẻ có g≥1 giết được 0 CT, 0 Linh Hạch | 0 |
| **L2 Trọng Thương** (C3+, mọi nhân vật động vật) | Đòn kết liễu **do người chơi** không giết ngay: nạn nhân Trọng Thương 30s (bò 1 ô/s, không đánh/ăn). Kẻ giết phải **Kết Liễu** (kênh 1,5s, ngắt được, lộ vị trí trong 20 ô). Đồng minh cứu (giữ 3s → dậy 30% HP). Hết 30s không bị Kết Liễu → tự dậy 10% HP + Hồn Hộ 60s. AI, đói, Ẩm, thời tiết vẫn giết thẳng. 1 lần/5'. Kết Liễu khi g≥2: +2 Sát Nghiệp | 0,3 |
| **L3 Thiên Đạo Luật** | Giữ m(g). Đánh Úp Kiếp hoặc giết người đang Nhập Định = +1 Sát Nghiệp **bất kể g**, 0 CT, 0 Linh Hạch. **Oán Linh** mới: đời kế của nạn nhân g≥2 có **Mộng Tích đầy** (×2 CT 30' đầu), 1 lần/24h — **chờ người dùng xác nhận** (Q-B) | 0,05 |
| **L4 Kiếp thất bại ≠ chết** | Sét kiếp và Tâm Ma không đưa HP dưới 10%. Chỉ chết khi bị người chơi/AI đánh về 0 (L2 vẫn áp). Director không spawn kẻ săn trong 30 ô quanh vòng kiếp và 60s sau kiếp | 0,05 |
| **L5 Rớt mạng không phải chết** | Nhập Định giữ, nhưng Trọng Thương áp **ở mọi cảnh**, sát thương AI ×0,5, kẻ giết 0 CT + Sát Nghiệp | 0,05 |
| **L6 Cây offline bất tử** | Giữ §5.10 | 0 |

**Hazard mục tiêu (telemetry tách theo nguồn × cảnh):** C1–C2 ≤0,15 chết/giờ · C3 ≤0,10 · C4 ≤0,08. Nếu hazard C3+ do PvP >0,06/giờ thì siết L2/L3 trước khi đụng needs. **Death spiral check:** đời mới ở Bìa (sàn Linh Quỹ 50%, Ấu Linh, Hồn Hộ); kẻ vừa giết mình không lấy được gì trong 10'.

### 7.3 Khởi động lại & nghi thức *(SURV-09b, WORLD-02b, PX-13)*
- Chết → điều khiển đời mới **≤20s**. Trung Ấm lần đầu 45s, sau đó 8–12s, bỏ qua được. Trong ≤90s: chọn tộc (5 thẻ) + chọn điểm sinh. **Lựa chọn Đạo Lộ đầu tiên ≤5'** (M1 ở phút 4).
- **Trung Ấm trên mặt nước:** xác chìm, đốm sáng tản ra. **Cái chết đọc được:** nguồn, cảnh `g`, đòn cuối (vd "Ẩm 0 trong 4'12s"), **"Ngươi để lại"**: Mộ Linh tại Đầm Mục, 8 CT cho đất, cây con nơi ngã, Linh Quỹ +x%, trang Biên Niên, +N Đạo Hạnh.
- **Lão Quy** (thay Bà Khuẩn): rùa già mai phủ rêu, rắn nước cuộn trên mai (Huyền Vũ), ngồi trên tảng đá giữa Ao Gương. Giọng chậm, câu ngắn, hay "ừ", chỉ dùng trường nghĩa nước (không dùng *nấm, bào tử, ủ, mục*). Chào theo Tâm Hướng: Sinh *"Nước trong khi ngươi tới. Ngồi đi."* · Trung tính *"Ừ. Lại một đốm lửa biết bơi."* · Sát *"Nước đục theo bước ngươi. Ta vẫn nhìn."* · với Oa *"Lại một đứa còn đuôi. Bơi đi, ta không cõng đâu."*
- **Pool Trung Ấm 40 câu** (~10 nhóm × 4). Mẫu: bị Lang ăn *"Răng nó nhớ ngươi lâu hơn ngươi nhớ nó. Ừ."* · bị Vũ giết *"Trời cũng biết đói. Lần sau, nhìn lên."* · đói *"Bụng rỗng thì nước cũng lạnh."* · cây chết hạn *"Rễ ngươi khát từ lâu. Nước không giận ai."* · Oa cạn Ẩm *"Ngươi đi xa nước quá. Nước vẫn chờ."* · Nghĩ mất bầy *"Một con kiến không chết. Chỉ là tổ quên nó."* · mang Sát Nghiệp *"Nước rửa được máu. Không rửa được tên."* · lần đầu mất trắng C3+ *"Đừng tìm lại. Nhìn chỗ ngươi ngã đi: có gì đang mọc kìa."* · đang có Đạo Chủng *"Thân ngươi ta trả cho rừng. Hạt kia, ta giữ hộ."*
- **Giảm rủi ro retention (UX, PX-13):** dạy luật ở FTUE khi chưa mất gì · vòng gỗ hiện "Đời này: 2h10'" (chỉ trong menu) · thanh Đạo Hạnh luôn đi lên · điểm dừng an toàn rõ (thoát ở Nơi Trú = ngủ an toàn, ngoài trời = đếm ngược 30s) · huy hiệu "đời có giá trị" khi >90' nhắc điểm an toàn gần nhất · Mộng Báo hôm sau *"Cây con nơi ngươi ngã đã cao 2 ô"* · đặt hoa ở Mộ Linh · ad an ủi chỉ sau 8s, không che nút "Đời mới" · thẻ hero lần chọn sau là **tộc chưa thử**.
- Biên Niên (mỗi đời 1 trang), Nghiệp Duyên [U1], Tiền Kiếp Ấn [U1] (cosmetic), Tâm Hướng lùi 50% qua đời: giữ v1.0.

---

## 8. Thiên Đạo Luật: PvP tự do & chống bắt nạt — owner: PROG/SURV · PX
**Giữ nguyên v1.0** (không công tắc PvP; g theo cảnh thật; bảng m(g); Sát Nghiệp, Huyết Sát ≥3, Thiên Phạt ≥5 [U1], giảm Nghiệp −1/2h online; miễn trừ đánh trả 60s; Ấu Linh; Áp Chế; Thoát Sinh +2 CT; UX vòng cảnh ▲●▼), với các sửa:
| Chỗ sửa | v1.0 | v1.1 |
|---|---|---|
| Nạn nhân g=1 | +10% Đạo Quả | +10% **Đạo Hạnh** |
| Nạn nhân g≥2 | Oán Linh +25% Đạo Quả | **Oán Linh = Mộng Tích đầy** ở đời kế (chờ Q-B) |
| Mới | — | **Trọng Thương/Kết Liễu** (L2), **Đánh Úp Kiếp/giết người Nhập Định = +1 Sát Nghiệp bất kể g** (L3), rớt mạng (L5) |
| Thiên Kiếp chết | Đạo Quả ×2 | Đạo Hạnh ×2 [Post] |

---

## 9. Nội tâm & endgame — owner: WORLD · PROG
- **Tâm Hướng** (2 trục Sinh↔Sát, Hợp↔Độc, đo bằng hành vi; aura, 3 lời chào/Lão NPC, mẫu Tâm Ma): giữ v1.0. Nguồn "phá neo của người khác" → "phá Mầm Con/Tổ/Ổ của người khác".
- **Công Đức** [U1], Thần Bia lite, Thần Cách [Post]: giữ v1.0; nguồn "xác được phân giải vào Linh Quỹ" gồm cả xác vào nước; thêm "Tưới cây đồng minh", "Mở Xác".
- **Thần Vị (S4, Post)** — khớp biome v1.0, **mỗi ghế có tộc "tổ"** nhưng tộc nào cũng nhập vị được: Mộc = Rừng Lá Rộng (Mộc) · **Hỏa = Rừng Tro** (Vũ, Hoa Phượng Hỏa) · **Thổ = Đồng Cỏ** (Trùng, gò kiến) · **Kim = Vách Đá Rêu** (Thú) · **Thủy = Đầm Mục** (Thủy). Phần còn lại §9.3 v1.0 giữ; "Đạo Quả thưởng/×2" → Đạo Hạnh.

---

## 10. Sự kiện toàn rừng — owner: WORLD · SURV
Luật chung (Bạch Hạc báo 24h, pha nền + đỉnh + cao trào 20:00, Bế Quan miễn, kẻ thắng/thua theo tộc, trần 1 emergent/ngày) giữ v1.0.
| # | Sự kiện | Thay đổi so với v1.0 | Nhãn |
|---|---|---|---|
| E1 | Đại Linh Triều | Giữ; **bỏ Hóa Hình Mộng khỏi MVP** (→ U1) | MVP |
| E8 | Đại Kiếp lite (ngày 28) | Mọi đời kết thúc, **không mất Đạo Chủng**, nhận Đạo Hạnh thưởng; Biên Niên tổng kết | MVP |
| E2 | Huyết Nguyệt | Thua: **con mồi nhỏ (Nha ở đất, Oa ở cạn)** ở Trung Lâm | U1 |
| E6 | Đại Hạn | Vũng mưa cạn trước, Hồ Con không cạn. Thua: cây, **Oa** | 1.0 |
| E3 | Đại Hỏa | Thắng: cây tiên phong, **cá trong đầm** (thay "nấm") | 1.0 |
| E4 | Đại Di Cư | Giữ | 1.0 |
| E7 | **Mưa Vong** (thay Bào Tử Triều) | Đêm sau một ngày nhiều cái chết: mưa 10', ao lan rộng thêm 2 ô, không lũ. Thắng: Thủy, cây gần nước. *"Nước trên trời trả lại những gì nước dưới đất đã nhận."* (bỏ "+1 Duyên tại Mộ Linh") | 1.0 |
| E5 | Tu Sĩ Nhập Sơn | Giữ | Post |
| — | Linh Tức | Giữ (**[B'/C']** chỉ ở FTUE/Linh Triều) | MVP |
| — | Kỷ Nguyên modifier | Giữ | U1 |
| — | **"[Tộc] Giáng Lâm"** | **[C']** sự kiện ra mắt Vũ Tộc đợt 2 (tuần 58), Bạch Hạc báo trước 7 ngày | đợt 2 |

Luật chung "Quạ Già báo trước 24h" → **Bạch Hạc** báo trước. **[B'/C']** chỉ giữ Đại Linh Triều + Đại Kiếp lite ở MVP. Giông và Mưa Vong cấm/hạn chế bay (§4.2a).

---

## 11. Chế độ chơi, server, co-op — owner: PX
Giữ v1.0 (T0 Rừng riêng, T1 co-op ≤4, T2 Rừng chung ≤40 CCU, chế độ ngủ 1 Hz, Singapore trước, không chat/tên tự do, Ops ≤6h/tuần, bảng chi phí server). Sửa: **gộp phòng khi CCU <10** (từ 8), vì có 5 tộc.

**Phân bố tộc ở CCU 24–40 (PX-14):** mục tiêu Mộc 30%, Lang 22%, mỗi tộc còn lại 16%. Ở cấp phòng, CCU ≥24 đủ đa dạng nếu mọi tộc ≥12%; ở cấp vòng map, 25–50% thời gian một tộc 16% vắng mặt → (1) ma trận áp lên AI cùng tộc, (2) không vai nào phụ thuộc tộc khác có mặt, (3) bánh xe hiện số người mỗi tộc trong phòng; tộc <10% trong 30' bật ưu ái + nhãn "Rừng đang cần"; lobby ưu tiên phòng mà tộc của người chơi ít nhất (Could, 0,05); +20% Đạo Hạnh cho tộc <8% lượt chọn trong phòng (3 ngày).

---

## 12. FTUE 20 phút: "Chuột mang hạt" (mới) — owner: PX · WORLD *(PX-10c)*
Nguyên tắc giữ: mỗi beat dạy **một** động từ, 100% local, đường cong kịch bản Tiền Thân. Mới: (1) người chơi **hiểu luật E/F ngay lần chết đầu, khi chưa mất gì**; (2) **cả 5 tộc được nhìn thấy trước** khi chọn.
| Phút | Beat | Học được | Cảm xúc | Tộc thấy |
|---|---|---|---|---|
| 0:00–0:40 | Mộng Hỏa rơi qua tán Lão Tùng: *"Lại một đốm mộng hỏa… Sống đi, nhỏ bé."* Nhập vào Linh Thử | Chạm/kéo | Kỳ vĩ | Mộc |
| 0:40–3:00 | Ăn hạt Linh Thảo phát sáng. Vignette 5s: kiến khiêng hạt qua đường (swarm sẵn có) | Ăn = tu vi | Thỏa mãn | Trùng |
| 3:00–5:00 | Bóng diều hâu. Nút Ẩn ở bụi. Viền Ấu Linh | Có kẻ săn, trốn được | Hồi hộp | Vũ |
| 5:00–7:30 | Tiểu Kiếp C1→C2, rồi **lựa chọn Đạo Lộ đầu tiên: 3 thẻ** (1 thẻ ★ Gợi ý) | Đột phá = chọn hướng | Hùng tráng (fun #1) | — |
| 7:30–10:30 | Gai cây non; Lão Tùng thả Linh Quả, chuột ngậm hạt. **Quạ AI bay xuống từ cành bới lá lộ sâu rồi cất cánh lại** (background — bay là hook, phải thấy trước khi chọn) | Cây có ý thức | Ngạc nhiên | Vũ (Nha) |
| 10:30–12:00 | Thọ Nguyên 12' (chỉ FTUE). Bạch Hạc báo Linh Tức. Ếch AI quăng lưỡi bắt bướm ở Hồ Con rồi **lặn mất xuống ao** (background) | Sinh mệnh có hạn | Khẩn trương nhẹ | Thủy (Oa) |
| 12:00–14:00 | Sói AI tiến về ổ. (A) dụ sói ra xa: ổ chuột con sống, Biên Niên "Hộ Ổ", Tâm Hướng Sinh/Hợp · (B) về chết già dưới Lão Tùng: **đất nơi xác +30% Dưỡng Chất** (trạng thái thế giới, không phải sức mạnh mang theo) | Cái chết là lựa chọn | Day dứt | Thú (Lang) |
| 14:00–15:00 | **Trung Ấm bên mặt nước (45s):** xác chìm, camera theo xuống dưới mặt nước 3s (lần đầu thấy tầng Đáy). Lão Quy (Bạch Hạc trên lưng): *"Ngươi đã mang nó cả đời. Giờ nó mang ngươi."* rồi luật nói một lần: *"Chết giữa đường, ngươi trả lại cho rừng. Đi hết đường, rừng trả lại cho ngươi."* Thẻ "Ngươi để lại": hạt nảy mầm, 38 linh khí, Biên Niên trang 1, +Đạo Hạnh | **Luật E và F** | Xúc động (fun #2) | Thủy (Lão Quy) |
| 15:00–15:40 | **Chọn tộc: 5 thẻ.** Hero (chọn sẵn): Linh Mộc *"Trở thành hạt giống ngươi đã mang"* | Đổi tộc | Háo hức | Cả 5 |
| 15:40–20:00 | Đời 2. Linh Mộc: beat v1.0 (rễ, Vệt Nắng, gai hươu, Manh Nha). Tộc khác: hint 60s + Director cho "thắng đầu" ≤3' (Lang: thỏ · Nghĩ: xác cạnh tổ · Oa: bắt cá dưới nước ở Hồ Con · Nha: vỗ cánh lên cành và bới sâu ≤60s; bay thật lần đầu ở C2). **Lựa chọn đầu của đời 2 ≤5'**. Vòng gỗ hiện vòng cuối mờ: *"Viên Mãn: mang theo 1 Đạo Chủng"* | Lối chơi thứ hai khác hẳn | "Mình là cái cây/sói/kiến…" | — |
| ~20:00 | Mở Rừng chung/riêng. Vé **Tự Quy** (kết thúc đời này, đi đời khác; P2 sang sói ngay) | — | — | — |
| ~25:00 | Gương: Linh Thử AI ăn Linh Quả đầu của cây (nếu chọn A: chuột con của ổ) | Vòng tuần hoàn khép lại | Hiểu ra | — |

**Màn chọn tộc (PX-12a, PX-34):** landscape, thẻ hero bên trái (40% rộng), lưới 2×2 bên phải. Mỗi thẻ: tên + vai ≤6 chữ + icon động từ + **icon đặc tính tộc** (Tự dưỡng / Săn / Bầy / Dưới nước / Bay) + độ khó ●○○ + ảnh "Ngươi đã thấy" từ FTUE. Không chỉ số. Chạm thẻ mở clip 4s. Lần sau thêm "Đời gần nhất: …" và số người tộc đó trong phòng.
**Đo:** ≥80% đạt Tiểu Kiếp trước phút 8 · ≥70% bắt đầu đời 2 trong 60s · ≥80% trả lời đúng "chết thì mất gì, giữ gì" · ≥60% kể được ≥4/5 tộc · chọn tộc trung vị ≤25s · ≥55% chơi cây tới phút 20 · A/B 35–65%.

---

## 13. UI/UX đa nền tảng & accessibility — owner: PX
Giữ v1.0 (≤4 chỉ báo + 1 tu vi, ≤5 nút, 3 skill + 1 Thần Thông, nút ≥48dp, HUD ≤18%, cây chơi một tay ≤6 chạm/phút, accessibility). Thêm: UI Niên Luân/Đạo Lộ, Đặt Trước/Chọn Sau (§6.4), màn chọn tộc 5 thẻ (§12). **Rừng riêng (solo):** trục "Hình phạt chết" có bật "1 lần Hộ Mệnh mỗi đời" hay không → **Q-C** (mặc định: không). Bỏ ad "Hồi sinh tại chỗ".

---

## 14. Kinh tế & monetization F2P — owner: PX *(PX-09b)*

### 14.1 Ví và luồng
```
chơi tích cực ~70% / Mộng Tích ~20% / sự kiện / PvP ≤5% ─► [Tu vi = CT] ─► cảnh giới, mốc Đạo Lộ
                                                            chết giữa đường: về C1 · kiếp thất bại: −CT tầng
ăn/hấp thu/Linh Hạch/quỹ vùng ──► [Linh Khí] ──► skill, khiên kiếp, Đả Tọa (≤15% CT phiên)
quang hợp/xác/đất/Tưới ─────────► [Quang Tinh · Dưỡng Chất · Thủy] ──► rễ, phòng thủ, quả, hạt, kiến
cảnh đạt (mỗi đời, tính ngay) ~60% ─┐
Viên Mãn (thưởng ×3) ~25%            ├─► [Đạo Hạnh] (cấp tài khoản, KHÔNG tiêu) ─► mỗi cấp 1 phần thưởng ngang
đời đầu mỗi tộc +50% ~10%            │     (Tiền Kiếp Ấn bậc, khung Biên Niên, hậu tố Đạo hiệu). Prestige mỗi 10 cấp
sự kiện ~5%                         ┘
Viên Mãn ───────────────────────► [Sổ Đạo Chủng] (không phải tiền) ─► ô 1/2/3
sự kiện/thành tựu/ad ───────────► [Hoa Lộ] (ví kiếm được duy nhất) ─► skin (~1/10h) · hoa Mộ Linh (tiêu hao) · [A'+] trang trí Hóa Tích
nạp tiền ───────────────────────► [Ngọc Tinh] ─► skin, Pass. KHÔNG đổi sang ví khác
```
- **Đạo Quả → Đạo Hạnh:** không tiêu được, vì danh mục mở khóa ngang hữu hạn (cả 5 tộc mở sẵn sau FTUE) → ví tiêu được sẽ bão hòa sau ~8–10h. Thanh cấp không lạm phát, là "thanh luôn đi lên" khi chết. Người chơi chỉ còn 2 ví phải hiểu: Hoa Lộ, Ngọc Tinh.
- **Chống farm:** Đạo Hạnh tính theo **lần đầu đạt mỗi cảnh trong một đời** (tự sát làm lại chỉ farm được C1). Không có Đạo Hạnh từ kill PvP.
- **Không bán tộc.** Loài thứ 2 của mỗi tộc (1.0/Post) mở bằng cấp Đạo Hạnh hoặc Nghiệp Duyên.

| Exploit | Chặn bằng |
|---|---|
| Kill-trading | Sinh Năng cố định 20 CT, cùng cặp 1 lần/30', nạn nhân mất cả đời |
| Chồng hệ số | Gia Trì cộng, trần ×3 · ô Q · trần Ω 1,60 |
| Cây idle offline | 0 CT offline |
| Farm Đạo Hạnh bằng tự sát | Tính theo lần đầu mỗi cảnh/đời |
| Lánh dưới nước / trên trời để farm CT | Bay CT ×0 · Đáy ×0,3 · AI săn dưới nước và Diều hâu tầng Không |

**Gia Trì** (Mộng Tích +1, Bù Đắp +0,5, loài thiếu +0,25, Mộ Linh +0,2, vòng, Linh Triều +1; trần ×3), **Mộng Tích**, **party** (1 + 0,6·min(k−1, 2)), **Bù Đắp**: giữ v1.0 §6.8. **Hồi Ức: bỏ.**

### 14.2 Monetization (không P2W)
| Vị trí ad | Rừng riêng | Rừng chung |
|---|---|---|
| Hoa Lộ ×2 | ✅ 3/ngày | ✅ 3/ngày |
| Đạo Hạnh khi chết +30% | ✅ 3/ngày | ✅ 3/ngày (không phải sức mạnh) |
| +5' Mộng Tích | ✅ 1/ngày | ❌ |
| Hồi sinh tại chỗ | **❌ (vi phạm E)** | ❌ |
| Mọi thứ cho CT/chỉ số/Đạo Chủng | — | ❌ |

- Skin không đổi silhouette/hitbox/bóng bay, không ngụy trang. **Shop MVP [A']** 6 skin · **[B'/C']** 4 skin (Lang, Nghĩ, Oa, Nha; Linh Mộc procedural).
- **Pass Kỷ Nguyên [U1]:** **spotlight 1 tộc mỗi 28 ngày**, xoay vòng 5 tộc (đồng thời là đòn bẩy cân bằng dân số). Free: Hoa Lộ + 2 skin. Premium ~4,99 USD: 6 skin tộc spotlight + hiệu ứng Viên Mãn. **Không bao giờ có Đạo Hạnh, CT, Đạo Chủng.**
- Pháp Tướng [U1], Founders Steam [1.0], mục tiêu ad ≥25% DAU: giữ v1.0.

---

## 15. Tech stack — owner: PX
Giữ v1.0 (TypeScript, Phaser/PixiJS sau spike, Colyseus từ ngày 1, Postgres, CDN, PostHog/Sentry, Capacitor/Tauri, art AI + style guide, cây procedural, kiến/côn trùng swarm VFX, ≤300 entity). Thêm: **autotile nước 3 bậc**, shader phản chiếu mặt nước (Ao Gương, Trung Ấm), **hệ tầng Z dùng chung** cho bay và lặn (Đất / Không / Đáy là trạng thái rời; **server quyết định đổi tầng** và lọc tầm nhìn theo tầng — không gửi vị trí người ở Đáy cho người ở Đất; thời gian cất cánh che độ trễ; chỉ bù lag cho đòn cùng tầng; tốc bay ≤1,6× Lang để interest management không xáo trộn ở 40 CCU), camera zoom ra tối đa ×1,25 khi bay, tùy chọn nước chỉ đổi màu phẳng cho máy yếu. **Spike tuần 2:** Quăng Lưỡi + đổi tầng trên 2 client trễ 150ms.

---

## 16. Phạm vi & roadmap — owner: PX ⚠️ SCOPE RISK
Baseline v1.0: 45,75 t-n + 4,25 đệm = 50 tuần (t-n = tuần-người; dự án 1 người).

### 16.1 Ngân sách MVP — lớp 1: delta v1.0 → v1.1 *(PX-04c)*
*(Lớp này là nền cho lớp 2 ở §16.1b. Các dòng "lite" được nâng lên đầy đủ ở lớp 2.)*
| # | Hạng mục | A | B | C |
|---|---|---|---|---|
| **Thêm** | | | | |
| 1 | Linh Nghĩ lite C1–C3 (Hậu + Lính, Tha, 10 thẻ, sprite; dùng lại swarm Kiến) | 1,0 | 1,0 | 1,0 |
| 2 | Thanh Oa lite C1–C3 (Quăng Lưỡi, Lặn, Ẩm, Nòng Nọc, 10 thẻ) | 0,9 | 0,9 | 0,9 |
| 3 | Linh Kê lite C1–C3 (Sải Cánh, Gáy, Bới, 10 thẻ) | 0,8 | 0,8 | 0 (đợt 2) |
| 4 | Kiếp Viên Mãn template × loài lite | 0,3 | 0,3 | 0,2 |
| 5 | UI 5 tộc: bánh xe, tên cảnh giới, hint, Director "thắng đầu" | 0,35 | 0,3 | 0,3 |
| 6 | Nước: autotile nông/sâu, bảng địa hình, Hồ Con, cá decor, Ướt | 0,7 | 0,55 | 0,55 |
| 7 | Ma trận 10 cặp × 1 cơ chế (data) + icon/tooltip | 0,4 | 0,4 | 0,35 |
| 8 | Cộng sinh thật | 0,4 (4) | 0,15 (2) | 0,15 (2) |
| 9 | Trung Ấm nước, Lão Quy, pool 40 câu, đổi tên Khuẩn (+ Hoa Mộ Linh vàng) | 0,3 | 0,3 | 0,3 |
| 10 | D: UI Đạo Lộ (Đặt Trước/Chọn Sau) + pipeline 57 thẻ + tái cấu trúc Mộc/Lang (Bách Thảo) | 0,6 | 0,6 | 0,6 |
| 11 | E: Trọng Thương, kiếp thất bại ≠ chết, rớt mạng, "Ngươi để lại", Trung Ấm 2 biến thể, nén đường cong | 0,6 | 0,5 | 0,5 |
| 12 | Đạo Hạnh | 0,15 | 0,15 | 0,15 |
| 13 | F: random 3, Sổ Đạo Chủng, ô 1/2/3, bảng dịch 25 ô, Vớt Chủng | 0,5 | 0,4 | 0,4 |
| 14 | Linh Thử FTUE + AI (reskin controller, Hạt Quên) | 0,25 | 0,25 | 0,25 |
| 15 | QA/sim cân bằng 5 tộc, band PvP | 0,45 | 0,4 | 0,35 |
| | **Tổng thêm** | **7,70** | **7,00** | **6,00** |
| **Bớt** | | | | |
| c1 | Linh Thử bản đầy đủ (#4 v1.0) | −1,0 | −1,0 | −1,0 |
| c2 | Kiến lite: swarm/AI chuyển vào Nghĩ | −0,4 | −0,4 | −0,4 |
| c3 | Hóa Hình Mộng → U1 | −0,25 | −0,25 | −0,25 |
| c4 | Huyết Mạch + Ngộ Đạo draft + Keystone → Đạo Lộ | −0,5 | −0,5 | −0,5 |
| c4b | Nội dung Linh Thử (6 skill, 2 Huyết Mạch) | −0,3 | −0,3 | −0,3 |
| c5 | Hậu Duệ, Túc Tuệ, Hồi Ức, Đạo Quả Bàn | −0,8 | −0,8 | −0,8 |
| c6 | Pool Trung Ấm 60 → 40 câu | −0,1 | −0,1 | −0,1 |
| c7 | Linh Thức → chỉ do thám | 0 | −0,4 | −0,4 |
| c8 | Palette mùa 4 → 2 | 0 | −0,2 | −0,2 |
| c9 | Shop 6 → 4 skin | 0 | −0,1 | −0,1 |
| c10 | Linh Tức chỉ ở FTUE/Linh Triều | 0 | −0,1 | −0,1 |
| c11 | Linh Quỹ động → mật độ tĩnh (mất Khô Linh, cá thành decor tĩnh) | 0 | −0,75 | −0,75 |
| c12 | Catch-up solo rút gọn | 0 | −0,3 | −0,3 |
| c13 | Sự kiện: chỉ Đại Linh Triều + Đại Kiếp lite | 0 | −0,3 | −0,3 |
| | **Tổng bớt** | **−3,35** | **−5,50** | **−5,50** |
| | **Net** | **+4,35** | **+1,50** | **+0,50** |
| | **Tổng việc (t-n)** | **50,10** | **47,25** | **46,25** |

*(Đối chiếu: các ước tính R1–R2 của team dao động +0,7 đến +4,4 do đơn giá lite thấp và chưa tính D–G; bảng này mỗi dòng chỉ tính một lần.)*

### 16.1b Ngân sách MVP — lớp 2: Bổ sung 4 (trên nền A = 50,10 t-n) *(PX-30)*
Bay và lặn là công nghệ team chưa làm: dòng N6–N8 sai số **±40%**.
| # | Hạng mục | t-n |
|---|---|---|
| N1–N3 | Nghĩ, Oa, Nha từ lite lên đầy đủ C4 (sprite tầng C4, A1 Thăng, 3 thẻ M5/M6, tên cảnh, đường cong) | +0,40 × 3 |
| N4 | Hợp Đạo × 3 loài (9 thẻ) | +0,15 |
| N5 | Kiếp C4 × 3 (Phi Thăng I + Viên Mãn C4, dùng lại template) | +0,20 |
| N6 | **Hệ tầng Z dùng chung** (Đất/Không/Đáy; server lọc tầm nhìn theo tầng; ma trận ai đánh trúng ai; camera) | +0,70 |
| N7 | **Bay thật** (cất/lượn/hạ cánh/đậu cành, Thể Lực bay, art 8 hướng + bóng, Diều hâu tầng Không, client prediction) | +1,60 |
| N7b | Gộp Sải Cánh vào bay | −0,20 |
| N8 | **Sống dưới nước** (shader lớp nước, tileset đáy, thức ăn/CT dưới nước, 3 AI săn dưới nước) | +1,10 |
| N8b | Bớt phần trùng với Lặn / autotile nước sâu | −0,15 |
| N9 | Nội tại × 5 + đặc tính tộc + tooltip | +0,40 |
| N10 | UI: chỉ báo tầng, Cất/Hạ cánh trên ô BN1, thẻ chọn tộc có icon đặc tính, sửa FTUE | +0,15 |
| N11 | QA/sim duel giữa các tầng, 5 nhân vật đầy đủ | +0,40 |
| | **Net lớp 2** | **+5,55** |

### 16.2 Ba cấu hình — **người dùng chọn (Q-A)** *(PX-31)*
**Luật: đệm dưới 8,5% không bao giờ là khuyến nghị. Không có cấu hình 50 tuần nào giữ được 5 nhân vật đầy đủ và đệm ≥8,5%.**
| | **A': Đủ hết** (khuyến nghị PX) | B': Rút gọn | C': Theo đợt |
|---|---|---|---|
| Tổng việc | 55,65 t-n | 52,15 | 49,35 |
| Đệm | 4,75 (8,5%) | 4,45 (8,5%) | 4,20 (8,5%) |
| Soft launch | **Tuần 61** (đệm 10% thì tuần 62) | Tuần 57 | **Tuần 54 với 4 tộc** + **Vũ đợt 2 tuần 58** (3,1 t-n) |
| Bị cắt | Chỉ những gì quyết định của người dùng đã thay + Hóa Hình Mộng (→ U1) | c7–c13 (Linh Thức chỉ do thám, 2 mùa, 4 skin, **Linh Quỹ tĩnh** — vi phạm luật hóa theme §1.2 tới U1, catch-up gọn, 1 sự kiện lớn, 2 cộng sinh thật) · bay không đậu cành, Diều hâu là kẻ săn trên không duy nhất · dưới nước 2 AI, Đáy chỉ đổi màu shader · Hợp Đạo của 3 loài mới → 1.0 · **giữ nước sâu Đầm Mục** | Như B' + hoãn cả Vũ (lite + C4 + phần riêng của bay) |
| Rủi ro chính | Chậm hơn v1.1 6 tuần; bay chưa có số liệu thực | Linh Quỹ tĩnh trái luật theme | Hook "bay" (cảnh trailer mạnh nhất) không có ngày 1 → copy "tộc thứ năm giáng lâm" |
| Gói A'+ (tùy chọn) | +0,75: Hóa Tích đầy đủ (0,3) + cơ chế phụ mỗi tộc (0,45) | — | — |

Cả ba giữ **≥4 tộc chơi được ngày 1**. **Thứ tự làm (module):** E → D (trên Mộc/Lang) → **N6 tầng Z** → Oa + lặn → Nghĩ → F → Nha + bay → cơ chế phụ G.
*(Cấu hình A/B/C của v1.1 — tuần 55/50/50+53 — đã bị thay thế vì vẫn còn bản lite.)*

### 16.3 Cổng kiểm tra & fallback *(PX-15)*
| Cổng | Đo | Ngưỡng trượt | Hành động |
|---|---|---|---|
| Tuần 2 (spike) | Quăng Lưỡi + đổi tầng (bay) trên 2 client trễ 150ms; server lọc tầm nhìn theo tầng; bundle ≤20MB | Giật/hit sai >10% | Lưỡi lên người chỉ làm chậm (đã là mặc định) |
| **Tuần 8 (prototype bay)** | Lệch hit giữa các tầng; fps máy yếu ở 40 CCU | Lệch >5% hoặc <30fps | **A' → C'**; fallback bay = lướt dài 10 ô + Đậu |
| **Tuần 16 (VS)** | VS = FTUE chuột → Trung Ấm Lão Quy → bánh xe 5 thẻ → Linh Mộc C1–C2 với Đạo Lộ · Lang AI · **Oa lặn dưới nước** · mất trắng + Trọng Thương · 2 client PvP | VS >13 t-n | A' → C'. >15 t-n: C' + dời 2 tuần |
| Tuần 24 | Chi phí thực của một nhân vật đầy đủ (Nghĩ) | >1,7 t-n | Áp B' |
| **Tuần 30 (closed alpha)** | Lịch | Trễ >2 t-n | Áp c7–c13. Trễ >4: C' |
| Tuần 38 (beta) | HE-1, HE-3 | Rời game sau chết C3+ >35% | Trọng Thương áp cho mọi nguyên nhân chết; Ấu Linh kéo tới hết C2 |

**Không bao giờ cắt:** Linh Mộc, Lang, FTUE chuột, mất trắng **có lớp đệm**, Đạo Lộ 3–5 thẻ, Viên Mãn + Đạo Chủng, độ kiếp, Rừng chung PvP, Thiên Đạo L1–L3, **≥4 tộc chơi được ngày 1**, **mỗi nhân vật đã ra mắt phải đầy đủ C1–C4** (quyết định của người dùng). Fallback cuối cho một nhân vật trượt: **hoãn cả loài** sang đợt sau. Nếu vẫn trượt: lùi soft launch, không ra mắt thiếu PvP.

### 16.4 Lịch (theo A')
| Giai đoạn | Tuần | Mốc |
|---|---|---|
| Tiền sản xuất | 1–2 | Spike (Lưỡi, tầng Z, bundle, CCU), style guide |
| Prototype bay | 3–8 | Cổng tuần 8 |
| Vertical Slice | 3–14 (kiểm 14–16) | Playtest 15–20 người (HF-1…3, HC-1, H3, HB-2) |
| Alpha | 15–40 | 5 tộc đầy đủ, Đạo Lộ, mất trắng, tầng Z, Thiên Đạo, Rừng chung. Closed alpha PvP Discord từ tuần ~30 (đo cohort D30 sớm) |
| Beta | 41–52 | UI/accessibility, ads/shop, telemetry, open beta itch.io 1 chu kỳ 28 ngày |
| Đệm + soft launch | 53–61 | CrazyGames + itch.io + site riêng |

### 16.5 Sau MVP
- **[U1]** (~11,5 tuần, giữ v1.0): C5 Bản Thể + Di Căn cho **cả 5 nhân vật** (kẹp M_thẻ ≤1,30), Trung Kiếp, Phi Thăng Kiếp II, Công Kiếp/Pháp Tướng · Pass (spotlight tộc), Android · Huyết Nguyệt, biome 2, co-op riêng, Thiên Phạt · Kế Hoạch Sinh Trưởng đầy đủ, Nghiệp Duyên, Tiền Kiếp Ấn · Công Đức + Thần Bia lite, Kỷ Nguyên modifier · Hóa Hình Mộng · Quăng Lưỡi kéo người chơi (nếu netcode đạt) · **[C']** Nha nếu chưa ra · **[B']** Hợp Đạo 3 loài mới.
- **[1.0]:** loài thứ 2 đầu tiên (**Linh Thử** chơi được; ứng viên: Linh Kê, Phong) · đủ 10 cộng sinh thật · Hóa Tích đầy đủ (nếu chưa có) · Tơ Nấm cộng sinh cây · Mộc Độn, Ký Hồn Mộc, Trận Pháp · Đại Hỏa + Rừng Tro, Đại Hạn, Đại Di Cư, **Mưa Vong** · Mộng Cảnh + Lôi Trì · Linh Lâm 384² · Steam EA.
- **[Post]:** Thần Lâm, C6–C7, Thiên Kiếp, Thần Vị · Nhân Hình · Xuất Khiếu thật · Tu Sĩ Nhập Sơn · các loài roadmap §4.1 (Mộc: Hương Thảo, Ma Vân Đằng, Thiết Mộc, Tùng, Bách, Nắp Ấm…; Thủy: Linh Cáp, Linh Lý, Giải, **Miết**, Thiện, Ngạc; Vũ: Tước, Yến, Thúy Điểu, Hiêu, Ưng; Thú, Trùng…) · iOS · tông môn.
- **[Won't]:** chat/tên tự do · công tắc tắt PvP ở Rừng chung · loot box trả tiền, VIP, năng lượng, P2W · lũ, sương mù · Cửu Cảnh · **độ cao bay liên tục / combat trên không ngoài Bổ Nhào** · **mua/ad để né mất trắng** · **Khuẩn Tộc** · **bản lite cho nhân vật đã ra mắt**.

---

## 17. Rủi ro & giả thuyết playtest — owner: PX

### 17.1 Risk Register
| Rủi ro | KN | TĐ | Giảm thiểu | Fallback |
|---|---|---|---|---|
| Lịch dài (A' tuần 61) / ước tính bay–lặn sai ±40% | Cao | Rất cao | Cổng tuần 2/8/16/24/30; module tầng Z làm sớm | A' → C' → B' |
| **Bầu trời / dưới nước thành vùng bất tử** | TB | Cao | Bay CT ×0, trần 15s, cất cánh bị ngắt, Diều hâu tầng Không; Đáy CT ×0,3, không hồi, Cá Lóc/Cá Sấu AI, xác trôi vào bờ | SURV chỉnh số; fallback bay = lướt + Đậu |
| Netcode lệch trạng thái tầng; đọc tầng trên mobile 844×390 | TB | Cao | Server quyết định đổi tầng, bóng + vòng chỉ tầng, zoom ×1,25 | Cổng tuần 8 → C' |
| Vũ hút quá nhiều người chọn | TB | Cao | Không tộc nào >45% (HE-4 mở rộng), Pass spotlight | Hạ ưu tiên Vũ trên bánh xe |
| **Mất trắng làm sụp D7/D30** | Cao | Rất cao | 6 lớp đệm, đường cong nén, Đạo Hạnh, thang Đạo Chủng, UX PX-13; đo cohort từ tuần 30 | Cổng tuần 38 |
| Bốn hệ lõi đổi cùng lúc (D, E, F, G) | Cao | Rất cao | Làm theo module E → D → F → G | Cơ chế phụ G chỉ ở A+ |
| Đơn giá nhân vật đầy đủ sai ≥30% | Cao | Cao | Đo Nghĩ ở tuần 24 | Áp B' |
| Choice paralysis trên mobile | TB | Cao | Đặt Trước, Chọn Sau, ≤12 chữ, 5 thẻ không vuốt | Thẻ C2→3 từ 4 xuống 3 |
| Ma trận vô hình ở CCU thấp | Cao | TB | Áp lên AI cùng tộc, cộng sinh party | Tăng mật độ AI theo tộc |
| Mộc độc chiếm (bến an toàn vì bất tử offline) | Cao | Cao | Hero card gợi ý tộc mới, Pass spotlight, ưu ái loài thiếu | Hạ ưu tiên Mộc trên bánh xe sau FTUE |
| Đời 2 dài (~5h) làm giảm cảm giác "mới mẻ mỗi đời" | TB | TB | Cái mới đến từ lúc chết + Tự Quy + gợi ý tộc chưa thử; đo HG-2 | Tăng thưởng Đạo Hạnh đời đầu mỗi tộc |
| Nước nông thành bẫy cho Vũ | TB | TB | Ướt không cộng dồn, miễn 10s | SURV chỉnh bảng địa hình |
| Quăng Lưỡi lỗi netcode | TB | TB | Spike tuần 2, không kéo người ở MVP | — |
| Store hứa "Ngũ Tộc" nhưng ra 4 (C) | TB | TB | Copy "tộc thứ năm giáng lâm", ngày cụ thể | — |
| Các rủi ro v1.0 khác (PvP bị đẩy lùi, cây không vui, rừng vắng, ad thấp, cheat, kiệt sức solo dev, bundle, art AI, khán giả nhỏ tuổi) | — | — | Giữ v1.0 (gộp phòng khi CCU <10) | — |

### 17.2 Giả thuyết playtest
| ID | Giả thuyết | Ngưỡng | GĐ | Nếu trượt |
|---|---|---|---|---|
| HF-1 | FTUE mới tạo ham muốn chơi đời 2 | ≥70% bắt đầu đời 2 trong 60s | VS | Trung Ấm lần đầu 30s |
| HF-2 | Hiểu luật E/F sau FTUE | ≥80% trả lời đúng "chết mất gì, giữ gì" | VS | Thêm 1 dòng luật ở màn chết lần 2 |
| HF-3 | Cả 5 tộc được nhận ra | ≥60% kể được ≥4/5 | VS | Đẩy vignette ếch/gà ra foreground |
| H3 | Cây đủ vui | ≥50% chơi cây ≥10' · ≤6 chạm/phút | VS | Dừng 2 tuần làm lại cây |
| HC-1 | Chọn tộc không tê liệt | Trung vị ≤25s, ≤15% mở >2 clip | VS | Bớt chữ trên thẻ |
| HC-2 | Đạo Lộ nhanh trên mobile | Trung vị ≤20s · ≥70% không mở chi tiết · ≥50% ở C2+ dùng Đặt Trước | Alpha | Giảm thẻ C2→3 xuống 3 |
| HC-3 | Không thẻ trội/thẻ chết | Không thẻ nào >50% hay <5% lượt chọn khi có mặt | Alpha | PROG chỉnh số |
| HE-1 | Mất trắng chịu được | Chết C3+ do PvP: ≥45% quay lại trong 72h · rời ≤60s sau chết ≤25% | Alpha/Beta | Cổng tuần 38 |
| HE-2 | Chết sớm không gây bỏ game | Chết trước C3: ≥65% bắt đầu đời mới trong 2' | Alpha | Rút thời gian tới lựa chọn đầu |
| HE-3 | P1 không bỏ game | P1 bỏ ≤40% trong phiên 1–6 | Alpha | Ấu Linh tới hết C2, điểm dừng rõ hơn |
| HE-4 | Không tộc nào độc chiếm (Mộc vì an toàn, Vũ vì bay) | Mỗi tộc ≤45% lượt chọn sau 7 ngày | Alpha | Hero card, Pass spotlight |
| HV-1 | Viên Mãn đạt được | P(hoàn thành) ≥55% · trung vị ≤7h cho **mọi** tộc | Alpha | PROG nén thêm CT_cảnh |
| HV-2 | Đạo Chủng kéo đời tiếp | ≥70% chọn trong ≤15s và bắt đầu đời mới trong 2' | Alpha | Hiện bản dịch rõ hơn |
| HV-3 | Đạo Chủng không phá PvP | Người có Đạo Chủng thắng cùng cảnh ≤55% | Alpha | Hạ Thâm Sát |
| HG-1 | "Chất" tộc khác biệt | ≥65% mô tả được "tộc X chơi khác chỗ nào" trong 1 câu | Alpha | Tăng tương phản động từ, không thêm cơ chế |
| HG-2 | Đổi tộc tự nhiên | ≥50% chơi ≥3 tộc trong 5 đời đầu | Beta | Đạo Hạnh đời đầu mỗi tộc +100% |
| HD-1 | Phân bố tộc | Mỗi tộc 10–40% trong 7 ngày | Alpha | §11 |
| HD-2 | Ma trận được cảm nhận | ≥60% giải thích đúng ≥2 quan hệ · ≥3 lần gặp cặp sinh/khắc mỗi phiên (cả AI) | Alpha | Sửa tooltip trước; tăng mật độ AI. WORLD đổi vòng chỉ khi <50% hiểu và vòng thay thế đạt cao hơn |
| HD-3 | Không cặp nào lệch | Duel PvP cùng cảnh mọi cặp 40–60% | Alpha | SURV chỉnh cơ chế khắc |
| HW-1 | Nước nông không là bẫy cho Vũ | Chết trên ô nước ≤1,3× trung bình | Alpha | Chỉnh bảng địa hình |
| HN-1 | Dưới nước nguy hiểm thật | CT dưới nước ≤0,8× ở bờ · ≥20% số lần Oa chết xảy ra dưới nước | Alpha | Thêm AI, giảm thức ăn dưới nước |
| HN-2 | Lặn vui và có lý do lên bờ | ≥60% người chơi Oa ở dưới nước 30–70% thời gian · ≥65% nói được vì sao mình lên bờ | Alpha | Dời mốc tu lên bờ |
| HB-1 | Bay không phải lối thoát chắc thắng | Vũ thoát khi bị đuổi ≤55% · thời gian trên không ≤35% | Alpha | Thể Lực bay cạn nhanh ×1,3 |
| HB-2 | Đọc được tầng trên mobile | ≥80% gọi đúng tầng của 3 mục tiêu trong 3s · cất/hạ cánh nhầm <5% | VS | "Giữ để cất cánh", tăng tương phản bóng |
| HB-3 | Netcode giữa các tầng ổn | Lệch hit ≤5% ở trễ 150ms · ≥30fps máy yếu ở 40 CCU | Spike tuần 8 | Chuyển C' |
| HK-2 | Hoa Lộ không tích trữ vô nghĩa | <30% người 10h+ dư ≥3 skin Hoa Lộ | Beta | Hàng xoay vòng, tiêu hao Mộ Linh |
| H4 · H5 · H6 · H10 · H12 · H13 | Bế Quan · Thiên Đạo Luật · Mộng Báo · ngân sách UI · P2 không bị khóa sói · Khô Linh đọc được | Giữ v1.0 | — | — |

**KPI go/no-go U1** giữ v1.0 (D1 ≥25/30% · D7 ≥8% · **D30 ≥3% — đánh dấu rủi ro cao** · session ≥14' · ad ≥25% DAU · crash <1% · CCU đỉnh/phòng ≥12). **Telemetry thêm:** tộc được chọn theo phòng/giờ/vòng map · hazard theo nguồn × cảnh × tộc · phút mất mỗi lần chết · P(Viên Mãn) theo tộc · pick-rate từng thẻ Đạo Lộ · thời gian chọn thẻ · Đạo Chủng được chọn · số lần gặp cặp sinh/khắc · % thời gian theo tầng (Không / Mặt / Đáy) · CT theo tầng · tỉ lệ thoát khi bị đuổi bằng bay/lặn · tỉ lệ bỏ game ở đời 2.

---

## 18. Glossary — owner: WORLD
| Thuật ngữ | Nghĩa |
|---|---|
| **Mộng Hỏa** | Người chơi: ngọn lửa ý chí, tia mộng của Kiến Mộc |
| **Ngũ Tộc** | Mộc (mọi cây cỏ) · Thú · Trùng · **Thủy** (loài sống ở/gần nước, đầm lầy) · Vũ (chim, gà, quạ, cú…) |
| **Đặc tính tộc** | Tự Dưỡng (Mộc) · Khứu Tung (Thú) · Bầy & Thoát Xác (Trùng) · Thủy Tức (Thủy) · Lăng Không (Vũ) |
| **Nội tại** | Passive đặc trưng của từng nhân vật: Niên Luân Ký · Cắn Giữ · Hy Sinh · Nhựa Da · Ký Diện |
| **Tầng Z** · **Không / Mặt / Đáy** | Hệ trạng thái rời cho bay và lặn / tầng bay · mặt nước sâu (tầng Đất) · đáy nước (ẩn) |
| **Lão Tùng / Lão Quy / Bạch Hạc** | Lão NPC Mộc / Thủy (giữ luân hồi, Ao Gương) / Vũ (sứ giả, đứng trên lưng Lão Quy) |
| **Linh Tuyền · Ao Gương · Hồ Con · Mắt Suối · Ao Sương** | Mạch trồi lên mặt / ao của Lão Quy / hố sâu nhỏ ở Bìa (điểm sinh Oa) / đầu nguồn / vũng Mộng Ấn 1 |
| **CT** / **Tu Vi** | Đơn vị kế toán / thanh tiến độ cảnh giới |
| **Linh Khí · Linh Quỹ · Khô Linh · Sinh Năng** | Giữ v1.0 |
| **Đạo Lộ · Niên Luân · Thiên Phú · Hợp Đạo · Thâm Hóa** | Hệ thẻ 3–5 lựa chọn mỗi mốc / UI vòng gỗ / thẻ khuếch đại động từ tộc / thẻ nối 2 nhánh / thẻ đệm |
| **Viên Mãn · Viên Mãn Kiếp** | Hoàn thành cảnh cuối của một đời / kiếp cuối đời |
| **Đạo Chủng · Sổ Đạo Chủng · Vớt Chủng** | Hiệu ứng di sản theo trục (Sát/Hộ/Sinh/Hành/Thức) / sổ sưu tập vĩnh viễn, ô 1–3 / nghi thức chọn 1 trong 3 |
| **Hóa Tích** | Dấu tích nơi Viên Mãn (khác Mộ Linh = nơi chết) |
| **Đạo Hạnh** | Cấp tài khoản, không tiêu được (thay Đạo Quả) |
| **Trọng Thương · Kết Liễu** | Trạng thái 30s trước khi chết do người chơi (C3+) / kênh 1,5s để kết thúc |
| **Ẩm · Ướt · Đắm · Lặn** | Thanh của Thủy trên cạn / debuff Vũ trúng đòn Thủy / Vũ rơi xuống nước sâu / xuống tầng Đáy |
| **Đậu · Rơi** | Vũ nghỉ trên Cành/Tán / Vũ hết Thể Lực khi bay |
| **Căn Thương** | Đòn duy nhất trừ Tâm Rễ; của Linh Nghĩ chỉ chạy khi cây Mộc Tàn |
| **Tha · Đánh Hơi · Quăng Lưỡi · Kêu Báo · Bổ Nhào · Bới · Mở Xác · Tưới** | Động từ riêng của các tộc |
| **Cá Lóc Linh · Cá Sấu** | Kẻ săn AI dưới nước (Thủy) |
| **Nơi Trú** | Hang / lãnh thổ rễ / Tổ / Hồ Con / Ổ — một hệ, 5 skin |
| **Mưa Vong** | Sự kiện E7 (thay Bào Tử Triều) |
| **Ô Q · Ω** | Hệ số quan hệ tộc duy nhất (PvP ×1) / trần tổng hệ số ngoài cảnh giới (≤1,60) |
| Áp Chế, Phân Thân, Thiên Đạo Luật, Sát Nghiệp, Huyết Sát, Thiên Phạt, Nghịch Thiên, Oán Linh, Ấu Linh, Bất Nhân, Thoát Sinh, Hồn Hộ, Bế Quan, Nhập Định, Đả Tọa, Mộng Báo, Mộng Tích, Gia Trì, Tán/Thân/Tâm Rễ/Đổ/Mộc Tàn, Vệt Nắng, Quả Ước, Linh Thức, các kiếp, Đại Kiếp, Kỷ Nguyên, Hạ/Linh/Thần Lâm, các vòng, Công Đức, Thần Vị, Ý Chí Rừng, Linh Ảnh | Giữ v1.0 |

**Bị loại (v1.1–v1.2):** Khuẩn Tộc, Bà Khuẩn, Bào Tử Triều, Hậu Duệ, Neo, Ổ Hậu Duệ, Hồi Ức, Túc Tuệ, Đạo Quả, Đạo Quả Bàn, Huyết Mạch, Ấn, Ngộ Đạo, Keystone, Notable/Minor, Độn Thử, Tàng Thử, Cụ Ngao, Triều Mộng, Nghiệp Ấn, Viên Mãn (nghĩa "tầng thứ 4"), **Quạ Già, Sải Cánh, Hạ Cánh Đạp, Gáy (Nha dùng Kêu Báo), bản lite, phẩm Sơ/Thâm, "Linh Quy" (loài chơi được → Miết)**.

---

## 19. Decision Log

**Quyết định của người dùng (chốt, không tranh luận):** Ngũ Tộc định nghĩa lại (Thủy thay Khuẩn) · A thế mạnh riêng · B sinh/khắc/cộng sinh · C MVP 5 tộc × 1 nhân vật · D 3–5 lựa chọn mỗi mốc, kế thừa, hiệu quả hết đời · E chết giữa chừng = mới hoàn toàn · F Viên Mãn → random 3 chọn 1 · G gameplay mỗi tộc khác một chút · **Bổ sung 4:** Khuẩn = môi trường · danh sách loài mở rộng · mỗi nhân vật MVP phát triển đầy đủ, có nội tại riêng + đặc tính tộc (cây tự dưỡng, chim bay, cá sống dưới nước…).

| # | Quyết định | Phương án bị loại | Ai ủng hộ / phản đối | Lý do |
|---|---|---|---|---|
| D20 | **Thú = Lang**, Linh Thử → FTUE + AI | Linh Thử (PROG R1) | 4/4 từ R2 | Lang là fantasy P2, đã có số; Thử yếu vai |
| D21 | **Thủy = Thanh Oa** (C1 Nòng Nọc); Lão Quy là NPC | Linh Quy (SURV R1, WORLD R2), Linh Lý (PROG R1) | 4/4 ở R3 (WORLD rút Quy) | Rùa chậm trên cạn, không có "wow" 60s đầu; cá chỉ sống trong nước, bị nhốt (~5% map); nước sâu dễ thành vùng bất tử. Huyền Vũ vẫn có qua Lão Quy |
| D22 | ~~Vũ = Linh Kê, không bay~~ → **thay bởi D40** | — | — | Người dùng chốt "chim biết bay" (Bổ sung 4) |
| D23 | **Trùng = Linh Nghĩ** (Hậu + Lính tốn No) | — | 4/4 | Swarm có sẵn; Lính tốn No để bầy không là "nửa cảnh miễn phí" (SURV) |
| D24 | **Vòng Hành Tứ Tượng:** Thú = Kim, Vũ = Hỏa, Trùng = Thổ. Sinh Mộc→Vũ→Trùng→Thú→Thủy; Khắc Mộc⊣Trùng⊣Thủy⊣Vũ⊣Thú⊣Mộc | Mộc→Thú→Trùng→Vũ→Thủy (PX R1, SURV R2) | SURV, PROG, WORLD (owner) ở R3; PX chấp nhận có điều kiện HD-2 | PROG chứng minh mọi cách xếp là cùng một vòng 5 → chọn theo lore: 10/10 cặp có hình ảnh vật chất, Thú⊣Mộc đúng trục PvP chính, Vũ⊣Thú đúng cái chết đầu tiên (diều hâu/chuột), Thần Vị khớp biome |
| D25 | **Khắc cấp tộc là cơ chế; ô Q: PvP ×1, PvE ×1,10/×0,91** [orch] | Q ×1,10 cả PvP (PROG), E ×1,25 (v1.0), ×1,15 (WORLD/PX R1) | PvP ×1: SURV, WORLD, PX (3) vs Q 1,10: PROG (owner số ×1,5). R4 không chạy, orchestrator phân xử theo luật trọng số + phương án lai | Đáp ứng mục tiêu duel 40–60% của SURV, vẫn giữ ma trận "được cảm thấy" ở phòng vắng nhờ AI (lý do chính của PROG/PX). Không nhân chồng |
| D26 | **Đạo Lộ** (3 nhánh Tồn/Sát/Vai × 3 Bậc + Thiên Phú + Hợp Đạo + Thâm Hóa), mốc M1–M6 | Huyết Mạch + Ngộ Đạo (v1.0); chọn chỉ ở đột phá cảnh (PX) | PROG owner; 4/4 | Đáp ứng D; lượt chọn đầu ở phút 4; sim: 43 build, chênh ≤1,17 |
| D27 | ~~Lite = C1–C3~~ → **thay bởi D41** (cả 5 đầy đủ C1–C4) | — | — | Người dùng chốt (Bổ sung 4) |
| D28 | **Fallback nhân vật trượt = hoãn cả loài** sang đợt sau, không làm bản thu gọn | Fallback C2 của PROG | PX (owner scope ×1,5) + WORLD vs PROG | Thu gọn vi phạm D/F và quyết định "phát triển đầy đủ" |
| D29 | **Đường cong nén ×0,5** | Giữ đường cong v1.0 | 4/4 | Không nén thì Mid cần 11,4h cho 1 Viên Mãn full |
| D30 | **Kiếp thất bại ≠ chết** | Kiếp thất bại = chết (WORLD R2) | SURV, PROG (BLOCK), PX; WORLD rút ở R3 | P(Viên Mãn đời đầu) 13% → 75%. Kiếp do người chơi tự khởi, nếu là bẫy mất trắng người chơi sẽ né kiếp |
| D31 | **6 lớp đệm L0–L6** (Trọng Thương C3+, rớt mạng không mất trắng…) | Chết = mất trắng không đệm | SURV owner, PROG/PX ủng hộ | Chặn "một nhát gank mất 3 giờ" và "mất 5h vì Wi-Fi" |
| D32 | **Đạo Chủng = hiệu ứng theo trục, dịch theo động từ tộc**, Sổ S2 (ô 1/2/3) | Bản sao thẻ; S1 (1 ô thay thế — SURV); S3 (WORLD R2) | PROG, PX, WORLD (R3); SURV dissent nhẹ | Bản sao thẻ = khởi đầu Bậc III; S2 tạo mục tiêu 16–30h và đẩy đổi tộc (G) |
| D33 | **Đạo Chủng không mất khi đời sau chết (L1)** | Mất hết (L2), Ngủ 1 đời (L3) | 4/4 ở R3 (WORLD rút) | Mất thêm Đạo Chủng = phạt kép, tăng động cơ gank; sim: L2 chỉ giữ 2,2 hạt sau 10 đời |
| D34 | **Khuẩn chia ba:** phân giải = Trùng (cạn) + Thủy (nước); luân hồi = Thủy/Lão Quy; **nấm không thuộc tộc nào** | Nấm thuộc Mộc; Thủy kiêm phân giải toàn bộ | 4/4 | Mỗi tộc là loài sinh vật; nấm giữ được làm prop/breadcrumb không cần tộc |
| D35 | **Cỏ = nhánh Bách Thảo của Linh Mộc** ở MVP; vật phẩm giữ tên Linh Thảo | Linh Thảo là loài riêng (v1.0); đổi tên "Dược Thảo" (PX R1) | 4/4 | "Mộc gồm cỏ" với chi phí 0 loài mới |
| D36 | **Đạo Quả → Đạo Hạnh** (không tiêu được); bỏ ad hồi sinh | Ví meta tiêu được | PX owner | Danh mục mở khóa ngang hữu hạn → ví tiêu được bão hòa |
| D37 | **Quăng Lưỡi không kéo người chơi ở MVP** | Kéo người chơi | SURV, PX, PROG; WORLD chấp nhận lai | Netcode 10–15 Hz trên mobile |
| D38 | **Số liệu chi tiết theo owner** [orch]: HP/Công/kỹ năng theo PROG; needs, nước theo SURV; Căn Thương theo PROG (50s); mức phạt kiếp thất bại giữ v1.0 | SURV: Căn Thương 77s, Sải Cánh 7 ô; PROG: kiếp thất bại lùi đầu tầng Hậu | Orchestrator | Mỗi số có một owner; phương án còn lại ghi để chỉnh theo telemetry |
| D39 | ~~3 cấu hình A/B/C~~ → **thay bởi D46** | — | — | — |
| D40 | **Vũ = Linh Nha (quạ), bay thật**; Linh Kê → roadmap 1.0; NPC Quạ Già → **Bạch Hạc** (đứng trên lưng Lão Quy) | Gà rừng (bay ngắn 7s — dạy sai đặc tính tộc); Sẻ (SURV); Cú (lệch nhịp đêm, trùng vai rình của Lang) | WORLD (owner loài ×1,5); SURV chọn Sẻ; PROG, PX trung lập. Orchestrator theo WORLD | Quạ bay giỏi, ăn xác, kêu báo bầy (đúng "mắt & miệng"), Vũ = Hỏa qua **Kim Ô**; dùng lại gần hết kit Vũ cũ |
| D41 | **Cả 5 nhân vật đầy đủ C1–C4 + Viên Mãn C4**; bỏ phẩm Sơ/Thâm; 66 thẻ; Lính Đỡ 25% → 12% | Giữ lite C1–C3 | Người dùng chốt; PROG sim (chênh ≤1,21) | "Đầy đủ các level" = đủ trong phạm vi MVP map (C1–C4) [giả định orchestrator, xem Q-D] |
| D42 | **Đặc tính tộc** (Tự Dưỡng · Khứu Tung · Bầy & Thoát Xác · Thủy Tức · Lăng Không) tách khỏi **nội tại riêng** | Đánh Hơi là động từ riêng của Lang | SURV (cơ chế) + WORLD (tên) + PROG (giới hạn) | Đặc tính áp cho mọi loài sau này trong tộc; nội tại làm bản sắc từng nhân vật |
| D43 | **Nội tại:** Niên Luân Ký · Cắn Giữ · Hy Sinh · Nhựa Da (số PROG) · **Ký Diện** cho Nha (WORLD, chỉ tiện ích) [orch] | Ý tưởng WORLD cho Lang/Nghĩ/Oa (Truy Huyết +Tốc, Sào Ký cộng dồn, Hô Vũ +CT); Giật Mình (PROG) cho Vũ | Orchestrator | Luật PROG: nội tại không cộng CT, tấn công ≤+2%. Hô Vũ cộng CT → loại. Ký Diện hợp quạ và là công cụ chống bắt nạt tự nhiên; Giật Mình làm phương án dự phòng |
| D44 | **Bay:** 2 tầng rời Đất/Không, bóng luôn hiện, CT ×0, không ăn/đánh khi bay (trừ Bổ Nhào), Thể Lực −8/s, trần 15s ở C4, cất cánh 0,6s bị ngắt được; **cấm hệ số sát thương lên kẻ bay** [orch: bỏ "+30% khi cất/hạ cánh" của SURV] | Độ cao liên tục; bay tự do | SURV (luật) + PROG (giới hạn, Ω) + PX (netcode) | Không thành vùng bất tử; Ω với ×1,25 lên kẻ bay = 1,95 > 1,60 |
| D45 | **Dưới nước:** Mặt (CT ×0,8, lộ gợn, bị Bổ Nhào) + Đáy (ẩn, CT ×0,3, không hồi, Thần Thức 4 ô) + nông CT ×1,15; Cá Lóc + Cá Sấu AI; xác trôi vào bờ; lặn khi giao tranh kênh 1,5s [orch: hợp nhất SURV 2 tầng nước + PROG 1 lớp submerged + PX tầng Z] | "Nước sâu CT ×0" (v1.1); CT ×0,5 một mức (PROG) | SURV, PROG, PX | Thủy thật sự sống được dưới nước (người dùng) mà CT dưới nước ≤0,8× bờ (PX HN-1) |
| D46 | **3 cấu hình A'/B'/C', đều đệm 8,5%; PX khuyến nghị A' (tuần 61)** | Cấu hình 50 tuần | PX | **Người dùng chọn (Q-A)** |

**Quyết định v1.0 bị thay thế:** D2 (Đạo Quả) → D36 · D4 (Hậu Duệ) → E, D30–D31 · D6 (Kiến lite, Hóa Hình Mộng ở MVP) → swarm vào Nghĩ, Hóa Hình Mộng U1 · D13 (Ngộ Đạo) → D26 · D18 ("Linh Thử chơi được") → D20. Các D còn lại (D1, D3, D5, D7–D12, D14–D17, D19) giữ nguyên.

---

## 20. Dissent & câu hỏi mở

### 20.1 Dissent ghi nhận
- **PROG (D25):** muốn Q ×1,10 cả ở PvP (bên khắc thắng ~67%). Sẵn sàng chấp nhận ×1 nếu HD-2 cho thấy ma trận vẫn được cảm nhận.
- **SURV (D32):** thích S1 (1 ô, thay thế) vì đơn giản hơn. **(D38):** Căn Thương 77s — chốt ở prototype. **(D40):** chọn Sẻ cho Vũ. **(D44):** muốn +30% sát thương lên kẻ cất/hạ cánh.
- **PROG (D28):** giữ sẵn fallback thu gọn C2 làm phương án kỹ thuật cuối. **(D43):** Giật Mình cho Vũ.
- **WORLD (D43):** nội tại Truy Huyết, Sào Ký, Hô Vũ (thiên lore hơn) — có thể thành thẻ Đạo Lộ/loài sau.
- **PX (D46):** B' tạm vi phạm luật hóa theme (Linh Quỹ tĩnh tới U1).
- v1.0: dissent D19 (SURV, PX, Thiên Kiếp chết thật) giữ; dissent D2 (Đạo Quả/Đạo Tâm) không còn áp dụng.

### 20.2 Câu hỏi mở cho người dùng
| # | Câu hỏi | Mặc định của team |
|---|---|---|
| **Q-A** | Cấu hình phạm vi: **A'** (đủ 5 tộc, ra mắt tuần 61) · **B'** (rút gọn, tuần 57) · **C'** (4 tộc ở tuần 54, Vũ đợt 2 tuần 58)? Có muốn gói A'+ (Hóa Tích + cơ chế phụ)? | **A'** (thay thế: C') |
| **Q-D** | "Phát triển đầy đủ các level" = đủ **C1–C4** trong MVP (C5–C7 theo U1/1.0/Post vì cần map Linh Lâm/Thần Lâm) — đúng ý bạn? | Có (đủ C1–C4) |
| **Q-B** | Oán Linh mới (nạn nhân bị kẻ cao ≥2 cảnh giết: đời kế có Mộng Tích đầy, ×2 CT 30' đầu, 1 lần/24h) có trái ý "bắt đầu lại hoàn toàn mới" không? Đây là tăng tốc leo lại, không phải sức mạnh mang theo | Có áp dụng |
| **Q-C** | Rừng riêng (solo) có tùy chọn "1 lần Hộ Mệnh mỗi đời" không? | Không |
| Q3 · Q4 · Q5 · Q6 · Q7 | (v1.0) Thiên Kiếp thất bại vì sét · miễn reset cho nhân vật 7 ngày cuối · slot phòng thủ 2 của cây · portal · full-time | Giữ mặc định v1.0 |

---

## Phụ lục: quy trình & kiểm tra
- Nguồn trong session: `00-brief.md` (4 bổ sung của người dùng) → `r1-proposal-*` → `r2-critique-*` → `r3-revision-*` → `r7-patch-*` (vòng vá theo Bổ sung 4, mỗi designer chỉ xử lý phần được giao) · `sim/prog_r1_sim.py`, `prog_r2_sim.py`, `prog_r3_sim.py`, `prog_r7_sim.py` (+ output).
- **BLOCK mới ở R7 (SURV):** B-SURV-7 bay không được có CT >0 hoặc gây sát thương mà không hạ cánh ✓ · B-SURV-8 nước sâu phải có kẻ săn AI dưới nước và cửa để tộc khác chạm Thủy (Mặt/Bổ Nhào/xác trôi) ✓ · gate prototype tầng bay (cổng tuần 8) ✓.
- **R4 không chạy:** sau R3 chỉ còn một xung đột thật (D25), orchestrator phân xử theo luật trọng số. **R6 không chạy** theo yêu cầu tiết kiệm token của người dùng; thay bằng đối chiếu các điều kiện BLOCK mà các designer đã khai ở R3:
  - **SURV (8 điều kiện):** kiếp ≠ chết ✓ · Trọng Thương C3+ ✓ · rớt mạng không mất trắng ✓ · cây offline bất tử ✓ · P(hoàn thành full) ≥55% ở hazard 0,1/h (sim 75%) ✓ · không hệ số khắc ngoài ô Q ✓ · nước sâu CT ×0, không thức ăn ✓ · Căn Thương chỉ khi Mộc Tàn ✓.
  - **PROG:** kiếp ≠ chết ✓ · lite C3 ✓ (nay vượt: cả 5 đủ C4) · nén ×0,5 ✓ · một ô Q + trần Ω, cấm nhân chồng ✓ · Đạo Chủng theo trục ✓.
  - **PX:** không lite C2 ✓ · 5 thẻ chọn tộc không ẩn ✓ · Chọn Sau bắt buộc ✓ · Đạo Chủng không mất ✓ · B không được khuyến nghị ✓.
  - **WORLD:** Lão Quy giữ luân hồi bằng nước ✓ · câu luật ✓ · Đạo Chủng hiện từ nước ✓ · nấm không thuộc tộc ✓ · một Hành mỗi tộc ✓ · NPC khác loài chơi được ✓ · Hóa Tích tách Mộ Linh ✓.
