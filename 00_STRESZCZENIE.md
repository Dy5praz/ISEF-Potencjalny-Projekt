# 00 — Streszczenie etapu 1

**Data:** 15 sierpnia 2026
**Zakres:** przemiał literatury wg sekcji 10 handbooka, plus 12 zadań weryfikacyjnych z `00_PYTANIA_I_LUKI.md` sekcja 4d.

---

## 0. Status źródłowy tego etapu — przeczytaj przed resztą

**[fakt] Dostęp do sieci nadal nie został przełączony na `Full`.** Sprawdzone trzema niezależnymi drogami 15 VIII 2026: tunel HTTPS kontenera (brama odpowiada 403 na CONNECT), narzędzie WebFetch (`EGRESS_BLOCKED` dla każdej domeny), bezpośredni `curl`. Przechodzą wyłącznie rejestry pakietów i GitHub.

Działa jedno narzędzie: wyszukiwarka, która zwraca **listę tytułów z adresami plus streszczenie wygenerowane przez inny model**. Nie otworzyłem ani jednej pracy źródłowej.

**Co z tego wynika dla wiarygodności tego etapu — bez owijania:**

| Rodzaj twierdzenia | Status po tym etapie |
|---|---|
| istnienie pracy, autorzy, rok, czasopismo | **wiarygodne** — tytuły i adresy pochodzą z indeksu wyszukiwarki, nie ze streszczenia |
| liczby przypisane pracy (dokładności, ITR, ceny, impedancje) | **do potwierdzenia w oryginale.** Wszystkie oznaczone `[wniosek, streszczenie]` |
| treść dokumentów regulaminowych (ISEF, Explory, El-Robo-Mech) | **nie zamknięte.** Dokument regulaminowy stoi na szczycie hierarchii z sekcji 13 handbooka i parafraza streszczenia go nie zastępuje |

Nie rozpisałem tego etapu na streszczeniach udając, że to przemiał literatury. Rozpisałem to, co daje się rzetelnie ustalić na tym kanale, i **przy każdej liczbie widać, skąd pochodzi**. Sekcja 6 poniżej mówi, co dokładnie zostaje do zrobienia po odblokowaniu sieci — jest tego mniej, niż zakładałem przed startem, ale nie jest to zero.

---

## 1. Trzy ustalenia, które zmieniają plan

### 1.1 [wniosek, dwa źródła zgodne] Teza „jeden strzał" **przeżywa**. K-007 zamknięte na korzyść handbooka

To było pytanie o najwyższej stawce w całym projekcie (zadanie 4d nr 1).

Ustalony wzorzec: **finał krajowy w październiku roku N wyłania reprezentację na ISEF w maju roku N+1.**

| Edycja | Finał | ISEF |
|---|---|---|
| Explory 2025 (XIV GEW) | X 2025 | ISEF 2026, Phoenix |
| Explory 2026 (XV GEW) | 21–23 X 2026 | ISEF 2027 |
| **edycja użytkownika** | **X 2027** | **ISEF V 2028** |

Potwierdzenie krzyżowe: reprezentacja na ISEF 2026 to Emil Pająk, Jagoda Sułek oraz Marta Truszczyńska z Pauliną Duszyńską — **3 projekty, 4 osoby**, dokładnie tak, jak podaje sekcja 4.9 handbooka. Zgodność niezależnie zebranej listy z liczbą z handbooka podnosi zaufanie do obu.

**Konsekwencja:** okno zgłoszeń IX 2026 – II 2027 prowadzi do finału X 2027 i do ISEF 2028. Kalendarz z sekcji 3 handbooka jest poprawny, alternatywa z punktu 1.4 `00_PYTANIA_I_LUKI.md` (że reprezentacja na 2028 została już wyłoniona) **odpada**. Kolizja z maturą nie występuje.

To jedyna dobra wiadomość w tej sekcji.

### 1.2 [fakt] Pomysł „sygnały mięśniowo-oczne przy uchu jako sterowanie" jest zajęty, opublikowany i zademonstrowany

**ID.EARS**, konferencja CHI 2025 (An, Oh, Kim, Kim, Park, Oh), DOI 10.1145/3706598.3714185.

Urządzenie na **jedno ucho**, elektrody suche, rozpoznaje w czasie rzeczywistym pięć gestów: mrugnięcie, mrugnięcie lewym okiem, mrugnięcie prawym okiem, zaciśnięcie zębów, żucie. **Ponad 90% dokładności** w walidacji krzyżowej [wniosek, streszczenie]. Zastosowania pokazane przez autorów: sterowanie muzyką, dostępność, sterowanie MR/XR.

Sformułowanie z abstraktu jest dla nas kluczowe: dotychczasowe badania nad EEG dousznym traktowały EMG i EOG **jako niepożądany szum do usunięcia**, a ID.EARS odwraca to i robi z szumu sygnał.

**Co to zabija:** rolę 1 z sekcji 4b/C3 `00_PYTANIA_I_LUKI.md` — sEMG/EOG jako źródło sterowania w formie zausznej. Nie „prawdopodobnie zajęte", tylko zajęte, z demonstracją, na topowej konferencji od HCI, rok temu. Użytkownik odłożył ten wariant z innego powodu (uczciwość twierdzenia); teraz dochodzi drugi, twardszy.

**Czego to nie zabija:** roli 2, czyli usuwania tych sygnałów z EEG. ID.EARS idzie w **przeciwną stronę** niż nasz kandydat na oś projektu. To nie jest kolizja — ale jest to dowód, że okolica ucha jest terenem, po którym chodzą ludzie z dobrymi publikacjami, i że „nikt tego nie robił" nie jest tu bezpiecznym założeniem o niczym.

### 1.3 [wniosek] Uzasadnienie „odczyt ciągły wymusza hełm" jest **słabsze**, niż je postawiłem w rundzie drugiej

W sekcji 4c `00_PYTANIA_I_LUKI.md` napisałem, że rytmy sensomotoryczne z okolicy ucha spadają prawdopodobnie do poziomu szumu własnego wzmacniacza, i na tym oparłem rozstrzygnięcie o odczycie dyskretnym.

Znalezione: **„Detection of motor-related mu rhythm desynchronization by ear EEG"**, PLOS One 2025. Praca dokładnie o tym, że desynchronizacja mu związana z ruchem **jest wykrywalna** z ucha [wniosek, streszczenie, jedno źródło].

Ustalenie „odczyt dyskretny" zostaje w mocy, bo stoi też na innych nogach (metryka standardowa, krótki trening, czyste zejście o poziom w dół, pokaz na stoisku). Ale **argument, którym je uzasadniłem, był za mocny i muszę go skorygować**, zanim użytkownik użyje go przed jurorem, który zna dziedzinę. Wpis w `KOREKTY.md` jako K-014. Szczegóły w `03_SCIANY_FIZYCZNE.md` sekcja 3.

---

## 2. Odpowiedź na zadanie nr 3 — czy oś projektu jest zajęta

Pytanie z sekcji 4c/C3, zapisane w `KOREKTY.md` jako K-009 **przed** sprawdzeniem: czy sprzętowe usuwanie zakłóceń mięśniowo-ocznych w torze analogowym urządzenia przyusznego jest już zrobione.

**Odpowiedź: typ K-009 był trafny co do kierunku i zbyt optymistyczny co do szerokości szczeliny.**

| Warstwa pomysłu | Status | Źródło |
|---|---|---|
| usuwanie artefaktów ocznych przez osobny kanał odniesienia, programowo, po nagraniu | **zajęte od 1983**, technika podręcznikowa | Gratton, Coles, Donchin, *Electroencephalogr Clin Neurophysiol* 55:468–484 [wniosek, streszczenie; metoda regresyjna sięga Hillyard i Galambos 1970] |
| usuwanie artefaktów w domenie analogowej, przed końcowym wzmocnieniem | **zajęte na poziomie układów scalonych** — 8-kanałowy układ EEG z wewnątrzkanałową, w pełni analogową ekstrakcją i usuwaniem artefaktów ruchowych, CMRR >115 dB przy 50/60 Hz | IC ambulatoryjny, ~2023 [wniosek, streszczenie, jedno źródło] |
| kompensacja analogowa **konkretnie EMG szczękowego i EOG**, z dedykowanego kanału odniesienia, w urządzeniu **noszonym przy uchu** | **nie znalazłem takiej pracy** | `[luka]` — brak dowodu nieistnienia, patrz niżej |
| patent na adaptacyjny kompensator artefaktów ruchowych i ocznych w EEG | istnieje, US 5513649 | [wniosek, streszczenie] |

**Uczciwe postawienie sprawy — i to jest zdanie, które trzeba obronić przed jurorem, nie przede mną:** ani sam pomysł, ani jego realizacja analogowa nie są nowe. Nowa może być wyłącznie **kombinacja**: analogowa kompensacja, sygnałów mięśniowo-ocznych, z kanału referencyjnego, w urządzeniu przyusznym, przy poziomie kosztów i złożoności osiągalnym poza laboratorium ASIC. To jest szczelina, nie pole, dokładnie jak zapisał typ K-009.

**Czego nie wolno zrobić:** oprzeć twierdzenia projektu na „nikt tego nie zrobił". Nie mogłem otworzyć IEEE Xplore ani PubMed, więc **brak znaleziska nie jest dowodem nieistnienia** — to jest przeszukanie jednym kanałem, nie przegląd systematyczny. To pozycja obowiązkowa do domknięcia po odblokowaniu sieci.

**Czego natomiast dostarcza literatura, a co wzmacnia sensowność kierunku:** Kappel i in. 2017 (*BioMedical Engineering OnLine* 16, art. 103) mierzyli artefakty fizjologiczne w EEG skalpowym i dousznym równolegle. Wynik: pogorszenie SNR od artefaktów szczękowych jest **w uchu ogólnie większe niż na skalpie** [wniosek, streszczenie]. Czyli problem, który nasz kandydat na oś rozwiązuje, jest w tej właśnie formie udokumentowany jako **poważniejszy**, a nie mniejszy. To jest dobra przesłanka dla projektu i pochodzi z pracy recenzowanej, nie z naszego domysłu.

---

## 3. Pułap tego, co da się obiecać — liczby

Pełna tabela w `06_TABELA_PARAMETROW.md`. Skrót, bo to jest liczba, wokół której trzeba zbudować twierdzenie:

| Rozwiązanie | Dokładność | ITR | Uwaga |
|---|---|---|---|
| SSVEP, elektrody potyliczne, laboratorium | 92,8% | **~92 bit/min**, rekordy wyżej | wymaga hełmu/czapki |
| SSVEP, elektrody uszne, online | 87,9 ± 12,1% | **16,6 ± 6,6 bit/min** | forma douszna |
| SSVEP, elektrody uszne, T7/T8 | 63,5% | 6,4 bit/min | |
| P300 słuchowy, ear-EEG | 95,6% | **~3,0 bit/min** | |
| ASSR, uwaga słuchowa | 64,7–84,3% | **1,9–2,1 bit/min** | wybór binarny |
| dekodowanie uwagi słuchowej, cEEGrid, okno 30 s | 41,5% przy 3 mówcach | — | zadanie trudniejsze niż sterowanie |

Wszystkie `[wniosek, streszczenie]`.

**Wniosek dla twierdzenia projektu [wniosek]:** różnica ITR między formą niewidoczną a czapką jest rzędu **5–15×**, nie kilku procent. Wariant „lepszy od komercyjnych w przepustowości" jest zamknięty — nie z powodu naszego warsztatu, tylko z powodu geometrii. To potwierdza analizę z sekcji 2.1 `00_PYTANIA_I_LUKI.md` i przesuwa decyzję C2 na wariant 1 (przewaga przy stałej widoczności) albo 2 (metryka użytkowa).

**Ostrzeżenie do paradygmatu, który sam rekomendowałem [wniosek, jedno źródło, wysoka waga]:** praca *„Signal-specific performance of in-ear EEG: strengths and limitations"* (Frontiers in Neuroscience 20, 2026; 19 osób, system douszny suchy vs 32-kanałowy BioSemi) podaje, że w konfiguracji dousznej **alfa spoczynkowa wychodzi pewnie, a odpowiedź słuchowa N1-P2 nie** — wiarygodne N1-P2 uzyskano tylko przy uśrednionej referencji skalpowej. Paradygmaty słuchowe, które rekomendowałem w rundzie drugiej jako „te, których generator leży blisko ucha", mogą więc być **gorszym**, a nie lepszym wyborem dla formy dousznej. Do rozstrzygnięcia w oryginale pracy — to jest jedna z ważniejszych pozycji na po odblokowaniu sieci.

---

## 4. Zadanie nr 10 — projekt referencyjny. Kod w handbooku jest błędny

**[fakt] Kod `ENBM074` nie należy do projektu opisanego w sekcji 9.2 handbooka.**

`ENBM074` to **„Synthetic DNA Engineering With ICOR"**, Rishab Jain, Westview High School, Oregon, **ISEF 2022** — projekt nagrodzony George D. Yancopoulos Innovator Award. Potwierdzone tytułem strony w bazie isef.net i osobnym wpisem w bazie abstraktów.

Kody projektów ISEF są **numerowane w obrębie edycji i używane ponownie w kolejnych latach**, więc sam kod bez rocznika nie identyfikuje pracy. Wpis do `KOREKTY.md` jako K-012.

Sam projekt referencyjny istnieje i jest realny: *„Breaking the Brain-Computer Interface Ceiling: Discovering a New Paradigm for Brain-Machine Communication That Enables Noninvasive Interfaces to Reach Invasive-Class Communication Speed"*, autorstwo Ameya Kharade, Nashua High School South, New Hampshire, kwalifikacja przez New Hampshire Science & Engineering Expo, **Grand Award na ISEF 2026** [wniosek, dwa źródła zgodne co do tytułu i szkoły].

**Pełnego abstraktu nadal nie odczytałem** — `isef.net` i baza abstraktów są zablokowane. Liczby 65 i 3 wpm z sekcji 9.2 handbooka pozostają `[domysł]` zgodnie z K-004. Zadanie 4d nr 10 **nie jest zamknięte**.

Kontekst, który udało się ustalić i który jest dla nas ważniejszy niż sam abstrakt — patrz sekcja 5 poniżej oraz `07_DEKODOWANIE.md` sekcja 6.

---

## 5. Skąd biorą się „słowa na minutę" — zadanie z sekcji 10.G handbooka

Handbook kazał sprawdzić szczególnie uważnie dwie rzeczy. Odpowiedzi, obie `[wniosek, streszczenie]`:

**Jak liczone są wpm i ile z tego robi model językowy.** W pracach nad protezami mowy metryka jest liczona **na wyjściu całego łańcucha**, z modelem językowym włącznie. Skala udziału modelu jest duża i mierzalna: w pracy Willetta i in. (Nature 2023) surowy błąd fonemowy sieci rekurencyjnej wynosił **19,7%**, a dopiero po dołożeniu modelu 5-gramowego i przeważaniu dużym modelem językowym schodzi się do błędu słownego rzędu jednocyfrowego. W benchmarku Brain-to-Text '24 algorytm bazowy miał 9,7% WER, zwycięzca 5,8% — przy **tym samym sygnale neuronowym**, czyli cała różnica leży w dekodowaniu.

**Punkt odniesienia dla rozwiązań nieinwazyjnych.** Liczba „kilka słów na minutę" ma pokrycie, ale jest to **środek szerokiego rozrzutu, nie najgorszy przypadek**: klasyczny speller P300 Farwella i Donchina daje ~5 znaków/min, typowe spellery 1–5 znaków/min, a szybkie systemy SSVEP dochodzą do ~60 znaków/min, czyli ~12 słów/min (Chen i in., PNAS 2015). Zestawianie ~60 wpm inwazyjnych z ~3 wpm nieinwazyjnych **wybiera dolny koniec rozrzutu nieinwazyjnego**; uczciwy górny koniec to ~12 wpm.

**Do czego to jest nam potrzebne — dokładnie tak, jak zastrzegł handbook:** nie do audytowania cudzej pracy, tylko po to, żeby **nasza własna liczba znaczyła to, co powiemy, że znaczy**. Reguła operacyjna do etapu 2: każda liczba wydajności naszego układu podawana w dwóch wersjach — surowe dekodowanie i wynik z całą warstwą wspomagającą. Jeżeli podamy jedną, jurorzy z dziedziny zapytają o drugą.

---

## 6. Co zostaje niezamknięte i czego to wymaga

| # z 4d | Zadanie | Stan | Czego brakuje |
|---|---|---|---|
| 1 | który finał wysyła na ISEF 2028 | **zamknięte**, patrz 1.1 | — |
| 2 | ISEF Human Participants | **częściowo**, `ISEF_HUMAN_PARTICIPANTS.md` | oryginał International Rules |
| 3 | czy oś projektu zajęta | **częściowo**, patrz 2 | IEEE Xplore, PubMed — przegląd systematyczny |
| 4 | amplitudy rytmów przy uchu | **częściowo**, `03` | PLOS One 2025, liczby z oryginału |
| 5 | paradygmaty przy uchu | **zrobione**, `07` | potwierdzenie liczb ITR w oryginałach |
| 6 | podział pracy człowiek–maszyna | **zrobione**, `04` + `07` | — |
| 7 | materiały do kontaktu ze skórą | **zrobione**, `05` | — |
| 8 | pomiar szumu bez oscyloskopu | **zrobione**, `03` | — |
| 9 | El-Robo-Mech | **zrobione**, `08` | regulamin edycji 2026/2027, publikacja ~X 2026 |
| 10 | abstrakt projektu referencyjnego | **niezamknięte**, patrz 4 | baza abstraktów |
| 11 | projekty neuro w finałach Explory | **niezamknięte** | listy finalistów 2016–2026 |
| 12 | arkusze oceny ISEF | **niezamknięte** | societyforscience.org |

Pozycje 10, 11, 12 i oryginały regulaminów wymagają `Network access: Full`. Instrukcja przełączenia — `README.md`.

---

## 7. Co z tego wynika dla decyzji, które czekają

1. **C2 rozstrzygnąć na wariant 1 albo 2** z sekcji 2.1 `00_PYTANIA_I_LUKI.md`. Wariant „lepszy w przepustowości" jest zamknięty liczbami z sekcji 3. Moja rekomendacja: **wariant 2, metryka użytkowa**, z wariantem 1 jako tabelą towarzyszącą — bo w metryce użytkowej forma zauszna realnie wygrywa, a w przepustowości najwyżej remisuje sama ze sobą.
2. **Oś „analogowe usuwanie zakłóceń" zostaje kandydatem**, ale twierdzenie projektu nie może brzmieć „pierwszy raz". Musi brzmieć jako pomiar: o ile poprawia się coś mierzalnego względem tego samego układu bez kompensacji. To jest twierdzenie, którego nie unieważni znalezienie cudzej pracy.
3. **Zakup drukarki:** rekomendacja z rundy drugiej potwierdzona, szczegóły w `05_RYNEK.md` sekcja 5.
4. **El-Robo-Mech przestaje być oczywistym źródłem zewnętrznej walidacji** — 34 laureatów w edycji 2026, nagrodą jest indeks na studia, nie miejsce na podium. Szczegóły i alternatywy w `08_KONKURENCJA_ISEF.md` sekcja 4.
</content>
</invoke>
