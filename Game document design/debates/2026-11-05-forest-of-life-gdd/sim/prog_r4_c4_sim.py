#!/usr/bin/env python3
"""PROG R4 — C4 giá cái chết: so sánh A/B/C trên đường cong Thất Cảnh v2 (PROG-04c).
Mid 5×40' : 34' hiệu dụng/phiên, 30' đầu Mộng Tích +1 → 64 CT/phiên, 320 CT/tuần.
Hai cách hiểu hệ số Hồi Ức:
  M (nhân, như sim P R3): tốc độ = 64 × k CT/phiên.
  G (cộng vào Gia Trì, như PROG-17): mult = min(cap, 1 + Mộng(1, 30') + (k-1)), cap ×4 khi Hồi Ức.
Chạy: python3 prog_r4_c4_sim.py > prog_r4_c4_sim_output.md
"""
import random, statistics as st
random.seed(4)
REALM = [36, 100, 180, 280, 380, 520]; SPLIT = [0.30, 0.33, 0.37]; OV = [5, 15, 30, 45, 70]
ACTIVE, RESTED, BASE = 34, 30, 64
t = [REALM[r]*s for r in range(6) for s in SPLIT]
starts, c, rs = [], 0.0, {}
for i, x in enumerate(t):
    r = i//3+1
    if i % 3 == 0:
        if r > 1: c += OV[r-2]
        rs[r] = c
    starts.append(c); c += x

def per_session(k, mode):
    if k == 1: return BASE
    if mode == "M": return BASE*k
    m1 = min(4, 1+1+(k-1)); m2 = min(4, 1+(k-1))
    return RESTED*m1 + (ACTIVE-RESTED)*m2

def regain(seg, k, mode):  # seg: list of (CT, k)
    return sum(ct/per_session(kk, mode) for ct, kk in seg)

def hau_due(pos, R, i, plan, mode):
    if plan == "A":
        back = max(starts[i], pos-130); return regain([(pos-back, 1)], 1, mode)
    back = max(rs[R], pos-130)
    k = 1.5 if plan == "C" else 1
    return regain([(pos-back, k)], k, mode)

def luan_hoi(pos, R, kc, kp, mode):
    return regain([(rs[R], kc), (pos-rs[R], kp)], None, mode)

def sample(R):  # vị trí chết đều trong cảnh R
    i = 3*(R-1)+random.randrange(3); return i, starts[i]+random.random()*t[i]

print("# R4 C4 — chi phí chết (phiên Mid), Thất Cảnh v2\n")
print("Hồi Ức hiệu dụng mỗi phiên (CT): ", {f"×{k}": (per_session(k,'M'), per_session(k,'G')) for k in (1.5,2,3,4)}, "(M, G)\n")
for mode in ("M", "G"):
    print(f"\n## Cách hiểu {mode}\n")
    print("| Cảnh | Hậu Duệ A TB / tệ nhất | Hậu Duệ B TB / tệ nhất | Hậu Duệ C TB / tệ nhất | Luân Hồi ×4/×2 TB (tuần) | ×3/×1,5 TB (tuần) | PX ×3 (×4 từ C5)/×1,5 TB (tuần) |")
    print("|---|---|---|---|---|---|---|")
    for R in range(3, 7):
        N = 20000; res = {k: [] for k in ("A","B","C","L4","L3","LPX")}
        for _ in range(N):
            i, pos = sample(R)
            for p in "ABC": res[p].append(hau_due(pos, R, i, p, mode))
            res["L4"].append(luan_hoi(pos, R, 4, 2, mode))
            res["L3"].append(luan_hoi(pos, R, 3, 1.5, mode))
            kc = 4 if R >= 5 else 3
            res["LPX"].append(luan_hoi(pos, R, kc, 1.5, mode))
        f = lambda k: f"{st.mean(res[k]):.2f} / {max(res[k]):.2f}"
        w = lambda k: f"{st.mean(res[k]):.1f} ({st.mean(res[k])/5:.2f})"
        print(f"| C{R} | {f('A')} | {f('B')} | {f('C')} | {w('L4')} | {w('L3')} | {w('LPX')} |")
print("\nTrần PX: Hậu Duệ TB ≤1,5 / tệ nhất ≤3 phiên; Luân Hồi ≤1 tuần (5 phiên).")
# Kiểm tra động cơ đổi loài: tỉ lệ Luân Hồi/Hậu Duệ
