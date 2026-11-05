# R7 Patch: SURV (sau BỔ SUNG 4)

Nền: Thể Lực max 100, chạy −12/s, hồi +20/s khi đứng (v1.0). Mọi số dưới đây là đề xuất, chốt ở prototype.

## S1. Đặc tính tộc (áp mọi loài trong tộc)

**SURV-30 Mộc: Tự Dưỡng** (chuẩn hóa, 0 t-n). Không có No. Dinh dưỡng = Thủy + Quang Tinh + Dưỡng Chất (§5.3, giữ số). CT thụ động chỉ chạy khi online, Ánh Sáng ≥40% và Thủy ≥30. Loài ăn chủ động (nắp ấm) là **nội tại riêng**, không phải đặc tính tộc.

**SURV-31 Vũ: Bay + Nhanh** (luật top-down 2D)
| Luật | Số |
|---|---|
| Tầng | 2 tầng rời rạc: **Đất / Không**. Netcode dùng 1 bit, không có độ cao liên tục. Khi bay, sprite ×1,15 và **bóng dưới đất luôn hiện với mọi người** |
| Cất cánh | 0,5s, −20 Thể Lực, trúng đòn thì hủy |
| Hạ cánh | 0,4s, có vòng báo trước tại điểm đáp. **Cất/hạ cánh: nhận +30% sát thương** |
| Thể Lực khi bay | Tốn theo loài (S4), **không hồi**. Về 0 thì **Rơi**: choáng 1s, −5% HP max |
| Tốc | Bay theo loài (S4), bỏ qua địa hình, không qua Giới Bia |
| Khi bay | **Không ăn, không hồi HP, CT ×0, không vào Nơi Trú, không Bế Quan** |
| Đánh từ trên không | Chỉ có **Bổ Nhào** = hạ cánh lên mục tiêu (dùng lại Hạ Cánh Đạp: ×1,4, choáng 0,8s). Muốn gây sát thương phải xuống đất |
| Đậu | Ở node Cành (cây lớn, Tán người chơi Mộc). Hồi Thể Lực +15/s, ăn quả/sâu trên Tán được, CT ×0,5. Lính Nghĩ leo Cành được; Gai Bạo của cây đối địch trúng chim đang đậu |
| Ai đánh được kẻ đang bay | Diều hâu AI (ở tầng Không, ưu tiên mục tiêu bay ×2) · Vũ khác đang bay · đòn tầm xa: Quăng Lưỡi (trúng thì Ướt, §S2), Toan Dịch, Gai/Độc AoE khi bay qua Tán đối địch. Lang **không** cắn được |
| Lộ vị | Bay thì lộ trong tầm nhìn ×1,5, không ẩn được. Gáy khi đang bay ping cả 2 chiều (đồng minh thấy địch, địch thấy mình) |
| Giông | Bay trong giông: Thể Lực ×2, **sét ưu tiên mục tiêu bay** trong 8 ô (−15% HP max) |
| Chống bất tử | Director: Vũ ở trên không >50% thời gian trong 3' thì thêm 1 Diều hâu (trần 2 Diều hâu/người) |

Chi phí ước tính: layer + Diều hâu đuổi tầng ≈0,3 t-n (PX kiểm).

**SURV-32 Thủy: Sống dưới nước** (thay §5.8)
| Ô | Thủy | Loài cạn (Lang, Nghĩ) | Vũ | Mộc |
|---|---|---|---|---|
| Cạn | Ẩm giảm (hệ số theo loài) · cá **không lên** | ×1,0 | ×1,0 | — |
| Nông | ×1,2, hồi 1% HP/5s, Ẩm +10/s | ×0,8, có tiếng · Lính không vào | đi ×0,8, đáp xuống thì Ướt | W=3 |
| Sâu: **Mặt** | Thở, ăn (cá con +10, tảo +4, xác chìm), **CT ×0,8**, không tốn Thể Lực. Gợn nước làm lộ vị trí với kẻ trên bờ trong 6 ô | Chặn | Bay qua được, **Bổ Nhào được** | — |
| Sâu: **Đáy** (giữ nút Lặn) | Ẩn với mọi tộc khác, nhưng **không hồi HP, CT ×0,3, Thần Thức 4 ô** | Chặn | Không chạm được | — |

Luật chống vùng bất tử:
1. **Kẻ săn dưới nước (AI):** Cá Lóc Linh ở mọi khối sâu ≥16 ô (1 con/khối, tuần tra Đáy). **Cá Sấu AI** chỉ ở lõi Đầm Mục (2 con, cảnh C4, đánh cả Mặt lẫn nông). Director: ở nước sâu >4' liên tục thì Cá Lóc chuyển sang Stalking.
2. **Thủy đánh Thủy** dưới nước như bình thường (cùng tầng).
3. Nước có đáy: sâu ≈650 ô (1% map). Mỗi ao có ≥2 người chơi Thủy thì −1 bầy cá (tranh thức ăn).
4. Xác chết ở nước sâu **trôi vào ô nông gần nhất sau 5s**: Linh Hạch không bị giấu.
5. **Ẩm (đặc tính tộc):** cá 0 (chỉ quẫy tối đa 2s) · ếch/nhái 10' · cua/rùa/cá sấu 20'.
6. Độ kiếp dưới nước: sét kiếp ×1,25. Thủy phải lên bờ/nông để độ kiếp.

Bỏ luật "không combat dưới nước". Giữ "không oxy, không chết đuối" cho Thủy.

**SURV-33 Thú: Khứu & Bền.** Đánh Hơi thành đặc tính tộc, tầm theo loài (Lang 12 · Thử 8 · Lộc 6). Thể Lực hồi ×1,25 khi No ≥60. Chỉ Thú cắn kết liễu được kẻ đang Trọng Thương nhanh ×1,5. Đổi lại No decay cao nhất trong nhóm loài cùng cỡ.

**SURV-34 Trùng: Bầy & Lột Xác.** Bầy + Tha thành đặc tính tộc (số Lính theo loài). **Lột Xác**: mỗi lần đột phá cảnh thành công thì hồi 100% HP, xóa debuff, miễn sát thương 1,5s (0,05 t-n). Đông: ở Tổ thì No ×0,5.

## S2. Ma trận §4.6: chỉ các cặp bị ảnh hưởng
| Cặp | Cơ chế mới |
|---|---|
| **Thủy ⊣ Vũ** | Quăng Lưỡi/đòn tầm xa của Thủy trúng Vũ đang bay → **Ướt** (bay tốn Thể Lực ×2 trong 5s). Vũ rơi xuống nước sâu thì **Đắm**: Tốc ×0,4, −2% HP/s, không cất cánh được 3s. Bổ Nhào hụt mục tiêu ở Mặt → Ướt |
| **Vũ ⊣ Thú** | Tầng Không: Lang không chạm được. Gáy từ trên không làm lộ Thú đang ẩn. Bổ Nhào choáng 0,8s. Lang phản đòn bằng cách canh cửa sổ hạ cánh (+30%). Bỏ dòng "không cắn trúng khi Sải Cánh" |
| **Trùng ⊣ Thủy** | Bầy ≥2 Lính ở bờ: Thủy ở nông/Mặt trong 6 ô không hồi HP và hiện trên Thần Thức Hậu. Quăng Lưỡi trúng Lính trước Hậu (giữ) |
| **Mộc → Vũ** (sinh) | Thêm: Vũ đậu trên Tán đồng minh hồi Thể Lực ×1,5 |
| **Thú → Thủy** (sinh) | Thêm: xác chìm là thức ăn của Thủy ở Mặt (+8 No) |

Các cặp còn lại giữ nguyên.

## S3. Phân giải = môi trường thuần
Xác nhận §5.5: phân giải là **timer môi trường**, không tộc nào sở hữu. Nấm và vi khuẩn chỉ là prop và chỉ báo. Trùng (Mở Xác) và Thủy (xác chìm) chỉ **tăng tốc hoặc chuyển hướng** dòng Đất, không thay timer. Số: cạn 3' · ô ướt 90s · **Đầm Mục ×0,75** (2'15" / 68s) · Mở Xác 45s. Sửa §2.7: bỏ câu "vai phân giải chia cho Trùng và Thủy".

## S4. Đại diện Vũ và C4 phía sinh tồn

**Needs Vũ (No 100→59: tính warning đầu)**
| Trường hợp | HP | No decay | Warning đầu | Đất / Bay (ô/s) | Thể Lực khi bay | Bay tối đa | Ghi chú |
|---|---|---|---|---|---|---|---|
| A. **Gà rừng** (bay ngắn) | 260 | −4,5/phút | 9,1' | 5,5 / 7,0 | −12/s | ≈6,7s (~47 ô) | Đậu chỉ ở Cành thấp, ban đêm. Mạnh ở đất |
| B1. **Sẻ** (bay thật) | 220 | −5/phút | 8,2' | 4,5 / 7,5 | −4/s | ≈20s (~150 ô) | HP mỏng nhất, phải Bới hoặc Đậu để ăn |
| B2. **Cú** (bay thật, đêm) | 280 | −4/phút | 10,2' | 4,0 / 7,0 | −5/s | ≈16s | Bay đêm im lặng (bóng vẫn hiện). Đêm Thần Thức +30%, ngày −20% |

**SURV nghiêng về B1 (Sẻ).** Gà rừng chỉ bay được 7s nên mâu thuẫn với "tộc biết bay". Cú trùng vai rình đêm của Lang. Nếu WORLD giữ gà thì luật bay vẫn áp, chỉ đổi số.

**C4 phía sinh tồn (116–218')**
| Nhân vật | Vai ở Thâm Lâm / Đầm Mục | Áp lực chính | Công cụ chống | Độ kiếp Viên Mãn |
|---|---|---|---|---|
| Linh Nghĩ | **Giữ bến**: chiếm 1 trong 3 bến cạn. Xác ở Đầm tan nhanh nên Mở Xác + Tha cho CT cao nhất | Nước nông tách bầy. Lang C4 đói. Vũ đổ Bổ Nhào vào Lính | Tổ Phụ ở Thâm Lâm, Hầm Ngầm, Lột Xác | Ở Tổ. Lính đỡ 25% sát thương sét |
| Thủy (Oa) | **Chủ Đầm**: lõi sâu ~600 ô. Tu ở Mặt (×0,8), săn cá | Cá Sấu AI ở lõi. Thủy khác. Nghĩ giữ bến (Trùng ⊣ Thủy) | Đáy để cắt đuôi, Ngủ Bùn | Phải lên bến/nông (sét ×1,25 dưới nước), nên bị lộ |
| Vũ | **Mắt của Đầm**: trinh sát Linh Mạch/Linh Hạch, Bổ Nhào kết liễu | Diều hâu C4. Đầm trống tán nên bay bị lộ. Sét giông. Oa ở Đầm (Thủy ⊣ Vũ) | Đậu trên Liễu Chết/Tán đồng minh, Gáy, đường bay vòng qua Tán | Ở đất dưới Tán. Độ kiếp khi đang bay thì sét ×1,5 |

Pressure Map §5.11: đổi dòng C4 thành áp dụng cho **cả 5 tộc** với các vai trên.

## BLOCK mới
- **B-SURV-7:** BLOCK nếu bay có CT >0 hoặc gây sát thương được mà không phải hạ cánh.
- **B-SURV-8:** BLOCK nếu nước sâu không có kẻ săn AI dưới nước **và** không có cửa nào để tộc khác chạm được Thủy (Mặt/Bổ Nhào/xác trôi).
- **Gate (không phải block):** prototype tầng bay ở 20Hz với 40 CCU. Nếu fail thì fallback "bay = lướt dài 10 ô + Đậu".
- Yêu cầu PX: tính 2 archetype AI mới (Cá Lóc, Cá Sấu; reskin template Báo) ≈0,2 t-n.
