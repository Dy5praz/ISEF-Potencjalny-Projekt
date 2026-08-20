# Kontekst projektu — czytaj to pierwsze

Użytkownik: Julek. **Odpowiadaj po polsku.**

## Co czytać, w tej kolejności

1. **`README.md`** — stan bieżący i mapa plików. Najkrótsza droga do tego, co się dzieje teraz.
2. **`30_POWROT_DO_INTERFEJSU.md`** — **projekt bieżący.** Czym jest, twierdzenie, przebudowa demonstracji, poprawki 6a. Potem `32_STUDIA_USA.md` (cel nadrzędny: uczelnie, SAT, egzamin z angielskiego), `31_ANALIZA_STAWKI_2026.md` (konkurencja), `33_KONKURSY_ROZBIEGOWE.md` (El-Robo-Mech, olimpiada).
   **Pliki `20`–`23` (łożysko magnetyczne) usunięte 18 VIII 2026** — wszystko przenośne jest w **`34_PARAMETRY_I_RAMY.md`** (budżet, godziny, kategoria, drabinka zejść, plan pomiarowy), a rejestr odrzuconych kierunków w `29_ODRZUCONE_KIERUNKI.md`. **`34` czytaj zaraz po `30`.**
3. **`HANDBOOK.md`** — zasady współpracy, cel, kalendarz, ściągawka Explory i ISEF, historia odrzuconych kierunków. **Sekcje 1–8 i 12–13 obowiązują nadal. Sekcje 9–11 dotyczą interfejsu neuralnego i po powrocie do tego kierunku są znowu materiałem roboczym, nie samą historią.**
4. **`KOREKTY.md`** — rejestr błędów, K-001…K-076. Dopisuj każdy nowy.
5. **`12_AUDYT.md`** — wzorzec audytu adwersaryjnego. Metoda zostaje w mocy, treść dotyczy zamkniętego kierunku.

## Zadanie bieżące

**Stan na 18 sierpnia 2026.** Kierunek bieżący to **nieinwazyjny interfejs neuralny sterowany bodźcem wzrokowym, w zwartej formie noszonej** — powrót decyzją użytkownika z 17 VIII 2026. Opis w `30_POWROT_DO_INTERFEJSU.md`, **ten plik zastępuje `20`–`24`**.

**Audyt adwersaryjny wykonany 18 VIII 2026 — `35_AUDYT_2026_08_18.md`. To jest plik do przeczytania zaraz po `30` i `34`.** Wynik: twierdzenie w brzmieniu ogólnym („ile kosztuje wygoda") **zabite przez pracę chińskojęzyczną PMID 40566767** (K-077); wersja wąska przeżyła przeszukanie siedmiu baz. Pewność audytu: **92%**. Osiem sprzeczności między plikami znalezionych i poprawionych (K-077…K-091).

**Najbliższe zadanie: P11 — reanaliza publicznego zbioru Zhu i in. 2021 (102 osoby, PMID 33578754)**, powtórzenie analizy montaży z `14` §5 na próbie ośmiokrotnie większej. Kod z `analiza/` już działa, koszt zero złotych.

Twierdzenie, **brzmienie obowiązujące od 18 VIII 2026** (`35_AUDYT_2026_08_18.md` §4.2 — poprzednie „ile kosztuje wygoda" ma opublikowaną odpowiedź, K-077):

> **Mierzę, o ile spada dokładność i przepustowość interfejsu SSVEP, gdy elektroda odniesienia musi zmieścić się w module noszonym na potylicy zamiast leżeć w miejscu standardowym, i wyznaczam najmniejszą odległość odniesienia od kory wzrokowej, przy której przepustowość jeszcze się nie załamuje — na jednym własnym torze analogowym, tą samą osobą, tym samym paradygmatem.**

Punkt odniesienia wewnętrzny: **ten sam tor analogowy, dwa położenia elektrody odniesienia.** Kupiony OpenBCI to narzędzie kontrolne i ubezpieczenie, **nie punkt odniesienia twierdzenia** (K-071). **Metryka w bitach, nigdy słowa na minutę** (K-055).

Parametry, **ustalone 18 VIII 2026 i wiążące**: **budżet 8 000 zł**, **10 godzin tygodniowo**, kategoria ISEF **EBED**, obszar Explory **Człowiek i Społeczeństwo**, poprzeczka **gotowy w całości, nie prototyp**. Rozbiór i konsekwencje: `34_PARAMETRY_I_RAMY.md`. **Zakupy: `20_ZAKUPY.md` — używany Cyton do 1 600 zł, termin poszukiwań 30 IX 2026.**

**Kalendarz rekrutacyjny jest nadrzędny nad konkursowym:** aplikacje na studia w USA idą jesienią 2028, więc **liczy się ISEF 2028, czyli ścieżka przez Explory 2027**. ISEF 2029 wypada po decyzjach rekrutacyjnych. Harmonogram wymaga przeliczenia pod jeden cykl (P2).

## Ustalenia wiążące, nie do podważania bez nowego argumentu

- **twierdzenie ma być pomiarowe, z punktem odniesienia wewnętrznym.** To jedyny kształt, który przeżył trzy przejścia audytu etapu 1, i jedyny, którego cudza publikacja nie unieważnia. Trzy poprzednie kierunki zginęły dokładnie na tym
- **nie filtruj kandydatów po nowości.** Arkusz inżynierski ISEF nie ma kryterium nowości; Explory §7 pkt 2a dopuszcza „innowacyjny **i/lub** wnosi dodatkową wartość". Filtr to: wykonalność, demonstracja, głębokość pomiaru, obsada kategorii, podział na dwa pytania. Błąd opisany w `KOREKTY.md` K-051, sześciu zabitych kandydatów w `24_ODRZUCONE_KANDYDATY.md`
- **nigdy nie używaj słowa „pierwszy"** w materiałach zgłoszeniowych (K-044)
- **rzemiosło eksperymentalne z ENBM074 (2026) kopiujemy świadomie** — warunek kontrolny na tym samym sprzęcie, randomizacja i kontrbalansowanie, replikacja, poprawka na wielokrotne porównania, test mechanizmu. Sekcja 9.2 handbooka zakazuje kopiowania tamtego **rozwiązania**, nie rzemiosła
- **projekt indywidualny.** Decyzja użytkownika z sekcji 1 handbooka, nie ruszać
- **badani ludzie WCHODZĄ w grę i procedura Human Participants obowiązuje.** Interfejs zbiera sygnał z człowieka, więc `ISEF_HUMAN_PARTICIPANTS.md` jest dokumentem czynnym, nie archiwalnym: Adult Sponsor, Direct Supervisor, formularze, kwestia komisji IRB przy szkole i pytanie do FZT o SRC. **Zdanie „zero badanych ludzi" pochodziło z zamkniętego kierunku łożyskowego i było błędem — K-069**
- **drabinka zejść jest napisana z góry** (`34_PARAMETRY_I_RAMY.md` sekcja 6). Zejście o szczebel wymaga wpisu do `KOREKTY.md` z powodem liczbowym i wskazaniem, co poświęcone. Bez wpisu zejście się nie liczy

## Zasady, których łamanie kosztowało miesiące

Pełna lista w sekcjach 2.1 i 2.2 handbooka. Skrót:

- **znaczniki pewności przy każdym stwierdzeniu:** `[fakt]` `[wniosek]` `[domysł]` `[luka]`. Jeżeli większość odpowiedzi to zgadywanie — powiedz to w pierwszym zdaniu
- **zakaz „nie da się"** bez kompletu trzech: który parametr się nie spina (liczba), wersja projektu z tym parametrem poza pętlą, pomiar przeżywający tę zmianę
- **nie pracuj w ratach.** Zakaz kończenia zdaniem „sprawdzę to w następnej wiadomości"
- **weryfikuj 2–3 razy** każdą liczbę, na której cokolwiek stoi. Jedno źródło — oznacz to przy twierdzeniu, nie w przypisie
- **nie zaczynaj od przyznania racji.** Ale nie podważaj odruchowo, kiedy rozumowanie jest prawidłowe
- **bez emotek**
- zwroty zakazane: „Świetne pytanie", „Masz całkowitą rację", „To ma głęboki sens", „Absolutnie", „Zdecydowanie"
- **dokumentacja żyje w plikach.** Jeżeli ustalenie z handbooka okaże się błędne — popraw handbook, nie tylko odpowiedź, i dopisz wpis do `KOREKTY.md`
- użytkownik jest licealistą drugiej klasy. Zna fizykę i matematykę szkolną, nie zna terminologii specjalistycznej — w tym projekcie dotyczy to teorii sterowania i elektroniki analogowej. **Każdy termin użyty pierwszy raz dostaje wyjaśnienie**

## Uwagi praktyczne

- użytkownik często pisze z telefonu — nie zlecaj mu czynności wymagających przełączania się między aplikacjami, jeżeli da się je wykonać po twojej stronie
- **ZAWSZE SCALAJ DO `main` NA KONIEC SESJI, bez pytania i niezależnie od tego, na jakiej gałęzi wylądowałeś.** Decyzja użytkownika z 18 VIII 2026, cytat: *„Tak, zawsze scalaj nie ważne co."* Powód jest zapisany dwoma korektami: **K-062** (praca całej sesji wylądowała na gałęzi niewidocznej dla nowej rozmowy) i **K-076** (26 plików, których `main` nigdy nie widziała, odzyskane dopiero po trzech dniach). Procedura: commit na gałęzi roboczej → `git checkout main` → `git merge <gałąź>` → `git push -u origin main` → wrócić na gałąź roboczą i wypchnąć ją też. **Nie pytaj użytkownika o zgodę na scalenie — zgoda jest udzielona z góry i bezterminowo.**
- repozytorium ma dwie gałęzie o identycznej treści: `main` i `claude/oto-handbook-instrukcje-g3e7hd`. `main` została dodana 15 VIII 2026 tylko po to, żeby formularz nowej sesji się nie wykrzaczał. **Commituj na tę gałąź, na której wylądowałeś, i nie zajmuj użytkownika gałęziami** — pisze z telefonu
- **środowisko z `Network access: Full` jest konieczne** i to repozytorium było już raz zablokowane brakiem dostępu. Sprawdzaj sieć na starcie: `https://www.societyforscience.org/isef/international-rules/human-participants/`. Przy 403 albo `EGRESS_BLOCKED` — przerwij i powiedz
- **przeglądarka (Chromium) nie ma dostępu do sieci nawet przez proxy.** Stron renderowanych po stronie klienta nie odczytasz. **Obejścia sprawdzone 18 VIII 2026 i działające:** metatagi; **pliki PDF publikowane obok strony** (tak pobrano regulamin Explory); **formularze POST z tokenem sesji i ciasteczkiem** (tak przeszukano bazę abstraktów ISEF, trzynaście roczników); **pełne teksty z `pmc.ncbi.nlm.nih.gov/articles/PMCxxxxxx/`** — działa także dla artykułów chińskojęzycznych; **treść renderowana po stronie serwera** (tak odczytano abstrakty z chińskiej bazy CQVIP, gdy CNKI zrywa połączenie na poziomie TLS). Pełna tabela dostępności 29 baz: `36_ROZBIOR_LI2025_I_PRZESZUKANIE.md` §4. Szczegóły w `PRZEKAZANIE.md` sekcja 5
- **przed napisaniem, że coś jest zajęte, martwe albo zrobione — procedura tożsamości z `37_PROCEDURA_TOZSAMOSCI_I_ROZBIORY.md` §3.** Siedem pytań, **z pełnego tekstu**, werdykt jednym z trzech słów: **tożsamy / sąsiedni / niezwiązany**. Zbieżność tematu nie jest zbieżnością projektu — dwa razy kosztowało to tydzień przebudowy (K-089, K-092)
- **przeszukiwanie po grafie cytowań, nie tylko po słowach.** `[fakt]` W OpenAlex i Semantic Scholar **wyszukiwanie jest płatne albo zablokowane, ale pojedyncze rekordy i cytowania są darmowe**: `api.openalex.org/works/pmid:<PMID>` (daje `related_works` i `referenced_works`) oraz `api.semanticscholar.org/graph/v1/paper/PMID:<PMID>/citations` i `/references`. **Graf cytowań nie zależy od słownictwa** — a to własne słownictwo trzy razy dało w tym projekcie fałszywe „zero trafień" (K-074, K-093)
- **gdy PMC zwraca reCAPTCHA:** `eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=<numer bez PMC>&retmode=xml` oddaje pełny XML. Pełna tabela obejść: `37` §14
- **najlepszy kanał do literatury: PubMed przez E-utilities NCBI.** Indeksuje też IEEE TBioCAS i TBME, więc obejmuje literaturę układową, nie tylko medyczną
