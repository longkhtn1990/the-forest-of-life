# PROG R2 — duel toan cuc 4 toc (dung yen, khong dia hinh), test nerf Lang
# Mo hinh don gian hoa tu prog_r1_nghi_sim.py; xu huong > con so.
import random, statistics as st
random.seed(7)
DR = lambda d: d/(d+1)
BASE = {"lang":dict(hp=420,cong=50,d=0.40),"oa":dict(hp=330,cong=30,d=0.30),
        "nha":dict(hp=260,cong=26,d=0.25),"nghi":dict(hp=300,cong=22,d=0.25)}
def kit(name, c, cd, dt, me):
    yc = me["cong"]; out = yc*dt
    for k in cd: cd[k] -= dt
    if name == "lang":
        if cd["A"] <= 0: out += yc*1.5; cd["A"] = 12
        if c >= 3 and cd["B"] <= 0: out += yc*(1.6 if c==3 else 1.8) + yc*0.4; cd["B"] = 10
    elif name == "oa":
        if cd["A"] <= 0: out += yc*1.0; cd["A"] = 8
        if c >= 3 and cd["B"] <= 0: out += yc*(1.3 if c==3 else 1.5) + yc*(0.3 if c==3 else 0.45); cd["B"] = 10
    elif name == "nha":
        if cd["A"] <= 0: out += yc*(1.4 if c<4 else 1.6); cd["A"] = 10 if c<4 else 12
        if c >= 3 and cd["B"] <= 0: out += yc*1.8; cd["B"] = 10
    else:  # nghi
        alive = sum(1 for x in me["lhp"] if x > 0)
        lp = 0.15*alive*(1.5 if me["xung"] > 0 else 1); me["xung"] -= dt
        eff = yc*(1+lp); out = eff*dt
        if cd["A"] <= 0: me["xung"] = 4; cd["A"] = 10
        if c >= 2 and cd["B"] <= 0: out += eff*0.8; cd["B"] = 12
        if c >= 3 and cd["C"] <= 0: out += eff*(1.2 if c==3 else 1.5); cd["C"] = 14
    return out
def mk(name, c, mod):
    b = dict(BASE[name]); m = mod.get(name, {})
    s = 1.10**({1:0,2:3,3:6,4:9}[c])
    me = dict(hp=b["hp"]*m.get("hp",1)*s, cong=b["cong"]*m.get("cong",1)*s, d=b["d"])
    me["max"] = me["hp"]
    if name == "nghi": me["lhp"] = [me["max"]*0.12]*(2 if c==1 else 3); me["xung"] = 0
    return me
def hit(me, dmg, c, blk):
    dmg *= (1-DR(me["d"]))*random.uniform(0.85,1.15)
    if "lhp" in me:
        alive = [i for i,x in enumerate(me["lhp"]) if x > 0]
        if alive and random.random() < blk:
            i = alive[0]; me["lhp"][i] -= dmg
            if me["lhp"][i] <= 0:
                hs = 0.02 + 0.02*({1:1,2:4,3:7,4:10}[c]-1)/11
                me["hp"] = min(me["max"], me["hp"] + hs*me["max"])
            return
    me["hp"] -= dmg
def run(a, b, c, mod, blk=0.4, T=60, dt=0.05):
    A, B = mk(a,c,mod), mk(b,c,mod)
    ca = dict(A=random.uniform(0,1),B=random.uniform(0,2),C=2); cb = dict(A=random.uniform(0,1),B=random.uniform(0,2),C=2)
    t = 0
    while t < T:
        t += dt
        hit(B, kit(a,c,ca,dt,A), c, blk); hit(A, kit(b,c,cb,dt,B), c, blk)
        if B["hp"] <= 0 and A["hp"] <= 0: return 0.5, t
        if B["hp"] <= 0: return 1, t
        if A["hp"] <= 0: return 0, t
    return (1 if A["hp"]/A["max"] > B["hp"]/B["max"] else 0), T
def P(a,b,c,mod,N=300):
    r = [run(a,b,c,mod) for _ in range(N)]
    return sum(x for x,_ in r)/N, st.mean(t for _,t in r)
T4 = ["lang","oa","nha","nghi"]
VAR = [("v1.2 goc", {}),
       ("Lang Cong -10%", {"lang":dict(cong=0.90)}),
       ("Lang Cong -15%", {"lang":dict(cong=0.85)}),
       ("Lang Cong -15% HP -10%", {"lang":dict(cong=0.85,hp=0.90)}),
       ("Lang Cong -20% HP -10%", {"lang":dict(cong=0.80,hp=0.90)})]
for lab, mod in VAR:
    print(f"\n### {lab}  — P(hang thang cot), cung canh, block Linh 40%")
    for c in (2,4):
        print(f"C{c}: | " + " | ".join(
            f"{a}>{b} {P(a,b,c,mod)[0]:.0%}" for i,a in enumerate(T4) for b in T4[i+1:]))
    pt = P("lang","nghi",3,mod); print(f"  C3 Lang giet Nghi trung binh {pt[1]:.1f}s (KPI thoat >=4s)")

print("\n### Quet he so k nhan ca HP va Cong cua Lang (C2 / C4), N=300")
for k in (1.0, 0.85, 0.80, 0.75, 0.72, 0.70, 0.65):
    mod = {"lang":dict(cong=k,hp=k)}
    row = []
    for c in (2,4):
        row.append(f"C{c}: oa {P('lang','oa',c,mod)[0]:.0%} nha {P('lang','nha',c,mod)[0]:.0%} nghi {P('lang','nghi',c,mod)[0]:.0%}")
    print(f"k={k:.2f} Lang thang -> " + " || ".join(row) + f" | C3 TTK Nghi {P('lang','nghi',3,mod)[1]:.1f}s")
print("\n### Phuong an B: giu Lang, nang 3 toc moi x m (HP va Cong)")
for m in (1.15, 1.20, 1.25):
    mod = {t:dict(cong=m,hp=m) for t in ("oa","nha","nghi")}
    print(f"m={m:.2f} C4: lang>oa {P('lang','oa',4,mod)[0]:.0%} lang>nha {P('lang','nha',4,mod)[0]:.0%} lang>nghi {P('lang','nghi',4,mod)[0]:.0%} | oa>nghi {P('oa','nghi',4,mod)[0]:.0%} nha>nghi {P('nha','nghi',4,mod)[0]:.0%}")
