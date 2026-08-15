# 07 — Warstwa dekodowania

**Zakres wg sekcji 10.G handbooka.** Odblokowana decyzją użytkownika z 14 VIII 2026, więc traktowana z tą samą dokładnością co sprzęt.

---

## 1. Paradygmaty sterowania

**Paradygmat** = umowa między człowiekiem a maszyną o tym, co człowiek robi, żeby w sygnale pojawiło się coś odróżnialnego. Bez paradygmatu nie ma czego dekodować — algorytm nie „czyta myśli", tylko rozpoznaje wzorzec, który sam kazał wywołać.

| Paradygmat | Co robi użytkownik | Trening | Realne ITR | Wymagana pozycja elektrod | Przy uchu? |
|---|---|---|---|---|---|
| **SSVEP** | patrzy na migający obiekt | minuty | 70–92 bit/min z potylicy; **6–17 bit/min z ucha** | potylica | **tak, z 5–15× stratą** |
| **P300 / oddball** | czeka na rzadki bodziec | minuty–godziny | 3–9 bit/min | ciemieniowo | **tak, ~3 bit/min** |
| **wyobrażenie ruchu** | wyobraża ruch kończyną | **tygodnie** | zmienne | kora ruchowa C3/Cz/C4 | **detekcja tak, sterowanie wątpliwe** |
| **uwaga słuchowa / ASSR** | skupia się na jednym z dźwięków | krótki | **1,9–2,1 bit/min** | skroń | **tak, ale patrz sekcja 1.1** |
| **potencjały wolnozmienne (SCP)** | uczy się regulować powolne zmiany | **miesiące** | bardzo niskie | czoło | historyczne, porzucone |
| **wyobrażona mowa** | wyobraża wypowiadanie słowa | — | nieinwazyjnie bardzo słabe | — | nie |

Wszystkie liczby `[wniosek, streszczenie]`, namiary w `ZRODLA.md`.

### 1.1 Ostrzeżenie do paradygmatów słuchowych

W rundzie drugiej rekomendowałem je jako „te, których generator leży blisko ucha". Materiał tego nie potwierdza jednoznacznie — patrz `03_SCIANY_FIZYCZNE.md` sekcja 3.1. Skrót: praca Frontiers 2026 podaje, że w konfiguracji dousznej **odpowiedź słuchowa N1-P2 nie wychodzi wiarygodnie**, podczas gdy alfa spoczynkowa wychodzi.

Do tego liczby: uwaga słuchowa daje **1,9–2,1 bit/min**, najniżej w całej tabeli. Przy dwóch komendach i sześciosekundowych odstępach dokładność 84,3% oznacza w praktyce ~3 komendy na minutę.

**[wniosek] Wniosek, przeciwny do mojej wcześniejszej rekomendacji:** dla sterowania w formie zausznej **SSVEP wygląda lepiej niż paradygmaty słuchowe**, mimo że kora wzrokowa leży dalej od ucha niż słuchowa. Powód: SSVEP daje sygnał okresowy o znanej z góry częstotliwości, więc da się go wyłuskać uśrednianiem i filtracją wąskopasmową nawet przy złym SNR, a odpowiedź ERP takiej struktury nie ma. To jest przewaga **metody detekcji**, nie amplitudy.

**Koszt SSVEP, do uczciwego zapisania:** wymaga patrzenia na migający obiekt, czyli wzroku i źródła migotania w polu widzenia. To osłabia argument „działa przy zamkniętych oczach" z `02_MECHANIZMY.md` sekcja 3.6 i zbliża paradygmat do konkurencji z eye trackingiem. **Rozstrzygnięcie należy do etapu 2 i musi być świadome, nie odziedziczone.**

---

## 2. Metody klasyczne

**CSP (Common Spatial Patterns)** — szuka takich kombinacji kanałów (filtrów przestrzennych), przy których różnica wariancji między dwiema klasami jest największa. Działa dobrze przy wielu kanałach; **przy dwóch–czterech kanałach traci sens**, bo nie ma czego kombinować. To jest bezpośredni problem formy zausznej.

**LDA (liniowa analiza dyskryminacyjna)** — prosty klasyfikator liniowy, standard dla P300 od dziesięcioleci. Odporny na małą liczbę prób.

**Geometria riemannowska macierzy kowariancji** — zamiast liczyć cechy, traktuje się macierz kowariancji sygnału jako punkt w przestrzeni zakrzywionej i klasyfikuje po odległościach w tej przestrzeni. Metoda z lat 2010., dziś jeden z najmocniejszych klasycznych punktów odniesienia.

**Kluczowy wynik porównawczy [wniosek, streszczenie]:** benchmark w *J Neural Eng* (2024, DOI 10.1088/1741-2552/ad6793) porównał sieci konwolucyjne (EEGNet, shallow ConvNet, deep ConvNet) z metodami riemannowskimi na zbiorach MOABB, w wariantach wewnątrzsesyjnym, międzysesyjnym i międzyosobniczym. Wynik: **metody riemannowskie osiągnęły wyższą średnią F1 przy różnych konfiguracjach kanałów i wymagały do dwóch rzędów wielkości mniej czasu treningu.** EEGNet wypadł stabilnie i wysoko, ale nie lepiej.

**[wniosek] Co to znaczy dla projektu — i jest to punkt, w którym oszczędza się miesiące:** w klasyfikacji EEG **sieci neuronowe nie biją metod klasycznych**, zwłaszcza przy małej liczbie kanałów i małej liczbie danych, czyli dokładnie w naszym reżimie. Budowanie osi projektu na uczeniu głębokim byłoby wejściem na pole zatłoczone (ostrzeżenie z sekcji 9.4 handbooka) **przy braku przewagi wydajnościowej**. Rekomendacja: klasyczne metody jako podstawa, sieć najwyżej jako punkt odniesienia.

To jest też zgodne z ograniczeniem z sekcji 1 handbooka — programowanie dopuszczone, ale nie ma z tego robić ćwiczenia z uczenia maszynowego. Tutaj literatura mówi to samo co użytkownik.

---

## 3. Gdzie leży poprawa z ostatnich pięciu lat

Handbook pytał wprost: w architekturze, w danych, w kalibracji między sesjami, czy w modelu językowym doklejonym na wyjściu.

**Odpowiedź: to zależy od zadania i te dwa przypadki trzeba rozdzielić.**

| Zadanie | Gdzie leży poprawa |
|---|---|
| **komunikacja (mowa, tekst)** | **w modelu językowym i w danych.** Patrz sekcja 5 |
| **sterowanie dyskretne (nasz przypadek)** | **w kalibracji i transferze, nie w architekturze** |

Dla drugiego wiersza: benchmark z sekcji 2 pokazuje, że architektura nie daje przewagi. Ruch jest w **redukcji kalibracji** — TFTL (PMID 39365711) deklaruje **zero prób kalibracyjnych** dla klasyfikacji międzyosobniczej i międzyzbiorowej; meta-uczenie i adaptacja w czasie testu idą w tę samą stronę `[wniosek, streszczenie]`.

**[wniosek] Konsekwencja dla nas, dwustronna:**
- **korzystna:** metody redukcji kalibracji są publiczne i można ich użyć jako narzędzia. Krótszy montaż i brak kalibracji to metryka użytkowa, czyli wariant 2 twierdzenia
- **ostrzegawcza:** to jest pole zatłoczone i **nie może być osią projektu**. Ktoś z laptopem i publicznym zbiorem robi to samo, bez sprzętu

---

## 4. Transfer międzyosobniczy i kalibracja

Problem: EEG różni się między osobami (anatomia, grubość czaszki, ustawienie elektrod) i między sesjami tej samej osoby (nawodnienie, ułożenie elektrody, pora dnia). Model wytrenowany wczoraj jutro działa gorzej.

Podejścia w literaturze `[wniosek, streszczenie]`: dostrajanie wstępnie wytrenowanych sieci, meta-uczenie pod szybką adaptację, uogólnianie dziedzinowe, transfer riemannowski (arXiv 2111.12071), adaptacja w czasie testu, ciągłe dostrajanie między sesjami.

**Do planu eksperymentalnego, pozycja obowiązkowa:** raportować wyniki **osobno dla wariantu wewnątrzsesyjnego, międzysesyjnego i międzyosobniczego**. Podanie samego wyniku wewnątrzsesyjnego jako „dokładności układu" jest najczęstszym sposobem zawyżenia liczby w tej dziedzinie — jurorzy znający temat pytają o to w pierwszej kolejności. Sekcja 4.5 regulaminu Explory (krytycyzm wobec własnych wyników) wymaga tego wprost.

---

## 5. Jak liczone są „słowa na minutę" — zadanie z sekcji 10.G

Handbook kazał sprawdzić szczególnie uważnie. Dwie odpowiedzi:

### 5.1 Ile z wpm robi model językowy

**Metryka jest liczona na wyjściu całego łańcucha, z modelem językowym włącznie.** Udział modelu jest duży i mierzalny `[wniosek, streszczenie]`:

- Willett i in. (Nature 620, 2023): **surowy błąd fonemowy sieci rekurencyjnej 19,7%** dla mowy wokalizowanej. Dopiero model 5-gramowy plus przeważanie dużym modelem językowym schodzi do jednocyfrowego błędu słownego. Autorzy interpretują to jako dowód, że wynik **nie jest nadmiernie zależny** od modelu językowego — warto zauważyć, że to jest ich interpretacja tej liczby, a nie jedyna możliwa
- **Brain-to-Text '24**: algorytm bazowy 9,7% WER, zwycięzca **5,8% WER** — **na tych samych danych neuronowych**. Całe 40% redukcji błędu pochodzi z warstwy dekodowania
- typowa architektura: sieć rekurencyjna → fonemy → hipotezy 5-gramowe → przeważanie dużym modelem językowym

**Wniosek [wniosek]:** deklarowane wpm jest własnością **łańcucha**, nie czujnika. Ten sam sygnał z lepszym modelem językowym daje inną liczbę.

### 5.2 Skąd biorą się „3 słowa na minutę" dla rozwiązań nieinwazyjnych

`[wniosek, streszczenie]`:

| System | Wydajność | Przeliczenie |
|---|---|---|
| speller P300 Farwella–Donchina (1988) | ~5 znaków/min | ~1 słowo/min |
| typowe spellery P300 | 1–5 znaków/min | ~0,2–1 słowo/min |
| spellery ogólnie, przegląd | 5–60 znaków/min przy 70–95% trafności | 1–12 słów/min |
| **SSVEP high-speed (Chen 2015)** | **~60 znaków/min** | **~12 słów/min** |

**Odpowiedź na pytanie handbooka:** liczba rzędu kilku słów na minutę **nie jest najgorszym przypadkiem** — jest środkiem szerokiego rozrzutu i odpowiada typowemu spellerowi P300. Ale **uczciwy górny koniec nieinwazyjnego to ~12 wpm**, nie 3. Zestawienie „62 inwazyjne vs 3 nieinwazyjne" wybiera z rozrzutu nieinwazyjnego dolny koniec, przy jednoczesnym wzięciu górnego końca inwazyjnego.

**Reguła operacyjna na etap 2, wynikająca wprost z tych dwóch punktów:**
> Każdą liczbę wydajności naszego układu podajemy w dwóch wersjach: **surowe dekodowanie** i **wynik z całą warstwą wspomagającą**. Baseline podajemy z zakresem, nie jedną liczbą, i mówimy, skąd wzięliśmy końce zakresu.

To nie jest ostrożność dla samej ostrożności. To jest jedyny sposób, żeby nasza liczba znaczyła to, co mówimy, że znaczy — dokładnie tak, jak żąda sekcja 10.G handbooka.

---

## 6. Projekt referencyjny — co da się powiedzieć bez abstraktu

Sekcja 9.2 handbooka każe ustalić, co konkretnie zostało zrobione, **żeby wiedzieć, którą ścieżką nie idziemy**.

**Abstraktu nie odczytałem** (baza zablokowana). Ale kontekst z sekcji 5 pozwala postawić hipotezę **falsyfikowalną**, i to jest lepsze niż nic:

`[domysł, do zweryfikowania po odblokowaniu sieci]` Jeżeli deklarowany jest skok z ~3 do ~65 wpm w rozwiązaniu nieinwazyjnym, to przy fizyce z `03_SCIANY_FIZYCZNE.md` **nie może to pochodzić z sprzętu** — czaszka nie zniknęła. Zostają trzy możliwości, wzajemnie niewykluczające się:
1. warstwa dekodowania z silnym modelem językowym (mechanizm z sekcji 5.1, gdzie zysk jest udokumentowany i duży)
2. dobór punktu odniesienia (3 wpm to dolny koniec rozrzutu, sekcja 5.2)
3. inna definicja „słowa na minutę" niż w pracach, z którymi jest to zestawiane

Wzmacnia to obserwacja z sekcji 9.2 handbooka: ta sama osoba wygrała rok wcześniej w kategorii BEHA za pracę o sieciach konwolucyjnych na rs-fMRI. **To jest profil osoby pracującej w dekodowaniu, nie w czujnikach.**

**Ścieżka, w którą nie wchodzimy:** komunikacja, dekodowanie językowe, duże modele na wyjściu. Decyzja C1 użytkownika (sterowanie, nie komunikacja) prowadzi w przeciwną stronę i **to jest zgodne z zakazem z sekcji 9.2** — nie dlatego, że unikamy porównania, tylko dlatego, że to inne zadanie.

---

## 7. Publiczne zbiory danych EEG

| Zbiór | Zawartość | Uwagi |
|---|---|---|
| **BCI Competition IV 2a** | 9 osób, 22 elektrody, 2 sesje, 288 prób 4-sekundowych, 4 klasy (lewa/prawa ręka, stopy, język) | standardowy punkt odniesienia dla wyobrażenia ruchu |
| **PhysioNet MI/ME** | **109 osób**, 64 kanały | największy klasyczny zbiór wyobrażenia ruchu |
| **MOABB** | agregat wielu zbiorów: 2–4 klasy, 3–128 kanałów, 9–109 osób | **infrastruktura do porównań**, nie pojedynczy zbiór. Kluczowa, jeśli chcemy porównywać się uczciwie |
| **ear-EEG sen** | **320 zapisów, 30 osób**, ear-EEG, część równolegle ze skalpem i aktygrafią | *Scientific Data*, 19 II 2025. Największy publiczny ear-EEG, jaki znalazłem |
| **cEEGrid, uwaga słuchowa** | **98 osób**, 16 kanałów, 63 próby × 30 s = 31,5 min na osobę | arXiv 2510.19174 |
| ICASSP 2024 Auditory EEG Challenge | dekodowanie mowy | — |
| EEG-Dash / EEGDash | **791 zbiorów** skatalogowanych, format gotowy do uczenia maszynowego | arXiv 2606.16041 — brama do reszty |
| speech decoding, artykulacja | otwarty zbiór | *Scientific Data* 2025 |

**[luka] Licencji nie sprawdziłem dla żadnego zbioru** — to wymaga otwarcia stron. Przed użyciem czegokolwiek w projekcie konkursowym licencja musi być sprawdzona, bo standardy etyczne Explory (sekcja 4.5) i zasady ISEF dotyczą także danych wtórnych.

**[wniosek] Obserwacja, która może być elementem wkładu projektu:** **nie znalazłem publicznego zbioru ear-EEG pod zadania sterowania.** Istniejące dotyczą snu i uwagi słuchowej. Jeżeli to się potwierdzi po przeszukaniu baz, opublikowanie własnego zbioru razem z projektem jest tanie i punktowane — pokazuje weryfikowalność, której nie ma żaden produkt komercyjny z `05_RYNEK.md` sekcja 6.
