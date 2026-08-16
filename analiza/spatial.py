import numpy as np, pickle
from analiza import load_all, clean, classify, TARGETS
from svm_test import feats, loso
import warnings; warnings.filterwarnings('ignore')

def transform(tgt, mode):
    O1,O2,Oz = tgt[:,:,0],tgt[:,:,1],tgt[:,:,2]
    if mode=='raw':      return tgt
    if mode=='car3':     return tgt - tgt.mean(axis=2,keepdims=True)
    if mode=='bipolar':  return np.stack([O1-Oz,O2-Oz,O1-O2],axis=2)
    if mode=='lap':      return np.stack([Oz-(O1+O2)/2, O1-Oz, O2-Oz],axis=2)
    raise ValueError(mode)

MODES=['raw','car3','bipolar','lap']
recs=load_all()

print('=== FBCCA (bez uczenia) ===')
fb={}
for m in MODES:
    per={}
    for r in recs:
        lab=TARGETS.index(r['f0']); sig=transform(r['tgt'],m)
        per.setdefault(r['subj'],[]).append((classify(sig)==lab).astype(float))
    v=np.array([np.concatenate(per[f'S{i:02d}']).mean()*100 for i in range(1,13)])
    fb[m]=v; print(f'  O {m:8s} {v.mean():5.1f} +/- {v.std(ddof=1):4.1f}')
# Cz-regressed reference point
per={}
for r in recs:
    lab=TARGETS.index(r['f0']); sig=clean(r['tgt'],r['aux'],[0])
    per.setdefault(r['subj'],[]).append((classify(sig)==lab).astype(float))
v=np.array([np.concatenate(per[f'S{i:02d}']).mean()*100 for i in range(1,13)])
fb['Cz-reg']=v; print(f'  O {"Cz-reg":8s} {v.mean():5.1f} +/- {v.std(ddof=1):4.1f}')
# car3 AND Cz regression combined
per={}
for r in recs:
    lab=TARGETS.index(r['f0']); sig=transform(clean(r['tgt'],r['aux'],[0]),'car3')
    per.setdefault(r['subj'],[]).append((classify(sig)==lab).astype(float))
v=np.array([np.concatenate(per[f'S{i:02d}']).mean()*100 for i in range(1,13)])
fb['car3+Cz']=v; print(f'  O {"car3+Cz":8s} {v.mean():5.1f} +/- {v.std(ddof=1):4.1f}')

print('\n=== SVM/FFT, LOSO ===')
sv={}
for m in MODES+['Cz-reg','car3+Cz']:
    X=[];y=[];g=[]
    for r in recs:
        if m=='Cz-reg': sig=clean(r['tgt'],r['aux'],[0])
        elif m=='car3+Cz': sig=transform(clean(r['tgt'],r['aux'],[0]),'car3')
        else: sig=transform(r['tgt'],m)
        X.append(feats(sig)); y.append(np.full(sig.shape[0],TARGETS.index(r['f0']))); g.append([r['subj']]*sig.shape[0])
    X=np.vstack(X);y=np.concatenate(y);g=np.concatenate([np.array(a) for a in g])
    a=loso(X,y,g); v=np.array([a[f'S{i:02d}'] for i in range(1,13)])
    sv[m]=v; print(f'  O {m:8s} {v.mean():5.1f} +/- {v.std(ddof=1):4.1f}')
pickle.dump({'fbcca':fb,'svm':sv},open('spatial.pkl','wb'))
