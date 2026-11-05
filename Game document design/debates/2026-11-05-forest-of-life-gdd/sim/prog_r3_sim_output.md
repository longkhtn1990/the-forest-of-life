# PROG R3 — kết quả mô phỏng (`python3 sim/prog_r3_sim.py`)

## N. Thất Cảnh v2 — 6 cảnh giới cày × 3 tầng + C7 Thành Thần (Thiên Kiếp ở cuối C6)
| C | Khung | Vùng | CT tầng Sơ/Trung/Hậu | CT cả cảnh | Kiếp rời cảnh (CT) | Lũy kế khi xong cảnh (gồm kiếp) | Phiên Mid trong cảnh | Tuần Casual | Tuần Mid | Tuần Core |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Khai Linh | Rừng Non (Bìa) | 11/12/13 | 36 | Tiểu Kiếp (5) | 41 | 0.6 | 0.3 | 0.1 | 0.1 |
| 2 | Tụ Linh | Rừng Non (Bìa→Trung) | 30/33/37 | 100 | Tiểu Kiếp (15) | 156 | 1.6 | 1.2 | 0.5 | 0.3 |
| 3 | Trúc Cơ | Rừng Non (Trung Lâm) | 54/59/67 | 180 | Trung Kiếp (Phi Thăng → Nguyên Sinh) (30) | 366 | 2.8 | 2.9 | 1.1 | 0.6 |
| 4 | Kết Đan | Nguyên Sinh / MVP: Linh Lâm | 84/92/104 | 280 | Trung Kiếp (45) | 691 | 4.4 | 5.4 | 2.2 | 1.2 |
| 5 | Hóa Hình | Nguyên Sinh / MVP: Linh Lâm | 114/125/141 | 380 | Đại Kiếp (Phi Thăng → Cổ Đại) (70) | 1141 | 5.9 | 8.9 | 3.6 | 2.0 |
| 6 | Xuất Khiếu | Cổ Đại | 156/172/192 | 520 | Thiên Kiếp (Thần Cách) | 1661 | 8.1 | 13.0 | 5.2 | 2.9 |

Tổng tới Thiên Kiếp: **1661 CT**. Giờ chơi thực Mid: **17.3 h** (Cửu Cảnh R2: 1671 CT/17.4 h; R1: 2089 CT/21.8 h).
Tầng dài nhất: 192 CT = 3.0 phiên Mid. Cửu Cảnh R2: 104 CT = 1.6 phiên.
MVP (hết C5 + Đại Kiếp Phi Thăng): 1141 CT = 3.6 tuần Mid / 2.0 tuần Core / 8.9 tuần Casual.

### So sánh 7 vs 9 cảnh: số phiên Mid giữa hai lần đột phá đại cảnh giới
| | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | Trung bình | Max | Số bộ (tên × loài, kiếp, Thần Thông...) phải làm |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Thất Cảnh v2 | 0.6 | 1.6 | 2.8 | 4.4 | 5.9 | 8.1 | — | — | 3.9 | 8.1 | 7 cảnh × loài |
| Cửu Cảnh R2 | 0.6 | 1.4 | 2.5 | 3.0 | 3.3 | 3.6 | 4.1 | 4.4 | 2.8 | 4.4 | 9 cảnh × loài (+29%) |

### Phiên đầu tiên (người mới, thời gian thực)
FTUE Linh Thử dùng đường cong kịch bản riêng (PX-08): tầng 1/2/3 ở phút 2/4/6, Tiểu Kiếp → C2 ở phút 7, chết/Thọ Nguyên ở phút 14–16.
- phút 20: cây xong tầng 1
- phút 23: cây xong tầng 2
- phút 29: cây xong C1 + Tiểu Kiếp → C2
- phút 60: cây xong C2 Sơ
(Phiên 2+: Mộng Tích ×2 cho 30' đầu; C2 cần ~1.5 phiên, C3 Huyết Mạch ở phiên 3.)

## O. TTK — thú vs thú và thú vs cây HP 3 lớp (n=10 = C4 Sơ, mọi chỉ số ×1.10/tầng)
Lang: HP 420, Công 50, d 0.40 · Linh Thử: HP 300, Công 26, d 0.30 · Linh Mộc: Thân = 3×420 (Tốc 0 → ×3), Tán = 0.5×Thân, Tâm Rễ = 0.5×Thân, Công 30, d 0.80.
Hệ số DPS chuỗi đòn Lang ≈ 1.56×Công/s (đánh thường + Huyết Trảo + chảy máu + Lang Nha).

### O1. Thú vs thú (không né, không kỹ năng phòng thủ)
| Tình huống | TTK (s) | % HP mất trong 2s mở màn |
|---|---|---|
| Lang vs Lang cùng tầng (C4 Sơ) | 7.5 | 26% |
| Lang vs Lang, khắc hệ | 6.0 | 32% |
| Lang vs Lang thấp hơn 1 cảnh | 5.3 | 37% |
| Lang vs Linh Thử cùng tầng | 5.0 | 38% |
| Lang vs Linh Thử thấp hơn 1 cảnh | 3.5 | 54% |

### O2. Sói đánh cây (Monte Carlo 400 trận/ô; cây phản ứng: Vỏ Cứng −50% 5s/CD 15s, trễ phản ứng 1.5–2.5s; rễ quất 0.5×Công/s; gai 10%; sói hút máu 10%, rút lui khi HP <35%)
| Kịch bản | Cây | Thời gian tới Đổ — nếu sói không rút (s) | P(cây Đổ) có luật rút lui | Trung vị t Đổ khi Đổ (s) | Kết cục Tâm Rễ |
|---|---|---|---|---|---|
| 1 Lang cùng tầng, trung tính | Linh Mộc | 54 | 0% | — | không chạm được → mọc lại sau Mộc Tàn 120s |
| 1 Lang cùng tầng, **khắc hệ ×1.25** (vd Huyết Lang Hỏa → cây hệ Kim) | Linh Mộc | 43 | 0% | — | không chạm được → mọc lại sau Mộc Tàn 120s |
| 1 Lang khắc hệ, **cây AFK** (không Vỏ Cứng) | Linh Mộc | 35 | 0% | — | không chạm được → mọc lại sau Mộc Tàn 120s |
| 1 Huyết Lang (Hỏa) vs **Thiết Mộc** (Kim, gai 25%) | Thiết Mộc | 43 | 0% | — | không chạm được → mọc lại sau Mộc Tàn 120s |
| 1 Lang cao hơn 1 cảnh (C5 Sơ), trung tính | Linh Mộc | 36 | 100% | 36 | không chạm được → mọc lại sau Mộc Tàn 120s |
| 2 Lang cùng tầng, trung tính | Linh Mộc | 27 | 100% | 27 | không chạm được → mọc lại sau Mộc Tàn 120s |
| 3 Lang cùng tầng, trung tính | Linh Mộc | 17 | 100% | 17 | không chạm được → mọc lại sau Mộc Tàn 120s |
| 3 Lang + 1 Độn Thử (Căn Thương 1%/s, ×2 khi Mộc Tàn) | Linh Mộc | 17 | 100% | 17 | chết thật 100% (trung vị 50s sau Đổ) |
| 2 Lang + Đại Hỏa (lửa 2%/s Tâm Rễ) | Linh Mộc | 27 | 100% | 27 | chết thật 100% (trung vị 25s sau Đổ) |

## P. Chi phí chết — chết ở giữa tầng Trung của mỗi cảnh (Mid 64 CT/phiên, 320 CT/tuần)
| Chết tại | Đã đầu tư (giờ Mid) | **Trùng Tu** tại neo: về đầu tầng, trần 130 CT (phiên) | R1 Luân Hồi ×3/×1.5 (phiên) | **Luân Hồi ×4/×2** (phiên) | ×4/×2 (tuần Mid) | Đạo Quả nhận khi Luân Hồi (25% CT lũy kế) |
|---|---|---|---|---|---|---|
| C2 Tụ Linh | 0.9 h | 0.3 | 0.7 | 0.5 | 0.10 | 22 |
| C3 Trúc Cơ | 2.5 h | 0.5 | 1.7 | 1.3 | 0.25 | 60 |
| C4 Kết Đan | 5.2 h | 0.7 | 3.3 | 2.4 | 0.49 | 124 |
| C5 Hóa Hình | 9.0 h | 1.0 | 5.4 | 4.1 | 0.82 | 217 |
| C6 Xuất Khiếu | 14.4 h | 1.3 | 8.5 | 6.3 | 1.27 | 346 |
| C6 Hậu viên mãn (bị giết trong Thiên Kiếp) | 17.3 h | — | 11.4 | 8.5 | 1.70 | 830 (×2) |

Trần PX: Trùng Tu ≤2 phiên ✔ ở mọi cảnh; Luân Hồi ≤1 tuần (5 phiên) — xem cột ×4/×2.
Thiên Kiếp thất bại do sét (không bị người giết): mất 50% CT tầng Hậu C6 = 96 CT = 1.5 phiên, thử lại sau 1 phiên online (Kiếp Thương).

## Q. Monte Carlo Kiếp server — 3000 người/ô; 45% Casual / 40% Mid / 15% Core; 40% vào muộn (đều trong 80% đầu Kiếp)
Chết/giờ chơi: 0.08 (C1–3), 0.06 (C4–5), 0.05 (C6). Khi chết: neo còn (75%, không dùng trong 24h) → 65% chọn Trùng Tu (về đầu tầng, trần 130 CT), còn lại Luân Hồi (×4 tới hết cảnh đỉnh−1, ×2 tới đỉnh). C6 không neo: Nguyên Thần Bất Diệt 50%.
Thiên Kiếp: 10% bị đánh úp chết thật; còn lại thành công 60/75/90/95%; thất bại do sét = −50% tầng Hậu, chờ 1 phiên. Bonus cộng dồn trần ×3 (×4 khi Hồi Ức). Thiên Đạo Bù Đắp +0.5 khi dưới 60% tiến độ Mid tham chiếu (chốt R3).
| Chế độ | Kiếp (ngày) | Hồ sơ | % xong Rừng Non (C3) | % vào C5 Hóa Hình | % Phi Thăng Cổ Đại (xong C5 + Đại Kiếp) | % chạm Thiên Kiếp | % Thành Thần | Trung vị ngày tới Thiên Kiếp | % người vào đầu Kiếp đạt mục tiêu cuối | Chết TB | % lần chết là Luân Hồi |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MVP (trần C5) | 28 | Casual 3×25' | 81% | 9% | 0% | — | — | — | 0% | 0.3 | 50% |
| MVP (trần C5) | 28 | Mid 5×40' | 99% | 89% | 52% | — | — | — | 75% | 0.7 | 54% |
| MVP (trần C5) | 28 | Core 7×60' | 100% | 99% | 85% | — | — | — | 100% | 1.4 | 49% |
| MVP (trần C5) | 42 | Casual 3×25' | 91% | 69% | 0% | — | — | — | 0% | 0.5 | 49% |
| MVP (trần C5) | 42 | Mid 5×40' | 100% | 97% | 87% | — | — | — | 99% | 1.1 | 48% |
| MVP (trần C5) | 42 | Core 7×60' | 100% | 100% | 96% | — | — | — | 100% | 2.0 | 48% |
| Đầy đủ | 42 | Casual 3×25' | 92% | 72% | 0% | 0% | 0% | — | 0% | 0.4 | 53% |
| Đầy đủ | 42 | Mid 5×40' | 100% | 96% | 85% | 52% | 41% | 35 | 73% | 1.1 | 52% |
| Đầy đủ | 42 | Core 7×60' | 100% | 100% | 97% | 87% | 81% | 21 | 100% | 1.7 | 51% |
| Đầy đủ | 48 | Casual 3×25' | 93% | 77% | 18% | 0% | 0% | — | 0% | 0.5 | 52% |
| Đầy đủ | 48 | Mid 5×40' | 100% | 98% | 89% | 66% | 53% | 35 | 87% | 1.2 | 50% |
| Đầy đủ | 48 | Core 7×60' | 100% | 100% | 99% | 92% | 88% | 20 | 100% | 1.7 | 52% |
| Đầy đủ | 56 | Casual 3×25' | 97% | 83% | 55% | 0% | 0% | — | 0% | 0.6 | 50% |
| Đầy đủ | 56 | Mid 5×40' | 100% | 99% | 91% | 78% | 68% | 35 | 95% | 1.2 | 51% |
| Đầy đủ | 56 | Core 7×60' | 100% | 100% | 100% | 93% | 90% | 20 | 100% | 1.9 | 55% |
| Đầy đủ | 63 | Casual 3×25' | 98% | 86% | 61% | 0% | 0% | 62 | 0% | 0.6 | 48% |
| Đầy đủ | 63 | Mid 5×40' | 100% | 100% | 94% | 83% | 76% | 35 | 99% | 1.3 | 54% |
| Đầy đủ | 63 | Core 7×60' | 100% | 100% | 100% | 96% | 94% | 20 | 100% | 1.7 | 55% |

### Q2. Độ nhạy: Kiếp 56 ngày, Mid — thay đổi hành vi chọn Trùng Tu / tỉ lệ neo còn
| Neo còn | Chọn Trùng Tu khi có neo | % Mid chạm Thiên Kiếp | % Mid Thành Thần | % lần chết là Luân Hồi |
|---|---|---|---|---|
| 75% | 65% | 78% | 68% | 52% |
| 75% | 95% | 82% | 72% | 35% |
| 50% | 65% | 78% | 68% | 64% |
| 0% | 0% | 70% | 60% | 90% |

### Q3. Độ nhạy Thiên Đạo Bù Đắp — Kiếp 56 ngày, Casual
| Ngưỡng (so với tiến độ Mid tham chiếu) | Bonus | % Casual vào C5 | % Casual Phi Thăng Cổ Đại | % Mid chạm Thiên Kiếp |
|---|---|---|---|---|
| 40% | +0.5 | 82% | 3% | 75% |
| 60% | +0.5 | 83% | 54% | 78% |
| 60% | +1.0 | 87% | 66% | 84% |
| 0% | +0.0 | 74% | 2% | 72% |

## R. PvP theo chênh lệch (×1.10/tầng → ×1.33 chỉ số, ×1.77 combat power mỗi cảnh; nhiễu kỹ năng σ=0.40)
| Chênh | Combat power | P(1 thấp thắng) | P(2 thấp thắng) | P(3 thấp thắng) |
|---|---|---|---|---|
| 1 tầng | ×1.21 | 37% | 99% | 100% |
| 1 cảnh | ×1.77 | 15% | 96% | 100% |
| 2 cảnh | ×3.14 | 2% | 70% | 99% |
| 3 cảnh | ×5.56 | 0% | 26% | 86% |
| 4 cảnh | ×9.85 | 0% | 4% | 44% |

Áp Chế Rừng Non: C6 Hậu (n=18→9) vs C2 Trung (n=5): combat ×2.14 (không Áp Chế: ×11.9); P(C2 thắng 1v1) = 9%.

## S. Chia CT trong nhóm — tổng CT nhóm = 1 + 0.6·min(k−1, 2), chia đều
Giả định săn: tốc độ hạ mồi của bầy k con so với 1 con = 1, 1.35, 1.6, 1.75, 1.85 (thời gian tìm mồi dùng chung).
| k | R1 (85% + 10%/người) mỗi người | R3 mỗi người nhận / hành động | Tốc độ hạ mồi | CT/phút mỗi người (R1) | CT/phút mỗi người (R3) |
|---|---|---|---|---|---|
| 1 | 100% | 100% | ×1 | 1.00 | 1.00 |
| 2 | 95% | 80% | ×1.35 | 1.28 | 1.08 |
| 3 | 105% | 73% | ×1.6 | 1.68 | 1.17 |
| 4 | 115% | 55% | ×1.75 | 2.01 | 0.96 |
| 5 | 115% | 44% | ×1.85 | 2.13 | 0.81 |

## T. Thiên Đạo Gia Trì — cộng dồn kiểu cộng, trần ×3 (×4 khi đang Hồi Ức)
| Nguồn | + | 
|---|---|
| Mộng Tích/Tĩnh Tu (30' đầu phiên) | +1.0 |
| Thiên Đạo Bù Đắp | +0.5 |
| Loài thiếu <15% (PX-16) | +0.25 |
| Đầu thai tại Mộ Linh/Mộc Mộ | +0.2 |
| Linh Triều (sự kiện) | +1.0 |
| Đạo Quả Bàn 'Linh Căn' (trần) | +0.1 |

Tổng cộng thô: ×4.05 → áp trần ×3.0. Với Hồi Ức ×4 (= +3): ×7.05 → trần ×4.0. (R2 kiểu nhân: ×82.)
Exploit 'tự sát ở C2 Trung để lấy bonus': mất 88 CT tiến độ, cày lại tốn 34 phút ở ×4/×2; được thêm tối đa +25% (loài thiếu) trên một khoảng ≈ 30 phút → lãi ≤ 8 CT < chi phí 34 CT. **Không lãi.**

## U. Quỹ linh khí vùng (mô hình đồ chơi; 1 vùng Trung Lâm; Q=200 LK, dòng vào 1.2 LK/phút; ngày-rừng 24')
Rút: thú 1.0 LK/CT · cây 0.4 · nấm 0.2. Cây Linh Hóa Địa trả +0.6 LK/CT. 40% phần thú rút quay về đất (bán rã 48', có nấm 16'). Khô Linh <30%: thú CT ×0.5, cây/nấm ×0.8; 30–60%: ×0.85–1.0.
| Dân trong vùng (online liên tục 4h) | Khô Linh sau (phút / ngày-rừng) | Quỹ thấp nhất | Quỹ sau 4h |
|---|---|---|---|
| 4 thú săn | 68 / 2.8 | 29% | 29% |
| 3 thú săn | 146 / 6.1 | 30% | 30% |
| 2 thú + 1 cây + 1 nấm | không | 91% | 91% |
| 3 thú + 1 cây | 239 / 10.0 | 30% | 30% |
| 2 cây + 2 nấm | không | 100% | 100% |
Bìa Rừng: sàn quỹ 50% (SURV) → không bao giờ Khô Linh; hệ số CT tối thiểu ở Bìa = ×0.925.
