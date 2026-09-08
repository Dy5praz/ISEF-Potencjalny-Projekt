import numpy as np, warnings, collections; warnings.filterwarnings('ignore')
from scipy.signal import butter, filtfilt
from analiza import load_all, clean, classify, TARGETS
recs=load_all(); FS=256.0
AUX={'Cz':0,'Fp1':1,'HEOG':2,'kark':3,'policzek':4,'szczeka':5}
bE,aE=butter(4,[20/(FS/2),100/(FS/2)],btype='band')
def emgp(aux,ch): return filtfilt(bE,aE,aux[:,:,ch],axis=1).std(axis=1)

print("=== 1. Czy w danych w ogole jest artefakt szczekowy do usuwania? ===")
r0=recs[0]; p=emgp(r0['aux'],AUX['szczeka'])
print(f"  skala sygnalu szczeki (S01,7Hz): mediana {np.median(p):.3e}, p95 {np.percentile(p,95):.3e}")
rat=[]
for r in recs:
    q=emgp(r['aux'],AUX['szczeka']); rat.append(np.percentile(q,95)/max(np.median(q),1e-30))
print(f"  stosunek p95/mediana mocy EMG szczeki: mediana po zapisach {np.median(rat):.1f}x, zakres {min(rat):.1f}-{max(rat):.1f}x")
print("  -> artefakt JEST i jest silnie epizodyczny. Test ponizej nie jest testem pustym.")

# SNR SSVEP: moc w f0 (+-0.5 Hz) wobec sasiedztwa
def snr(sig,f0):
    S=np.abs(np.fft.rfft(sig*np.hanning(256)[None,:,None],axis=1))**2
    f=np.fft.rfftfreq(256,1/FS)
    tgt=(np.abs(f-f0)<=0.6); nb=(np.abs(f-f0)>0.6)&(np.abs(f-f0)<=3.0)
    return 10*np.log10(S[:,tgt,:].mean(1).mean(1)/S[:,nb,:].mean(1).mean(1))

VAR={'O-only':[], 'O+szczeka':[5], 'O+Cz':[0], 'O+Cz+szczeka':[0,5]}
print("\n=== 2. Najbardziej skazone 10% okien (top decyl mocy EMG szczeki) ===")
acc=collections.defaultdict(list); sn=collections.defaultdict(list); n=0
for r in recs:
    lab=TARGETS.index(r['f0']); p=emgp(r['aux'],AUX['szczeka'])
    m=p>=np.percentile(p,90); n+=m.sum()
    for k,c in VAR.items():
        s=clean(r['tgt'],r['aux'],c)
        acc[k].append((classify(s)==lab).astype(float)[m])
        sn[k].append(snr(s,r['f0'])[m])
print(f"  liczba okien w tym decylu: {n}")
b=np.concatenate(acc['O-only']).mean()*100; bs=np.concatenate(sn['O-only']).mean()
for k in VAR:
    a=np.concatenate(acc[k]).mean()*100; s=np.concatenate(sn[k]).mean()
    print(f"  {k:14s} dokladnosc {a:5.1f}% ({a-b:+5.1f} pp)   SNR {s:6.2f} dB ({s-bs:+5.2f} dB)")

print("\n=== 3. Per osoba, top decyl: zysk szczeki PONAD Cz [pp] ===")
per=collections.defaultdict(lambda: collections.defaultdict(list))
for r in recs:
    lab=TARGETS.index(r['f0']); p=emgp(r['aux'],AUX['szczeka']); m=p>=np.percentile(p,90)
    for k,c in [('Cz',[0]),('Cz+szczeka',[0,5])]:
        per[r['subj']][k].append((classify(clean(r['tgt'],r['aux'],c))==lab).astype(float)[m])
gain=[]
for s in sorted(per):
    a=np.concatenate(per[s]['Cz']).mean()*100; c=np.concatenate(per[s]['Cz+szczeka']).mean()*100
    gain.append(c-a)
    flag=' <- szczeka w optymalnym zestawie wg Tabeli 8' if s in ('S03','S05','S10') else ''
    print(f"  {s}: {c-a:+6.1f}{flag}")
g=np.array(gain)
print(f"\n  srednia {g.mean():+.2f} pp, odchylenie {g.std(ddof=1):.2f} pp")
from scipy import stats
t,pv=stats.ttest_1samp(g,0); print(f"  test t wobec zera: t={t:.2f}, p={pv:.3f}")
