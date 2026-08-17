# 23 — Ryzyka i drabinka zejść

**Data:** 17 sierpnia 2026

`[fakt, sekcja 11 handbooka]` *„Nie ma opcji, że nie wyjdzie. Jak coś nie działa — szukasz rozwiązania. Jak dalej nie działa — dopiero wtedy schodzisz o poziom niżej w ambicji. Każde zejście zapisujesz z powodem i z tym, co zostało poświęcone. Nie schodzisz po cichu."*

Ten plik jest drabinką zejść napisaną **z góry**, żeby zejście było decyzją, a nie osunięciem.

---

## 1. Drabinka: co zostaje na każdym szczeblu

| Szczebel | Zakres | Co poświęcone | Czy to nadal projekt konkursowy |
|---|---|---|---|
| **A — pełny** | dwie osie promieniowe, wirnik obracający się, porównanie: czujniki vs dwa estymatory | nic | tak, cel |
| **B** | dwie osie, **bez obrotu**, porównanie pełne | odpowiedź na niewyważenie, prędkości krytyczne, cała rodzina P10 | **tak** — twierdzenie główne stoi w całości, bo dotyczy pomiaru położenia, a nie wirowania |
| **C** | **jedna oś**, porównanie czujnik vs estymator | sprzężenie skrośne osi, czyli jedna z czterech hipotez mechanizmu | tak, słabsze o jeden wymiar |
| **D** | jedna oś, **tylko czujniki**, pełna charakteryzacja + własny czujnik na PCB jako wkład | całe pytanie roku 2 | **tak** — zostaje scharakteryzowany czujnik i scharakteryzowany układ regulacji; to jest nadal więcej pomiarów niż ma jakikolwiek finalista Explory 2026 |
| **E — dno** | sam czujnik prądów wirowych na PCB, skalibrowany i scharakteryzowany, bez lewitacji | wszystko oprócz metrologii czujnika | **tak, i to jest ważne** — karta katalogowa własnego czujnika z kalibracją wobec wzorca jest kompletnym, uczciwym projektem inżynierskim |

`[wniosek]` **Właściwość, której nie miał poprzedni plan: dno drabinki jest osiągalne w cztery miesiące i nadal jest projektem.** Poprzedni projekt miał scenariusz „własna płytka nie wyszła, nie ma nic". Tutaj szczebel E jest osiągnięty w fazie 2, czyli w styczniu 2027, i wszystko powyżej jest nadbudową.

**Reguła schodzenia:** zejście o szczebel wymaga wpisu do `KOREKTY.md` z datą, powodem liczbowym i wskazaniem, co zostało poświęcone. Bez wpisu zejście się nie liczy i trzeba wrócić.

---

## 2. Ryzyka techniczne

| # | Ryzyko | `[domysł]` P | Skutek | Co robimy |
|---|---|---|---|---|
| T1 | pętla nie stabilizuje się mimo poprawnego sprzętu | 25% | brak lewitacji | poziom zerowy (faza 1) jest udokumentowanym ćwiczeniem dydaktycznym — **MIT publikował zestawy maglev do kursu sterowania**; zaczynamy od kopii znanej ścieżki, nie od własnego pomysłu. Regulator: najpierw wyprzedzająco-opóźniający albo PID, dopiero potem cokolwiek ambitniejszego |
| T2 | czujnik na PCB za bardzo zaszumiony albo za wolny | 30% | brak dobrego odniesienia | **dwie niezależne ścieżki od początku**: cewka prądów wirowych ze scalonym przetwornikiem indukcyjności ORAZ prosty czujnik optyczny cieniowy (dioda + szczelina + fotodioda), który jest tani, szybki i bardzo mało szumi. Jeden jest odniesieniem dla drugiego |
| T3 | **estymacja bez czujnika nie działa** | 40% | pytanie roku 2 bez odpowiedzi pozytywnej | to **nie jest porażka**, tylko wynik — patrz `22_PLAN_POMIAROWY.md` sekcja 6. Warunek: powód musi być **zmierzony**, a nie zgadnięty. Temu służy sekcja 5 planu pomiarowego |
| T4 | tor pomiaru prądu ma za małe pasmo, żeby złapać nachylenie tętnienia | 35% | estymator nr 1 nieosiągalny | estymator nr 2 (wstrzykiwanie HF) jest ścieżką niezależną i wymaga innych własności toru. **Dwa estymatory istnieją w planie właśnie po to, żeby nie było jednego punktu awarii** |
| T5 | wirnik niewyważony, drgania psują pomiary | 40% | rozrzut zamiast wyniku | szczebel B (bez obrotu) usuwa to całkowicie; wyważenie przez firmę brata jako pozycja planowana |
| T6 | brak dostępu do obróbki mechanicznej z wymaganą tolerancją | 30% | opóźnienie fazy 3 | stojan z przerobionego stojana silnika BLDC albo z gotowych rdzeni E; wirnik z wałka szlifowanego kupionego gotowego (wałki liniowe h6 są tanie i dokładne) |

---

## 3. Ryzyka konkursowe i formalne

| # | Ryzyko | Co robimy |
|---|---|---|
| K1 | **rubryka oddziaływania społecznego w finale Explory** — temat przemysłowy przegrywa z medycznym i środowiskowym | wybór SDG 9 i obszaru Gospodarka i Bezpieczeństwo, czyli obszaru najsłabiej obsadzonego (`20_PROJEKT.md` 7.2). Argument przygotowany: maszyny bez smaru to brak skażenia olejem i brak przestojów serwisowych, a bariera w małych maszynach jest kosztowa |
| K2 | juror ISEF zna dziedzinę i pyta „czym to się różni od self-sensing AMB z literatury" | **odpowiedź przygotowana i przećwiczona**, tak jak w poprzednim projekcie przygotowywano odpowiedź o Kołodzieja: *„niczym co do zasady — zasada jest opisana od lat. Mierzę, ile ta zasada kosztuje na sprzęcie tej klasy i który z czterech opisanych mechanizmów dominuje. Oto liczby."* Nieprzygotowana odpowiedź kosztuje część z 25 punktów za rozmowę |
| K3 | `[luka]` **nie policzyłem kategorii ETSD** (ma podkategorię Control Theory) | policzyć w bazie abstraktów Society for Science **przed zgłoszeniem do ISEF**, tak jak policzono EBED (49 projektów, 43% nagrodzonych) i ENBM (98, 40%). Decyzja o kategorii dopiero po liczbach |
| K4 | ktoś publikuje to samo porównanie | **nie ma znaczenia dla twierdzenia** — jest wewnętrzne. Ma znaczenie dla narracji: wtedy projekt jest niezależnym potwierdzeniem, co nadal jest poprawnym projektem ISEF. **Zakaz słowa „pierwszy" w materiałach zgłoszeniowych obowiązuje dalej (K-044)** |
| K5 | Form 7 odrzucony, bo rok 2 uznany za powtórzenie | podział jest zbudowany jako dwa różne pytania z inną aparaturą pomiarową i innymi zmiennymi niezależnymi (`20_PROJEKT.md` sekcja 6). Formularz wypełniany z dziennika, nie z pamięci |
| K6 | Explory: „projekt indywidualny czy zespół" | indywidualny, decyzja użytkownika z sekcji 1 handbooka. Nie ruszam |

---

## 4. Ryzyka harmonogramowe

| # | Ryzyko | Co robimy |
|---|---|---|
| H1 | faza 1 nie kończy się lewitacją do końca XI 2026 | **twardy punkt kontrolny.** Jeżeli 30 XI 2026 nic nie lewituje — przegląd całego podejścia, nie dokładanie godzin. Wpis do `KOREKTY.md` |
| H2 | zgłoszenie do Explory nie wychodzi do 28 II 2027 | cały cykl przepada. **Zgłoszenie jest pozycją kalendarzową z własnym terminem, niezależną od stanu sprzętu** — regulamin nie wymaga ukończonego projektu |
| H3 | wideo półfinałowe robione w ostatnim tygodniu | wideo ma własny termin: **gotowe do 30 IV 2027**, przed otwarciem okna półfinału. To jest jedyny nośnik demonstracji w najwęższym miejscu lejka |
| H4 | matura zjada rok 2 | godziny na wiosnę 2029 są z góry ścięte do 2/tydzień (`21_PLAN_BUDOWY.md`). Kampania pomiarowa roku 2 kończy się **we wrześniu 2028**, siedem miesięcy przed maturą |
| H5 | SAT/TOEFL kolidują z projektem | `[luka]` nieplanowane w tym pliku, bo nie znam terminarza. **Pozycja do rozstrzygnięcia jesienią 2027**, kiedy będzie wiadomo, na kiedy celuje aplikacja |

---

## 5. Bezpieczeństwo — pozycja nowa, której poprzedni projekt nie miał

**Wirujący element jest jedynym realnym zagrożeniem w tym projekcie i traktuję go poważnie.**

| Zasada | Realizacja |
|---|---|
| masa i prędkość ograniczone projektowo | wirnik rzędu 0,2–0,5 kg; prędkość maksymalna dobrana tak, żeby energia kinetyczna była mała, a nie „tak szybko, jak się da" |
| osłona zawsze | poliwęglan wokół wirnika, montaż uniemożliwiający pracę bez osłony |
| łożyska zapasowe | zwykłe łożyska z luzem większym niż szczelina magnetyczna — przy zaniku sterowania wirnik siada na nie, a nie na stojan |
| brak obrotu na stoisku, jeżeli organizator tego wymaga | demonstracja statycznej lewitacji jest równie efektowna i całkowicie bezpieczna |
| zasilanie | bateryjne albo z zasilacza z izolacją galwaniczną. `[fakt]` Reguły elektryczne ISEF dotyczą **stoiska**, próg to 36 V na obwodach odsłoniętych — projekt mieści się z zapasem |

`[fakt]` Osobna kategoria ryzyka dla urządzeń elektrycznych w ISEF **nie istnieje** — sekcja *Hazardous Chemicals, Activities or Devices* obejmuje substancje kontrolowane, leki, alkohol, broń, promieniowanie, lasery i drony. `[luka]` **Czego nie sprawdziłem: czy wirujące elementy mają osobny wymóg na stoisku ISEF.** Do sprawdzenia w *International Rules* przed zgłoszeniem — pozycja na jesień 2027.

`[fakt]` **Human Participants: nie dotyczy.** Zero badanych, zero formularzy, zero komisji IRB przy szkole. Cała najcięższa pozycja formalna poprzedniego projektu znika.

---

## 6. Rzecz, której ten plik nie może obiecać

`[wniosek]` Nie umiem zagwarantować, że stanowisko zadziała. Umiem zagwarantować, że **każdy szczebel drabinki z sekcji 1 kończy się czymś, co da się pokazać i zmierzyć** — i że najniższy szczebel jest osiągalny w cztery miesiące od startu.

To jest różnica wobec poprzedniego planu, w którym scenariusz „nie wyszło" oznaczał brak przedmiotu na stoisku.
