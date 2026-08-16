import numpy as np, warnings, collections; warnings.filterwarnings('ignore')
from scipy.signal import butter, filtfilt, hilbert
from numpy.linalg import lstsq
from analiza import load_all, classify, TARGETS
recs=load_all(); FS=256.0
bE,aE=butter(4,[20/(FS/2),100/(FS/2)],btype='band')
bL,aL=butter(2,8/(FS/2),btype='low')

def regressors(aux, mode):
    """buduje macierz regresorow dla okna: aux (256,6)"""
    jaw=aux[:,5]; neck=aux[:,3]; cheek=aux[:,4]; cz=aux[:,0]
    R=[]
    if 'cz' in mode: R.append(cz)
    if 'lin' in mode: R += [jaw]
    if 'lin3' in mode: R += [jaw,neck,cheek]
    if 'env' in mode:
        for x in ([jaw] if 'env3' not in mode else [jaw,neck,cheek]):
            e=filtfilt(bL,aL,np.abs(hilbert(filtfilt(bE,aE,x))))
            R += [e, e*0+0]  # obwiednia
            R[-1]=e**2       # i jej kwadrat (nieliniowosc)
    if 'sq' in mode: R += [jaw**2]
    return np.column_stack(R) if R else None

def clean_mode(tgt,aux,mode):
    out=np.empty_like(tgt)
    for w in range(tgt.shape[0]):
        A=regressors(aux[w],mode)
        if A is None: out[w]=tgt[w]; continue
        A=np.column_stack([A,np.ones(256)])
        b,*_=lstsq(A,tgt[w],rcond=None); out[w]=tgt[w]-A@b
    return out

MODES=['brak','lin','sq','env','lin+env','lin3','lin3+env3','cz','cz+lin','cz+lin+env','cz+lin3+env3']
def emgp(aux): return filtfilt(bE,aE,aux[:,:,5],axis=1).std(axis=1)

print("=== wszystkie okna / najbardziej skazony decyl ===")
print(f"{'regresory':22s} {'wszystkie':>10s} {'decyl':>10s}")
res={}
for m in MODES:
    A=[];D=[]
    for r in recs:
        lab=TARGETS.index(r['f0'])
        ok=(classify(clean_mode(r['tgt'],r['aux'],m))==lab).astype(float)
        A.append(ok)
        p=emgp(r['aux']); D.append(ok[p>=np.percentile(p,90)])
    a=np.concatenate(A).mean()*100; d=np.concatenate(D).mean()*100
    res[m]=(a,d); print(f"{m:22s} {a:9.1f}% {d:9.1f}%")
print()
b,bd=res['brak']
print(f"zysk samej szczeki, najlepszy wariant nieliniowy: "
      f"{max(res[k][0] for k in ['lin','sq','env','lin+env'])-b:+.1f} pp (wszystkie), "
      f"{max(res[k][1] for k in ['lin','sq','env','lin+env'])-bd:+.1f} pp (decyl)")
c,cd=res['cz']
print(f"zysk kanalow miesniowych PONAD Cz, najlepszy wariant: "
      f"{max(res[k][0] for k in ['cz+lin','cz+lin+env','cz+lin3+env3'])-c:+.1f} pp (wszystkie), "
      f"{max(res[k][1] for k in ['cz+lin','cz+lin+env','cz+lin3+env3'])-cd:+.1f} pp (decyl)")
