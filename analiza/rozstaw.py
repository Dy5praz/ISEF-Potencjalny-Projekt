import numpy as np, pickle, warnings; warnings.filterwarnings('ignore')
from analiza import load_all, clean, classify, TARGETS
recs=load_all()
# O1=0, O2=1, Oz=2. 10-20: O1-Oz ~ O2-Oz ~ 3-4 cm, O1-O2 ~ 7 cm (odleglosci przyblizone)
derivs={
 'Oz (ref. maloowina, 1 kan.)'      : lambda t: t[:,:,[2]],
 'O1+O2+Oz (ref. maloowina, 3 kan.)': lambda t: t,
 'O1-Oz (~3,5 cm)'                  : lambda t: (t[:,:,0]-t[:,:,2])[:,:,None],
 'O2-Oz (~3,5 cm)'                  : lambda t: (t[:,:,1]-t[:,:,2])[:,:,None],
 'O1-O2 (~7 cm)'                    : lambda t: (t[:,:,0]-t[:,:,1])[:,:,None],
 'Oz-(O1+O2)/2 (laplasjan)'         : lambda t: (t[:,:,2]-(t[:,:,0]+t[:,:,1])/2)[:,:,None],
}
out={}
for n,f in derivs.items():
    per={}
    for r in recs:
        lab=TARGETS.index(r['f0'])
        per.setdefault(r['subj'],[]).append((classify(f(r['tgt']))==lab).astype(float))
    v=np.array([np.concatenate(per[f'S{i:02d}']).mean()*100 for i in range(1,13)])
    out[n]=v; print(f'{n:36s} {v.mean():5.1f} +/- {v.std(ddof=1):4.1f}')
pickle.dump(out,open('rozstaw.pkl','wb'))
