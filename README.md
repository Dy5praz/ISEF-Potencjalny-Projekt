# Interfejs SSVEP w module noszonym — dokumentacja projektu

**Stan na 21 sierpnia 2026.** Projekt indywidualny, autor: Julek. Cel: Explory 2027 → **ISEF 2028**.

---

## Projekt w trzech zdaniach

> **Buduję interfejs, który odczytuje z tyłu głowy, na co patrzysz, i zamienia to na komendę — dla ludzi, którzy nie mogą mówić ani się ruszać.**
>
> **Żeby taki przyrząd dało się nosić, musi być mały, a wtedy obie elektrody siedzą obok siebie i mogą skasować sygnał, który mają mierzyć.**
>
> **Mierzę, jak blisko mogą usiąść, zanim to się stanie — i z której strony — czego nikt dotąd nie zmierzył.**

---

## Czytaj w tej kolejności

### Dla kogoś, kto wchodzi w projekt pierwszy raz

| # | Plik | Po co |
|---|---|---|
| **1** | **`01_PROJEKT_DLA_LAIKA.md`** | czym to jest, bez żargonu. **Zacznij tutaj, niezależnie od tego, kim jesteś** |
| **2** | **`02_TWIERDZENIE.md`** | zdanie obowiązujące, metryka, granice, **trzy gotowe odpowiedzi dla jurora** |
| **3** | **`11_EWOLUCJA.md`** | jak projekt doszedł do tego kształtu: cztery zabite twierdzenia, kto je zabił, jakie decyzje zapadły |

### Dla pracy nad projektem

| Plik | Zawiera |
|---|---|
| **`03_SPRZET.md`** | tor sygnałowy, rozkład ośmiu elektrod, stymulator, bezpieczeństwo, **zakupy i budżet** |
| **`04_PLAN_POMIAROWY.md`** | rejestracja twierdzeń z góry, eksperymenty E0–E5, częstotliwości, liczba prób |
| **`05_STAN_WIEDZY.md`** | **wszystko opublikowane przeliczone na bit/min**, sześć prac do cytowania, mechanizm falowy, dlaczego pole jest puste |
| **`06_RYZYKA.md`** | dwanaście ryzyk z planami awaryjnymi, **drabinka zejść z terminami** |
| **`07_HARMONOGRAM.md`** | kamienie milowe od dziś do ISEF 2028, lista zadań |
| **`08_KONKURSY.md`** | Explory i ISEF: regulaminy, kryteria, arkusze oceny, stawka, trening prezentacyjny |
| **`09_FORMALNOSCI.md`** | Human Participants, komisja IRB, formularze, reguła dwunastu miesięcy |
| **`10_STUDIA_USA.md`** | cel nadrzędny: uczelnie, kalendarz rekrutacyjny, SAT i egzamin z angielskiego |
| **`12_REANALIZA.md`** | **jedyny własny pomiar, jaki projekt dotąd ma** — reanaliza cudzych danych, odtworzona dwukrotnie |
| **`METODA.md`** | jak się w tym projekcie sprawdza literaturę: procedura tożsamości, trzy kanały przeszukania, stan dostępu do baz |
| **`KOREKTY.md`** | rejestr błędów, **K-001…K-101**. Dopisuj każdy nowy |
| **`analiza/`** | jedenaście skryptów w Pythonie — FBCCA, TRCA, SVM, montaże, okna, harmoniczne |
| **`archiwum/`** | 42 pliki poprzednich wersji. **Nic nie zostało usunięte** |

---

## Stan bieżący

**Twierdzenie** — pełne brzmienie w `02_TWIERDZENIE.md`:

> Mierzę, o ile spada dokładność i przepustowość interfejsu SSVEP, gdy elektroda odniesienia musi zmieścić się w module noszonym na potylicy zamiast leżeć w miejscu standardowym, i wyznaczam najmniejszą odległość, przy której przepustowość jeszcze się nie załamuje.

**Parametry, wiążące:** budżet **8 000 zł** · **10 h/tydzień** · kategoria ISEF **EBED** · obszar Explory **Człowiek i Społeczeństwo** · poprzeczka **„gotowy w całości, nie prototyp"**.

**Metryka:** dokładność i **ITR w bitach**, zawsze z podaniem N, P i t. **Nigdy słowa na minutę.**

**Pewność, że przegląd literatury jest domknięty: 97%.** Rozbiór — `05_STAN_WIEDZY.md` §10.

| Cel | Szansa |
|---|---|
| finał Explory | ~50% |
| reprezentacja na ISEF | **~14%** |
| Nagroda Główna Explory | **~5%** |
| **wartość dla aplikacji na studia, niezależna od wyniku** | **~100%, jeżeli projekt powstanie** |

---

## Co jest teraz do zrobienia

| # | Zadanie | Termin |
|---|---|---|
| **P5** | **szukać UŻYWANEGO Cytona, do 1 600 zł.** Warunki odbioru w `03_SPRZET.md` §7.1. Bez oferty do terminu — nowy Ganglion, nie nowy Cyton | **do 30 IX 2026** |
| **P11** | **reanaliza zbioru Zhu i in. 2021** (102 osoby, PMID 33578754, publiczny) — kod z `analiza/` już działa, koszt zero złotych | IX 2026 |
| **P14** | trzy pytania do FZT jednym mailem: SRC jako IRB · łączenie z EUCYS · **czy badanie na sobie jest zwolnione** | jesień 2026 |
| **E0** | **przesiew: czy SSVEP działa u autora.** ~20 minut na kupionej platformie. **Najważniejszy punkt w całym planie** | **X 2026** |
| **P20** | kontrola grafu cytowań co pół roku (Wu i Su 2014, Diez 2010) | co pół roku |
| **P37** | **nauka projektowania PCB — zacząć we wrześniu.** **Zatwierdzone 21 VIII 2026** | **IX 2026** |
| **P34** | rozstrzygnąć przy projekcie płytki, czy DRL mieści się na spodzie obudowy, czy zostaje na przewodzie do karku (`03_SPRZET.md` §4.1) | I 2027 |
| **P38** | **[!] decyzja: czy dokładamy E6** — tryb bez sterowania wzrokiem, **11–15 h**, nie rusza modułu, elektrod ani metryki. Zabija zarzut o kamerkę demonstracją zamiast argumentem (`05_STAN_WIEDZY.md` §7) | **czeka** |
| **P35** | **zmierzyć taśmą własny łuk nasion–inion** — pięć minut, zero złotych | **od ręki** |

**Zamknięte 21 VIII 2026:**
- **P28a** — dwa cienkie przewody w bok do O1 i O2 dopuszczone; gabaryt ~32×48×12 mm zostaje w mocy
- **P36** — elektroda 5 przeniesiona na **Iz**, symetrycznie do POz. Para kierunkowa przestaje mieszać kierunek z odległością (K-106)
- **P37** — nauka PCB przesunięta na IX–X 2026
- **materiał półfinałowy** przeniesiony na III–IV 2027; maj i czerwiec zostają na kampanię (K-107)

Pełna lista: `07_HARMONOGRAM.md`.

---

## Zasady obowiązujące w każdym pliku

**Znaczniki pewności przy każdym stwierdzeniu:** `[fakt]` `[wniosek]` `[domysł]` `[luka]`.

**Każda liczba, na której cokolwiek stoi: 2–3 niezależne źródła.** Jedno źródło — oznaczone przy twierdzeniu, nie w przypisie.

**Liczba pojedyncza w całej dokumentacji.** Projekt jest indywidualny, autorem jest Julek, rola modelu jest doradcza.

**Zakaz słowa „pierwszy" w materiałach zgłoszeniowych.** Twierdzenie jest pomiarowe, nie o pierwszeństwie.

**Zdanie o luce ma jedną dopuszczalną postać i nie wolno go skracać:** *nie ma tego w dziewięciu bazach naukowych, trzech niezależnych grafach cytowań, sekcjach metod 178 prac i trzynastu rocznikach abstraktów ISEF.*
