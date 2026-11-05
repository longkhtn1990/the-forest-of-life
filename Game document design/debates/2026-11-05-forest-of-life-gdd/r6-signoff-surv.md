# R6 Sign-off — SURV
**Verdict:** BLOCK (3 blocker. Cả 3 đều là lỗi logic sửa được bằng 1–2 câu luật, không tốn thêm tuần-người. Sửa xong là tôi APPROVE-WITH-NOTES)

> Phạm vi tôi đã đối chiếu: §3, §4.3–4.5, §5 (toàn bộ), §6.6, §7.1, §8, §10, D4/D7/D8/D18/D19, cùng mọi chỗ [orch] chạm vào domain SURV. Nguồn đối chiếu: `r3-revision-surv.md`, `r4-position-surv.md`.

---

## Blockers

| # | Vị trí trong FINAL | Vấn đề | Sửa cụ thể (đoạn thay thế viết sẵn) |
|---|---|---|---|
| **B1** | §6.6, gạch đầu dòng 2: *"Đánh Úp Kiếp cũng tính Sát Nghiệp như giết thường"*. Đối chiếu với D19 và §8 | **Mâu thuẫn nội tại, đồng thời thiếu một điều kiện của D19.** D19 ghi điều kiện bắt buộc *"kẻ giết người độ kiếp nhận Sát Nghiệp"*. Nhưng "như giết thường" lại đi theo bảng §8, mà ở đó Nghiệp chỉ sinh khi g≥2. Người độ kiếp Thiên Kiếp ở C6 nên gần như mọi kẻ phá kiếp đều có g≤0. Theo §8 họ được **Nghịch Thiên ×(1+0,5·\|g\|) và 0 Nghiệp**. *Tình huống:* một Lang C5 đánh úp Lang C6 đang độ Thiên Kiếp. Nạn nhân chết thật sau khoảng 5 tuần đầu tư, còn kẻ giết nhận ×1,5 CT, 0 Nghiệp và không có hào quang đỏ. Lỗ thứ hai: người độ kiếp vẫn gây 50% sát thương ra ngoài. Nếu họ đánh trúng kẻ phá trước, kẻ phá được hưởng miễn trừ "đánh trả trong 60s". Ở R4 tôi đã ghi rõ: thiếu điều kiện này thì BLOCK | **Thay gạch đầu dòng đó bằng:** *"**Đánh Úp Kiếp** là việc giết người đang ở trong vòng kiếp. (1) Không có thưởng Nghịch Thiên: m(g) trần ×1. (2) Không áp dụng miễn trừ 'đánh trả trong 60s', vì người độ kiếp không rời vòng được. (3) Nghiệp ở Tiểu Kiếp, Phi Thăng Kiếp I, Trung Kiếp và Phi Thăng Kiếp II tính theo bảng §8 như giết thường. (4) **Thiên Kiếp [Post]: kẻ giết luôn nhận +2 Sát Nghiệp, bất kể g.** Hộ Pháp giết kẻ phá kiếp thì được miễn trừ."* **Thêm 1 dòng vào bảng g của §8:** `| Đánh Úp Kiếp | m(g) trần ×1 | 100% | theo g. Thiên Kiếp: +2 bất kể g | — |`. Chi phí: luật dữ liệu, S, nằm trong hạng mục #13. |
| **B2** | §5.9, dòng *"Thoát game trong Hang/lãnh thổ rễ → Bế Quan ngay"* | **Lỗ combat-logging làm vỡ PvP với cây.** Lỗi này xuất phát từ SURV-12b của chính tôi. Cây **luôn** đứng trong lãnh thổ rễ của mình, nên khi đang bị đánh nó chỉ cần thoát game là vào Bế Quan ngay, và khi offline thì Thân cùng Tâm Rễ **bất tử**. *Tình huống:* 3 Lang cộng 1 Độn Thử phối hợp, làm cây Đổ ở giây 17. Người chơi cây bấm thoát và cây thành bất tử. Như vậy cả bảng TTK ở §4.3 ("muốn tận diệt cây cần phối hợp nhiều loài"), Build Card "Độn Thử · tận diệt" và H5 đều mất ý nghĩa. Thú cũng làm y như vậy: đang bị đuổi thì chạy vào Hang rồi thoát. Đây là lý do Rust phải giữ thân người chơi đang ngủ lại trong thế giới | **Thay 2 dòng đầu bảng §5.9 bằng:** `| Thoát game trong Hang/lãnh thổ rễ, **không gây và không nhận sát thương trong 30s gần nhất** | **Bế Quan** ngay. Thú rời thế giới, cây thành bất tử |` và `| Thoát khi vừa combat (kể cả trong Hang/lãnh thổ rễ), thoát ở chỗ khác, hoặc rớt mạng | **Nhập Định** 30s (**60s nếu vừa combat**). Thân ở lại thế giới và đánh được. Cây giữ phòng thủ thụ động (Gai và kiến tự kích), thú tự chạy vào bụi/hang ≤5 ô (PX-18). Hết Nhập Định thì Bế Quan |`. Cây đang Mộc Tàn không nhận sát thương vào Thân, nên sau 30s là vào được Bế Quan. Cây vẫn có lối thoát, chỉ là không thoát được ngay giữa trận. Chi phí: 1 điều kiện trong hạng mục #12, S. |
| **B3** | §4.3 (*"Thân = 0 → Đổ: mất Tán và 25% CT tầng hiện tại…"*) và §7.1 dòng **Cây Đổ** | **Bậc thang giá chết bị đảo.** "Đổ" được định nghĩa là "chưa chết", nên phải rẻ hơn Hậu Duệ (trần 130 CT). Nhưng Đổ lặp lại được mà không có giới hạn. *Tình huống:* 3 Lang cùng cảnh (g=0, nên 0 Nghiệp và 0 thưởng) cắm trại quanh một cây C4. Chu kỳ là Đổ ở giây 17, đợi Mộc Tàn 120s, cây mọc lại rồi Đổ tiếp, tức khoảng 137s mỗi lần. Mỗi lần mất 25% × 104 = 26 CT. Sau 5 lần (khoảng 11') cây đã mất 130 CT, **bằng một lần chết**. Sau 10 lần mất 260 CT, **gấp đôi trần chết**, mà cây không chạy được. Đây là griefing không tốn gì của kẻ tấn công, nhắm thẳng vào loài USP (persona P3 sợ đúng điều này) | **Thay câu ở §4.3 bằng:** *"**Thân = 0 → Đổ** (chưa chết): mất Tán và **25% CT tầng hiện tại, tối đa 1 lần mỗi 30' thực** (những lần Đổ khác trong 30' đó chỉ mất Tán). Cây vào **Mộc Tàn** 120s (không quang hợp, Căn Thương ×2) và mọc lại nếu Quang Tinh ≥30. Tổng CT mất vì Đổ trong 24h thực không vượt quá trần Hậu Duệ (130 CT). **Tâm Rễ = 0 mới là chết.**"* **Ở §7.1, dòng Cây Đổ, cột "Mất":** `Tán, 25% CT tầng (1 lần/30', tổng ≤130 CT/24h), Mộc Tàn 120s`. Kiểm chứng: sau khi sửa, 3 Lang cắm trại 1h chỉ lấy được 52 CT, ít hơn 1 lần chết, và cây vào được Bế Quan trong Mộc Tàn (xem B2). |

---

## Notes (không chặn)

| # | Vị trí | Ghi chú | Đề xuất / đoạn viết sẵn |
|---|---|---|---|
| N1 | §4.3 Hóa Hình Mộng · §10 E1 | Hóa Hình Mộng chỉ mở trong **cao trào 30'** của Đại Linh Triều, tức 30'/tuần vào một thứ cố định lúc 20:00, và chỉ cho cây C4. Tôi ước tính dưới 30% cây C4 sẽ từng thấy nó trong MVP. Khi đó câu "4/4 cách chơi thực vật có trong MVP", vốn là cơ sở của D6, chỉ đúng trên giấy. Người chỉ chơi cuối tuần thì **không bao giờ** gặp Linh Triều, vì Xuân luôn rơi vào cùng các ngày trong tuần | Sửa ở E1: *"Hóa Hình Mộng: trong pha nền 24h, mỗi đỉnh bình minh game (3') cây C4 có rễ trên Linh Mạch được Hóa Hình Mộng 3'. Trong cao trào thì kéo dài đủ 30'."* Không tốn code thêm vì chỉ đổi điều kiện kích hoạt. Từ [U1]: mỗi Kỷ Nguyên dời điểm bắt đầu năm-rừng +2 ngày để xoay thứ trong tuần. Thêm telemetry: tỉ lệ cây C4 đã từng Hóa Hình Mộng, mục tiêu ≥50% |
| N2 | §10 "Lịch năm-rừng 7 ngày (SURV R4)" | Ở R4 tôi viết "pha nền của mỗi sự kiện nằm gọn trong mùa của nó". **Câu đó sai.** Nếu "ngày 6" là giờ 120–144 thì nó lấn 6h vào Thu (Đông bắt đầu từ giờ 126). Hiện chỉ Linh Triều là MVP nên chưa gây hậu quả | Ghi lịch theo giờ của năm-rừng: **Linh Triều giờ 0–24** (Xuân 0–42) · **Đại Hạn giờ 48–72** (Hạ 42–84) · **Huyết Nguyệt giờ 132–156** (Đông 126–168) |
| N3 | §2.3 cột Linh Quỹ · §5.7 | "Hồi chậm" (Thâm Lâm) và "Giàu, tải cao" (Linh Nhãn) chưa có số. Thêm một rủi ro: Mid chạm trần C4 ở tuần 2,2 rồi dồn hết vào Thâm Lâm. Tôi ước tính tải 12–15 trên sức chứa 6, tức −35 đến −52%/h, nên toàn bộ Thâm Lâm có thể Khô Linh mỗi tối giờ cao điểm. FINAL cũng đã rơi mất tiêu chí sim mà tôi đặt ở R3 | Thâm Lâm: hồi nền **+2%/h** (thay vì +4). Linh Nhãn: sức chứa nền **10**, hồi **+6%/h**. Giao PROG chạy **agent sim 40 người × 7 ngày** với phân bố cảnh giới của tuần 3. Mục tiêu: Thâm Lâm Khô Linh ≤30% số giờ cao điểm, Bìa có CT <×0,8 trong <10% thời gian. Nếu trượt thì nâng sức chứa nền của Thâm Lâm lên 8 |
| N4 | §5.9 trần tổn thất offline | Chưa nói rõ neo có được bảo vệ khi chủ offline hay không. Nếu Mầm-Neo hoặc Huyết Noãn bị phá trong lúc chủ offline, lần chết kế tiếp sẽ bị **ép Luân Hồi mà người chơi không hiểu vì sao** | Thêm vào dòng trần tổn thất: *"Neo nằm trong mạng rễ hoặc trong Hang bất tử khi chủ offline. Mầm-Neo ngoài mạng rễ thì không, và Mộng Báo phải báo nếu neo bị phá."* |
| N5 | §7.1 điều kiện Luân Hồi | Danh sách điều kiện chưa có trường hợp "bị giết trong Thiên Kiếp", và chưa nói Nguyên Thần Bất Diệt (§6.7) có kích hoạt trong trường hợp đó không ([Post]) | Thêm: *"…hoặc bị sinh vật khác giết trong Thiên Kiếp. Khi đó Nguyên Thần Bất Diệt không kích hoạt."* |
| N6 | §4.3 Plant Pressure Map ("−2 lá/cắn"), §5.3 | Đơn vị "lá" chưa được quy đổi sang HP Tán | Quy ước **1 lá = 2 HP Tán** (Tán C1 60 HP = 30 lá). Giá mọc 1 lá vẫn là 2 Quang Tinh |
| N7 | §5.9 "nơi đặt Ổ Hậu Duệ" | Tên chưa khớp với §7.1 và glossary (Huyết Noãn / Ổ Hạt) | Đổi thành "nơi đặt neo **Huyết Noãn** (Lang) / **Ổ Hạt** (Linh Thử)" |
| N8 | §10 Linh Tức [orch] | Hệ số vẫn còn trống | Khuyến nghị PROG chốt **+0,25 Gia Trì**, để Linh Tức cộng thêm ≤3% CT/phiên và không thành lịch hẹn giờ kiểu FOMO |
| N9 | Các mục [orch] trong domain SURV | Đã duyệt và **đồng ý**: HUD thú không có Thủy (§5.1) · Diều hâu và sói AI trong FTUE là skin của archetype kẻ săn (§5.8) · tên Thâm Lâm (§2.2) · 3 biome dùng chung 1 tileset (§2.3) · Linh Thức lite 60s / 30 ô / CD 3' (§4.3). Mục Đạo Quả Bàn 3 node là domain PROG, tôi không xét | — |

---

## Nhất quán số liệu (tôi tự kiểm phần SURV)

| Kiểm tra | Kết quả |
|---|---|
| Lần Warning đói đầu tiên: Thử (100−59)/5 = 8,2' · Lang 41/4 = 10,25' | ✓ nằm trong mục tiêu 8–15' |
| Thủy = 0 → Tâm Rễ −1%/5s → chết héo sau 500s ≈ 8,3' | ✓ khớp "~8'" |
| Quang Tinh/ngày-rừng: 12'×6 = 72 · Vệt Nắng 14,4 vệt × 8s × 1,5 × 0,1 = 17,3 · đêm 6'×4 = 24 → +65 | ✓ |
| Khô Linh: 4 Lang C4 có tải 12, sức chứa 6 → −35%/h → 100→30% mất 2,0h | ✓ |
| 2 Lang C4 + 1 cây: tải 6,5 ≤ sức chứa 7 | ✓ không bao giờ Khô Linh (FINAL bỏ nấm vì nấm là [1.0], phép tính vẫn đúng) |
| Hậu Duệ tệ nhất: 130 / 1,5 = 86,7 CT = 1,35 phiên Mid | ✓ |
| 3 Lang + Độn Thử: Tâm Rễ 100% ÷ (1%/s × 2 trong Mộc Tàn) = 50s < Mộc Tàn 120s | ✓ khớp "chết thêm 50s" |
| D19: Luân Hồi từ C6 mất 1,28 tuần ≤ 1,5 · mây báo trước ≥60s, thấy trong 30 ô · có Hộ Pháp · tự chọn thời điểm | ✓, **trừ điều kiện Nghiệp → B1** |
| Đổ lặp lại so với trần chết 130 CT | ✗ → B3 |

---

## Dissent ghi nhận (chấp nhận, không chặn)
1. **Mùa 4→2 (D6):** vẫn giữ như §20.1. Tôi chấp nhận "4 palette, chỉ Xuân/Đông có modifier".
2. **D19 Thiên Kiếp chết thật:** dissent nhẹ có điều kiện vẫn đứng. Khi B1 được sửa thì đủ cả 5 điều kiện và tôi chấp nhận.
3. **Đổi ý, không phải dissent:** (a) ở R4 tôi muốn Hồi Ức nằm trong trần Gia Trì. Tôi nhận cách của PROG (Hồi Ức nằm ngoài trần), vì để trong trần thì Luân Hồi từ C5 tốn 1,38 tuần, vượt trần PX. (b) Đổ mất 25% CT tầng thay cho "mất 1 bậc chiều cao" của SURV-03b: tôi chấp nhận, với điều kiện có trần như B3.
