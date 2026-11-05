
## A. Bảng tầng tu vi
| n | Cảnh giới | Tầng | CT cần | Lũy kế CT | TV/phút hiển thị | TV cần (hiển thị) |
|---|---|---|---|---|---|---|
| 1 | 1·Khai Linh | Sơ | 4 | 4 | 10 | 40 |
| 2 | 1·Khai Linh | Trung | 11 | 15 | 12 | 137 |
| 3 | 1·Khai Linh | Hậu | 20 | 35 | 16 | 307 |
| 4 | 2·Tụ Linh | Sơ | 30 | 64 | 20 | 583 |
| 5 | 2·Tụ Linh | Trung | 41 | 106 | 24 | 1,007 |
| 6 | 2·Tụ Linh | Hậu | 54 | 159 | 31 | 1,640 |
| 7 | 3·Trúc Cơ | Sơ | 67 | 227 | 38 | 2,564 |
| 8 | 3·Trúc Cơ | Trung | 82 | 308 | 48 | 3,890 |
| 9 | 3·Trúc Cơ | Hậu | 97 | 405 | 60 | 5,768 |
| 10 | 4·Kết Đan | Sơ | 113 | 518 | 75 | 8,399 |
| 11 | 4·Kết Đan | Trung | 129 | 647 | 93 | 12,055 |
| 12 | 4·Kết Đan | Hậu | 147 | 794 | 116 | 17,096 |
| 13 | 5·Hóa Hình | Sơ | 165 | 959 | 146 | 23,999 |
| 14 | 5·Hóa Hình | Trung | 180 | 1139 | 182 | 32,742 |
| 15 | 5·Hóa Hình | Hậu | 180 | 1319 | 227 | 40,927 |
| 16 | 6·Xuất Khiếu | Sơ | 180 | 1499 | 284 | 51,159 |
| 17 | 6·Xuất Khiếu | Trung | 180 | 1679 | 355 | 63,949 |
| 18 | 6·Xuất Khiếu | Hậu | 180 | 1859 | 444 | 79,936 |

Tổng CT tầng: 1859; + Cơ Duyên/Độ Kiếp: 230; = 2089 CT
  Cảnh giới 1 (Khai Linh): 35 CT
  Cảnh giới 2 (Tụ Linh): 125 CT
  Cảnh giới 3 (Trúc Cơ): 246 CT
  Cảnh giới 4 (Kết Đan): 389 CT
  Cảnh giới 5 (Hóa Hình): 525 CT
  Cảnh giới 6 (Xuất Khiếu): 540 CT

## B. Lịch thời gian thực (tuần) để chạm mỗi cảnh giới — không tính chết
| Hồ sơ | CT/tuần | →C2 | →C3 | →C4 | →C5 | →C6 | →C7 |
|---|---|---|---|---|---|---|---|
| Casual 3×25' | 128 | 0.3 | 1.3 | 3.5 | 6.9 | 11.4 | 16.4 |
| Mid 5×40' | 320 | 0.1 | 0.5 | 1.4 | 2.7 | 4.6 | 6.5 |
| Core 7×60' | 567 | 0.1 | 0.3 | 0.8 | 1.5 | 2.6 | 3.7 |

Giờ chơi thực (Mid) để chạm C7: 21.8 h
  Phiên đầu: đạt hết tầng n=1 ở phút thực 3
  Phiên đầu: đạt hết tầng n=2 ở phút thực 9
  Phiên đầu: đạt hết tầng n=3 ở phút thực 21
  Phiên đầu: đạt hết tầng n=4 ở phút thực 46

## C. Chi phí luân hồi — chết ở giữa cảnh giới R, leo lại đến đúng chỗ cũ
Quy tắc Tiền Kiếp Hồi Ức: ×3 đến hết cảnh giới (đỉnh-1), ×1.5 đến đỉnh cũ, sau đó ×1. Overhead kiếp đã vượt chỉ tính 50%.
| Chết tại | CT mất (không catch-up) | CT leo lại (có catch-up) | Tuần (Mid) | Phiên 40' (Mid) | Đạo Tâm nhận |
|---|---|---|---|---|---|
| C2 Trung (Tụ Linh) | 64 | 31 | 0.10 | 0.5 | 40 |
| C3 Trung (Trúc Cơ) | 237 | 103 | 0.32 | 1.6 | 90 |
| C4 Trung (Kết Đan) | 553 | 228 | 0.71 | 3.6 | 160 |
| C5 Trung (Hóa Hình) | 1039 | 415 | 1.30 | 6.5 | 250 |
| C6 Trung (Xuất Khiếu) | 1639 | 630 | 1.97 | 9.8 | 360 |

## D. Monte Carlo tu vi/phút theo loài (phiên 40', 4000 lần) — trước và sau hiệu chỉnh k_s
| Loài | CT/phút thô | k_s | CT/phút sau hiệu chỉnh | P10 | P90 | Hệ số biến thiên |
|---|---|---|---|---|---|---|
| Linh Mộc | 0.92 | 1.09 | 1.00 | 0.81 | 1.21 | 16% |
| Linh Thảo | 0.73 | 1.37 | 1.00 | 0.82 | 1.19 | 14% |
| Lộc | 0.92 | 1.09 | 1.00 | 0.73 | 1.27 | 21% |
| Lang | 0.85 | 1.17 | 1.00 | 0.59 | 1.46 | 34% |
| Khuẩn | 1.04 | 0.96 | 1.00 | 0.59 | 1.49 | 34% |

## E. PvP — chênh lệch cảnh giới
| Chênh (tầng) | Hệ số chỉ số | Tỉ lệ sức mạnh (HP×DPS) | TTK cao→thấp so với cùng cấp | Số người thấp cần (Lanchester) | P(thấp thắng 1v1) | P(2 thấp thắng 1 cao) |
|---|---|---|---|---|---|---|
| 0 tầng | ×1.00 | ×1.00 | 100% | 1 | 50% | 100% |
| 1 tầng | ×1.10 | ×1.21 | 83% | 2 | 37% | 99% |
| 2 tầng | ×1.21 | ×1.46 | 68% | 2 | 25% | 98% |
| 3 tầng (=1 cảnh giới) | ×1.33 | ×1.77 | 56% | 2 | 15% | 96% |
| 6 tầng (=2 cảnh giới) | ×1.77 | ×3.14 | 32% | 2 | 2% | 70% |
| 9 tầng (=3 cảnh giới) | ×2.36 | ×5.56 | 18% | 3 | 0% | 27% |
| 12 tầng (=4 cảnh giới) | ×3.14 | ×9.85 | 10% | 4 | 0% | 4% |
| 18 tầng (=6 cảnh giới) | ×5.56 | ×30.91 | 3% | 6 | 0% | 0% |

Thiên Đạo Áp Chế: Rừng Non trần tầng 9 (C3 Hậu), Nguyên Sinh vùng ngoài trần tầng 15 (C5 Hậu).
Ví dụ: C6 Hậu (n=18) vào Rừng Non bị kéo về n=9; so với C2 Trung (n=5): chênh 4 tầng thay vì 13.
  n=18 vs n=5: tỉ lệ sức mạnh ×11.9, P(thấp thắng 1v1)=0.0%
  n=9 vs n=5: tỉ lệ sức mạnh ×2.1, P(thấp thắng 1v1)=9.1%
