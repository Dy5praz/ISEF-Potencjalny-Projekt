import h5py, numpy as np, glob, os, itertools, json
from scipy.signal import butter, filtfilt
from numpy.linalg import lstsq

# katalog z rozpakowanymi S01..S12; nadpisywalny zmienna srodowiskowa EEG_DATA
ROOT = os.environ.get('EEG_DATA', 'un')
FS = 256.0
TARGETS = [7.0, 8.0, 9.0]
AUX_NAMES = ['Cz', 'Fp1', 'HEOG', 'neck', 'cheek', 'jaw']

def load_all():
    recs = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'S*', '*_windows.mat'))):
        with h5py.File(f, 'r') as h:
            tgt = np.array(h['X_tgt_raw'])          # (60,256,3)
            aux = np.array(h['X_aux_raw'])          # (60,256,6)
            cln = np.array(h['X_tgt_cln'])
            f0 = float(np.array(h['meta/f0_Hz']).flatten()[0])
        subj = os.path.basename(os.path.dirname(f))
        recs.append(dict(subj=subj, f0=f0, tgt=tgt, aux=aux, cln=cln, path=f))
    return recs

def clean(tgt, aux, cols):
    """LS regression per 1-s window; cols = indices of aux channels used."""
    if len(cols) == 0:
        return tgt.copy()
    out = np.empty_like(tgt)
    for w in range(tgt.shape[0]):
        A = aux[w][:, cols]
        A = np.column_stack([A, np.ones(A.shape[0])])
        Y = tgt[w]
        beta, *_ = lstsq(A, Y, rcond=None)
        out[w] = Y - A @ beta
    return out

def betas(tgt, aux):
    """mean |beta| per aux channel, averaged over windows and target channels,
    standardised regressors (as in a correlation-scale reading of Table 9)."""
    B = np.zeros((tgt.shape[0], aux.shape[2], tgt.shape[2]))
    for w in range(tgt.shape[0]):
        A = aux[w]
        A = (A - A.mean(0))
        Y = tgt[w] - tgt[w].mean(0)
        Ai = np.column_stack([A, np.ones(A.shape[0])])
        beta, *_ = lstsq(Ai, Y, rcond=None)
        B[w] = beta[:-1]
    return np.abs(B).mean(axis=(0, 2))

# ---------- FBCCA ----------
def make_ref(f0, n_harm, n_samp, fs=FS):
    t = np.arange(n_samp) / fs
    r = []
    for h in range(1, n_harm + 1):
        r.append(np.sin(2 * np.pi * h * f0 * t))
        r.append(np.cos(2 * np.pi * h * f0 * t))
    return np.array(r).T

def cca_corr(X, Y):
    X = X - X.mean(0); Y = Y - Y.mean(0)
    qx, _ = np.linalg.qr(X); qy, _ = np.linalg.qr(Y)
    s = np.linalg.svd(qx.T @ qy, compute_uv=False)
    return float(np.clip(s[0], 0, 1))

SUBBANDS = [(6, 50), (13, 50), (20, 50)]
SBFILT = [butter(4, [lo / (FS / 2), hi / (FS / 2)], btype='band') for lo, hi in SUBBANDS]
W_SB = np.array([(n + 1) ** -1.25 + 0.25 for n in range(len(SUBBANDS))])
NH = 3
REFS = {f: make_ref(f, NH, 256) for f in TARGETS}

def classify(sig, method='fbcca'):
    """sig: (n_win, 256, 3) -> predicted target index per window"""
    nb = len(SUBBANDS) if method == 'fbcca' else 1
    preds = []
    filt = []
    for k in range(nb):
        b, a = SBFILT[k]
        filt.append(filtfilt(b, a, sig, axis=1))
    for w in range(sig.shape[0]):
        scores = []
        for f in TARGETS:
            R = REFS[f]
            s = 0.0
            for k in range(nb):
                s += W_SB[k] * cca_corr(filt[k][w], R) ** 2
            scores.append(s)
        preds.append(int(np.argmax(scores)))
    return np.array(preds)

def run(cols, recs, method='fbcca'):
    per_subj = {}
    for r in recs:
        lab = TARGETS.index(r['f0'])
        sig = clean(r['tgt'], r['aux'], cols)
        p = classify(sig, method)
        per_subj.setdefault(r['subj'], []).append((p == lab).astype(float))
    acc = {s: float(np.concatenate(v).mean() * 100) for s, v in per_subj.items()}
    return acc

if __name__ == '__main__':
    recs = load_all()
    print('records:', len(recs), 'windows total:', sum(r['tgt'].shape[0] for r in recs))

    # --- 1. validate channel order against Table 9 ---
    allb = np.array([betas(r['tgt'], r['aux']) for r in recs])
    print('\n=== mean |beta| per aux channel (my reproduction) ===')
    for i, n in enumerate(AUX_NAMES):
        print(f'  {n:6s} {allb[:, i].mean():.3f}')
    print('  paper Table 9: Cz 0.416  Fp1 0.115  HEOG 0.136  neck 0.097  cheek 0.127  jaw 0.132')

    # --- 2. does my all-aux cleaning match the file's X_tgt_cln? ---
    r = recs[0]
    mine = clean(r['tgt'], r['aux'], list(range(6)))
    err = np.abs(mine - r['cln']).mean() / (np.abs(r['cln']).mean() + 1e-12)
    print(f'\nrel. difference my all-aux clean vs stored X_tgt_cln: {err:.4f}')

    np.save('betas.npy', allb)

def sweep():
    recs = load_all()
    subsets = {
        'O-only (bez kompensacji)': [],
        'wszystkie 6 aux': [0,1,2,3,4,5],
        'Cz sam': [0],
        'bez Cz (Fp1+HEOG+neck+cheek+jaw)': [1,2,3,4,5],
        'tylko mięśniowe (neck+cheek+jaw)': [3,4,5],
        'jaw sam': [5],
        'neck sam': [3],
        'cheek sam': [4],
        'neck+jaw': [3,5],
        'Cz+jaw': [0,5],
        'Cz+cheek': [0,4],
        'Fp1 sam': [1],
        'HEOG sam': [2],
    }
    out = {}
    for name, cols in subsets.items():
        acc = run(cols, recs, 'fbcca')
        vals = np.array([acc[f'S{i:02d}'] for i in range(1,13)])
        out[name] = (vals, vals.mean(), vals.std(ddof=1))
        print(f'{name:36s} {vals.mean():5.1f} +/- {vals.std(ddof=1):4.1f}')
    return out
