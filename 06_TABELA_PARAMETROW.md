# 06 — Tabela parametrów porównawczych

**Zakres wg sekcji 10.F handbooka.** Wspólna metryka dla wszystkiego z plików 01–05, plus **kolumna widoczności** wynikająca z twardego wymagania użytkownika, plus **kolumna „skąd ta liczba"** wymagana przez K-004 z `KOREKTY.md`.

---

## 0. Jak czytać tę tabelę — trzy zastrzeżenia, bez których wprowadza w błąd

**1. Kolumna „skąd ta liczba" jest ważniejsza niż sama liczba.**

> **AKTUALIZACJA 15 VIII 2026, wieczór.** Część liczb została **zweryfikowana w abstraktach odczytanych z PubMed**. Te mają w kolumnie „skąd" wpis **`abstrakt`** i numer PMID, i **nie mają już znacznika `[wniosek, streszczenie]`**. Reszta pozostaje na streszczeniach i jest tak oznaczona. Trzy liczby okazały się błędne — patrz `KOREKTY.md` K-030, K-031, K-032.
>
> **Dodana kolumna „n"** — liczba badanych. Jej brak był realnym błędem poprzedniej wersji: liczba bez wielkości próby nie znaczy tego, co się wydaje, że znaczy. Dokładnie tego wymaga sekcja 10.G handbooka od naszych własnych liczb, więc nie ma powodu, żeby cudze traktować łagodniej.

**2. ITR między pracami nie jest wprost porównywalny.** Wzór Wolpawa jest jeden:

> ITR [bit/min] = [log₂N + P·log₂P + (1−P)·log₂((1−P)/(N−1))] / (t/60)

gdzie **N** to liczba możliwych wyborów, **P** dokładność, **t** średni czas jednego wyboru w sekundach `[fakt, wiele źródeł zgodnych; źródło pierwotne: Wolpaw i in., Clin Neurophysiol 113:767–791, 2002]`.

Ale to samo N przy innym zadaniu znaczy co innego, a **t** bywa liczone raz z przerwami międzypróbowymi, raz bez. Różnice rzędu dwukrotności wynikają z konwencji, nie z jakości układu. **Kolumny ITR używać do porównań rzędu wielkości, nie do rankingu.**

**3. „Słowa na minutę" to nie jest ta sama metryka co ITR** i między pracami nad mową też nie jest ta sama. Rozbiór w `07_DEKODOWANIE.md` sekcja 5.

---

## 1. Interfejsy sterujące i komunikacyjne — wydajność

| Rozwiązanie | Modalność | Kanały | n | Dokładność | ITR | wpm | Widoczne? | Skąd ta liczba |
|---|---|---|---|---|---|---|---|---|
| SSVEP wielokomendowy, potylica | EEG skalp | wiele | ? | 92,8% | **91,7 bit/min** | — | **tak, czapka** | streszczenie, 12 celów |
| SSVEP high-speed (Chen 2015) | EEG skalp | wiele | ? | — | — | **~12** (60 znaków/min) | **tak** | namiar potwierdzony, PNAS 112, PMID 26483479 |
| SSVEP ogólnie | EEG skalp | wiele | — | wysoka | ~70 bit/min | — | **tak** | streszczenie, wartość zbiorcza |
| **SSVEP douszne, SpiralE, offline** | **ear-EEG konformalne** | mało | ? | **95%** (9 celów) | — | — | **nie** | **abstrakt, Nat Commun 14:4213, PMID 37452047** |
| **SSVEP douszne, SpiralE, speller online** | **ear-EEG konformalne** | mało | ? | **40 celów, bez kalibracji** | — | — | **nie** | **abstrakt, j.w.** |
| SSVEP douszne, online (2015) | ear-EEG | mało | **4** | **87,9 ± 12,1%** | **16,6 ± 6,6 bit/min** | — | **nie** | **abstrakt, EMBC 2015, PMID 26736745** |
| SSVEP douszne, offline, okno 4 s (2015) | ear-EEG | mało | **4** | 82,7 ± 11,8% | — | — | **nie** | **abstrakt, j.w.** |
| SSVEP douszne, T7/T8, CNN | ear-EEG | 2 | ? | 63,5% (69,2% trening grupowy) | 6,4 bit/min | — | **nie** | **abstrakt, Front Comput Neurosci 16:868642, PMID 35664916** |
| P300 słuchowy, ear-EEG | ear-EEG | mało | **95,6%** | **~2,97 bit/min** | — | **nie** | streszczenie, IEEE 8311519 |
| P300 słuchowy hybrydowy | EEG skalp | — | 85,3% | 9,1 bit/min | — | tak | streszczenie |
| P300 słuchowy klasyczny | EEG skalp | — | 74,6% | 4,2 bit/min | — | tak | streszczenie |
| ASSR / uwaga słuchowa | EEG skalp | — | 64,7–84,3% | **1,89–2,08 bit/min** | — | tak | streszczenie, Applied Acoustics 2024 |
| ASSR BCI, binarne | EEG skalp | — | 66,7% | 2,0 bit/min | — | tak | streszczenie |
| EEG jednokanałowy, ERP słuchowy, 3 komendy | EEG czoło | **1** | 80,0 ± 19,4% | 1,16 ± 0,83 bit/min | — | tak | streszczenie, PMC6669913 |
| dekodowanie uwagi słuchowej, cEEGrid, 3 mówców, okno 30 s | ear-EEG | 16 | **41,5%** (Wiener) | — | — | **nie** | streszczenie, arXiv 2510.19174 |
| dekodowanie uwagi, cEEGrid, okno 10 s | ear-EEG | 16 | 37,8% (CSP) / 37,6% (Riemann) | — | — | **nie** | j.w. |
| speller P300 klasyczny (Farwell–Donchin) | EEG skalp | — | — | ~0,5 bit/s | ~1 (5 znaków/min) | tak | streszczenie |
| **proteza mowy wewnątrzkorowa (Willett 2023)** | **inwazyjne** | Utah | WER 9,1% / 23,8% | — | **62** | n/d | streszczenie, Nature 620 |
| **proteza mowy ECoG (Metzger 2023)** | **półinwazyjne** | ECoG | WER 25,5% (1024 słowa) | — | **78** | n/d | streszczenie, Nature |
| proteza mowy (Card 2024) | inwazyjne | — | 99,6% (50 słów) / 90,2% (125k) | — | — | n/d | streszczenie, NEJM 391:609 |
| speller ECoG P300 | półinwazyjne | ECoG | — | do 1,9 bit/s | ~3–4 (17–22 znaki/min) | n/d | streszczenie |
| **AlterEgo (silent speech)** | **sEMG, nie mózg** | — | 92% (2018) | — | **>100** deklarowane | tak, na twarzy | streszczenie |
| OPM-MEG mind-spelling | MEG | 80+ | **97,7%** | — | — | **tak, i wymaga ekranowania** | streszczenie, jedno źródło |
| **ID.EARS, 5 gestów** | **EMG/EOG przy uchu** | 1 ucho | **>90%** | — | — | **nie** | streszczenie, CHI 2025 |
| eye tracking | kamera | — | ułamek stopnia | bardzo wysokie | — | zależy od montażu | wiedza ogólna |
| **projekt referencyjny ENBM074 (2026)** | nieinwazyjne, **sprzęt konsumencki za 1 800 USD** | ? | 111 prób + replikacja | — | — | **65 vs 3** (baseline: własny speller na tym samym sprzęcie) | tak, sprzęt kupiony | **abstrakt odczytany w bazie Society for Science. K-004 ZAMKNIĘTE — liczby są prawdziwe** |

---

## 2. Parametry sprzętowe

| Element | Wartość | Skąd ta liczba |
|---|---|---|
| **amplituda EEG** | 10–100 µV (skrajnie 15–150) | streszczenia, kilka źródeł zgodnych |
| **amplituda EOG** | do 30–40 mV u źródła | streszczenie |
| **amplituda EMG** | 50 µV – 30 mV | streszczenie |
| stosunek EMG/EEG | **×10–100** | streszczenie, zgodne z powyższymi |
| **szum wejściowy ADS1299** | **1,0 µV p-p @ 70 Hz** | **strona producenta (TI), odczytana. Potwierdzone** |
| **CMRR ADS1299** | **−110 dB** | **strona producenta. POPRAWKA — było −120 dB, K-030** |
| rozdzielczość / wzmocnienie / próbkowanie ADS1299 | 24 bity / 1–24 / 250 SPS – 16 kSPS | strona producenta |
| ~~CMRR dobrego IC EEG @ 50/60 Hz >115 dB~~ | **WYCOFANE** | liczba przypisana błędnie pracy Dabbaghian 2019; nie występuje w tym źródle. K-029 |
| CMRR układu RLD | 80–100 dB | streszczenie |
| impedancja, elektroda mokra Ag, kanał słuchowy @50 Hz | **4 kΩ** (σ=3) | streszczenie, jedno źródło |
| impedancja, elektroda sucha Ag | **452 kΩ** (σ=737) | j.w. |
| impedancja, elektroda sucha IrO₂ | **435 kΩ** (σ=515) | j.w. |
| impedancja, elastomer z Ag/AgCl | 25–300 kΩ | streszczenie |
| rozdzielczość przestrzenna EEG skalpowego | **5–9 cm** | streszczenie, kilka źródeł |
| przewaga jakości sygnału inwazyjnego nad nieinwazyjnym | **20 – ponad 100×** | streszczenie, jedno źródło |
| zmiana mocy alfa (oczy otwarte/zamknięte), skalp | **152%** | streszczenie, jedno źródło |
| zmiana mocy alfa, ucho | **57%** | j.w. |
| **korelacja sygnału dousznego ze skalpowym** | **istotna w ~80% przypadków** (p<0,01), n=**30** | **abstrakt, Front Neurosci 18:1441897, PMID 39319310. POPRAWKA — wcześniej opisane jako „wykrywalność alfy w ~80% zapisów", to co innego. K-032** |
| amplituda alfy i SNR w uchu vs skalp | **niższe w uchu**, n=30 | abstrakt, j.w. |
| SNR douszne vs czołowe | 5–6 vs 8 | streszczenie, jedno źródło |
| BCI illiteracy, wyobrażenie ruchu | **15–30% osób** | streszczenie, dwa źródła zgodne |

---

## 3. Rynek i widoczność

| Produkt | Kanały | Cena | Montaż | Widoczne? | Sterowanie? |
|---|---|---|---|---|---|
| OpenBCI Cyton | 8 | modułowa | minuty | zależy od czapki | tak, surowy sygnał |
| Emotiv EPOC X | 14 | **999 USD** | ~minuta | **tak, wyraźnie** | ograniczone |
| Emotiv Insight | 5 | 499 USD | ~minuta | **tak** | ograniczone |
| Muse S Athena | mało | ~400–500 USD | sekundy | **tak, opaska** | nie |
| Neurable MW75 Neuro | — | **699 USD** | sekundy | wygląda jak słuchawki | **nie** |
| NextSense Smartbuds | **6** | **399,99 USD** | sekundy | wygląda jak słuchawki | **nie** |
| IDUN Guardian 4 | — | brak ceny | sekundy | wygląda jak słuchawki | **nie** |
| **cel projektu** | ? | ? | sekundy | **zauszne, wielkości aparatu słuchowego** | **tak — to jest różnica** |

---

## 4. Skala widoczności — domknięcie luki 2.4 z `00_PYTANIA_I_LUKI.md`

Handbook żądał kolumny „czy widać, że użytkownik to ma na sobie", ale nie podał progu. Bez progu kolumna jest opinią. Proponowana skala, do zatwierdzenia albo poprawienia przez użytkownika:

| Stopień | Definicja operacyjna | Przykłady | Werdykt użytkownika |
|---|---|---|---|
| **0** | niewidoczne dla obserwatora z 2 m | całkowicie w kanale słuchowym, schowane pod włosami | — |
| **1** | widoczne, ale nierozpoznawalne jako sprzęt pomiarowy | aparat słuchowy, słuchawki douszne | **przechodzi** (D1) |
| **2** | rozpoznawalne jako elektronika noszona, ale zwyczajna | słuchawki nauszne (MW75) | nierozstrzygnięte |
| **3** | rozpoznawalne jako sprzęt na głowę | opaska Muse | **raczej odpada** (D1) |
| **4** | wyraźnie sprzęt pomiarowy | czapka EEG, EPOC X | odpada |

**AKTUALIZACJA 15 VIII 2026 — próg przesunięty, kryterium zmienione.**

Użytkownik rozstrzygnął, że kryterium to **gabaryt, nie widoczność**: *„może być nawet widoczne … pod warunkiem, że będą mniejsze, a nie cała stacja pomiarowa"*. Kategoryczne „nie" dotyczyło hełmów.

| Nowe kryterium | Przechodzi |
|---|---|
| moduł wielkości aparatu słuchowego lub słuchawki dousznej | **tak**, także kilka takich |
| moduł z tyłu głowy, widoczny | **tak** |
| cienki łuk lub przewód przy głowie | **tak** |
| konstrukcja nad czubkiem głowy lub przez czoło | **nie** |
| pasek pod brodą, opaska czołowa, moduł zewnętrzny na kablu | **nie** |
| cokolwiek typu hełm | **nie, granica twarda, powtórzona dwukrotnie** |

Kolejność ustępstw przy konflikcie: najpierw gabaryt i widoczność, potem wygoda, **nigdy hełm**.

Stopnie 0–4 poniżej zostają jako narzędzie opisowe, ale **próg akceptacji nie leży już na granicy 1/2**. Szczegóły: `09_UMIEJSCOWIENIE.md` sekcja 5a.

**[wniosek] Dlaczego ta skala jest użyteczna nie tylko wewnętrznie:** stopnie 0–1 są sprawdzalne prostym testem, który da się wykonać i pokazać na stoisku — zdjęcie osoby w urządzeniu, pytanie do widza „gdzie ono jest". To zamienia kolumnę opiniową w pomiar, a plakat zyskuje element, którego nie ma nikt inny.

---

## 5. Co z tej tabeli wynika dla twierdzenia projektu

**PRZELICZONE 15 VIII 2026 wieczorem. Punkt 1 był błędny i był fundamentem rekomendacji C2.**

**1. Wariant „lepszy w przepustowości" NIE jest zamknięty — `KOREKTY.md` K-028.** Liczby 6–17 bit/min, na których stało to zamknięcie, pochodziły z prac z **2015 (n=4)** i **2022**. Praca z **Nature Communications 2023** pokazuje z kanału słuchowego 95% na 9 celach i speller 40-celowy online bez kalibracji. Różnica względem potylicy okazała się kosztem **kontaktu elektrody**, nie geometrii — a kontakt elektrody to warstwy 1 i 2 z sekcji 9.4 handbooka, czyli **warsztat użytkownika**.

**Co to znaczy dla decyzji C2:** rekomendacja na wariant 2 (metryka użytkowa) **traci swoje główne uzasadnienie liczbowe**. Nie znaczy to, że wariant 2 jest zły — znaczy, że wybór trzeba przeprowadzić od nowa, na trzech wariantach o porównywalnym statusie, a nie na jednym pozostałym po eliminacji. **To jest decyzja użytkownika i zostaje otwarta.**

**2. Wariant „przewaga przy stałej widoczności" ma baseline słaby, ale nie pusty.** Żaden produkt komercyjny na stopniu 0–1 nie robi sterowania. Porównywać trzeba się z **literaturą** ear-EEG. Doszła pozycja, której wcześniej nie miałem: *„Electrophysiological Characterisation of Commercial Ear-EEG Devices"*, EMBC 2025, PMID 41336899 — charakterystyka elektrofizjologiczna urządzeń komercyjnych, czyli gotowy materiał na ten baseline.

**3. Wariant „metryka użytkowa" nadal ma najwięcej wolnego miejsca.** Czas montażu, stabilność w ciągu dnia, odsetek sesji bez rekalibracji, tolerancja na ruch i mówienie — praktycznie nieraportowane, a wskazywane jako motywacja całej linii ear-EEG.

**Uwaga formalna, której nie było, a która ogranicza wariant 3 (`ISEF_HUMAN_PARTICIPANTS.md` sekcja 1.1):** metryki zależne od stanu badanego (wyspanie, zmęczenie) są w regulaminie ISEF **zmienną ludzką** i łamią zwolnienie dla badania na sobie. Mierzenie dryfu jakości sygnału w czasie noszenia — dozwolone. Mierzenie, jak wynik zależy od tego, ile badany spał — wymaga zgody IRB. Granica jest cienka i trzeba ją trzymać świadomie.

**4. Wiersz projektu referencyjnego jest już wypełniony i K-004 zamknięte.** Liczby 65 i 3 wpm są prawdziwe, pochodzą z abstraktu, a baseline 3 wpm to **własny warunek kontrolny autora na tym samym sprzęcie**, nie wybrany dolny koniec cudzego rozrzutu. Mój zarzut z `07` sekcja 5.2 nie dotyczy tej pracy i został wycofany. Zgodnie z sekcją 9.2 handbooka nadal nie ustawiamy tego wyniku jako progu — ale teraz przynajmniej wiadomo, czego się nie ustawia.
