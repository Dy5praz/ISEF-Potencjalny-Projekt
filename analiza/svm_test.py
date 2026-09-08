import numpy as np, itertools, pickle
from analiza import load_all, clean, TARGETS, AUX_NAMES
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

FS=256.0
FEAT_HZ=[7,8,9,14,16,18,21,24,27]

def feats(sig):
    # sig (n,256,3) -> FFT amplitudes at FEAT_HZ for each channel
    S=np.abs(np.fft.rfft(sig*np.hanning(256)[None,:,None],axis=1))
    f=np.fft.rfftfreq(256,1/FS)
    idx=[int(np.argmin(np.abs(f-x))) for x in FEAT_HZ]
    return S[:,idx,:].reshape(sig.shape[0],-1)

def build(recs, cols):
    X=[];y=[];g=[]
    for r in recs:
        sig=clean(r['tgt'],r['aux'],cols)
        X.append(feats(sig)); y.append(np.full(sig.shape[0],TARGETS.index(r['f0']))); g.append([r['subj']]*sig.shape[0])
    return np.vstack(X), np.concatenate(y), np.concatenate([np.array(a) for a in g])

def loso(X,y,g):
    accs={}
    for s in sorted(set(g)):
        te=g==s; tr=~te
        m=make_pipeline(StandardScaler(),LinearSVC(C=1.0,max_iter=5000,dual='auto'))
        m.fit(X[tr],y[tr])
        accs[s]=float((m.predict(X[te])==y[te]).mean()*100)
    return accs

if __name__=='__main__':
    recs=load_all()
    subsets={'O-only':[], 'wszystkie 6':[0,1,2,3,4,5], 'Cz sam':[0],
             'bez Cz':[1,2,3,4,5], 'mięśniowe (neck+cheek+jaw)':[3,4,5],
             'jaw sam':[5], 'neck sam':[3], 'Cz+jaw':[0,5]}
    res={}
    for n,c in subsets.items():
        X,y,g=build(recs,c); a=loso(X,y,g)
        v=np.array([a[f'S{i:02d}'] for i in range(1,13)])
        res[n]=v
        print(f'{n:28s} {v.mean():5.1f} +/- {v.std(ddof=1):4.1f}')
    pickle.dump(res,open('svm.pkl','wb'))
