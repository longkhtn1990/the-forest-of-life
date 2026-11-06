# PROG R1 — Linh Nghi: (A) timeline 12 tang, (B) chi so/tang, (C) kinh te CT & No, (D) duel TTK, (E) M_the / Omega
import random, statistics as st
random.seed(7)
k = lambda n: 1.10 ** (n - 1)
TIERS = [("C1S",1,6),("C1T",2,7),("C1H",3,7),("C2S",4,15),("C2T",5,16),("C2H",6,18),
         ("C3S",7,27),("C3T",8,30),("C3H",9,33),("C4S",10,42),("C4T",11,46),("C4H",12,52)]
KIEP = {1:3,2:8,3:15,4:23}
RATE = {1:23/14, 2:57/36, 3:105/66, 4:163/102}   # CT/phut khop moc Mid v1.2
LINH = {1:1,2:2,3:2,4:3,5:3,6:3,7:3,8:3,9:3,10:3,11:3,12:3}  # de xuat PROG-01: 1 -> 2 (C1T) -> 3 (C2S)
print("## A/B. Bang tang (Mid, khong chet)")
print("| Tang | n | phut vao | CT tang | HP Hau | HP Linh | Cong Hau | Linh | Cong hieu dung | DPS chuan* |")
t = 0.0
for name, n, ct in TIERS:
    c = int(name[1])
    L = LINH[n]; hp = 300*k(n); cg = 22*k(n)
    eff = cg*(1+0.15*L)
    xung = 0.4*0.15*0.5*L*cg            # Xung: phan Linh x1,5 trong 4/10s
    a1 = (1.2 if c == 3 else 1.5 if c == 4 else 0)/14
    dps = eff*1.0 + xung + eff*(0.8/12 + a1) if c >= 2 else eff + xung
    print(f"| {name} | {n} | {t:5.1f} | {ct} | {hp:5.0f} | {0.12*hp:4.0f} | {cg:4.1f} | {L} | {eff:5.1f} | {dps:5.1f} |")
    t += ct / RATE[c]
    if name.endswith("H"):
        tk = KIEP[c] / RATE[c]; print(f"| Kiep C{c} | | {t:5.1f} | {KIEP[c]} | | | | | | |"); t += tk
print(f"Ket thuc: {t:.0f}' (v1.2: 218')\n")

# ---------- C. Kinh te CT & No theo canh ----------
print("## C. Kinh te CT/No theo canh (ti le thoi gian -> CT/phut, ti trong, No rong/phut)")
SP = 5.4
def tha_trip(d, slow=0.7): return 2 + d/SP + d/(SP*slow)
D = {1:8, 2:14, 3:18, 4:22}
# hanh dong: (giay, CT, No-tuc-thi)
def acts(c):
    d = D[c]
    return {
      "an":     (5, 0.10, 7),
      "tha":    (tha_trip(d), 0.25, 0),
      "thabay": (tha_trip(d, 0.6) + 2, 0.70, 0),
      "moxac":  (12, 0.60, 12),
      "can":    (50, 3.0, 0),
      "san":    (8, 0.20, 6),
      "an_kho": (4, 0.0, 7*1.25),   # an do da Tha ve To
    }
MIX = {  # ti le thoi gian Hau
 1: {"an":0.45,"tha":0.35,"moxac":0.10,"san":0.10},
 2: {"an":0.15,"tha":0.30,"thabay":0.15,"moxac":0.20,"san":0.15,"an_kho":0.05},
 3: {"an":0.08,"tha":0.22,"thabay":0.12,"moxac":0.25,"can":0.10,"san":0.15,"an_kho":0.08},
 4: {"an":0.04,"tha":0.18,"thabay":0.12,"moxac":0.32,"can":0.10,"san":0.16,"an_kho":0.08},
}
IDLE = {1:0.22, 2:0.42, 3:0.52, 4:0.50}   # % thoi gian di chuyen/danh/tron/Bê Quan (khong sinh CT)
SAI = {1:0, 2:0.5, 3:1.0, 4:1.0}          # so Linh sai di Tha trung binh (de xuat PROG-02)
GROUP = {"an":"Tha+an","tha":"Tha+an","thabay":"Tha+an","an_kho":"Tha+an","sai":"Tha+an",
         "moxac":"Mo Xac","can":"Can Thuong/san","san":"Can Thuong/san"}
tot = {}
for c in (1,2,3,4):
    A = acts(c); act = 1-IDLE[c]; ct = 0; no = 0; share = {}
    for a, f in MIX[c].items():
        sec, cta, noa = A[a]; per_min = 60*act*f/sec
        ct += per_min*cta; no += per_min*noa
        share[GROUP[a]] = share.get(GROUP[a],0) + per_min*cta
    sai_ct = SAI[c]*60/tha_trip(D[c])*0.25*0.5  # Linh sai: 50% CT cua Hau
    ct += sai_ct; share["Tha+an"] += sai_ct
    L = 3 if c >= 2 else 1.5
    decay = 4 + L*(60/90)
    # Tha vat ve kho: moi chuyen Tha = 1 vat 7 No vao Kho (an lai x1,25 da tinh o an_kho)
    mins = {1:14,2:36,3:66,4:102}[c]
    for g,v in share.items(): tot[g] = tot.get(g,0) + v*mins
    print(f"C{c}: CT/phut {ct:4.2f} (muc tieu {RATE[c]:.2f}, lech {ct/RATE[c]-1:+.0%}) | " +
          " ".join(f"{g} {v/ct:.0%}" for g,v in share.items()) + f" | No vao {no:4.1f}/phut vs decay {decay:4.1f}")
s = sum(tot.values()); print("Ca doi (theo phut): " + " ".join(f"{g} {v/s:.0%}" for g,v in tot.items()) + "  (v1.2: 45/30/25)\n")

# ---------- D. Duel cung canh ----------
DR = lambda d: d/(d+1)          # cung tang: k trieu tieu
def nghi(c, L=None, hp_mul=1.0, cong=22, linh_pct=0.12, block=0.0, build=None, resp=None):
    L = L if L is not None else (2 if c == 1 else 3)
    b = build or {}
    return dict(kind="nghi", c=c, hp=300*hp_mul, hpmax=300*hp_mul, cong=cong, d=0.25, L=L+b.get("L4",0),
                lhp=300*linh_pct*(0.85 if b.get("L4") else 1), block=block, b=b, resp=resp)
def run(att, dfn_name, c, policy="hau", T=60, dt=0.05):
    # tra ve (thang?, thoi gian)
    n = att
    lhp = [n["lhp"]]*n["L"]; hp = n["hp"]
    ycfg = {"lang":dict(hp=420,cong=50,d=0.40),"oa":dict(hp=330,cong=30,d=0.30),"nha":dict(hp=260,cong=26,d=0.25)}[dfn_name]
    yhp = ycfg["hp"]; yc = ycfg["cong"]
    b = n["b"]
    hs = 0.02 + 0.02*({1:1,2:4,3:7,4:10}[c]-1)/11
    t = 0; cd = dict(x=random.uniform(0,1), tdx=1, dr=2, yA=random.uniform(0,0.5), yB=0, yC=1); xung = 0; bleed = []
    slowy = 0; stun = 0; poison_t = 0
    while t < T:
        t += dt
        alive = sum(1 for x in lhp if x > 0)
        # --- Nghi danh ---
        lpart = 0.15*alive*(1+b.get("ham",0))
        if xung > 0: lpart *= 1.5; xung -= dt
        eff = n["cong"]*(1 + lpart)
        dmg = eff*1.0*dt
        for key in ("x","tdx","dr"): cd[key] -= dt
        if cd["x"] <= 0: xung = 6 if b.get("van") else 4; cd["x"] = 10
        if c >= 2 and cd["tdx"] <= 0: dmg += eff*0.8; cd["tdx"] = 12
        if c >= 3 and cd["dr"] <= 0:
            dmg += eff*(1.2 if c == 3 else 1.5); cd["dr"] = 14
            if c == 4 and alive >= 3: stun = 0.5
        yhp -= dmg*(1-DR(ycfg["d"]))*random.uniform(0.85,1.15)
        if dfn_name == "oa":  # Nhua Da: can chien trung Oa
            hp -= yc*({1:.04,2:.06,3:.08,4:.10}[c])/2*dt*(1-DR(0.25))*2*0.5
        if yhp <= 0: return True, t
        # --- doi thu danh ---
        if stun > 0: stun -= dt; continue
        for key in ("yA","yB","yC"): cd[key] -= dt
        out = yc*1.0*dt
        if dfn_name == "lang":
            if cd["yA"] <= 0: out += yc*1.5; cd["yA"] = 12
            if c >= 3 and cd["yB"] <= 0:
                out += yc*(1.6 if c == 3 else 1.8); bleed.append([4 if c==3 else 6, yc*0.4/(4 if c==3 else 6)]); cd["yB"] = 10
        elif dfn_name == "oa":
            if cd["yA"] <= 0: out += yc*1.0; cd["yA"] = 8
            if c >= 3 and cd["yB"] <= 0:
                out += yc*(1.3 if c==3 else 1.5); bleed.append([3 if c==3 else 4, yc*(0.3 if c==3 else 0.45)/(3 if c==3 else 4)]); cd["yB"] = 10
        else:
            if cd["yA"] <= 0: out += yc*(1.4 if c < 4 else 1.6); stun_n = 0.8; cd["yA"] = 10 if c < 4 else 12
            if c >= 3 and cd["yB"] <= 0: out += yc*1.8; cd["yB"] = 10
        for bl in bleed:
            if bl[0] > 0: out += bl[1]*dt; bl[0] -= dt
        out *= (1-DR(n["d"]))*random.uniform(0.85,1.15)
        # muc tieu: Linh hay Hau
        to_linh = (policy == "linh" and alive > 0) or (random.random() < n["block"] and alive > 0)
        if dfn_name == "oa" and cd["yA"] > 7.9 and alive > 0: to_linh = True   # Quang Luoi trung Linh truoc
        if b.get("do") and alive > 0 and not to_linh:
            for i,x in enumerate(lhp):
                if x > 0: lhp[i] -= out*0.12; break
            out *= 0.88
        if to_linh:
            for i,x in enumerate(lhp):
                if x > 0:
                    lhp[i] -= out
                    if lhp[i] <= 0: hp = min(n["hpmax"], hp + hs*n["hpmax"])
                    break
        else: hp -= out
        for i,x in enumerate(lhp):
            if -1e8 < x <= 0 and lhp[i] != -1e9:
                hp = min(n["hpmax"], hp + hs*n["hpmax"]); lhp[i] = -1e9
        if n["resp"]:
            rt = n.setdefault("rt", 0) - dt; n["rt"] = rt
            if rt <= 0 and any(x == -1e9 for x in lhp):
                lhp[lhp.index(-1e9)] = n["lhp"]; n["rt"] = n["resp"]
        if hp <= 0: return False, t
    return yhp/ycfg["hp"] < hp/n["hpmax"], T
def duel(c, foe, N=400, **kw):
    pol = kw.pop("policy","hau")
    r = [run(nghi(c, **kw), foe, c, pol) for _ in range(N)]
    return sum(w for w,_ in r)/N, st.mean(tt for _,tt in r)
print("## D. Duel Nghi vs (cung tang, dung yen danh nhau, khong dia hinh) — P(Nghi thang), thoi gian TB")
print("| Canh | vs Lang (danh Hau) | vs Lang (block 40%) | vs Oa | vs Nha |")
for c in (1,2,3,4):
    a = duel(c,"lang"); b = duel(c,"lang",block=0.4); o = duel(c,"oa",block=0.4); h = duel(c,"nha",block=0.4)
    print(f"| C{c} | {a[0]:.0%} / {a[1]:.1f}s | {b[0]:.0%} / {b[1]:.1f}s | {o[0]:.0%} / {o[1]:.1f}s | {h[0]:.0%} / {h[1]:.1f}s |")
print("\nCan gat (C4, vs Lang, block 40%):")
for lab, kw in [("goc", {}), ("Cong 22->26", dict(cong=26)), ("Linh 12%->18% HP", dict(linh_pct=0.18)),
                ("HP Hau 300->340", dict(hp_mul=340/300)), ("Cong 26 + Linh 18%", dict(cong=26, linh_pct=0.18)),
                ("Cong 26 + Linh 18% + block 60% (san To)", dict(cong=26, linh_pct=0.18, block=0.6))]:
    kw2 = dict(block=0.4); kw2.update(kw)
    p = [duel(c,f,**kw2)[0] for c,f in ((4,"lang"),(4,"oa"),(4,"nha"),(2,"lang"))]
    print(f"  {lab:40s} Lang C4 {p[0]:.0%} | Oa C4 {p[1]:.0%} | Nha C4 {p[2]:.0%} | Lang C2 {p[3]:.0%}")

print("\nSan To (Linh hoi sinh tai cho moi resp giay, 1 con/lan), block 40%, C4 / C2 vs Lang:")
for resp in (8, 5, 3):
    for blk in (0.4, 0.6):
        a = duel(4,"lang",block=blk,resp=resp); b2 = duel(2,"lang",block=blk,resp=resp)
        print(f"  resp {resp}s block {blk:.0%}: C4 {a[0]:.0%} ({a[1]:.1f}s) | C2 {b2[0]:.0%}")
print("Thoat: Lang danh Hau, Nghi song duoc bao lau (s) = thoi gian TB cot 'danh Hau' o tren; Ham Ngam can 2s keo + CD 25s")

# ---------- E. M_the Toan Nghi day du ----------
print("\n## E. DPS tuong doi theo build (C4, vs muc tieu dung yen, khong chet Linh)")
def dps(L=3, ham=0, van=False, doan=0):
    cg = 1; lp = 0.15*L*(1+ham)*(1+doan)
    up = (6 if van else 4)/10
    base = (1+lp) + up*lp*0.5
    return base + (1+lp)*(0.8/12 + 1.5/14)
b0 = dps()
for lab, v in [("Ham Thep (I)", dps(ham=0.15)), ("Linh Thu Tu (II)", dps(L=4)), ("Van Nghi Xung (III)", dps(van=True)),
               ("Toan I+II", dps(L=4, ham=0.15)), ("Toan I+II+III", dps(L=4, ham=0.15, van=True)),
               ("Toan I-III + Doan Quan (2/3 uptime)", dps(L=4, ham=0.15, van=True, doan=0.08*0.67))]:
    print(f"  {lab:38s} x{v/b0:.3f}")
m = dps(L=4, ham=0.15, van=True, doan=0.08*0.67)/b0
print(f"Omega (PvE): {m:.3f} x Q 1,10 x Dao Chung Sat(Linh ~1,035) = {m*1.10*1.035:.3f}  (tran 1,60)")
