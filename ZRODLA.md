# ŹRÓDŁA — bibliografia z oceną wiarygodności

**Zakres wg sekcji 10 handbooka.** Pełna bibliografia etapu 1.

---

## 0. Skala wiarygodności użyta w tym pliku

Sekcja 13 handbooka wymaga oznaczenia, jak pewne jest każde źródło. Skala uwzględniająca ograniczenie tego etapu:

| Stopień | Znaczenie |
|---|---|
| **A** | pozycja istnieje na pewno (tytuł, autorzy, czasopismo i numer z indeksu wyszukiwarki), **treść potwierdzona co najmniej dwoma niezależnymi streszczeniami** |
| **B** | pozycja istnieje na pewno, treść z jednego streszczenia |
| **C** | pozycja istnieje, treści nie ustaliłem — sam namiar do sprawdzenia |
| **D** | źródło niskiej jakości, użyte wyłącznie jako sygnał, że temat istnieje. Nie opierać na tym niczego |
| **X** | **odrzucone** — sprzeczne z lepszym źródłem albo niewiarygodne |

**Zastrzeżenie nadrzędne, obowiązujące dla całego pliku: ani jednej z tych prac nie otworzyłem.** Nawet stopień A oznacza „dwa streszczenia zgodne", a nie „przeczytane". Przy każdej liczbie użytej w plikach 00–08 stoi znacznik `[wniosek, streszczenie]` właśnie z tego powodu.

---

## 1. Ear-EEG — podstawy i przeglądy

| # | Pozycja | Stopień | Do czego użyte |
|---|---|---|---|
| 1 | Looney, Kidmose i in., *The in-the-ear recording concept: user-centered and wearable brain monitoring*, 2012 | B | `01` — początek linii ear-EEG |
| 2 | Kidmose i in., *EEG Recorded from the Ear: Characterizing the Ear-EEG Method*, ~2015, PMC4649040 / PMID 26635514 | B | `01`, `02` |
| 3 | Debener i in., *Unobtrusive ambulatory EEG using a smartphone and flexible printed electrodes around the ear*, **Sci Rep 5:16743 (2015)**, PMID 26572314 | **A** | `01` — cEEGrid, P300 po 7 h, r ≥ 0,74 |
| 4 | Mirkovic, Debener i in., *Identifying auditory attention with ear-EEG: cEEGrid versus high-density cap-EEG*, **J Neural Eng 13:066004 (2016)** | B | `01` |
| 5 | **Kappel i in., *Physiological artifacts in scalp EEG and ear-EEG*, BioMed Eng OnLine 16:103 (2017)**, DOI 10.1186/s12938-017-0391-2 | **A** | **`03`, `04` — artefakty szczękowe gorsze w uchu niż na skalpie. Kluczowa przesłanka projektu** |
| 6 | *Signal quality evaluation of an in-ear EEG device in comparison to a conventional cap system*, **Front Neurosci 18:1441897 (2024)**, PMC11420159 | **A** | `01`, `06` — alfa w ~80% zapisów, SNR 5–6 vs 8 |
| 7 | *The Next Frontier in Brain Monitoring: In-Ear EEG Electrodes and Their Applications*, **MDPI Sensors 25(11):3321 (2025)**, PMID 40968884 | **A** | `04` — lista wyzwań otwartych |
| 8 | ***Signal-specific performance of in-ear EEG: strengths and limitations*, Front Neurosci 20:1859327 (2026)** | **A** | **`03`, `07` — alfa wychodzi, N1-P2 nie. 19 osób vs BioSemi 32-kan.** |
| 9 | *In-ear EEG wearables for brain activity assessment and cognitive rehabilitation*, Front Hum Neurosci art. 1793705 (2026) | B | `04` |
| 10 | *Recent Progress in In-Ear EEG Technology*, MDPI Micromachines 17(7):764, DOI 10.3390/mic17070764 | **C** | do przejrzenia |
| 11 | *Advancing towards Ubiquitous EEG, Correlation of In-Ear EEG with Forehead EEG*, Sensors 22:1568, DOI 10.3390/s22041568 | B | `06` — SNR |
| 12 | *Ear-EEG detects ictal and interictal abnormalities in focal and generalized epilepsy*, Clin Neurophysiol (Elsevier) | C | kontekst kliniczny |
| 13 | *Wireless Ear EEG to Monitor Drowsiness*, arXiv 2401.06076 | C | — |

## 2. Ear-EEG — sterowanie i paradygmaty

| # | Pozycja | Stopień | Do czego |
|---|---|---|---|
| 14 | *A CNN-Based Deep Learning Approach for SSVEP Detection Targeting Binaural Ear-EEG*, **Front Comput Neurosci 16:868642 (2022)**, PMC9160186 | **A** | `06` — 69,2% / 6,4 bit/min @ 63,5% na T7/T8 |
| 15 | *Developing an online SSVEP-based BCI using EarEEG*, EMBC 2015, PMID 26736745 | B | `06` |
| 16 | Ahn i in., *Wearable in-the-ear EEG system for SSVEP-based BCI*, **Electronics Letters 54 (2018)**, DOI 10.1049/el.2017.3970 | B | `01` |
| 17 | *An auditory P300-based brain-computer interface using Ear-EEG*, IEEE 8311519 | B | `06` — 95,6% / 2,97 bit/min |
| 18 | ***ID.EARS: One-Ear EEG Device with Biosignal Noise for Real-Time Gesture Recognition***, An, Oh, Kim, Kim, Park, Oh, **CHI 2025**, DOI 10.1145/3706598.3714185 | **A** | **`00`, `04` — pięć gestów >90%. Zamyka rolę 1 dla sEMG/EOG** |
| 19 | *Detection of motor-related mu rhythm desynchronization by ear EEG*, **PLOS One (2025)** | B | **`03` — koryguje mój argument o korze ruchowej** |
| 20 | *Auditory Attention Decoding from Ear-EEG Signals: A Dataset with Dynamic Attention Switching*, arXiv 2510.19174 | B | `06`, `07` — 41,5% / 30 s, 98 osób |
| 21 | *A Direct Comparison of Simultaneously Recorded Scalp, Around-Ear, and In-Ear EEG for Auditory Attention Decoding*, arXiv 2505.14478 | C | do przejrzenia — **porównanie równoległe trzech geometrii, potencjalnie ważne** |
| 22 | *An auditory selective attention BCI based on auditory steady-state response*, Applied Acoustics (2024) | B | `06` — 64,7–84,3%, 1,89–2,08 bit/min |
| 23 | *Analysis of Prefrontal Single-Channel EEG for Portable Auditory ERP-Based BCIs*, PMC6669913 | B | `06` — jeden kanał, 3 komendy |
| 24 | *Comparison of linear and nonlinear methods for decoding selective attention to speech from ear-EEG*, arXiv 2401.05187 | C | — |

## 3. Historia i BCI inwazyjne

| # | Pozycja | Stopień | Do czego |
|---|---|---|---|
| 25 | Berger, EEG u człowieka, 1924/1929 | **A** (fakt historyczny) | `01` |
| 26 | Vidal, termin „brain–computer interface", 1973 | **A** | `01` |
| 27 | **Gratton, Coles, Donchin, *A new method for off-line removal of ocular artifact*, Electroencephalogr Clin Neurophysiol 55:468–484 (1983)** | **A** | **`04` — pierwowzór kanału referencyjnego. Kluczowe dla oceny nowości** |
| 28 | Hillyard, Galambos (1970) — poprzednik metody regresyjnej | B | `04` |
| 29 | Farwell, Donchin, speller P300, 1988 | **A** | `01`, `07` |
| 30 | **Wolpaw i in., *Brain–computer interfaces for communication and control*, Clin Neurophysiol 113:767–791 (2002)** | **A** | **`06` — wzór na ITR** |
| 31 | Chen i in., *High-speed spelling with a noninvasive BCI*, **PNAS 112 (2015)**, DOI 10.1073/pnas.1508080112 | **A** | `07` — ~60 znaków/min |
| 32 | Hochberg i in., BrainGate, Nature 2006 | **A** | `01` |
| 33 | Normann, Utah array, ~1992–1997 | **A** | `01` |
| 34 | **Willett i in., *A high-performance speech neuroprosthesis*, Nature 620 (2023)**, PMID 36711591, DOI 10.1038/s41586-023-06377-x | **A** | `01`, `07` — 62 wpm, surowy PER 19,7% |
| 35 | Metzger i in., Nature (2023) — ECoG, 78 wpm | **A** | `01`, `06` |
| 36 | **Card i in., *An Accurate and Rapidly Calibrating Speech Neuroprosthesis*, NEJM 391:609 (2024)**, DOI 10.1056/NEJMoa2314132 | **A** | `01` |
| 37 | *Brain-to-Text Benchmark '24: Lessons Learned*, arXiv 2412.17227 | B | `07` — 9,7% → 5,8% WER |
| 38 | *Brain implants that enable speech pass performance milestones*, Nature (news) d41586-023-02546-0 | B | kontekst |

## 4. Tor analogowy, elektrody, materiały

| # | Pozycja | Stopień | Do czego |
|---|---|---|---|
| 39 | **ADS1299, karta katalogowa Texas Instruments** — 1,0 µV p-p @ 70 Hz, CMRR −120 dB | **A** | **`02`, `06` — najpewniejsza liczba w całym etapie, trzy niezależne opisy** |
| 40 | *An 8-Channel Ambulatory EEG Recording IC with In-Channel Fully-Analog Real-Time Motion Artifact Extraction and Removal*, ~2023 | B | **`04` — stan techniki dla kompensacji analogowej** |
| 41 | *A Novel Battery-Supplied AFE EEG Circuit Capable of Muscle Movement Artifact Suppression*, MDPI Appl Sci 14:6886, DOI 10.3390/app14166886 | B | `04` |
| 42 | US 5513649 — *Adaptive interference canceler for EEG movement and eye artifacts* | B | `04` — patent |
| 43 | *EOG Artifact Removal from Single and Multi-channel EEG*, arXiv 2308.13371 | C | `04` |
| 44 | *Development of Low-Contact-Impedance Dry Electrodes for EEG*, PMC10181682 | B | `02`, `06` |
| 45 | *Dry Electrodes for Human Bioelectrical Signal Monitoring*, PMC7374322 | B | `02` |
| 46 | *Hydrogel electrodes with conductive and substrate-adhesive layers*, Microsyst Nanoeng, DOI 10.1038/s41378-023-00524-0 | C | materiały |
| 47 | *Fully organic compliant dry electrodes self-adhesive to skin*, Nat Commun, PMID 32943621 | C | materiały |
| 48 | BrainAccess, *Dry-contact EEG electrodes: materials, trade-offs* | **D** | materiał producenta — orientacyjnie |
| 49 | *Biocompatible 3D printing resins for medical applications*, ScienceDirect S2666964121000394 | B | `05` |
| 50 | EnvisionTEC/ETEC E-Shell 300/600/3000 — materiały producenta | **D** | `05` — deklaracja producenta, nie źródło niezależne |
| 51 | ISO 10993-5, ISO 10993-10 | **A** (norma) | `05` |

## 5. Dekodowanie

| # | Pozycja | Stopień | Do czego |
|---|---|---|---|
| 52 | ***Benchmarking BCI algorithms: Riemannian approaches vs convolutional neural networks*, J Neural Eng (2024), DOI 10.1088/1741-2552/ad6793** | **A** | **`07` — riemannowskie ≥ CNN, do 2 rzędów szybsze** |
| 53 | *TFTL: A Task-Free Transfer Learning Strategy*, PMID 39365711 | B | `07` — zero prób kalibracyjnych |
| 54 | *Minimizing subject-dependent calibration for BCI with Riemannian transfer learning*, arXiv 2111.12071 | B | `07` |
| 55 | Vidaurre, Blankertz, *Towards a Cure for BCI Illiteracy*, Brain Topogr | **A** | `03` — 15–30% |
| 56 | *A large scale screening study with an SMR-based BCI*, PLOS One, DOI 10.1371/journal.pone.0207351 | B | `03` |
| 57 | MOABB — Mother of All BCI Benchmarks | B | `07` |
| 58 | BCI Competition IV 2a | **A** | `07` |
| 59 | PhysioNet MI/ME, 109 osób | **A** | `07` |
| 60 | *Ear-EEG sleep monitoring data sets*, **Sci Data (19 II 2025)**, DOI 10.1038/s41597-025-04579-8, PMC11840015 | **A** | `07` — 320 zapisów, 30 osób |
| 61 | *EEGDash*, arXiv 2606.16041 — 791 zbiorów | B | `07` |
| 62 | *An open-access EEG dataset for speech decoding*, Sci Data, s41597-025-05187-2 | C | `07` |

## 6. Shared control

| # | Pozycja | Stopień | Do czego |
|---|---|---|---|
| 63 | *Brain–computer interface control with artificial intelligence copilots*, **Nat Mach Intell (2025)**, s42256-025-01090-y | **A** | `04` |
| 64 | *A brain-actuated robotic arm system using non-invasive hybrid BCI and shared control*, **J Neural Eng (2021)**, DOI 10.1088/1741-2552/abf8cb, PMID 33862607 | **A** | `04` |
| 65 | *Shared control of a robotic arm using non-invasive BCI and computer vision guidance*, Robot Auton Syst | B | `04` |
| 66 | *Continuous shared control of a mobile robot with BCI*, Comput Struct Biotechnol J (2023), PMC10433001 | B | `04` |
| 67 | *Blending of BMI and vision-guided autonomous robotics*, PMC4797113 | B | `04` |
| 68 | *Semi-Autonomous Robotic Arm Reaching With Hybrid Gaze–Brain Machine Interface*, PMC6992643 | C | `04` |

## 7. Inne modalności

| # | Pozycja | Stopień | Do czego |
|---|---|---|---|
| 69 | *OPM-MEG: the next generation of functional neuroimaging*, Trends Neurosci (2022), S0166-2236(22)00102-3 | **A** | `01`, `02` |
| 70 | *Facilitating cognitive neuroscience research with 80-sensor OPM-MEG*, NeuroImage (2025) | B | `01` |
| 71 | *Towards a 384-channel MEG system based on OPMs*, arXiv 2509.03107 | C | `01` |
| 72 | *Applications of OPM-MEG for translational neuroscience*, Transl Psychiatry, s41398-024-03047-y | C | `01` |
| 73 | AlterEgo — MIT Media Lab, praca dyplomowa o ciągłym rozpoznawaniu mowy cichej (dspace.mit.edu) | B | `01` |
| 74 | *Knowledge Distilled Ensemble Model for sEMG-based Silent Speech Interface*, arXiv 2308.06533 | C | `01` |
| 75 | *Minimally Invasive BCIs: Evaluating the Impact of Tissue Layers on Signal Quality of Sub-Scalp EEG*, arXiv 2506.03452 | B | `02`, `03` |

## 8. Konkursy i regulaminy

| # | Pozycja | Stopień | Uwaga |
|---|---|---|---|
| 76 | isef.explory.pl — reprezentacja Polski na ISEF | B | **`08` sekcja 1 — podstawa zamknięcia K-007** |
| 77 | ORLEN, informacja o reprezentacji na ISEF 2026 | B | potwierdzenie krzyżowe składu |
| 78 | ppnt.pl, lit.lukasiewicz.gov.pl — zwycięzcy Explory 2025 | B | potwierdzenie krzyżowe |
| 79 | polfinal.explory.pl, final.explory.pl, gew.explory.pl, konkurs.explory.pl | **C** | **strony organizatora — do otwarcia w pierwszej kolejności** |
| 80 | **Regulamin Konkursu Explory** | **C** | **niedostępny. Najwyższy w hierarchii sekcji 13** |
| 81 | societyforscience.org — International Rules, Human Participants, formularze | **C** | **niedostępne. Patrz `ISEF_HUMAN_PARTICIPANTS.md`** |
| 82 | isef.net — baza projektów; abstracts.societyforscience.org | **C** | **niedostępne. Blokuje zadanie 4d nr 10** |
| 83 | isef.net, strona projektu **ENBM074 = „Synthetic DNA Engineering With ICOR"** | **A** (tytuł strony z indeksu) | **`08` sekcja 2 — podstawa korekty K-012** |
| 84 | pb.edu.pl, we.pb.edu.pl, wm.pb.edu.pl — El-Robo-Mech XI (2025/2026) | **A** | `08` sekcja 4 — terminy, 34 laureatów |
| 85 | Society for Science, komunikaty prasowe ISEF 2025 i 2026 (pełne listy nagród) | **C** | do otwarcia — **zawierają listy nagrodzonych, przydatne do zadania 11** |

## 9. Źródła odrzucone

| Pozycja | Powód |
|---|---|
| **biohackeratlas.com — Emotiv EPOC X „99 USD"** | **X** — sprzeczne ze stroną producenta (999 USD). Witryna afiliacyjna. Patrz `05` sekcja 4 |
| „rynek BCI wart 400 mld USD" (blogi branżowe) | **X** — brak metodologii, najniższa pozycja w hierarchii |
| neuroba.com, 3zebras.com, axis-intelligence.com, pdpspectra.com, teahose.com i pokrewne zestawienia „BCI 2026" | **D/X** — treść wtórna, prawdopodobnie generowana. Użyte wyłącznie jako sygnał, że dana firma istnieje; **żadna liczba stąd nie weszła do plików bez potwierdzenia** |
| neurosity.co (poradniki) | **D** | materiał producenta, orientacyjnie |
| LinkedIn i Facebook, profile o nazwisku zbieżnym z autorstwem projektu referencyjnego | **X** — brak związku z projektem, patrz K-008 i `08` sekcja 2 |

---

## 10. Bilans

| Stopień | Liczba pozycji |
|---|---|
| A — treść potwierdzona dwoma streszczeniami | **26** |
| B — jedno streszczenie | 32 |
| C — sam namiar, treści nie ustalono | 20 |
| D — niska jakość, tylko sygnał | 4 |
| X — odrzucone | 5 |

**[fakt] Pozycji przeczytanych w oryginale: 0.** To jest liczba, która opisuje ten etap najuczciwiej i dlatego stoi na końcu bibliografii, a nie w przypisie.
