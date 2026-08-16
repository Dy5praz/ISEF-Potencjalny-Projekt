# ISEF — nieinwazyjny interfejs neuralny

Repozytorium robocze projektu. Dokumentacja żyje tutaj, nie w wątkach rozmowy.

**Cel:** Explory 2027 → reprezentacja Polski na Regeneron ISEF, maj 2028.

---

## ETAP 2 W TOKU — od 16 sierpnia 2026

> **Oś projektu została wymieniona pierwszego dnia etapu 2.** Zbiór danych, na którym stała stara oś, okazał się publiczny (CC-BY). Reanaliza surowych danych — z odtworzeniem tabeli autorów co do trzeciego miejsca po przecinku — pokazała, że przyrost **+9 pp należy w całości do elektrody Cz**, a kanał szczękowy, który był osią projektu, dokłada **0,3 pp**.
>
> **Nowa oś:** zależność przepustowości SSVEP od **odległości elektrody odniesienia** od okolicy potylicznej, czyli od gabarytu modułu. Efekt zmierzony na cudzych danych: **9–24 pp** — dwadzieścia do sześćdziesięciu razy większy niż ten, który odpadł, i wykrywalny na jednej osobie.
>
> **Czytaj w kolejności: `14_REANALIZA.md` → `15_PROJEKT.md` → `16_PLAN_EKSPERYMENTALNY.md` → `17_RYZYKA.md` → `18_PYTANIA_ETAP2.md`.**
> `PRZEKAZANIE.md` i `12_AUDYT.md` zostają jako tło historyczne — **oba zawierają nieaktualną oś**.

### Pliki etapu 2

| Plik | Zawartość |
|---|---|
| **`14_REANALIZA.md`** | **reanaliza surowych danych Kołodziej i in. 2026; zmiana osi projektu; prior art dla nowej osi** |
| `15_PROJEKT.md` | co budujemy, z czego, za ile, w jakiej kolejności; kamienie milowe |
| `16_PLAN_EKSPERYMENTALNY.md` | E1–E5, liczba prób policzona, niepewności, granice zwolnienia ISEF |
| `17_RYZYKA.md` | jedenaście ryzyk, każde z planem awaryjnym, w trzech wymiarach |
| `18_PYTANIA_ETAP2.md` | pięć pytań do użytkownika, każde z wariantem domyślnym |
| `19_SZANSE_PO_ZMIANIE.md` | **ocena szans przeliczona po zmianie osi** — piąty i ostatni punkt handbooka §11 |
| `analiza/` | kod reanalizy, uruchamialny od zera, zwalidowany wobec publikacji |

**Decyzje 5 i 6 zapadły 16 VIII 2026** (`DECYZJE.md`): oś projektu — **wariant C**, czyli sprzęt obsługuje obie osie, wybór po pierwszych własnych pomiarach; wyprowadzenie elektrody odniesienia za ucho — **zgoda**.

**Kanał szczękowy sprawdzony na żądanie użytkownika i zamknięty** (`14_REANALIZA.md` §6A): sufit **+0,6 pp** nawet w oknach najbardziej skażonych artefaktem i przy regresorach nieliniowych, p = 0,166. **Elektroda szczękowa wychodzi ze sprzętu**, kanał mięśniowy przenosi się na kark — sprzęt się upraszcza.

**Etap 2 — wszystkie pięć punktów `HANDBOOK.md` §11 domknięte:** gotowy projekt (`15`), twierdzenie z punktem odniesienia (`15` §1), plan eksperymentalny (`16`), ocena szans (`19`), ryzyka z planami awaryjnymi (`17`).

**Nowe korekty: K-051, K-052, K-053.**

---

## ETAP 1 ZAMKNIĘTY — 15 sierpnia 2026

> Zamknięty po **trzech przejściach audytu adwersaryjnego** (`12_AUDYT.md`). Przeszukane kanały: PubMed, arXiv, Crossref, baza patentów, bazy abstraktów ISEF, regulaminy obu konkursów. **Dwadzieścia osiem korekt, K-020…K-047.**

### Stan po weryfikacji w oryginałach

| Etap | Status |
|---|---|
| Sekcja 14 handbooka — drugie czytanie, luki i pytania | **zrobione** → `00_PYTANIA_I_LUKI.md` |
| Odpowiedzi użytkownika, rundy 1 i 2 | **zebrane** → `00_PYTANIA_I_LUKI.md` sekcje 4b i 4c |
| **Etap 1 — przemiał literatury** | **ZAMKNIĘTY** → `00_STRESZCZENIE.md` |
| Etap 2 — opracowanie projektu | **gotowy do startu**, czeka na cztery decyzje użytkownika |

### Co się zmieniło względem stanu porannego

Sesja poranna wykonała etap 1 **bez dostępu do źródeł** — żadna praca nie została otwarta, każda liczba miała znacznik `[wniosek, streszczenie]`. Ta sesja miała dostęp i **odczytała w oryginale 12 prac naukowych oraz 7 dokumentów regulaminowych i konkursowych**.

Wyszło z tego **szesnaście korekt**, `KOREKTY.md` K-020…K-035.

**Trzy zmieniają decyzje projektowe, nie tylko zapis:**

- **K-026** — oś projektu dotyczy artefaktu **szczękowego**, nie pary „szczęka i oko". Kappel 2017 w oryginale: przy uchu **mrugnięcie w ogóle nie psuje SNR**. Układ się upraszcza
- **K-027** — publiczny zbiór ear-EEG pod zadania sterowania **istnieje** (24 osoby, ERP i SSVEP, z EOG i pomiarem ruchu). Twierdziłem, że nie istnieje. Można pracować nad dekodowaniem, zanim powstanie sprzęt
- **K-028** — pułap SSVEP z ucha jest **o rząd wielkości wyżej**, niż podawałem. Nature Communications 2023: speller 40-celowy online bez kalibracji z kanału słuchowego. Ograniczeniem był kontakt elektrody, czyli warsztat użytkownika. **Rekomendacja C2 z porannej wersji stała na tej błędnej liczbie i została wycofana**

**Wskaźnik, który warto znać:** z dwunastu prac odczytanych w oryginale **cztery miały istotny błąd** w opisie ze streszczenia. Jedna trzecia. Przy przeglądzie literatury to nie jest szum — to unieważnia wynik.

---

## Struktura

| Plik | Zawartość | Status |
|---|---|---|
| `HANDBOOK.md` | kontekst i zlecenie | źródło, **pięć wstawek „POPRAWKA"** |
| **`00_STRESZCZENIE.md`** | **co z etapu 1 wynika — czytaj to pierwsze** | gotowy, wersja 3 |
| `00_PYTANIA_I_LUKI.md` | luki, pytania, odpowiedzi użytkownika, lista zadań 4d | gotowy |
| `01_HISTORIA.md` | rozwój technologii, z datami | gotowy, linia ear-EEG zweryfikowana |
| `02_MECHANIZMY.md` | mechanizm fizyczny, po polsku, terminy z definicjami | gotowy, **niezweryfikowany źródłowo** |
| `03_SCIANY_FIZYCZNE.md` | fizyczne vs technologiczne; pomiar szumu bez oscyloskopu | gotowy, jedna ściana wycofana |
| `04_LUKI_ZAPISANE.md` | future work; **przegląd systematyczny osi projektu** | gotowy |
| `05_RYNEK.md` | baseline komercyjny; materiały; **OpenBCI jako punkt odniesienia** | gotowy |
| `06_TABELA_PARAMETROW.md` | metryka porównawcza, kolumna „n", kolumna „skąd ta liczba" | gotowy |
| `07_DEKODOWANIE.md` | paradygmaty, metody, zbiory danych, metryka „słów na minutę" | gotowy |
| `08_KONKURENCJA_ISEF.md` | **abstrakt ENBM074, liczby konkurencji, alternatywy konkursowe** | gotowy |
| `09_UMIEJSCOWIENIE.md` | **gdzie ma być interfejs — decyzja otwarta** | czeka na użytkownika |
| **`ISEF_HUMAN_PARTICIPANTS.md`** | badania z udziałem ludzi, terminarz wsteczny | **gotowy, z oryginału regulaminu** |
| **`ISEF_ARKUSZE_OCENY.md`** | **nowy** — oba arkusze oceny, kategorie, abstrakt, zasady AI | gotowy |
| `ZRODLA.md` | bibliografia; skala z nowym stopniem **AA** = odczytane | gotowy |
| `KOREKTY.md` | rejestr błędów, K-001…K-035 | prowadzony |

---

## Ustalenia kierunkowe — stan po weryfikacji

Zmiany względem stanu porannego zaznaczone **pogrubieniem**.

- **zdolność:** sterowanie, nie komunikacja. Odczyt dyskretny, zachowanie sterowanego obiektu ciągłe. Bez zmian (uzasadnienie skorygowane w K-014)
- **kalendarz: potwierdzony CYTATEM Z REGULAMINU.** Explory §8 pkt 7c — wyjazd na ISEF „w maju kolejnego roku". Finał X 2027 → ISEF V 2028. **Pozycja zamknięta ostatecznie**
- **reguła 12 miesięcy: przeliczona.** Okno I 2027 – V 2028. Reguły „18 miesięcy" w regulaminie nie ma. **Kampanię pod ISEF zaczynać w maju 2027. K-023**
- **formalności ISEF: alarm był fałszywy.** Badanie na sobie zwolnione; osobnej kategorii ryzyka dla urządzeń elektrycznych nie ma. **Doszła jedna realna pozycja: komisję IRB trzeba powołać przy szkole. K-022**
- **opiekun naukowy:** magister wystarcza jako Adult Sponsor i Direct Supervisor. **Qualified Scientist nie wymaga doktoratu. K-020**
- **oś projektu: zawężona do artefaktu szczękowego.** Mrugnięcie przy uchu nie przeszkadza. **K-026**
- **pułap formy dousznej: znacznie wyżej, niż podawałem. K-028.** Wariant twierdzenia przepustowościowego **wraca do gry**
- **rekomendacja C2: WYCOFANA.** Stała na błędnej liczbie. Decyzja wraca do użytkownika
- **konkurencja: policzona.** Explory — 1 projekt EEG na 133 zgłoszenia, zero w finałach. ISEF — 22 projekty EEG w 2026 wobec 8 w 2024. **K-033, K-034**
- **kod projektu referencyjnego ENBM074 (2026) prawidłowy**, abstrakt odczytany, **nagroda to drugie miejsce**, liczby 65/3 wpm potwierdzone. **K-025**
- **żywica ISO 10993: dostępna.** Liqcreate Bio-Med Clear, zwykłe drukarki MSLA, polskie sklepy, ~456 zł/0,5 kg. **Luka zamknięta. K-035**
- **El-Robo-Mech:** bez zmian, ale **znaleziono lepszych zamienników** — OITwEiM i EUCYS
- **umiejscowienie: DECYZJA OTWARTA**, K-019. Argument za potylicą **osłabł** po K-028
- badani, czas, budżet, sprzęt pomiarowy: bez zmian

---

## Decyzje — stan po 15 VIII wieczorem

| # | Decyzja | Status |
|---|---|---|
| 1 | C2 — w czym „lepsze od komercyjnych" | **otwarta**, zawężona do wariantów 2 i 3. Propozycja: zapisać oba z góry, wybrać główne po pierwszych wynikach. `DECYZJE.md` |
| 2 | umiejscowienie | **ZAMKNIĘTA: moduł zwarty na potylicy**, bez łuku i bez drugiego miejsca. Weryfikacja pokazała, że dwa miejsca elektrod **pogarszają** SNR dla SSVEP. K-036 |
| 3 | skala gabarytu | **zatwierdzona**, z granicą twardą: żadnej konstrukcji zbliżającej się do opaski przechylonej na tył głowy |
| 4 | E1 — kalendarz | **przyjęty** |
| E3 | skąd liczby 65 i 3 wpm | **zamknięte** — z abstraktu projektu referencyjnego, prawdziwe |
| formalności / IRB | | **zdjęte z listy ryzyk** decyzją użytkownika |

## Finał etapu 1

| Plik | Zawartość |
|---|---|
| **`10_PROJEKT_DLA_LAIKA.md`** | czym jest projekt bez żargonu; **co realnie umie i czego nie umie**; odpowiedź na „a czemu nie kamerka" |
| **`11_OCENA_SZANS.md`** | **ocena szans Explory i ISEF z liczbami**, w trzech wymiarach: prawdopodobieństwo, sterowalność, koszt porażki |

**Skrót werdyktu:** cel z handbooka (miejsce w kategorii na ISEF) ma prawdopodobieństwo rzędu **1%**; wyjazd na ISEF ~6%; jakikolwiek wymierny sukces konkursowy ~50%. Liczby są niskie, ale wąskie gardło leży tam, gdzie masz największy wpływ, a każda ścieżka porażki zostawia umiejętność albo wpis do dorobku. Pełne uzasadnienie w `11`.

## Trzy rzeczy do zrobienia poza komputerem, jesień 2026

Wynikają z tej sesji i żadnej z nich nie da się załatwić po mojej stronie:

1. **rozmowa z dyrekcją szkoły** — czy da się powołać komisję IRB w składzie: nauczyciel (inny niż opiekun projektu), dyrektor lub wicedyrektor, pielęgniarka szkolna lub psycholog. To najdłuższy proces w całym harmonogramie formalnym
2. **mail do FZT** (`konkurs@fzt.org.pl`) — czy organizator prowadzi SRC pełniące funkcję IRB dla polskich uczestników ISEF. Jedno pytanie, może skasować punkt 1
3. **pisemna zgoda opiekuna szkolnego** na rolę Adult Sponsor i Direct Supervisor — tanie, bez terminu, zdejmuje ryzyko

---

## Zasady obowiązujące w każdym pliku

Znaczniki pewności przy każdym stwierdzeniu: `[fakt]` `[wniosek]` `[domysł]` `[luka]`.

Znacznik złożony **`[wniosek, streszczenie]`** oznacza twierdzenie oparte na streszczeniu wyszukiwarki, bez otwarcia źródła. **Po tej sesji zniknął z większości liczb w plikach 01, 03, 04, 06, 07, 08** — tam, gdzie został, jest to zaznaczone przy twierdzeniu.

W `ZRODLA.md` doszedł stopień **AA** — pozycja odczytana bezpośrednio u wydawcy albo w PubMed.

Każda liczba, na której cokolwiek się opiera: 2–3 niezależne źródła. Jedno źródło — oznaczone przy twierdzeniu, nie w przypisie. **Zgodność trzech streszczeń nie jest weryfikacją** — patrz K-030.

Hierarchia przy sprzeczności: dokument regulaminowy > publikacja recenzowana > preprint > materiał prasowy > blog/forum.
