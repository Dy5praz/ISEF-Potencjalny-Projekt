import numpy as np, warnings, os; warnings.filterwarnings('ignore')
from scipy.signal import butter, filtfilt
from analiza import load_all, clean, classify, TARGETS
recs=load_all(); FS=256.0

# moc EMG szczeki w oknie: pasmo 20-100 Hz (EMG), odchylenie standardowe
bE,aE=butter(4,[20/(FS/2),100/(FS/2)],btype='band')
AUX={'Cz':0,'Fp1':1,'HEOG':2,'kark':3,'policzek':4,'szczeka':5}

def emg_power(aux, ch):
    x=filtfilt(bE,aE,aux[:,:,ch],axis=1)
    return x.std(axis=1)

# --- 1. ile okien jest w ogole skazonych ---
print("=== rozklad mocy EMG szczeki, per osoba (kwantyle 50/80/95%) ===")
allp=[]
for r in recs:
    p=emg_power(r['aux'],AUX['szczeka']); allp.append((r['subj'],p))
import collections
bysub=collections.defaultdict(list)
for s,p in allp: bysub[s].extend(p)
for s in sorted(bysub):
    v=np.array(bysub[s]); print(f"  {s}: mediana {np.median(v):6.2f}  p80 {np.percentile(v,80):7.2f}  p95 {np.percentile(v,95):8.2f}  max {v.max():9.2f}  (stosunek p95/mediana = {np.percentile(v,95)/np.median(v):5.1f})")

# --- 2. dokladnosc w podziale na kwintyle mocy EMG szczeki (per osoba) ---
VAR={'O-only':[], 'O+szczeka':[AUX['szczeka']], 'O+Cz':[AUX['Cz']], 'O+Cz+szczeka':[AUX['Cz'],AUX['szczeka']],
     'O+miesniowe(3)':[AUX['kark'],AUX['policzek'],AUX['szczeka']]}
NB=5
res={k:[[] for _ in range(NB)] for k in VAR}
for r in recs:
    lab=TARGETS.index(r['f0'])
    p=emg_power(r['aux'],AUX['szczeka'])
    # kwintyle w obrebie zapisu
    edges=np.quantile(p,np.linspace(0,1,NB+1)); edges[-1]+=1e-9
    bin_id=np.clip(np.digitize(p,edges[1:-1]),0,NB-1)
    for name,cols in VAR.items():
        pred=classify(clean(r['tgt'],r['aux'],cols))
        ok=(pred==lab).astype(float)
        for b in range(NB): 
            m=bin_id==b
            if m.any(): res[name][b].append(ok[m])
print("\n=== dokladnosc [%] wg kwintyla mocy EMG szczeki w oknie ===")
print(f"{'wariant':16s} " + " ".join(f"Q{i+1:d}" .rjust(7) for i in range(NB)))
base=None
for name in VAR:
    row=[np.concatenate(res[name][b]).mean()*100 for b in range(NB)]
    if name=='O-only': base=row
    print(f"{name:16s} " + " ".join(f"{v:7.1f}" for v in row))
print(f"{'zysk szczeki':16s} " + " ".join(f"{np.concatenate(res['O+szczeka'][b]).mean()*100-base[b]:+7.1f}" for b in range(NB)))
print(f"{'zysk Cz':16s} " + " ".join(f"{np.concatenate(res['O+Cz'][b]).mean()*100-base[b]:+7.1f}" for b in range(NB)))
print(f"{'szczeka ponad Cz':16s} " + " ".join(f"{np.concatenate(res['O+Cz+szczeka'][b]).mean()*100-np.concatenate(res['O+Cz'][b]).mean()*100:+7.1f}" for b in range(NB)))
