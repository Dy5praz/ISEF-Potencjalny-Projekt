import numpy as np, h5py, glob, os, warnings; warnings.filterwarnings('ignore')
from scipy.signal import butter, filtfilt
FS=256.0; TARGETS=[7.0,8.0,9.0]
ROOT=os.environ.get('EEG_DATA','un')

def load_cont():
    out=[]
    for f in sorted(glob.glob(os.path.join(ROOT,'S*','*_windows.mat'))):
        with h5py.File(f,'r') as h:
            tgt=np.array(h['X_tgt_raw']); aux=np.array(h['X_aux_raw'])
            st=np.array(h['meta/idx_starts']).flatten(); f0=float(np.array(h['meta/f0_Hz']).flatten()[0])
        assert np.allclose(np.diff(st),256), 'okna nie sa ciagle'
        out.append(dict(subj=os.path.basename(os.path.dirname(f)),f0=f0,
                        tgt=tgt.reshape(-1,tgt.shape[2]), aux=aux.reshape(-1,aux.shape[2])))
    return out

def refs(f0,n,nh=3):
    t=np.arange(n)/FS; r=[]
    for h in range(1,nh+1):
        r+= [np.sin(2*np.pi*h*f0*t), np.cos(2*np.pi*h*f0*t)]
    return np.array(r).T

def cca(X,Y):
    X=X-X.mean(0); Y=Y-Y.mean(0)
    qx,_=np.linalg.qr(X); qy,_=np.linalg.qr(Y)
    return float(np.clip(np.linalg.svd(qx.T@qy,compute_uv=False)[0],0,1))

SB=[(6,50),(13,50),(20,50)]; W=np.array([(n+1)**-1.25+0.25 for n in range(3)])

def acc_for(recs, T, montage):
    n=int(T*FS); F=[butter(4,[lo/(FS/2),hi/(FS/2)],btype='band') for lo,hi in SB]
    R={f:refs(f,n) for f in TARGETS}
    per={}
    for r in recs:
        sig=montage(r['tgt']); lab=TARGETS.index(r['f0'])
        nw=sig.shape[0]//n
        seg=sig[:nw*n].reshape(nw,n,-1)
        fl=[filtfilt(b,a,seg,axis=1) for b,a in F]
        ok=[]
        for w in range(nw):
            sc=[sum(W[k]*cca(fl[k][w],R[f])**2 for k in range(3)) for f in TARGETS]
            ok.append(int(np.argmax(sc))==lab)
        per.setdefault(r['subj'],[]).extend(ok)
    return np.array([np.mean(per[f'S{i:02d}'])*100 for i in range(1,13)])

def itr(N,P,t):
    P=min(max(P,1e-6),1-1e-9)
    return (np.log2(N)+P*np.log2(P)+(1-P)*np.log2((1-P)/(N-1)))*60/t

recs=load_cont()
M={'odniesienie odlegle (O1,O2,Oz)': lambda t:t,
   'montaz roznicowy w module'      : lambda t:np.stack([t[:,0]-t[:,1],t[:,0]-t[:,2],t[:,1]-t[:,2]],1)}
print(f"{'okno':>6} | {'odl.ref %':>10} {'ITR':>6} | {'roznicowy %':>12} {'ITR':>6} | strata")
for T in [0.5,1,2,3,4,5]:
    a=acc_for(recs,T,M['odniesienie odlegle (O1,O2,Oz)']).mean()
    b=acc_for(recs,T,M['montaz roznicowy w module']).mean()
    print(f"{T:5.1f}s | {a:9.1f} {itr(3,a/100,T):6.1f} | {b:11.1f} {itr(3,b/100,T):6.1f} | {a-b:+5.1f} pp")
