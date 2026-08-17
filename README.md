# ISEF — aktywne łożysko magnetyczne z estymacją położenia bez czujników

Repozytorium robocze projektu. Dokumentacja żyje tutaj, nie w wątkach rozmowy.

**Cel:** Explory 2027 **i** 2028 → reprezentacja Polski na Regeneron ISEF (2028 i/lub 2029).
**Cel nadrzędny użytkownika:** studia w USA. ISEF jest drogą, nie celem samym w sobie.

---

## STAN: etap 2 otwarty, projekt wybrany — 17 sierpnia 2026

**Kierunek „nieinwazyjny interfejs neuralny" zamknięty decyzją użytkownika.** Pliki `00`–`13` zostają: przemiał literatury, trzy przejścia audytu i cała metodyka są dorobkiem, a `12_AUDYT.md` pozostaje wzorcem postępowania dla nowego projektu.

### Projekt

> **Aktywne łożysko magnetyczne — wirnik trzymany w powietrzu polem magnetycznym, bez kontaktu — a następnie pomiar tego, ile dokładnie się traci, kiedy usunie się z niego czujniki położenia i zastąpi je samą cewką wykonawczą.**

| Rok | Pytanie | Konkursy |
|---|---|---|
| **1** (2026/27) | Jaką charakterystykę da się osiągnąć i zmierzyć na samodzielnie zbudowanym AMB z własnymi czujnikami na PCB? | Explory 2027, OITwEiM, ISEF 2028 |
| **2** (2027/29) | Ile kosztuje usunięcie czujników i **który** z czterech opisanych w literaturze mechanizmów dominuje? | Explory 2028, ISEF 2029 (Form 7) |

**Twierdzenie** — pomiarowe, z punktem odniesienia wewnętrznym, więc nieunieważnialne cudzą publikacją:

> Na jednym stanowisku self-sensing kosztuje X µm szumu położenia, Y N/mm sztywności i Z dB zapasu wzmocnienia względem tego samego stanowiska z czujnikami na PCB; dominującym ogranicznikiem jest [zmierzone].

**Parametry:** dwa lata, ~890 h (10 h/tydz. w roku 1, potem malejąco), ~9 900 zł z 15 000 budżetu, kategoria ISEF **EBED**, Explory **SDG 9 / Gospodarka i Bezpieczeństwo**.

### Struktura etapu 2

| Plik | Zawartość |
|---|---|
| **`20_PROJEKT.md`** | **czym jest projekt, twierdzenie, dlaczego to, kategorie — czytaj to pierwsze** |
| `21_PLAN_BUDOWY.md` | fazy, kalendarz z terminami, budżet z pozycjami, plan zużycia zasobów zewnętrznych |
| `22_PLAN_POMIAROWY.md` | co mierzone, ile prób, budżet niepewności, eksperymenty rozdzielające mechanizm |
| `23_RYZYKA.md` | drabinka zejść (5 szczebli), ryzyka techniczne, konkursowe, harmonogramowe, bezpieczeństwo |
| `24_ODRZUCONE_KANDYDATY.md` | sześciu kandydatów zabitych przy wyborze, z powodami i źródłami |

### Trzy rzeczy, które ten projekt zdejmuje z poprzedniego planu

1. **Human Participants w całości** — zero badanych, zero formularzy, zero komisji IRB przy szkole. Najcięższa pozycja formalna poprzedniego planu znika.
2. **Nazwany konkurent z terminem** — nie istnieje, bo porównanie jest wewnętrzne.
3. **Scenariusz „nie ma nic"** — dno drabinki zejść (własny czujnik na PCB, skalibrowany i scharakteryzowany) jest osiągalne do stycznia 2027 i samo w sobie jest kompletnym projektem.

**Doszło jedno ryzyko:** wirujący element. Obsługa w `23_RYZYKA.md` sekcja 5.

---

## ETAP 1 — zamknięty 15 sierpnia 2026, dorobek zachowany

Zamknięty po **trzech przejściach audytu adwersaryjnego** (`12_AUDYT.md`). Przeszukane kanały: PubMed, arXiv, Crossref, baza patentów, bazy abstraktów ISEF, regulaminy obu konkursów. **Korekty K-001…K-050.**

**Co z etapu 1 przenosi się do nowego projektu i jest tam używane:**

- **kształt twierdzenia, który przeżył audyt** — pomiarowe, nie o pierwszeństwie, z punktem odniesienia wewnętrznym. Nowy projekt jest zbudowany dokładnie w tym kształcie
- **rzemiosło eksperymentalne skopiowane z ENBM074 (2026)** — warunek kontrolny na tym samym sprzęcie, randomizacja i kontrbalansowanie, replikacja, poprawka na wielokrotne porównania, test mechanizmu. Sekcja 9.2 handbooka zakazuje kopiowania tamtego **rozwiązania**; nie zakazuje kopiowania rzemiosła
- **liczby o lejku i o stawce** — `11_OCENA_SZANS.md`, `13_PODNIESIENIE_SZANS.md`: struktura TOP 5 na obszar, plebiscyt „Bilet na Finał" (próg 904 głosy), EBED 49 projektów vs ENBM 98, wideo półfinałowe jako jedyny nośnik demonstracji w najwęższym miejscu lejka
- **punkt kalibracyjny ENBM079 (2026)** — domowe EEG, 52% trafności przy zadaniu dwuklasowym, trzecia nagroda. Próg wejścia do nagród ISEF jest niski
- **obserwacja o stawce Explory** — żaden z 21 finalistów 2026 nie łączy zbudowanego sprzętu z rygorem pomiarowym. To jest luka pozycyjna i nowy projekt trafia w nią wprost

**Pliki etapu 1:** `HANDBOOK.md`, `00_STRESZCZENIE.md`, `00_PYTANIA_I_LUKI.md`, `01`–`13`, `ISEF_HUMAN_PARTICIPANTS.md`, `ISEF_ARKUSZE_OCENY.md`, `ZRODLA.md`, `DECYZJE.md`, `PRZEKAZANIE.md`.

**Nieaktualne dla nowego kierunku:** `09_UMIEJSCOWIENIE.md`, `10_PROJEKT_DLA_LAIKA.md`, `DECYZJE.md` (dotyczyły interfejsu). `11` i `13` zachowują wartość w częściach o lejku, kategoriach i konkursach — nie w częściach o twierdzeniu.

---

## Otwarte pozycje, żadna nie blokuje startu

| # | Pozycja | Termin |
|---|---|---|
| 1 | policzyć kategorię **ETSD** w bazie abstraktów (ma podkategorię Control Theory) — decyzja o kategorii ISEF dopiero po liczbach | przed zgłoszeniem do ISEF |
| 2 | sprawdzić, czy istnieje praca zestawiająca **oba estymatory na jednym stanowisku** — nie zmienia projektu, zmienia opis wkładu | faza 0, IX 2026 |
| 3 | sprawdzić w *International Rules*, czy **wirujące elementy** mają osobny wymóg na stoisku ISEF | jesień 2027 |
| 4 | pytanie do OKE o **termin dodatkowy matury** kolidującej z ISEF 2029 | jesień 2028 |
| 5 | terminarz **SAT/TOEFL** wobec kalendarza projektu | jesień 2027 |

---

## Zasady obowiązujące w każdym pliku

Znaczniki pewności przy każdym stwierdzeniu: `[fakt]` `[wniosek]` `[domysł]` `[luka]`.

Każda liczba, na której cokolwiek się opiera: 2–3 niezależne źródła. Jedno źródło — oznaczone przy twierdzeniu, nie w przypisie. **Zgodność trzech streszczeń nie jest weryfikacją** (K-030).

Hierarchia przy sprzeczności: dokument regulaminowy > publikacja recenzowana > preprint > materiał prasowy > blog/forum.

**Zakaz słowa „pierwszy" w materiałach zgłoszeniowych obowiązuje dalej** (K-044).
