# analiza — kod reanalizy danych Kołodziej i in. 2026

Kod, który wyprodukował liczby w `../14_REANALIZA.md`. Zwalidowany wobec publikacji:
odtwarza Tabelę 9 pracy co do trzeciego miejsca po przecinku, a czyszczenie regresją
zgadza się z gotowym `X_tgt_cln` autorów co do zera.

## Uruchomienie

```bash
git clone https://github.com/kolodzima/EEG_artefact_SSVEP_EMG_EOG.git ds
for i in $(seq -w 1 12); do unzip -q ds/S$i.zip -d un; done
pip install numpy scipy scikit-learn h5py
```

Ustawić `ROOT` w `analiza.py` na katalog `un`, potem:

| Skrypt | Co liczy |
|---|---|
| `analiza.py` | walidacja wobec Tabeli 9; FBCCA; funkcja `sweep()` — ablacja kanałów pomocniczych |
| `svm_test.py` | SVM liniowy na cechach FFT, leave-one-subject-out — pipeline autorów |
| `spatial.py` | montaże przestrzenne: CAR, dwubiegunowy, laplasjan, wobec regresji Cz |
| `rozstaw.py` | pochodne o różnym rozstawie elektrod |
| `hipoteza.py` | czy kanały pomocnicze pomagają w montażu różnicowym (nie pomagają) |

## Licencja danych

Zbiór: CC-BY, https://github.com/kolodzima/EEG_artefact_SSVEP_EMG_EOG
Artykuł: Kołodziej M., Majkowski A., Wiszniewski P., *Sensors* 26(3):917, 2026,
PMID 41682433, PMC12899023. **Przy każdym użyciu cytować pracę źródłową.**
