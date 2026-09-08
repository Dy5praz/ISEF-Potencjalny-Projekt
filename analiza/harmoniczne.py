#!/usr/bin/env python3
"""Czy strata montazu zwartego jest wieksza dla harmonicznych niz dla podstawowej?
Rozdziela dwa mechanizmy:
 - gladkie pole SSVEP  -> strata podobna dla f0 i 2f0
 - zanieczyszczenie odniesienia sygnalem wzrokowym/miesniowym (ECeG, EMG karku)
   -> strata WIEKSZA dla 2f0, bo tam siedzi pasmo beta
"""
import h5py, numpy as np, glob, os
from scipy.signal import butter, filtfilt

ROOT=os.environ.get('EEG_DATA','un'); FS=256.0

def snr_at(x, f, fs=FS, nb=10):
    """SNR w dB: moc w prazku f wobec mediany 2*nb prazkow sasiednich."""
    n=x.shape[-1]
    X=np.fft.rfft(x*np.hanning(n), axis=-1)
    P=np.abs(X)**2
    fr=np.fft.rfftfreq(n, 1/fs)
    k=int(np.argmin(np.abs(fr-f)))
    sig=P[..., k]
    idx=[j for j in range(k-nb-2, k+nb+3) if abs(j-k)>2 and 0<=j<P.shape[-1]]
    noi=np.median(P[..., idx], axis=-1)
    return 10*np.log10(np.maximum(sig,1e-30)/np.maximum(noi,1e-30))

b,a = butter(4, [3/(FS/2), 60/(FS/2)], btype='band')
rows=[]
for f in sorted(glob.glob(os.path.join(ROOT,'S*','*_windows.mat'))):
    with h5py.File(f,'r') as h:
        tgt=np.array(h['X_tgt_raw'])           # (60,256,3) = O1,O2,Oz
        f0=float(np.array(h['meta/f0_Hz']).flatten()[0])
    tgt=filtfilt(b,a,tgt,axis=1)
    O1,O2,Oz = tgt[:,:,0], tgt[:,:,1], tgt[:,:,2]
    montaze = {
        'ref-odlegle (Oz)'      : Oz,
        'ref-odlegle (sr. 3 kan)': (O1+O2+Oz)/3.0,
        'zwarty O1-Oz'          : O1-Oz,
        'zwarty O2-Oz'          : O2-Oz,
        'zwarty laplasjan'      : Oz-(O1+O2)/2.0,
    }
    for name,sig in montaze.items():
        rows.append((name, f0, snr_at(sig,f0).mean(), snr_at(sig,2*f0).mean()))

import collections
agg=collections.defaultdict(lambda: [[],[]])
for name,f0,s1,s2 in rows:
    agg[name][0].append(s1); agg[name][1].append(s2)

print(f"{'montaz':26} {'SNR f0 [dB]':>12} {'SNR 2f0 [dB]':>13}")
base=None
res={}
for name in ['ref-odlegle (Oz)','ref-odlegle (sr. 3 kan)','zwarty O1-Oz','zwarty O2-Oz','zwarty laplasjan']:
    s1=np.mean(agg[name][0]); s2=np.mean(agg[name][1]); res[name]=(s1,s2)
    print(f"{name:26} {s1:12.2f} {s2:13.2f}")

print()
print("STRATA montazu zwartego wobec 'ref-odlegle (sr. 3 kan)':")
b1,b2=res['ref-odlegle (sr. 3 kan)']
print(f"{'montaz':26} {'strata f0':>11} {'strata 2f0':>12} {'roznica':>10}")
for name in ['zwarty O1-Oz','zwarty O2-Oz','zwarty laplasjan']:
    s1,s2=res[name]
    d1,d2=s1-b1, s2-b2
    print(f"{name:26} {d1:11.2f} {d2:12.2f} {d2-d1:10.2f}")
print()
print("Interpretacja: 'roznica' ujemna => harmoniczne traca WIECEJ niz podstawowa")
print("               => przeslanka za zanieczyszczeniem odniesienia, nie tylko gladkim polem")
