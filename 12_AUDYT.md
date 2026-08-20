# 12 — Audyt całkowity etapu 1

**Data:** 15 sierpnia 2026, po zamknięciu etapu 1
**Zlecenie użytkownika:** *„całkowita weryfikacja etapu 1 (…) chcę mieć absolutną pewność, że to co robimy nie zostało już zrobione i faktycznie nasza teza o innowacyjności nie upadnie (…) sprawdź czy nasze założenia i oczekiwania są realne, aby nie padło to jak z dronem."*

> **UZUPEŁNIENIE METODY, 21 VIII 2026.** Do wzorca audytu dochodzi **procedura sprawdzania tożsamości projektu** — `37_PROCEDURA_TOZSAMOSCI_I_ROZBIORY.md` §3. Powód: dwa razy ogłosiłem twierdzenie za martwe na podstawie **zbieżności tematu**, nie zbieżności eksperymentu (K-089, K-092). **Zanim cokolwiek zostanie nazwane zajętym, siedem pytań z pełnego tekstu i werdykt jednym z trzech słów: tożsamy, sąsiedni, niezwiązany.** Wszystkie pięć prac, które w tym projekcie zabiły jakąś oś, po zastosowaniu procedury okazały się **sąsiednie** — `37` część II.

**Metoda: audyt adwersaryjny.** Próbowałem ten projekt zabić, nie obronić. Każde twierdzenie traktowałem jako hipotezę do obalenia, a nie do potwierdzenia.

**Wynik w jednym zdaniu: trzy z czterech kandydujących twierdzeń projektu są martwe, czwarte żyje i jest opisane w literaturze jako luka — ale ma nazwanego konkurenta z terminem.**

---

## 1. Co zabiłem

### 1.1 „Tani interfejs SSVEP o wysokiej przepustowości" — MARTWE

`[fakt, abstrakt odczytany]` **Teversham, Wong, Hsieh, Rapeaux, Troiani, Savolainen, Zhang, Maslik, Constandinou — Imperial College London, EMBC 2022, PMID 36086083.**

> „a novel, approx. **£20** electroencephalogram (EEG)-based brain-computer interface (…) All BCI functionality is executed on board an inexpensive **ESP32** microcontroller. SSVEP decoding accuracy of **95.56 ± 3.74%** with an **ITR of 102 bits/min** was achieved with modest calibration."

**Dwadzieścia funtów. Sto dwa bity na minutę. Na ESP32.** To jest **więcej** niż 92,35 bit/min z pracy Xing 2018, którą ustawiłem jako punkt odniesienia, i za ułamek kosztu.

Do tego kontekst, którego nie miałem:
- **Arpaia i in., *J Vis Expl* 2023, PMID 37486136** — pojedynczy kanał różnicowy, elektrody suche, okulary XR, **20 badanych, 80–95% dokładności**
- **Yang, Nguyen, Chung 2020, PMID 32987871** — **38 komend, 96,92%, jeden kanał bipolarny**
- **HardwareX 2024** — „Low-cost, mobile EEG hardware for SSVEP applications", otwarty sprzęt
- **arXiv 2601.01772 (2026)** — „Design and Quantitative Evaluation of an Embedded EEG Instrumentation Platform for Real-Time SSVEP Decoding"

**Konsekwencja:** twierdzenie „zbudowałem tani interfejs SSVEP osiągający wysokie ITR" **nie ma żadnej wartości nowościowej**. Jest zrobione, wielokrotnie, taniej i lepiej, przez zespoły uczelniane publikujące otwarty sprzęt.

**To jest jednocześnie najlepsza wiadomość o realności w całym audycie** — patrz sekcja 3.

### 1.2 „Mały suchy czujnik przez włosy na potylicy" — MARTWE, i to na najwyższym poziomie

`[fakt, abstrakt odczytany]` **Kim H., Kim J.H., Lee Y.J. i in. (Georgia Institute of Technology, Yonsei, Hanyang), *PNAS* 122(15):e2419304122, 15 IV 2025, PMID 40193612.**

> „**motion artifact-controlled micro-brain sensors between hair strands** (…) An array of low-profile microstructured electrodes with a highly conductive polymer is **seamlessly inserted into the space between hair follicles**, offering high-fidelity neural signal capture for **up to 12 h** while maintaining the **lowest contact impedance density (0,03 kΩ·cm⁻²) among reported articles**. Implemented wireless BCI, detecting steady-state visually evoked potentials, offers **96,4% accuracy** in signal classification with a **train-free algorithm even during the subject's excessive motions, including standing, walking, and running**."

Do tego: demonstracja rozmowy wideo w AR sterowanej bez rąk, oraz **zgłoszenie patentowe w toku** (deklaracja konfliktu interesów: „Hodam Kim and W.-H.Y. are inventors on a **pending patent application** related to this work at Georgia Tech").

**To jest dokładnie ten problem, który zapisałem jako „elektroda sucha przez włosy plus mocowanie odporne na ruch", rozwiązany przez Georgia Tech, opublikowany w PNAS, opatentowywany.**

Dodatkowo w tej samej niszy: **MXene-Based Microneedle Electrode for Brain-Computer Interface** (*ACS Appl Mater Interfaces* 2025, PMID 40455568) oraz silikonowa elastyczna elektroda sucha (*Biomed Eng Lett* 2025, PMID 40271395).

**Konsekwencja:** twierdzenie o konstrukcji elektrody suchej jako wkładzie projektu **jest niedostępne**. Elektrodę trzeba zrobić dobrze, ale nie wolno jej sprzedawać jako wynalazku.

### 1.3 „Kanał pomocniczy do usuwania artefaktów mięśniowych z potylicznego SSVEP" — ZROBIONE OSIEM MIESIĘCY TEMU, W POLSCE

To jest najważniejsze znalezisko audytu i najbliżej trafia w oś projektu.

`[fakt, pełny tekst odczytany]` **Kołodziej M., Majkowski A., Wiszniewski P. — Wydział Elektryczny, Politechnika Warszawska. *Sensors* 26(3):917, 31 I 2026, PMID 41682433, PMC12899023.**

*„Improved SSVEP Classification Through EEG Artifact Reduction Using Auxiliary Sensors"*

| Element | Co zrobili |
|---|---|
| elektrody czynne | **O1, O2, Oz** — nasze umiejscowienie |
| kanały pomocnicze | Cz, Fp1, HEOG, oraz **mięśniowe: kark, policzek, szczęka** |
| bodziec | **diody LED**, 7, 8 i 9 Hz |
| metoda | **regresja liniowa w oknach 1-sekundowych**, potem SVM i CNN |
| badani | **12 osób** |
| wynik | SVM: 70,8 ± 20% → **79,9 ± 17,3%** (+9,1 ± 6,4 pp); CNN: 70,7 ± 21,1% → **79,7 ± 18,5%** (+9,9 ± 8,2 pp) |
| **które kanały pomocnicze działały najlepiej** | **Cz i szczęka** |
| rozrzut indywidualny | od **−1,0 pp** (S7, brak korzyści) do **+22,4 pp** (S11) |

**Czyli: pomysł „zmierz artefakt szczękowy osobną elektrodą i odejmij go od sygnału potylicznego" jest opublikowany, zmierzony na 12 osobach i skwantyfikowany.** Zysk to około 9 punktów procentowych dokładności.

**Dwie rzeczy, które to zmienia natychmiast:**

1. **Rozwiązuje sprzeczność, którą wszedłem sprawdzić.** `09_UMIEJSCOWIENIE.md` sekcja 4 mówiła wprost, że oś i miejsce są sprzężone i że przy potylicy oś trzeba wyprowadzić od nowa, bo „problem szczęki tam nie dominuje". Wybraliśmy potylicę i **przeniosłem oś mechanicznie, wbrew własnemu zapisowi**. Kołodziej pokazuje, że przeniesienie było przypadkowo trafne: **przy elektrodach potylicznych kanał szczękowy jest jednym z dwóch najskuteczniejszych kanałów pomocniczych.** Oś przeżywa — ale przeżywa dzięki cudzej pracy, nie dzięki mojemu rozumowaniu.
2. **Odbiera twierdzenie o pierwszeństwie w wersji ogólnej, definitywnie.** Nie „nie znalazłem, więc może nikt nie zrobił" tylko „zrobiono, oto liczby".

---

## 2. Co przeżyło — i dlaczego to jest mocniejsza pozycja niż przed audytem

### 2.1 Luka, którą autorzy sami wypisali

Sekcja 10.D handbooka mówi: **luki są opisane, nie trzeba ich zgadywać.** Ta jest opisana, dosłownie, przez ludzi, którzy zrobili wersję cyfrową.

`[fakt, cytat z sekcji przyszłych prac Kołodziej i in. 2026]`

> „identification of a minimal electrode set (Cz and selected EMG/EOG channels) provides a foundation for designing **low-channel, wearable SSVEP–BCI systems in which artifact reduction is addressed already at the signal acquisition stage**."

**To zdanie opisuje projekt użytkownika.** Nisko-kanałowy, noszalny system SSVEP-BCI, w którym redukcja artefaktów odbywa się **już na etapie akwizycji sygnału** — czyli w torze analogowym, przed przetwornikiem.

Autorzy podają też, dlaczego to ma sens, i jest to gotowe uzasadnienie do wykorzystania:

> „Existing EEG artifact reduction methods—such as ICA, PCA-based techniques, adaptive filtering, and deep learning approaches—can be effective but often require **high computational cost, extensive parameter tuning, or manual component selection, limiting their suitability for real-time and mobile BCI systems**."

**Sprawdziłem, czy ktoś to zrobił.** Zapytanie `EEG AND ("analog front-end" OR AFE OR "readout IC") AND ("artifact cancellation" OR "artifact suppression" OR "interference cancellation") AND (EMG OR muscle OR motion)` w PubMed: **zero trafień**. Najbliższe istniejące prace to Dabbaghian 2019 (analogowa kompensacja artefaktów **ruchowych**, opaska) i Kim 2026 (kompensacja **offsetu** w module zausznym) — obie robią coś innego.

### 2.2 Twierdzenie w kształcie, który przeżywa audyt

> **Kompensacja artefaktu szczękowego w torze analogowym, przed przetwornikiem, w zwartym module potylicznym — mierzona względem tego samego układu bez kompensacji, na tle wyniku cyfrowego Kołodziej i in. (+9 pp).**

Dlaczego ten kształt jest odporny:

- **nie jest twierdzeniem o pierwszeństwie**, więc nie upada od znalezienia cudzej pracy
- **ma zewnętrzny punkt odniesienia z liczbą** — +9 pp z regresji cyfrowej. Jeżeli wersja analogowa da więcej, jest wynik; jeżeli tyle samo przy niższym koszcie obliczeniowym, też jest wynik; jeżeli mniej, **to też jest wynik** i uczciwie raportowalny
- **ma uzasadnienie mechanistyczne, którego cyfrowa wersja nie ma**: artefakt usunięty przed wzmocnieniem nie zjada zakresu dynamicznego. Regresja po przetworniku nie odzyska sygnału, który został obcięty przy nasyceniu
- **jest tanie do sprawdzenia** — ten sam układ, dwa warianty, jedna kampania

### 2.3 Drugie pytanie, które audyt zostawił otwarte i które jest nasze

`[fakt]` Zapytania o zwarte, gęsto upakowane tablice potyliczne: **zero trafień** w PubMed (`EEG AND "electrode array" AND (miniature OR compact OR "closely spaced") AND (Laplacian OR bipolar) AND (SSVEP OR visual)` oraz `EEG AND ("hair clip" OR barrette OR "miniaturized patch") AND (scalp OR occipital OR wearable)`).

Xing 2018 używał elektrod w pozycjach **PO5, PO3, POz, PO4, PO6, O1, Oz, O2** — czyli rozstawu szerokiego, rzędu 10 cm. **Nikt nie sprawdził, czy gęste próbkowanie małego obszaru zastępuje rzadkie próbkowanie dużego** dla potylicznego SSVEP.

To jest pytanie, na które odpowiedź jest **tabelą z Twojego układu**, i które jest bezpośrednio o to, co czyni urządzenie noszalnym.

---

## 3. Realność — werdykt odwrotny do obaw

Pytanie użytkownika: czy założenia są realne, żeby nie padło jak z dronem.

**Cel przepustowościowy jest realny i to jest ustalone twardo, a nie oszacowane.**

| Kto | Sprzęt | Wynik |
|---|---|---|
| Imperial College 2022 | **~£20, ESP32** | 95,56%, **102 bit/min** |
| Xing 2018 (CAS) | 8 elektrod suchych | 93,2%, 92,35 bit/min |
| inne prace z elektrodami suchymi | 8 kanałów | 70,6 bit/min; 117,05 bit/min (speller 60-znakowy) |
| Arpaia 2023 | **jeden kanał** | 80–95%, 20 badanych |
| Kołodziej 2026 (PW) | O1/O2/Oz + pomocnicze | **70,7% bazowo**, 3 cele |

**Rozstrzygnięcie: 90–100 bit/min nie wymaga instytutu.** Wymaga poprawnej implementacji filter-bank CCA albo TRCA i przyzwoitego kontaktu elektrod. Ryzyko techniczne projektu jest **niższe**, niż zakładałem w `11_OCENA_SZANS.md`.

**Ale uwaga na kalibrację oczekiwań w drugą stronę:** Kołodziej i in., zespół uczelniany z Politechniki Warszawskiej, uzyskali **70,7% przy trzech celach**. Xing przy dwunastu celach uzyskał 93,2%. Różnica leży w elektrodach, torze i algorytmie. **Nie zakładaj, że pierwsze uruchomienie da wynik z górnej półki** — dolna półka w recenzowanej literaturze to 70% przy trzech celach.

### 3.1 Czym to się różni od drona

| | Dron / orteza / STM | Ten projekt |
|---|---|---|
| kiedy sprawdzono prior art | **po** zbudowaniu strategii | **przed** |
| co zostało z twierdzenia | „przy koszcie konsumenckim" — nie jest twierdzeniem naukowym | pomiar z zewnętrznym punktem odniesienia i liczbą |
| czy wykonalność była pytaniem | tak, i to otwartym | **nie — £20 device robi 102 bit/min** |
| tryb śmierci | cudza publikacja unieważnia twierdzenie | **nie unieważnia, bo twierdzenie jest o pomiarze własnego układu** |

---

## 4. Ryzyka, które audyt ujawnił i których wcześniej nie było na liście

### 4.1 Nazwany konkurent z terminem — ryzyko najwyższe

**Grupa z Politechniki Warszawskiej napisała w styczniu 2026, że następnym krokiem jest redukcja artefaktów na etapie akwizycji w noszalnym systemie nisko-kanałowym.** To jest zespół z Wydziału Elektrycznego, czyli mający kompetencje, żeby to zrobić, i motywację, bo sami to wskazali.

`[wniosek]` **Najbardziej prawdopodobnym scenariuszem utraty pierwszeństwa jest publikacja tej samej grupy w latach 2026–2027.** To nie jest abstrakcyjne ryzyko — to jest nazwany aktor z nazwiskami i afiliacją.

**Dlaczego to nie zabija projektu:** twierdzenie pomiarowe przeżywa. Jeżeli opublikują pierwsi, nasz projekt staje się **niezależnym potwierdzeniem na własnym sprzęcie**, co jest nadal poprawnym projektem ISEF — sekcja Execution arkusza inżynierskiego punktuje wykonanie i testowanie, nie pierwszeństwo. Degradacja jest z „nowe" na „potwierdzone niezależnie", nie z „projekt" na „nic".

**Co z tym robić operacyjnie:** sprawdzać tę grupę okresowo (PubMed, autorzy: Kołodziej M., Majkowski A.) i **nie budować żadnego zdania w materiałach zgłoszeniowych na słowie „pierwszy"**.

### 4.2 Problem Cz — konflikt między najlepszym rozwiązaniem a formą

`[fakt]` Kołodziej i in. ustalili, że **najskuteczniejsze kanały pomocnicze to Cz i szczęka.**

**Cz to wierzchołek głowy.** Nasze ograniczenie gabarytowe — moduł zwarty na potylicy, żadnej konstrukcji nad czubkiem głowy — **wyklucza dostęp do Cz**.

Trzy wyjścia i żadne nie jest darmowe:
1. zrezygnować z Cz i przyjąć mniejszy zysk — **ile mniejszy, nie wiadomo**
2. znaleźć zamiennik bliżej potylicy pełniący tę samą rolę (Cz prawdopodobnie łapie składową wspólną, nie mięśniową) — do sprawdzenia
3. **zmierzyć, ile korzyści przeżywa bez Cz** — i to jest odpowiedź w duchu całej reszty projektu

`[wniosek]` Wariant 3 jest nie tylko wyjściem awaryjnym, ale **osobnym, publikowalnym pytaniem**: „ile z redukcji artefaktów da się uzyskać przy ograniczeniu do elektrod mieszczących się w module noszonym". To jest pytanie o wykonalność formy, czyli dokładnie to, o co użytkownikowi chodzi od początku.

### 4.3 Ryzyko, że artefakt szczękowy na potylicy jest za mały, żeby było co kompensować

`[fakt]` Willis, Nelson, Rice, Black, *Clin Electroencephalogr* 24(3):123–126 (1993), PMID 8403444: **„Muscle artifact contaminates anterior electrode sites more than posterior sites, making the posterior scalp electrodes superior for studying beta activity."** Elektrody tylne stabilne do 24 Hz; powyżej 24 Hz skażone wszędzie.

Czyli: potylica jest **relatywnie odporna** na artefakt mięśniowy w porównaniu z czołem. To osłabia przesłankę „artefakt szczękowy to główny problem" — która była wyprowadzona dla ucha (Kappel 2017), a nie dla potylicy.

**Przeciwwaga:** Kołodziej mierzył właśnie na O1/O2/Oz i uzyskał +9 pp z kompensacją, w tym z kanału szczękowego. Czyli mimo relatywnej odporności **jest co kompensować**. Do tego pasmo: SSVEP używa harmonicznych powyżej 24 Hz, a tam wg pracy z 1993 skażenie jest wszędzie.

`[luka]` **Czego nie wiem:** jaki jest udział szczęki wobec karku w artefakcie potylicznym. Kołodziej mierzył oba (kark i szczęka jako osobne kanały) i podał, że szczęka była skuteczniejsza — ale nie odczytałem rozbicia. **To jest pierwsza rzecz do wyciągnięcia z pełnego tekstu w etapie 2.**

---

## 5. Co zweryfikowałem i przeżyło bez zmian

| Ustalenie | Status po audycie |
|---|---|
| kalendarz Explory → ISEF 2028 | **potwierdzone cytatem z regulaminu**, §8 pkt 7c |
| **reguła 12 miesięcy** | **wzmocnione: sprawdzone na TRZECH rocznikach.** ISEF 2024: „before January 2023", okno I 2023 – V 2024. ISEF 2025: „before January 2024", okno I 2024 – V 2025. ISEF 2027: „before January 2026", okno I 2026 – V 2027. **Wzorzec stabilny, ekstrapolacja na I 2027 – V 2028 przestaje być ekstrapolacją** |
| formalności ISEF, zwolnienie dla badania na sobie | bez zmian |
| konkurencja neuro na Explory (1 na 133) | bez zmian |
| konkurencja EEG na ISEF (22 w 2026) | bez zmian |
| referencja laplasjanowa optymalna dla SSVEP | bez zmian, trzy źródła |
| licencje zbiorów danych CC-BY | bez zmian |

---

## 6. Werdykt

**Teza o innowacyjności w wersji, w jakiej istniała przed audytem, nie przeżyła.** „Tani interfejs", „elektroda sucha przez włosy", „kanał pomocniczy do usuwania artefaktów" — wszystkie trzy są zajęte, w tym jeden przez PNAS z patentem i jeden przez zespół z Warszawy sprzed ośmiu miesięcy.

**Przeżyła jedna rzecz, i jest lepiej udokumentowana niż cokolwiek wcześniej w tym projekcie:** redukcja artefaktu **na etapie akwizycji**, w torze analogowym, w module nisko-kanałowym — wskazana jako następny krok przez autorów wersji cyfrowej, w recenzowanej pracy, z podanym uzasadnieniem, dlaczego wersja cyfrowa nie wystarcza dla systemów mobilnych.

**To jest mocniejsza pozycja niż przed audytem**, mimo że zostało mniej. Wcześniej mieliśmy cztery twierdzenia, z których żadne nie było sprawdzone do końca. Teraz mamy jedno, sprawdzone, z zewnętrznym punktem odniesienia (+9 pp), z nazwanym konkurentem i z planem awaryjnym na wypadek, gdyby ten konkurent opublikował pierwszy.

**Odpowiedź na pytanie „czy padnie jak z dronem": nie w ten sam sposób.** Dron padł, bo prior art znaleziono po zbudowaniu strategii, a z twierdzenia został slogan bez treści naukowej. Tutaj prior art znaleziono przed, zabił trzy czwarte pomysłu, a to, co zostało, jest twierdzeniem pomiarowym — czyli takim, którego cudza publikacja nie unieważnia.

**Czego ten audyt nie może zagwarantować:** że nikt nie opublikuje wersji analogowej w ciągu najbliższych osiemnastu miesięcy. Przy nazwanym konkurencie z Politechniki Warszawskiej to jest ryzyko realne i policzalne raczej na dziesiątki procent niż na jednostki. **Dlatego twierdzenie projektu nie może zawierać słowa „pierwszy" w żadnym materiale zgłoszeniowym** — i dlatego dobrze, że już go nie zawiera.

---

# CZĘŚĆ II — drugie przejście, 15 VIII 2026

**Zlecenie:** *„wykonaj jeszcze raz sprawdzenie (…) wolę mieć 100% pewności"*.

**Metoda:** kanały, których w pierwszym przejściu nie użyłem — **arXiv przez API, baza patentów, inna terminologia** (adaptive noise cancellation, active electrode, common mode, biopotential), oraz **sprawdzenie dorobku samej grupy konkurencyjnej**.

---

## 7. Patenty — sprawdzone, wypadają na naszą korzyść

### 7.1 US 5513649 A — *Adaptive interference canceler for EEG movement and eye artifacts*

Sam Technology Inc., 1996. Był w `ZRODLA.md` od pierwszej sesji, ale **nigdy nie sprawdziłem, co właściwie zastrzega.** Teraz sprawdzone:

| Cecha | Treść |
|---|---|
| kompensacja | **cyfrowa** — „a conventional general purpose digital computer or a DSP processor" |
| sygnał referencyjny | akcelerometry, detektory ruchu, **średnia przestrzenna kanałów EEG**, kanały EOG |
| uzasadnienie średniej przestrzennej | „head movement artifacts have an approximately uniform distribution over the head" |
| **status** | **WYGASŁY** — „Anticipated expiration" 22 III 2014 |

**Wniosek:** dotyczy artefaktów **ruchowych i ocznych**, nie mięśniowych; referencją jest średnia przestrzenna albo czujnik ruchu, **nie dedykowana elektroda mięśniowa**; jest **cyfrowy**; i **wygasł dwanaście lat temu**. Nie koliduje.

### 7.2 US 11241183 B2 — *EEG headsets with precise and consistent electrode positioning*

**Neurolutions Inc., przyznany 8 II 2022, żywy.** To jest firma stojąca za IpsiHand, interfejsem BCI dopuszczonym przez FDA do rehabilitacji poudarowej.

Zastrzega układ **jednej elektrody centralnej i co najmniej trzech obwodowych**, w którym elektrody obwodowe służą do wyznaczenia **szumu wspólnego (common mode noise)** odejmowanego od sygnału elektrody centralnej, przy czym uśrednianie i odejmowanie może wykonywać sam zestaw.

**To jest sprzętowy laplasjan — czyli architektura elektrod, którą wybraliśmy.**

**Dlaczego to nie zabija projektu, w trzech punktach:**
1. **Patent nie jest przeszkodą konkursową.** Regulamin ISEF wymaga poszanowania własności intelektualnej w sensie cytowania i nieużywania cudzych nieopublikowanych danych; nie zakazuje budowania urządzeń wykorzystujących opatentowane architektury do badań własnych. Projekt szkolny nie jest wdrożeniem komercyjnym.
2. **Zastrzeżenie dotyczy szumu wspólnego z elektrod obwodowych**, a nasza oś to **dedykowana elektroda nad mięśniem** i odejmowanie **konkretnego artefaktu biologicznego przed wzmocnieniem**. To są różne rzeczy.
3. **Potwierdza to, co i tak zapisaliśmy w K-043:** układ elektrod nie może być sprzedawany jako wynalazek projektu. Teraz wiadomo, dlaczego — bo jest opatentowany przez firmę medyczną.

`[luka]` Nie czytałem pełnego tekstu zastrzeżeń i interpretacja zastrzeżeń patentowych to zadanie dla prawnika, nie dla mnie. **Dla celów konkursowych to nie ma znaczenia; zapisuję jako niedokończone, żeby nie udawać pewności, której nie mam.**

---

## 8. arXiv — jedno trafienie bardzo blisko, i jest instrukcją, nie zagrożeniem

`[fakt]` **„Design and Quantitative Evaluation of an Embedded EEG Instrumentation Platform for Real-Time SSVEP Decoding", arXiv 2601.01772, 5 I 2026.**

Platforma: **ESP32-S3 plus ADS1299** — dokładnie te komponenty, które rekomendowałem. Osiem kanałów, filtracja zerofazowa i analiza korelacji kanonicznej **w całości na urządzeniu**, łączność bezprzewodowa, praca w pętli zamkniętej bez komputera.

Zmierzone parametry:

| Parametr | Wartość |
|---|---|
| **szum przy zwartym wejściu** | **≈0,08 µV RMS** |
| jitter próbkowania | 0,56 µs (odch. std.) |
| dryf długoterminowy | < 1 ppm |
| tłumienie sygnału wspólnego | **>112 dB**, spadek o 26,9 dB przy niedopasowaniu impedancji źródła |
| dokładność online | **99,17%** |
| **ITR** | **27,66 bit/min** |

**Dlaczego to jest dobra wiadomość, a nie zła:**

1. **Potwierdza wybór komponentów.** ESP32 + ADS1299 to nie zgadywanka — jest scharakteryzowana, opublikowana platforma o tej architekturze.
2. **Daje gotową metodologię pomiaru toru**, dokładnie tę, którą zapisałem w `03_SCIANY_FIZYCZNE.md` sekcja 6: zewrzeć wejście, zmierzyć szum. Teraz jest liczba, do której można się porównać: **0,08 µV RMS**.
3. **Pokazuje, gdzie leży realny problem, i nie jest nim szum.** Ich CMRR spada o 26,9 dB przy **niedopasowaniu impedancji źródła** — czyli wtedy, gdy elektrody mają różne impedancje. To jest dokładnie sytuacja elektrod suchych na owłosionej potylicy. **To jest konkretna, zmierzona przez kogoś innego wskazówka, gdzie nasz układ się wywróci.**
4. **Ich ITR to 27,66 bit/min przy 99,17% dokładności** — czyli bardzo dokładnie, ale wolno. To ustawia realistyczne widełki inaczej niż 102 bit/min Imperialu.

**Czego to nie zabiera:** oni nie robią kompensacji artefaktu. Budują i charakteryzują platformę.

---

## 9. Znalezisko, które WZMACNIA tezę projektu

`[fakt, abstrakt odczytany]` **Yang S.Y., Lin Y.P., *IEEE Trans Neural Syst Rehabil Eng* (2023), PMID 37751338** — *„Movement Artifact Suppression in Wearable Low-Density and Dry EEG Recordings Using Active Electrodes and Artifact Subspace Reconstruction"*.

Osiemnastu badanych, zadanie oddball podczas chodzenia na bieżni (1 i 2 km/h), trzy warianty systemu trzykanałowego: elektrody suche pasywne, suche aktywne, mokre pasywne.

Wynik, cytat:

> „only the **active-electrode design** more or less rectified movement artifacts for dry electrodes, whereas the **ASR pipeline was substantially compromised by limited electrodes**. These findings suggest that a lightweight, minimally obtrusive dry EEG headset should **at least equip an active-electrode infrastructure** to withstand realistic movement artifacts."

**To jest recenzowany dowód na tezę, którą projekt stawia:** w reżimie **małej liczby kanałów i elektrod suchych** rozwiązanie **sprzętowe działa, a programowe zawodzi**. ASR — czyli klasa metod cyfrowych — „substantially compromised by limited electrodes".

To jest drugi, niezależny od Kołodzieja argument za tym, żeby artefaktem zająć się w sprzęcie, i pochodzi z innego zespołu, innego kraju i innego roku.

---

## 10. Grupa konkurencyjna — sprawdzona imiennie

`[fakt]` Przeszukanie PubMed po autorze `Kolodziej M[au]` w połączeniu z EEG/BCI/SSVEP daje **siedem pozycji**, z czego dotyczące EEG i BCI to:

| Rok | Praca | Charakter |
|---|---|---|
| 2026 | Improved SSVEP Classification Through EEG Artifact Reduction Using Auxiliary Sensors | **regresja liniowa, SVM, CNN** |
| 2022 | Implementation of a Convolutional Neural Network for Eye Blink Artifacts Removal | **sieć neuronowa** |
| 2018 | The Impact of Different Visual Feedbacks in User Training on Motor Imagery Control in BCI | **badanie behawioralne** |

**Wniosek `[wniosek]`, istotny dla oceny ryzyka z K-044:** to jest zespół **przetwarzania sygnałów i uczenia maszynowego**, nie projektowania układów analogowych. W ich dorobku nie ma ani jednej pracy sprzętowej.

**Skutek: ryzyko, że sami wykonają wersję analogową, jest niższe, niż zapisałem w K-044.** Zdanie o „artifact reduction at the signal acquisition stage" w sekcji przyszłych prac czyta się w tym kontekście jako **wskazanie kierunku dla kogoś innego**, a nie zapowiedź własnego następnego kroku. Obniżam to ryzyko z „dziesiątki procent" na **rząd 10–20%** — nadal realne, ale nie dominujące.

**Czego to nie wyklucza:** że zrobi to inny zespół, albo że nawiążą współpracę z grupą układową. Monitorowanie zostaje w planie.

---

## 11. Co drugie przejście zmieniło

| Ustalenie | Przed | Po drugim przejściu |
|---|---|---|
| ryzyko, że grupa z PW zrobi to sama | dziesiątki procent | **10–20%** — to zespół algorytmiczny, bez dorobku sprzętowego |
| wykonalność techniczna platformy | `[wniosek]`, oszacowanie | **potwierdzona: opublikowana, scharakteryzowana platforma ESP32+ADS1299 z pomiarami** |
| gdzie układ się wywróci | nieznane | **niedopasowanie impedancji źródła — spadek CMRR o 26,9 dB**, zmierzone przez innych |
| argument „sprzęt zamiast programu" | nasze rozumowanie | **recenzowany dowód: Yang i Lin 2023, ASR zawodzi przy małej liczbie kanałów, elektroda aktywna działa** |
| układ elektrod jako wynalazek | „raczej nie" | **definitywnie nie — opatentowane, US 11241183 B2, Neurolutions, żywy** |
| US 5513649 jako zagrożenie | niesprawdzone | **nie jest — cyfrowy, o artefaktach ruchowych, wygasł w 2014** |

**Twierdzenie projektu po dwóch przejściach audytu pozostaje to samo, ale stoi teraz na trzech niezależnych podporach zamiast jednej:**

1. **Kołodziej i in. 2026** — kanał szczękowy poprawia klasyfikację potylicznego SSVEP o ~9 pp, i wskazanie etapu akwizycji jako następnego kroku
2. **Yang i Lin 2023** — w reżimie małej liczby kanałów i elektrod suchych sprzęt działa, a metody cyfrowe zawodzą
3. **arXiv 2601.01772** — platforma ESP32+ADS1299 jest wykonalna i scharakteryzowana, a jej słabym punktem jest niedopasowanie impedancji, czyli dokładnie to, co kompensacja może poprawić

**Czego nie znalazłem w żadnym z dwóch przejść:** analogowej kompensacji zmierzonego artefaktu mięśniowego z dedykowanego kanału, przed wzmocnieniem, w noszalnym urządzeniu EEG.

---

# CZĘŚĆ III — trzecie przejście: konferencje układowe

**Zlecenie:** domknąć jedyną lukę zgłoszoną na końcu części II — ISSCC, JSSC i pokrewne konferencje układowe, których nie ma w PubMed.

**Kanał:** **Crossref API**, który indeksuje IEEE TBioCAS, ISSCC, ISCAS, A-SSCC, BioCAS i pokrewne. (OpenAlex i Semantic Scholar odmówiły — wyczerpany limit zapytań i 429. Crossref zadziałał i pokrywa te same wydawnictwa.)

---

## 12. Znalezisko, które koryguje MOJĄ WŁASNĄ korektę

`[fakt]` **Dabbaghian A., Kassiri H., *„An 8-Channel Ambulatory EEG Recording IC With In-Channel Fully-Analog Real-Time Motion Artifact Extraction and Removal"*, IEEE Transactions on Biomedical Circuits and Systems, 2023, DOI 10.1109/tbcas.2023.3289159.**

Do tego, tej samej grupy: *„An 8-Channel 0,45 mm²/Channel EEG Recording IC with ADC-Free Mixed-Signal In-Channel Motion Artifact Detection"*, **ISCAS 2020**.

**Pierwsza sesja miała rację, a ja ją błędnie poprawiłem.** Opis „8-kanałowy IC EEG ambulatoryjny z wewnątrzkanałową, w pełni analogową ekstrakcją i usuwaniem artefaktów ruchowych, publikacja ~2023" był **poprawny co do wszystkiego** — jest to układ scalony, jest ośmiokanałowy, jest z 2023 roku.

W K-029 uznałem, że chodzi o *„A 9,2-g Fully-Flexible Wireless Ambulatory EEG Monitoring and Diagnostics Headband"* (2019, ten sam pierwszy autor) i „poprawiłem" rok oraz klasę urządzenia. **To są dwie różne prace tej samej grupy** (laboratorium Kassiriego, York University): opaska z 2019 i układ scalony z 2023.

**K-029 zostaje wycofana w części dotyczącej roku i klasy urządzenia.** Utrzymuje się wyłącznie zastrzeżenie o parametrze CMRR >115 dB, którego nie zweryfikowałem w żadnej z tych prac.

**To trzeci przypadek w tej sesji, gdy przesadziłem w korekcie** (poprzednie: K-040 — zawyżenie wyniku SpiralE; K-029 — właśnie ten). **Wzorzec jest jednoznaczny: koryguję zbyt pewnie, na podstawie pierwszego znalezionego dopasowania, nie sprawdzając, czy nie istnieje druga praca tych samych autorów.** Reguła operacyjna, która z tego zostaje: przed skorygowaniem cudzego namiaru sprawdzić, czy autorzy nie mają kilku prac o zbliżonym tytule.

---

## 13. Pełen obraz analogowego usuwania artefaktów — po przeszukaniu konferencji układowych

| Rok | Praca | Co robi | Czy to nasza oś |
|---|---|---|---|
| **1984** | *EMG artifact minimization during clinical EEG recordings by **special analog filtering***, Electroenceph Clin Neurophysiol | analogowe **filtrowanie pasmowe** EMG | **nie** — filtracja częstotliwościowa, nie odejmowanie zmierzonego artefaktu |
| 1996 | *Application of **LMS adaptive predictive filtering** for muscle artifact cancellation from EEG*, Comput Electr Eng | filtr adaptacyjny LMS | **nie** — cyfrowy |
| 2016 | *An analog front-end with fast **motion artifact recovery*** for bio-signal recording, VLSI-DAT | odzyskiwanie po artefakcie ruchowym | **nie** — ruch, nie mięsień |
| 2020 | Dabbaghian, Kassiri, ISCAS — IC z mieszaną detekcją artefaktu ruchowego bez ADC | artefakt **ruchowy** | **nie** |
| 2023 | **Dabbaghian, Kassiri, TBioCAS — IC z w pełni analogową ekstrakcją i usuwaniem artefaktu ruchowego** | artefakt **ruchowy**, wewnątrzkanałowo, analogowo | **nie — ale najbliżej ze wszystkiego** |
| 2023 | *A Low-power Reconfigurable Neural Interface AFE IC with **Common-mode Artifact Cancellation Loop*** | **szum wspólny** | **nie** |
| 2025 | *EEG Artifact Removal At the Edge Using **AI Hardware***, IEEE Sensors Lett | wnioskowanie na brzegu | **nie** — cyfrowe, tylko lokalnie |
| **2026** | **Kołodziej i in., Sensors — kanały pomocnicze, w tym szczękowy, dla potylicznego SSVEP** | **artefakt mięśniowy, kanał referencyjny** | **tak co do idei — ale CYFROWO, regresją** |

**Wniosek po trzech przejściach i czterech bazach:**

Analogowe radzenie sobie z artefaktami w EEG jest dziedziną zajętą — ale **konsekwentnie dla artefaktów ruchowych, szumu wspólnego i offsetu**. Artefakt **mięśniowy** obsługuje się albo analogowym filtrowaniem pasmowym (1984, prymitywne i zawodne, bo pasma EMG i EEG się pokrywają), albo **cyfrowo** (1996 → 2026).

**Nie znalazłem — w PubMed, arXiv, Crossref i bazie patentów — analogowego odejmowania zmierzonego artefaktu mięśniowego z dedykowanego kanału referencyjnego, przed wzmocnieniem, w noszalnym urządzeniu EEG.**

To jest najmocniejsze zdanie o nowości, jakie mogę uczciwie napisać. **I nadal nie jest dowodem nieistnienia** — jest opisem tego, gdzie szukałem i czego nie znalazłem.

---

## 14. Zamknięcie audytu

**Przeszukane kanały:** PubMed (E-utilities), arXiv (API), Crossref (API), Google Patents przez wyszukiwarkę, bazy abstraktów ISEF, strony i regulaminy obu konkursów. **Nieprzeszukane i zgłaszam to jawnie:** literatura nieanglojęzyczna, pełne teksty zastrzeżeń patentowych, IEEE Xplore bezpośrednio (pokryty pośrednio przez Crossref i PubMed), oraz prace za paywallem, których abstrakty przeczytałem, ale pełnych tekstów nie.

**Stan tezy o innowacyjności po trzech przejściach:**

| Warstwa | Status |
|---|---|
| tani interfejs SSVEP | **zajęte** — £20, 102 bit/min, Imperial College |
| elektroda sucha przez włosy | **zajęte** — PNAS 2025, Georgia Tech, patent w toku |
| układ elektrod centralna + obwodowe | **zajęte i opatentowane** — US 11241183 B2, Neurolutions |
| platforma ESP32 + ADS1299 | **zajęte** — arXiv 2601.01772, ze scharakteryzowanymi parametrami |
| kanał pomocniczy przeciw artefaktowi mięśniowemu, cyfrowo | **zajęte** — Kołodziej i in. 2026, +9 pp |
| analogowa kompensacja artefaktu **ruchowego** | **zajęte** — Dabbaghian, Kassiri, IC 2023 |
| **analogowa kompensacja artefaktu MIĘŚNIOWEGO z kanału referencyjnego, przed wzmocnieniem, w urządzeniu noszonym** | **nie znalezione w czterech bazach** |

**To jest wynik audytu i na nim kończę.** Nie umiem sprawdzić więcej kanałami, które mam.
