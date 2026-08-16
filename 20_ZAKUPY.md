# 20 — Zakupy: platforma odniesienia i sprzęt pomiarowy

**Data:** 16 sierpnia 2026
**Odpowiada na:** P4 i P5 z `18_PYTANIA_ETAP2.md` oraz pytanie użytkownika o OpenBCI.

---

## 1. Ceny OpenBCI — odczytane u producenta, nie oszacowane

`[fakt, katalog sklepu OpenBCI odczytany 16 VIII 2026]`

| Pozycja | Cena | Dostępność |
|---|---|---|
| **Cyton Biosensing Board, 8 kanałów** | **1 249,00 USD** | dostępne |
| Cyton + Daisy, 16 kanałów | 2 499,00 USD | dostępne |
| **Ganglion Board, 4 kanały** | **624,99 USD** | dostępne |
| Cyton Dongle (część zamienna) | 249,00 USD | dostępne |
| Ultracortex „Mark IV" (czepek) | 1 399,99 USD | dostępne |
| Earclip Electrode | 79,99 USD | dostępne |
| Gold Cup Electrodes | 54,99 USD | **brak** |
| Dry EEG Comb Electrodes, 30 szt. | 49,99 USD | dostępne |
| Ten20 Conductive Paste | 24,99 USD | dostępne |

**Twoja liczba się zgadza.** 1 249 USD to przy kursie 3,7–4,1 zł/USD `[luka — kursu nie sprawdzałem]` około **4 600–5 100 zł**, a z wysyłką ze Stanów, cłem i VAT realnie **6 000–6 800 zł**.

### 1.1 Korekta mojego oszacowania — K-055

W `15_PROJEKT.md` §3.1 wpisałem „platforma odniesienia ~2 800–4 000 zł". **To było zaniżone o połowę** i oparte na pamięci ceny sprzed lat, a nie na sprawdzeniu. Twoje pytanie wyłapało błąd, którego sam bym nie zauważył do momentu zakupu.

**Skutek dla budżetu całkowitego:** nie 5 700–8 800 zł, tylko **8 900–11 600 zł**, jeżeli kupować Cyton nowy. To zmienia charakter decyzji — z „pozycja do przyjęcia" na „największy wydatek projektu, wymagający uzasadnienia".

---

## 2. Czy realnie użyjemy jej po zbudowaniu własnej płytki — trzy funkcje, dwie prawdziwe

Rozbieram to uczciwie, bo to jest sedno Twojego pytania.

| Funkcja | Czy prawdziwa | Kiedy potrzebna |
|---|---|---|
| **1. Test R1 — czy SSVEP u Ciebie w ogóle działa** | **tak, i jest krytyczna** | **X 2026**, czyli zanim własna płytka istnieje |
| **2. Ubezpieczenie na R2 — własny tor nie zadziała (40%)** | **tak** | II–IV 2027 |
| 3. „Baseline komercyjny" do twierdzenia | **słaba** | — |

**Dlaczego funkcja 3 jest słaba, choć sam ją wpisałem w `13_PODNIESIENIE_SZANS.md` §6:** OpenBCI **nie jest produktem konsumenckim**. To płytka badawczo-hobbystyczna, sprzedawana bez obudowy i bez elektrod. Twierdzenie „mój sprzęt jest lepszy od komercyjnego" oparte na porównaniu z OpenBCI byłoby porównaniem z cudzym prototypem, nie z rynkiem. **Wycofuję ten argument** — nie jest wart 6 000 zł.

**Zostają funkcje 1 i 2, i one nie wymagają ośmiu kanałów za 1 249 USD.** Do testu R1 wystarczą dwa kanały potyliczne i odniesienie.

---

## 3. Pięć wariantów, z ceną i z tym, co się traci

| | Wariant | Koszt orientacyjny | Co daje | Co traci |
|---|---|---|---|---|
| **A** | Cyton 8 kan., nowy | **6 000–6 800 zł** | wszystko, pełne E2 na kupionym sprzęcie | połowa budżetu projektu |
| **B** | Ganglion 4 kan., nowy | **3 000–3 400 zł** | R1 w pełni; E2 w wersji okrojonej (2 aktywne + 2 kandydatów na odniesienie) | **inny układ scalony (MCP3912, nie ADS1299)** — zero transferu wiedzy do własnej płytki |
| **C** | **Cyton używany, eBay ~300 EUR** | **1 300–1 600 zł** | to samo co A | ryzyko zakupu, brak gwarancji |
| **D** | płytka ADS1299 z AliExpress | 400–900 zł | teoretycznie to samo co A | **ryzyko podrobionego ADS1299** `[domysł]` |
| **E** | nie kupować nic, od razu własna płytka | 0 zł | — | **R1 rozstrzyga się dopiero w II 2027**, a przy R2 nie ma planu B |

### 3.1 Rekomendacja: C, z A jako awaryjnym

**Kupić używany Cyton, budżet do 1 600 zł, termin poszukiwań do końca września 2026. Jeżeli do 30 IX nie ma dobrej oferty — kupić Ganglion (B), nie Cyton nowy (A).**

Uzasadnienie: wartość tej platformy leży w tym, że jest **zaufanym punktem odniesienia**. Używany egzemplarz oryginalny zachowuje tę wartość w całości przy jednej czwartej ceny. Cyton to konstrukcja od lat niezmieniona, więc „starsza wersja" nie oznacza gorszej.

**Czego wymagać od oferty używanej — lista do odhaczenia:**
1. **płytka ORAZ klucz USB w komplecie** — sam klucz kosztuje nowy 249 USD, więc oferta bez niego nie jest tania
2. zdjęcie płytki z czytelnymi oznaczeniami układów: **ADS1299** i mikrokontroler **PIC32**
3. sprzedawca dopuszcza zwrot
4. koszyk na baterie albo złącze ogniwa — Cyton **musi** być zasilany bateryjnie
5. po otrzymaniu: uruchomić w OpenBCI GUI i **zewrzeć wejścia, zmierzyć szum RMS** — to jest test odbiorczy i zajmuje kwadrans

### 3.2 Dlaczego odradzam AliExpress, mimo że jest najtańszy

`[domysł, bez twardego źródła — oznaczam wyraźnie]` W środowisku hobbystycznym powtarzają się doniesienia o podrobionych układach ADS1299 w tanich modułach. Nie zweryfikowałem tego u żadnego wiarygodnego źródła i nie twierdzę, że to reguła.

**Ale argument nie wymaga rozstrzygnięcia tej kwestii.** Rola tej platformy to **być przyrządem, któremu ufamy**, kiedy własna płytka da dziwny wynik. Przyrząd odniesienia jest dokładnie tym miejscem, w którym nie wolno wprowadzać niepewności co do autentyczności układu. **Za 400 zł oszczędności kupujemy sobie nierozstrzygalną wątpliwość w momencie, w którym najbardziej potrzebujemy pewności.**

---

## 4. Sprzęt pomiarowy — i tu mam do skorygowania własne rozumowanie

### 4.1 Błąd w `16_PLAN_EKSPERYMENTALNY.md` §2 — K-056

Napisałem: *„E1 wymaga generatora i przyrządu o szumie własnym poniżej mierzonego"*. **To jest nieprawda dla najważniejszego pomiaru E1.**

`[fakt]` Szum wejściowy toru mierzy się **samym torem**: zwiera się wejście przez rezystor i liczy RMS z próbek własnego przetwornika 24-bitowego. Dokładnie tak zrobili autorzy arXiv 2601.01772, uzyskując 0,08 µV RMS. **Żaden zewnętrzny przyrząd nie bierze w tym udziału** — i nie mógłby, bo oscyloskop hobbystyczny ma własny szum rzędu setek mikrowoltów, czyli tysiąc razy większy od mierzonej wielkości.

**Właściwe sformułowanie wymagania:** przyrząd zewnętrzny jest potrzebny **jako źródło znanego sygnału**, nie jako miernik. Mierzy zawsze nasz tor.

### 4.2 Co z tego wynika dla listy zakupowej

| Pomiar | Czego naprawdę wymaga |
|---|---|
| szum wejściowy RMS | **nic zewnętrznego** — zwarte wejście, własny przetwornik |
| dryf długoterminowy | **nic zewnętrznego** |
| **CMRR** | generator sygnału. **Jego własny szum jest sygnałem wspólnym i tłumi się razem z nim**, więc nie musi być drogi |
| pasmo i wzmocnienie | generator + **dzielnik napięcia o znanym stosunku** |
| **kalibracja skali amplitudy** (czy 1 µV to naprawdę 1 µV) | **dzielnik precyzyjny — to jest jedyne miejsce, gdzie dokładność jest krytyczna** |
| jitter próbkowania | generator o stabilnym zegarze (TCXO) |
| debugowanie płytki | oscyloskop — **do tętnienia zasilania i SPI, nie do mikrowoltów** |

### 4.3 Lista zakupowa, w kolejności ważności

`[domysł]` **Wszystkie ceny to rzędy wielkości.** Sklepy renderują ceny po stronie klienta, a przeglądarka w tym środowisku nie ma dostępu do sieci — sprawdź przed zakupem.

| # | Pozycja | Koszt | Konieczność |
|---|---|---|---|
| **1** | **dzielnik precyzyjny do samodzielnego zlutowania** — rezystory 0,1%, dwa–trzy stopnie, 1:1000 i 1:100 | **30–80 zł** | **niezbędny.** Najtańsza pozycja i jedyna, w której dokładność jest krytyczna |
| **2** | **generator funkcyjny** — wystarczy DDS ze średniej półki | 250–600 zł | **niezbędny** dla CMRR, pasma i kalibracji |
| 3 | oscyloskop do debugowania — nowy z serii Rigol DHO800 albo używany DS1054Z | 1 200–2 500 zł | **przydatny, nie niezbędny** — pierwszy kandydat do pożyczenia od brata |
| 4 | zasilacz laboratoryjny | 300–600 zł | przydatny przy uruchamianiu płytki; urządzenie docelowo bateryjne |

**Masz już stację lutowniczą z regulacją i multimetr** — to pokrywa cały montaż i podstawową diagnostykę.

### 4.4 Odpowiedź na Twoje „nie ma miejsca na błąd, bo za słabo mierzy"

**Zgoda co do zasady, ale w tym projekcie zasada prowadzi gdzie indziej, niż się wydaje.** Dokładność pomiaru nie leży w oscyloskopie — leży w **przetworniku 24-bitowym na naszej płytce** i w **dzielniku, który mówi mu, ile wynosi wolt**. Kupowanie drogiego oscyloskopu do mierzenia mikrowoltów byłoby wydaniem kilku tysięcy złotych na przyrząd tysiąc razy za mało czuły do tego zadania.

**Pieniądze przeznaczone na dokładność mają iść w: rezystory 0,1% w dzielniku, przyzwoity generator, i drugą serię PCB** — bo to są miejsca, w których dokładność faktycznie powstaje.

### 4.5 Czego nie da się zmierzyć bez pożyczonego sprzętu

`[luka]` **Jitter próbkowania** i **bezwzględne potwierdzenie CMRR powyżej ~100 dB** wymagają źródła lepszego niż tani DDS. To jest właściwe zastosowanie zasobu „brat", zaplanowane na **luty 2027**, na gotową płytkę v1. Do tego czasu obie liczby podajemy jako katalogowe, z jawnym zaznaczeniem, że nie są własnym pomiarem.

---

## 5. Budżet po korekcie

| Pozycja | Kwota |
|---|---|
| platforma odniesienia — wariant C (używany Cyton) | 1 300–1 600 zł |
| elektrody, pasta, stymulator LED, fotodioda | 300–550 zł |
| dzielnik precyzyjny + generator funkcyjny | 280–680 zł |
| własny tor analogowy (ADS1299, PCB, obudowa, elektrody) | 1 600–2 800 zł |
| rezerwa 30% na drugą serię płytek | 1 000–1 700 zł |
| **razem, wariant zalecany** | **4 500–7 300 zł** |
| *to samo z nowym Cytonem (wariant A)* | *9 200–12 500 zł* |

**Wariant zalecany jest tańszy niż moje pierwotne oszacowanie**, mimo że pierwotne oszacowanie zaniżało cenę OpenBCI o połowę. Powód: wypadł drogi oscyloskop, którego do mikrowoltów i tak nie da się użyć, a platforma schodzi na rynek wtórny.
