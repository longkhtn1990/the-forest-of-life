# PROG R7 sim — patch H1–H3
# (A) Build Nghi/Oa/Ke full (9 the + Thien Phu + 3 Hop Dao, 6 pick): so build, min the/moc, max/min, M_the max
# (B) Tran Omega co noi tai
# (C) Oa: CT/gio theo ti le thoi gian o nuoc sau
# (D) Vu bay: thoi gian/quang duong bay toi da theo canh; cua so cat canh vs Lang Nha
# (E) Vong doi 5 nhan vat full (Mid) + tong gio lan dau Vien Man ca 5
import random, math, itertools
random.seed(11)

# ---------- (A) ----------
# (dao, bac) -> (dps_solo, dps_party, ehp)
CH = {
 "Nghi": {
  ("T",1):(0.00,0.00,0.05), ("T",2):(0.01,0.01,0.04), ("T",3):(0.00,0.00,0.13),  # Lính Đỡ 25%->12%
  ("S",1):(0.04,0.04,0.00), ("S",2):(0.06,0.06,-0.02), ("S",3):(0.05,0.06,0.02),
  ("V",1):(0.01,0.02,0.00), ("V",2):(0.02,0.05,0.00), ("V",3):(0.01,0.03,0.04),
  ("TP",1):(0.01,0.01,0.03),
  "H":{("T","S"):(0.04,0.04,0.01), ("T","V"):(0.00,0.02,0.04), ("S","V"):(0.03,0.05,0.00)}},
 "Oa": {
  ("T",1):(0.00,0.00,0.04), ("T",2):(0.01,0.01,0.05), ("T",3):(0.00,0.00,0.07),
  ("S",1):(0.03,0.03,0.00), ("S",2):(0.05,0.05,0.01), ("S",3):(0.06,0.06,0.00),
  ("V",1):(0.01,0.02,0.00), ("V",2):(0.00,0.03,0.03), ("V",3):(0.02,0.04,0.02),
  ("TP",1):(0.01,0.01,0.03),
  "H":{("T","S"):(0.05,0.04,0.00), ("T","V"):(0.00,0.01,0.05), ("S","V"):(0.03,0.05,0.00)}},
 "Ke": {
  ("T",1):(0.00,0.00,0.04), ("T",2):(0.01,0.01,0.05), ("T",3):(0.00,0.00,0.06),
  ("S",1):(0.04,0.04,0.00), ("S",2):(0.03,0.03,0.02), ("S",3):(0.06,0.06,0.00),
  ("V",1):(0.01,0.02,0.01), ("V",2):(0.01,0.04,0.00), ("V",3):(0.01,0.04,0.02),
  ("TP",1):(0.01,0.01,0.03),
  "H":{("T","S"):(0.03,0.03,0.03), ("T","V"):(0.00,0.02,0.04), ("S","V"):(0.04,0.05,0.00)}},
}
D3 = ("T","S","V")
def opts(st, k):
    o = [("C",d) for d in D3 if st["b"][d] < 3]
    if not st["tp"] and k >= 1: o.append(("TP",))
    if k >= 5:
        for p in itertools.combinations(D3, 2):
            if p not in st["hop"] and st["b"][p[0]] >= 2 and st["b"][p[1]] >= 2: o.append(("H",p))
    if len(o) < 3: o.append(("TH",))
    return o
def app(st, o):
    s = {"b":dict(st["b"]), "tp":st["tp"], "hop":set(st["hop"]), "th":st["th"]}
    if o[0]=="C": s["b"][o[1]] += 1
    elif o[0]=="TP": s["tp"] = True
    elif o[0]=="H": s["hop"].add(o[1])
    else: s["th"] += 1
    return s
def score(cd, s, i):
    dps = ehp = 1.0
    for d, lv in s["b"].items():
        for k in range(1, lv+1): dps *= 1+cd[(d,k)][i]; ehp *= 1+cd[(d,k)][2]
    if s["tp"]: dps *= 1+cd[("TP",1)][i]; ehp *= 1+cd[("TP",1)][2]
    for p in s["hop"]: dps *= 1+cd["H"][p][i]; ehp *= 1+cd["H"][p][2]
    dps *= 1.015**s["th"]; ehp *= 1.015**s["th"]
    return dps, ehp
print("## A. Build full 6 pick")
MT = {}
for name, cd in CH.items():
    sts = [{"b":{d:0 for d in D3}, "tp":False, "hop":set(), "th":0}]; mo = 9
    for k in range(6):
        ns = []
        for st in sts:
            o = opts(st, k); mo = min(mo, len(o)); ns += [app(st, x) for x in o]
        sts = ns
    uniq = {(tuple(sorted(s["b"].items())), s["tp"], tuple(sorted(s["hop"])), s["th"]): s for s in sts}.values()
    for i, ctx in ((0,"solo"),(1,"party")):
        sc = sorted(score(cd, s, i)[0]*score(cd, s, i)[1] for s in uniq)
        mdps = max(score(cd, s, i)[0] for s in uniq)
        MT[(name,ctx)] = mdps
        print(f"{name:5s} {ctx:5s} build={len(uniq):3d} min the/moc={mo} max/min={sc[-1]/sc[0]:.2f} M_the(dps) max={mdps:.2f}")

# ---------- (B) ----------
print("\n## B. Tran Omega (PvE, Q 1,10; Dao Chung Sat 3,5%; noi tai tan cong <=2%)")
mt = max(max(MT.values()), 1.34)
for lab, v in [("M_the max (gom Lang 1,34)", mt), ("x noi tai tan cong 1,02", mt*1.02),
               ("x Q 1,10", mt*1.02*1.10), ("x Dao Chung Sat 1,035", mt*1.02*1.10*1.035),
               ("U1 x Ban The 1,04", mt*1.02*1.10*1.035*1.04),
               ("U1 neu kep M_the 1,30", 1.30*1.02*1.10*1.035*1.04),
               ("(loai bo) x 'danh ke bay' 1,25", mt*1.02*1.10*1.035*1.25)]:
    print(f"{lab:34s} {v:.3f} {'OK' if v <= 1.60 else 'VUOT 1,60'}")

# ---------- (C) ----------
print("\n## C. Oa: ti le CT theo thoi gian o nuoc sau f (sau x0,5, bo/nong x1,15)")
for f in (0.0, 0.2, 0.3, 0.38, 0.5, 0.8, 1.0):
    r = f*0.5 + (1-f)*1.15
    print(f"f={f:.2f}: CT x{r:.3f}  {'trong +-10%' if 0.9 <= r <= 1.1 else 'NGOAI'}  -> phut toi Vien Man C4 {348/(1.6*r):.0f}'")

# ---------- (D) ----------
print("\n## D. Vu bay: Bay = -8 The Luc/s, toc 6,4 x1,10 = 7,04 o/s; tran thoi gian theo canh")
TL = {1:(60,6), 2:(80,9), 3:(100,12), 4:(120,15)}
for c,(tl,cap) in TL.items():
    t = min(tl/8, cap); print(f"C{c}: The Luc {tl} -> {tl/8:.1f}s, tran {cap}s -> bay {t:.1f}s = {t*7.04:.0f} o (vung 64 o)")
print("Cat canh 0,6s; Lang Nha lao 4 o/0,35s. Ke phat hien Lang o khoang cach d (o), phan xa 0,25s:")
for d in (4, 6, 8, 10, 14):
    t_lang = max(0, (d-4)/6.0) + 0.35      # chay toi tam 4 o roi lao
    print(f"  d={d:2d}: Lang toi sau {t_lang:.2f}s vs Ke can 0,85s -> {'THOAT' if t_lang > 0.85 else 'BI NGAT (Rot)'}")

# ---------- (E) ----------
print("\n## E. Vong doi full C4, Mid (h=0,10/gio, PvP 60%, bao ve che do 2)")
F = {1:0.6, 2:0.8, 3:1.0, 4:1.3}
CTC = [(20,7,3),(50,18,8),(90,33,15),(140,52,23)]  # CT canh, tang Hau, kiep
CHAR = {"Linh Moc":(0.75,1.00), "Lang":(1.00,1.00), "Linh Nghi":(1.05,1.00), "Thanh Oa":(0.95,0.93), "Vu (Ke)":(1.10,1.00)}
def life(hm, rm, N=20000):
    T = 0; first = 0
    for n in range(N):
        tot = 0; L = 0
        while True:
            L += 1; t = 0; dead = False
            for c,(ctc,hau,kp) in enumerate(CTC, 1):
                hz = 0.10*hm*F[c]; pv = hz*0.6*(0.4 if c<=2 else 0.6); hz = pv + hz*0.4
                rate = 1.6*rm; dur = ctc/rate/60
                td = -math.log(random.random())/hz
                if td < dur: t += td; dead = True; break
                t += dur; p = 0.65
                while random.random() >= p:
                    redo = hau/rate/60
                    if random.random() < 1-math.exp(-hz*redo): dead = True; t += redo/2; break
                    t += redo; p = min(0.95, p+0.15)
                if dead: break
                t += kp/rate/60
            tot += t
            if not dead: break
        T += tot; first += (L == 1)
    return T/N, first/N
tot = 0
for k,(hm,rm) in CHAR.items():
    T,p = life(hm, rm); tot += T
    print(f"{k:10s} hazard x{hm:.2f} CT x{rm:.2f}: P(doi dau VM)={p*100:3.0f}%  gio/1 VM={T:.1f}h")
print(f"TONG lan dau Vien Man ca 5 (Mid): {tot:.1f}h  ~ {tot/3.4:.1f} tuan o 3,4h/tuan")
print(f"So sanh v1.1 (2 full + 3 lite): ~{2*4.8+3*2.3:.1f}h")
