# PRZEKAZANIE — start etapu 2

> ## ⚠ PLIK CZĘŚCIOWO NIEAKTUALNY — 16 VIII 2026
>
> **Oś projektu opisana w tym pliku (analogowa kompensacja artefaktu szczękowego) upadła pierwszego dnia etapu 2.** Zbiór danych Kołodzieja okazał się publiczny; reanaliza pokazała, że przyrost +9 pp należy w całości do **Cz**, a kanał szczękowy dokłada 0,3 pp. `KOREKTY.md` **K-051**, **K-052**, **K-053**.
>
> **Aktualny stan: `14_REANALIZA.md` → `15_PROJEKT.md` → `16_PLAN_EKSPERYMENTALNY.md` → `17_RYZYKA.md` → `18_PYTANIA_ETAP2.md`.**
>
> **Co w tym pliku dalej obowiązuje:** sekcja 3 poza wierszem o osi naukowej, sekcja 5 (wzorce błędów) i sekcja 6 (środowisko). **Sekcje 4.1 i 4.2 są wykonane** — patrz niżej.


**Data:** 15 sierpnia 2026, po zamknięciu etapu 1
**Po co ten plik:** etap 1 jest zamknięty. Ten plik mówi nowej sesji, co zastaje, czego nie wolno podważać, i od czego zacząć etap 2.

---

## 1. Stan: ETAP 1 ZAMKNIĘTY

Zamknięty po **trzech przejściach audytu adwersaryjnego**. Odczytane w oryginale: **regulamin ISEF 2026–2027 w całości** (plus roczniki 2024 i 2025 do weryfikacji reguły 12 miesięcy), **regulamin Explory w całości**, oba arkusze oceny ISEF, pełny abstrakt projektu referencyjnego, pełne teksty dwóch kluczowych prac, kilkanaście abstraktów, dwa patenty, oficjalne listy finalistów Explory.

**Przeszukane bazy:** PubMed (E-utilities), arXiv (API), Crossref (API — pokrywa IEEE TBioCAS, ISSCC, ISCAS, BioCAS), Google Patents, baza abstraktów Society for Science.

**Dwadzieścia osiem korekt: K-020…K-047.**

---

## 2. Co przeczytać i w jakiej kolejności

1. **`CLAUDE.md`** — zasady współpracy, obowiązują bezwzględnie
2. **`12_AUDYT.md`** — **najważniejszy plik w repozytorium.** Trzy przejścia audytu, co zostało zabite, co przeżyło i dlaczego. Sekcja 14 to zamknięcie
3. **`DECYZJE.md`** — cztery decyzje użytkownika, wszystkie zapadłe
4. **`10_PROJEKT_DLA_LAIKA.md`** — czym jest projekt, co umie, czego nie umie
5. **`11_OCENA_SZANS.md`** — szanse, w tym rozbicie na poszczególne wyniki (sekcja F)
6. **`KOREKTY.md`** — K-020…K-047. Czytać, bo zawierają wzorce błędów, które się powtarzają
7. reszta wg potrzeby, nawigacja w `00_STRESZCZENIE.md` sekcja 6

---

## 3. Ustalenia zamknięte — nie podważać bez nowego argumentu

| Ustalenie | Podstawa |
|---|---|
| **paradygmat: SSVEP** | wynika z decyzji C2 i z umiejscowienia |
| **umiejscowienie: zwarty moduł potyliczny**, bez łuku, bez drugiego miejsca | K-036, trzy źródła: referencja laplasjanowa optymalna dla SSVEP |
| **rozstaw elektrod: zmienna mierzona, nie założenie** | decyzja użytkownika; płytka ma obsłużyć kilka rozstawów |
| **twierdzenie: przepustowościowe (ITR, bit/min)** | decyzja C2 użytkownika |
| **oś naukowa: analogowa kompensacja artefaktu SZCZĘKOWEGO przed wzmocnieniem** | K-026, K-043; punkt odniesienia Kołodziej 2026 (+9 pp cyfrowo) |
| **kalendarz: kampania pod ISEF od V 2027** | K-023, K-046 — potwierdzone na trzech rocznikach regulaminu |
| **gabaryt: nic zbliżonego do opaski przechylonej na tył głowy** | granica twarda użytkownika |
| **zakaz słowa „pierwszy" w materiałach zgłoszeniowych** | K-044 — nazwany konkurent |

---

## 4. Od czego zacząć etap 2

Handbook, sekcja 11, żąda pięciu rzeczy. Ocena szans jest zrobiona z wyprzedzeniem. Zostają cztery:

1. **gotowy projekt** — co konkretnie budujemy, z czego, za ile, w jakiej kolejności, z kamieniami milowymi w kalendarzu z sekcji 3 handbooka
2. **twierdzenie w jednym zdaniu, z baseline'em** — szkielet jest, wymaga domknięcia
3. **plan eksperymentalny** — co mierzone, ile prób, jakie zakresy, jaka niepewność. **To jest największy blok pracy**
4. **ryzyka z planem awaryjnym** dla każdego

### 4.1 Trzy tory na jesień 2026, dwa niezależne od powodzenia trzeciego

**Tor A — sprzęt kupiony.** Moduł ADS1299, stymulator migający (diody, nie ekran — Kołodziej używał LED-ów), pierwsze własne zapisy z potylicy. Cel: **własny, zmierzony punkt wyjścia**.

**Tor B — dekodowanie.** Dwa publiczne zbiory na licencji CC-BY: Zhu 2021 (**102 osoby**, 12 celów, elektrody mokre i suche) oraz Lee 2021 (24 osoby, ear-EEG + skalp, ERP i SSVEP, EOG, IMU). Cel: klasyfikator odtwarzający opublikowane liczby.

**Tor C — własny sprzęt.** Nauka PCB, projekt front-endu z kompensacją. Tu leży wkład naukowy i tu leży ryzyko.

**Kolejność: A i B równolegle od zaraz, C po opanowaniu projektowania płytek.** Wszystko przed majem 2027 jest poza oknem 12 miesięcy ISEF, więc to jest czas rozwojowy.

### 4.2 Dwie rzeczy do wyciągnięcia z literatury na start

1. **Pełny tekst Kołodziej i in. 2026** (PMC12899023, otwarty dostęp) — konkretnie **rozbicie udziału kanału szczękowego wobec karkowego**. Podali, że szczęka i Cz były najskuteczniejsze, ale nie odczytałem rozbicia. To jest pierwsza liczba potrzebna do projektu układu.
2. **Problem Cz** (K-045) — Kołodziej ustalił, że Cz jest jednym z dwóch najlepszych kanałów pomocniczych, a Cz leży na wierzchołku głowy, czyli poza dopuszczalną formą. Ile korzyści przeżywa bez Cz — do zmierzenia, i jest to osobne, publikowalne pytanie.

### 4.3 Dwie rzeczy poza komputerem

Użytkownik zgłosił, że z komisją IRB i formalnościami nie będzie problemu, więc te pozycje schodzą z listy ryzyk. Zostaje:

- **mail do FZT i do Funduszu ZDOLNI** — czy start w Explory i EUCYS można łączyć
- **regulamin El-Robo-Mech XII i OITwEiM 2026/27** — ukażą się jesienią 2026

---

## 5. Wzorce błędów z tej sesji — czytać przed pierwszą korektą

Poprzednia wersja tego pliku wymieniała wzorzec: **budowanie mocnego twierdzenia na własnym założeniu, bez sprawdzenia.** Etap 1 dołożył trzy nowe i wszystkie są moje.

1. **Zmiana konfiguracji projektu nie wywołała ponownego audytu prior art.** Pierwsze przeszukanie robiłem dla wersji dousznej; po przejściu na potylicę nie powtórzyłem go. Praca Kołodzieja (O1/O2/Oz) nie mogła wyjść pod zapytaniami o ucho. **Każda zmiana umiejscowienia, paradygmatu albo osi wymaga powtórzenia przeszukania.**
2. **Przenoszenie osi projektu razem ze zmianą miejsca, wbrew własnemu zapisowi** (K-042). Plik `09` mówił wprost, że przy potylicy oś trzeba wyprowadzić od nowa. Zignorowałem to.
3. **Przesadzone korekty — trzy przypadki** (K-029/K-047, K-040). Korygowałem zbyt pewnie, na pierwszym znalezionym dopasowaniu, nie sprawdzając, czy autorzy nie mają kilku prac o zbliżonym tytule, i nie czytając pełnego tekstu, zanim podważyłem liczbę.

**Reguła operacyjna, która z tego zostaje:** przed skorygowaniem czegokolwiek — sprawdź, czy nie ma drugiej pracy tych samych autorów, i czy masz pełny tekst, a nie sam abstrakt.

---

## 6. Sprawy techniczne środowiska

- **sieć działa.** Zweryfikowane: `societyforscience.org`, `explory.pl`, `pubmed.ncbi.nlm.nih.gov`, `export.arxiv.org`, `api.crossref.org`, `patents.google.com`, `ti.com`, `isef.net`, `sspcdn.blob.core.windows.net`, `pmc.ncbi.nlm.nih.gov`
- **przeglądarka nie działa** — Chromium jest zainstalowany, ale nie ma dostępu do sieci nawet przez proxy (`ERR_CONNECTION_RESET`). Stron renderowanych po stronie klienta nie odczytasz. Obejścia, które zadziałały: metatagi (`isef.net`), pliki PDF publikowane obok strony (`Wyniki_Polfinal_2026.pdf`), formularze POST (`abstracts.societyforscience.org`)
- **kanały do literatury, w kolejności użyteczności:** PubMed E-utilities (najlepszy, indeksuje też IEEE TBioCAS i TBME), **Crossref API** (pokrywa ISSCC, ISCAS, BioCAS — czyli konferencje układowe, których nie ma w PubMed), arXiv API. **OpenAlex i Semantic Scholar odmówiły** — wyczerpany limit zapytań, HTTP 429
- **`pypdf` wymaga naprawy `cffi`** przed użyciem: `pip install --force-reinstall cffi`
- **uwaga na polskie cudzysłowy** w skryptach Pythona pisanych w heredoc — znak zamykający jest zwykłym `"` i kończy napis
- **gałęzie:** `main` oraz `claude/verify-complete-docs-mmu2qn`. Po zamknięciu etapu 1 obie mają identyczną treść. **Commituj na tę, na której wylądujesz, i nie zajmuj użytkownika gałęziami** — pisze z telefonu

---

## 7. Jedno zdanie na koniec etapu 1

Z czterech kandydujących twierdzeń projektu **przeżyło jedno**, i jest to jedyne, które od początku było formułowane jako pomiar, a nie jako pierwszeństwo. Trzy pozostałe zabił audyt — zanim cokolwiek zbudowano, zanim wydano złotówkę i zanim złożono zgłoszenie. **To jest różnica między tym projektem a dronem.**
