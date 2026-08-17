# 30 — Powrót do interfejsu neuralnego. Optymalizacja pod Explory

**Data:** 17 sierpnia 2026, wieczór
**Status:** kierunek bieżący. **Zastępuje pliki `20`–`24`.**

---

## 0. Stan nawigacyjny — przeczytaj to, zanim otworzysz cokolwiek innego

| Pliki | Status |
|---|---|
| `00`–`13`, `HANDBOOK`, `ISEF_*`, `ZRODLA` | **dorobek etapu 1 dla interfejsu neuralnego — AKTUALNE** |
| **`20`–`24`** (aktywne łożysko magnetyczne) | **KIERUNEK ZAMKNIĘTY.** Odrzucony przez użytkownika. Nie czytać jako projekt bieżący. Przenośne są z nich wyłącznie: struktura planu pomiarowego (`22`) i drabinka zejść (`23`) |
| `24_ODRZUCONE_KANDYDATY.md` | aktualne jako rejestr — **dopisać do niego łożysko i miony** |
| **`30`** (ten plik) | **projekt bieżący** |

**Decyzja użytkownika z 17 VIII 2026:** powrót do interfejsu neuralnego. Uzasadnienie jego słowami: cel „bardzo wysokie miejsce na ISEF" uznany za nieosiągalny przy jego budżecie, kontaktach, kompetencjach i czasie; interfejs ma realny potencjał i jest w zasięgu.

**Sześć projektów zaproponowanych i odrzuconych w tej sesji** (łożysko magnetyczne, kamera akustyczna, tomografia mionowa, obrazowanie fali milimetrowej, badanie zmęczeniowe wydruków, maszyna napędzana cyklem termicznym) — powody w `24_ODRZUCONE_KANDYDATY.md`. Nie proponować ponownie.

---

## 1. Znalezisko, które przestawia cały kalendarz

`[wniosek, z dat rekrutacyjnych]` Użytkownik zaczyna drugą klasę IX 2026, matura V 2029, studia od IX 2029. **Aplikacje do uczelni w USA składa się jesienią 2028, decyzje zapadają w marcu 2029.**

> **ISEF 2029 (maj 2029) jest PO decyzjach rekrutacyjnych i nie wchodzi do aplikacji.**
> **Jedyny ISEF, który liczy się dla celu nadrzędnego, to maj 2028 — czyli ścieżka przez Explory 2027.**

To unieważnia logikę planu dwuletniego opisaną w `21_PLAN_BUDOWY.md`. Pod rekrutację liczy się jeden strzał, ten wcześniejszy. Rok drugi zachowuje wartość konkursową i naukową, ale **nie rekrutacyjną**.

---

## 2. Diagnoza użytkownika, przyjęta bez zastrzeżeń

*„Najwięcej punktów traciliśmy na prezentacji i zastosowaniu. (…) Projekt jest już dobry na realia ISEF, ma ładne pytanie — »ile kosztuje nas wygoda«, pomiary itd. Ale pod Explory brakuje mu tej strony laickiej. Tam nie będzie żadnego eksperta od tej dziedziny."*

Diagnoza trafna. Explory ocenia w finale trzy obszary po równo: doskonałość merytoryczna i jakość wykonania, praktyczna stosowalność, oddziaływanie społeczne. Projekt w wersji „patrzę na migającą tablicę i skręcam" wypada dobrze w pierwszym i słabo w dwóch pozostałych.

---

## 3. Propozycja użytkownika i dlaczego jej nie przyjmuję w tej postaci

**Propozycja:** przerzucić się na sterowanie wyobrażeniem ruchu, żeby uciec od migającego bodźca.

**Cel słuszny, mechanizm najgorszy z możliwych.** `[fakt]` Liczby z literatury:

| Wielkość | Wartość |
|---|---|
| dokładność dwuklasowa u wytrenowanego użytkownika | **70–85%** |
| odsetek osób poniżej progu 70% przy pierwszej sesji | **55,6%** |
| odsetek utykających trwale w przedziale 60–80% | **~70%** |
| **odsetek osób niezdolnych do opanowania tego w ogóle** | **15–30%** |

Dwie konsekwencje:

1. **Przy stoisku pojazd myli się co czwarty do co szósty raz.** Demonstracja, która zawodzi przy jurorze, jest gorsza niż nudna demonstracja, która działa.
2. **Psuje stronę ISEF-ową.** Twierdzenie „ile kosztuje wygoda" mierzy wpływ **sprzętu**. Zmienność wyobrażenia ruchu między sesjami przykryłaby mierzony efekt — pomiar właściwości układu zamieniłby się w pomiar dziennej formy operatora.

---

## 4. Przebudowa — trzy zmiany, wszystkie realne, żadna nie jest trikiem

### 4.1 Bodziec wyprowadzony z twarzy do świata

Bodziec nie musi być tablicą przed użytkownikiem. Umieszczony **na celach** — na pojeździe, na przeszkodach, na punktach docelowych — powoduje, że użytkownik patrzy tam, dokąd chce jechać, a nie na migacz.

Niezawodność zostaje na poziomie 90–95%, bo mechanizm detekcji jest ten sam. Zmienia się wyłącznie umiejscowienie bodźca.

### 4.2 Jedno wykrycie = jedna pełna intencja

Zamiast dwudziestu komend kierunkowych — **jedno wskazanie celu**, a pojazd dojeżdża sam, omijając przeszkody.

To jest ta sama dźwignia, którą wykorzystał projekt referencyjny ENBM074 (2026): **nie porzucił paradygmatu, zmienił znaczenie jednego wykrycia.** Warstwa sygnałowa jest ograniczona fizyką; warstwa definicji zadania nie jest ograniczona niczym. To jedyne miejsce w tym problemie, gdzie da się uzyskać efekt wielokrotny zamiast procentowego.

Architektura nazywa się **sterowaniem dzielonym**: interfejs dostarcza cel, maszyna wykonuje trasę. Jest to opisana, uznana klasa rozwiązań stosowana w realnych systemach wspomagających.

**Warunek uczciwości, nienegocjowalny.** Na plakacie i przy stoisku musi stać wprost, że pojazd porusza się autonomicznie, a interfejs wybiera cel. Odpowiedź na pytanie „czyli autko samo jeździ?" ma brzmieć: *tak, a mój wkład jest w tym, ile intencji da się przekazać na jedno wskazanie i ile z tego zostaje, gdy urządzenie robi się wygodne.* Nieprzygotowana odpowiedź kosztuje wiarygodność całego stoiska. `[fakt]` Standardy etyczne Explory (Załącznik nr 1, Kodeks Etyki PAN) wymagają krytycyzmu wobec własnych wyników.

### 4.3 Strona społeczna zbudowana od nowa

Uczciwe zastosowanie: **komunikacja i sterowanie dla osób, które nie mogą mówić ani się poruszać.** To nie jest naciągnięcie — to jest funkcja tej technologii.

**Wycofuję wcześniejszą rekomendację ucieczki do obszaru Gospodarka i Bezpieczeństwo.** Była wyprowadzona dla wersji projektu bez demonstracji i przy tej wersji jest błędna. Obszar Człowiek i Społeczeństwo jest najgęstszy, ale wchodzi się tam z jedyną rzeczą, której projekty biologiczne z mentorami akademickimi nie mają: **działającym urządzeniem, które robi coś na oczach jury.**

---

## 5. Co ta przebudowa kosztuje

| Pozycja | Koszt |
|---|---|
| **warstwa autonomii pojazdu** — czujniki odległości, omijanie przeszkód, dojazd do punktu | kilkadziesiąt godzin, do wpisania w harmonogram, nie do dorobienia wiosną |
| przećwiczona odpowiedź o autonomii | godziny, ale obowiązkowe |
| wideo półfinałowe z **licznikiem skuteczności na ekranie** | uczciwsze i robi lepsze wrażenie niż zmontowany jeden udany przejazd |

---

## 6. Co przeżywa bez zmian po stronie ISEF

Twierdzenie **„ile kosztuje nas wygoda"** stoi w całości. Zyskuje nawet jednostkę lepszą niż surowa dokładność: **informacja przypadająca na jedno wskazanie**, która jest mierzalna i ma znaczenie dla użytkownika końcowego.

Reszta dorobku etapu 1 — przemiał literatury, trzy przejścia audytu, `ISEF_HUMAN_PARTICIPANTS.md`, arkusze oceny — obowiązuje bez zmian.

---

## 6a. Poprawki z 17 VIII 2026, wieczór — obowiązujące

### 6a.1 Liczba pojedyncza. Projekt jest autorstwa użytkownika

**Zakaz pisania „my", „nasz", „zrobiliśmy" w dokumentacji projektu i we wszystkich materiałach.** Projekt jest indywidualny i jego autorem jest użytkownik. Rola modelu jest doradcza i taka ma być nazywana.

`[fakt]` To nie jest kwestia stylu. Regulamin Explory (Załącznik nr 1, standardy etyczne wg Kodeksu Etyki Pracownika Naukowego PAN) oraz reguły ISEF wymagają, żeby praca była własna, a udział osób trzecich jawnie deklarowany. Liczba mnoga w materiałach idących do jury zaciemnia autorstwo.

### 6a.2 Mowa syntetyczna wypada z demonstracji

**Powód: kolizja z projektem referencyjnym ENBM074 (2026).** Makieta, w której urządzenie wypowiada zdania wybrane jednym wskazaniem, jest tym samym rejestrem co „rozstrzyganie intencji zamiast literowania" — czyli ścieżką zakazaną w `08_KONKURENCJA_ISEF.md` sekcja 2.3 i w sekcji 9.2 handbooka.

| Wypada | Zostaje |
|---|---|
| mowa syntetyczna wypowiadająca zdania | sterowanie fizycznymi przedmiotami |
| metryka w słowach na minutę | **dokładność i przepustowość w bitach** |
| rejestr komunikacyjny | rejestr sterowania (decyzja C1) |

**Linia graniczna, której pilnujemy przez cały projekt:** produktem jest **sprzęt i pomiar tego, ile kosztuje wygoda**. W chwili, gdy metryką stają się słowa na minutę, projekt staje się wariantem cudzej pracy.

### 6a.3 Obiekty demonstracyjne kupowane, nigdy budowane

**Reguła: do półfinału nie powstaje nic, co nie jest interfejsem.** Każda godzina warsztatu włożona w rekwizyt jest godziną zabraną urządzeniu, a oceniane jest urządzenie.

Zestaw demonstracyjny: żarówka sterowana bezprzewodowo (~50 zł), gniazdko sterowane bezprzewodowo z lampką lub wentylatorem (~60 zł), opcjonalnie brzęczyk przywoławczy (~30 zł). **Poniżej 200 zł, zero godzin warsztatu.**

`[wniosek]` **Kupione przedmioty są też lepszym dowodem uczciwości niż zbudowane.** Przy własnoręcznej makiecie pierwsze pytanie brzmi „co jest w środku". Przy zwykłej żarówce ze sklepu nie pada.

### 6a.4 Poprzeczka „w całości, nie prototyp"

Decyzja użytkownika: interfejs ma być na półfinał gotowy w całości, nie w wersji prototypowej.

`[wniosek]` To jest poprzeczka **wyżej** niż wcześniejsze oszacowanie „urządzenie działa i ma pomiary do maja 2027" (~70%). Reguła 6a.3 jest głównym mechanizmem ochrony tej poprzeczki. Do przeliczenia przy budowie harmonogramu.

---

## 7. Pozycje otwarte

| # | Pozycja | Termin |
|---|---|---|
| 1 | przeliczyć harmonogram całego projektu pod **jeden cykl** (Explory 2027 → ISEF 2028), bo rok drugi nie liczy się rekrutacyjnie | przed planowaniem budowy |
| 2 | rozstrzygnąć, gdzie fizycznie siedzi bodziec na celach i czy nie psuje to warunku „zero hełmów" | etap projektowy |
| 3 | zaplanować warstwę autonomii jako osobny podprojekt z własnym terminem | j.w. |
| 4 | `[luka]` czy CMU jest need-blind czy need-aware wobec obcokrajowców | jesień 2027 |
| 5 | dopisać łożysko i miony do `24_ODRZUCONE_KANDYDATY.md` | przy najbliższej okazji |
