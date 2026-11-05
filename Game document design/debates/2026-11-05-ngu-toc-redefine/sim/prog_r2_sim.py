# PROG R2 sim: (A) stack audit & duel win prob, (B) life/restart Monte Carlo, (C) choice-tree build count
import math, random, itertools
from math import erf, sqrt, log
Phi=lambda z:0.5*(1+erf(z/sqrt(2)))
sigma=-log(1.77)/-1.036  # calibrated: gap x1.77 -> weaker wins 15%
print("## A. Duel win prob (same realm) theo ti le suc manh r; sigma=%.3f"%sigma)
for name,r in [("khong khac",1.0),("khac 1.10 vs 0.91",1.10/0.909),("khac 1.15 vs 0.87",1.15/0.87),("E 1.25 vs 0.80",1.25/0.80),("E x tong 1.25*1.15 vs 0.80/1.15",1.25*1.15/(0.8/1.15)),("khac cua 1 canh 1.77",1.77)]:
    print(f"{name:34s} r={r:.2f}  nguoi khac thang {Phi(log(r)/sigma)*100:.0f}%")
print("\n## A2. Tran tan cong (khong crit): Huyet Cuong 1.20*Ban The 1.10=1.32")
base=1.2*1.1
for name,q in [("E nhanh 1.25 (v1.0)",1.25),("E 1.25 * tuc 1.15 (cong don)",1.25*1.15),("E * SURV Gai x1.5 cho Nghia",1.25*1.5),("max(E,tuc) 1.25",1.25),("them Than Vi 1.05",1.25*1.05)]:
    t=base*q; print(f"{name:34s} {t:.2f} {'VUOT 1.77' if t>1.77 else 'ok (<1.77)'}  margin {1.77/t:.2f}")
print("Ty le cap co quan he (thu tu): 25 cap, 5 cung tuc, 10 sinh, 10 khac/bi khac => 40% gap chiu swing")

print("\n## B. Doi nhan vat reset hoan toan: P(hoan thanh) & gio ky vong / lan hoan thanh")
def life(L,h,prot=0.0,seed=1,N=40000):
    random.seed(seed); done=0; hours=0
    for _ in range(N):
        t=0
        while True:
            # hazard tang theo tien trinh: 0.5h dau (Au Linh prot) -> h
            tt=0; dead=False
            while tt<L:
                step=0.25; hz=h*(0.5+tt/L)*(1-prot if tt<min(1.0,L*0.2) else 1)
                if random.random()<hz*step: dead=True;break
                tt+=step
            t+=tt
            if not dead: done+=1; hours+=t; break
    return hours/N
for L in (2.6,6.1,11.5,3.0,5.5):
    row=[]
    for h in (0.05,0.10,0.20):
        p=math.exp(-h*L) # xap xi P hoan thanh voi hazard TB h
        row.append(f"h={h}: P={p*100:.0f}% T/hoanthanh={life(L,h):.1f}h")
    print(f"L={L:4.1f}h  "+" | ".join(row))

print("\n## C. Cay lua chon: 3 nhanh bac<=3, moi canh 1 pick; options: 3 (nhanh) +1 Thien Phu tu C2 +1 Hop Dao tu C4")
def builds(picks):
    states={ (0,0,0,0):1 }  # (b1,b2,b3,tp)
    for k in range(picks):
        ns={}
        for s in states:
            opts=[]
            for j in range(3):
                if s[j]<3:
                    t=list(s);t[j]+=1;opts.append(tuple(t))
            if k>=1 and s[3]<2:
                t=list(s);t[3]+=1;opts.append(tuple(t))
            for o in opts: ns[o]=1
        states=ns
    return states
def power(s,syn=0.5):
    v=lambda b:b**1.3
    p=sum(v(b) for b in s[:3])+1.2*s[3]
    # Hop Dao synergy: co >=2 nhanh bac>=1 cho +syn
    if sum(1 for b in s[:3] if b>=1)>=2: p+=syn
    return p
for picks,lab in [(3,"lite C1-C3 (3 pick)"),(4,"full C1-C4 (4 pick)"),(6,"full + 2 pick Hau ky")]:
    st=builds(picks); ps=[power(s) for s in st]
    print(f"{lab:24s} builds khac nhau={len(st):3d}  power min/max={min(ps):.2f}/{max(ps):.2f} (ratio {max(ps)/min(ps):.2f})")
# legacy cap
print("\n## F. Tran di san: attack cap 1.65*(1+x)<1.77 => x<=%.3f"%(1.77/1.65-1))
