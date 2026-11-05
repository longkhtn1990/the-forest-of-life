#!/usr/bin/env python3
"""PROG R2 simulation — kiểm chứng số liệu chéo giữa 4 proposal.
Đơn vị: 1 CT (Chu Thiên) = tu vi chuẩn của 1 phút chơi tích cực (xem prog_sim.py).
  F. Cửu Cảnh (9 cảnh giới, 8 cày × 3 tầng) — đường cong mới để khớp WORLD (3/3/3) + PX (nhịp 2–4 phiên/cảnh)
  G. PvP: hệ số/tầng 1.08 (≈×1.26 chỉ số, ×1.59 combat power mỗi cảnh giới) so với R1 (×1.33 / ×1.77)
  H. Mô hình offline: PROG rested vs PX 60%×8h vs SURV 25%×8h vs ads +2h
  I. Monte Carlo mùa server (14/28/48/56 ngày) × đường cong (R1 7 cảnh / R2 Cửu Cảnh) có chết + người vào giữa mùa
  J. Chi phí chết: SURV Hậu Duệ (−1 tiểu cảnh) / SURV đổi loài (×2 tới 50%) / PROG R1 / đề xuất R2
  K. Cộng dồn bonus tốc độ (worst case)
  L. Xác suất người chơi "có mặt" trong world event theo độ dài/lịch sự kiện
  M. Sinh Năng 40/20/40 — giá trị 1 kill theo 3 định nghĩa, và lãi của kill-trading
"""
import math, random, statistics as st
random.seed(7)

# ---------------- hồ sơ người chơi (giống R1) ----------------
PROFILES = {"Casual 3×25'": (3, 25), "Mid 5×40'": (5, 40), "Core 7×60'": (7, 60)}
def weekly_ct(s, m, eff=0.85, rested=30):
    a = m * eff
    return s * (a + min(rested, a))

# ---------------- F. Cửu Cảnh ----------------
R2_NAMES = ["Khai Linh", "Luyện Khí", "Trúc Cơ", "Kết Đan", "Hóa Hình", "Nguyên Anh", "Phản Hư", "Hợp Đạo"]
R2_REALM_CT = [36, 90, 160, 190, 210, 230, 260, 280]   # CT tổng mỗi cảnh giới 1..8 (9 = Thành Thần, không cày)
R2_SPLIT = [0.30, 0.33, 0.37]
R2_OV = [5, 10, 20, 30, 40, 50, 60]                    # Cơ Duyên + kiếp khi rời cảnh giới 1..7
FOREST = {1: "Rừng Non", 2: "Rừng Non", 3: "Rừng Non", 4: "Nguyên Sinh", 5: "Nguyên Sinh", 6: "Nguyên Sinh", 7: "Cổ Đại", 8: "Cổ Đại"}

def r2_tiers():
    return [R2_REALM_CT[r] * s for r in range(8) for s in R2_SPLIT]

R1_A, R1_B, R1_CAP = 4.0, 1.45, 180
R1_OV = [0, 10, 25, 45, 60, 90]
def r1_tiers():
    return [min(R1_CAP, R1_A * n ** R1_B) for n in range(1, 19)]

def curve(tiers, ov, per_realm=3):
    """trả về list (vị trí CT lũy kế khi bắt đầu mỗi tầng), tổng tới Thiên Kiếp, ranh giới mỗi cảnh giới"""
    starts, c = [], 0.0
    realm_start = {}
    nrealm = len(tiers) // per_realm
    for i, t in enumerate(tiers):
        r = i // per_realm + 1
        if i % per_realm == 0:
            if r > 1:
                c += ov[r - 2] if r - 2 < len(ov) else 0
            realm_start[r] = c
        starts.append(c)
        c += t
    total = c + (ov[nrealm - 1] if nrealm - 1 < len(ov) else 0)
    realm_start[nrealm + 1] = total
    return starts, total, realm_start

def section_f():
    print("\n## F. Cửu Cảnh — 8 cảnh giới cày × 3 tầng + C9 Thành Thần (Thiên Kiếp ở cuối C8)")
    t = r2_tiers(); starts, total, rs = curve(t, R2_OV)
    print("| C | Khung chung (WORLD-12) | Cấp rừng | CT tầng Sơ/Trung/Hậu | CT cả cảnh | Lũy kế khi xong cảnh (gồm kiếp) | Phiên Mid (64 CT/phiên) | Tuần Casual | Tuần Mid | Tuần Core |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    W = {k: weekly_ct(*v) for k, v in PROFILES.items()}
    for r in range(1, 9):
        tri = t[3*r-3:3*r]
        endc = rs[r + 1]
        print(f"| {r} | {R2_NAMES[r-1]} | {FOREST[r]} | {'/'.join(f'{x:.0f}' for x in tri)} | {sum(tri):.0f} | {endc:.0f} | {sum(tri)/64:.1f} | " +
              " | ".join(f"{endc/W[k]:.1f}" for k in PROFILES) + " |")
    mid_h = total / weekly_ct(5, 40) * 200 / 60
    print(f"\nTổng tới Thiên Kiếp: {total:.0f} CT (R1: {curve(r1_tiers(), R1_OV)[1]:.0f} CT). Giờ chơi thực Mid: {mid_h:.1f} h (R1: 21.8 h)")
    # phiên đầu
    prog, n, tmin = 0.0, 0, 0
    while n < 4:
        tmin += 1; prog += (2 if tmin <= 30 else 1) * 0.85
        need = t[n] + (R2_OV[0] if n == 3 else 0)
        if prog >= need:
            print(f"  Phiên đầu (rested đầy): xong tầng {n+1} ở phút {tmin}" + (" (đã gồm Tiểu Kiếp lên C2)" if n == 3 else ""))
            prog -= need; n += 1
    return t

# ---------------- G. PvP ----------------
def pwin(power, sigma=0.40, T=40000):
    w1 = w2 = w3 = 0
    for _ in range(T):
        hi = power * random.lognormvariate(0, sigma)
        w1 += random.lognormvariate(0, sigma) > hi
        w2 += (sum(math.sqrt(random.lognormvariate(0, sigma)) for _ in range(2)) ** 2) > hi
        w3 += (sum(math.sqrt(random.lognormvariate(0, sigma)) for _ in range(3)) ** 2) > hi
    return w1 / T, w2 / T, w3 / T

def section_g():
    print("\n## G. PvP theo chênh lệch — R1 (×1.10/tầng) vs R2 (×1.08/tầng)")
    print("| Chênh | R1 combat power | R1 P(1v1) | R1 P(2v1) | R2 combat power | R2 P(1v1) | R2 P(2v1) | R2 P(3v1) |")
    print("|---|---|---|---|---|---|---|---|")
    for g, lab in [(1, "1 tầng"), (3, "1 cảnh"), (6, "2 cảnh"), (9, "3 cảnh"), (12, "4 cảnh"), (21, "7 cảnh")]:
        p1 = (1.10 ** g) ** 2; p2 = (1.08 ** g) ** 2
        a = pwin(p1); b = pwin(p2)
        print(f"| {lab} | ×{p1:.2f} | {a[0]:.0%} | {a[1]:.0%} | ×{p2:.2f} | {b[0]:.0%} | {b[1]:.0%} | {b[2]:.0%} |")
    print("\nPX-05 yêu cầu '3 người cảnh N hạ được 1 người N+1' và '1.6–1.8× combat power/cảnh': R1 = ×1.77 (cận trên), R2 = ×1.59 (cận dưới).")

# ---------------- H. Offline ----------------
def section_h():
    print("\n## H. Mô hình offline — CT/tuần (Mid 5×40', offline ≥8h/ngày) và tuần tới Thiên Kiếp (Cửu Cảnh, không chết)")
    _, total, _ = curve(r2_tiers(), R2_OV)
    active = 5 * 40 * 0.85
    rows = [
        ("PROG-04 Tĩnh Tu (×2 cho 30' đầu mỗi phiên, 0 thụ động)", weekly_ct(5, 40)),
        ("PX-10 'Linh khí dồi dào' ×1.5 cho 30' đầu/ngày (thay rested)", active + 5 * 30 * 0.5),
        ("PROG + PX cộng dồn (×2 và ×1.5 cùng lúc)", active + 5 * 30 * 2.0),
        ("PX-04 offline 60% × 8h/ngày × 7 ngày (+ rested PROG)", weekly_ct(5, 40) + 0.60 * 480 * 7),
        ("PX-04 + ad 'tăng tốc bế quan +2h' mỗi ngày", weekly_ct(5, 40) + 0.60 * 600 * 7),
        ("SURV-12 cây offline 25% × 8h (nếu tính vào CT)", weekly_ct(5, 40) + 0.25 * 480 * 7),
        ("Đề xuất R2 (=PROG-04): offline 0 CT; cây offline chỉ tích tài nguyên (Quang Tinh/lá), không tích CT", weekly_ct(5, 40)),
        ("Tham chiếu: nếu cho 10% thụ động × 4h/ngày (dù nhỏ)", weekly_ct(5, 40) + 0.10 * 240 * 7),
    ]
    print("| Mô hình | CT/tuần | × so với PROG-04 | Tuần tới Thiên Kiếp |")
    print("|---|---|---|---|")
    base = rows[0][1]
    for name, w in rows:
        print(f"| {name} | {w:.0f} | ×{w/base:.2f} | {total/w:.1f} |")

# ---------------- I. Mùa server ----------------
HAZ = {"R1": lambda r: 0.08 if r <= 3 else (0.06 if r <= 5 else 0.05),
       "R2": lambda r: 0.08 if r <= 3 else (0.06 if r <= 6 else 0.05)}  # số lần chết / giờ chơi
SOUL_REALM = {"R1": 6, "R2": 6}      # Nguyên Thần Bất Diệt từ cảnh này: 50% chỉ rơi 1 tầng
TK_SUCCESS = [0.5, 0.65, 0.8, 0.9]   # xác suất qua Thiên Kiếp lần 1,2,3,4+ (thất bại = chết)
MIX = [("Casual 3×25'", 0.45), ("Mid 5×40'", 0.40), ("Core 7×60'", 0.15)]

def season_mc(cv, L, runs=3000, late_frac=0.4, catchup=False):
    tiers = r1_tiers() if cv == "R1" else r2_tiers()
    ov = R1_OV if cv == "R1" else R2_OV
    starts, total, rs = curve(tiers, ov)
    nreal = len(tiers) // 3
    tier_end_rn = rs[4]  # xong cảnh giới 3 = xong Rừng Non
    ref_mid = weekly_ct(5, 40) / 7
    res = {p: {"rn": 0, "tk": 0, "god": 0, "n": 0, "deaths": [], "tkday": []} for p, _ in MIX}
    for _ in range(runs):
        u = random.random(); acc = 0
        for prof, w in MIX:
            acc += w
            if u <= acc: break
        s, m = PROFILES[prof]
        join = 0 if random.random() > late_frac else random.uniform(0, L * 0.8)
        p = peak = 0.0; deaths = 0; reached_rn = reached_tk = god = False; tk_tries = 0; tkday = None
        day = join
        while day < L and not god:
            noise = random.lognormvariate(0, 0.3)
            ct_day = weekly_ct(s, m) / 7 * noise
            hours = s * m / 7 / 60 * noise
            realm = next(r for r in range(1, nreal + 1) if rs[r + 1] > p) if p < total else nreal
            # catch-up Tiền Kiếp Hồi Ức
            peak_realm = next((r for r in range(1, nreal + 1) if rs[r + 1] > peak), nreal)
            if p < rs[peak_realm]: mult = 3.0
            elif p < peak: mult = 1.5
            else: mult = 1.0
            if catchup and p < 0.4 * ref_mid * day: mult *= 1.5
            p = min(total, p + ct_day * mult)
            if p >= tier_end_rn: reached_rn = True
            # chết
            k = sum(1 for _ in range(10) if random.random() < HAZ[cv](realm) * hours / 10)
            for _d in range(k):
                deaths += 1
                if realm >= SOUL_REALM[cv] and random.random() < 0.5:
                    p = max(0, p - tiers[min(len(tiers) - 1, int(realm * 3 - 2))])
                else:
                    peak = max(peak, p); p = 0.0
            if p >= total:
                reached_tk = True; tkday = tkday or day - join
                q = TK_SUCCESS[min(tk_tries, 3)]; tk_tries += 1
                if random.random() < q: god = True
                else:
                    deaths += 1; peak = max(peak, p); p = 0.0
            day += 1
        r = res[prof]; r["n"] += 1; r["rn"] += reached_rn; r["tk"] += reached_tk; r["god"] += god; r["deaths"].append(deaths)
        if tkday is not None: r["tkday"].append(tkday)
    return res

def section_i():
    print("\n## I. Monte Carlo mùa server — 3000 người/ô, 45% Casual / 40% Mid / 15% Core, 40% vào giữa mùa")
    print("Chết: 0.08/giờ chơi (cảnh 1–3), 0.06 (giữa), 0.05 (cuối); luân hồi đổi loài với Hồi Ức ×3/×1.5; Nguyên Thần Bất Diệt 50% từ cảnh 6; Thiên Kiếp thành công 50/65/80/90%.")
    print("| Đường cong | Mùa (ngày) | Bù Đắp | Hồ sơ | % xong Rừng Non | % chạm Thiên Kiếp | % thành Thần | Trung vị ngày tới Thiên Kiếp | Số lần chết TB |")
    print("|---|---|---|---|---|---|---|---|---|")
    for cv in ["R1", "R2"]:
        for L in [14, 28, 48, 56]:
            for cu in ([False, True] if L == 48 else [False]):
                res = season_mc(cv, L, catchup=cu)
                for prof, _ in MIX:
                    r = res[prof]; n = r["n"]
                    md = f"{st.median(r['tkday']):.0f}" if r["tkday"] else "—"
                    print(f"| {cv} | {L} | {'+50%' if cu else '—'} | {prof} | {r['rn']/n:.0%} | {r['tk']/n:.0%} | {r['god']/n:.0%} | {md} | {st.mean(r['deaths']):.1f} |")

# ---------------- J. Chi phí chết ----------------
def section_j():
    print("\n## J. Chi phí chết (Cửu Cảnh, chết ở tầng Trung) — CT phải cày lại, quy ra tuần Mid")
    t = r2_tiers(); starts, total, rs = curve(t, R2_OV)
    W = weekly_ct(5, 40)
    print("| Chết tại | Đã đầu tư (giờ Mid) | SURV Hậu Duệ (−1 tiểu cảnh) | SURV đổi loài (×2 tới 50% đỉnh) | PROG R1 đổi loài (×3/×1.5) | R2 Hậu Duệ (−1 cảnh, giữ build) | R2 đổi loài (×3/×1.5) |")
    print("|---|---|---|---|---|---|---|")
    for R in range(2, 9):
        pos = starts[3 * R - 2]  # đầu tầng Trung
        hours = pos / W * 200 / 60
        surv_hd = t[3 * R - 3]  # mất 1 tầng
        # SURV ×2 tới 50% đỉnh rồi ×1
        surv_x = 0.5 * pos / 2 + 0.5 * pos
        # PROG ×3 tới đầu cảnh R (hết R−1), ×1.5 tới đỉnh
        prog = rs[R] / 3 + (pos - rs[R]) / 1.5
        r2_hd = pos - starts[3 * (R - 1) - 2] if R > 1 else pos  # rơi về Trung của cảnh R−1, tốc độ ×1.5
        r2_hd /= 1.5
        print(f"| C{R} {R2_NAMES[R-1]} | {hours:.1f} h | {surv_hd/W:.2f} tuần | {surv_x/W:.2f} tuần | {prog/W:.2f} tuần | {r2_hd/W:.2f} tuần | {prog/W:.2f} tuần |")
    print("\nSURV-15 mục tiêu 'R7+ đầu tư 60h+, hồi phục ≤2 tuần' cần catch-up trung bình ≥ ×", end="")
    print(f"{60/(2*200/60):.1f} với Mid (2 tuần Mid = {2*200/60:.1f} giờ chơi).")

# ---------------- K. Cộng dồn bonus ----------------
def section_k():
    print("\n## K. Cộng dồn bonus tốc độ tu vi (đầu kiếp mới, trường hợp xấu nhất)")
    b = [("PROG-10 Tiền Kiếp Hồi Ức", 3.0), ("PROG-04 Tĩnh Tu (30' đầu)", 2.0), ("PX-10 Linh khí dồi dào (30' đầu/ngày)", 1.5),
         ("PX-12 ưu thế đầu kiếp (Đạo Tâm, C1–2)", 1.25), ("PX-16 Thiên Đạo ưu ái loài <15%", 1.25),
         ("PROG-04 Thiên Đạo Bù Đắp", 1.25), ("SURV-15 đầu thai tại Mộc Mộ (R1–R2)", 1.20), ("PX-06 đầu thai tại Linh Thổ", 1.30),
         ("SURV-06 Bế Quan ×1.5 (luyện linh khí)", 1.5), ("WORLD-10 E1 Linh Triều ×2", 2.0)]
    m = 1.0
    print("| Nguồn | × | Lũy kế nhân |"); print("|---|---|---|")
    for n, x in b:
        m *= x; print(f"| {n} | ×{x} | ×{m:.1f} |")
    add = 1 + sum(x - 1 for _, x in b)
    print(f"\nNếu cộng (additive) thay vì nhân: ×{add:.1f}. Đề xuất R2: mọi bonus cộng vào 1 'Thiên Đạo Gia Trì' additive, trần ×3.0 (×4.0 trong 30' đầu sau luân hồi).")

# ---------------- L. Có mặt trong sự kiện ----------------
def session_starts(days, s_per_week):
    out = []
    for d in range(days):
        if random.random() < s_per_week / 7:
            u = random.random()
            if u < 0.55: h = random.uniform(19, 23)
            elif u < 0.80: h = random.uniform(11.5, 13.5)
            else: h = random.uniform(7, 23)
            out.append(d * 24 + h)
    return out

def section_l():
    print("\n## L. Người chơi có mặt trong world event? (overlap ≥5 phút; giờ chơi: 55% 19–23h, 25% trưa, 20% rải rác)")
    DAYS, RUNS = 48, 2000
    events = {
        "PX-15 Linh Khí Triều 12h & 20h, 15'/lần": lambda: [(d*24+12, 0.25) for d in range(DAYS)] + [(d*24+20, 0.25) for d in range(DAYS)],
        "WORLD E2 Huyết Nguyệt 8', 21h ngày thứ 7": lambda: [(d*24+21, 8/60) for d in range(6, DAYS, 7)],
        "WORLD E1 Linh Triều 24', mỗi 4 ngày, giờ ngẫu nhiên": lambda: [(d*24+random.uniform(0, 24), 0.4) for d in range(0, DAYS, 4)],
        "SURV-17 Linh Triều 2h, 1/tuần, giờ ngẫu nhiên": lambda: [(d*24+random.uniform(0, 24), 2) for d in range(0, DAYS, 7)],
        "SURV-17 Đại Hạn 6h, 1/mùa Hạ (mỗi 8 ngày)": lambda: [(d*24+random.uniform(0, 24), 6) for d in range(2, DAYS, 8)],
        "Đề xuất: sự kiện tuần 36h (bắt đầu 19h thứ 6) + đỉnh 30' lúc 20h": lambda: [(d*24+19, 36) for d in range(4, DAYS, 7)],
    }
    print("| Sự kiện | Casual: % tuần gặp ≥1 lần | Mid: % tuần gặp ≥1 lần | Mid: số lần gặp / mùa 48 ngày |")
    print("|---|---|---|---|")
    for name, gen in events.items():
        out = []
        for prof, (s, m) in [("c", PROFILES["Casual 3×25'"]), ("m", PROFILES["Mid 5×40'"])]:
            wk_hit = 0; wk_n = 0; tot = 0
            for _ in range(RUNS // 4):
                ss = session_starts(DAYS, s); ev = gen()
                hits = [any(min(a + m/60, e + dur) - max(a, e) >= 5/60 for e, dur in ev) for a in ss]
                tot += sum(hits)
                for w in range(DAYS // 7):
                    wk_n += 1
                    wk_hit += any(h for a, h in zip(ss, hits) if w*168 <= a < (w+1)*168)
            out.append((wk_hit / wk_n, tot / (RUNS // 4)))
        print(f"| {name} | {out[0][0]:.0%} | {out[1][0]:.0%} | {out[1][1]:.1f} |")

# ---------------- M. Sinh Năng ----------------
def section_m():
    print("\n## M. Sinh Năng 40/20/40 — 1 kill PvP cùng cảnh đáng bao nhiêu CT cho kẻ ăn?")
    t = r2_tiers(); starts, total, rs = curve(t, R2_OV)
    print("| Nạn nhân | Định nghĩa A: Sinh Năng = tu vi lũy kế | B: = tu vi tầng hiện tại (TB 50%) | C (đề xuất): = 20 CT chuẩn hóa | Phút chơi tương đương của A / B / C |")
    print("|---|---|---|---|---|")
    for R in [2, 4, 6, 8]:
        pos = starts[3 * R - 2] + 0.5 * t[3 * R - 2]
        A = 0.4 * pos; B = 0.4 * 0.5 * t[3 * R - 2]; C = 0.4 * 20
        print(f"| C{R} Trung | {A:.0f} CT | {B:.0f} CT | {C:.0f} CT | {A:.0f}' / {B:.0f}' / {C:.0f}' |")
    print("\nKill-trading (2 tài khoản cùng cảnh luân phiên giết nhau, mỗi vòng ~3' gồm hồi sinh tại neo Hậu Duệ):")
    for lab, gain in [("A", 0.4 * (starts[3*4-2])), ("B", 0.4 * 0.5 * t[3*4-2]), ("C", 8.0)]:
        # người chết mất 1 tầng (Hậu Duệ) ~ t, người giết nhận gain; cặp lời ròng / vòng
        loss = t[3 * 4 - 3]
        print(f"  Định nghĩa {lab} @C4: kẻ giết +{gain:.0f} CT, người chết −{loss:.0f} CT (Hậu Duệ) → ròng cặp {gain - loss:+.0f} CT/vòng; với trần 1 kill đầy đủ/cặp/30' (PROG-12) → {max(0,gain-loss)*2:.0f} CT/giờ")

if __name__ == "__main__":
    section_f(); section_g(); section_h(); section_i(); section_j(); section_k(); section_l(); section_m()
