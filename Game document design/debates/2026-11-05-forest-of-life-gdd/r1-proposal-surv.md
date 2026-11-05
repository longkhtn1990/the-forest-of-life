# R1 Proposal — SURV

> Domain: core survival loop, needs/vitals, tài nguyên & linh khí, chuỗi thức ăn, mối đe dọa, lãnh thổ, cái chết.
> Mọi con số dưới đây là **giá trị khởi điểm để playtest/simulate**, không phải chân lý. Đơn vị thời gian là **thời gian thực** trừ khi ghi "game".

## 1. Cách tôi hiểu yêu cầu

Người chơi là **một sinh mệnh trong chuỗi thức ăn thật** — không có "người chơi đứng ngoài hệ sinh thái". Sinh tồn ở đây không phải "tìm đồ ăn rồi xây nhà" kiểu Valheim, mà là **giữ thăng bằng năng lượng sống trong một hệ sinh thái mà chính những người chơi khác là thức ăn, đối thủ và đồng minh**. Tu vi (EXP) và sinh tồn phải là **cùng một dòng chảy năng lượng**: cái bạn ăn/hấp thu vừa giữ bạn sống vừa đẩy bạn lên cảnh giới. Cái chết không phải điểm cuối mà là **chuyển giao năng lượng** cho rừng.

Giả định tôi đặt ra:
- **A1:** 1 ngày game = **20 phút thực** (Ngày 12' · Hoàng hôn 2' · Đêm 6'). Session 15–60' = ~1–3 ngày game → mỗi session luôn có ít nhất một chu kỳ căng (đêm/hạn) → thả (bình minh/bế quan).
- **A2:** 1 mùa = **2 ngày thực** trên server online (1 năm rừng = 8 ngày). Solo: mùa đổi theo số ngày game (1 mùa = 12 ngày game).
- **A3:** Bản đồ dùng **lưới ô (hex hoặc vuông, 1 ô ≈ 1 bước sói)** cho rễ, độ ẩm, dinh dưỡng, mật độ linh khí. Rẻ cho 2D, dễ simulate, dễ đọc trên mobile.
- **A4:** Cảnh giới đánh số R1–R9 (tên riêng từng loài do PROG/WORLD đặt). Tôi chỉ dùng số.
- **A5:** "Luôn PvP" giữ nguyên, nhưng tôi chống bắt nạt bằng **luật sinh thái** (năng lượng, nghiệp, mật độ linh khí), không bằng vùng cấm PvP.

## 2. Ý tưởng cốt lõi (hook)

**"Mọi sinh mệnh là năng lượng đang mượn tạm."** Bạn ăn để sống và để tu; khi chết, năng lượng của bạn bị chia cho kẻ giết, cho đất và cho linh hồn bạn mang đi — và cái cây bạn từng gặm có thể chính là kẻ hút xác bạn để đột phá.

## 3. Đề xuất chi tiết

### SURV-01: Khung sinh tồn "2+2" thống nhất cho mọi giới
- **Mô tả:** Mọi loài chỉ có **4 thanh** trên HUD, cùng một bố cục để UI/code dùng chung, nhưng ý nghĩa khác theo giới:
  1. **Sinh Mệnh** (HP) — chung.
  2. **Linh Khí** (pool tu luyện & skill) — chung.
  3. **Bản Nguyên A** — need suy giảm chính của giới.
  4. **Bản Nguyên B** — need/tiền tệ thứ hai của giới.
- **Môi trường (nhiệt, mùa, thời tiết) KHÔNG phải thanh riêng**, mà là **hệ số nhân** lên A/B (xem SURV-05). Tự kiểm tra điểm mù: tôi đã bỏ Khát cho động vật và Thân nhiệt cho mọi loài — game không tệ đi vì nước/nhiệt vẫn tồn tại qua hệ số, và cây có nước làm điểm khác biệt.

| Giới | Bản Nguyên A (suy giảm) | Bản Nguyên B | "Vật liệu" phụ (không suy giảm) |
|---|---|---|---|
| Thực vật (Mộc) | **Thủy** (nước) | **Quang Tinh** (năng lượng quang hợp, có hô hấp đêm) | Dưỡng Chất (từ đất, để lớn) |
| Động vật (Thú) | **No** (satiety) | **Thể Lực** (stamina) | — |
| Nấm (Khuẩn) | **Ẩm** | **Mục Chất** (chất phân giải tích trữ) | Sợi Nấm (độ dài mạng) |
| Côn trùng-đàn (Trùng) *(hậu MVP)* | **Kho Mật/Thực** (của cả tổ) | **Thể Lực** (của thân chủ) | Số cá thể đàn |

- **Vì sao tốt:** 1 hệ thống UI, 1 bộ code needs, 4 cảm giác chơi khác nhau. Người chơi luân hồi sang loài mới không phải học lại HUD.

### SURV-02: Needs Table — Động vật
Giá trị cho R1, thang 0–100. Ăn cỏ và ăn thịt **khác decay** vì khác độ sẵn có của thức ăn.

| Need | Decay | Ngưỡng (Comfort / Warning / Critical / Lethal) | Hậu quả | Cách hồi |
|---|---|---|---|---|
| **No – ăn cỏ** | −1/9s (≈ −6.7/phút); chạy ×1.5 | 100–60 / 59–25 / 24–1 / 0 | Comfort: hồi HP 1%/5s · Warning: ngừng hồi HP · Critical: Thể Lực max −30%, tu luyện ×0.5 · 0: −1% HP/3s, tu vi ngừng | Cỏ dại +4/cắn (1.5s), lá cây +6, quả +15 |
| **No – ăn thịt** | −1/15s (≈ −4/phút); chạy ×1.5 | như trên | như trên | Thịt +30/cắn (2s), xác thối +12 & 25% Trúng Độc |
| **Thể Lực** | Chạy −15/s, đòn đánh −15 đến −25, né −20 | 100–40 / 39–15 / 14–1 / 0 | <15: không chạy được · 0: choáng 1.5s | +20/s đứng yên, +10/s đi bộ; ×0.6 khi No Critical |
| **Sinh Mệnh** | — | 100–50 / 49–25 / 24–1 / 0 | <25: để lại vệt máu (kẻ săn đánh hơi được) | Hồi qua No Comfort, bế quan, linh khí |

- **Kiểm tra "phút đầu tiên":** ăn cỏ chạm Warning sau **~6 phút**, ăn thịt sau **~10 phút** → trong khoảng mục tiêu 8–15' cho cảnh báo đầu (ăn cỏ nhanh hơn nhưng thức ăn ở khắp nơi; ăn thịt chậm hơn nhưng một cuộc săn hỏng là đói thật).
- **Tình huống:** Sói R1 săn thỏ hụt 2 lần, chạy tổng 40s → No từ 70 rơi còn ~52 trong 4 phút, Thể Lực lặp lại về 0. Nó phải quyết định: tiếp tục săn hay ăn xác thối bên bờ suối (rủi ro trúng độc, và xác thối thường có nấm đang chiếm).

### SURV-03: Needs Table — Thực vật (Mộc) và "3 lớp thân"
**Cấu trúc HP của cây gồm 3 lớp** — đây là chìa khóa để cây sống được trong một thế giới PvP mà nó không thể chạy trốn:

| Lớp | R1 | Vai trò | Ai phá được |
|---|---|---|---|
| **Tán** (Lá) | 60 đơn vị | Khả năng quang hợp **và** lá chắn ngoài | Mọi loài ăn lá, sâu, lửa, mưa đá |
| **Thân** | 200 HP | Chiều cao, tán rộng | Thú lớn (R≥ cây), bọ đục thân, lửa, sét, cây khác (thắt cổ) |
| **Tâm Rễ** (Linh Căn) | 100 HP, dưới đất | **Mạng sống thật** | Hạn hán, nấm mục, thú đào, rễ đối thủ, lửa lớn, Thiên Kiếp |

- Tán = 0 → cắn tiếp sẽ lột vỏ Thân (×0.5 sát thương). Thân = 0 → **Đổ**: cây về trạng thái "Rễ Ngủ", tái mọc sau **3 phút** nếu Quang Tinh ≥30, mất 1 bậc chiều cao (≈ 15–25 phút tiến độ). **Chỉ chết thật khi Tâm Rễ = 0.**

| Need | Decay | Ngưỡng | Hậu quả | Cách hồi |
|---|---|---|---|---|
| **Thủy** | Ngày −3/phút; đêm −1/phút; +0.5/phút mỗi bậc chiều cao; mùa hạ ×1.5; Đại Hạn ×2.5 | 100–50 / 49–30 / 29–10 / 0 | <30: quang hợp ×0.5 (đóng khí khổng) · <10: rụng 1 lá/10s · 0: Tâm Rễ −1%/5s (chết héo sau ~8 phút) | Mỗi ô rễ trên đất ẩm +2/phút, ô suối +6/phút, mưa +10/phút, sương bình minh +15 một lần |
| **Quang Tinh** (tiền tệ) | Đêm: hô hấp −0.05 × (Tán + Thân/10) mỗi phút ≈ −4/phút ở R1 | Kho 0–150 | 0 vào đêm: tiêu Tán để thở (−1 lá/15s) | Ngày: Tán × Ánh Sáng% × Hệ số Thủy × 0.1/phút ≈ +6/phút ở R1 nắng đủ; Vệt Nắng ×3 |
| **Dưỡng Chất** (vật liệu) | Không suy giảm | — | Thiếu thì không lớn/không ra hạt | Ô đất màu, xác chết, phân thú, tro sau cháy (×3) |

- **Ánh Sáng%:** 100% ở chỗ trống; mỗi tán cây cao hơn chồng lên trừ 30% (tối thiểu 10%). **Đánh đổi chiều cao:** cao = nhiều nắng + che bóng đối thủ, nhưng tốn nước hơn, bị thú lớn thấy từ xa, và **hút sét** trong giông (SURV-14).
- **Tiêu Quang Tinh vào đâu** (≥2 cách dùng + đánh đổi): mọc Tán (2/lá), mọc rễ (8/ô), tăng chiều cao (40/bậc), gai/độc (skill), hạt giống (25/hạt), quả mời thú (15/quả), dự trữ cho đêm & hạn. Đây là **"gỗ để sưởi hay để xây tường" của cây**.

### SURV-04: Needs — Nấm và Côn trùng-đàn
- **Nấm (Khuẩn):** **Ẩm** −4/phút dưới nắng trực tiếp, −1/phút trong bóng râm, +2/phút đêm/mưa. Nắng trực tiếp >60s liên tục: −2% HP/s → nấm là **giới của đêm, bóng râm và xác chết**. **Mục Chất** thu từ xác, gỗ mục, lá rụng; dùng để vươn sợi nấm (5/ô, nhanh gấp 2 rễ cây), mọc thể quả (cơ thể nhìn thấy được, bị ăn được), phóng bào tử (respawn anchor/tấn công). Nấm có **mycorrhiza**: nối sợi với rễ cây (thỏa thuận 2 người chơi hoặc AI) → trao Dưỡng Chất lấy Quang Tinh.
- **Côn trùng-đàn:** đề xuất **hậu MVP** vì chi phí AI swarm. Ở MVP, kiến/ong xuất hiện như **cộng sinh do cây điều khiển** (SURV-07) để tái dùng asset.

### SURV-05: Ma trận tương tác môi trường × needs
| Điều kiện | Thú: No | Thú: Thể Lực | Mộc: Thủy | Mộc: Quang hợp | Khuẩn: Ẩm | Ghi chú |
|---|---|---|---|---|---|---|
| Đêm | ×1.0 | regen ×1.0 | ×0.33 | 0 (hô hấp) | +2/phút | Thú săn đêm thấy +30% |
| Xuân | ×0.9 | — | ×1.0 | ×1.2 | ×1.0 | Mùa sinh sản, cỏ dày |
| Hạ | ×1.0 | regen ×0.8 | ×1.5 | ×1.3 | ×1.5 decay | Nguy cơ cháy tăng |
| Thu | ×1.1 | — | ×1.0 | ×0.9 | ×0.7 decay | Quả rụng nhiều, Mùa nấm |
| Đông | ×1.4 | regen ×0.8 | ×0.5 | ×0.4 | đóng băng: ngủ | Cây có thể **Ngủ Đông** (SURV-12) |
| Mưa | ×1.0 | — | +10/phút | ×0.6 | +3/phút | Xóa mùi → con mồi dễ trốn |
| Giông | ×1.0 | — | +10/phút | ×0.4 | +3/phút | Sét đánh vật cao nhất trong 8 ô |
| Sương mù | — | — | — | ×0.7 | +1/phút | Tầm nhìn −60% → mùa phục kích |

### SURV-06: Core loop 4 tầng (song song Thú/Mộc)

```
MOMENT (giây)
  Thú:  rình → vồ/né → cắn → nuốt (2s, bị gián đoạn được)
  Mộc:  bắt Vệt Nắng → kích gai/độc khi bị cắn → rút rễ khỏi ô bị tranh
        ↓
ACTIVITY (3–8 phút)
  Thú:  một chuyến kiếm ăn/săn → mang thịt về Hang hoặc ăn tại chỗ (rủi ro)
  Mộc:  một "chu kỳ sinh trưởng": dồn Quang Tinh vào Tán/Rễ/Phòng thủ/Hạt,
        vươn rễ tới mục tiêu (xác, suối, linh mạch), đẩy lùi một đợt ăn lá
        ↓
SESSION (15–60 phút = 1–3 ngày game)
  Sáng: tích lũy → Trưa: mở rộng/đi xa → Hoàng hôn: rút về →
  Đêm: phòng thủ/săn đêm → BẾ QUAN tại Hang/Tâm Rễ (luyện linh khí → tu vi ×1.5, lưu an toàn)
        ↓
CAMPAIGN (tuần)
  Đột phá tiểu cảnh → Độ Kiếp (đại cảnh giới) → vào vùng trong → sự kiện toàn rừng
  → chết/luân hồi → kiếp sau mạnh hơn nhờ Đạo Tâm
```

- **Release được đảm bảo:** Bế quan là "về base nấu ăn" của game này — luôn có, luôn an toàn nếu Hang/Tâm Rễ chưa bị chiếm.

### SURV-07: Vòng chơi Cây 15–60 phút — "cái cây phải bận rộn và phải sợ"
Đây là phần khó nhất. Một cái cây đứng yên dễ thành idle game. Tôi giải bằng **6 động từ chủ động** + **5 nguồn áp lực đến tìm cây**.

**6 động từ chủ động của cây:**

| Động từ | Cơ chế | Số liệu R1 | Đánh đổi |
|---|---|---|---|
| **Bắt Vệt Nắng** | Các đốm sáng lọt tán di chuyển trên tán cây; chạm/kéo chồi tới → quang hợp ×3 trong 5s. **Linh Quang** (vệt vàng, 1/3 phút) cho thêm +5 linh khí | 3–6 vệt/phút khi bị che bóng, 1–2 khi trống | AFK = mất ~40% thu nhập ban ngày → cây chủ động có lợi, nhưng AFK vẫn sống |
| **Vươn rễ** | Kéo đường rễ qua lưới ô; 1 ô/20s; ô rễ = lãnh thổ, nước, dưỡng chất, **cảm ứng rung** (thấy kẻ bước vào) | Tối đa 12 ô ở R1, ×2 mỗi đại cảnh giới | 8 Quang Tinh/ô; rễ dài = nhiều điểm bị đối thủ cắt |
| **Phòng thủ** | Skill chủ động: Gai Bạo (phản 15% sát thương/cắn trong 10s), Độc Tiết (sau 5 cắn: chậm −30%, −2 HP/s 6s), Đắng Hóa (giá trị No của lá −50% trong 60s), Trói Rễ (giữ chân 2s trên ô rễ) | CD 20–45s, 10–20 Quang Tinh | Tiêu Tinh phòng thủ = ít Tinh lớn lên |
| **Gieo hạt** | Ngắm & bắn hạt tới ô trong tầm 6 ô (gió mạnh: 20 ô). Hạt nảy thành **Mầm Con**: mở rộng lãnh thổ + **neo luân hồi** (SURV-15) | 25 Tinh + 5 Dưỡng Chất; tối đa 3 Mầm ở R1 | Mầm yếu (30 HP) → mồi cho thú; nhưng mất mầm không mất cây chính |
| **Gọi cộng sinh** | Tiết mật nuôi **kiến** (đội phòng thủ đến sau 8s, cắn kẻ ăn lá), **ong** (thụ phấn → quả), nối **nấm** (mạng ngầm, nhắn tin/trao đổi với cây khác) | Duy trì: kiến −1 Tinh/phút/tổ | Cộng sinh hút Tinh liên tục; bỏ đói → chúng rời đi |
| **Xuất Khiếu** | Phóng linh thức thành hồn ảnh di động: do thám, hút linh khí ở nút xa, vào bí cảnh linh hồn, giao tiếp/giao dịch với thú | R1: 90s, hồi 5 phút; R5: 6 phút | **Thân bị bỏ trống**: phòng thủ tự động chỉ 50% hiệu quả. Hồn ảnh bị đánh tan → choáng thân 10s |

(Hóa Hình từ R5: thân người/linh thú di chuyển được, nối với Tâm Rễ bằng "sợi mệnh" bán kính 30 ô; ra ngoài bán kính → mất 2% HP/s. Đặc tả chi tiết để PROG/WORLD.)

**5 nguồn áp lực tìm đến cây (Plant Pressure Map):**

| Áp lực | Xuất hiện | Tác động | Đối phó |
|---|---|---|---|
| Thú ăn lá (AI/người chơi) | Mỗi 4–7 phút ở vùng ngoài; Director điều chỉnh | −2 lá/cắn | Gai/Độc/Đắng/kiến; hoặc **mời quả** để chúng ăn quả thay lá |
| Sâu bướm / bọ đục thân | Đẻ trứng khi Tán > 70% & không có kiến; nở sau 2 phút | −1 lá/5s mỗi ổ, đục thân −1 HP/s | Kiến, chim (thú người chơi ăn côn trùng!), Độc Tiết |
| Dây Tơ Hồng Yêu (ký sinh) | Bám khi cây ở vùng ẩm, 1 lần/ngày game | −20% Quang Tinh thu được cho tới khi cắt | Gai Bạo cắt được trong 3 lần; hoặc thú người chơi cắn đứt |
| Cây đối thủ | Liên tục | Che bóng (−30% sáng), tranh ô rễ, tiết chất ức chế (allelopathy) | Vươn cao hơn, chiếm ô trước, rễ ức chế ngược |
| Hạn / cháy / sét | Theo mùa & sự kiện | Thủy, Tán, Thân, Tâm Rễ | Rễ tới suối, vỏ dày (chống cháy), không vươn quá cao trong giông |

**Session mẫu 30 phút — Cây Linh Sam R2:**
- 0–3': đăng nhập, đọc **Nhật Ký Rễ** (offline bị nai gặm 12 lá — đã giới hạn, xem SURV-12). Dồn 24 Tinh mọc lại Tán.
- 3–10': rễ cảm ứng một con sói người chơi giết hươu cách 4 ô. Vươn 3 ô rễ tới **xác** trước khi nấm của người chơi khác chiếm → +35 Dưỡng Chất, +linh khí.
- 10–16': hai con hươu người chơi kéo tới. Cây thả 2 quả Ngọt (30 Tinh) ở rìa lãnh thổ: một con ăn quả rồi đi (mang hạt đi, cây nhận Mầm Con ở 15 ô xa — **lợi**); con kia gặm lá → Độc Tiết + kiến → bỏ đi với 18 No.
- 16–22': giông kéo tới; cây đang ở bậc cao nhất trong 8 ô → nguy cơ sét. Chọn **thu Tán** (giảm 1 bậc tạm thời) thay vì liều.
- 22–28': Xuất Khiếu 2 phút tới Linh Tuyền gần đó hút 20 linh khí; về kịp khi bọ đục thân đẻ trứng.
- 28–30': đêm xuống → Bế Quan, chuyển 60 linh khí → tu vi.
→ Cây có **mất mát thực** (Tán, rủi ro sét, rủi ro hồn ảnh) và **quyết định thực** (quả hay độc, cao hay an toàn, đi xa hay ở nhà).

### SURV-08: Linh Khí như một tài nguyên sinh thái
- **Mật độ linh khí L0–L5** trên từng ô. Vùng ngoài L0–L1, giữa L2–L3, lõi rừng cổ L4–L5. Linh mạch (đường), Linh Tuyền (điểm), Linh Quả (vật phẩm) là nguồn tập trung.
- **Duy trì theo cảnh giới (upkeep):** mỗi đại cảnh giới cần mật độ tối thiểu; dưới mức → **Linh Khí Thất Thoát**.

| Cảnh giới | Mật độ tối thiểu | Hấp thu tĩnh tọa/phút ở mật độ đủ | Thất thoát khi dưới mức |
|---|---|---|---|
| R1–R2 | L0 | +3 | — |
| R3–R4 | L1 | +6 | −2/phút & tu vi đóng băng |
| R5–R6 | L2 | +12 | −6/phút, sau 10' bắt đầu −tu vi |
| R7–R9 | L3 | +25 | −15/phút, sau 5' −tu vi |

- **Cách dùng (đánh đổi):** (1) luyện thành tu vi khi Bế Quan, (2) đốt cho skill, (3) hồi thương (10 linh khí = 10% HP), (4) **lá chắn Độ Kiếp**, (5) *riêng cây:* "Linh Hóa Địa" — đầu tư 200 linh khí nâng +1 mật độ trong lãnh thổ rễ suốt 1 ngày thực → thu hút thú (đồng minh lẫn kẻ thù) và nấm tới.
- **Nguồn:** hấp thu môi trường, ăn/hấp thu sinh vật (chứa linh khí tích lũy), Linh Hạch từ xác, nút tranh chấp, sự kiện Linh Triều.
- **Vì sao tốt:** cây cổ thụ là **"máy phát linh khí"** của rừng → động vật có lý do sống cạnh cây lớn, cây có lý do chịu đựng thú. Mật độ ép kẻ mạnh vào sâu (SURV-11).

### SURV-09: Chuỗi thức ăn PvP & Sổ Năng Lượng (Trophic Ledger)
Mỗi sinh mệnh mang một lượng **Sinh Năng** = f(cảnh giới, tu vi hiện có). Khi chết, Sinh Năng chia **40 / 20 / 40**:
- **40% → kẻ ăn** (chỉ nhận được bằng hành động ăn/hấp thu, mất thời gian, bị ngắt được).
- **20% → Linh Hạch** rơi tại xác, **ai nhặt trước được** (đối thủ thứ ba có thể cướp).
- **40% → đất**, tỏa vào bán kính 3 ô trong thời gian phân rã; rễ cây và sợi nấm hấp thu.
- *(Linh hồn mang đi Đạo Tâm — tính riêng, không lấy từ pool này, PROG chốt.)*

**Ma trận "ai ăn ai"** — mỗi giới có ít nhất 1 kẻ săn và 1 con mồi:

| Kẻ hành động → Đối tượng | Thực vật | Ăn cỏ | Ăn thịt | Nấm |
|---|---|---|---|---|
| **Thực vật** | Che bóng, tranh rễ, thắt cổ (nhánh Đằng) | Nhánh **Thực Nhục Mộc**: bẫy dưới tán (Nắp Ấm, Bẫy Kẹp) | Nhánh Thực Nhục; hút xác | Hợp tác mycorrhiza / tranh xác |
| **Ăn cỏ** | Ăn lá (gây hại) **hoặc ăn quả** (cộng sinh) | Tranh cỏ, húc (lãnh thổ) | Phản công đàn (co-op), giẫm | Ăn thể quả (rủi ro độc) |
| **Ăn thịt** | Hầu như không (đào rễ ở nhánh Đào) | **Săn** — nguồn chính | Săn cùng loài lớn/nhỏ | Không ăn được (độc) |
| **Nấm** | **Mục rễ** (đánh Tâm Rễ yếu) | Nhánh **Đông Trùng**: ký sinh, DoT, nảy nấm khi chết | Ký sinh (chậm) | Tranh xác, cắt sợi |

- **Vì sao tốt:** PvP tự do không còn là "ai mạnh đánh người yếu" mà là **vòng tròn sinh thái**; một người chơi cây R4 có thể là thứ đáng sợ nhất với sói R3 lỡ chân dưới tán Nắp Ấm.

### SURV-10: Công bằng Cây ↔ Thú — kinh tế gặm cỏ
Nguyên tắc: **thú ăn cây được lợi ít hơn cây mất; cây không chết vì bị gặm, mà chậm lại.**

| Chỉ số (cùng cảnh giới) | Giá trị |
|---|---|
| Hiệu suất chuyển hóa lá → thú | **40%** (mất 10 Tinh-giá-trị lá → thú nhận 4) |
| Cỏ dại (không rủi ro) | +4 No/cắn, 0 linh khí |
| Lá cây người chơi | +6 No/cắn + 1 linh khí (lý do đi ăn cây người chơi) |
| Quả mời | +15 No + 3 linh khí, **cây được +1 hạt phát tán + phân bón tại chỗ thú đi qua** |
| Chi phí phòng thủ cho thú | Gai: −4 HP/cắn; Độc: ~−12 HP + chậm; Kiến: −3 HP/s tới khi rời ô rễ |
| Mục tiêu cân bằng (simulate) | Thú gặm 60s cây có phòng thủ: nhận ≈ 1.5× giá trị 60s cỏ dại nhưng mất ~25% HP. Cây mất ≈ 8–10 phút quang hợp, **không** mất Tâm Rễ |
| Hạ cây (Thân về 0) | Cần ≥1 cảnh giới **cao hơn** cây hoặc 3+ thú phối hợp ≥2 phút, hoặc lửa/sét |
| Giết cây (Tâm Rễ) | Chỉ: hạn, lửa lớn, nấm mục, thú nhánh Đào, rễ đối thủ, Thiên Kiếp |

- **Ngược lại — cây săn thú:** nhánh Thực Nhục Mộc có Nắp Ấm/Bẫy Kẹp đặt trên ô rễ (vô hình với thú thấp hơn 1 cảnh giới trở xuống trừ khi có skill khứu giác). Bẫy giữ 3s + tiêu hóa 5% HP/s; cây nhận 40% Sinh Năng nếu giết. Giới hạn 2 bẫy/R1, hồi 60s.
- **Tình huống:** Hươu người chơi R3 thấy cây Sồi R3 có Tán đầy linh khí. Nó có thể (a) ăn quả cây đang treo → no nhanh, an toàn, giúp cây; (b) gặm lá → ăn được 40s rồi dính độc, kiến kéo đến. Cả hai đều hợp lệ; cái nào cũng có câu chuyện.

### SURV-11: Chống bắt nạt bằng luật sinh thái (không vùng cấm PvP)
| Cơ chế | Quy tắc | Tác động |
|---|---|---|
| **Linh Khí Đói** (từ SURV-08) | R5+ ở vùng ngoài (L0–L1) thất thoát linh khí, sau 10' mất tu vi | Kẻ mạnh **không muốn** ở lâu vùng tân thủ |
| **Sát Nghiệp** | Giết sinh vật **thấp hơn ≥2 đại cảnh giới**: kẻ giết chỉ nhận **10%** Sinh Năng (thay 40%), +1 Nghiệp. Mỗi Nghiệp: Thiên Kiếp kế tiếp +15% sát thương, hào quang đỏ thấy được 20 ô, AI Hộ Rừng ưu tiên tấn công. Nghiệp giảm 1/ngày thực | Săn người mới vừa vô lợi vừa nguy hiểm — rất "tiên hiệp" |
| **Ấu Thể Ẩn Khí** | R1–R2 không hiện trên Thần Thức (radar) của kẻ cao hơn ≥2 cảnh giới; chỉ thấy bằng mắt trong 5 ô | Người mới không bị "định vị" từ xa |
| **Thoát Sinh** | Sống sót khi bị kẻ săn cao hơn đuổi (gây sát thương rồi thoát 30s) → +tu vi bằng 5% Sinh Năng kẻ săn | Bị săn mà sống = có thưởng → con mồi có lý do chơi tiếp |
| **Thiên Đạo Áp Chế** (chỉ server Rừng Non) | Chỉ số trần ở mức R3 | Server nhỏ thân thiện mà vẫn PvP |

### SURV-12: Lãnh thổ, Hang ổ và quy tắc offline
**Cây — Mạng Rễ:** ô rễ = lãnh thổ (nước, dưỡng chất, linh khí, cảm ứng). Hai mạng rễ giáp nhau → **tranh ô**: bên có Tinh đầu tư/ô cao hơn sau 30s chiếm ô. Không có tường — **rễ là tường**.
**Thú — Hang Ổ:** 1 hang/người chơi, đặt ở hang đá, hốc cây (**hốc cây của người chơi cây** → hợp đồng cộng sinh: cây được +phân bón & cảnh báo, thú được nơi trú ẩn), bụi gai. Cấp Hang 1–4 (vật liệu thu thập: lông, cành, đá linh): kho thức ăn (thịt thối sau 10 phút trừ khi Hang cấp 3 "hầm lạnh"), Bế Quan ×1.5, ổ **Huyết Noãn** (neo luân hồi).
**Nấm — Vòng Tiên:** vòng nấm tự nhiên = điểm Bế Quan và neo bào tử.

**Quy tắc offline (bắt buộc cho thế giới online có cây đứng yên):**
| Loài | Khi offline |
|---|---|
| Thú trong Hang | Biến mất khỏi thế giới; Hang vẫn có thể bị phát hiện/phá kho nhưng thân **không** bị giết |
| Thú ngoài Hang | Thân ở lại **30s** ("Hồn Thoát") rồi mới ẩn → chống combat-logging |
| Cây | **Nhập Định:** Tâm Rễ & Thân bất tử; Tán mất tối đa **20%**/lần offline; tu vi không giảm. Quang hợp offline 25% tốc độ, trần 8 giờ |
| Mùa Đông (cây) | Tùy chọn **Ngủ Đông**: rụng Tán, Thủy decay 0, miễn nhiễm ăn lá, nhưng không tu luyện |

- **Vì sao tốt:** cây không bị "giết lúc ngủ" — đó sẽ là lý do số 1 người chơi cây bỏ game.

### SURV-13: Hệ sinh thái mối đe dọa AI + "Ý Chí Rừng" (Director)
Giới hạn **6 archetype AI** (tái dùng skin theo vùng) để vừa sức 1 người + AI:

| Archetype | Ví dụ | State machine | Ai sợ nó |
|---|---|---|---|
| Ăn cỏ đàn | Hươu Sừng Ngọc | Graze → Alert → Flee (đàn) | Cây |
| Kẻ săn | Báo Bóng Đêm | Idle → Curious → Stalk → Attack → Eat/Flee (HP<30%) | Thú nhỏ |
| Bầy côn trùng | Sâu Lửa, Châu Chấu | Spawn → Swarm → Consume → Disperse | Cây |
| Ký sinh tĩnh | Tơ Hồng Yêu | Dormant → Attach → Drain | Cây |
| Ăn xác | Quạ Linh, Linh Cẩu | Circle → Wait (HP mục tiêu thấp) → Steal | Ai vừa giết |
| Hộ Rừng / Yêu Thú (boss) | Cổ Hùng Giữ Suối | Guard → Warn → Attack → Return | Kẻ mang Nghiệp, kẻ xâm bí cảnh |

**Ý Chí Rừng (Director):** tính **Áp Lực** của từng người chơi (0–100) = f(HP, needs, khoảng cách tới Hang/Tâm Rễ, số kẻ thù gần). Áp Lực <30 trong 5 phút → tăng spawn áp lực (đàn hươu, quạ, sâu). Áp Lực >75 → không spawn mới quanh người đó trong 3 phút, mở một "cửa thoát" (quả rơi, mưa xóa mùi). Solo: Director quản cả "PvP" bằng AI đối thủ cùng loài người chơi.

### SURV-14: Mối đe dọa môi trường
- **Đêm:** kẻ săn AI +50% số lượng; ăn thịt người chơi +30% tầm nhìn; cây không quang hợp → đêm là lúc **cây phòng thủ, thú săn**.
- **Lửa:** chỉ ở Hạ/Thu khô hoặc sét. Lan 1 ô/8s trên ô khô, 1 ô/30s ô ẩm, không qua suối. Cây: Tán cháy −10/s, Thân −5 HP/s. Nhánh "Vỏ Dày" giảm 60%; nhánh "Nhựa Thông" tăng gấp đôi (đánh đổi: nhựa là phòng thủ mạnh chống côn trùng). Sau cháy: ô thành **Tro Màu** (Dưỡng Chất ×3 trong 2 ngày thực) → **diễn thế sinh thái**: rừng tái sinh nhanh, cây non đầu thai vào đây có lợi.
- **Sét (Giông):** mỗi 20s đánh vật cao nhất trong bán kính 8 ô, 30% Thân max. Thú đứng dưới cây bị đánh lan 20 HP.
- **Lũ:** ô trũng ngập 3 phút: thú bơi −Thể Lực ×2, nấm/rễ ngập úng.

### SURV-15: Cái chết → Xác → Dinh dưỡng → Luân hồi
**Phân rã xác:**
| Kích thước | Thời gian xác tồn tại | Ghi chú |
|---|---|---|
| Nhỏ (thỏ, nấm) | 3 phút | |
| Vừa (sói, hươu) | 6 phút | Quạ AI đến sau 60s |
| Lớn (gấu, R5+) | 12 phút | Hút người chơi xung quanh → hot zone |
| **Cổ thụ R5+ đổ** | **Mộc Mộ**: tồn tại 2 ngày thực | Mật độ linh khí +2 quanh 5 ô, Dưỡng Chất cao; người luân hồi chọn "đầu thai tại Mộc Mộ" nhận +20% tốc độ tu vi R1–R2. **Cái chết của kẻ lớn trở thành landmark nuôi thế hệ sau** |

**Màn Luân Hồi — 2 lựa chọn:**
1. **Đầu thai Hậu Duệ** (cùng loài, tại neo: Mầm Con / Huyết Noãn / Bào Tử): giữ cảnh giới **giảm 1 tiểu cảnh**, mất đồ trong kho cá nhân, giữ Hang/lãnh thổ còn lại. Neo phải còn sống (đối thủ có thể phá neo trước khi bạn giết thân chính → chiến thuật "tận diệt").
2. **Đầu thai Loài Khác**: về R1 loài mới, mang theo **Đạo Tâm** (meta; PROG chốt tỷ lệ), nhận **Tiền Kiếp Gia Tốc** ×2 tu vi cho tới khi đạt 50% đỉnh cảnh giới kiếp trước.

**Cost of death (mục tiêu):**
| Cảnh giới khi chết | Thời gian đã đầu tư vào thân | Mất nếu có neo | Mất nếu không neo / đổi loài | Hồi phục ước tính |
|---|---|---|---|---|
| R1–R2 | 0–2h | ~10 phút | toàn bộ thân (rẻ) | <1 session |
| R3–R4 | 4–15h | ~1 session (30–45') | còn Đạo Tâm + gia tốc ×2 | 2–4 session |
| R5–R6 | 20–50h | ~2 session | như trên | ~1 tuần |
| R7+ | 60h+ | ~3 session | như trên | ≤2 tuần |

→ Đủ đau để PvP có ý nghĩa, không bao giờ > 2 tuần để quay lại vùng đã mất. **Chống death spiral:** sau chết, 10 phút **Hồn Hộ** (kẻ cao hơn ≥1 cảnh giới không nhận Sinh Năng khi giết bạn lần nữa → không có lý do camp).

### SURV-16: Độ Kiếp như thử thách sinh tồn công khai
- Khi đủ tu vi đại cảnh giới, người chơi **chọn thời điểm & địa điểm** (không bắt buộc ngay). Mây kiếp xuất hiện **60s trước**, thấy được trong 30 ô → mọi người biết. Kẻ thù có thể đến phá, đồng đội có thể **Hộ Pháp** (đỡ sét, đuổi kẻ phá).
- Ví dụ R3→R4: 3 đợt × 3 sét, mỗi sét 25% HP max, linh khí đốt làm khiên (1 linh khí = 1 HP). Cộng +15% sát thương/Nghiệp.
- **Cây:** không chạy được → phải **chuẩn bị**: rễ vào ô ẩm (dẫn sét xuống đất, −20% sát thương), Tích Lôi Mộc (nhánh skill), hạt dự phòng. Đây là lúc cây "hùng tráng" nhất.
- Thất bại không chết (trừ khi HP = 0): **Kiếp Thương** −10% tu vi, chờ 24h thực.

### SURV-17: Sự kiện lớn toàn rừng như mối đe dọa
Quy tắc: **báo trước 24h thực** (điềm báo trong rừng + UI), cảnh báo 10 phút trước khi bắt đầu, **mỗi sự kiện có kẻ thắng và kẻ thua theo giới** → không giới nào luôn chịu thiệt.

| Sự kiện | Thời lượng | Tần suất | Ai khổ | Ai lợi | Phần thưởng/di sản |
|---|---|---|---|---|---|
| **Đại Hạn** | 6h thực | 1/mùa Hạ | Cây (Thủy ×2.5), nấm | Ăn thịt (thú tụ ở suối = bãi săn) | Cây sống qua: +"Hạn Căn" (kháng hạn vĩnh viễn kiếp này) |
| **Sâm Lâm Hỏa Kiếp** | 2h | Hạ/Thu, do sét | Cây, ổ trên mặt đất | Nấm & cây non sau đó (tro ×3) | Vùng cháy → diễn thế, mở lối vào bí cảnh dưới tro |
| **Linh Triều** | 2h | 1/tuần | — | Ai chiếm Linh Mạch (L+2) | Tu vi bùng nổ → PvP tập trung |
| **Thú Triều** | 1h, đi từ lõi ra ngoài | 2/mùa | Thú nhỏ, Hang vùng ngoài | Cây (xác thú triều = dưỡng chất), ăn xác | Linh Hạch yêu thú |
| **Trùng Tai** | 3h | 1/mùa Xuân | Cây (Tán) | Thú ăn côn trùng, cây có kiến | Mật kiến/ong |
| **Đại Di Cư** | 4h | Thu | Ăn cỏ (bị săn) | Ăn thịt, cây trên đường đi (phân bón) | Ăn cỏ đi hết đường di cư: +tu vi lớn |
| **Khô Mục Xâm Lấn** (hook lore cho WORLD) | Lan dần nhiều ngày | Theo season | **Tất cả** | — | Cần toàn server hợp lực (cây chặn bằng rễ, nấm phân giải, thú tiêu diệt nguồn) |

### SURV-18: "Luyện Hóa" thay cho crafting + item sinks
Sinh vật không chế đồ. Thay vào đó có lớp crafting mỏng, chi phí sản xuất thấp:
- **Thiên Tài Địa Bảo** (Linh Thảo, Huyết Tinh, Lôi Mộc Tâm) thu thập ở vùng trong → **Luyện Hóa** khi Bế Quan thành: mở nhánh tiến hóa, kháng tính (lửa/độc/hạn), vật liệu nâng Hang.
- **Item sinks:** Linh Hạch chưa luyện tự tan sau 30 phút; thịt trong kho thối sau 10 phút; quả rụng sau 5 phút; ô rễ không đầu tư bị "teo" −1 ô/ngày khi Thủy <30. → không có kho vô hạn, không lạm phát.

### SURV-19: Tension graph (1 ngày game = 20 phút)
```
Căng
 100|                                  ▲Đêm: săn/phòng thủ
  75|               ▲Trưa: đi xa       ███
  50|        ▄▄▄▄██████▄           ▄████████▄
  25|  ▄▄▄███                ▄▄▄██           ██▄   ▼Bế quan
   0|██_______________________________________________█__
     0'   3'   6'   9'   12'  (Hoàng hôn 12–14') 14'  17'  20'
     Bình minh: sương, ăn, thả   →  Đi xa / mở rộng  →  Rút về  →  Đêm  →  Release
```
- Session dài (60') = 3 đỉnh; Director (SURV-13) bảo đảm mỗi 20' có ≥1 đỉnh >60 và ≥1 đáy <25.

## 4. Kết nối với các domain khác
- **PROG:** cần tỷ lệ Đạo Tâm giữ lại, công thức Sinh Năng theo cảnh giới, tu vi/phút mục tiêu cho từng giới sao cho cây (thu nhập ổn định, ít bùng nổ) ≈ thú (thu nhập dao động) trong ±15% sau 1 giờ chơi. Tôi đề xuất PROG chạy simulation trong `sim/` cho SURV-10 và SURV-15.
- **WORLD:** đặt tên/lore cho 6 archetype AI, Khô Mục, Mộc Mộ, Ý Chí Rừng; phân bố L0–L5 theo vùng ngoài→trong; xác nhận chu kỳ mùa 2 ngày thực.
- **PX:** (1) cây phải chơi được bằng cảm ứng: Vệt Nắng = tap, rễ = kéo, phòng thủ = 4 nút; (2) đánh giá chi phí 6 archetype AI + 3 giới; (3) FTUE: Director nên script một đợt ăn lá ở phút 4–6 cho cây mới và một cuộc săn hụt ở phút 5 cho thú mới; (4) rewarded ads **không được** hồi HP/needs giữa PvP — chỉ ngoài combat (vd tăng tốc Bế Quan).
- **Đề xuất MVP loài (từ góc sinh tồn):** Cây thân gỗ, Ăn cỏ, Ăn thịt, Nấm = 4 giới tạo đủ vòng tròn sinh thái. Cỏ/thảo mộc là ứng viên tốt cho loài "đời ngắn" (sống nhanh chết nhanh, roguelite) nếu còn ngân sách.

## 5. Rủi ro tự nhận diện
1. **Cây vẫn có thể nhàm** nếu Vệt Nắng thành chore. Kiểm chứng: playtest 20 người, đo % thời gian cây "không có hành động có nghĩa" — mục tiêu <25% thời gian ban ngày.
2. **Tôi có thể đang quá khắc nghiệt:** No ăn cỏ −6.7/phút có thể khiến mobile player bận ăn liên tục. Phương án dự phòng: −1/12s và tăng giá trị cỏ.
3. **Quy tắc offline của cây** (bất tử Tâm Rễ) có thể bị lợi dụng: offline-tank để giữ lãnh thổ. Giải: ô rễ của cây offline >48h bị "teo" dần.
4. **Sát Nghiệp** có thể bị lách bằng tài khoản phụ cố tình làm mồi (farm). Giải: Sinh Năng nhận từ cùng 1 nạn nhân giảm 50% mỗi lần trong 24h.
5. **Mật độ server:** chuỗi thức ăn PvP chỉ sống được khi đủ người chơi mỗi giới. Nếu tỷ lệ lệch (90% chọn sói), Director phải bù AI con mồi. Cần cơ chế "Thiên Đạo cân bằng" (thưởng đầu thai loài thiếu) — chờ PROG/PX.
6. **Chi phí:** 3 hệ needs khác nhau + lưới ô sinh thái. Tôi tin rẻ hơn 3 hệ combat, nhưng PX nên kiểm.

## 6. Câu hỏi mở
1. Cây chết thật có nên **luôn** để lại Mộc Mộ (kể cả R1) hay chỉ R5+? (Tôi nghiêng R5+ để Mộc Mộ hiếm và có nghĩa.)
2. Có cho **thú người chơi làm tổ trong hốc cây người chơi** ngay MVP không? Đây là tương tác cộng sinh mạnh nhất nhưng cần UI hợp đồng.
3. Solo mode: giữ nguyên decay hay giảm 20% vì không có đồng đội?
4. Độ Kiếp có bắt buộc sau X giờ ở đỉnh cảnh giới không (kiểu "kiếp tự tìm đến") — tăng áp lực nhưng có thể gây ức chế?
5. Nghiệp có nên ảnh hưởng **loài được phép đầu thai** ở kiếp sau (sát nghiệp nặng → chỉ được đầu thai loài thấp) — rất hợp chủ đề luân hồi, cần WORLD/PROG quyết.
