# 06 — Ryzyka, plany awaryjne i drabinka zejść

**Stan na 21 sierpnia 2026.**

Każde ryzyko w trzech wymiarach: **prawdopodobieństwo**, **sterowalność** (na ile wynik zależy od autora), **koszt porażki**. Dwie pozycje o tej samej szansie mogą być zupełnie różnymi decyzjami.

---

## Tabela zbiorcza

| # | Ryzyko | P | Sterowalność | Koszt | Kiedy się rozstrzyga |
|---|---|---|---|---|---|
| **R1** | słaba odpowiedź SSVEP u autora | **20–30%** | niska | **bardzo wysoki** | **X 2026, przesiew E0 — 20 min** |
| **R2** | własny tor analogowy nie osiąga użytecznego szumu | 40% | wysoka | średni | II 2027 |
| **R3** | brak sprzętu pomiarowego do charakterystyki toru | **20%** | średnia | **niski** | **przeszacowane, K-072** |
| **R4** | efekt odległości odniesienia < 3 pp — T1 upada | **25%** | zerowa | wysoki | XI 2026 (na cudzych danych: już częściowo znany) |
| **R5** | ktoś publikuje tę samą oś przed nami | 10–20% | zerowa | **niski** | ciągle |
| **R6** | komisja IRB przy szkole nie powstaje | 30% | średnia | niski | XII 2026 |
| **R7** | poślizg: druga wersja płytki wypada po V 2027 | 35% | wysoka | wysoki | III 2027 |
| **R8** | ~~nowa oś zajęta w bazach nieprzeszukanych~~ → **oś JEST zajęta w wersji szerokiej** | **ziściło się** | — | średni | **ZAMKNIĘTE 16 VIII: K-074** |
| **R9** | moduł nie mieści się w granicy gabarytu | 25% | wysoka | średni | I 2027 |
| **R10** | brak opiekuna z tytułem / Qualified Scientist | 20% `[luka]` | średnia | **bardzo wysoki** | XI 2026 |
| **R12** | **elektroda odniesienia w module siedzi nad móżdżkiem i mięśniem karku** | `[domysł]` **40–60%** | średnia | **niski dla twierdzenia, średni dla gabarytu** | pierwsza własna sesja, wiosna 2027 |
| **R14** | **wynik wychodzi NUDNY — poprawny, ale dokładnie taki, jakiego każdy się spodziewał** | `[domysł]` **35–45%** | **wysoka** | **średni dla noty, wysoki dla rubryki Creativity** | VI 2027, po kampanii |
| **R13** | **montaż zredukowany przestaje działać u części osób całkowicie, nie stopniowo** | `[fakt]` **39% u Fodora 2025** | średnia | **wysoki dla demonstracji** | **X 2026, przesiew E0** |
| **R11** | ~~użytkownik odrzuca zmianę osi~~ | — | — | — | **ZAMKNIĘTE 16 VIII: wariant C** |

---

## R1 — słaba odpowiedź SSVEP u autora

**Najgroźniejsze ryzyko w projekcie i najmniej sterowalne.**

`[fakt, dane Kołodzieja]` Rozrzut dokładności bazowej między osobami: **od 40,0% (S08) do 95,6% (S12)** przy trzech celach. To nie jest szum pomiarowy — to jest różnica fizjologiczna. Odsetek osób, u których SSVEP praktycznie nie działa („BCI illiteracy"), podaje się w literaturze rzędu **10–30%** `[wniosek, jedno źródło pośrednie — do domknięcia]`.

Cały plan jednoosobowy do maja 2027 stoi na założeniu, że autor nie jest takim przypadkiem. **Założenie niesprawdzone.**

**Plan awaryjny — i jest tani:**
1. **Test wykonać jako pierwszy pomiar w ogóle**, w torze A na kupionej platformie, październik 2026. Nie po zbudowaniu płytki. Koszt testu: jedno popołudnie na sprzęcie, który i tak kupujemy
2. jeżeli odpowiedź jest słaba: **zmiana osoby odniesienia** — pomiary główne na kimś innym, ale to **wymaga komisji IRB** i przesuwa R6 z „niski koszt" na „blokujący". Dlatego rozmowa z dyrekcją musi się odbyć jesienią 2026 **niezależnie od tego, czy wydaje się potrzebna**
3. jeżeli odpowiedź jest słaba u kilku osób: paradygmat SSVEP zostaje, ale twierdzenie T1 przechodzi na **SNR w paśmie bodźca** zamiast dokładności klasyfikacji — wielkość fizyczna, mierzalna nawet przy niskiej dokładności, i wciąż zależna od odległości odniesienia

**Uwaga:** punkt 3 jest zejściem o poziom w ambicji i zapisuję to jako zejście, zgodnie z `METODA.md` §11. Poświęcone: metryka zrozumiała dla laika (ITR) na rzecz metryki zrozumiałej dla jurora od elektroniki (SNR). W kategorii **EBED** ta zamiana kosztuje mniej niż w ENBM.

---

## R2 — własny tor nie osiąga użytecznego szumu

**Prawdopodobieństwo wysokie i to jest normalne.** Pierwsza własna płytka dla sygnałów mikrowoltowych rzadko działa za pierwszym razem.

**Plan awaryjny, w kolejności:**
1. **rezerwa 30% w budżecie i v2 w harmonogramie na marzec–kwiecień 2027** — wpisane, nie doproszone (`03_SPRZET.md` §5.2)
2. jeżeli v2 też zawodzi: **twierdzenie T1 nie wymaga własnego toru.** Wymaga *jakiegoś* toru o znanej charakterystyce i wymiennych wiązek elektrodowych. Kupiona platforma z własnym zestawem elektrod obsługuje E2, E3 i E5 w całości
3. co się wtedy traci: kontrybucja sprzętowa i rubryka „własny front-end". Co zostaje: **pomiar, twierdzenie, wynik.** Projekt schodzi z „własny sprzęt plus pomiar" na „pomiar na sprzęcie kupionym z własną częścią elektrodową" — czyli mniej więcej tam, gdzie leżał projekt referencyjny ENBM074, który za to dostał drugie miejsce na ISEF

**To jest realny plan B, nie pocieszenie.** Dlatego kolejność z `03_SPRZET.md` §4.1 stawia platformę kupioną **przed** własną płytką, a nie po niej.

---

## R3 — brak sprzętu pomiarowego do E1

**Ryzyko przeszacowane — obniżam z 50% na 20%, K-072.** Użytkownik odpowiedział na B3: ma **regulowaną stację lutowniczą i multimetr**. Ważniejsze jest jednak to, że moje sformułowanie wymagania było błędne.

`[fakt]` Szum wejściowy toru mierzy się **samym torem**, nie przyrządem zewnętrznym — zwarte wejście, RMS z próbek przetwornika 24-bitowego. Oscyloskop hobbystyczny ma szum własny rzędu setek mikrowoltów, czyli **tysiąc razy większy** od mierzonej wielkości, i do tego pomiaru jest bezużyteczny. Przyrząd zewnętrzny jest potrzebny **jako źródło znanego sygnału**.

**Realny brak sprowadza się do dwóch pozycji za łącznie 280–680 zł** (dzielnik precyzyjny do zlutowania oraz generator funkcyjny) — `03_SPRZET.md` §4. Oscyloskop schodzi z „niezbędny" na „przydatny do debugowania", czyli pierwszy kandydat do pożyczenia.

**Plan awaryjny:**
1. **droga przez brata** — pracuje w firmie produkującej precyzyjną elektronikę; to jest zasób jednorazowy i trzeba go zaplanować, nie zużyć przypadkiem (`METODA.md` §1). Zaplanować na **luty 2027**, na gotową płytkę v1, nie wcześniej
2. **obejście bez oscyloskopu**, opisane w `archiwum/03_SCIANY_FIZYCZNE.md` §6: szum toru mierzy się **samym torem** — zewrzeć wejście przez rezystor i policzyć RMS z zarejestrowanych próbek. Przetwornik 24‑bitowy jest tu przyrządem. Tego nie da się użyć do pomiaru CMRR przy 50 Hz, ale **da się do szumu i dryfu**
3. co zostaje niezmierzone bez sprzętu: CMRR i jitter. **Obie liczby można podać jako katalogowe z ADS1299 z jawnym zaznaczeniem, że nie są własnym pomiarem.** Jest to słabsze i tak trzeba to opisać

---

## R4 — efekt okazuje się mały, T1 upada

**Częściowo już rozstrzygnięte i to na korzyść.** Na cudzych surowych danych efekt wynosi **9,3–24,5 pp** (`12_REANALIZA.md` §5). Żeby T1 upadło, własny pomiar musiałby się rozejść z tamtym o rząd wielkości.

**Zastrzeżenie dołożone 16 VIII 2026, i jest realne** `[luka]`: te liczby obowiązują dla metod **bez fazy** (FBCCA, CCA, cechy FFT). **TRCA sprawdzone i na tamtym zbiorze niewykonalne** — faza SSVEP nie jest zsynchronizowana z oknami (`12_REANALIZA.md` §6B). Możliwe, że filtr przestrzenny uczony na osobie odzyskuje część straty montażu zwartego. **Podnosi to prawdopodobieństwo R4 z 15% na 25%** i jest głównym powodem, dla którego własne stanowisko musi zapisywać moment zapłonu bodźca od pierwszej sesji.

**Plan awaryjny:** jeżeli efekt wyjdzie mały, to znaczy, że **moduł zwarty działa prawie tak dobrze jak montaż literaturowy** — czyli twierdzenie odwraca znak i staje się **lepszą wiadomością dla urządzenia**: „gabaryt mieszczący się w module nie kosztuje przepustowości". To też jest wynik, też jest publikowalny i **jest korzystniejszy z punktu widzenia produktu**.

`[wniosek]` **T1 jest tak skonstruowane, że nie ma wyniku, który by je unieważnił** — jest tylko wynik, który zmienia jego znak. To jest ta sama własność, którą miało poprzednie twierdzenie, i to jest powód, dla którego oba przeszły audyt.

---

## R5 — ktoś publikuje pierwszy

> **OBNIŻONE 21 VIII 2026 z 10–20% na 5–10% — `METODA.md` §6 i §9.** Podstawa nie jest już oszacowaniem profilu grupy, tylko pomiarem: `[fakt, graf cytowań Semantic Scholar]` praca Kołodziej i in. 2026 ma **po siedmiu miesiącach jedno cytowanie**, i jest nim koreański speller (PMID 41978050), nie kontynuacja sprzętowa. Do tego zero nowych prac obu autorów w PubMed (sprawdzone imiennie). **Mocniejsza przesłanka ogólna:** dwie jedyne prace, które kiedykolwiek porównały montaże dla SSVEP — **Wu i Su 2014 (16 cytowań w dwanaście lat)** i **Diez i in. 2010 (23 cytowania w szesnaście lat)** — **nie mają ani jednej kontynuacji w stronę geometrii montażu**. Pole otwarto dwa razy i dwa razy nikt nie wszedł.

Ocena z `METODA.md` §10 pozostaje: grupa z Politechniki Warszawskiej to **zespół przetwarzania sygnałów, bez dorobku sprzętowego**, więc ryzyko, że sami wykonają wersję sprzętową, to **10–20%**.

**Dla nowej osi ryzyko jest jeszcze niższe** `[wniosek]`: pytanie o odległość odniesienia jest pytaniem konstrukcyjnym, nie algorytmicznym, i nie leży w ich profilu ani w profilu żadnego nazwanego aktora, którego znam.

**Plan awaryjny — bez zmian i nadal wystarczający:** twierdzenie jest pomiarowe, więc cudza publikacja go nie unieważnia. Degradacja jest z „nowe" na „potwierdzone niezależnie". **Zakaz słowa „pierwszy" w materiałach zgłoszeniowych obowiązuje bez zmian (K-044).**

**Monitorowanie:** PubMed po autorach `Kolodziej M`, `Majkowski A`, plus zapytania o odległość odniesienia z `12_REANALIZA.md` §11, **co dwa miesiące**.

---

## R6 — komisja IRB nie powstaje

> **STATUS ZMIENIANY DWA RAZY 21 VIII 2026, końcowo: PLAN AWARYJNY.** Rano podniesiony na **warunek wstępny**, bo plan trzech historii wyglądał na wymagający własnych wywiadów. Wieczorem, po wyjaśnieniu autora i odczytaniu zwolnienia dla **relacji już opublikowanych** (`09_FORMALNOSCI.md` §1.2), **obniżony z powrotem.** `[wniosek]` **Przy relacjach opublikowanych IRB nie jest do narracji potrzebne w ogóle.** Wraca jako warunek wstępny wyłącznie wtedy, gdy autor zdecyduje się na własne rozmowy albo na badanie innych osób po złym E0.

Skład wymagany: **nauczyciel inny niż opiekun projektu + dyrektor lub wicedyrektor + pielęgniarka szkolna lub psycholog** (K-022). Najdłuższy proces w harmonogramie formalnym i **jedyny zależny od osób trzecich**.

Użytkownik zgłosił, że z formalnościami nie będzie problemu, i pozycja zeszła z listy ryzyk. **Wpisuję ją z powrotem, ale z niskim kosztem** — bo po R1 wiadomo, że IRB może się okazać potrzebna nie „na wszelki wypadek", tylko jako **plan awaryjny na słabą odpowiedź SSVEP u autora**. To zmienia jej wagę.

**Plan awaryjny:**
1. **mail do FZT jako pierwszy krok** — jeżeli organizator prowadzi SRC pełniące funkcję IRB, punkt odpada w całości. Jedno pytanie, jesień 2026
2. jeżeli komisji nie da się powołać: cały plan pomiarowy zostaje na jednej osobie. **To jest wykonalne** — E1…E5 są zaprojektowane jako wewnątrzosobnicze. Traci się uogólnienie na populację i rubrykę „testowane na wielu osobach"

---

## R7 — poślizg harmonogramowy

**Najbardziej prawdopodobny konkretny scenariusz:** v1 płytki gotowa w lutym, błędy wykryte w marcu, v2 zamówiona w kwietniu, dociera w maju — **czyli w miesiącu startu formalnej kampanii ISEF**. Kampania zaczyna się od czekania na przesyłkę.

**Plan awaryjny:**
1. **kampania nie musi startować na własnym sprzęcie.** Okno to maj 2027 – maj 2028, dwanaście ciągłych miesięcy. Można zacząć w maju na platformie kupionej i przejść na własną w lipcu, w środku okna
2. **zamawiać dwie serie PCB naraz**, jeżeli budżet pozwala — v1 w dwóch wariantach różniących się tym, co najbardziej niepewne (rozkład masy, ekranowanie). Koszt drugiej serii przy tym samym zamówieniu jest ułamkiem kosztu osobnego cyklu
3. **28 II 2027 nie jest zagrożone** — zgłoszenie do Explory nie wymaga gotowego projektu (§4.1 regulaminu)

---

## R8 — nowa oś zajęta w bazach, których nie przeszukałem

> **ZISCIŁO SIĘ, 16 VIII 2026 wieczorem — K-074.** OpenAIRE (baza, której limit wcześniej mnie blokował, obeszta przez inny indeks) pokazała **siedem prac o doborze montażu i odniesienia dla SSVEP, od 2005 roku**, w tym pomiar dokładnie naszej zmiennej (EMBC 2010: dwubiegunowy 80,1% wobec jednobiegunowego 74,5%) i pracę z 2026 z naszym zdaniem problemowym w tytule. **Przyczyna przeoczenia: szukałem własnym słownictwem, nie słownictwem dziedziny.** Ryzyko podniesione z 10–15% na **25–40%** dla wąskiej wersji osi. Rozbiór: `METODA.md`.

**Historia pozycji — zamknięte w trzech czwartych tego samego dnia.** Pierwotnie dla nowej osi miałem tylko PubMed — czyli dokładnie ten błąd, który `METODA.md` §5 wymienia jako **wzorzec numer 1**: zmiana konfiguracji projektu bez powtórzenia audytu prior art. Zamiast zapisać go jako zadanie na później, domknąłem go od razu.

**Stan po 16 VIII 2026** (`12_REANALIZA.md` §11): **PubMed, Crossref i arXiv przeszukane — nowa oś niezajęta.** Znaleziona jedna nowa pozycja o formie urządzenia (arXiv 2509.15449, elektroda douszna dla SSVEP, pięciu badanych), która osi nie zajmuje.

> **ZAMKNIĘTE 18 VIII 2026, `05_STAN_WIEDZY.md` §2.8 i §2.1.** **Patenty przeszukane** (Google Patents, pięć zapytań): żaden patent nie zajmuje pomiaru — patenty chronią konstrukcje, a te są chronione gęsto (InteraXon, Neurable, Mybrain, Brainpatch, Meta, Cognixion, Georgia Tech, UPenn). **Skutek: nie wolno opisać modułu jako wynalazku.** **Chińska literatura czasopiśmiennicza otwarta 18 VIII po południu przez CQVIP** (CNKI nadal zrywa połączenie) — wąska oś **niezajęta również tam**, `36` §4.2. **Literatura nieanglojęzyczna przeszukana po raz pierwszy** — i tam leżał wynik zabijający szeroką wersję twierdzenia: **Li X. i in., PMID 40566767, 2025, po chińsku** — noszalny interfejs SSVEP, 94,10% przy 40 celach, ITR 115,25 bit/min, *„no significant difference"* wobec warunków laboratoryjnych. **K-077.**

~~`[luka]` **Nieprzeszukana zostaje baza patentów** dla nowej osi, oraz literatura nieanglojęzyczna.~~

**Plan awaryjny:** patenty do sprawdzenia przed jakimkolwiek zakupem, czyli przed X 2026. Jeżeli oś okaże się zajęta, wraca pytanie o oś — ale **sprzęt z `03_SPRZET.md` się nie zmienia**, więc koszt jest w dokumentacji, nie w pieniądzach.

---

## R9 — gabaryt

Granica twarda: **nic zbliżonego do opaski przechylonej na tył głowy**, żadnej konstrukcji nad czubkiem głowy ani przez czoło (`11_EWOLUCJA.md` decyzja 3).

**Napięcie, które reanaliza ujawniła:** najlepsze odniesienie może leżeć na wyrostku sutkowatym (za uchem, ~7 cm od Oz) albo na płatku ucha (~10 cm). **Wyprowadzenie odniesienia za ucho to cienki przewód przy głowie, który tabela gabarytowa dopuszcza wprost** („cienki przewód lub łuk między modułami, przy głowie" — przechodzi). Zausznik odrzucony w K-036 był **drugim miejscem elektrod aktywnych**, a nie pojedynczym odniesieniem.

`[wniosek]` **To nie jest złamanie decyzji 2, tylko jej doprecyzowanie**, i wymaga potwierdzenia użytkownika — pytanie P2 w `archiwum/18_PYTANIA_ETAP2.md`.

**Uzupełnienie z 21 VIII 2026 (K-105):** granica gabarytowa dotyczy **konfiguracji demonstracyjnej** — moduł plus dwa przewody do O1 i O2. **Konfiguracja pomiarowa ma osiem elektrod i siedem wyprowadzeń** i granicy gabarytowej nie podlega, bo jest aparaturą, a nie wyrobem (`03_SPRZET.md` §4.1). `[wniosek]` Ryzyko, którego to nie zmniejsza: **zdjęcie z sesji pomiarowej nie nadaje się na plakat**. Materiał wizualny robi się osobno, w konfiguracji demonstracyjnej, i to jest pozycja w harmonogramie, a nie rzecz do zrobienia przy okazji.

**Plan awaryjny:** kolejność ustępstw z `11_EWOLUCJA.md` decyzja 3 — najpierw gabaryt i widoczność, potem wygoda, **nigdy hełm**.

---

## R10 — opiekun naukowy

`[luka]` Pytanie B5 bez odpowiedzi od etapu 1. Formalnie: **magister wystarcza na role Adult Sponsor i Direct Supervisor**, a Qualified Scientist **nie wymaga doktoratu** — dopuszczalne jest „extensive experience and expertise" (K-020, K-021).

**Koszt porażki bardzo wysoki, bo dyskwalifikuje niezależnie od jakości projektu.** Prawdopodobieństwo niskie, bo próg formalny okazał się niższy, niż zakładał handbook.

**Plan awaryjny:** pisemna zgoda opiekuna szkolnego, jesień 2026. **Tanie, bez terminu, zdejmuje ryzyko** — i dlatego nie ma powodu z tym czekać.

---

## R11 — ZAMKNIĘTE 16 VIII 2026

**Rozstrzygnięcie użytkownika: wariant C** — osi nie zamykamy teraz, sprzęt obsługuje obie, wybór następuje po pierwszych własnych pomiarach (`11_EWOLUCJA.md` decyzja 5).

Użytkownik zażądał przy tym sprawdzenia, czy kanał szczękowy w ogóle daje dość, żeby być osią. **Sprawdzone, `12_REANALIZA.md` §6A: nie daje, sufit +0,6 pp, p = 0,166.** Skutek: elektroda szczękowa wychodzi ze sprzętu, kanał mięśniowy przenosi się na kark, **sprzęt się upraszcza**.

**Ryzyko rezydualne, które z tego zostaje i jest realne** `[wniosek]`: wariant C oznacza, że **do pierwszych własnych pomiarów projekt nie ma jednego zdania twierdzenia**. Do zgłoszenia Explory (28 II 2027) zdanie musi istnieć. Pierwsze pomiary w torze A planowane są na **X 2026**, czyli z czteromiesięcznym zapasem — ale jeżeli tor A się opóźni, zgłoszenie pisze się na osi wybranej bez pomiaru, czyli dokładnie tak, jak nie chcemy.

**Plan awaryjny:** jeżeli do **31 XII 2026** nie ma własnych pomiarów, oś wybieramy **wariantem A** (odległość odniesienia) na podstawie samej reanalizy i zapisujemy, że wybór był bez własnego pomiaru. Reanaliza jest do tego wystarczającą podstawą — efekt 9–24 pp wobec 0,6 pp nie jest bliskim rozstrzygnięciem.

---

## R12 — okolica podpotyliczna nie jest elektrycznie cicha

**Dopisane 21 VIII 2026 po pytaniu użytkownika „dlaczego nikt tego nie tyka". Rozbiór: `05_STAN_WIEDZY.md`.**

Trzech nazwanych mieszkańców miejsca, w którym musiałaby usiąść elektroda odniesienia modułu:

1. `[fakt, PMID 12948787]` **mięśnie karku** — Goncharova i in. 2003: *„EMG contamination is greatest at the **periphery of the scalp** near the active muscles"*, a widmo EMG ma *„peaks in the **beta** frequency range that resemble EEG beta peaks"*
2. `[fakt, PMID 29886131]` **móżdżek** — Todd, Govender, Colebatch 2018: elektrody nad tylnym dołem czaszki (CB1/CB2, ~5% poniżej PO9/PO10) rejestrują ECeG, a *„**visual stimulation (…) was effective in increasing the high-frequency power in CB electrodes, including in beta (14–30 Hz)** and gamma"*. **Odniesienie może samo nieść sygnał reagujący na bodziec, w paśmie drugich harmonicznych SSVEP**
3. `[fakt, pomiar własny]` **gładkie pole SSVEP** — `12_REANALIZA.md` §5, plus nowa liczba: montaż zwarty kosztuje **2,7–3,6 dB SNR** w prążku bodźca (`analiza/harmoniczne.py`)

**Dlaczego to nie zabija twierdzenia:** brzmi ono *„wyznaczam najmniejszą odległość, przy której przepustowość się nie załamuje"*. Jeżeli ta odległość wypadnie **powyżej inionu albo za uchem — to jest wynik, nie porażka.** Traci się gabaryt, nie pomiar.

**Poprawka planu z 21 VIII 2026 (P26) obniża to ryzyko, zanim się ziści:** kandydat na odniesienie zwarte przeniesiony z okolicy podpotylicznej na **POz, ~3,5 cm POWYŻEJ Oz** — czyli **powyżej inionu, poza zasięgiem mięśnia karku i tylnego dołu czaszki**. Wariant w dół zostaje jako **warunek porównawczy**, a nie jako podstawowy. `05_STAN_WIEDZY.md` §3.

**Plan awaryjny — już istnieje:** decyzja 6 (`11_EWOLUCJA.md`) dopuszcza wyprowadzenie odniesienia cienkim przewodem na wyrostek sutkowaty. Zmienia się jedno położenie elektrody i jedno zdanie o gabarycie.

**Test rozdzielający, koszt zerowy (P23):** raportować SNR **osobno dla f₀ i 2f₀** przy każdym położeniu odniesienia. Strata rosnąca z harmoniczną wskazuje na zanieczyszczenie odniesienia; strata niezależna od częstotliwości — na gładkie pole. `[luka]` Na danych Kołodzieja testu **nie da się wykonać** — przy bodźcach 7/8/9 Hz drugiej harmonicznej praktycznie nie ma (SNR −0,04 do +0,16 dB we wszystkich montażach). Zestaw 8,0–17,8 Hz z `16` §3.2 daje harmoniczne w paśmie 16–35,6 Hz i test umożliwia.

---

## R14 — wynik nudny. Ryzyko, którego rejestr nie miał

**Dopisane 21 VIII 2026 po pytaniu autora, czy nie lepiej szukać projektu o większym potencjale. K-115.**

**Czym to NIE jest.** `[fakt]` R4 pokrywa scenariusz *„efekt za mały, twierdzenie upada"*. **Nie pokrywa scenariusza odwrotnego: efekt wychodzi dokładnie taki, jakiego wszyscy się spodziewali.**

**Na czym polega.** `[wniosek]` Zdanie *„odniesienie o 3,5 cm kosztuje 9 punktów procentowych"* jest uczciwą, dobrze zmierzoną liczbą — **i nikogo nie zaskoczy.** Bliżej znaczy gorzej; tego się spodziewano. Projekt zbiera wtedy pełnię punktów w `Execution` i `Design and Methodology`, a **traci w `Creativity & Potential Impact`, która na arkuszu ISEF waży 20 punktów na 100 i jest już dziś najsłabszą rubryką tego projektu (12–14/20).**

**Dlaczego to jest ryzyko sterowalne, w przeciwieństwie do R1 i R4.** `[wniosek]` **Odpowiedzią nie jest zmiana projektu, tylko podniesienie rangi testu mechanizmu.**

`[fakt, `04_PLAN_POMIAROWY.md` §3.3a]` Model falowy daje **przewidywanie 1: strata musi zmieniać się z częstotliwością bodźca**, bo zależy od `d/λ`, a nie od samego `d`. **Model „gładkiej plamy" nie przewiduje żadnej zależności od częstotliwości.** To jest test rozstrzygający między dwoma obrazami świata — i **jedyna rzecz w projekcie, której wynik nie jest z góry oczywisty dla nikogo.**

**A rodzina R-C jest dziś EKSPLORACYJNA**, bo przy 32 porównaniach potrzeba **277 prób na częstotliwość**, a osiem sesji daje **240. Brakuje 15%.**

### Poprawka: E2 rozszerzone do dziesięciu sesji — pozycja warunkowa

| | zaplanowane | **rozszerzone** |
|---|---|---|
| sesje | 8 | **10** |
| prób na częstotliwość | 240 | **300** wobec wymaganych 277 |
| **rodzina R-C** | **eksploracyjna** | **KONFIRMACYJNA** |
| czas w kalendarzu (co drugi dzień) | 16 dni | **20 dni** |
| koszt pracy | — | **~4–6 h plus 4 dni** |

`[wniosek]` **Cztery dni i dwa popołudnia zamieniają najciekawszą rzecz w projekcie ze „zgodności kierunku" w potwierdzony test mechanizmu.** Arkusz ISEF mówi wprost: *„Judges should place emphasis on **research outcomes and analysis** in evaluating creativity"* — a **mechanizm przewidziany ilościowo przed pomiarem jest najmocniejszą rzeczą, jaką projekt inżynierski może pokazać.**

**Status: warunkowa.** Uruchamiana, **jeżeli kalendarz na to pozwoli** — decyzja przy planowaniu kampanii, **kwiecień 2027**. `[wniosek]` **Nie wolno jej uruchomić kosztem rodzin konfirmacyjnych R-A i R-B ani kosztem materiału półfinałowego.**

**Druga pozycja z tej samej półki:** **E6** (warunek bez sterowania wzrokiem, 11–15 h, `05_STAN_WIEDZY.md` §7.6) — odłożony 21 VIII **z powodu czasu, nie wartości.** Zabija zarzut o kamerkę demonstracją zamiast argumentem i daje **drugi mały wynik pomiarowy.** Przy nadwyżce godzin wraca jako pierwszy.

---

## R13 — montaż zredukowany bywa nie „gorszy", tylko niedziałający

`[fakt]` **Fodor, Cantürk, Heisenberg, Volosyak 2025**, Brain Sci 15(6):549, **PMID 40563723**, 38 osób, badanie **online**, c-VEP, cztery cele. Redukcja z 16 elektrod do 6 (PO3, POz, PO4, O1, Oz, O2), odniesienie **cały czas na Cz**:

| Warunek | Dokładność | ITR [bit/min] | **Dla ilu z 38 osób układ w ogóle działał** |
|---|---|---|---|
| 16 elektrod | 95,62 ± 8,31% | 49,33 ± 17,07 | **38** |
| 6 elektrod, bez douczenia | 94,18 ± 8,00% | 37,79 ± 18,68 | **18** |
| 6 elektrod, po douczeniu | 98,01 ± 3,21% | 48,39 ± 14,24 | **23** |

`[wniosek]` **To jest najważniejsza liczba w tej tabeli i nie widać jej w średnich.** Średnia dokładność po douczeniu **wzrosła** do 98% — bo liczona jest tylko dla tych, u których układ jeszcze działał. **Piętnaście osób z trzydziestu ośmiu (39%) wypadło całkowicie.** Zmniejszanie montażu nie degraduje wyniku gładko; u części osób **przewraca klasyfikator**.

**Skutek dla tego projektu, dwa:**

1. **Dla twierdzenia — żaden.** Twierdzenie jest pomiarowe i mierzy jedną osobę, więc „u ilu procent działa" nie jest jego zmienną. Ale **odsetek zdatnych trzeba raportować** przy każdym warunku, tak jak robi to Liang 2021 (58,3% → 75%).
2. **Dla demonstracji — duży.** `[domysł]` Jeżeli układ potrafi się przewrócić u 39% osób przy sześciu elektrodach i odniesieniu na Cz, to przy montażu zwartym **pokaz na losowym jurorze może nie zadziałać w ogóle**. **Konsekwencja planu: demonstracja na jurorze jest zakazana jako jedyna forma pokazu.** Pokaz obowiązkowy prowadzi się na autorze, a wariant „dla chętnych" wolno uruchamiać wyłącznie po pokazie właściwym i z zapowiedzią, że u części osób nie zadziała — co samo w sobie jest wynikiem do opowiedzenia.

**Sterowalność:** średnia. Przesiew E0 (X 2026) mierzy to u autora. Wariant „dla chętnych" wymaga **osobnej zgody i procedury Human Participants** (`09_FORMALNOSCI.md`) — bez niej nie wolno go uruchomić nawet na stoisku.

---

## Czego na tej liście nie ma i dlaczego

- **„projekt jest za trudny"** — nie jest ryzykiem, tylko oceną. Wykonalność platformy ESP32+ADS1299 jest **potwierdzona opublikowaną, scharakteryzowaną konstrukcją** (arXiv 2601.01772), a cel 90–100 bit/min osiągnięto na sprzęcie za £20 (`METODA.md` §3)
- **„ktoś inny zgłosi interfejs neuralny do Explory"** — policzone: 1 projekt EEG na 133 zgłoszenia w 2026, zero w finałach 2025 i 2026 (K-034)
- **formalności ISEF w wersji z §5.5 handbooka** — alarm był fałszywy i został zamknięty w etapie 1

---

## Drabinka zejść

**Przeniesiona 21 VIII 2026 z `archiwum/34_PARAMETRY_I_RAMY.md` §6, z werdyktem audytu i terminami.**

**Reguła schodzenia:** zejście o szczebel wymaga wpisu do `KOREKTY.md` z **datą, powodem liczbowym i wskazaniem, co zostało poświęcone**. **Bez wpisu zejście się nie liczy.**

| Szczebel | Zakres | Co poświęcone | Werdykt audytu |
|---|---|---|---|
| **A — pełny** | odniesienie w czterech położeniach i dwóch kierunkach, pełne porównanie dokładności i ITR, demonstracja | nic | cel. **Szansa na termin: 35–50%** |
| **B** | jak A, ale **mniej warunków pomiarowych** (np. bez badania wpływu ruchu głowy) | część tabeli wieloczynnikowej | **zostawia projekt bez zastrzeżeń** — twierdzenie stoi, traci jeden wymiar |
| **C** | pomiar **tylko na autorze**, bez innych badanych | uogólnienie na populację; **znika też cała procedura zgód** | **to jest plan bazowy, nie zejście.** `04_PLAN_POMIAROWY.md` planuje 1 920 prób na jedną osobę, a efekt 9–24 pp jest wewnątrzosobniczo wykrywalny wielokrotnie |
| **D** | jedna wersja montażu, pełna charakteryzacja toru, dekodowanie i demonstracja działają | **całe pytanie o położenie odniesienia** | zostawia **urządzenie bez wyniku**. Pełna punktacja w `Execution`, połowa w `Research Problem` |
| **E — dno** | sam tor analogowy: szum, pasmo, CMRR, kalibracja, bez sterowania czymkolwiek | wszystko oprócz metrologii | poprawny projekt inżynierski i **słaby projekt konkursowy** — `[fakt]` arXiv 2601.01772 jest dokładnie tym i już to opublikował |

`[wniosek]` **Rzeczywisty próg leży między C a D: powyżej niego projekt ma wynik, poniżej ma tylko urządzenie.** Szczeble B i C nie są myśleniem życzeniowym; opis D i E jako równoważnych pozostałym — był.

**Terminy decyzji o zejściu.** Bez nich zejście następuje w maju 2027 pod presją, a nie zimą z decyzji:

| Zejście | Termin | Wyzwalacz |
|---|---|---|
| **A → B** | **31 I 2027** | v1 nie działa — tabela wieloczynnikowa wypada z planu |
| **B → C** | **31 III 2027** | komisja IRB nie istnieje — kampania jednoosobowa, tak opisana w zgłoszeniu |
| **C → D** | **30 IV 2027** | druga wersja montażu niegotowa — do półfinału idzie jedna |
| **D → E** | **31 VII 2027** | ostatni moment na przestawienie planu finałowego na metrologię toru |
