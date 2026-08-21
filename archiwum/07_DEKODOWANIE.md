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

## 6. Projekt referencyjny — ABSTRAKT ODCZYTANY, hipoteza rozstrzygnięta

Sekcja 9.2 handbooka każe ustalić, co konkretnie zostało zrobione, **żeby wiedzieć, którą ścieżką nie idziemy**.

**[fakt] Pełny abstrakt odczytany** w bazie abstraktów Society for Science, 15 VIII 2026. Cytaty i pełny rozbiór: `08_KONKURENCJA_ISEF.md` sekcja 2.

**Moja hipoteza z poprzedniej wersji — trafiona w dwóch punktach z trzech, i chybiona w tym, który wydawał się najpewniejszy.**

| Co stawiałem | Jak jest |
|---|---|
| „nie może to pochodzić ze sprzętu" | **trafione.** Sprzęt to kupione konsumenckie EEG za **1 800 USD**. Nic nie zostało zbudowane |
| „zysk siedzi w warstwie dekodowania z silnym modelem językowym" | **chybione co do mechanizmu.** Zysk nie pochodzi z modelu językowego doklejonego na wyjściu, tylko ze **zmiany zadania**: „resolving intent directly, instead of spelling messages out letter by letter" |
| „dobór punktu odniesienia — 3 wpm to dolny koniec rozrzutu" | **chybione i wycofuję ten zarzut.** Baseline 3 wpm to **klasyczny speller uruchomiony przez tego samego autora, na tym samym sprzęcie, jako warunek kontrolny**, w 111 randomizowanych i kontrbalansowanych próbach. To jest uczciwie zmierzone odniesienie wewnętrzne, a nie wybrana z literatury liczba |
| „inna definicja słowa na minutę" | nierozstrzygnięte, ale nieistotne przy baseline wewnętrznym |

**Wniosek, który trzeba zapisać wprost, bo jest niewygodny:** podejrzewałem tę pracę o naciągnięcie punktu odniesienia i **nie miałem racji**. Metodologicznie jest ona mocniejsza niż moje wobec niej zastrzeżenie: warunek kontrolny na tym samym sprzęcie, randomizacja, kontrbalansowanie, replikacja na drugiej, naiwnej grupie, poprawka na wielokrotne porównania (`q` zamiast `p`), rozmiar efektu (Cohen's d = 2,9) i **test mechanizmu przez podwójną dysocjację**, a nie tylko test wyniku.

Obserwacja z sekcji 9.2 handbooka pozostaje trafna: profil osoby pracującej w dekodowaniu, nie w czujnikach. Rok wcześniej Grand Award w BEHA za sieci konwolucyjne na rs-fMRI.

**Ścieżka, w którą nie wchodzimy, sformułowana precyzyjniej niż dotąd:** rozstrzyganie intencji z małego zbioru zamiast literowania, mierzone w słowach na minutę, na kupionym sprzęcie, z twierdzeniem o uniwersalnym prawie dla interfejsów ograniczonych pasmem.

**Ostrzeżenie do pilnowania przez cały etap 2, ostrzejsze niż dotychczasowe:** „sterowanie dyskretne z ośmioma komendami" i „rozstrzyganie intencji z ośmiu możliwości" to **jest ta sama rzecz opisana dwoma językami**. Granicy nie pilnuje temat, tylko to, że naszym produktem jest **sprzęt i pomiar toru analogowego**, a metryką dokładność i ITR — nie słowa na minutę.

**Co wolno skopiować, i co należy:** strukturę planu eksperymentalnego. Zakaz z sekcji 9.2 dotyczy rozwiązania, nie rzemiosła. Trzy warunki z `04` sekcja 3 idą w tę stronę i mają teraz potwierdzenie, że taka struktura wygrywa w tej kategorii.

---

## 7. Publiczne zbiory danych EEG

| Zbiór | Zawartość | Uwagi |
|---|---|---|
| **BCI Competition IV 2a** | 9 osób, 22 elektrody, 2 sesje, 288 prób 4-sekundowych, 4 klasy (lewa/prawa ręka, stopy, język) | standardowy punkt odniesienia dla wyobrażenia ruchu |
| **PhysioNet MI/ME** | **109 osób**, 64 kanały | największy klasyczny zbiór wyobrażenia ruchu |
| **MOABB** | agregat wielu zbiorów: 2–4 klasy, 3–128 kanałów, 9–109 osób | **infrastruktura do porównań**, nie pojedynczy zbiór. Kluczowa, jeśli chcemy porównywać się uczciwie |
| **ear-EEG, BCI: ERP + SSVEP, w ruchu** | **24 osoby**; 32-kan. skalp **+ 14-kan. ear-EEG + 4-kan. EOG + 9-kan. IMU**; cztery prędkości: 0 / 0,8 / 1,6 / 2,0 m/s; dwa paradygmaty BCI dla każdej | **Lee i in., *Sci Data* 8:315 (2021), PMID 34930915. `[fakt, abstrakt odczytany]` NAJWAŻNIEJSZA POZYCJA W TEJ TABELI — patrz sekcja 7.1** |
| **ear-EEG sen** | **320 zapisów, 30 osób**, ear-EEG, część równolegle ze skalpem i aktygrafią | *Scientific Data*, 19 II 2025 |
| **cEEGrid, uwaga słuchowa** | **98 osób**, 16 kanałów, 63 próby × 30 s = 31,5 min na osobę | arXiv 2510.19174 |
| ICASSP 2024 Auditory EEG Challenge | dekodowanie mowy | — |
| EEG-Dash / EEGDash | **791 zbiorów** skatalogowanych, format gotowy do uczenia maszynowego | arXiv 2606.16041 — brama do reszty |
| speech decoding, artykulacja | otwarty zbiór | *Scientific Data* 2025 |

**[luka] Licencji nie sprawdziłem dla żadnego zbioru** — to wymaga otwarcia stron z danymi, nie samych artykułów. Przed użyciem czegokolwiek w projekcie konkursowym licencja musi być sprawdzona, bo standardy etyczne Explory (Załącznik nr 1) i etyka ISEF dotyczą także danych wtórnych. Regulamin ISEF wymaga osobno: *„Confidential communications, as well as patents, copyrights, and other forms of intellectual property must be honored."*

### 7.1 Twierdzenie z poprzedniej wersji: OBALONE

Poprzednia wersja tej sekcji twierdziła: „**nie znalazłem publicznego zbioru ear-EEG pod zadania sterowania.** Istniejące dotyczą snu i uwagi słuchowej" — i proponowała opublikowanie własnego zbioru jako element wkładu.

**[fakt] To jest nieprawda.** Zbiór Lee i in. (*Sci Data* 8:315, 2021) zawiera 14-kanałowy ear-EEG z paradygmatami **ERP i SSVEP**, czyli wprost pod sterowanie, na 24 osobach — plus równoległy EOG i pomiar ruchu. `KOREKTY.md` **K-027**.

**Trzy konsekwencje, dwie dobre:**

1. **Teza „własny zbiór to tani wyróżnik" — osłabiona.** Pole nie jest puste, więc publikacja własnego zbioru jest dobrą praktyką, a nie argumentem konkursowym. Nie budować na tym twierdzenia.
2. **Warstwę dekodowania da się rozwijać, zanim powstanie sprzęt.** To jest realna zmiana w planowaniu jesieni 2026: nauka projektowania PCB nie musi blokować pracy nad warstwą 4 z sekcji 9.4 handbooka. Dane są, są darmowe i mają właściwe paradygmaty.
3. **Zbiór daje punkt odniesienia dla własnego urządzenia** — te same paradygmaty, znany materiał, uczciwe porównanie „mój tor analogowy wobec zbioru referencyjnego". Tego rodzaju porównanie punktuje wprost w sekcji Execution arkusza inżynierskiego ISEF.

**Dlaczego zapisuję to tak dokładnie:** to była pozycja, na której budowałem element wkładu projektu, oparta na jednym nieudanym przeszukaniu. Ten sam wzorzec co K-009 i K-028 — twierdzenie o nieistnieniu postawione na podstawie tego, że czegoś nie znalazłem.
