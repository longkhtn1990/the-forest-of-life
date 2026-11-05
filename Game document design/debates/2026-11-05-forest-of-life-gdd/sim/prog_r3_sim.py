#!/usr/bin/env python3
"""PROG R3 simulation — chốt số cho bản revision.
Đơn vị: 1 CT (Chu Thiên) = tu vi chuẩn của 1 phút chơi tích cực.
  N. Thất Cảnh v2 (7 cảnh giới: 6 cày × 3 tầng + C7 Thành Thần) — đường cong, nhịp phiên, so với Cửu Cảnh R2
  O. TTK: thú vs thú, thú vs cây HP 3 lớp (Tán/Thân/Tâm Rễ) — trả lời BLOCKER SURV về PROG-11
  P. Chi phí chết: Trùng Tu (neo) vs Luân Hồi (×4/×2) — trả lời BLOCKER PX về PROG-10
  Q. Monte Carlo Kiếp server: 28 (MVP) / 42 / 48 / 56 / 63 ngày, mô hình chết mới
  R. PvP theo chênh lệch với ×1.10/tầng (1v1 / 2v1 / 3v1)
  S. Chia CT trong nhóm (party) — trả lời PX Q3
  T. Cộng dồn bonus kiểu cộng, trần ×3 / ×4 — kiểm tra exploit "chết có chủ đích"
  U. Quỹ linh khí vùng (mô hình đồ chơi) — trả lời WORLD/SURV
Chạy: python3 prog_r3_sim.py > prog_r3_sim_output.md
"""
import math, random, statistics as st
random.seed(11)

PROFILES = {"Casual 3×25'": (3, 25), "Mid 5×40'": (5, 40), "Core 7×60'": (7, 60)}
EFF, RESTED = 0.85, 30

def weekly_ct(s, m):
    a = m * EFF
    return s * (a + min(RESTED, a))

# ---------------- N. Thất Cảnh v2 ----------------
NAMES = ["Khai Linh", "Tụ Linh", "Trúc Cơ", "Kết Đan", "Hóa Hình", "Xuất Khiếu"]
FOREST = {1: "Rừng Non (Bìa)", 2: "Rừng Non (Bìa→Trung)", 3: "Rừng Non (Trung Lâm)",
          4: "Nguyên Sinh / MVP: Linh Lâm", 5: "Nguyên Sinh / MVP: Linh Lâm", 6: "Cổ Đại"}
REALM_CT = [36, 100, 180, 280, 380, 520]
SPLIT = [0.30, 0.33, 0.37]
OV = [5, 15, 30, 45, 70]        # Cơ Duyên + kiếp khi rời C1..C5 (Tiểu, Tiểu, Trung, Trung, Đại)
KIEP = ["Tiểu Kiếp", "Tiểu Kiếp", "Trung Kiếp (Phi Thăng → Nguyên Sinh)", "Trung Kiếp", "Đại Kiếp (Phi Thăng → Cổ Đại)"]

def tiers():
    return [REALM_CT[r] * s for r in range(6) for s in SPLIT]

def curve(t=None, ov=OV):
    t = t or tiers()
    starts, c, rs = [], 0.0, {}
    for i, x in enumerate(t):
        r = i // 3 + 1
        if i % 3 == 0:
            if r > 1: c += ov[r - 2]
            rs[r] = c
        starts.append(c); c += x
    rs[7] = c
    return starts, c, rs

CUU_REALM = [36, 90, 160, 190, 210, 230, 260, 280]

def section_n():
    print("## N. Thất Cảnh v2 — 6 cảnh giới cày × 3 tầng + C7 Thành Thần (Thiên Kiếp ở cuối C6)")
    t = tiers(); starts, total, rs = curve(t)
    W = {k: weekly_ct(*v) for k, v in PROFILES.items()}
    print("| C | Khung | Vùng | CT tầng Sơ/Trung/Hậu | CT cả cảnh | Kiếp rời cảnh (CT) | Lũy kế khi xong cảnh (gồm kiếp) | Phiên Mid trong cảnh | Tuần Casual | Tuần Mid | Tuần Core |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for r in range(1, 7):
        tri = t[3*r-3:3*r]
        endc = rs[r] + sum(tri) + (OV[r-1] if r <= 5 else 0)
        kiep = f"{KIEP[r-1]} ({OV[r-1]})" if r <= 5 else "Thiên Kiếp (Thần Cách)"
        print(f"| {r} | {NAMES[r-1]} | {FOREST[r]} | {'/'.join(f'{x:.0f}' for x in tri)} | {sum(tri):.0f} | {kiep} | {endc:.0f} | {sum(tri)/64:.1f} | " +
              " | ".join(f"{endc/W[k]:.1f}" for k in PROFILES) + " |")
    mid_h = total / weekly_ct(5, 40) * 200 / 60
    print(f"\nTổng tới Thiên Kiếp: **{total:.0f} CT**. Giờ chơi thực Mid: **{mid_h:.1f} h** (Cửu Cảnh R2: 1671 CT/17.4 h; R1: 2089 CT/21.8 h).")
    print(f"Tầng dài nhất: {max(t):.0f} CT = {max(t)/64:.1f} phiên Mid. Cửu Cảnh R2: 104 CT = 1.6 phiên.")
    wm, wc, wca = weekly_ct(5, 40), weekly_ct(7, 60), weekly_ct(3, 25)
    print(f"MVP (hết C5 + Đại Kiếp Phi Thăng): {rs[6]:.0f} CT = {rs[6]/wm:.1f} tuần Mid / {rs[6]/wc:.1f} tuần Core / {rs[6]/wca:.1f} tuần Casual.")
    # So sánh nhịp mở khóa lớn
    print("\n### So sánh 7 vs 9 cảnh: số phiên Mid giữa hai lần đột phá đại cảnh giới")
    print("| | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | Trung bình | Max | Số bộ (tên × loài, kiếp, Thần Thông...) phải làm |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|")
    seven = [x/64 for x in REALM_CT]; nine = [x/64 for x in CUU_REALM]
    print("| Thất Cảnh v2 | " + " | ".join(f"{x:.1f}" for x in seven) + " | — | — | " + f"{st.mean(seven):.1f} | {max(seven):.1f} | 7 cảnh × loài |")
    print("| Cửu Cảnh R2 | " + " | ".join(f"{x:.1f}" for x in nine) + f" | {st.mean(nine):.1f} | {max(nine):.1f} | 9 cảnh × loài (+29%) |")
    print("\n### Phiên đầu tiên (người mới, thời gian thực)")
    print("FTUE Linh Thử dùng đường cong kịch bản riêng (PX-08): tầng 1/2/3 ở phút 2/4/6, Tiểu Kiếp → C2 ở phút 7, chết/Thọ Nguyên ở phút 14–16.")
    # kiếp 2 (cây) bắt đầu ở phút 16 của phiên đầu; đỉnh FTUE = vừa vào C2 → Hồi Ức ×4 cho toàn bộ C1 (+Tiểu Kiếp)
    p, tmin, marks = 0.0, 16, [(starts[1], "cây xong tầng 1"), (starts[2], "cây xong tầng 2"), (rs[2], "cây xong C1 + Tiểu Kiếp → C2"), (starts[4], "cây xong C2 Sơ")]
    mi = 0
    while mi < len(marks) and tmin < 120:
        tmin += 1
        mult = 4 if p < rs[2] else (2 if tmin <= 30 else 1)
        p += mult * EFF
        while mi < len(marks) and p >= marks[mi][0]:
            print(f"- phút {tmin}: {marks[mi][1]}"); mi += 1
    print("(Phiên 2+: Mộng Tích ×2 cho 30' đầu; C2 cần ~1.5 phiên, C3 Huyết Mạch ở phiên 3.)")
    return t

# ---------------- O. TTK ----------------
def k(n): return 1.10 ** (n - 1)

SPEC = {  # base tại n=1
    "Lang":     dict(hp=420, cong=50, d=0.40),
    "Linh Thử": dict(hp=300, cong=26, d=0.30),
    "Linh Mộc": dict(than=3 * 420, tan_ratio=0.5, root_ratio=0.5, cong=30, d=0.80),
}

def dr(d, n_def, n_att):
    a = d * k(n_def)
    return min(0.75, a / (a + k(n_att)))

def wolf_dps_coef():
    # đánh thường 1.0/s, Huyết Trảo 1.6 CD 6s + chảy máu 0.25×Công/s × 4s, Lang Nha 1.5 CD 12s (mở màn)
    return 1.0 + 1.6 / 6 + 1.0 / 6 + 1.5 / 12

def ttk_animal(att_n, def_name, def_n, khac=1.0):
    s = SPEC[def_name]
    hp = s["hp"] * k(def_n)
    dps = SPEC["Lang"]["cong"] * k(att_n) * wolf_dps_coef() * (1 - dr(s["d"], def_n, att_n)) * khac
    burst = SPEC["Lang"]["cong"] * k(att_n) * (1.5 + 1.0 + 0.5) * (1 - dr(s["d"], def_n, att_n)) * khac  # 2s mở màn: Lang Nha + 1 đòn thường + chảy máu
    return hp / dps, burst / hp

def tree_fight(n_tree=10, wolves=((10, 1.25),), thorns=0.10, lash=0.5, react=1.5, shell=True,
               lifesteal=0.10, retreat=0.35, digger=False, fire=False, dt=0.1, T=400, seed=None):
    """1..k sói đánh cây. Cây: Tán (đỡ trước) → Thân → Đổ. Tâm Rễ chỉ bị Căn Thương (đào/lửa).
    Trả về (t_do, t_root_dead, outcome)."""
    rnd = random.Random(seed)
    S = SPEC["Linh Mộc"]
    than = S["than"] * k(n_tree); tan = than * S["tan_ratio"]; root = than * S["root_ratio"]; root_max = root
    tcong = S["cong"] * k(n_tree)
    W = []
    for (wn, kh) in wolves:
        W.append(dict(n=wn, kh=kh, hp=SPEC["Lang"]["hp"] * k(wn), hpmax=SPEC["Lang"]["hp"] * k(wn), alive=True))
    t, shell_t, shell_cd = 0.0, 0.0, react + rnd.uniform(0, 1.0) if shell else 1e9
    t_do = None; mt = None
    while t < T:
        t += dt
        active = [w for w in W if w["alive"]]
        if t_do is None:
            if not active: return (None, None, "cây đẩy lui")
            # cây bật Vỏ Cứng
            if shell:
                if shell_cd <= 0: shell_t, shell_cd = 5.0, 15.0
                shell_t -= dt; shell_cd -= dt
            mit = 0.5 if (shell and shell_t > 0) else 1.0
            dmg_total = 0.0
            for w in active:
                dps = SPEC["Lang"]["cong"] * k(w["n"]) * wolf_dps_coef() * (1 - dr(S["d"], n_tree, w["n"])) * w["kh"] * mit
                dmg_total += dps * dt
                w["hp"] += lifesteal * dps * dt
                w["hp"] -= thorns * dps * dt * (1 - dr(SPEC["Lang"]["d"], w["n"], n_tree))
            # rễ quất đánh con sói đầu tiên
            tgt = active[0]
            tgt["hp"] -= lash * tcong * (1 - dr(SPEC["Lang"]["d"], tgt["n"], n_tree)) * dt
            for w in active:
                w["hp"] = min(w["hp"], w["hpmax"])
                if w["hp"] < retreat * w["hpmax"]: w["alive"] = False
            take = min(tan, dmg_total); tan -= take; than -= (dmg_total - take)
            if than <= 0:
                t_do = t; mt = 0.0
        else:
            mt += dt
            mul = 2.0 if mt <= 120 else 1.0
            rate = (0.01 if digger else 0) + (0.02 if fire else 0)
            root -= rate * mul * root_max * dt
            if root <= 0: return (t_do, t, "chết thật (luân hồi)")
            if mt > 120 and not (digger or fire): return (t_do, None, "Đổ → mọc lại")
            if mt > 180: return (t_do, None, "Đổ → mọc lại")
    return (t_do, None, "hết giờ")

def section_o():
    print("\n## O. TTK — thú vs thú và thú vs cây HP 3 lớp (n=10 = C4 Sơ, mọi chỉ số ×1.10/tầng)")
    print("Lang: HP 420, Công 50, d 0.40 · Linh Thử: HP 300, Công 26, d 0.30 · Linh Mộc: Thân = 3×420 (Tốc 0 → ×3), Tán = 0.5×Thân, Tâm Rễ = 0.5×Thân, Công 30, d 0.80.")
    print(f"Hệ số DPS chuỗi đòn Lang ≈ {wolf_dps_coef():.2f}×Công/s (đánh thường + Huyết Trảo + chảy máu + Lang Nha).")
    print("\n### O1. Thú vs thú (không né, không kỹ năng phòng thủ)")
    print("| Tình huống | TTK (s) | % HP mất trong 2s mở màn |")
    print("|---|---|---|")
    for lab, an, dn, dname, kh in [("Lang vs Lang cùng tầng (C4 Sơ)", 10, 10, "Lang", 1.0),
                                   ("Lang vs Lang, khắc hệ", 10, 10, "Lang", 1.25),
                                   ("Lang vs Lang thấp hơn 1 cảnh", 13, 10, "Lang", 1.0),
                                   ("Lang vs Linh Thử cùng tầng", 10, 10, "Linh Thử", 1.0),
                                   ("Lang vs Linh Thử thấp hơn 1 cảnh", 13, 10, "Linh Thử", 1.0)]:
        tt, b = ttk_animal(an, dname, dn, kh)
        print(f"| {lab} | {tt:.1f} | {b:.0%} |")
    print("\n### O2. Sói đánh cây (Monte Carlo 400 trận/ô; cây phản ứng: Vỏ Cứng −50% 5s/CD 15s, trễ phản ứng 1.5–2.5s; rễ quất 0.5×Công/s; gai 10%; sói hút máu 10%, rút lui khi HP <35%)")
    print("| Kịch bản | Cây | Thời gian tới Đổ — nếu sói không rút (s) | P(cây Đổ) có luật rút lui | Trung vị t Đổ khi Đổ (s) | Kết cục Tâm Rễ |")
    print("|---|---|---|---|---|---|")
    scen = [
        ("1 Lang cùng tầng, trung tính", dict(wolves=((10, 1.0),))),
        ("1 Lang cùng tầng, **khắc hệ ×1.25** (vd Huyết Lang Hỏa → cây hệ Kim)", dict(wolves=((10, 1.25),))),
        ("1 Lang khắc hệ, **cây AFK** (không Vỏ Cứng)", dict(wolves=((10, 1.25),), shell=False)),
        ("1 Huyết Lang (Hỏa) vs **Thiết Mộc** (Kim, gai 25%)", dict(wolves=((10, 1.25),), thorns=0.25)),
        ("1 Lang cao hơn 1 cảnh (C5 Sơ), trung tính", dict(wolves=((13, 1.0),))),
        ("2 Lang cùng tầng, trung tính", dict(wolves=((10, 1.0), (10, 1.0)))),
        ("3 Lang cùng tầng, trung tính", dict(wolves=((10, 1.0),) * 3)),
        ("3 Lang + 1 Độn Thử (Căn Thương 1%/s, ×2 khi Mộc Tàn)", dict(wolves=((10, 1.0),) * 3, digger=True)),
        ("2 Lang + Đại Hỏa (lửa 2%/s Tâm Rễ)", dict(wolves=((10, 1.0),) * 2, fire=True)),
    ]
    for lab, kw in scen:
        nr = dict(kw); nr["retreat"] = -1.0; nr["lifesteal"] = 0.0
        raw = [tree_fight(seed=i, **nr)[0] for i in range(60)]
        raw = [x for x in raw if x]
        res = [tree_fight(seed=1000 + i, **kw) for i in range(400)]
        dos = [r[0] for r in res if r[0]]
        roots = [r for r in res if r[2] == "chết thật (luân hồi)"]
        rt = f"chết thật {len(roots)/400:.0%} (trung vị {st.median([r[1]-r[0] for r in roots]):.0f}s sau Đổ)" if roots else "không chạm được → mọc lại sau Mộc Tàn 120s"
        thor = "Thiết Mộc" if kw.get("thorns", 0.1) > 0.1 else "Linh Mộc"
        print(f"| {lab} | {thor} | {st.median(raw):.0f} | {len(dos)/400:.0%} | {st.median(dos):.0f} | {rt} |" if dos else
              f"| {lab} | {thor} | {st.median(raw):.0f} | 0% | — | {rt} |")

# ---------------- P. Chi phí chết ----------------
def section_p():
    print("\n## P. Chi phí chết — chết ở giữa tầng Trung của mỗi cảnh (Mid 64 CT/phiên, 320 CT/tuần)")
    t = tiers(); starts, total, rs = curve(t)
    print("| Chết tại | Đã đầu tư (giờ Mid) | **Trùng Tu** tại neo: về đầu tầng, trần 130 CT (phiên) | R1 Luân Hồi ×3/×1.5 (phiên) | **Luân Hồi ×4/×2** (phiên) | ×4/×2 (tuần Mid) | Đạo Quả nhận khi Luân Hồi (25% CT lũy kế) |")
    print("|---|---|---|---|---|---|---|")
    for R in range(2, 7):
        i = 3 * R - 2
        pos = starts[i] + 0.5 * t[i]
        hours = pos / weekly_ct(5, 40) * 200 / 60
        tt = min(130, pos - starts[i]) / 64
        r1 = (rs[R] / 3 + (pos - rs[R]) / 1.5) / 64
        r3 = (rs[R] / 4 + (pos - rs[R]) / 2) / 64
        print(f"| C{R} {NAMES[R-1]} | {hours:.1f} h | {tt:.1f} | {r1:.1f} | {r3:.1f} | {r3*64/320:.2f} | {0.25*pos:.0f} |")
    # cuối C6 (Hậu viên mãn) — chết khi đang độ Thiên Kiếp
    pos = total
    r3 = (rs[6] / 4 + (pos - rs[6]) / 2) / 64
    print(f"| C6 Hậu viên mãn (bị giết trong Thiên Kiếp) | {pos/320*200/60:.1f} h | — | {(rs[6]/3+(pos-rs[6])/1.5)/64:.1f} | {r3:.1f} | {r3*64/320:.2f} | {0.25*pos*2:.0f} (×2) |")
    print("\nTrần PX: Trùng Tu ≤2 phiên ✔ ở mọi cảnh; Luân Hồi ≤1 tuần (5 phiên) — xem cột ×4/×2.")
    print("Thiên Kiếp thất bại do sét (không bị người giết): mất 50% CT tầng Hậu C6 = "
          f"{0.5*t[-1]:.0f} CT = {0.5*t[-1]/64:.1f} phiên, thử lại sau 1 phiên online (Kiếp Thương).")

# ---------------- Q. Monte Carlo Kiếp ----------------
MIX = [("Casual 3×25'", 0.45), ("Mid 5×40'", 0.40), ("Core 7×60'", 0.15)]
def haz(r): return 0.08 if r <= 3 else (0.06 if r <= 5 else 0.05)
TK_P = [0.60, 0.75, 0.90, 0.95]

def day_ct(s, m, noise, bonus, cap):
    a = m * EFF; rest = min(RESTED, a)
    per = rest * min(cap, 2 + bonus) + (a - rest) * min(cap, 1 + bonus)
    return s / 7 * per * noise

def kiep_mc(L, runs=3000, late=0.4, mvp=False, anchor_p=0.75, choose_td=0.65, budap=True, seed=3, bd_th=0.6, bd_b=0.5):
    rnd = random.Random(seed)
    t = tiers(); starts, total, rs = curve(t)
    goal = rs[6] if mvp else total
    ref = weekly_ct(5, 40) / 7
    out = {p: dict(n=0, rn=0, c5=0, phi=0, tk=0, god=0, d=[], lh=0, dd=0, tkday=[], early_tk=0, early_n=0) for p, _ in MIX}
    for _ in range(runs):
        u = rnd.random(); acc = 0
        for prof, w in MIX:
            acc += w
            if u <= acc: break
        s, m = PROFILES[prof]
        is_late = rnd.random() < late
        join = rnd.uniform(0, 0.8 * L) if is_late else 0
        p = peak = 0.0; deaths = lh = 0; last_td = -9; tries = 0; kt_until = -1
        flags = dict(rn=False, c5=False, phi=False, tk=False, god=False); tkday = None
        day = join
        while day < L and not flags["god"]:
            noise = rnd.lognormvariate(0, 0.3)
            realm = next((r for r in range(1, 7) if rs[r + 1] > p), 6)
            peak_realm = next((r for r in range(1, 7) if rs[r + 1] > peak), 6)
            bonus, cap = 0.0, 3.0
            if p < rs[peak_realm]: bonus, cap = 3.0, 4.0
            elif p < peak: bonus, cap = 1.0, 4.0
            if budap and p < bd_th * ref * day:  # Thiên Đạo Bù Đắp: dưới ngưỡng tiến độ Mid tham chiếu của server
                bonus += bd_b
            p = min(goal, p + day_ct(s, m, noise, bonus, cap))
            if p >= rs[4]: flags["rn"] = True
            if p >= rs[6]: flags["phi"] = True
            if p >= rs[5]: flags["c5"] = True
            hours = s * m / 7 / 60 * noise
            nd = sum(1 for _ in range(10) if rnd.random() < haz(realm) * hours / 10)
            for _d in range(nd):
                deaths += 1
                anchor = rnd.random() < anchor_p and day - last_td >= 1
                soul = realm >= 6 and rnd.random() < 0.5
                if (anchor and rnd.random() < choose_td) or (not anchor and soul):
                    idx = max(i for i in range(len(starts)) if starts[i] <= p)
                    p = max(starts[idx], p - 130); last_td = day
                else:
                    lh += 1; peak = max(peak, p); p = 0.0
            if not mvp and p >= total and day >= kt_until:
                flags["tk"] = True; tkday = tkday if tkday is not None else day - join
                if rnd.random() < 0.10:  # bị đánh úp chết trong Thiên Kiếp
                    deaths += 1; lh += 1; peak = max(peak, p); p = 0.0
                elif rnd.random() < TK_P[min(tries, 3)]:
                    flags["god"] = True
                else:
                    p -= 0.5 * t[-1]; kt_until = day + 7 / s
                tries += 1
            day += 1
        r = out[prof]; r["n"] += 1
        for kf in ["rn", "c5", "phi", "tk", "god"]: r[kf] += flags[kf]
        r["d"].append(deaths); r["lh"] += lh; r["dd"] += deaths
        if tkday is not None: r["tkday"].append(tkday)
        if not is_late:
            r["early_n"] += 1; r["early_tk"] += (flags["phi"] if mvp else flags["tk"])
    return out

def section_q():
    print("\n## Q. Monte Carlo Kiếp server — 3000 người/ô; 45% Casual / 40% Mid / 15% Core; 40% vào muộn (đều trong 80% đầu Kiếp)")
    print("Chết/giờ chơi: 0.08 (C1–3), 0.06 (C4–5), 0.05 (C6). Khi chết: neo còn (75%, không dùng trong 24h) → 65% chọn Trùng Tu (về đầu tầng, trần 130 CT), còn lại Luân Hồi (×4 tới hết cảnh đỉnh−1, ×2 tới đỉnh). C6 không neo: Nguyên Thần Bất Diệt 50%.")
    print("Thiên Kiếp: 10% bị đánh úp chết thật; còn lại thành công 60/75/90/95%; thất bại do sét = −50% tầng Hậu, chờ 1 phiên. Bonus cộng dồn trần ×3 (×4 khi Hồi Ức). Thiên Đạo Bù Đắp +0.5 khi dưới 60% tiến độ Mid tham chiếu (chốt R3).")
    print("| Chế độ | Kiếp (ngày) | Hồ sơ | % xong Rừng Non (C3) | % vào C5 Hóa Hình | % Phi Thăng Cổ Đại (xong C5 + Đại Kiếp) | % chạm Thiên Kiếp | % Thành Thần | Trung vị ngày tới Thiên Kiếp | % người vào đầu Kiếp đạt mục tiêu cuối | Chết TB | % lần chết là Luân Hồi |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for mode, L in [("MVP (trần C5)", 28), ("MVP (trần C5)", 42), ("Đầy đủ", 42), ("Đầy đủ", 48), ("Đầy đủ", 56), ("Đầy đủ", 63)]:
        mvp = mode.startswith("MVP")
        res = kiep_mc(L, mvp=mvp)
        for prof, _ in MIX:
            r = res[prof]; n = r["n"]
            md = f"{st.median(r['tkday']):.0f}" if r["tkday"] else "—"
            tk = "—" if mvp else f"{r['tk']/n:.0%}"; gd = "—" if mvp else f"{r['god']/n:.0%}"
            lhp = f"{r['lh']/max(1,r['dd']):.0%}"
            print(f"| {mode} | {L} | {prof} | {r['rn']/n:.0%} | {r['c5']/n:.0%} | {r['phi']/n:.0%} | {tk} | {gd} | {md} | {r['early_tk']/max(1,r['early_n']):.0%} | {st.mean(r['d']):.1f} | {lhp} |")
    print("\n### Q2. Độ nhạy: Kiếp 56 ngày, Mid — thay đổi hành vi chọn Trùng Tu / tỉ lệ neo còn")
    print("| Neo còn | Chọn Trùng Tu khi có neo | % Mid chạm Thiên Kiếp | % Mid Thành Thần | % lần chết là Luân Hồi |")
    print("|---|---|---|---|---|")
    for ap, ct in [(0.75, 0.65), (0.75, 0.95), (0.5, 0.65), (0.0, 0.0)]:
        r = kiep_mc(56, runs=2500, anchor_p=ap, choose_td=ct)["Mid 5×40'"]
        print(f"| {ap:.0%} | {ct:.0%} | {r['tk']/r['n']:.0%} | {r['god']/r['n']:.0%} | {r['lh']/max(1,r['dd']):.0%} |")

    print("\n### Q3. Độ nhạy Thiên Đạo Bù Đắp — Kiếp 56 ngày, Casual")
    print("| Ngưỡng (so với tiến độ Mid tham chiếu) | Bonus | % Casual vào C5 | % Casual Phi Thăng Cổ Đại | % Mid chạm Thiên Kiếp |")
    print("|---|---|---|---|---|")
    for th, b in [(0.4, 0.5), (0.6, 0.5), (0.6, 1.0), (0.0, 0.0)]:
        res = kiep_mc(56, runs=2500, bd_th=th, bd_b=b, budap=th > 0)
        c = res["Casual 3×25'"]; mm = res["Mid 5×40'"]
        print(f"| {th:.0%} | +{b} | {c['c5']/c['n']:.0%} | {c['phi']/c['n']:.0%} | {mm['tk']/mm['n']:.0%} |")

# ---------------- R. PvP ----------------
def pwin(power, sigma=0.40, T=30000, rnd=random.Random(5)):
    w = [0, 0, 0]
    for _ in range(T):
        hi = power * rnd.lognormvariate(0, sigma)
        for j, kk in enumerate([1, 2, 3]):
            team = (sum(math.sqrt(rnd.lognormvariate(0, sigma)) for _ in range(kk)) ** 2) if kk > 1 else rnd.lognormvariate(0, sigma)
            w[j] += team > hi
    return [x / T for x in w]

def section_r():
    print("\n## R. PvP theo chênh lệch (×1.10/tầng → ×1.33 chỉ số, ×1.77 combat power mỗi cảnh; nhiễu kỹ năng σ=0.40)")
    print("| Chênh | Combat power | P(1 thấp thắng) | P(2 thấp thắng) | P(3 thấp thắng) |")
    print("|---|---|---|---|---|")
    for g, lab in [(1, "1 tầng"), (3, "1 cảnh"), (6, "2 cảnh"), (9, "3 cảnh"), (12, "4 cảnh")]:
        pw = (1.10 ** g) ** 2
        a = pwin(pw)
        print(f"| {lab} | ×{pw:.2f} | {a[0]:.0%} | {a[1]:.0%} | {a[2]:.0%} |")
    # Áp Chế Rừng Non: C6 Hậu (n=18) bị nén về n=9 vs C2 Trung (n=5)
    pw = (1.10 ** (9 - 5)) ** 2
    print(f"\nÁp Chế Rừng Non: C6 Hậu (n=18→9) vs C2 Trung (n=5): combat ×{pw:.2f} (không Áp Chế: ×{(1.1**13)**2:.1f}); P(C2 thắng 1v1) = {pwin(pw)[0]:.0%}.")

# ---------------- S. Party ----------------
def section_s():
    print("\n## S. Chia CT trong nhóm — tổng CT nhóm = 1 + 0.6·min(k−1, 2), chia đều")
    print("Giả định săn: tốc độ hạ mồi của bầy k con so với 1 con = 1, 1.35, 1.6, 1.75, 1.85 (thời gian tìm mồi dùng chung).")
    print("| k | R1 (85% + 10%/người) mỗi người | R3 mỗi người nhận / hành động | Tốc độ hạ mồi | CT/phút mỗi người (R1) | CT/phút mỗi người (R3) |")
    print("|---|---|---|---|---|---|")
    kr = [1, 1.35, 1.6, 1.75, 1.85]
    for kk in range(1, 6):
        r1 = 1.0 if kk == 1 else 0.85 + 0.10 * min(kk - 1, 3)
        r3 = (1 + 0.6 * min(kk - 1, 2)) / kk
        print(f"| {kk} | {r1:.0%} | {r3:.0%} | ×{kr[kk-1]} | {r1*kr[kk-1]:.2f} | {r3*kr[kk-1]:.2f} |")

# ---------------- T. Bonus ----------------
def section_t():
    print("\n## T. Thiên Đạo Gia Trì — cộng dồn kiểu cộng, trần ×3 (×4 khi đang Hồi Ức)")
    src = [("Mộng Tích/Tĩnh Tu (30' đầu phiên)", 1.0), ("Thiên Đạo Bù Đắp", 0.5), ("Loài thiếu <15% (PX-16)", 0.25),
           ("Đầu thai tại Mộ Linh/Mộc Mộ", 0.2), ("Linh Triều (sự kiện)", 1.0), ("Đạo Quả Bàn 'Linh Căn' (trần)", 0.10)]
    tot = 1 + sum(x for _, x in src)
    print("| Nguồn | + | ")
    print("|---|---|")
    for n_, x in src: print(f"| {n_} | +{x} |")
    print(f"\nTổng cộng thô: ×{tot:.2f} → áp trần ×3.0. Với Hồi Ức ×4 (= +3): ×{tot+3:.2f} → trần ×4.0. (R2 kiểu nhân: ×82.)")
    # exploit: chết có chủ đích ở C2 Trung để đầu thai loài thiếu
    t = tiers(); starts, total, rs = curve(t)
    pos = starts[4] + 0.5 * t[4]
    lost = pos
    regain = rs[2] / 4 + (pos - rs[2]) / 2
    print(f"Exploit 'tự sát ở C2 Trung để lấy bonus': mất {lost:.0f} CT tiến độ, cày lại tốn {regain:.0f} phút ở ×4/×2; được thêm tối đa +25% (loài thiếu) trên một khoảng ≈ 30 phút → lãi ≤ {0.25*30:.0f} CT < chi phí {regain:.0f} CT. **Không lãi.**")

# ---------------- U. Quỹ vùng ----------------
def zone(pop, minutes=240, Q=200, inflow=1.2, dt=1.0):
    """pop: list loại ('thu','cay','nam'), mỗi người 1 CT/phút khi online. Rút: thú 1.0 LK/CT, cây 0.4, nấm 0.2.
    Cây Linh Hóa Địa +0.6 LK/CT cây kiếm. Trả về: 40% phần thú rút quay lại chậm (bán rã 48'; có nấm: 16')."""
    q = Q; pend = 0.0; hl = 16 if "nam" in pop else 48; t_kho = None; low = q
    lam = math.log(2) / hl
    for t in range(int(minutes / dt)):
        f = q / Q
        mul_c = 0.5 if f < 0.3 else (1.0 if f >= 0.6 else 0.85 + 0.15 * (f - 0.3) / 0.3)
        mul_p = 0.8 if f < 0.3 else (1.0 if f >= 0.6 else 0.85 + 0.15 * (f - 0.3) / 0.3)
        draw = add = 0.0
        for p in pop:
            if p == "thu":
                ct = mul_c; draw += 1.0 * ct; pend += 0.4 * ct
            elif p == "cay":
                ct = mul_p; draw += 0.4 * ct; add += 0.6 * ct
            else:
                ct = mul_p; draw += 0.2 * ct
        ret = pend * lam * dt; pend -= ret
        q = max(0, min(Q, q + (inflow + add + ret - draw) * dt))
        low = min(low, q)
        if t_kho is None and q < 0.3 * Q: t_kho = t
    return t_kho, low / Q, q / Q

def section_u():
    print("\n## U. Quỹ linh khí vùng (mô hình đồ chơi; 1 vùng Trung Lâm; Q=200 LK, dòng vào 1.2 LK/phút; ngày-rừng 24')")
    print("Rút: thú 1.0 LK/CT · cây 0.4 · nấm 0.2. Cây Linh Hóa Địa trả +0.6 LK/CT. 40% phần thú rút quay về đất (bán rã 48', có nấm 16'). Khô Linh <30%: thú CT ×0.5, cây/nấm ×0.8; 30–60%: ×0.85–1.0.")
    print("| Dân trong vùng (online liên tục 4h) | Khô Linh sau (phút / ngày-rừng) | Quỹ thấp nhất | Quỹ sau 4h |")
    print("|---|---|---|---|")
    for lab, pop in [("4 thú săn", ["thu"] * 4), ("3 thú săn", ["thu"] * 3), ("2 thú + 1 cây + 1 nấm", ["thu", "thu", "cay", "nam"]),
                     ("3 thú + 1 cây", ["thu"] * 3 + ["cay"]), ("2 cây + 2 nấm", ["cay", "cay", "nam", "nam"])]:
        tk, lo, end = zone(pop)
        tks = f"{tk} / {tk/24:.1f}" if tk is not None else "không"
        print(f"| {lab} | {tks} | {lo:.0%} | {end:.0%} |")
    print("Bìa Rừng: sàn quỹ 50% (SURV) → không bao giờ Khô Linh; hệ số CT tối thiểu ở Bìa = ×0.925.")

if __name__ == "__main__":
    print("# PROG R3 — kết quả mô phỏng (`python3 sim/prog_r3_sim.py`)\n")
    section_n(); section_o(); section_p(); section_q(); section_r(); section_s(); section_t(); section_u()
