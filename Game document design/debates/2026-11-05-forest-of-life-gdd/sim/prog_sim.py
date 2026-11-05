#!/usr/bin/env python3
"""PROG R1 simulation — The Forest of Life.
Đơn vị chuẩn: 1 CT (Chu Thiên) = lượng tu vi chuẩn của 1 phút chơi tích cực ở cảnh giới hiện tại.
Các phần:
  A. Bảng tầng (tier) x CT cần x TV hiển thị
  B. Lịch thời gian thực theo 3 hồ sơ người chơi (có Tĩnh Tu Tích Lũy = rested bonus)
  C. Chi phí luân hồi (chết ở cảnh giới R -> leo lại với Tiền Kiếp Hồi Ức)
  D. Monte Carlo tu vi/phút cho 5 loài (hiệu chỉnh hệ số k_s về 1.0 CT/phút)
  E. PvP: tỉ lệ sức mạnh theo chênh lệch cảnh giới, số người cần để hạ 1 người cao hơn, xác suất thắng 1v1
"""
import math, random, statistics as st

random.seed(42)
REALMS = ["Khai Linh", "Tụ Linh", "Trúc Cơ", "Kết Đan", "Hóa Hình", "Xuất Khiếu"]
TIERS = ["Sơ", "Trung", "Hậu"]
N = 18                      # 6 cảnh giới x 3 tầng; cảnh giới 7 (Thành Thần) không cày bằng TV
A, B, CAP = 4.0, 1.45, 180  # t(n) = min(CAP, A*n^B)  [CT]
R0, G = 10, 1.25            # TV hiển thị/phút = R0*G^(n-1)
KIEP_OVERHEAD = {1: 0, 2: 10, 3: 25, 4: 45, 5: 60, 6: 90}  # CT-tương-đương cho Cơ Duyên + Độ Kiếp khi rời cảnh giới R


def ct(n):
    return min(CAP, A * n ** B)


def realm_of(n):
    return (n - 1) // 3 + 1


def section_a():
    print("\n## A. Bảng tầng tu vi")
    print("| n | Cảnh giới | Tầng | CT cần | Lũy kế CT | TV/phút hiển thị | TV cần (hiển thị) |")
    print("|---|---|---|---|---|---|---|")
    cum = 0
    for n in range(1, N + 1):
        t = ct(n); cum += t
        rate = R0 * G ** (n - 1)
        print(f"| {n} | {realm_of(n)}·{REALMS[realm_of(n)-1]} | {TIERS[(n-1)%3]} | {t:.0f} | {cum:.0f} | {rate:.0f} | {t*rate:,.0f} |")
    tot = sum(ct(n) for n in range(1, N + 1)) + sum(KIEP_OVERHEAD.values())
    print(f"\nTổng CT tầng: {sum(ct(n) for n in range(1,N+1)):.0f}; + Cơ Duyên/Độ Kiếp: {sum(KIEP_OVERHEAD.values())}; = {tot:.0f} CT")
    for r in range(1, 7):
        s = sum(ct(n) for n in range(3*r-2, 3*r+1))
        print(f"  Cảnh giới {r} ({REALMS[r-1]}): {s:.0f} CT")
    return tot


PROFILES = {  # (phiên/tuần, phút/phiên)
    "Casual 3×25'": (3, 25),
    "Mid 5×40'": (5, 40),
    "Core 7×60'": (7, 60),
}
RESTED_CAP = 30  # phút được nhân đôi mỗi ngày (pool đầy sau 8h offline)


def weekly_ct(sessions, minutes, efficiency=0.85):
    # efficiency: tỉ lệ thời gian "tích cực" (di chuyển, UI, chết vặt...) ; rested nhân đôi tối đa 30 phút/phiên-ngày
    active = minutes * efficiency
    per = active + min(RESTED_CAP, active)
    return sessions * per


def milestones():
    # CT lũy kế khi chạm mỗi cảnh giới (bao gồm overhead kiếp của cảnh giới trước)
    out = {}
    cum = 0
    for r in range(1, 7):
        out[r] = cum
        cum += sum(ct(n) for n in range(3*r-2, 3*r+1)) + KIEP_OVERHEAD[r] if r < 6 else sum(ct(n) for n in range(16, 19))
    out[7] = cum + KIEP_OVERHEAD[6]
    return out


def section_b():
    print("\n## B. Lịch thời gian thực (tuần) để chạm mỗi cảnh giới — không tính chết")
    ms = milestones()
    hdr = "| Hồ sơ | CT/tuần | " + " | ".join(f"→C{r}" for r in range(2, 8)) + " |"
    print(hdr); print("|---" * 8 + "|")
    for name, (s, m) in PROFILES.items():
        w = weekly_ct(s, m)
        print(f"| {name} | {w:.0f} | " + " | ".join(f"{ms[r]/w:.1f}" for r in range(2, 8)) + " |")
    print("\nGiờ chơi thực (Mid) để chạm C7:", round(ms[7] / weekly_ct(5, 40) * 5 * 40 / 60, 1), "h")
    # phiên đầu: người mới có pool rested đầy
    first = 0; t = 0; n = 1; prog = 0
    while n <= 4:
        rate = 2 if t < RESTED_CAP else 1
        prog += rate * 0.85; t += 1
        if prog >= ct(n):
            print(f"  Phiên đầu: đạt hết tầng n={n} ở phút thực {t}")
            prog -= ct(n); n += 1
    return ms


CATCH_FAST, CATCH_SLOW = 3.0, 1.5


def section_c(ms):
    print("\n## C. Chi phí luân hồi — chết ở giữa cảnh giới R, leo lại đến đúng chỗ cũ")
    print("Quy tắc Tiền Kiếp Hồi Ức: ×3 đến hết cảnh giới (đỉnh-1), ×1.5 đến đỉnh cũ, sau đó ×1. Overhead kiếp đã vượt chỉ tính 50%.")
    print("| Chết tại | CT mất (không catch-up) | CT leo lại (có catch-up) | Tuần (Mid) | Phiên 40' (Mid) | Đạo Tâm nhận |")
    print("|---|---|---|---|---|---|")
    w = weekly_ct(5, 40)
    for R in range(2, 7):
        peak_n = 3*R - 1  # chết ở tầng Trung của cảnh giới R
        raw = sum(ct(n) for n in range(1, peak_n)) + sum(KIEP_OVERHEAD[r] for r in range(1, R))
        cost = 0
        for n in range(1, peak_n):
            mult = CATCH_FAST if realm_of(n) <= R - 1 else CATCH_SLOW
            cost += ct(n) / mult
        cost += 0.5 * sum(KIEP_OVERHEAD[r] for r in range(1, R))
        dao_tam = 10 * R * R
        print(f"| C{R} Trung ({REALMS[R-1]}) | {raw:.0f} | {cost:.0f} | {cost/w:.2f} | {cost/(w/5):.1f} | {dao_tam} |")


# ---------------- D. Monte Carlo nguồn tu vi theo loài ----------------
def poisson_events(rate_per_min, minutes):
    t, k = 0.0, 0
    while True:
        t += random.expovariate(rate_per_min)
        if t > minutes:
            return k
        k += 1


def sess_moc(m):   # Linh Mộc: quang hợp (thụ động khi online) + cắm rễ Linh Mạch + phản vệ + quả bị ăn
    light = random.uniform(0.6, 1.0)   # ngày/đêm, bị tán cây lớn che
    ct_ = 0.45 * light * m
    ct_ += sum(1.2 * random.uniform(0.7, 1.3) for _ in range(poisson_events(1/4, m)))
    ct_ += sum(2.0 for _ in range(poisson_events(1/8, m)) if random.random() < 0.7)
    ct_ += 0.08 * m
    return ct_


def sess_thao(m):  # Linh Thảo: lan hạt + quang hợp nhẹ + bị ăn-mà-không-chết (Phản Sinh) + thụ phấn
    ct_ = 0.35 * random.uniform(0.7, 1.0) * m
    ct_ += sum(0.9 * random.uniform(0.6, 1.4) for _ in range(poisson_events(1/3, m)))
    ct_ += sum(0.8 for _ in range(poisson_events(1/6, m)))
    return ct_


def sess_loc(m):   # Lộc: gặm Linh Thảo (chất lượng ô cỏ) + uống Linh Tuyền + thoát truy sát (Kinh Hồn Ngộ)
    ct_ = 0.55 * random.uniform(0.6, 1.4) * m
    ct_ += sum(2.0 for _ in range(poisson_events(1/12, m)))
    for _ in range(poisson_events(1/10, m)):
        ct_ += 2.5 if random.random() < 0.8 else 0.0
    return ct_


def sess_lang(m):  # Lang: săn — tìm + đuổi; thành công 55%; con mồi chất lượng biến thiên; hiếm khi săn người chơi
    t, ct_ = 0.0, 0.0
    while True:
        t += random.expovariate(1/2.2) + random.uniform(0.5, 1.5)  # tìm + đuổi
        if t > m:
            break
        if random.random() < 0.55:
            ct_ += random.gammavariate(4, 1.1)      # mean 4.4
            t += 0.5                                # ăn
        else:
            ct_ += 0.2
        if random.random() < 0.04:
            ct_ += 8.0                              # hạ người chơi cùng cảnh giới
    ct_ += 0.05 * m                                 # đánh dấu lãnh thổ
    return ct_


def sess_khuan(m): # Khuẩn: phân giải xác (phụ thuộc số chết trên server) + lan mạng tơ + khế ước cộng sinh
    corpse_rate = random.choice([1/8, 1/5, 1/3])     # server vắng / vừa / đông
    ct_ = sum(3.0 * random.uniform(0.5, 1.5) for _ in range(poisson_events(corpse_rate, m)))
    ct_ += 0.30 * m
    ct_ += 0.15 * m if random.random() < 0.6 else 0
    return ct_


SPECIES = {"Linh Mộc": sess_moc, "Linh Thảo": sess_thao, "Lộc": sess_loc, "Lang": sess_lang, "Khuẩn": sess_khuan}


def section_d():
    print("\n## D. Monte Carlo tu vi/phút theo loài (phiên 40', 4000 lần) — trước và sau hiệu chỉnh k_s")
    print("| Loài | CT/phút thô | k_s | CT/phút sau hiệu chỉnh | P10 | P90 | Hệ số biến thiên |")
    print("|---|---|---|---|---|---|---|")
    M, RUNS = 40, 4000
    for name, f in SPECIES.items():
        xs = [f(M) / M for _ in range(RUNS)]
        mu = st.mean(xs); k = 1.0 / mu
        ys = sorted(x * k for x in xs)
        p10, p90 = ys[int(0.1*RUNS)], ys[int(0.9*RUNS)]
        print(f"| {name} | {mu:.2f} | {k:.2f} | {st.mean(ys):.2f} | {p10:.2f} | {p90:.2f} | {st.pstdev(ys)/st.mean(ys):.0%} |")


# ---------------- E. PvP ----------------
S = 1.10   # hệ số HP và ATK mỗi tầng (≈1.33 mỗi cảnh giới)
SIGMA = 0.40  # độ lệch log-normal cho kỹ năng người chơi / build / địa hình / tình huống


def section_e():
    print("\n## E. PvP — chênh lệch cảnh giới")
    print("| Chênh (tầng) | Hệ số chỉ số | Tỉ lệ sức mạnh (HP×DPS) | TTK cao→thấp so với cùng cấp | Số người thấp cần (Lanchester) | P(thấp thắng 1v1) | P(2 thấp thắng 1 cao) |")
    print("|---|---|---|---|---|---|---|")
    for g in [0, 1, 2, 3, 6, 9, 12, 18]:
        mult = S ** g
        power = mult ** 2
        ttk = 1 / power
        need = math.ceil(mult - 1e-9) if g else 1
        wins1 = wins2 = 0
        T = 20000
        for _ in range(T):
            lo = random.lognormvariate(0, SIGMA)
            hi = power * random.lognormvariate(0, SIGMA)
            wins1 += lo > hi
            lo2 = random.lognormvariate(0, SIGMA) + random.lognormvariate(0, SIGMA)
            # 2 đánh 1: sức mạnh đội theo luật bình phương ~ (tổng căn)^2
            team = (math.sqrt(random.lognormvariate(0, SIGMA)) + math.sqrt(random.lognormvariate(0, SIGMA))) ** 2
            wins2 += team > hi
        lab = f"{g} tầng" + (f" (={g//3} cảnh giới)" if g and g % 3 == 0 else "")
        print(f"| {lab} | ×{mult:.2f} | ×{power:.2f} | {ttk:.0%} | {need} | {wins1/T:.0%} | {wins2/T:.0%} |")
    print("\nThiên Đạo Áp Chế: Rừng Non trần tầng 9 (C3 Hậu), Nguyên Sinh vùng ngoài trần tầng 15 (C5 Hậu).")
    print("Ví dụ: C6 Hậu (n=18) vào Rừng Non bị kéo về n=9; so với C2 Trung (n=5): chênh 4 tầng thay vì 13.")
    for hi_n, lo_n in [(18, 5), (9, 5)]:
        d = hi_n - lo_n
        p = (S ** d) ** 2
        w = sum(random.lognormvariate(0, SIGMA) > p * random.lognormvariate(0, SIGMA) for _ in range(20000)) / 20000
        print(f"  n={hi_n} vs n={lo_n}: tỉ lệ sức mạnh ×{p:.1f}, P(thấp thắng 1v1)={w:.1%}")


if __name__ == "__main__":
    section_a()
    ms = section_b()
    section_c(ms)
    section_d()
    section_e()
