import numpy as np, collections, warnings, os; warnings.filterwarnings('ignore')
from scipy.signal import butter, filtfilt
from analiza import load_all, TARGETS
FS=256.0
recs=load_all()
b,a=butter(4,[6/(FS/2),50/(FS/2)],btype='band')

def mont(t,mode):
    if mode=='ref-odlegle': return t
    if mode=='bipolarny':   return np.stack([t[:,:,0]-t[:,:,1],t[:,:,0]-t[:,:,2],t[:,:,1]-t[:,:,2]],2)
    if mode=='1kan-ref':    return t[:,:,[2]]
    if mode=='1kan-bip':    return (t[:,:,0]-t[:,:,2])[:,:,None]

def trca_w(X):
    """X: (n_trials, n_samp, n_ch) -> filtr przestrzenny"""
    n,ns,nc=X.shape
    Xc=X-X.mean(1,keepdims=True)
    S=np.zeros((nc,nc))
    for i in range(n):
        for j in range(n):
            if i==j: continue
            S+=Xc[i].T@Xc[j]
    U=Xc.reshape(-1,nc)
    Q=U.T@U
    ev,evec=np.linalg.eig(np.linalg.pinv(Q)@S)
    return np.real(evec[:,np.argmax(np.real(ev))])

def run(mode, nfold=5):
    per={}
    bysub=collections.defaultdict(lambda: collections.defaultdict(list))
    for r in recs:
        sig=filtfilt(b,a,mont(r['tgt'],mode),axis=1)
        bysub[r['subj']][TARGETS.index(r['f0'])].append(sig)
    for s,cls in bysub.items():
        data={k:np.concatenate(v,0) for k,v in cls.items()}
        nmin=min(d.shape[0] for d in data.values())
        idx={k:np.arange(nmin) for k in data}
        ok=[]
        folds=np.array_split(np.arange(nmin),nfold)
        for f in folds:
            tr={k:np.delete(data[k][:nmin],f,axis=0) for k in data}
            W={k:trca_w(tr[k]) for k in tr}
            T={k:(tr[k].mean(0)@W[k]) for k in tr}
            for k in data:
                for x in data[k][:nmin][f]:
                    sc=[np.corrcoef(x@W[c], T[c])[0,1] for c in sorted(T)]
                    ok.append(int(np.argmax(sc))==k)
        per[s]=np.mean(ok)*100
    v=np.array([per[f'S{i:02d}'] for i in range(1,13)])
    return v

print(f"{'montaz':16s} {'TRCA':>16s}")
res={}
for m in ['ref-odlegle','bipolarny','1kan-ref','1kan-bip']:
    v=run(m); res[m]=v
    print(f"{m:16s} {v.mean():7.1f} +/- {v.std(ddof=1):4.1f}")
print()
print(f"strata montazu bipolarnego wg TRCA:  {res['ref-odlegle'].mean()-res['bipolarny'].mean():+.1f} pp")
print(f"  (wg FBCCA bylo: -9,3 pp)")
print(f"strata 1 kanalu bipolarnego wg TRCA: {res['ref-odlegle'].mean()-res['1kan-bip'].mean():+.1f} pp")
print(f"  (wg FBCCA bylo: -24,5 pp)")
