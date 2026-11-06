# PROG R3 bo sung — nhip choi x1/x1.5/x2/x3 + lop an toan; can bang 36 dong Huong cua Linh Nghi
# Mo hinh vong doi giu tu sim B (ngu-toc-redefine/prog_r3_sim.py): hazard/gio theo canh, PvP share,
# Au Linh (C1-C2 PvP x0.4, chi khi t<180'), Trong Thuong C3+ (PvP x0.6), kiep that bai != chet.
import random, math, itertools
random.seed(11)

BASE_MIN = [14, 36, 66, 102]           # phut Mid moi canh (v1.2), da gom kiep
HAU_SHARE = 0.37 * 0.87                # phan thoi gian tang Hau trong canh (lam lai khi kiep hong)
F_CANH = [0.6, 0.8, 1.0, 1.3]
PERSONA = {  # h co so/gio, PvP share, phut/phien, phien/tuan
    "P1 xe buyt": (0.06, 0.40, 15, 14),
    "Mid":        (0.10, 0.60, 40, 5),
    "P2 ke san":  (0.18, 0.75, 60, 5),
}
OPTIONS = {"x1 (v1.2)": [1, 1, 1, 1],
           "A x1.5 deu": [1.5, 1.5, 1.5, 1.5],
           "B x2 lech": [1.4, 1.9, 2.0, 2.2],
           "C x3 deu": [3, 3, 3, 3]}
KIEP_P = 0.65

def life(mins, h, s, safe):
    """1 doi. safe: dict(dens=bool, du_am=prev_max or None, bq=float). Tra (hoan thanh?, phut, canh max dat)"""
    t = 0.0
    k_avg = sum(mins) / sum(BASE_MIN)
    for c in range(4):
        dur = mins[c]
        if safe.get("du_am") is not None and c < safe["du_am"] and c < 3:
            dur = dur / 1.5                       # Du Am: CT x1.5 o canh da qua doi truoc (tru C4)
        bq = safe.get("bq", 0.0)                  # ti le thoi gian Be Quan/Nhap Dinh co CT (hazard ~0)
        expo = dur * (1 - bq) / 60                # gio phoi nhiem
        hz = h * F_CANH[c]
        if safe.get("dens"): hz *= (mins[c] / BASE_MIN[c]) ** -0.5
        pvp, env = hz * s, hz * (1 - s)
        if c <= 1 and t < 180: pvp *= 0.4
        elif c >= 2: pvp *= 0.6
        hz = pvp + env
        td = -math.log(random.random()) / hz
        if td < expo:
            return False, t + td * 60 / (1 - bq), c
        t += dur
        p = KIEP_P
        while random.random() > p:               # kiep hong -> lam lai tang Hau
            redo = dur * HAU_SHARE
            if random.random() < 1 - math.exp(-hz * redo * (1 - bq) / 60):
                return False, t + redo / 2, c
            t += redo; p = min(0.95, p + 0.15)
    return True, t, 4

def run(mins, h, s, safe_cfg, N=12000):
    first_ok = 0; total = 0.0; losses = []
    for _ in range(N):
        prev = None; tt = 0.0; first = True
        while True:
            cfg = dict(safe_cfg)
            cfg["du_am"] = prev if safe_cfg.get("du_am") else None
            ok, t, cmax = life(mins, h, s, cfg)
            tt += t
            if first: first_ok += ok; first = False
            if ok: break
            losses.append(t); prev = max(prev or 0, cmax)
        total += tt
    lost = sum(losses) / len(losses) if losses else 0
    exp_lost = sum(losses) / N
    return first_ok / N, total / N / 60, lost, exp_lost

print("## 1. Phut Mid moi canh (khong chet) va so phien")
for name, k in OPTIONS.items():
    m = [b * x for b, x in zip(BASE_MIN, k)]
    cum = list(itertools.accumulate(m))
    print(f"{name:12s} C1 {m[0]:4.0f}' C2 {m[1]:4.0f}' C3 {m[2]:4.0f}' C4 {m[3]:4.0f}' | doi {cum[-1]:4.0f}' ({cum[-1]/60:.1f}h)"
          f" | phien Mid(40') {cum[-1]/40:4.1f} | P1(15') {cum[-1]/15:4.1f}"
          f" | phien Mid/canh {' / '.join(f'{x/40:.1f}' for x in m)}")

SAFE = {"S0 khong": {}, "S1 mat do": {"dens": True}, "S2 Du Am": {"du_am": True},
        "S3 Be Quan 20%": {"bq": 0.2}, "S1+S3": {"dens": True, "bq": 0.2}, "S1+S2+S3": {"dens": True, "du_am": True, "bq": 0.2}}
print("\n## 2. Vong doi: P(doi dau Vien Man) | gio/1 Vien Man | phut mat TB moi lan chet | phut mat ky vong moi Vien Man")
for name, k in OPTIONS.items():
    m = [b * x for b, x in zip(BASE_MIN, k)]
    for sname, cfg in SAFE.items():
        if name == "x1 (v1.2)" and sname != "S0 khong": continue
        row = []
        for pn, (h, s, ses, wk) in PERSONA.items():
            p, hrs, lost, el = run(m, h, s, cfg, N=6000)
            row.append(f"{pn}: {p*100:3.0f}% {hrs:4.1f}h mat {lost:4.0f}' kv {el:4.0f}' ({hrs*60/ses/wk:.1f} tuan)")
        print(f"{name:12s} {sname:15s} | " + " | ".join(row))

# ---------------- 3. Can bang 36 dong Huong ----------------
# Moi node: he so (dps, ehp_bai_trong, CT/phut, party) — ngan sach huong: tang o the manh, tra o diem yeu.
GOC = {"Binh": (1.02, 1.08, 0.96, 0.98), "Phu": (0.93, 0.97, 1.06, 1.06),
       "Huyet": (0.95, 1.10, 0.97, 0.97), "Vien": (0.93, 1.00, 1.04, 1.07)}
TRUNG = {"HanhQuan": (("Binh", "Phu"), (1.02, 1.00, 0.99, 1.02)),
         "ToanDoc": (("Binh", "Vien"), (1.02, 1.00, 0.98, 1.05)),
         "PhucDia": (("Binh", "Huyet"), (1.02, 1.05, 0.98, 0.97)),
         "MachNgam": (("Huyet", "Phu"), (0.94, 1.08, 1.03, 1.02)),
         "DiepVien": (("Vien", "Huyet"), (0.96, 1.04, 1.04, 0.98)),
         "MucRep": (("Vien", "Phu"), (0.95, 0.98, 1.02, 1.08))}
DINH = {"Binh": (1.00, 1.05, 0.98, 1.03), "Phu": (0.97, 0.99, 1.04, 1.05),
        "Huyet": (0.98, 1.02, 1.00, 0.98), "Vien": (0.97, 1.00, 1.03, 1.05)}
THUAN = (1.00, 1.03, 1.02, 1.01)        # Thang cua A1 Trung (data, khong cong dps)
W = (0.35, 0.25, 0.25, 0.15)            # trong so: dps, song sot bai trong, kinh te, party
def mul(a, b): return tuple(x * y for x, y in zip(a, b))
lines = []
for g, gv in GOC.items():
    for t, (par, tv) in TRUNG.items():
        if g not in par: continue
        for d in list(par) + ["Thuan"]:
            dv = THUAN if d == "Thuan" else DINH[d]
            v = mul(mul(gv, tv), dv)
            score = math.prod(x ** w for x, w in zip(v, W))
            lines.append((f"{g}>{t}>{d}", v, score))
lines.sort(key=lambda x: -x[2])
sc = [l[2] for l in lines]
print(f"\n## 3. {len(lines)} dong Huong. Diem tong (hinh hoc co trong so) max {max(sc):.3f} min {min(sc):.3f} chenh {max(sc)/min(sc):.3f}")
for lab, v, s_ in lines[:4] + [("...", (0, 0, 0, 0), 0)] + lines[-4:]:
    if lab == "...": print("..."); continue
    print(f"  {lab:24s} dps {v[0]:.2f} ehp {v[1]:.2f} CT {v[2]:.2f} party {v[3]:.2f} | tong {s_:.3f}")
for i, nm in enumerate(("dps", "ehp", "CT", "party")):
    col = [l[1][i] for l in lines]
    print(f"  truc {nm:5s}: max {max(col):.2f} min {min(col):.2f} chenh {max(col)/min(col):.2f}")
dps = [l[1][0] for l in lines]; ehp = [l[1][1] for l in lines]
print(f"dps max {max(dps):.3f} (tran H<=1,05? {'OK' if max(dps)<=1.05+1e-9 else 'VUOT'}) | ehp min {min(ehp):.3f} -> TTK Lang C3 = 8,3s x ehp = {8.3*min(ehp):.1f}s (>=6s)")
OMEGA_NGHI = 1.25 * 1.10 * 1.035
print(f"Omega Nghi max = M_the 1,25 x Q 1,10 x DC 1,035 x H {max(dps):.3f} = {OMEGA_NGHI*max(dps):.3f} (<=1,60)")
print(f"Template: M_the<=1,30 x Noi tai 1,02 x 1,10 x 1,035 x H 1,05 = {1.30*1.02*1.10*1.035*1.05:.3f}")
# moi cap Goc: diem tot nhat cua Goc
for g in GOC:
    best = max(s_ for lab, v, s_ in lines if lab.startswith(g + ">"))
    worst = min(s_ for lab, v, s_ in lines if lab.startswith(g + ">"))
    print(f"  Goc {g:6s}: dong tot nhat {best:.3f} / te nhat {worst:.3f}")
