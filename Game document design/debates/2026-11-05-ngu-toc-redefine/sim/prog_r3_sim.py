# PROG R3 sim
# (A) Duong cong nen + moc chon the (Mid)
# (B) Monte Carlo vong doi theo persona, co/khong lop bao ve, v1.0 vs nen
# (C) Liet ke build Lang (9 the + Thien Phu + 3 Hop Dao, 6 pick) -> ti le suc manh, the bat buoc?
# (D) Di san: so Dao Chung giu duoc sau N doi theo 3 luat mat
import random, itertools, math
from math import erf, sqrt, log
random.seed(7)

# ---------------- (A) ----------------
SPLIT = (0.30, 0.33, 0.37)
def curve(ct_canh, kiep):
    rows = []; cum = 0
    for c, (ctc, kp) in enumerate(zip(ct_canh, kiep), 1):
        t = [round(ctc * s) for s in SPLIT]
        cum += sum(t) + kp
        rows.append((c, t, sum(t), kp, cum))
    return rows
V10 = curve([36, 100, 180, 280], [5, 15, 30, 45])
NEN = curve([20, 50, 90, 140], [3, 8, 15, 23])
MID_CT_PER_MIN = 64 / 40  # FINAL: 64 CT / phien 40' (da gom Mong Tich)
print("## A. Duong cong (CT) — v1.0 vs nen")
print("C | v1.0 tang S/T/H | luy ke v1.0 | NEN tang S/T/H | kiep | luy ke NEN | phut Mid (NEN)")
for a, b in zip(V10, NEN):
    print(f"{a[0]} | {a[1]} | {a[4]} | {b[1]} | {b[3]} | {b[4]} | {b[4]/MID_CT_PER_MIN:.0f}'")

def ct_at(rows, c, tier):  # CT luy ke khi VAO tang tier (0=So,1=Trung,2=Hau) cua canh c; tier=3 -> sau kiep
    cum = 0
    for r in rows:
        if r[0] == c:
            if tier == 3: return cum + r[2] + r[3]
            return cum + sum(r[1][:tier])
        cum = r[4]
moc_full = [("M1 vao C1 Trung", 1, 1), ("M2 dot pha C1->2", 1, 3), ("M3 dot pha C2->3", 2, 3),
            ("M4 vao C3 Hau", 3, 2), ("M5 dot pha C3->4", 3, 3), ("M6 vao C4 Hau", 4, 2), ("VIEN MAN (C4)", 4, 3)]
moc_lite = [("M1 vao C1 Trung", 1, 1), ("M2 dot pha C1->2", 1, 3), ("M3 dot pha C2->3", 2, 3),
            ("M4 vao C3 Hau", 3, 2), ("VIEN MAN (C3)", 3, 3)]
print("\n## A2. Moc chon the (NEN, Mid 1,6 CT/phut)")
prev = 0
for lab, c, t in moc_full:
    x = ct_at(NEN, c, t); m = x / MID_CT_PER_MIN
    print(f"FULL {lab:22s} CT {x:4d}  phut {m:4.0f}  khoang cach {m-prev:3.0f}'"); prev = m
prev = 0
for lab, c, t in moc_lite:
    x = ct_at(NEN, c, t); m = x / MID_CT_PER_MIN
    print(f"LITE {lab:22s} CT {x:4d}  phut {m:4.0f}  khoang cach {m-prev:3.0f}'"); prev = m

# ---------------- (B) ----------------
# hazard chet / gio choi tich cuc, theo canh: he so f; PvP share s
F_CANH = {1: 0.6, 2: 0.8, 3: 1.0, 4: 1.3}
PERSONA = {  # h co so /gio, ti le PvP, CT/phut
    "P1 xe buyt": (0.06, 0.40, 1.6),
    "P3 lam vuon": (0.08, 0.50, 1.6),
    "Mid chung":  (0.10, 0.60, 1.6),
    "P2 ke san":  (0.18, 0.75, 1.6),
}
KIEP_P1 = 0.65  # qua lan dau; +15%/lan sau
def run_life(rows, last_c, h, s, rate, prot, N=20000):
    done = 0; hours_total = 0.0; lost_min = []; kiep_fail = 0
    for _ in range(N):
        t_all = 0.0
        while True:  # cac doi cho toi khi hoan thanh
            t = 0.0; dead = False
            for r in rows:
                c = r[0]
                if c > last_c: break
                hz = h * F_CANH[c]
                pvp = hz * s; env = hz * (1 - s)
                if prot == 2:
                    if c <= 2: pvp *= 0.4           # Au Linh toi het C2
                    else: pvp *= 0.6                # Trong Thuong C3+
                hz = pvp + env
                need = r[2]  # CT ca canh
                dur = need / rate / 60              # gio
                # chet trong canh?
                u = random.random()
                tdeath = -math.log(u) / hz if hz > 0 else 1e9
                if tdeath < dur:
                    t += tdeath; dead = True; break
                t += dur
                # kiep
                p = KIEP_P1; k = 0
                while True:
                    k += 1
                    if random.random() < p: break
                    kiep_fail += 1
                    if prot == 0:  # kiep that bai = chet (gia dinh WORLD)
                        dead = True; break
                    redo = r[1][2] / rate / 60      # lui ve dau tang Hau
                    if random.random() < 1 - math.exp(-hz * redo):
                        dead = True; t += redo / 2; break
                    t += redo; p = min(0.95, p + 0.15)
                if dead: break
                t += r[3] / rate / 60
            t_all += t
            if dead: lost_min.append(t * 60); continue
            done += 1; break
        hours_total += t_all
    lives_per_done = (len(lost_min) + N) / N
    p_first = None
    return hours_total / N, lives_per_done, (sum(lost_min) / len(lost_min) if lost_min else 0)

def p_first_life(rows, last_c, h, s, rate, prot, N=20000):
    ok = 0
    for _ in range(N):
        dead = False
        for r in rows:
            c = r[0]
            if c > last_c: break
            hz = h * F_CANH[c]; pvp = hz * s; env = hz * (1 - s)
            if prot == 2: pvp *= (0.4 if c <= 2 else 0.6)
            hz = pvp + env
            dur = r[2] / rate / 60
            if random.random() < 1 - math.exp(-hz * dur): dead = True; break
            p = KIEP_P1
            while True:
                if random.random() < p: break
                if prot == 0: dead = True; break
                redo = r[1][2] / rate / 60
                if random.random() < 1 - math.exp(-hz * redo): dead = True; break
                p = min(0.95, p + 0.15)
            if dead: break
        ok += (not dead)
    return ok / N

print("\n## B. Vong doi theo persona (gio choi tich cuc). P1 = P(hoan thanh doi dau); T = gio ky vong toi 1 lan Vien Man; doi = so doi ky vong; mat = phut TB mat moi lan chet")
for label, rows, lc in [("FULL v1.0 C4", V10, 4), ("FULL NEN C4", NEN, 4), ("LITE v1.0 C3", V10, 3), ("LITE NEN C3", NEN, 3)]:
    for prot in (0, 1, 2):
        print(f"-- {label}  che do={['0: kiep that bai = chet','1: kiep that bai != chet','2: (1) + Au Linh het C2 + Trong Thuong C3+'][prot]}")
        for pn, (h, s, rate) in PERSONA.items():
            T, lives, lost = run_life(rows, lc, h, s, rate, prot, N=8000)
            p1 = p_first_life(rows, lc, h, s, rate, prot, N=8000)
            print(f"   {pn:12s} P1={p1*100:3.0f}%  T={T:5.1f}h  doi={lives:4.2f}  mat/lan chet={lost:4.0f}'")

# ---------------- (C) ----------------
# The Lang: (dao, bac) -> (dps_solo, dps_party, ehp)  (he so cong them, nhan voi nhau)
CARDS = {
 ("TH",1): (0.04, 0.04, 0.00),  # Rang Cua: Lang Nha gay chay mau 45% Cong/3s
 ("TH",2): (0.05, 0.05, 0.01),  # Khuu Huyet: +10% st len muc tieu chay mau (uptime ~50%)
 ("TH",3): (0.04, 0.04, 0.03),  # Huyet Boc: Xe kich no chay mau x1,5, hoi 30%
 ("DD",1): (0.02, 0.03, 0.00),  # Hu Bay: dong minh +8% Toc; solo: moi AI cham 15%
 ("DD",2): (0.03, 0.08, 0.00),  # Vay San: +10% st khi co dong minh danh cung; solo: Lang Nha +1 o tam, CD -2s
 ("DD",3): (0.04, 0.06, 0.02),  # Lang Vuong: Dau San +8% st party, khoa Hang 5s; solo CD Lang Nha -30%
 ("DH",1): (0.02, 0.01, 0.05),  # An Phong: an khoi Than Thuc ngoai 6 o; don dau x1,3
 ("DH",2): (0.00, 0.00, 0.05),  # Nuot Voi: an x2 toc, hoi 2% HP/can
 ("DH",3): (0.01, 0.01, 0.07),  # Ke Don Doc: <35% HP: +15% Toc 4s, xoa danh dau, CD 60s
 ("TP",1): (0.01, 0.01, 0.03),  # Mui Soi (Thien Phu): Danh Hoi 12->18 o
}
HOP = {  # can Bac >=2 o ca hai dao
 ("TH","DD"): (0.03, 0.04, 0.00),
 ("TH","DH"): (0.06, 0.04, 0.00),
 ("DD","DH"): (0.01, 0.02, 0.05),
}
def options(state, pick_idx, full=True):
    b = state["b"]; opts = []
    for d in ("TH","DD","DH"):
        if b[d] < 3: opts.append(("C", d))
    if not state["tp"] and pick_idx >= 1: opts.append(("TP",))
    if full and pick_idx >= 5:
        for pair in HOP:
            if pair not in state["hop"] and b[pair[0]] >= 2 and b[pair[1]] >= 2: opts.append(("H", pair))
    if len(opts) < 3 and state["seq"]:
        opts.append(("TH+",))
    return opts
def apply(state, o):
    s = {"b": dict(state["b"]), "tp": state["tp"], "hop": set(state["hop"]), "seq": state["seq"] + [o]}
    if o[0] == "C": s["b"][o[1]] += 1
    elif o[0] == "TP": s["tp"] = True
    elif o[0] == "TH+": s["thamhoa"] = state.get("thamhoa", 0) + 1
    else: s["hop"].add(o[1])
    s.setdefault("thamhoa", state.get("thamhoa", 0))
    return s
def score(s, ctx):
    i = 0 if ctx == "solo" else 1
    dps = 1.0; ehp = 1.0
    for d, lv in s["b"].items():
        for k in range(1, lv + 1):
            dps *= 1 + CARDS[(d, k)][i]; ehp *= 1 + CARDS[(d, k)][2]
    if s["tp"]: dps *= 1 + CARDS[("TP",1)][i]; ehp *= 1 + CARDS[("TP",1)][2]
    for p in s["hop"]: dps *= 1 + HOP[p][i]; ehp *= 1 + HOP[p][2]
    th = s.get("thamhoa", 0); dps *= (1 + 0.015) ** th; ehp *= (1 + 0.015) ** th
    return dps, ehp
def enumerate_builds(picks, full):
    states = [{"b": {"TH":0,"DD":0,"DH":0}, "tp": False, "hop": set(), "seq": []}]
    min_opts = 9
    for k in range(picks):
        ns = []
        for st in states:
            op = options(st, k, full); min_opts = min(min_opts, len(op))
            for o in op: ns.append(apply(st, o))
        states = ns
    final = {}
    for st in states:
        key = (tuple(sorted(st["b"].items())), st["tp"], tuple(sorted(st["hop"])), st.get("thamhoa",0))
        final[key] = st
    return list(final.values()), min_opts
print("\n## C. Build Lang (dps x ehp), 3 Dao x 3 Bac + Thien Phu + Hop Dao")
for picks, full, lab in [(6, True, "FULL 6 pick"), (4, False, "LITE-hoa 4 pick (cung khung)")]:
    builds, mo = enumerate_builds(picks, full)
    for ctx in ("solo", "party"):
        sc = sorted([(score(b, ctx)[0] * score(b, ctx)[1], b) for b in builds], key=lambda x: -x[0])
        top = sc[0][0]; bot = sc[-1][0]
        # the bat buoc: xuat hien trong 100% top 20%
        n20 = max(1, len(sc) // 5); topset = [b for _, b in sc[:n20]]
        def has(b, card):
            if card[0] == "TP": return b["tp"]
            return b["b"][card[0]] >= card[1]
        mand = [c for c in CARDS if all(has(b, c) for b in topset)]
        print(f"{lab:30s} {ctx:5s}: so build={len(builds):3d}  min so the hien={mo}  power max/min={top/bot:.2f}  top={top:.2f} "
              f"the co mat o 100% top20%: {mand if mand else 'khong'}")
        # 3 archetype dai dien
    for name, seq in [("Truy Huyet thuan", [("C","TH")]*3+[("C","DH")]*2+[("TP",)]),
                      ("Doc Hanh thuan", [("C","DH")]*3+[("C","TH")]*2+[("TP",)]),
                      ("Dau Dan (party)", [("C","DD")]*3+[("C","TH")]*2+[("TP",)]),
                      ("Lai Huyet-Bong", [("C","TH"),("C","DH"),("C","TH"),("C","DH"),("C","TH"),("H",("TH","DH"))])]:
        if not full: break
        st = {"b": {"TH":0,"DD":0,"DH":0}, "tp": False, "hop": set(), "seq": []}
        for o in seq: st = apply(st, o)
        d1, e1 = score(st, "solo"); d2, e2 = score(st, "party")
        print(f"   {name:18s} solo dps x{d1:.2f} ehp x{e1:.2f} = {d1*e1:.2f} | party dps x{d2:.2f} = {d2*e2:.2f}")

# tran tan cong
print("\n## C2. Tran he so tan cong Omega (ngoai canh gioi)")
best_dps = max(score(b, "party")[0] for b in enumerate_builds(6, True)[0])
for lab, v in [("M_the max (Lang party)", best_dps), ("x Q toc khac 1,10", best_dps*1.10),
               ("x Di San Sat <=5%", best_dps*1.10*1.05), ("x Ban The U1 1,10", best_dps*1.10*1.05*1.10)]:
    print(f"{lab:28s} {v:.2f}  {'OK' if v < 1.77 else 'VUOT'} (1 canh = 1,77)")
sigma = log(1.77) / 1.036
Phi = lambda z: 0.5 * (1 + erf(z / sqrt(2)))
for lab, r in [("Q 1,10/0,91", 1.10/0.91), ("Q 1,15/0,87", 1.15/0.87), ("Q 1,10 + co che ~5%", 1.10*1.05/0.91)]:
    print(f"duel cung canh {lab:22s} ben khac thang {Phi(log(r)/sigma)*100:.0f}%")

# ---------------- (D) ----------------
print("\n## D. Di san: so Dao Chung trong So / dang trang bi sau 10 doi (P hoan thanh moi doi = p)")
def legacy(p, rule, lives=10, N=20000):
    owned = 0; eq_hist = 0
    for _ in range(N):
        book = 0; equipped_ok = 0
        for L in range(lives):
            if random.random() < p:
                book += 1
            else:
                if rule == "M2": book = 0           # mat het
        owned += book
    return owned / N
for p in (0.55, 0.70, 0.85):
    print(f"p={p:.2f}: M1 (khong mat) {legacy(p,'M1'):.1f} | M2 (mat het khi chet) {legacy(p,'M2'):.1f}  (Dao Chung sau 10 doi)")
