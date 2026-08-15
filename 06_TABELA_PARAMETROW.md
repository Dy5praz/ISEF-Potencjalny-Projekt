# 06 — Tabela parametrów porównawczych

**Zakres wg sekcji 10.F handbooka.** Wspólna metryka dla wszystkiego z plików 01–05, plus **kolumna widoczności** wynikająca z twardego wymagania użytkownika, plus **kolumna „skąd ta liczba"** wymagana przez K-004 z `KOREKTY.md`.

---

## 0. Jak czytać tę tabelę — trzy zastrzeżenia, bez których wprowadza w błąd

**1. Kolumna „skąd ta liczba" jest ważniejsza niż sama liczba.** Żadnej z tych liczb nie odczytałem z pełnego tekstu pracy. Wszystkie pochodzą ze streszczeń wyszukiwarki.

**2. ITR między pracami nie jest wprost porównywalny.** Wzór Wolpawa jest jeden:

> ITR [bit/min] = [log₂N + P·log₂P + (1−P)·log₂((1−P)/(N−1))] / (t/60)

gdzie **N** to liczba możliwych wyborów, **P** dokładność, **t** średni czas jednego wyboru w sekundach `[fakt, wiele źródeł zgodnych; źródło pierwotne: Wolpaw i in., Clin Neurophysiol 113:767–791, 2002]`.

Ale to samo N przy innym zadaniu znaczy co innego, a **t** bywa liczone raz z przerwami międzypróbowymi, raz bez. Różnice rzędu dwukrotności wynikają z konwencji, nie z jakości układu. **Kolumny ITR używać do porównań rzędu wielkości, nie do rankingu.**

**3. „Słowa na minutę" to nie jest ta sama metryka co ITR** i między pracami nad mową też nie jest ta sama. Rozbiór w `07_DEKODOWANIE.md` sekcja 5.

---

## 1. Interfejsy sterujące i komunikacyjne — wydajność

| Rozwiązanie | Modalność | Kanały | Dokładność | ITR | wpm | Widoczne? | Skąd ta liczba |
|---|---|---|---|---|---|---|---|
| SSVEP wielokomendowy, potylica | EEG skalp | wiele | 92,8% | **91,7 bit/min** | — | **tak, czapka** | streszczenie, 12 celów |
| SSVEP high-speed (Chen 2015) | EEG skalp | wiele | — | — | **~12** (60 znaków/min) | **tak** | streszczenie, PNAS 112 |
| SSVEP ogólnie | EEG skalp | wiele | wysoka | ~70 bit/min | — | **tak** | streszczenie, wartość zbiorcza |
| **SSVEP douszne, online** | **ear-EEG** | mało | **87,9 ± 12,1%** | **16,6 ± 6,6 bit/min** | — | **nie** | streszczenie |
| SSVEP douszne, 7 s okna | ear-EEG | mało | 79,9 ± 13,1% | 11,0 ± 4,2 bit/min | — | **nie** | streszczenie |
| SSVEP douszne, T7/T8, CNN | ear-EEG | 2 | 63,5% (69,2% trening grupowy) | 6,4 bit/min | — | **nie** | streszczenie, Front Comput Neurosci 16:868642 |
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
| **projekt referencyjny (sekcja 9.2 handbooka)** | nieinwazyjne | ? | ? | ? | **~65 vs ~3** | ? | **`[domysł]` — relacja ustna użytkownika, abstraktu nie odczytano. K-004** |

---

## 2. Parametry sprzętowe

| Element | Wartość | Skąd ta liczba |
|---|---|---|
| **amplituda EEG** | 10–100 µV (skrajnie 15–150) | streszczenia, kilka źródeł zgodnych |
| **amplituda EOG** | do 30–40 mV u źródła | streszczenie |
| **amplituda EMG** | 50 µV – 30 mV | streszczenie |
| stosunek EMG/EEG | **×10–100** | streszczenie, zgodne z powyższymi |
| **szum wejściowy ADS1299** | **1,0 µV p-p @ 70 Hz** | **parametr katalogowy, trzy niezależne opisy — najpewniejsza liczba w tym pliku** |
| CMRR ADS1299 | −120 dB | j.w. |
| CMRR dobrego IC EEG @ 50/60 Hz | >115 dB | streszczenie |
| CMRR układu RLD | 80–100 dB | streszczenie |
| impedancja, elektroda mokra Ag, kanał słuchowy @50 Hz | **4 kΩ** (σ=3) | streszczenie, jedno źródło |
| impedancja, elektroda sucha Ag | **452 kΩ** (σ=737) | j.w. |
| impedancja, elektroda sucha IrO₂ | **435 kΩ** (σ=515) | j.w. |
| impedancja, elastomer z Ag/AgCl | 25–300 kΩ | streszczenie |
| rozdzielczość przestrzenna EEG skalpowego | **5–9 cm** | streszczenie, kilka źródeł |
| przewaga jakości sygnału inwazyjnego nad nieinwazyjnym | **20 – ponad 100×** | streszczenie, jedno źródło |
| zmiana mocy alfa (oczy otwarte/zamknięte), skalp | **152%** | streszczenie, jedno źródło |
| zmiana mocy alfa, ucho | **57%** | j.w. |
| wykrywalność alfa w zapisie dousznym | ~80% zapisów | streszczenie |
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

**Cel projektu: stopień 1.** Progiem akceptacji jest granica 1/2 — czyli forma nie może być większa niż słuchawka douszna albo aparat słuchowy.

**[wniosek] Dlaczego ta skala jest użyteczna nie tylko wewnętrznie:** stopnie 0–1 są sprawdzalne prostym testem, który da się wykonać i pokazać na stoisku — zdjęcie osoby w urządzeniu, pytanie do widza „gdzie ono jest". To zamienia kolumnę opiniową w pomiar, a plakat zyskuje element, którego nie ma nikt inny.

---

## 5. Co z tej tabeli wynika dla twierdzenia projektu

**[wniosek] 1. Wariant „lepszy w przepustowości" jest zamknięty.** SSVEP douszne 6–17 bit/min wobec ~92 bit/min z potylicy. To 5–15×, geometria, nie warsztat.

**[wniosek] 2. Wariant „przewaga przy stałej widoczności" ma pusty baseline.** Żaden produkt komercyjny na stopniu 0–1 nie robi sterowania. Trzeba porównywać się z **literaturą** ear-EEG (16,6 bit/min SSVEP, ~3 bit/min P300 słuchowy), nie z produktami. To jest wykonalne i uczciwe.

**[wniosek] 3. Wariant „metryka użytkowa" ma najwięcej wolnego miejsca.** Czas montażu, stabilność w ciągu dnia, odsetek sesji bez rekalibracji, tolerancja na ruch i mówienie — praktycznie nieraportowane, a wskazywane jako motywacja całej linii ear-EEG.

**Rekomendacja bez zmian względem `00_STRESZCZENIE.md`: wariant 2 jako oś twierdzenia, wariant 1 jako tabela towarzysząca.**

**4. Wiersz projektu referencyjnego zostaje pusty w każdej kolumnie poza wpm, a i tam z `[domysł]`.** Zgodnie z K-004 i sekcją 9.2 handbooka nie ustawiamy tego wyniku jako progu — ten wiersz jest w tabeli po to, żeby było widać, że nie ma z czym się porównywać, a nie żeby się porównywać.
</content>
