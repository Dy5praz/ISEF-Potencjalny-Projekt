# 00 — Streszczenie etapu 1: co z tego wynika dla projektu

**Data:** 15 sierpnia 2026, **wersja trzecia — po weryfikacji w oryginałach**
**Zakres:** przemiał literatury wg sekcji 10 handbooka, 12 zadań weryfikacyjnych z `00_PYTANIA_I_LUKI.md` sekcja 4d, oraz 9 pozycji z sekcji 3 `PRZEKAZANIE.md`.

Wersja druga była zbudowana bez dostępu do źródeł. Ta wersja powstała po odczytaniu **12 prac naukowych i 7 dokumentów regulaminowych w oryginale**. Wyszło z tego **szesnaście korekt** (`KOREKTY.md` K-020…K-035), z czego **trzy zmieniają decyzje projektowe**, a nie tylko zapis.

---

## 0. Przeczytaj to, jeżeli masz przeczytać jedną rzecz

Trzy ustalenia, które przewracają wnioski z poprzedniej wersji, i dwa, które je potwierdzają.

**Przewracają:**

1. **Pułap formy dousznej jest o rząd wielkości wyżej, niż napisałem.** Twierdziłem, że SSVEP z ucha to 6–17 bit/min i że to ściana geometryczna. Praca z **Nature Communications 2023** pokazuje z kanału słuchowego speller 40-celowy online bez kalibracji. Ograniczeniem był **kontakt elektrody**, nie odległość od kory — czyli mechanika i materiały, czyli **Twój warsztat**. `KOREKTY.md` **K-028**.
2. **Oś projektu dotyczy szczęki, nie pary „szczęka i oko".** Odczytałem Kappela 2017 w oryginale: przy uchu **mrugnięcie w ogóle nie psuje SNR**, w przeciwieństwie do skalpu. Zakłóceniem jest zaciskanie szczęki i, słabiej, ruch gałek ocznych. Układ upraszcza się, nie komplikuje. **K-026**.
3. **Publiczny zbiór ear-EEG pod sterowanie istnieje** — 24 osoby, ERP i SSVEP, z równoległym EOG i pomiarem ruchu. Twierdziłem, że nie istnieje, i budowałem na tym element wkładu projektu. **K-027**.

**Potwierdzają:**

4. **Formalności ISEF są dużo łagodniejsze, niż zakładaliśmy.** Badanie na sobie jest zwolnione z uprzedniej zgody komisji, a **osobna kategoria ryzyka dla urządzeń elektrycznych przy głowie nie istnieje**. Zdanie z sekcji 5.5 handbooka o „najbardziej prawdopodobnej przyczynie dyskwalifikacji" było ostrożnym domysłem i się nie potwierdziło.
5. **Na Explory nie ma konkurencji tematycznej.** Policzone: **1 projekt EEG na 133 zgłoszenia półfinałowe** edycji 2026, **zero w finałach 2025 i 2026**. Twój argument z sekcji 9.3 handbooka jest potwierdzony liczbowo. Ale na ISEF konkurencja jest i rośnie: **22 projekty EEG w 2026 wobec 8 w 2024**.

---

## 1. Co projekt ma robić — stan po weryfikacji

> **Urządzenie noszone na głowie, złożone z modułów nie większych niż aparat słuchowy, rejestrujące EEG, sterujące obiektem kilkoma komendami dyskretnymi.**
> **Twierdzenie jest pomiarowe**, nie o pierwszeństwie.
> **Umiejscowienie elektrod: DECYZJA OTWARTA** — `09_UMIEJSCOWIENIE.md`. Rekomendacja bez zmian: uczynić z geometrii **zmienną mierzoną**, nie wybieraną założeniem.

### 1.1 Twierdzenie pomiarowe zamiast twierdzenia o pierwszeństwie — BEZ ZMIAN, wzmocnione

Przegląd systematyczny (`04` sekcja 2) potwierdził typ z K-009: pomysł kompensacji artefaktu z kanału odniesienia jest stary (1983), a realizacja analogowa jest częściowo zajęta — dla artefaktów **ruchowych** (Dabbaghian 2019) i dla **offsetu** w formie zausznej (Kim 2026). Kompensacji artefaktu **szczękowego z kanału odniesienia przed przetwornikiem w urządzeniu przyusznym** nie znalazłem, ale zapytanie skrojone pod to dało zero trafień w jednej bazie — **to jest sygnał, nie dowód**.

**Wniosek bez zmian:** twierdzenie „pierwszy raz" jest niedostępne i nie warto o nie walczyć. Twierdzenie „ten układ poprawia X o Y, oto pomiar" jest dostępne i **nie unieważni go znalezienie cudzej pracy w połowie 2027**.

**Co doszło i jest ważne — właściwy baseline.** Praca Knierima 2023 (`05` sekcja 7) pokazuje, że **OpenBCI ma szum porównywalny ze wzmacniaczem badawczym** w zapisach wokółusznych. Czyli twierdzenie „zbudowałem cichy wzmacniacz" jest zajęte przez produkt z półki. **Ale to przesuwa oś we właściwą stronę:** OpenBCI staje się naszym punktem odniesienia, a twierdzenie brzmi „OpenBCI nie kompensuje artefaktu szczękowego przed przetwornikiem, a przy uchu to jest dominujące zakłócenie — oto pomiar tego samego układu z kompensacją i bez".

### 1.2 Przewaga w metryce użytkowej — **rekomendacja WYCOFANA, decyzja wraca do Ciebie**

Poprzednia wersja rozstrzygała pytanie C2 rekomendacją na wariant 2 (metryka użytkowa), uzasadniając to tym, że „w przepustowości nie da się wygrać, bo SSVEP z ucha to 6–17 bit/min wobec ~92 z potylicy, i to jest geometria".

**Ta liczba była nieaktualna o osiem lat, a wniosek z niej wyprowadzony był błędny.** Praca SpiralE (Nature Comms 2023) pokazuje 95% na 9 celach i speller 40-celowy online z kanału słuchowego.

**Co z tego wynika:** wariant 2 nie jest zły — ale **przestał być jedynym wyjściem po eliminacji pozostałych**, a taka była jego jedyna podstawa. **Wybór C2 wraca jako otwarty, z trzema wariantami o porównywalnym statusie.** Nie rozstrzygam go za Ciebie drugi raz, skoro pierwszy raz rozstrzygnąłem go na złej liczbie.

Co się przy tym nie zmienia: metryki użytkowe (czas montażu, stabilność, odsetek sesji bez rekalibracji, tolerancja na ruch) są **realnie nieraportowane** i tam jest wolne miejsce. To pozostaje prawdą.

**Uwaga formalna, nowa i ograniczająca:** metryki zależne od stanu badanego — wyspanie, zmęczenie — są w regulaminie ISEF **zmienną ludzką** i łamią zwolnienie dla badania na sobie (`ISEF_HUMAN_PARTICIPANTS.md` sekcja 1.1). Dryf jakości sygnału w czasie noszenia mierzyć wolno. „Jak wynik zależy od tego, ile spałem" — wymaga zgody komisji.

### 1.3 Paradygmat — nadal nierozstrzygnięty, ale przesłanki się wyostrzyły

Potwierdzone w oryginale (`03` sekcja 3.1): praca Frei 2026, **19 osób**, douszny system suchy vs 32-kanałowy BioSemi — **alfa spoczynkowa wychodzi pewnie, odpowiedź słuchowa N1-P2 nie**. Praca finansowana przez Logitech, który dostarczył badane urządzenie, co **wzmacnia wiarygodność wyniku negatywnego**.

Do tego doszło zastrzeżenie do pracy o rytmie mu (`03` sekcja 3): badani wykonywali **ruch rzeczywisty, nie wyobrażony**. Dla sterowania potrzebne jest wyobrażenie, a tego z ucha nikt nie pokazał — **`[luka]`**.

**Stan: SSVEP wygląda najlepiej i po pracy SpiralE wygląda znacznie lepiej niż wcześniej.** Koszt bez zmian: wymaga patrzenia na migający obiekt, więc traci argument „działa przy zamkniętych oczach" i wchodzi w porównanie z eye trackingiem. **Decyzja należy do etapu 2.**

### 1.4 Wariant hybrydowy zamknięty — i zamknięty dłużej, niż sądziłem

ID.EARS (CHI 2025) domyka rolę sEMG/EOG jako źródła sterowania w formie dousznej. **Ale pierwszeństwo jest starsze:** sterowanie ramieniem robota z artefaktów szczękowych opublikowano w *PLoS One* w **2014**, jedenaście lat wcześniej.

**Element do wzięcia, doprecyzowany po K-026:** potrzebny jest detektor **zaciśnięcia szczęki**, żeby wiedzieć, kiedy kompensować. Detektor mrugnięcia — **niepotrzebny**, bo mrugnięcie przy uchu nie psuje sygnału.

---

## 2. Co to zmienia w kalendarzu i w decyzjach zakupowych

| Sprawa | Stan przed | Stan po weryfikacji w oryginale |
|---|---|---|
| **czy zdążymy na ISEF 2028** | potwierdzone stronami organizatora | **potwierdzone cytatem z regulaminu.** §8 pkt 7c: wyjazd na ISEF „**w maju kolejnego roku**". Pozycja zamknięta ostatecznie |
| **reguła 12 miesięcy** | „12 mies. + zakaz danych starszych niż 18 mies." | **liczby 18 w regulaminie nie ma.** Okno to I 2027 – V 2028, blok 12 mies. w środku. **Kampanię pod ISEF zaczynać w V 2027.** K-023 |
| **badania na sobie** | „prawdopodobnie zwolnione", ryzyko dyskwalifikacji | **zwolnione**, dwa warunki: brak ryzyka **i brak zmiennej ludzkiej** |
| **urządzenie elektryczne przy głowie** | „jedyna pozycja o konsekwencjach dyskwalifikacyjnych" | **nie ma takiej kategorii ryzyka.** Reguły elektryczne dotyczą stoiska, próg 36 V. **Alarm był fałszywy** |
| **opiekun naukowy** | magister nie wystarcza, potrzebny doktor | **doktorat ALBO rozległe doświadczenie.** Brat jest realnym kandydatem. K-020 |
| **komisja IRB** | traktowana jak instytucja zewnętrzna | **trzeba ją powołać przy szkole**: edukator + dyrektor + pielęgniarka lub psycholog. Nowa pozycja harmonogramowa na jesień 2026 |
| **drukarka i żywica** | „nie kupować Q2", żywica `[luka]` | **luka zamknięta na TAK.** Liqcreate Bio-Med Clear, ISO 10993-5/-10/-23, zwykłe drukarki MSLA, ~456 zł/0,5 kg, polskie sklepy. K-035 |
| **El-Robo-Mech** | wymuszony termin, nie walidacja | bez zmian, **ale są lepsi zamiennicy**: OITwEiM (olimpiada, prototyp w etapie centralnym) i EUCYS (eliminacje krajowe → finał europejski). `08` sekcja 4.1 |
| **arkusze oceny ISEF** | rozbicie 10/15/20/20/35 niezweryfikowane | **potwierdzone**, plus: Presentation dzieli się na **Poster 10 + Interview 25**. K-024 |

**Najpilniejsza rzecz w tej tabeli już nie jest tą samą rzeczą.** Wcześniej był nią wiersz o badaniach na sobie. Teraz jest nim **wiersz o komisji IRB** — bo to jedyna pozycja wymagająca zgody osób trzecich i jedyna, której nie da się załatwić w tydzień. Rozmowa z dyrekcją szkoły jesienią 2026, plus jeden mail do FZT z pytaniem, czy organizator prowadzi SRC pełniące funkcję IRB.

---

## 3. Czego NIE robimy — lista skrócona o jedną pozycję

Wynika z `03_SCIANY_FIZYCZNE.md`.

- **rozdzielczość porównywalna z inwazyjnymi** — czaszka rozmywa sygnał do ~5–9 cm. **Ściana fizyczna, bez zmian**
- **sterowanie ciągłe, wielowymiarowe z jednej pozycji zausznej** — brak filtracji przestrzennej do rozdzielenia kierunków. Bez zmian
- **działanie u 100% badanych w wyobrażeniu ruchu** — 15–30% osób nie uzyskuje kontroli niezależnie od sprzętu. **Przy grupie kilku osób jedna niedziałająca jest zdarzeniem oczekiwanym i musi być wpisana w plan z góry**
- **paradygmaty słuchowe jako podstawa sterowania** — N1-P2 nie wychodzi w konfiguracji dousznej, n=19, potwierdzone w oryginale
- **oś projektu w uczeniu głębokim** — metody riemannowskie biją sieci przy małej liczbie kanałów i danych, czyli w naszym reżimie

**Pozycja WYCOFANA z tej listy:** „wyższy ITR niż czapka przy tym samym paradygmacie". To nie jest ściana geometryczna — `KOREKTY.md` K-028. **Nie wolno jej używać jako argumentu, powołując się na dokumenty tego repozytorium.**

---

## 4. Cztery rzeczy do wpisania w plan eksperymentalny już teraz

**4.1 Warunek kontrolny na sygnale losowym.** Trzy warianty tego samego układu: sterowanie z sygnału, sterowanie ze wspomaganiem, oraz **układ zasilany sygnałem losowym z tym samym wspomaganiem**. Trzeci warunek odpowiada na pytanie jurora „ile z tego to naprawdę mózg". Bez niego nie ma odpowiedzi pomiarowej.

**4.2 Każda liczba wydajności w dwóch wersjach** — surowe dekodowanie i wynik z całą warstwą wspomagającą. Powód i przykłady w `07` sekcja 5.

**4.3 Wyniki osobno dla wariantu wewnątrzsesyjnego, międzysesyjnego i międzyosobniczego.** Podanie samego wewnątrzsesyjnego jako „dokładności układu" to najczęstszy sposób zawyżania liczby w tej dziedzinie. **Punktowane w dwóch miejscach naraz:** Załącznik nr 1 regulaminu Explory (krytycyzm wobec własnych wyników) i rubryka Interview arkusza ISEF („understanding interpretation and **limitations** of results").

**4.4 NOWE — struktura eksperymentu wzorowana na projekcie referencyjnym.** Abstrakt ENBM074 (2026), odczytany w całości, pokazuje, co wygrywa w tej kategorii: warunek kontrolny **na tym samym sprzęcie**, randomizacja, kontrbalansowanie, **replikacja na drugiej grupie**, poprawka na wielokrotne porównania, rozmiar efektu, oraz **test mechanizmu**, a nie tylko test wyniku. Sekcja 9.2 handbooka zakazuje kopiowania tamtego **rozwiązania**; **rzemiosła nie zakazuje i należy je skopiować**.

---

## 5. Co zostaje otwarte

| Co | Dlaczego nie domknięte |
|---|---|
| **regulamin ISEF 2027–2028** | jeszcze nie istnieje, ukaże się ~poł. 2027. Przeczytać wtedy od nowa — daty i numery formularzy mogą się zmienić |
| **Explory 2016–2024, liczby projektów neuro** | listy finalistów sprzed 2025 są aplikacjami renderowanymi w przeglądarce, a przeglądarka w tym środowisku nie ma dostępu do sieci. Dwie ostatnie edycje policzone i wystarczają do decyzji |
| **licencje publicznych zbiorów danych** | wymagają otwarcia stron z danymi, nie samych artykułów. **Przed użyciem czegokolwiek** |
| **pełne teksty za paywallem** | IEEE i część Elsevier. Prace w otwartym dostępie (SpiralE, Kappel, Lee) da się przeczytać za darmo — pierwsza kolejka etapu 2 |
| **czy EUCYS i Explory da się łączyć** | jedno pytanie mailem do obu organizatorów |
| **czy FZT prowadzi SRC/IRB** | jedno pytanie mailem, może skasować całą procedurę z sekcji 4 `ISEF_HUMAN_PARTICIPANTS.md` |
| **C2 — w czym „lepsze od komercyjnych"** | **decyzja wraca do Ciebie**, patrz sekcja 1.2. Poprzednia rekomendacja stała na błędnej liczbie |
| **umiejscowienie** | `09_UMIEJSCOWIENIE.md`, decyzja Twoja |

---

## 6. Nawigacja

| Plik | Po co go otwierać |
|---|---|
| `ISEF_HUMAN_PARTICIPANTS.md` | **formalności — przepisane z oryginału regulaminu.** Alarm okazał się fałszywy, ale doszła komisja IRB |
| `ISEF_ARKUSZE_OCENY.md` | **nowy.** Oba arkusze oceny w całości, kategorie, wymogi abstraktu, zasady użycia AI |
| `08_KONKURENCJA_ISEF.md` | **pełny abstrakt projektu referencyjnego**, liczby konkurencji na ISEF i Explory, alternatywy dla El-Robo-Mech |
| `04_LUKI_ZAPISANE.md` | przegląd systematyczny osi projektu, praca SpiralE, obalone twierdzenie o zbiorach danych |
| `03_SCIANY_FIZYCZNE.md` | co jest fizyczne, co technologiczne, jak zmierzyć szum bez oscyloskopu |
| `06_TABELA_PARAMETROW.md` | wszystkie liczby, teraz z kolumną „n" i statusem weryfikacji |
| `07_DEKODOWANIE.md` | paradygmaty, metody, zbiory danych, rozbiór metryki „słów na minutę" |
| `05_RYNEK.md` | baseline komercyjny, **żywica ISO 10993 — luka zamknięta**, OpenBCI jako punkt odniesienia |
| `02_MECHANIZMY.md` | **jeżeli coś jest niejasne** — tam każdy termin ma wyjaśnienie |
| `KOREKTY.md` | K-001…K-035, w tym szesnaście z tej sesji |
