import random, statistics as st
# nguon: (ten, % CT/phut, so su kien/phut, gia tri su kien tu CT) ; CT/phut = rate*val
sp = {
 "Linh Ly [Thuy]": [("An tao/au trung/xac chim",.45,3),("Thanh Tri(Thuy Mach)",.25,0.5),("Thoat Sinh+NguocDong",.30,0.1)],
 "Linh Nghia [Trung]": [("Mang moi/don xac ve to",.40,2.5),("Tiep te Bau",.25,0.4),("Bau/Linh dac thu",.35,0.09)],
 "Linh Tuoc [Vu]":   [("Moc hat/trung",.40,2),("Gay Binh Minh/do tham",.25,0.25),("Doi dau+Thoat Sinh",.35,0.06)],
}
random.seed(1)
def pois(l):
    import math; L=math.exp(-l);k=0;p=1
    while True:
        p*=random.random()
        if p<=L: return k
        k+=1
for n,src in sp.items():
    out=[]
    for _ in range(3000):
        t=0
        for _,sh,r in src:
            lam=r*30; v=sh/r      # 30 phut, moi su kien mang sh/r CT/phut-tuong-duong
            t+=pois(lam)*v
        out.append(t/30)
    m=st.mean(out);print(n,"mean CT/phut=%.3f CV=%.1f%%"%(m,100*st.stdev(out)/m))
