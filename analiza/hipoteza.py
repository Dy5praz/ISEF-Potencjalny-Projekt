import numpy as np, pickle, warnings; warnings.filterwarnings('ignore')
from analiza import load_all, classify, TARGETS
from numpy.linalg import lstsq
recs=load_all()

def bip(t): return np.stack([t[:,:,0]-t[:,:,1], t[:,:,0]-t[:,:,2], t[:,:,1]-t[:,:,2]],axis=2)
def ident(t): return t

def cleanX(tgt,aux,cols):
    if not cols: return tgt.copy()
    out=np.empty_like(tgt)
    for w in range(tgt.shape[0]):
        A=np.column_stack([aux[w][:,cols],np.ones(256)])
        b,*_=lstsq(A,tgt[w],rcond=None); out[w]=tgt[w]-A@b
    return out

subsets={'brak':[], 'Cz':[0], 'jaw':[5], 'neck':[3], 'neck+cheek+jaw':[3,4,5], 'wszystkie 6':[0,1,2,3,4,5]}
for mont_name,mont in [('ref. maloowina (jak w pracy)',ident),('bipolarny wewnatrz modulu',bip)]:
    print(f'\n=== montaz: {mont_name} ===')
    base=None
    for n,cols in subsets.items():
        per={}
        for r in recs:
            lab=TARGETS.index(r['f0'])
            sig=mont(cleanX(r['tgt'],r['aux'],cols))   # kompensacja PRZED wyznaczeniem roznic
            per.setdefault(r['subj'],[]).append((classify(sig)==lab).astype(float))
        v=np.array([np.concatenate(per[f'S{i:02d}']).mean()*100 for i in range(1,13)])
        if base is None: base=v.mean()
        print(f'  aux={n:16s} {v.mean():5.1f} +/- {v.std(ddof=1):4.1f}   delta {v.mean()-base:+5.1f} pp')
