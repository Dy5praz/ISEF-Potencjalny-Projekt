# ISEF — interfejs neuralny, sterowanie intencją

**Stan na 18 sierpnia 2026.** Dokumentacja żyje tutaj, nie w wątkach rozmowy.

---

## Czytaj w tej kolejności

| # | Plik | Po co |
|---|---|---|
| **1** | **`35_AUDYT_2026_08_18.md`** | **NAJNOWSZY AUDYT, trzy przejścia, 18 VIII 2026.** Co zabija twierdzenie w brzmieniu ogólnym, co przeżyło, brzmienie obowiązujące, osiem sprzeczności między plikami, drabinka zejść rozbita, **pewność 92%** |
| 2 | **`30_POWROT_DO_INTERFEJSU.md`** | **projekt bieżący** — czym jest, twierdzenie, przebudowa demonstracji, poprawki 6a |
| 3 | **`32_STUDIA_USA.md`** | **cel nadrzędny** — uczelnie, kalendarz rekrutacyjny, zadania, werdykt „czy warto" |
| 4 | **`31_ANALIZA_STAWKI_2026.md`** | z kim się konkuruje: noty 21 finalistów Explory 2026, wzorce rzemiosła, plan treningu |
| 5 | **`34_PARAMETRY_I_RAMY.md`** | **budżet 8 000 zł, 10 h/tydzień, kategoria EBED, drabinka zejść, plan pomiarowy** |
| 6 | **`33_KONKURSY_ROZBIEGOWE.md`** | El-Robo-Mech i olimpiada OITwEiM: regulaminy, terminy, szanse, decyzja o przesunięciu olimpiady na edycję 2027/28 |
| 7 | `KOREKTY.md` | rejestr błędów **K-001…K-091**. Dopisuj każdy nowy. **Uwaga: odsyłacze K-051…K-059 w plikach odzyskanych z gałęzi `etap-2` zostały przemapowane 18 VIII 2026 — mapowanie przy K-089** |
| 8 | `HANDBOOK.md` | zasady współpracy. **Sekcje 1–8 i 12–13 obowiązują. Sekcje 9–11 to historia** |
| 9 | `12_AUDYT.md` | **wzorzec audytu adwersaryjnego** — metoda zostaje w mocy |

**Pliki odzyskane 18 VIII 2026 z gałęzi `claude/etap-2-v9dtnt` (K-076)** — dorobek etapu 2 dla interfejsu, którego `main` nigdy nie widziała:

| Plik | Co zawiera |
|---|---|
| **`20_ZAKUPY.md`** | **kosztorys i decyzje zakupowe**: ceny OpenBCI u producenta, pięć wariantów platformy odniesienia, rekomendacja używanego Cytona do 1 600 zł, warunki odbioru |
| `15_PROJEKT.md`, `16_PLAN_EKSPERYMENTALNY.md`, `17_RYZYKA.md` | projekt, plan eksperymentalny i ryzyka w wersji interfejsowej |
| `14_REANALIZA.md`, `19_SZANSE_PO_ZMIANIE.md`, `22_POROWNANIE.md`, `23_NOTY.md` | reanaliza osi, przeliczone szanse, porównania, noty |
| `18_PYTANIA_ETAP2.md`, `21_ODPOWIEDZI.md`, `24_PLAN_DZIALANIA.md`, `25_AUDYT_OPENAIRE.md`, `26_PRZEKAZANIE_ETAP3.md` | pytania, odpowiedzi, plan działania, audyt w OpenAIRE, przekazanie |
| **`analiza/`** | **dziesięć skryptów w Pythonie** — TRCA, SVM, analiza szczęki, okna, rozstaw elektrod |
| `archiwum_poprzednie/` | ConOps **drona** i **ortezy** |

**ZGODNOŚĆ SPRAWDZONA 18 VIII 2026 w audycie `35_AUDYT_2026_08_18.md` przejście 1.** Znalezionych i poprawionych **osiem sprzeczności** (K-078…K-087), w tym: dwa równoległe brzmienia twierdzenia, kolizja numeracji korekt w dziewięciu plikach, obszar Explory wpisany w liście zadań wbrew decyzji z `30`, sprawa Cytona rozstrzygnięta dwa razy w przeciwne strony, cena Cytona zaniżona o połowę w `15` §3.1.

> **Pliki `20`–`23` (aktywne łożysko magnetyczne) usunięte 18 VIII 2026** na życzenie użytkownika. Wszystko przenośne — drabinka zejść i struktura planu pomiarowego — jest w **`34_PARAMETRY_I_RAMY.md`**. Rejestr odrzuconych kierunków, skrócony do jednej linijki na kandydata: `29_ODRZUCONE_KIERUNKI.md`. Usunięte pliki są w historii gita.

---

## Trzy rzeczy, bez których nowa sesja zacznie od złego miejsca

**1. Projekt jest indywidualny. Autorem jest użytkownik, model jest doradcą.**
Zakaz liczby mnogiej („my", „nasz", „zrobiliśmy") w dokumentacji i materiałach zgłoszeniowych. `[fakt]` Regulamin Explory (Załącznik nr 1) i reguły ISEF wymagają pracy własnej i jawnego deklarowania udziału osób trzecich. K-054.

**2. Rekrutacyjnie liczy się wyłącznie ISEF 2028.**
Aplikacje na studia w USA składa się jesienią 2028, decyzje w marcu 2029. **ISEF 2029 jest po decyzjach.** Harmonogram wymaga przeliczenia pod jeden cykl — `32_STUDIA_USA.md` sekcja 1.

**3. Metryka to bity, nigdy słowa na minutę.**
To jedyny mechaniczny strażnik granicy z projektem referencyjnym ENBM074 (2026). W chwili, gdy w materiałach pojawi się „słów na minutę", projekt staje się wariantem cudzej pracy. K-055.

---

## Projekt bieżący, w jednym akapicie

Nieinwazyjny interfejs sterowany bodźcem wzrokowym, w zwartej formie noszonej. **Twierdzenie, brzmienie obowiązujące od 18 VIII 2026** (audyt `35_AUDYT_2026_08_18.md` §4.2; poprzednie „ile kosztuje wygoda" **ma opublikowaną odpowiedź** — K-077):

> **Mierzę, o ile spada dokładność i przepustowość interfejsu SSVEP, gdy elektroda odniesienia musi zmieścić się w module noszonym na potylicy zamiast leżeć w miejscu standardowym, i wyznaczam najmniejszą odległość odniesienia od kory wzrokowej, przy której przepustowość jeszcze się nie załamuje — na jednym własnym torze analogowym, tą samą osobą, tym samym paradygmatem.**

Punkt odniesienia wewnętrzny: ten sam tor analogowy, dwa położenia elektrody odniesienia. Kupiony OpenBCI służy jako **narzędzie kontrolne i ubezpieczenie**, nie jako oś twierdzenia — rola „baseline komercyjny" została wycofana już 16 VIII (`20_ZAKUPY.md` sekcja 2).

**Demonstracja:** bodziec przeniesiony z twarzy na cele w otoczeniu, jedno wykrycie = jedna pełna intencja, wykonanie przez sterowanie **kupionymi** przedmiotami (żarówka, gniazdko — poniżej 200 zł, zero godzin warsztatu). Bez mowy syntetycznej. **Bez pojazdu i bez warstwy autonomii** — `30` §4.2 i §5 zostały zawężone przez regułę 6a.3 z tego samego pliku (K-083).

**Obszar Explory:** Człowiek i Społeczeństwo, historia o dostępności. `[fakt]` Uwaga: obszar „Poza kategoriami" **nie ma nagrody SDG** — K-059.

---

## Szanse — stan po analizie stawki

`[domysł]`, błąd rzędu ×1,5 w każdą stronę.

| Cel | Wartość |
|---|---|
| finał Explory | ~50% |
| reprezentacja na ISEF | ~22% |
| **Nagroda Główna Explory** | ~9–10% |
| jakakolwiek nagroda na ISEF | ~8% |
| **wartość dla aplikacji na studia, niezależna od wyniku** | **~100%, jeżeli projekt powstanie** |

Lejek zweryfikowany w informacji prasowej FZT z 1 VI 2026: **377 zgłoszeń → ponad 130 półfinał → 20 finał + 1 z plebiscytu → 3 na ISEF.**

---

## Zadania otwarte — komplet

### Projekt

| # | Zadanie | Termin |
|---|---|---|
| ~~P1~~ | ~~audyt adwersaryjny, trzy przejścia~~ — **ZROBIONY 18 VIII 2026, `35_AUDYT_2026_08_18.md`.** Wynik: twierdzenie w brzmieniu ogólnym zabite (K-077), wersja wąska przeżyła, pewność **92%** | zrobione |
| **P11** | **reanaliza zbioru Zhu i in. 2021 — 102 osoby, PMID 33578754, publiczny.** Powtórzyć analizę montaży z `14` §5 na próbie ośmiokrotnie większej niż Kołodziej. Kod z `analiza/` już działa, koszt zero złotych | **IX 2026** |
| **P12** | **sekcja o stanie wiedzy** z sześcioma pracami z `35` §2 — pod §7 pkt 2d regulaminu Explory, który daje **10 pkt na 40 za znajomość dotychczasowych badań** | przed zgłoszeniem |
| **P13** | **przećwiczyć odpowiedź na zarzut „to wynika z fizyki objętościowego przewodzenia"** (`35` §2.7) | trening IX 2027 |
| **P14** | **trzecie pytanie do FZT:** czy badanie, w którym autor jest jedynym badanym własnego urządzenia, organizator klasyfikuje jako zwolnione z IRB (`35` §1.9, K-085) | jesień 2026 |
| P2 | **przeliczyć harmonogram pod jeden cykl** (Explory 2027 → ISEF 2028) | przed budową |
| P3 | sprawdzić dorobek grupy Kołodziej M., Majkowski A. — **sprawdzone 18 VIII 2026 imiennie w PubMed: zero nowych prac po `Sensors` 26(3):917.** Powtarzać co dwa miesiące | X 2026 |
| ~~P4~~ | ~~zamknąć zdanie z twierdzeniem i metrykę~~ — **ZAMKNIĘTE 18 VIII 2026, `35` §4.2.** Brzmienie przeniesione do `30`, `34`, `README` i `CLAUDE.md`; metryka bez zmian (dokładność + ITR Wolpawa, z jawnymi N, P, t) | zrobione |
| P5 | **szukać UŻYWANEGO Cytona, budżet do 1 600 zł** — decyzja z `20_ZAKUPY.md` sekcja 3.1, odzyskana 18 VIII (K-076). Wymagania odbioru w tamtym pliku. Jeżeli do terminu nie ma oferty — nowy Ganglion, nie nowy Cyton. Bez AliExpress | **do 30 IX 2026** |
| P6 | przejrzeć **filmy półfinałowe** Explory 2026 — użytkownik prosił o przypominanie | gdy internet pozwoli |
| P7 | dokument **go/no-go** — co musiałoby być prawdą, żeby projekt był wart zachodu | po audycie |
| P8 | **zapytać w szkole o Komitet Szkolny olimpiady OITwEiM** — bez rejestracji olimpiada odpada. Decyzją użytkownika start przesunięty na edycję 2027/28. `33` sekcja 8 | **do 31 X 2027** |
| P9 | sprawdzić ogłoszenie edycji XII El-Robo-Mech, w tym czy można startować dwa razy | X–XI 2026 |
| P10 | El-Robo-Mech **dwa starty**: IV 2027 (pierwszy dry-run) i IV 2028 (próba generalna przed ISEF) | wpisane |

### Rekrutacja — pełna lista w `32_STUDIA_USA.md` sekcja 7

| # | Zadanie | Termin |
|---|---|---|
| R1 | rozstrzygnąć **aerospace vs elektronika** jako kierunek — wpływa na listę uczelni | do 2028 |
| R1a | **Caltech i Stanford dopisane 17 VIII 2026** (`32` sekcja 2.6). Stanford ma aerospace na licencjacie, Caltech nie. Oba **need-aware wobec obcokrajowców** | ustalone |
| R1b | **Lista rozszerzona o dwie kategorie** (`32` sekcja 2.8). Aerospace z pieniędzmi: **MIT, Princeton, Notre Dame**. Pod tematykę projektu: **Brown** (BrainGate, need-blind). Plus ścieżka stypendiów za osiągnięcia i opcja europejska | ustalone |
| R2 | CMU: need-blind czy need-aware wobec obcokrajowców | jesień 2027 |
| R3 | Georgia Tech: czy wybór kierunku jest wiążący przy aplikacji | jesień 2027 |
| R4 | czy CMU ma aerospace na licencjacie | jesień 2027 |
| ~~R5~~ | **ZAMKNIĘTE 17 VIII 2026.** Liczb o „3–4× wyższych szansach" nie da się doprowadzić do źródła — wykreślone (K-068). Twarde dane to CDS sekcja C7: u Caltechu dorobek pozalekcyjny w drugim stopniu wagi, poniżej ocen, testów, esejów i rekomendacji. `32` sekcja 3.1 | zrobione |
| R6 | terminarz SAT/TOEFL | **częściowo zamknięte:** struktura, progi, terminy 2026/27 i powtarzanie w `32` sekcji 4.1. Zostaje ułożenie własnego terminarza pod aplikacje z jesieni 2028. Egzamin z angielskiego: progi i nowa skala TOEFL w sekcji 4.2 |
| R7 | ustawić rekomendacje w szkole | wiosna 2028 |
| R8 | pytanie do OKE o termin dodatkowy matury (dotyczy tylko ISEF 2029) | jesień 2028 |

### Trening prezentacyjny — plan w `31_ANALIZA_STAWKI_2026.md` sekcja 7

| Kiedy | Runda |
|---|---|
| IX 2027, po kampanii pomiarowej | diagnostyczna |
| IX–X 2027 | adwersaryjna, intensywna, trzy poziomy głębokości |
| III–V 2028 | to samo po angielsku pod ISEF |

`[fakt]` Waga: półfinał Explory 10 z 40, finał Explory część z 10 z 30, **ISEF Interview 25 ze 100 — największa pojedyncza pozycja arkusza.**

---

## Zasady obowiązujące w każdym pliku

Znaczniki pewności przy każdym stwierdzeniu: `[fakt]` `[wniosek]` `[domysł]` `[luka]`.

Każda liczba, na której cokolwiek się opiera: 2–3 niezależne źródła. Jedno źródło — oznaczone przy twierdzeniu, nie w przypisie. **Zgodność trzech streszczeń nie jest weryfikacją** (K-030).

Hierarchia przy sprzeczności: dokument regulaminowy > publikacja recenzowana > preprint > materiał prasowy > blog/forum.

**Zakaz słowa „pierwszy" w materiałach zgłoszeniowych** (K-044). **Liczba pojedyncza w całej dokumentacji** (K-054).

---

## Punkt wejścia dla następnej sesji

**Audyt wykonany 18 VIII 2026 — `35_AUDYT_2026_08_18.md`. Nowa sesja zaczyna od niego, nie od `30`.**

Trzy rzeczy do zrobienia w kolejności: **P11** (reanaliza zbioru 102-osobowego, darmowa, przed jakimkolwiek zakupem), **P5** (używany Cyton do 30 IX), **P12** (sekcja o stanie wiedzy). Pozycja P4 („zamknąć zdanie z twierdzeniem") **zamknięta w `35` §4.2** i przeniesiona do `30`, `34`, `README` i `CLAUDE.md`. Parametry, w których audyt ma się poruszać, są w `34_PARAMETRY_I_RAMY.md` i są **wiążące**: 8 000 zł, 10 h/tydzień, EBED, poprzeczka „gotowy w całości".

**Trzy rzeczy, które audyt miał rozbić — rozbite 18 VIII 2026, odpowiedzi w `35_AUDYT_2026_08_18.md`:**

1. **Kolizja budżetowa z OpenBCI — nie ma jej.** Wariant zalecany to 4 500–7 300 zł wobec 8 000 zł, z rezerwą 30% w środku (`35` §3.1)
2. **Poprzeczka „gotowy w całości" wobec ~230 h — przeszacowana.** Szansa na szczebel A w terminie: **35–50%**, nie ~70% (`35` §3.2)
3. **Drabinka zejść — nie jest życzeniowa w szczeblach B i C, jest w opisie D i E jako równoważnych.** Rzeczywisty próg leży między C a D; terminy dopisane do `34` §6 (`35` §3.3)

~~Trzy rzeczy, które audyt ma rozbić w pierwszej kolejności:~~

1. **Kolizja budżetowa z OpenBCI** — 5 800 zł z 8 000 zł na jeden kupiony przyrząd. Czy twierdzenie „ile kosztuje wygoda" stoi bez zewnętrznego punktu odniesienia (`34` sekcja 3)
2. **Poprzeczka „gotowy w całości" wobec ~230 h do zgłoszenia** przy pierwszym w życiu projekcie PCB (`34` sekcje 2 i 5)
3. **Drabinka zejść** — czy szczeble B–E rzeczywiście zostawiają projekt konkursowy, czy to myślenie życzeniowe (`34` sekcja 6)

---

## Uwaga o gałęziach

Praca z 17 VIII 2026 powstała na gałęzi `claude/isef-engineering-project-pjunzg` i **nie była widoczna z `main`**, przez co nowa sesja zaczęła bez kompletu. Gałęzie zostały zsynchronizowane. **Przy każdym zamknięciu sesji sprawdzić, czy `main` zawiera bieżący stan.**
