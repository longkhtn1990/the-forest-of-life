# Linh Nghĩ (Trùng Tộc) — Spec gameplay theo giai đoạn · v2 (Cây Hướng)

> Session: `debates/2026-11-06-trung-toc-gameplay/`
> Quy trình: R1 → R2 → spec v1 → góp ý của người dùng → R3 bổ sung (PROG thiết kế, SURV/WORLD/PX phản biện) → v2 · Ngày 2026-11-06.
> **Góp ý người dùng (đã chốt):** *"nhịp độ chơi quá nhanh và không có nhiều rẽ nhánh khác biệt — mỗi lần lên level cần 3~5 lựa chọn khác nhau rẽ ra nhiều phương hướng phát triển thế mạnh, tương tự về sau."*
> Nền: `The-Forest-of-Life-GDD-v1.2.md`. Chỗ phải sửa GDD gom ở §15.
> Quy ước:
> - Mã nguồn ý tưởng: `PROG-R3-02`, `SURV-R3-03`, `WORLD-R3-01`, `PX-R3-01`…
> - **[orch]** = orchestrator phân xử. **[Must]/[Should]** = nhãn phạm vi MVP.
> - Phút = phút chơi tích cực của người chơi Mid, không chết, theo nhịp **A-sớm** (§4).

---

## TL;DR
1. **Cây Hướng thay "thẻ cộng chỉ số":** mỗi lần đột phá cảnh, người chơi chọn một **Hướng** mới, đổi hẳn lối chơi (động từ, bầy, tổ, điểm mạnh, điểm yếu, hình dạng).
   - **C1→C2:** chọn 1 trong **4 Gốc**: Binh Nghĩ, Công Nghĩ, Huyệt Nghĩ, Mục Nghĩ.
   - **C2→C3:** chọn 1 trong **3 Trung**, mỗi Trung ghép từ Gốc đã có với một Gốc khác.
   - **C3→C4:** chọn 1 trong **3 Đỉnh**: Đỉnh của một trong hai Gốc đã ghép, hoặc **Nhất Tâm** (đi đến tận cùng Trung).
   - Kết quả: **36 dòng phát triển**, chỉ cần viết 14 nút hành vi.
2. **Hướng nào cũng là một loài kiến có thật.** Ví dụ Công Nghĩ là kiến thợ đi vệt, Cát Diệp là kiến cắt lá trồng nấm, Tàng Mật là kiến hũ mật, Chiến Hậu là loài có Hậu tự chiến đấu.
3. **Nhịp chậm hơn ≈1,55 lần.** Một đời ≈ **5,6h** (v1.2: 3,6h).
   - C1 vẫn ngắn (15') để ngã rẽ đầu tiên rơi vào **phiên chơi đầu**.
   - Mỗi đời có 11 quyết định (v1.2: 7). Mỗi cảnh có thêm 3 việc lớn gọi là **Hướng Tích**, nên khoảng giữa hai beat luôn ≤25'.
   - Hai lớp an toàn: **S1** giảm sự kiện gây chết, **S3** cho tu ở Tổ. Nhờ đó tỉ lệ Viên Mãn đời đầu của Mid vẫn ≈73%.
4. **Vẫn chỉ có 1 luật điều khiển** (chạm ăn, giữ làm việc) và **≤5 nút**. Hướng chỉ thay nội dung của các ô BN2, A1, vuốt né và Tương Tác.
5. **Phạm vi:** cây đầy đủ (K4) cho Nghĩ, cây rút gọn (K3) cho Mộc và Lang, Oa/Nha chỉ có tầng Gốc ở MVP. Chi phí ≈1,08 t-n, ra mắt **lùi khoảng 1 tuần (tuần 62)** để giữ đệm 8,5%. **Người dùng chốt.**

---

## 0. Các quyết định chốt
| # | Điểm | Quyết định | Hội tụ |
|---|---|---|---|
| Q1 | Tha | C1: Hậu tự Tha 1 vật (≤2 đv) về Ổ · C2: **Khiêng** (Tha Bầy) | 4/4 |
| Q2 | Số Lính đầu đời | Bắt đầu 1 Lính, Lính "Hai" nở ở lần mang về Ổ đầu tiên (≤90s), Lính "Ba" nở ở Thoát Xác #1. Riêng Gốc Binh đổi thành 2 Binh | [orch] |
| Q3 | Cấu trúc tiến trình | **Cây Hướng lưới K4** (§7). Thẻ Đạo Lộ lùi về **mốc trong cảnh**, làm phần chỉnh nhỏ | PROG thiết kế; SURV, WORLD, PX đồng ý có sửa |
| Q4 | Nhịp | **A-sớm**: C1 15' · C2 58' · C3 106' · C4 158' = **337' (5,6h)**, kèm S1 + S3. B (7,4h) bị loại khỏi MVP. S2 (Dư Âm) không làm | PX [orch, PROG cần sim lại]; SURV, PROG đồng ý A |
| Q5 | Tổ di động (Hành Quân) | **Giữ Sào.** Hành Quân có **Trại Quân** (Ngách di động, không kho, không là Nơi Trú) và thêm 1 lượt Dời Tổ mỗi cảnh | SURV BLOCK → đã gỡ |
| Q6 | Tầng Đỉnh | Mỗi Đỉnh và mỗi Nhất Tâm phải có **1 luật động từ**, không chỉ cộng số | PX |
| Q7 | Hầm Ngầm | Thành động từ của **Gốc Huyệt** (thay vuốt né). Gốc khác dùng vuốt né thường + Lính chắn | PROG |
| Q8 | Duel | Sân Tổ ≤8 ô, hồi Lính 10s, Lang thắng ở đó ≥40%. Bãi trống: Lang cần **≥6s** để giết Nghĩ, mọi dòng Hướng phải đạt (dòng ehp thấp nhất: 7,8s) | 4/4 |
| Q9 | Lang mạnh gấp đôi | Không đổi chỉ số trong session này. **Blocker cấp GDD** (§17) | PROG, SURV; PX dissent |
| Q10 | Tỉ trọng CT | ≈60/25/15. Mỗi dòng Hướng có CT trong [0,92 ; 1,14] | 4/4 |

---

## 1. Fantasy & arc
*"Tổ là não, bầy là tay, Hậu là tim."* Một đời kiến là **một con đường mùi**: mỗi chuyến mang về làm gò lớn thêm, và cuối đời gò hóa đá cho kiến đời sau. **Kiến dọn rừng, không giết rừng** (Căn Thương chỉ ăn cây đã ngã).

| Cảnh (phút) | Cảm giác | Wow | Cách hiển thị |
|---|---|---|---|
| **C1 Ấu Nghĩ** (0–15) | Nhỏ, dễ vỡ, không cô độc | Ổ sáng, Lính Hai nở | — |
| **C2 Lập Sào** (15–73) | "Ta có nhà" + **"ta là loài kiến gì"** | **Chọn Gốc** lúc Thoát Xác ở Ổ. Đặt Sào thành Gò | Phụ đề *"Lập Sào · Huyệt Nghĩ"* |
| **C3 Thành Quần** (73–179) | "Ta là bầy" | **Chọn Trung** (hai mùi gặp nhau). Căn Thương đầu tiên | *"Thành Quần · Ám Mạch"* |
| **C4 Nghĩ Đan** (179–337) | "Bầy mang hình ta" | **Chọn Đỉnh**: thân to ra, hiện hình Đan. **Đại Gò đổi hình theo Đỉnh** (§7.4) | *"Nghĩ Đan · Chiến Hậu"* |
| **Viên Mãn** (337) | "Ta để lại tổ" | Vỏ cuối hóa **Gò Tổ Cổ** mang hình của Đỉnh đã chọn | — |

Giữ nguyên 4 tên cảnh giới (hệ Kiếp, UI và 5 tộc dùng chung). **Tên Hướng hiện dưới dạng phụ đề** *(WORLD-R3-02)*.

---

## 2. Điều khiển (luật chung) — owner: PX

### 2.1 Một nút Tương Tác: "chạm để ăn, giữ để làm việc của kiến"
| Đối tượng | Chạm | Giữ (0,35s, có vòng tiến độ) |
|---|---|---|
| Kẻ địch | Đánh (Lính đánh cùng) | — |
| Vật nhỏ | Ăn | **Tha** · nếu đang Tha thì **Gửi Về** (giao cho Lính) |
| Xác nhỏ (4 đv) + ≥2 Lính trong 3 ô | Cắn | **Khiêng** |
| Xác lớn | Cắn | **Mở Xác** (6s) |
| Cây Mộc Tàn (C3+) | — | Nút A1 sáng (Căn Thương) |
| Đất trống hợp lệ | — | **Đặt Sào** (2s) · Đặt Ngách / **Trại Quân** (nếu Hướng có) |
| Đàn rệp chín (Mục) · lá (Cát Diệp) · miệng mạch (Ám Mạch) | Ăn mật | **Hái Mật** · **Tha lá** · **Chui mạch** |
| Sào / Ngách | Vào Nơi Trú | Mạch Tổ (nếu có) |

- Bảng ngữ cảnh tăng từ 9 lên ≈13 dòng. Rủi ro là **mơ hồ ngữ cảnh**, không phải thiếu nút. Vì vậy **bắt buộc** có bảng ưu tiên và icon nút đổi theo đối tượng (HR3-4). Nếu trượt: tách Tha lá/Hái Mật sang BN2.
- **Vuốt né:** Gốc Huyệt thay bằng Hầm Ngầm (CD 25s). Gốc khác dùng vuốt né thường.

### 2.2 Bầy: 2 lệnh
- **Theo** là mặc định, kèm **Lính chắn** (40% đòn cận chiến đầu bị chặn; Chiến Hậu nâng lên 55%).
- **Xung (BN1):** có địch trong 6 ô thì tự nhắm, địch ở 6–12 ô thì lao tới. **Không có địch trong 12 ô thì bầy "Đứng"** (leash 20 ô / 45s).
- **[Won't]:** lệnh "đi tới điểm", chọn từng Lính, đội hình.

### 2.3 Pip Lính
Sống (đặc) · Chết (rỗng + đếm ngược; chạm = hồi tại chỗ: kênh 1,5s, −6 No, trong giao tranh 1 Lính/8s, mùa Đông chỉ hồi ở Tổ) · Vắng (viền cam) · Đứng (vuông) · overlay mũi tên khi đang Gửi Về. Gốc Binh có 2 Pip lớn, Hành Quân thêm 1. Lính có tên Một/Hai/Ba: *"Hai đã ngã thay ngươi."*

### 2.4 Màn chọn Hướng *(WORLD-R3-03 + PX-R3-01)*
- **Ở Tổ (khuyến nghị):** sau Kiếp, tại Ổ/Sào, đúng lúc Thoát Xác. Lính tự Tha 3–4 vật vào Ổ, mỗi vật mang **mùi** một Hướng: hạt cứng = Binh · sợi mùi = Công · cục đất = Huyệt · giọt mật = Mục. Ở tầng Trung, vật là hai mùi xoắn vào nhau; ở tầng Đỉnh, vật là mảnh Đan mang màu Trung.
  - Hậu đi tới vật nào thì vỏ mới **thử hình** đó: hiện silhouette, 1 dòng fantasy, 1 dòng **Mạnh / Yếu**, nút "xem 10s".
  - Xác nhận bằng **giữ Tương Tác**. Không thêm nút, không cutscene.
- **Ngoài Tổ / đang PvP (Chọn Sau):** **không mở modal**. Có chấm vàng trên ô BN2/A1. Bảng chọn chiếm ≤40% màn hình dưới, chỉ mở khi đã ra khỏi giao tranh 5s hoặc khi về tới Nơi Trú. Chờ bao lâu cũng được, trong lúc chờ vẫn dùng kit cũ; chỉ khác là chưa chọn thì chưa được tính Hướng Tích. Hậu mang hình "vỏ mềm" (chỉ là hình ảnh) cho tới khi chọn.
- **Hiện trước:** nút "Cây" xem được mọi lúc.
  - Tầng kế tiếp: hiện đầy đủ.
  - Tầng Đỉnh: chỉ hiện tên và silhouette.
  - Từ đời thứ 2, các nhánh đã đi qua hiện đầy đủ (sổ sưu tập).
- **Câu của Ổ:**
  - Gốc: *"Vỏ cũ đã chật. Ngươi muốn bầy nhớ ngươi là gì?"*
  - Trung: *"Hai mùi trong ngươi đã gặp nhau. Mùi nào đi tiếp?"*
  - Đỉnh: *"Đan đã thành. Bầy sẽ mang hình ngươi tới đời sau."*
  - Nhất Tâm: *"Không rẽ cũng là một đường."*
- Đo: thời gian quyết định trung vị ≤25s ở Gốc, ≤40s ở Trung · chết trong 10s sau khi mở bảng ≤2%.

### 2.5 PC & accessibility
WASD · E Tương Tác · 1/2/3 BN1/BN2/A1 · Space né/Hầm Ngầm · G Đứng · R hồi Lính · chuột ngắm.
Accessibility: giữ ↔ bật · auto-target mặc định cho cả 3 skill (Vạn Lộ: A1 tự phát từ điểm trên vệt gần mục tiêu đang khóa nhất) · thời gian giữ 0,2/0,35/0,6s · rung khi mất Lính · Pip phân biệt bằng hình dạng.

---

## 3. Luật Tổ, Lính, Tha (nền chung mọi Hướng) — owner: SURV
- **Sào và bậc gò:** Ổ (C1, kho 20) → **Gò** (Đặt Sào ở C2, kho 40) → **Đại Gò** (80 đv tích lũy và ≥C3, kho 60, ≈C4 Trung).
  - **Đặt Sào:** ô cạn, ≥4 ô từ nước nông, ≥12 ô từ tổ người khác, không nằm trong rễ đối địch. **Bến cạn tính là đất khô**, tối đa 1 Tổ/bến.
  - **Dời Tổ:** 1 lần/cảnh từ C3 (Hành Quân +1), mang theo 50% kho.
  - **Sào không phá được** (luật Hang). **Luật một hang an toàn** giữ cho mọi Hướng.
- **Ngách (Tổ Phụ):** chỉ để hồi sinh Lính và làm điểm chui. Không kho, không là Nơi Trú, phá bằng 3 đòn, dựng lại sau 3'.
- **Lính:** HP 12% Hậu (Binh 24%) · −1 No/90s mỗi Lính · leash 8 ô (Đứng: 20 ô) · không vào nước nông · chết thì 0 CT, 0 Linh Hạch · hồi ở Tổ 20s.
- **Tha / Khiêng / Gửi Về:**
  - Trọng lượng: hạt/sâu 1 · thịt 2 · vỏ 2 · xác nhỏ 4 (phải Khiêng) · **Linh Hạch không Tha được**.
  - CT: Hậu Tha 0,25 · Khiêng 0,70 · Gửi Về 0,125.
  - Gửi Về: ≤30 ô, không có Hy Sinh khi Lính ngoài 6 ô, để lại vệt mùi 20s. Mặc định ×1 từ C2 Trung, ×2 từ C3 Trung. Công Nghĩ ×2 ngay từ C2. Binh **không** có.
- **Thoát Xác:** hồi đầy, xóa debuff, miễn 1,5s ở mỗi lần đột phá. **Cũng là nghi thức chọn Hướng.** Vỏ để 60s (Tha về +10 No vào kho).
- **Mùa Đông:** ở Tổ No ×0,5 · ngoài trời không hồi sinh Lính · kho 40 đủ qua 1 Đông nhưng vẫn phải ra ngoài ≥1 lần. **Giữ 2 Đông mỗi đời** (C2 Hậu, C4). Nhịp dài hơn có thể khiến một đời gặp 3 Đông, nên cần neo mùa theo nhịp cảnh hoặc sim lại kho (§17).
- **Mật độ thức ăn:** ~6 vật trong 15 ô quanh Tổ, respawn 90s · No nạp vào ≈1,2–1,4× decay · Đông 0,8×.

---

## 4. Nhịp chơi (A-sớm + lớp an toàn) — owner: PROG (số) · SURV (an toàn) · PX (retention)

### 4.1 Phương án (Mid, không chết)
| Phương án | C1 | C2 | C3 | C4 | Đời | Phiên Mid 40' | Phiên P1 15' | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| v1.2 | 14' | 36' | 66' | 102' | 218' (3,6h) | 5,5 | 14,5 | Quá nhanh (người dùng) |
| A ×1,5 đều | 21' | 54' | 99' | 153' | 327' (5,5h) | 8,2 | 22 | Ngã rẽ đầu ở 21' nên P1 không gặp trong phiên 1 |
| **A-sớm** (chọn) | **15'** | **58'** | **106'** | **158'** | **337' (5,6h)** | 8,4 | 22 | Ngã rẽ đầu trong phiên 1 (hook D1) |
| B ×2 lệch | 20' | 68' | 132' | 224' | 444' (7,4h) | 11 | 30 | Mất ≈4,5h mỗi lần chết; loại khỏi MVP, có thể làm server "Trường Sinh" ở [1.0] |

**Kết quả sim (phương án A, PROG; A-sớm gần như trùng, chờ PROG sim lại):**
| | P1 | Mid | P2 |
|---|---|---|---|
| A, không lớp an toàn | 71% · 7,6h | 62% · 8,3h | 46% · 10,0h |
| **A + S1 + S3** | **81% · 7,0h** | **73% · 7,5h · mất 201' mỗi lần chết · 78' kỳ vọng mỗi Viên Mãn** | 59% · 8,4h |
| B + S1 + S3 | 77% · 9,7h | 68% · 10,5h · 268' mỗi lần chết | 54% · 12,0h |
(Cột: P(Viên Mãn đời đầu) · giờ chơi tới 1 lần Viên Mãn.)

Chỉ số "phút mất kỳ vọng mỗi Viên Mãn" (KPI của v1.2) nới từ ≤60' lên **≤80'**.

### 4.2 Hai lớp an toàn (không đổi luật chết mất trắng)
- **S1 — giảm mật độ sự kiện gây chết:** hazard mỗi giờ ÷√1,5.
  - Mục tiêu mới: C1–C2 **≤0,12/h** · C3 **≤0,08/h** (PvP ≤0,05) · C4 **≤0,065/h** (Cá Sấu ≤0,025).
  - Chỉ giảm sự kiện gây chết (Director thưa kẻ săn, Huyết Nguyệt).
  - **Không** giảm thức ăn và **không** giảm các va chạm không chết (trộm kho, mất Lính, nước tách bầy), để nhịp không bị nhạt. Decay No giữ nguyên.
- **S3 — tu ở Tổ:**
  - ≤20% CT mỗi cảnh đến từ Nhập Định bán chủ động **chỉ ở Sào** (không ở Ngách hay Trại Quân): chạm ~10s/lần, AFK thì vẫn ×0,2.
  - Mùa Đông trần còn ≤15%. Rủi ro thấp chứ không bằng 0: kho vẫn bị trộm online, Hậu tỉnh dậy khi có kẻ trong 8 ô.
- Kiểm tra: độ phơi nhiễm mỗi đời ≈ 1,5 × 0,8 ÷ 1,22 ≈ **0,98× v1.2**.
- **S2 Dư Âm** (đời sau tăng tốc CT ở các cảnh đời trước đã qua): **không làm**. Lợi ích nhỏ và chạm quyết định E.

### 4.3 Nhịp trong cảnh
Mỗi cảnh có 3 tầng: **thẻ** ở tầng Trung và Hậu, **Hướng** ở đột phá. Thêm **Hướng Tích**: mỗi Hướng có 3 "công trình" mỗi cảnh, thưởng hình dạng / kho +5 / leash +2 (nằm **ngoài** trần sức mạnh Ω). Hướng Tích phải **thay ≥30% số chuyến lặp** để nhịp dài không thành grind.

---

## 5. Timeline 12 tầng (A-sớm) [orch: beat của PROG A, co theo A-sớm]
| Phút | Beat | Thao tác thêm |
|---|---|---|
| 0 | **C1 Sơ:** 1 Lính · Ổ · Tha · Xung · Hy Sinh · Lính chắn | Joystick, chạm, giữ = Tha, BN1 |
| ≤1,5 | Lính Hai nở | Đọc Pip |
| 4,5 | **C1 Trung · thẻ M1** | Chọn thẻ đầu |
| 9,5 | **C1 Hậu · Mở Xác** | Giữ trên xác lớn |
| 13–15 | Tiểu Kiếp → **Thoát Xác #1 → chọn GỐC (1/4)** · Lính Ba (Binh: 2 Binh) | Màn chọn Hướng |
| 15 | **C2 Sơ:** BN2 của Gốc · Khiêng · **Đặt Sào** → Gò · co-op | BN2 · giữ 2s đặt Sào · Khiêng |
| ~22 | Bờ nước đầu tiên → hint Đứng · Hướng Tích 1 | Xung không có địch = Đứng |
| 32 | **C2 Trung · thẻ** · Gửi Về ×1 | Giữ vật thứ 2 = Gửi Về |
| ~42 | Hướng Tích 2 | — |
| 52 | **C2 Hậu · thẻ** · Đông đầu (Tổ ≥25 đv) | Quản kho |
| ~62 | Hướng Tích 3 | — |
| 70–73 | Tiểu Kiếp → **Thoát Xác #2 → chọn TRUNG (1/3)** | — |
| 73 | **C3 Sơ:** **A1 của Trung** (+ Căn Thương ngữ cảnh) · hết Ấu Linh · Trọng Thương · Dời Tổ | A1 |
| ~85 | Gỗ Nứt (cây AI tự đổ, bảo đảm có Căn Thương) [Should] · Hướng Tích 1 | Căn Thương |
| 105 | **C3 Trung · thẻ** · Gửi Về ×2 | — |
| ~120 | Hướng Tích 2 · Dời Tổ | — |
| 140 | **C3 Hậu · thẻ** | — |
| ~155 | Hướng Tích 3 | — |
| 170–179 | Phi Thăng Kiếp I → **Thoát Xác #3 → chọn ĐỈNH (1/3)** | — |
| 179 | **C4 Sơ:** A1 Thăng (toán tử của Đỉnh) + luật động từ của Đỉnh · Thâm Lâm / Đầm Mục · Giữ bến | Luật mới của Đỉnh |
| ~195 | Ra bến · Hướng Tích 1 | Đứng ở bến |
| 226 | **C4 Trung · thẻ** | — |
| ~245 | **Đại Gò** (đổi hình theo Đỉnh) · Hướng Tích 2 | — |
| 278 | **C4 Hậu · thẻ + Hợp Đạo** | — |
| ~300 | Hướng Tích 3 · Đông thứ hai | — |
| 320–337 | **Kiếp Viên Mãn** ở Tổ → Gò Tổ Cổ → chọn 1 trong 3 Đạo Chủng (rút từ thẻ **và** Hướng) | — |

Mỗi đời có **11 quyết định**: 3 Hướng + 7 thẻ + Viên Mãn. Khoảng dài nhất giữa hai beat ≤25'.

---

## 6. Onboarding đời Nghĩ đầu tiên
Giữ nguyên v1 (4 beat do Director dàn dựng): xác thỏ cạnh Ổ → Lính Hai nở (≤90s) → sâu AI → Tha theo vệt mùi → M1 → Xung → Diều hâu, dạy Hy Sinh/Pip → Mở Xác khi Lang AI lảng vảng ở 12 ô.
**Thay đổi:** beat cuối ở phút **13–15** (Tiểu Kiếp tại Ổ → Thoát Xác) giờ thành **màn chọn Gốc đầu tiên**: 4 vật mang mùi, "xem 10s", nhãn ★ Gợi ý theo hành vi 10' gần nhất. Mục tiêu: **≥80% người chơi đạt Gốc trong phiên 1**.

---

## 7. Cây Hướng của Linh Nghĩ — owner: PROG (cơ chế, số) · WORLD (tên, hình) · SURV (luật sinh tồn) *(PROG-R3-01/02, SURV-R3-01…07, WORLD-R3-01, PX-R3-01)*

### 7.1 Template lưới K4 (áp cho mọi tộc)
| Đột phá | Chọn | Pool / tộc | Ô được đổi | Kế thừa |
|---|---|---|---|---|
| C1→C2 | **Gốc**: 1 trong 4 | 4 | Lính/thân + **BN2** + 1 bị động + 1 điểm yếu + hình | — |
| C2→C3 | **Trung**: 1 trong 3 | 6 (= 6 cặp Gốc) | **A1** + 1 bị động + 1 bộ phận hình | Gốc X chỉ thấy 3 Trung có chứa X. A1 có 1 dòng "nếu Gốc là X/Y" |
| C3→C4 | **Đỉnh**: 1 trong 3 | 4 Đỉnh + 6 Nhất Tâm | **A1 Thăng** (toán tử lên A1 Trung) + **1 luật động từ** + hình Đan | Trung(X,Y) chào Đỉnh X · Đỉnh Y · Nhất Tâm |

**Chống bùng nổ tổ hợp:**
1. Trung = cặp Gốc.
2. Đỉnh là **toán tử**, chạy với mọi A1 Trung.
3. Mọi kỹ năng dựng trên **6 primitive chung cho 5 tộc**: nón, vũng, lao, bẫy, hào quang, kênh.
4. Sprite: Gốc = thân · Trung = 1 bộ phận rời · Đỉnh = 1 lớp Đan.

Kết quả: 36 dòng chỉ từ 14 nút hành vi + 6 Nhất Tâm.
**Kit chung giữ cho mọi Hướng:** Xung, Tha, Khiêng, Mở Xác, Lính chắn, Hy Sinh. **Căn Thương luôn là ngữ cảnh của A1** (đúng luật Mộc Tàn).

### 7.2 Bốn Gốc (C1→C2)
| Gốc | Loài thật | Fantasy | Đổi lối chơi | Mạnh | Yếu | Hình |
|---|---|---|---|---|---|---|
| **Binh Nghĩ** | *Pheidole* major (kiến lính đầu to) | "Đầu to hơn thân, hàm là cửa tổ." | 3 Lính → **2 Binh** (HP 24%, Công 0,24× mỗi con). BN2 **Phun Toan**: nón axit, Thủ −15% 4s, **trúng kẻ bay**. Xung = Binh **kẹp giữ** 0,8s | Giao tranh, chịu AoE | Không Gửi Về · CT ×0,96 · mất 1 Binh là mất nửa bầy | Đầu ×1,6, hàm kìm, nâu đỏ |
| **Công Nghĩ** | *Lasius niger* (kiến thợ đen đi vệt) | "Không ai nhanh hơn kẻ biết đường." | Lính **tự Tha** khi đang Theo · **Gửi Về ×2 ngay từ C2** · BN2 **Vạch Mùi**: vệt 8 ô, bầy/đồng minh +15% Tốc, kẻ đứng trên vệt bị lộ | Kinh tế, party, đọc đường | HP Lính −15% · dps 0,93 | Thân mảnh, chân dài, đen bóng, vệt hổ phách |
| **Huyệt Nghĩ** | *Messor* (kiến đào/gặt hạt) | "Đất là áo giáp, hang là đường thoát." | Vuốt né → **Hầm Ngầm** (chui 2s, trồi ≤6 ô, CD 25s; Lính bị bỏ lại thì Đi lạc) · **Sào ngầm**: không lộ ngoài **12 ô**, nhưng vòng sáng Gò vẫn hiện khi đang bị trộm hoặc giao tranh · BN2 **Ụ Đất**: chặn đường và tầm nhìn 3 ô trong 6s | Thoát, phòng tổ | Chui là bỏ Lính · dps thấp | Đầu dẹt như xẻng, màu đất |
| **Mục Nghĩ** | *Lasius flavus* (kiến vàng nuôi rệp) | "Ta không săn, ta nuôi." | BN2 **Rải Rệp**: tối đa 3 đàn, chỉ đặt được lên **cây AI, cây có Khế ước, hoặc lau sậy**. Sau 60s giữ Tương Tác để **Hái Mật** (+No, +CT) · Mật nạp ≤**25%** No mỗi giờ · Khế ước với Mộc không chiếm slot của cây | Bền, cộng sinh với Mộc | dps 0,93 · đàn rệp bị Nha/Oa ăn thì mất 3' · phụ thuộc cây | Vàng mật, bụng trong thấy giọt mật |

*Rải rệp lên cây Mộc của người lạ (không có Khế ước): rệp hút −1% Thủy/phút và chủ cây **thấy rệp**.* *(SURV-R3-02)*

### 7.3 Sáu Trung (C2→C3) — thay A1 Đục Rễ
| Trung (cặp Gốc) | Loài thật | A1 / luật mới | Biến thể theo Gốc đã có | Đổi vòng sinh tồn |
|---|---|---|---|---|
| **Hành Quân** (Binh + Công) | *Dorylus/Eciton* (kiến quân đội) | **Giữ Sào.** **Trại Quân** = Ngách di động: dựng 3s, CD 5', chỉ hồi sinh Lính, **không kho, không là Nơi Trú, không Nhập Định**, phá bằng 3 đòn. Hình: cụm Lính ôm nhau thành gò sống. +1 Lính · **+1 lượt Dời Tổ mỗi cảnh**. A1 **Tràn Quân**: dòng bầy 6 ô, kẻ trên đường −20% Tốc | Binh: Tràn kẹp 0,5s / Công: Tràn nhặt vật trên đường | Có (cướp phá cơ động) *(SURV-R3-03, gỡ BLOCK)* |
| **Xích Toan** (Binh + Mục) | *Formica rufa* (kiến gỗ đỏ: nuôi rệp + phun axit) | A1 **Vũng Toan** 3×3 trong 6s: Thủ −20%, hồi máu −30% (khắc Mộc/Oa), mỗi lần dùng −4 No | Binh: Lính để vết axit / Mục: vũng ×1,3 cạnh cây có rệp | Combat + tốn No |
| **Phục Môn** (Binh + Huyệt) | *Cephalotes* (kiến lấy đầu bịt cửa hang) | A1 **Hố Bẫy**: tối đa 2 hố ẩn, kẻ dẫm vào bị giữ 1,2s, Lính trồi lên Xung miễn phí. **Hố chỉ đặt được trong Sân Tổ, hoặc tồn tại ≤3' nếu đặt ngoài** (chống bẫy lối kiếm ăn chung khi AFK) | Binh: giữ 1,5s / Huyệt: chui vào hố = Hầm Ngầm hồi ngay | Phòng tổ |
| **Ám Mạch** (Huyệt + Công) | *Solenopsis fugax* (kiến trộm đào hầm vào tổ khác) | A1 **Đào Mạch**: nối Sào với ≤2 Ngách, chui qua mạch kênh 2s. **Tha trong mạch: Tốc ×0,6, miệng mạch lộ 3s mỗi khi có vật đi qua, phá Ngách là cắt mạch** (giữ nỗi sợ chuyến Tha bị chặn) | Huyệt: +1 Ngách / Công: Gửi Về đi trong mạch | Có (tuyến Tha) *(SURV-R3-05)* |
| **Cát Diệp** (Mục + Huyệt) | *Atta* (kiến cắt lá trồng nấm) | Tha **lá** nuôi **Khuẩn Viên** (vườn nấm, ở dưới Sào): 10 lá → 1 nấm mỗi 5', nấm không thối → **nguồn ăn mùa Đông** (trần ≤30% No trong Đông). A1 **Cắt Tán**: Lính chỉ lấy lá từ **cây AI hoặc cây Mộc Tàn**; trên cây Mộc Tàn thì Căn Thương ×1,2 | Mục: rệp trong vườn / Huyệt: vườn không trộm được | Có (Đông) *(SURV-R3-06, WORLD-R3-01)* |
| **Tàng Mật** (Mục + Công) | *Myrmecocystus* (kiến hũ mật) | A1 **Gọi Mật**: **tiêu 1 đàn rệp** trong 15 ô (đàn ngừng ra mật 60s) → hồi 6% HP cho bầy và đồng minh trong 12 ô (healer). Một Lính bụng căng hổ phách | Mục: 4 đàn / Công: mật đi theo vệt mùi | Có (sustain có giá) *(SURV-R3-07)* |

### 7.4 Đỉnh (C3→C4): toán tử A1 Thăng + **luật động từ** + hình Đan
| Đỉnh | Loài thật | Toán tử lên A1 Trung | **Luật động từ mới** | Đại Gò đổi thành · câu Ổ |
|---|---|---|---|---|
| **Chiến Hậu** (Binh) | *Dinoponera* (Hậu tự chiến đấu) | Xung mang 50% hiệu ứng A1 | Hậu đứng tiền tuyến: Lính chắn 40% → **55%** | Gò đầy xác kẻ thù · *"Bầy đi sau lưng ngươi."* |
| **Vạn Lộ** (Công) | *Linepithema* (siêu tổ) | A1 tự phát từ điểm trên vệt gần mục tiêu đang khóa nhất (≤20 ô) | Vệt Gửi Về thành **Đường Cái** (cả server thấy): trên đường +15% Tốc (trong trần), đổi lại tự lộ mình | Đường mùi sáng tới bến cạn · *"Đường còn thì bầy còn."* |
| **Địa Cung** (Huyệt) | *Atta* tổ sâu | A1 trong Sân Tổ ×1,3 | **Lính trồi lên từ Hầm Ngầm** cùng Hậu · Hầm Ngầm 2 sạc. Sân Tổ 8 → 12 ô **chỉ khi sim xác nhận Lang vẫn thắng ≥40%** trong Sân Tổ, không thì giữ 8 ô | Chỉ thấy giếng thông khí · *"Rừng không thấy ngươi. Đất thấy."* |
| **Chức Diệp** (Mục) | *Oecophylla* (kiến vàng dệt lá, nông dân Việt dùng giữ vườn cam) | A1 cạnh cây cộng sinh hồi 3% HP cho bầy | **Rệp trên cây đồng minh tự Gửi Về mật** · cây đồng minh trong 20 ô: Gai không trúng bầy, cây +5% Thủy | Tổ lá treo trên cây · *"Cây ngươi giữ sẽ giữ ngươi."* |
| **Nhất Tâm · \<Trung\>** ×6 | — | A1 Trung Thăng (data) | **1 twist luật cho mỗi Trung** (vd Nhất Tâm · Phục Môn: đặt được hố khi đang Tha). PROG viết đủ 6 | **Đại Doanh** (gò bằng thân Lính) · *"Không rẽ cũng là một đường."* |

### 7.5 Thẻ Đạo Lộ (mốc trong cảnh, làm phần chỉnh nhỏ)
Khung nhánh Huyệt Nghĩ / Toan Nghĩ / Công Nghĩ giữ nguyên. **4 thẻ cấp động từ chuyển lên Hướng**, nên phải viết thẻ thay thế:
| Thẻ cũ | Đã thành | Thẻ thay thế |
|---|---|---|
| Hầm Ngầm | Gốc Huyệt | **Vỏ Dày** (−6% sát thương nhận khi ≥2 Lính sống) |
| Ngách | Ám Mạch / Hành Quân | **Lối Lui** (Lính chết → Hậu +12% Tốc 2s) |
| Tứ Binh | Hành Quân (+1 Lính) | **Binh Kỷ** (Lính +8% HP, +5% Công) |
| Vác Đôi | Gốc Công | **Chân Chắc** (Tốc khi Tha −30% → −18%) |

Hợp Đạo (Hầm Phục, Mạch Tổ, Đoàn Quân) viết lại thành toán tử theo tag.

### 7.6 Ba ví dụ dòng phát triển sau 10 giờ (khác thao tác, không chỉ khác số)
- **Binh → Hành Quân → Chiến Hậu:** đội quân cướp phá cơ động. Trại Quân dời theo trận, Hậu đứng tiền tuyến.
- **Huyệt → Ám Mạch → Địa Cung:** mê cung dưới đất. Mạch nối các Ngách, Lính trồi lên quanh Hậu.
- **Mục → Tàng Mật → Chức Diệp:** người chữa trị sống nhờ cây Mộc. Rệp tự gửi mật, cây đồng minh che bầy.

### 7.7 Cân bằng
- **Ngân sách Hướng:** mỗi nút dps ≤×1,02 (Đỉnh ×1,00), cả dòng **H ≤1,05**. Thế mạnh về ehp/CT/party phải trả bằng một trục yếu.
- **Ω template** = M_thẻ ≤1,30 × nội tại 1,02 × Q 1,10 × Đạo Chủng 1,035 × H 1,05 = **1,585 ≤1,60**. Trần M_thẻ ≤1,30 áp ngay từ MVP. Ω Nghĩ max **1,48**.
- **Sim 36 dòng:** điểm tổng 0,988–1,037, **chênh 1,05**. Mạnh nhất: Binh → Phục Môn → Nhất Tâm. Yếu nhất: Công → Tàng Mật → Công. Chênh theo trục là có chủ đích: dps 1,23 · CT 1,23 · ehp 1,30 · party 1,32.
- **Kẹp:** CT mỗi dòng ∈ [0,92 ; 1,14] · ehp ≤1,22. Dòng ehp thấp nhất vẫn để Lang C3 mất **7,8s** mới giết được (KPI ≥6s).
- ⚠️ **Rủi ro:** chênh thẻ 1,21 × chênh Hướng 1,05 = **1,27 >1,25**. Mục tiêu pool thẻ mới ≤1,18 (thẻ động từ đã lên Hướng nên pool đều hơn). **Phải sim lại** (§17).
- **Kiểm chứng sinh tồn (SURV):** **7/14 nút** đổi vòng sinh tồn thật (Binh, Công, Huyệt, Mục, Ám Mạch, Cát Diệp, Vạn Lộ). 4 nút chỉ đổi combat (Xích Toan, Phục Môn, Chiến Hậu, Địa Cung), chấp nhận được. Luật: mỗi Gốc phải có ≥1 Trung đổi vòng sinh tồn.
- **Ludonarrative:** Xích Toan và Cát Diệp đụng tới cây. Cắt Tán chỉ lấy lá cây AI/cây Mộc Tàn. Xích Toan là khắc chế có hậu quả. Hành Quân là "mặt tối" có chủ đích của tộc (kiến quân đội thật).

---

## 8. Số liệu theo tầng & nguồn CT
Chỉ số theo tầng giữ v1 (nhịp đổi phút chứ không đổi chỉ số mỗi tầng):
| Tầng | HP Hậu | HP Lính (Binh) | Công Hậu | Công hiệu dụng (3 Lính) |
|---|---|---|---|---|
| C1 Sơ / Hậu | 300 / 363 | 36 / 44 | 22,0 / 26,6 | 25 / 35 |
| C2 Sơ / Hậu | 399 / 483 | 48 / 58 (96 / 116) | 29,3 / 35,4 | 43 / 51 |
| C3 Sơ / Hậu | 531 / 643 | 64 / 77 (128 / 154) | 39,0 / 47,2 | 57 / 68 |
| C4 Sơ / Hậu | 707 / 856 | 85 / 103 (170 / 206) | 51,9 / 62,8 | 75 / 91 |

- CD: Xung 10s (chạy 4s) · BN2 12s · A1 14s · Hầm Ngầm 25s.
- CT/phút ≈1,5–1,8, tỉ trọng cả đời ≈60/25/15 (Tha+ăn / Mở Xác / Căn Thương+săn).
- CT theo Hướng: Binh ×0,96 · Công ×1,1 · Mục có Mật (≤25% No) · Cát Diệp có nấm Đông. Mỗi dòng nằm trong [0,92 ; 1,14].

---

## 9. Tải điều khiển
| Cảnh | Thao tác/phút (trung vị · đỉnh) | Quyết định/phút | Nút |
|---|---|---|---|
| C1 | 10 · 25 | 1–2 | 2 |
| C2 | 14 · 32 | 2–3 | 3 |
| C3 | 18 · 40 | 3 | 4 |
| C4 | 20 · **≤45** | 3–4 | 4 |

Điểm nóng:
- **Vào C3:** chọn Trung, A1 mới, PvP mở cùng lúc → dùng Chọn Sau; hint Căn Thương chỉ bật khi lần đầu đứng gần cây Mộc Tàn.
- **Tầng Đỉnh:** luật mới hiện ≤12 chữ.
- **Mơ hồ ngữ cảnh** của nút Tương Tác: bảng ưu tiên + icon đổi theo đối tượng.

---

## 10. Không gian trên map 256²
Giữ v1:
- **Bìa:** 6 Ổ (điểm sinh) · 3 **Gò Bỏ**, mỗi gò một hazard: A ngập · B đường Lang AI · C Diều hâu dày.
- **Trung Lâm:** 6 **Gốc Mục**.
- **Thâm Lâm:** **3 bến cạn**: Bến Xương (lối hẹp 2 ô) · Bến Rễ (Nha đậu được) · Bến Bùn (lộ thiên). Có **Hầm Đá** (chỉ là prop).
- **Wayfinding:** Cột Linh Quang + lớp mùi (đường kiến AI, vệt Cơ Duyên, vệt Gửi Về).

**Mới:** lau sậy ven Đầm (để Mục/Tàng Mật nuôi rệp được ở C4) · Đại Gò và Gò Tổ Cổ mang hình của Đỉnh.

---

## 11. Tương tác liên tộc
Giữ v1:
- **Khế ước Kiến:** Gai của cây không trúng Lính.
- **Mở Xác cho Lang**.
- **Trùng ⊣ Thủy:** Lính giữ bờ, Oa không hồi được HP.
- **Nha Bổ Nhào:** Toan Dịch trúng kẻ bay.
- **Căn Thương:** Lang phá Thân, Nghĩ đào.

Mới theo Hướng:
- **Mục, Tàng Mật, Chức Diệp** gắn chặt với Mộc (rệp trên cây Khế ước). Rệp bị **Nha và Oa ăn**.
- **Xích Toan** khắc hồi máu của Mộc và Oa.
- **Phun Toan** (Binh) là cách chính của Nghĩ để đánh Nha. Gốc khác đối phó Nha bằng Lính chắn + Hy Sinh (điểm yếu khai rõ).
- **Vạn Lộ:** Đường Cái lộ cho cả server, nên thành mục tiêu săn của Lang và Nha.

---

## 12. Cái chết & thoát
- Kit thoát gốc: vuốt né / Hầm Ngầm (Huyệt) + Lính chắn + Hy Sinh + Tổ gần.
- Hộ Giá: mỗi Lính trúng kẻ đang Kết Liễu làm kênh Kết Liễu +0,5s, trần +1,5s.
- Mất Lính là lỗi nhỏ, mất Hậu là hết đời.
- Hazard mục tiêu theo nhịp A-sớm: xem §4.2.
- Duel: xem Q8. Lang vẫn mạnh gấp ~2 lần (EHP × DPS: 40k so với Nghĩ 20k) → Blocker cấp GDD.

---

## 13. Phạm vi & chi phí — owner: PX *(PX-R3-03)*
- **Vấn đề:** gói Must của Nghĩ đã ≈1,71 t-n, sát cổng tuần 24 (>1,70 thì tự kích hoạt B'). Thêm cây K4 (0,40–0,46) là trượt cổng.
- **Tách cổng:** nhân vật Nghĩ ≤1,70 · **hệ cây** đo riêng (UI lưới + thư viện primitive là chi phí chung cho các tộc).

**Phương án MVP-H (PX chốt; người dùng duyệt):**
| Tộc | Cây ở MVP | t-n |
|---|---|---|
| **Linh Nghĩ** | **K4 đầy đủ** + luật động từ Đỉnh/Nhất Tâm | 0,46 |
| **Linh Mộc** | K3 lite (3 Gốc / 3 Trung / 3 Đỉnh). Là nhân vật FTUE/VS, nên ngã rẽ đầu tiên người chơi thấy là của Mộc | 0,21 |
| **Lang** | K3 lite | 0,21 |
| **Oa, Nha** | 3 Gốc; Trung và Đỉnh **[U1]** | 2 × 0,10 |
| Nghi thức chọn Hướng (WORLD) | — | ~0,02 |
| **Tổng hệ cây** | | **≈1,08–1,10** |

- Áp vào cấu hình A' (đệm 4,75) thì đệm còn ≈6,6%, **vi phạm luật đệm ≥8,5%** → **soft launch lùi ≈1 tuần (tuần 62)**.
- Spike tuần 12 đo chi phí thực trên 3 kỹ năng của Nghĩ (giả định 0,02 t-n mỗi kỹ năng là lạc quan). Nếu thực tế ×1,5 thì áp F1 ngay.
- **Fallback (cắt theo thứ tự):** F1 Nghĩ K4 → K3 (−0,19) · F2 Lang chỉ còn Gốc (−0,11) · F3 Đỉnh mọi tộc chỉ còn toán tử, bỏ hình Đan riêng (−0,08).
- **Không bao giờ cắt:** tầng Gốc của cả 5 tộc (hook D1) và Chọn Sau.

**Nghĩ (ngoài cây) — giữ v1:**
| Hạng mục | Nhãn |
|---|---|
| Tương Tác chạm/giữ, AI 2 lệnh + Đứng, Pip, Khiêng, Đặt Sào/Dời Tổ, bậc gò | **Must** |
| Gửi Về đầy đủ | Should (làm đầu tiên sau cổng); bản lite trong Must |
| Gỗ Nứt (Director bảo đảm cây đổ ở C3) | Should |
| Cá Sấu đớp bờ | Should |
| Gò Bỏ có hazard, 3 bến, Hầm Đá, câu thoại | Should |
| Tích Sào / Trứng Hộ | 1.0 |
| Sào Bến, Gác Tổ | Cắt |
| Micro bầy | Won't |

---

## 14. Giả thuyết playtest
| ID | Giả thuyết | Ngưỡng | Nếu trượt |
|---|---|---|---|
| **HR3-1** | Hướng khác biệt thật | Xem clip 30s, ≥65% đoán đúng Gốc · mỗi Gốc pick 15–40% · Nhất Tâm ≤30% · ≥60% nói được "Hướng của tôi làm gì khác" sau 1 đời | Thêm động từ cho Hướng yếu; Nhất Tâm >30% nghĩa là bẫy an toàn → giảm số |
| **HR3-2** | Chết thành "thử nhánh khác" | ≥40% đổi Gốc ở đời sau · tỉ lệ rời game sau chết không cao hơn v1.2 quá 5 điểm | Xem lại S2 Dư Âm (cần duyệt E) |
| **HR3-3** | A-sớm không nhạt | ≥80% đạt Gốc trong phiên 1 · phiên Mid trung vị ≥25' · "chán/lặp" ở C3–C4 ≤20% | Thêm Hướng Tích; rút C4 về ×1,4 |
| **HR3-4** | UI chọn và ngữ cảnh rõ | Quyết định trung vị Gốc ≤25s / Trung ≤40s · chết ≤10s sau khi mở bảng ≤2% · Tương Tác nhầm ngữ cảnh ≤5% | Ẩn bảng khi có địch trong 12 ô; tách Hái Mật/Tha lá sang BN2 |
| HR3-5 | Retention với nhịp dài | Rời game sau chết ở C2 ≤25% / ở C3+ ≤35% · Viên Mãn đầu trước D14 ≥50% (trong nhóm còn chơi ở D7) · phút mất kỳ vọng ≤80' | Cổng tuần 38 |
| HNg-1…9 | (giữ v1) thắng đầu, hiểu Tha, quá tải, đọc Pip, Đứng, Lang bất công, Lính không thành bia, Đi lạc, gặp Căn Thương | Như v1 | Như v1 |

---

## 15. Bản vá cho GDD v1.2 (áp khi người dùng duyệt → v1.3)
| Mục | Sửa |
|---|---|
| §6.4–6.6 (Đạo Lộ, toàn GDD) | Thêm **Cây Hướng K4** làm tầng tiến trình chính ở mỗi đột phá cảnh (template 5 tộc). Thẻ Đạo Lộ lùi về mốc trong cảnh. Đạo Chủng rút từ thẻ **và** Hướng |
| §6.3 (đường cong) | Nhịp **A-sớm** (C1 ×1,1, C2–C4 ×1,6; một đời ≈337'). Thêm S1 (hazard ÷√1,5) và S3 (tu ở Tổ ≤20%). KPI phút mất kỳ vọng ≤80' |
| §7.2 (hazard) | 0,12 / 0,08 / 0,065 mỗi giờ |
| §6.2 | Tên cảnh giới + **phụ đề Hướng**. "Lập Sào bắt đầu Khiêng và Đặt Sào" |
| §4.2, §4.5 (Linh Nghĩ) | 1 Lính đầu đời, Lính chắn; BN2/A1 theo Hướng; Toan Dịch chỉ còn ở Binh (Phun Toan); Đục Rễ thay bằng A1 của Trung (Căn Thương là ngữ cảnh của A1) |
| §5.1, §5.10 | Pip theo Gốc; bậc gò 20/40/60; Trại Quân; luật Ngách |
| §6.9 | CT ≈60/25/15; Ω template dùng M_thẻ ≤1,30 × H ≤1,05 |
| §4.6 | Duel 40–60% chỉ ở địa hình nhà; ở bãi trống đo bằng thoát được (≥6s) |
| §16 (scope) | MVP-H: hệ cây ≈1,08 t-n, soft launch tuần 62; fallback F1–F3 |
| §17 | Blocker cân bằng Lang |

---

## 16. Decision Log (phần thêm ở v2)
| # | Quyết định | Phương án bị loại | Ai ủng hộ / phản đối | Lý do |
|---|---|---|---|---|
| V1 | **Cây Hướng lưới K4** (4 Gốc → 3 Trung → 3 Đỉnh), template 5 tộc | Cây thường (4 + 12 + 36 nút); chỉ thẻ Đạo Lộ | PROG thiết kế; 4/4 | Đúng yêu cầu 3–5 lựa chọn khác biệt mỗi cảnh; 36 dòng chỉ từ 14 nút |
| V2 | Mỗi Đỉnh và mỗi Nhất Tâm có **1 luật động từ** | Đỉnh chỉ cộng số | PX | Tầng Đỉnh trước đó chỉ có ≈1,5 lựa chọn thật |
| V3 | **Hành Quân giữ Sào + Trại Quân** | "Bỏ Sào, Tổ Di" (PROG) | SURV BLOCK; WORLD giữ fantasy qua hình gò sống | Luật một hang an toàn, luật Đông, Viên Mãn ở Tổ |
| V4 | Vườn Lá → **Khuẩn Viên** (nấm nuôi Đông); Cắt Tán chỉ lấy cây AI/Mộc Tàn | Vườn +3% CT; Cắt Tán cây sống | SURV + WORLD | Đổi vòng sinh tồn thật; đúng sinh học; "kiến dọn rừng" |
| V5 | Ám Mạch: Tha trong mạch ×0,6, miệng lộ, cắt mạch khi Ngách bị phá | Tha trong mạch không bị bắt | SURV | Giữ nỗi sợ cốt lõi của Nghĩ |
| V6 | Mật ≤25% No/giờ; rệp chỉ trên cây AI/Khế ước/lau sậy; Gọi Mật tiêu 1 đàn | Rệp vô hạn | SURV | Giữ độ khan hiếm thức ăn; chống ký sinh không có phản đòn |
| V7 | Huyệt ẩn ngoài 12 ô; hố bẫy Phục Môn chỉ trong Sân Tổ hoặc ≤3' | Ẩn ngoài 6 ô; hố ở bất cứ đâu | SURV | Kẻ săn vẫn đọc được tổ; chống AFK-grief |
| V8 | Tên Hướng = loài kiến thật (Công Nghĩ, Mục Nghĩ, Xích Toan, Phục Môn, Ám Mạch, Cát Diệp, Tàng Mật, Chiến Hậu, Vạn Lộ, Chức Diệp, Nhất Tâm) | Tên tạm của PROG | WORLD (owner tên) | Người chơi tra Google ra loài thật, khám phá ngoài game |
| V9 | Chọn Hướng ở Tổ lúc Thoát Xác; Chọn Sau không modal ngoài Tổ | Modal lúc đột phá | WORLD + PX [orch: gộp] | Không thêm nút; an toàn trong PvP |
| V10 | **Nhịp A-sớm** + S1 + S3; loại B; không làm S2 | A đều (PROG), B, C ×3 | PX [orch]; SURV, PROG đồng ý họ A | Ngã rẽ đầu phải rơi vào phiên 1; B mất 4,5h mỗi lần chết |
| V11 | **MVP-H:** Nghĩ K4 · Mộc, Lang K3 · Oa, Nha chỉ Gốc; lùi ≈1 tuần | Nghĩ K4 + Lang K3, ba tộc còn lại chỉ Gốc (PROG) | PX (owner scope ×1,5) | Mộc là demo của game nên cần có ngã rẽ |
| V12 | 4 thẻ cấp động từ lên Hướng, viết 4 thẻ thay thế | Giữ trùng lặp | PROG | Tránh một hành vi xuất hiện ở hai tầng |
| — | Quyết định v1 T1–T15 giữ nguyên, trừ: T4 (Hầm Ngầm thành động từ Gốc Huyệt), T11 (Tứ Binh → Binh Kỷ), Gác Tổ/Sào Bến vẫn cắt | — | — | — |

---

## 17. Dissent, việc còn mở & câu hỏi cho người dùng
**Dissent:**
- **PROG (V10, V11):** khuyến nghị A đều (21' cho C1) và Mộc chỉ có Gốc. PX chọn A-sớm và Mộc K3.
- **PX:** K4 chỉ hơn K3 ở tầng Gốc (4 so với 3 lựa chọn) nhưng tốn gần gấp đôi, nên giữ fallback F1.
- **PX (Q9):** muốn giảm Lang ngay 10–15%.
- **WORLD:** đề xuất phạt "cắt Tán ≥3 lần thì cây không mọc rệp nữa". Đã thay bằng luật Cắt Tán chỉ trên cây AI/Mộc Tàn.

**Việc còn mở (trước tuần 24):**
1. PROG **sim lại A-sớm** để xác nhận Mid ≈73%.
2. PROG **sim lại pool thẻ** để chênh tổng ≤1,25 (hiện 1,27).
3. Sim **Địa Cung + Sân Tổ 12 ô** (Lang phải ≥40%).
4. **Neo mùa vào nhịp cảnh** để mỗi đời có đúng 2 Đông (SURV).
5. PROG viết **6 twist Nhất Tâm**.
6. **Session cân bằng 4 tộc** cho vấn đề Lang (Blocker cấp GDD).

**Người dùng đã chốt (2026-11-06):** T2-Q1 = **A (A-sớm)** · T2-Q2 = **duyệt MVP-H, soft launch tuần 62** · T2-Q3 = **cân bằng 4 tộc để sau** · T2-Q4 = **áp vào GDD → v1.3** (`The-Forest-of-Life-GDD-v1.3.md`).

**Câu hỏi đã hỏi người dùng:**
| # | Câu hỏi | Mặc định của team |
|---|---|---|
| T2-Q1 | Nhịp **A-sớm** (một đời ≈5,6h, ngã rẽ đầu ở phút 15) có đủ "chậm" chưa, hay muốn **B** (≈7,4h, mỗi lần chết mất ≈4,5h)? | A-sớm |
| T2-Q2 | Duyệt **MVP-H** (Nghĩ cây đầy đủ, Mộc/Lang cây rút gọn, Oa/Nha chỉ Gốc tới U1) và lùi soft launch ≈1 tuần (tuần 62)? | Có |
| T2-Q3 | Chạy **session cân bằng 4 tộc** (vấn đề Lang) trước khi đào sâu tộc khác? | Có |
| T2-Q4 | Áp bản vá §15 vào GDD thành **v1.3**? | Có, khi bạn duyệt |

---
*Phụ lục: `00-brief.md` (kèm góp ý) → R1 → R2 → spec v1 → `r3-branch-{prog,surv,world,px}.md` · sim `prog_r1_nghi_sim.py`, `prog_r2_duel_global.py`, `prog_r3_pacing.py`. Vòng bổ sung chạy theo quy định "chỉ gọi agent liên quan" của skill; không chạy R6 (yêu cầu tiết kiệm token). Các chỗ phân xử ghi [orch].*
