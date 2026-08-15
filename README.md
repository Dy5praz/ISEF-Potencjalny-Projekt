# ISEF — nieinwazyjny interfejs neuralny

Repozytorium robocze projektu. Dokumentacja żyje tutaj, nie w wątkach rozmowy.

**Cel:** Explory 2027 → reprezentacja Polski na Regeneron ISEF, maj 2028.

---

## Stan na 15 sierpnia 2026, po etapie 1

| Etap | Status |
|---|---|
| Sekcja 14 handbooka — drugie czytanie, luki i pytania | **zrobione** → `00_PYTANIA_I_LUKI.md` |
| Odpowiedzi użytkownika, rundy 1 i 2 | **zebrane** → `00_PYTANIA_I_LUKI.md` sekcje 4b i 4c |
| **Etap 1 — przemiał literatury** | **wykonany w części naukowej; część regulaminowa otwarta** → `00_STRESZCZENIE.md` |
| Etap 2 — opracowanie projektu | wymaga domknięcia pozycji z listy poniżej |

### Dlaczego etap 1 jest częściowy

**Ta sesja działa w niewłaściwym środowisku.** Sesja jest przypisana do `env_01NdKrhepeQo6dVAHusCvQFj` („Projekty"), podczas gdy `Network access: Full` zostało ustawione na `env_01USAAMBR9QZf9W8ERvrVkEA` („Projekty Full Acess", utworzone 15 VIII o 07:42). **Polityka sieciowa idzie ze środowiska sesji, a sesji nie da się przenieść między środowiskami.** Dlatego mimo poprawnych ustawień ta sesja dostaje 403 — sprawdzone tunelem kontenera, WebFetch i curl-em po restarcie kontenera o 14:00.

Działa wyłącznie wyszukiwarka zwracająca tytuły, adresy i streszczenia generowane przez inny model. **Żadna praca źródłowa nie została otwarta.** Etap 1 został wykonany na tym kanale, z widocznym oznaczeniem statusu przy każdej liczbie — pełne postawienie sprawy w `00_STRESZCZENIE.md` sekcja 0.

### Żeby domknąć resztę

**Nowa sesja założona w środowisku „Projekty Full Acess".** Ustawień nie zmieniać — są dobre. Chodzi wyłącznie o wybór właściwego środowiska z listy przy zakładaniu sesji. Gałąź `claude/etap-1-8fsbpm` ma cały dorobek, więc nowa sesja podniesie pracę bez strat.

### Co zostaje do zrobienia po odblokowaniu, w kolejności

1. **`ISEF_HUMAN_PARTICIPANTS.md` pozycje 5 i 7** — czy urządzenie elektryczne przy głowie łamie zwolnienie dla badania na sobie. Jedyna pozycja o bezpośrednich konsekwencjach dyskwalifikacyjnych
2. **pełny abstrakt projektu referencyjnego** (zadanie 4d nr 10) — baza abstraktów Society for Science
3. **projekty neuro/EEG/BCI w finałach Explory 2016–2026** (zadanie 4d nr 11) — liczby, nie wrażenie
4. **oba arkusze oceny ISEF** (zadanie 4d nr 12) — do osobnego pliku
5. **przegląd systematyczny w IEEE Xplore i PubMed** pod kompensację analogową artefaktów przy uchu — domyka `04_LUKI_ZAPISANE.md` sekcja 2
6. **oryginały regulaminów** Explory i El-Robo-Mech
7. weryfikacja liczb oznaczonych `[wniosek, streszczenie]` w plikach 01–08

---

## Struktura

| Plik | Zawartość | Status |
|---|---|---|
| `HANDBOOK.md` | kontekst i zlecenie | źródło |
| `00_PYTANIA_I_LUKI.md` | luki, pytania, odpowiedzi użytkownika, lista zadań 4d | gotowy |
| `00_STRESZCZENIE.md` | **co z etapu 1 wynika — czytaj to pierwsze** | gotowy |
| `01_HISTORIA.md` | rozwój technologii, z datami | gotowy |
| `02_MECHANIZMY.md` | mechanizm fizyczny, po polsku, terminy z definicjami | gotowy |
| `03_SCIANY_FIZYCZNE.md` | fizyczne vs technologiczne; pomiar szumu bez oscyloskopu | gotowy |
| `04_LUKI_ZAPISANE.md` | future work; **weryfikacja osi projektu** | gotowy, sekcja 2 do domknięcia |
| `05_RYNEK.md` | baseline komercyjny; materiały do kontaktu ze skórą | gotowy |
| `06_TABELA_PARAMETROW.md` | metryka porównawcza, widoczność, „skąd ta liczba" | gotowy |
| `07_DEKODOWANIE.md` | paradygmaty, metody, metryki, zbiory danych | gotowy |
| `08_KONKURENCJA_ISEF.md` | kalendarz ISEF, El-Robo-Mech, projekt referencyjny | gotowy, zadania 11 i 12 otwarte |
| `09_UMIEJSCOWIENIE.md` | **gdzie ma być interfejs — porównanie miejsc, decyzja otwarta** | czeka na użytkownika |
| `ISEF_HUMAN_PARTICIPANTS.md` | badania z udziałem ludzi, terminarz wsteczny | **częściowy, priorytet** |
| `ZRODLA.md` | bibliografia z oceną wiarygodności | gotowy |
| `KOREKTY.md` | rejestr błędów, K-001…K-019 | prowadzony |

---

## Ustalenia kierunkowe — stan po etapie 1

Zmiany względem stanu sprzed etapu 1 zaznaczone **pogrubieniem**.

- **zdolność:** sterowanie, nie komunikacja. Odczyt dyskretny, zachowanie sterowanego obiektu ciągłe. **Ustalenie zostaje, ale jego uzasadnienie zostało skorygowane — K-014**
- **kalendarz: potwierdzony.** Finał X 2027 → ISEF V 2028. Teza „jeden strzał" stoi. **K-013 zamyka K-007**
- **sEMG/EOG jako źródło sterowania: zamknięte.** ID.EARS, CHI 2025, pięć gestów przy uchu, >90%. **K-017**
- **kod projektu referencyjnego ENBM074 (2026) jest prawidłowy** — moja poprawka K-012 była błędna i została wycofana. **K-018.** Kody ISEF cytować zawsze z rocznikiem
- **sEMG/EOG jako kanał odniesienia: nadal kandydat na oś**, ale twierdzenie musi być pomiarowe, nie o pierwszeństwie. **K-009 rozstrzygnięte**
- **paradygmat: nieprzesądzony.** Moja rekomendacja paradygmatów słuchowych została podważona; SSVEP wygląda lepiej mimo większej odległości. **K-015**
- **umiejscowienie: DECYZJA OTWARTA, K-019.** Forma zauszna była moim założeniem, nie Twoim wymaganiem. Potylica daje 5–15× większe ITR dla SSVEP i **może być mniej widoczna** (pod włosami, stopień 0). Porównanie miejsc: `09_UMIEJSCOWIENIE.md`. **Miejsce i oś projektu są sprzężone** — przy potylicy oś trzeba wyprowadzić od nowa
- **El-Robo-Mech:** kwalifikuje się tematycznie, ale **to nie jest zewnętrzna walidacja, tylko wymuszony termin. K-016**
- **drukarka:** zakup Q2 wstrzymany, potwierdzone. Właściwy kierunek to druk żywiczny. **Otwarte: czy certyfikowana żywica ISO 10993 jest dostępna dla amatora w Polsce**
- badani, czas, budżet, sprzęt pomiarowy: bez zmian

## Decyzje czekające na użytkownika

1. **C2** — w czym „lepsze od komercyjnych". Rekomendacja po etapie 1: **wariant 2 (metryka użytkowa)** jako oś, wariant 1 jako tabela towarzysząca. Uzasadnienie liczbowe w `06` sekcja 5
2. **skala widoczności** z `06` sekcja 4 — zatwierdzić albo poprawić
3. **E1** — potwierdzenie korekty K-001 (8 miesięcy do El-Robo-Mech, nie 14)
4. **E3** — skąd pochodzą liczby 65 i 3 wpm z sekcji 9.2 handbooka

---

## Zasady obowiązujące w każdym pliku

Znaczniki pewności przy każdym stwierdzeniu:

- `[fakt]` — twarde dowody, źródło sprawdzone
- `[wniosek]` — silne wnioskowanie z faktów
- `[domysł]` — uzupełnianie luki, spekulacja
- `[luka]` — wiadomo, że nie wiadomo

W etapie 1 doszedł znacznik złożony **`[wniosek, streszczenie]`** — twierdzenie oparte na streszczeniu wyszukiwarki, bez otwarcia źródła. Występuje przy większości liczb i **znika dopiero po weryfikacji w oryginale**.

Każda liczba, na której cokolwiek się opiera: 2–3 niezależne źródła. Jedno źródło — oznaczone wyraźnie przy twierdzeniu, nie w przypisie.

Hierarchia przy sprzeczności: dokument regulaminowy > publikacja recenzowana > preprint > materiał prasowy > blog/forum.
