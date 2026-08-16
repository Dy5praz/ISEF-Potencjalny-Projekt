# 17 — Ryzyka i plany awaryjne

**Data:** 16 sierpnia 2026
**Podstawa:** `HANDBOOK.md` §11 punkt 5 — *„ryzyka z planem awaryjnym dla każdego"*.

Każde ryzyko oceniam w trzech wymiarach wymaganych przez `HANDBOOK.md` §2.2: **prawdopodobieństwo**, **sterowalność** (na ile wynik zależy od użytkownika), **koszt porażki**. Dwie pozycje o tej samej szansie mogą być zupełnie różnymi decyzjami.

---

## Tabela zbiorcza

| # | Ryzyko | P | Sterowalność | Koszt | Kiedy się rozstrzyga |
|---|---|---|---|---|---|
| **R1** | słaba odpowiedź SSVEP u autora | **20–30%** | niska | **bardzo wysoki** | **X 2026** |
| **R2** | własny tor analogowy nie osiąga użytecznego szumu | 40% | wysoka | średni | II 2027 |
| **R3** | brak sprzętu pomiarowego do charakterystyki toru | **50%** `[luka]` | średnia | średni | X 2026 |
| **R4** | efekt odległości odniesienia < 3 pp — T1 upada | **25%** | zerowa | wysoki | XI 2026 (na cudzych danych: już częściowo znany) |
| **R5** | ktoś publikuje tę samą oś przed nami | 10–20% | zerowa | **niski** | ciągle |
| **R6** | komisja IRB przy szkole nie powstaje | 30% | średnia | niski | XII 2026 |
| **R7** | poślizg: druga wersja płytki wypada po V 2027 | 35% | wysoka | wysoki | III 2027 |
| **R8** | nowa oś zajęta w bazach nieprzeszukanych | **5%** | wysoka | średni | **częściowo zamknięte 16 VIII 2026** |
| **R9** | moduł nie mieści się w granicy gabarytu | 25% | wysoka | średni | I 2027 |
| **R10** | brak opiekuna z tytułem / Qualified Scientist | 20% `[luka]` | średnia | **bardzo wysoki** | XI 2026 |
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

**Uwaga:** punkt 3 jest zejściem o poziom w ambicji i zapisuję to jako zejście, zgodnie z `HANDBOOK.md` §11. Poświęcone: metryka zrozumiała dla laika (ITR) na rzecz metryki zrozumiałej dla jurora od elektroniki (SNR). W kategorii **EBED** ta zamiana kosztuje mniej niż w ENBM.

---

## R2 — własny tor nie osiąga użytecznego szumu

**Prawdopodobieństwo wysokie i to jest normalne.** Pierwsza własna płytka dla sygnałów mikrowoltowych rzadko działa za pierwszym razem.

**Plan awaryjny, w kolejności:**
1. **rezerwa 30% w budżecie i v2 w harmonogramie na marzec–kwiecień 2027** — wpisane, nie doproszone (`15_PROJEKT.md` §5.2)
2. jeżeli v2 też zawodzi: **twierdzenie T1 nie wymaga własnego toru.** Wymaga *jakiegoś* toru o znanej charakterystyce i wymiennych wiązek elektrodowych. Kupiona platforma z własnym zestawem elektrod obsługuje E2, E3 i E5 w całości
3. co się wtedy traci: kontrybucja sprzętowa i rubryka „własny front-end". Co zostaje: **pomiar, twierdzenie, wynik.** Projekt schodzi z „własny sprzęt plus pomiar" na „pomiar na sprzęcie kupionym z własną częścią elektrodową" — czyli mniej więcej tam, gdzie leżał projekt referencyjny ENBM074, który za to dostał drugie miejsce na ISEF

**To jest realny plan B, nie pocieszenie.** Dlatego kolejność z `15_PROJEKT.md` §4.1 stawia platformę kupioną **przed** własną płytką, a nie po niej.

---

## R3 — brak sprzętu pomiarowego do E1

`[luka]` Pytanie B3 z `00_PYTANIA_I_LUKI.md` nadal bez odpowiedzi. Bez oscyloskopu o niskim szumie własnym albo karty pomiarowej nie da się **udowodnić**, że front-end działa.

**Plan awaryjny:**
1. **droga przez brata** — pracuje w firmie produkującej precyzyjną elektronikę; to jest zasób jednorazowy i trzeba go zaplanować, nie zużyć przypadkiem (`HANDBOOK.md` §1). Zaplanować na **luty 2027**, na gotową płytkę v1, nie wcześniej
2. **obejście bez oscyloskopu**, opisane w `03_SCIANY_FIZYCZNE.md` §6: szum toru mierzy się **samym torem** — zewrzeć wejście przez rezystor i policzyć RMS z zarejestrowanych próbek. Przetwornik 24‑bitowy jest tu przyrządem. Tego nie da się użyć do pomiaru CMRR przy 50 Hz, ale **da się do szumu i dryfu**
3. co zostaje niezmierzone bez sprzętu: CMRR i jitter. **Obie liczby można podać jako katalogowe z ADS1299 z jawnym zaznaczeniem, że nie są własnym pomiarem.** Jest to słabsze i tak trzeba to opisać

---

## R4 — efekt okazuje się mały, T1 upada

**Częściowo już rozstrzygnięte i to na korzyść.** Na cudzych surowych danych efekt wynosi **9,3–24,5 pp** (`14_REANALIZA.md` §5). Żeby T1 upadło, własny pomiar musiałby się rozejść z tamtym o rząd wielkości.

**Zastrzeżenie dołożone 16 VIII 2026, i jest realne** `[luka]`: te liczby obowiązują dla metod **bez fazy** (FBCCA, CCA, cechy FFT). **TRCA sprawdzone i na tamtym zbiorze niewykonalne** — faza SSVEP nie jest zsynchronizowana z oknami (`14_REANALIZA.md` §6B). Możliwe, że filtr przestrzenny uczony na osobie odzyskuje część straty montażu zwartego. **Podnosi to prawdopodobieństwo R4 z 15% na 25%** i jest głównym powodem, dla którego własne stanowisko musi zapisywać moment zapłonu bodźca od pierwszej sesji.

**Plan awaryjny:** jeżeli efekt wyjdzie mały, to znaczy, że **moduł zwarty działa prawie tak dobrze jak montaż literaturowy** — czyli twierdzenie odwraca znak i staje się **lepszą wiadomością dla urządzenia**: „gabaryt mieszczący się w module nie kosztuje przepustowości". To też jest wynik, też jest publikowalny i **jest korzystniejszy z punktu widzenia produktu**.

`[wniosek]` **T1 jest tak skonstruowane, że nie ma wyniku, który by je unieważnił** — jest tylko wynik, który zmienia jego znak. To jest ta sama własność, którą miało poprzednie twierdzenie, i to jest powód, dla którego oba przeszły audyt.

---

## R5 — ktoś publikuje pierwszy

Ocena z `12_AUDYT.md` §10 pozostaje: grupa z Politechniki Warszawskiej to **zespół przetwarzania sygnałów, bez dorobku sprzętowego**, więc ryzyko, że sami wykonają wersję sprzętową, to **10–20%**.

**Dla nowej osi ryzyko jest jeszcze niższe** `[wniosek]`: pytanie o odległość odniesienia jest pytaniem konstrukcyjnym, nie algorytmicznym, i nie leży w ich profilu ani w profilu żadnego nazwanego aktora, którego znam.

**Plan awaryjny — bez zmian i nadal wystarczający:** twierdzenie jest pomiarowe, więc cudza publikacja go nie unieważnia. Degradacja jest z „nowe" na „potwierdzone niezależnie". **Zakaz słowa „pierwszy" w materiałach zgłoszeniowych obowiązuje bez zmian (K-044).**

**Monitorowanie:** PubMed po autorach `Kolodziej M`, `Majkowski A`, plus zapytania o odległość odniesienia z `14_REANALIZA.md` §11, **co dwa miesiące**.

---

## R6 — komisja IRB nie powstaje

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

**Zamknięte w trzech czwartych tego samego dnia.** Pierwotnie dla nowej osi miałem tylko PubMed — czyli dokładnie ten błąd, który `PRZEKAZANIE.md` §5 wymienia jako **wzorzec numer 1**: zmiana konfiguracji projektu bez powtórzenia audytu prior art. Zamiast zapisać go jako zadanie na później, domknąłem go od razu.

**Stan po 16 VIII 2026** (`14_REANALIZA.md` §11): **PubMed, Crossref i arXiv przeszukane — nowa oś niezajęta.** Znaleziona jedna nowa pozycja o formie urządzenia (arXiv 2509.15449, elektroda douszna dla SSVEP, pięciu badanych), która osi nie zajmuje.

`[luka]` **Nieprzeszukana zostaje baza patentów** dla nowej osi, oraz literatura nieanglojęzyczna.

**Plan awaryjny:** patenty do sprawdzenia przed jakimkolwiek zakupem, czyli przed X 2026. Jeżeli oś okaże się zajęta, wraca pytanie o oś — ale **sprzęt z `15_PROJEKT.md` się nie zmienia**, więc koszt jest w dokumentacji, nie w pieniądzach.

---

## R9 — gabaryt

Granica twarda: **nic zbliżonego do opaski przechylonej na tył głowy**, żadnej konstrukcji nad czubkiem głowy ani przez czoło (`DECYZJE.md` decyzja 3).

**Napięcie, które reanaliza ujawniła:** najlepsze odniesienie może leżeć na wyrostku sutkowatym (za uchem, ~7 cm od Oz) albo na płatku ucha (~10 cm). **Wyprowadzenie odniesienia za ucho to cienki przewód przy głowie, który tabela gabarytowa dopuszcza wprost** („cienki przewód lub łuk między modułami, przy głowie" — przechodzi). Zausznik odrzucony w K-036 był **drugim miejscem elektrod aktywnych**, a nie pojedynczym odniesieniem.

`[wniosek]` **To nie jest złamanie decyzji 2, tylko jej doprecyzowanie**, i wymaga potwierdzenia użytkownika — pytanie P2 w `18_PYTANIA_ETAP2.md`.

**Plan awaryjny:** kolejność ustępstw z `DECYZJE.md` decyzja 3 — najpierw gabaryt i widoczność, potem wygoda, **nigdy hełm**.

---

## R10 — opiekun naukowy

`[luka]` Pytanie B5 bez odpowiedzi od etapu 1. Formalnie: **magister wystarcza na role Adult Sponsor i Direct Supervisor**, a Qualified Scientist **nie wymaga doktoratu** — dopuszczalne jest „extensive experience and expertise" (K-020, K-021).

**Koszt porażki bardzo wysoki, bo dyskwalifikuje niezależnie od jakości projektu.** Prawdopodobieństwo niskie, bo próg formalny okazał się niższy, niż zakładał handbook.

**Plan awaryjny:** pisemna zgoda opiekuna szkolnego, jesień 2026. **Tanie, bez terminu, zdejmuje ryzyko** — i dlatego nie ma powodu z tym czekać.

---

## R11 — ZAMKNIĘTE 16 VIII 2026

**Rozstrzygnięcie użytkownika: wariant C** — osi nie zamykamy teraz, sprzęt obsługuje obie, wybór następuje po pierwszych własnych pomiarach (`DECYZJE.md` decyzja 5).

Użytkownik zażądał przy tym sprawdzenia, czy kanał szczękowy w ogóle daje dość, żeby być osią. **Sprawdzone, `14_REANALIZA.md` §6A: nie daje, sufit +0,6 pp, p = 0,166.** Skutek: elektroda szczękowa wychodzi ze sprzętu, kanał mięśniowy przenosi się na kark, **sprzęt się upraszcza**.

**Ryzyko rezydualne, które z tego zostaje i jest realne** `[wniosek]`: wariant C oznacza, że **do pierwszych własnych pomiarów projekt nie ma jednego zdania twierdzenia**. Do zgłoszenia Explory (28 II 2027) zdanie musi istnieć. Pierwsze pomiary w torze A planowane są na **X 2026**, czyli z czteromiesięcznym zapasem — ale jeżeli tor A się opóźni, zgłoszenie pisze się na osi wybranej bez pomiaru, czyli dokładnie tak, jak nie chcemy.

**Plan awaryjny:** jeżeli do **31 XII 2026** nie ma własnych pomiarów, oś wybieramy **wariantem A** (odległość odniesienia) na podstawie samej reanalizy i zapisujemy, że wybór był bez własnego pomiaru. Reanaliza jest do tego wystarczającą podstawą — efekt 9–24 pp wobec 0,6 pp nie jest bliskim rozstrzygnięciem.

---

## Czego na tej liście nie ma i dlaczego

- **„projekt jest za trudny"** — nie jest ryzykiem, tylko oceną. Wykonalność platformy ESP32+ADS1299 jest **potwierdzona opublikowaną, scharakteryzowaną konstrukcją** (arXiv 2601.01772), a cel 90–100 bit/min osiągnięto na sprzęcie za £20 (`12_AUDYT.md` §3)
- **„ktoś inny zgłosi interfejs neuralny do Explory"** — policzone: 1 projekt EEG na 133 zgłoszenia w 2026, zero w finałach 2025 i 2026 (K-034)
- **formalności ISEF w wersji z §5.5 handbooka** — alarm był fałszywy i został zamknięty w etapie 1
