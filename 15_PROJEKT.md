# 15 — Gotowy projekt: co budujemy, z czego, za ile, w jakiej kolejności

**Data:** 16 sierpnia 2026
**Podstawa:** `HANDBOOK.md` §11 punkt 1. Oś projektu po reanalizie — `14_REANALIZA.md` §7.2.
**Zależność:** ten plik zakłada nową oś. Jeżeli użytkownik ją odrzuci, sprzęt i tak zostaje ten sam (§1.4).

---

## 1. Twierdzenie projektu

### 1.1 Jedno zdanie, z punktem odniesienia

> **W nisko‑kanałowym interfejsie SSVEP przepustowość spada monotonicznie wraz ze skracaniem odległości elektrody odniesienia od aktywnej okolicy potylicznej; mierzę tę zależność na własnym torze analogowym i wyznaczam najmniejszą odległość, przy której układ zachowuje przepustowość montażu z odniesieniem odległym — czyli najmniejszy gabaryt, przy którym urządzenie noszalne jeszcze działa.**

> **UZGODNIONE 18 VIII 2026 — K-078.** Zdanie powyżej i zdanie „ile kosztuje wygoda" z `30`/`34`/README **opisywały to samo, ale żaden plik tego nie mówił**, przez co projekt przez dobę miał w plikach bieżących dwa twierdzenia. **Obowiązuje brzmienie ujednolicone** (`35_AUDYT_2026_08_18.md` §4.2):

> **Mierzę, o ile spada dokładność i przepustowość interfejsu SSVEP, gdy elektroda odniesienia musi zmieścić się w module noszonym na potylicy zamiast leżeć w miejscu standardowym, i wyznaczam najmniejszą odległość odniesienia od kory wzrokowej, przy której przepustowość jeszcze się nie załamuje — na jednym własnym torze analogowym, tą samą osobą, tym samym paradygmatem.**

**Punkt odniesienia, podwójny i wewnętrzny** (~~`13_PODNIESIENIE_SZANS.md` §6~~ — punkt 2 wycofany 16 VIII, K-071):
1. **ten sam tor analogowy z odniesieniem na płatku ucha** — górna granica, montaż literaturowy
2. ~~**OpenBCI Cyton, kupiony** — dowód, że własny sprzęt ma sens~~ **Wycofane 16 VIII 2026 (K-071).** Cyton to narzędzie kontrolne i ubezpieczenie, nie punkt odniesienia twierdzenia (`20_ZAKUPY.md` §2)

**Punkt odniesienia zewnętrzny:** reanaliza danych Kołodziej i in. 2026 (`14_REANALIZA.md` §5) — na cudzych surowych danych zejście do montażu różnicowego wewnątrz potylicy kosztuje **9,3 pp** (trzy pochodne) do **24,5 pp** (jedna pochodna). Ta liczba jest **przewidywaniem, które własny pomiar potwierdzi albo obali**, i to jest właściwa rola zewnętrznego punktu odniesienia.

### 1.2 Metryka

Zgodnie z decyzją C2: **dokładność klasyfikacji oraz ITR w bit/min wg wzoru Wolpawa**, zawsze z podaniem N (liczba celów), P (dokładność) i t (czas na decyzję, z jawną konwencją liczenia — zakaz z `06_TABELA_PARAMETROW.md` §0 pkt 2).

### 1.3 Czym to twierdzenie NIE jest

- **nie jest twierdzeniem o pierwszeństwie.** Zakaz słowa „pierwszy" z K-044 obowiązuje bez zmian
- **nie jest twierdzeniem o pobiciu kogokolwiek.** Imperial College robi 102 bit/min za £20 (`12_AUDYT.md` §1.1); nie startujemy w tym wyścigu
- **nie jest twierdzeniem o wynalezieniu elektrody ani układu elektrod** — oba zajęte (PNAS 2025, US 11241183 B2)

### 1.4 Co się dzieje, jeżeli użytkownik odrzuci zmianę osi

Sprzęt z sekcji 2 obsługuje **obie** osie bez zmiany jednego elementu: stara oś potrzebuje kanału mięśniowego (jest, wejście 7), nowa potrzebuje wielu położeń odniesienia (są, wejścia 1–6). **Decyzję o osi można odłożyć do pierwszych własnych pomiarów** i to jest zalecana droga — dokładnie ta sama logika, którą użytkownik przyjął przy umiejscowieniu elektrod.

---

## 2. Architektura sprzętu

### 2.1 Zasada porządkująca cały projekt

**Rejestrujemy szeroko wobec jednego odniesienia odległego; montaże zwarte wyprowadzamy odejmowaniem, po fakcie.**

Dlaczego to jest ważne i dlaczego nie jest obejściem: gdyby każdą odległość odniesienia mierzyć w osobnej sesji, różnice między sesjami (impedancja kontaktu, zmęczenie, oświetlenie) byłyby **większe niż mierzony efekt**. Rejestracja wszystkich elektrod naraz wobec wspólnego odniesienia daje **wszystkie montaże z jednej sesji, na tych samych próbkach**. To jest metodycznie ta sama operacja, którą wykonałem na danych Kołodzieja (`14_REANALIZA.md` §5), i to jest powód, dla którego tamten wynik w ogóle dało się policzyć.

**Konsekwencja dla płytki:** liczba kanałów jest ważniejsza niż wyrafinowanie pojedynczego kanału. Stąd ADS1299 ośmiokanałowy, nie czterokanałowy.

### 2.2 Tor sygnałowy — trzy warstwy

| Warstwa | Co robi | Gdzie leży ryzyko |
|---|---|---|
| **elektrody** | kontakt ze skórą przez włosy, Ag/AgCl z żelem na etapie 1, suche na etapie 3 | niedopasowanie impedancji między elektrodami — **zmierzony przez innych spadek CMRR o 26,9 dB**, arXiv 2601.01772 |
| **front-end** | ADS1299: 8 wejść różnicowych, wzmacniacz PGA 1–24×, przetwornik 24 bit, wbudowany obwód pomiaru impedancji i sterowania prawą nogą (DRL) | zasilanie, masa analogowa, ekranowanie |
| **cyfrowa** | ESP32‑S3: odbiór SPI, znacznik czasu, transmisja; klasyfikacja FBCCA na urządzeniu albo na laptopie | jitter próbkowania |

**Wybór ADS1299 + ESP32‑S3 nie jest zgadywanką** — jest to architektura opublikowana i scharakteryzowana (arXiv 2601.01772: szum 0,08 µV RMS przy zwartym wejściu, jitter 0,56 µs, CMRR >112 dB). Mamy więc **liczby, do których własny tor ma się porównać**, i to jest połowa rubryki `Execution`.

### 2.3 Rozkład elektrod — osiem wejść, po co każde

Moduł na potylicy, plus zestaw punktów odniesienia o rosnącej odległości. Wszystkie mierzone **jednocześnie** wobec odniesienia najdalszego.

| Wejście | Położenie | Rola |
|---|---|---|
| 1 | Oz (guzowatość potyliczna, ~2 cm powyżej inionu) | aktywna, główna |
| 2 | O1 | aktywna |
| 3 | O2 | aktywna |
| 4 | ~2 cm poniżej Oz, w obrębie modułu | **kandydat na odniesienie zwarte** |
| 5 | ~4 cm poniżej Oz, poniżej inionu, nad mięśniem karku | kandydat na odniesienie, **wnosi EMG karku** |
| 6 | wyrostek sutkowaty (za uchem), cienkim przewodem | kandydat na odniesienie „krótki wyprowadzony" — **dopuszczony decyzją 6** |
| 7 | nad mięśniem karku, blisko wejścia 5 | **kanał mięśniowy** — kontrybucja druga, warunkowa. **Nie na szczęce** — patrz niżej |
| 8 | płatek ucha | **odniesienie literaturowe, górna granica** |
| DRL | kark, poza obszarem pomiarowym | sterowanie prawą nogą, tłumienie 50 Hz |

**Dlaczego kanał mięśniowy siedzi na karku, a nie na szczęce.** `[fakt, `14_REANALIZA.md` §6A]` Elektroda szczękowa została **usunięta z projektu po teście na żądanie użytkownika**: jej sufit to +0,6 pp nawet w oknach najbardziej skażonych artefaktem i przy regresorach nieliniowych, a wymagała elektrody na twarzy, czyli poza modułem. Kanał karkowy zostaje, bo jest **współlokowany z kandydatem na elektrodę odniesienia** (wejście 5) i tylko tam pozostaje pytanie, którego cudze dane nie rozstrzygają: co się dzieje, gdy odniesienie samo leży nad pracującym mięśniem.

`[wniosek]` Ten układ pozwala wyprowadzić offline **wszystkie** montaże z sekcji 5 pliku `14`, plus warianty, których w tamtym zbiorze nie było (odniesienie na sutkowatym i na karku). **Te dwa są całą stawką projektu i nie ma ich w żadnym publicznym zbiorze**, jaki znalazłem.

### 2.4 Stymulator

**Diody LED, nie ekran.** Powód `[fakt]`: ekran ma odświeżanie 60 albo 120 Hz i częstotliwości niebędące jego dzielnikami są odtwarzane z modulacją; Kołodziej użył panelu LED 6×6 cm, światło zielone, 7/8/9 Hz.

- panel LED sterowany osobnym mikrokontrolerem, wypełnienie i częstotliwość z licznika sprzętowego, nie z opóźnienia programowego
- **fotodioda wpięta w wejście pomocnicze rejestratora — WARUNEK KONIECZNY, nie udogodnienie.** Dwa zadania: udowodnić, że bodziec miał częstotliwość, którą deklarujemy, **oraz zapisać moment zapłonu, żeby okna dało się ciąć względem bodźca, a nie względem początku pliku**. `[fakt, `14_REANALIZA.md` §6B]` W zbiorze Kołodzieja tego nie ma i przez to **TRCA — metoda o najwyższym ITR w dziedzinie — jest tam niedostępna**, czego nie da się naprawić żadną analizą po fakcie. To najtańsza pozycja w całym zestawieniu i jedna z najważniejszych
- częstotliwości: **nie 7/8/9 Hz.** Pasmo 7–9 Hz leży w rytmie alfa, który sam w sobie ma tam maksimum nad potylicą — to zawyża poziom bazowy i mieszał się z artefaktami u Kołodzieja. Do własnych pomiarów **8–15 Hz z krokiem nierównomiernym** albo pasmo 12–20 Hz, żeby harmoniczne nie wpadały na siebie. Konkretny dobór — `16_PLAN_EKSPERYMENTALNY.md` §3.2

### 2.5 Bezpieczeństwo — warunek wstępny, nie pozycja na końcu

`[fakt, `HANDBOOK.md` §12]` Cokolwiek elektrycznego w kontakcie z głową: **zasilanie wyłącznie bateryjne, żadnego połączenia z siecią w czasie pomiaru.**

- zasilanie: ogniwo litowo‑polimerowe, przetwornica na ±2,5 V dla części analogowej
- transmisja: **bezprzewodowa (ESP32) w czasie pomiaru.** Kabel USB do laptopa zasilanego z sieci jest drogą powrotną prądu i jest zakazany w czasie noszenia
- programowanie i ładowanie: **wyłącznie przy zdjętym urządzeniu**, wpisane w procedurę
- `[fakt]` Reguły elektryczne ISEF dotyczą **stoiska**, próg 36 V na obwodach odsłoniętych (`ISEF_HUMAN_PARTICIPANTS.md`). Nasze napięcia są rzędu 5 V — próg nie jest problemem. Problemem byłoby zasilanie sieciowe, i dlatego go nie ma

---

## 3. Zestawienie materiałowe i koszt

**Ostrzeżenie o cenach `[luka]`:** ceny sklepowe są renderowane po stronie klienta i **przeglądarka w tym środowisku nie ma dostępu do sieci** (`PRZEKAZANIE.md` §6). Zweryfikowałem jedną pozycję u producenta; reszta to rzędy wielkości do potwierdzenia przy zakupie. **Nie planuj budżetu na tych liczbach bez sprawdzenia w sklepie.**

### 3.1 Etap A — platforma odniesienia, jesień 2026

| Pozycja | Ilość | Koszt orientacyjny | Skąd liczba |
|---|---|---|---|
| OpenBCI Cyton, 8 kanałów | 1 | **1 300–1 600 zł używany / 6 000–6 800 zł nowy** | **POPRAWKA 18 VIII 2026 — K-084.** `[fakt]` Cena katalogowa to **1 249 USD**, nie ~500 USD. Liczba w tej tabeli była zaniżona o połowę; poprawiono ją 16 VIII w `20_ZAKUPY.md` §1.1 (K-071), ale tutaj przetrwała. **Obowiązuje `20_ZAKUPY.md` §3.1: używany Cyton do 1 600 zł, termin 30 IX 2026** |
| elektrody kubkowe Ag/AgCl z żelem + pasta | komplet | ~150–300 zł | `[domysł]` |
| panel LED + sterownik + fotodioda | 1 | ~120–250 zł | `[domysł]` |
| **razem etap A** | | ~~**~2 800–4 000 zł**~~ **→ 1 750–2 450 zł** (używany Cyton) | **K-084.** Przeliczone 18 VIII 2026 wobec ceny rzeczywistej; wariant obowiązujący i pełne rozbicie: `20_ZAKUPY.md` §5 |

**Po co kupować, skoro celem jest własny sprzęt:** żeby **oddzielić błędy toru od błędów metody**. Bez działającego punktu odniesienia pierwsza nieudana rejestracja jest nierozstrzygalna — nie wiadomo, czy zawiódł wzmacniacz, elektrody, bodziec, czy klasyfikator. ~~Cyton daje też baseline komercyjny wymagany przez `13_PODNIESIENIE_SZANS.md` §6.~~ **Zdanie wycofane 16 VIII 2026 (K-071), adnotacja 18 VIII (K-084):** OpenBCI nie jest produktem konsumenckim, więc porównanie z nim nie jest porównaniem z rynkiem. Cyton pełni dwie role — test R1 i ubezpieczenie — i żadna nie jest rolą w twierdzeniu. Rozbiór: `20_ZAKUPY.md` §2.

### 3.2 Etap C — własny tor analogowy, wiosna 2027

| Pozycja | Ilość | Koszt orientacyjny | Skąd liczba |
|---|---|---|---|
| **ADS1299 (8 kan., obudowa TQFP‑64)** | 2 (jeden zapasowy) | **~45,9–69,8 USD/szt.** | `[fakt]` odczytane z cennika na stronie produktu ti.com, 16 VIII 2026; **wariant i próg ilościowy do potwierdzenia** |
| ESP32‑S3, moduł | 2 | ~60–100 zł | `[domysł]` |
| PCB 4‑warstwowa, ~5×5 cm, 5 szt. | 1 seria | ~150–300 zł | `[domysł]`, produkcja azjatycka z wysyłką |
| elementy bierne, precyzyjne, złącza, ekranowanie | komplet | ~200–400 zł | `[domysł]` |
| ogniwo LiPo + ładowarka + przetwornica ±2,5 V | komplet | ~120–200 zł | `[domysł]` |
| obudowa drukowana, żywica ISO 10993 (Liqcreate Bio‑Med Clear) | 0,5 kg | **~456 zł** | `[fakt]`, K-035 |
| elektrody suche, prototypy (druk + powłoka) | seria | ~200–500 zł | `[domysł]` |
| **razem etap C** | | **~1 600–2 800 zł** | |

### 3.3 Suma i rezerwa

| | Kwota |
|---|---|
| etap A | ~~2 800–4 000 zł~~ **1 750–2 450 zł** (K-084) |
| etap C | 1 600–2 800 zł |
| **rezerwa 30%** (druga seria PCB po błędzie — patrz §5.2) | 1 300–2 000 zł |
| **całość** | ~~**5 700–8 800 zł**~~ **4 500–7 300 zł** — suma obowiązująca z `20_ZAKUPY.md` §5, wobec budżetu **8 000 zł** (K-084, `35_AUDYT_2026_08_18.md` §3.1) |

**Odniesienie do tego, co użytkownik uznał za wyobrażalne:** 15 000 zł przy projekcie drona (`00_PYTANIA_I_LUKI.md` B1, wyraźnie **nie jako limit**). Projekt mieści się w połowie tamtej kwoty.

**Największa pojedyncza pozycja to platforma odniesienia, nie własny sprzęt.** Jeżeli budżet ma być cięty, to jest pierwsze miejsce do rozmowy — ale ciąć to znaczy przyjąć ryzyko z §5.2, i wtedy trzeba je zapisać.

---

## 4. Kolejność prac i kamienie milowe

Kalendarz z `DECYZJE.md` decyzja 4, przyjęty. **10 h/tydzień** (`00_PYTANIA_I_LUKI.md` B2).

### 4.1 Tor B rusza pierwszy, bo już ruszył

**Zmiana wobec `PRZEKAZANIE.md` §4.1, gdzie tory A i B miały iść równolegle.** Tor B (dekodowanie na danych publicznych) **jest już częściowo wykonany** — `14_REANALIZA.md` to działający pipeline FBCCA i SVM, zwalidowany wobec publikacji. To kilka tygodni pracy, których nie trzeba powtarzać.

| Okres | Co | Wynik do pokazania |
|---|---|---|
| **IX 2026** | dokończyć tor B: TRCA, okna 0,5–4 s, krzywa dokładność‑czas na danych Kołodzieja | wykres ITR(t) i wybór okna decyzyjnego |
| **IX–X 2026** | zakup platformy A; pierwsze własne zapisy z potylicy; **odtworzyć na sobie liczbę z literatury** | własny punkt wyjścia, zmierzony |
| **X–XII 2026** | nauka projektowania PCB; **równolegle** pomiar toru Cytona tą samą metodą co arXiv 2601.01772 (zwarte wejście, szum RMS) | tabela: nasz szum wobec 0,08 µV RMS |
| **XII 2026 – I 2027** | projekt płytki v1; zamówienie; montaż | płytka w ręku |
| **I–II 2027** | uruchomienie v1, pomiar szumu, CMRR, jitter | karta charakterystyki własnego toru |
| **28 II 2027** | **twardy termin: zgłoszenie Explory** | projekt nie musi być skończony (§4.1 regulaminu) |
| **III–IV 2027** | v2 po błędach v1; obudowa; elektrody suche | działający prototyp |
| **~IV 2027** | El-Robo-Mech / OITwEiM — dry-run prezentacji | wystąpienie |
| **V 2027** | **START formalnej kampanii pomiarowej pod ISEF** (K-023, K-046) | wszystko wcześniejsze = prace rozwojowe |
| **V–VI 2027** | półfinał Explory, online; **wideo jako produkt pierwszej klasy** (`13` §3) | wideo, plakat |
| **VI–IX 2027** | kampania: pełny plan z `16_PLAN_EKSPERYMENTALNY.md` | komplet danych |
| **X 2027** | finał krajowy, Gdynia | stoisko z działającym urządzeniem |
| **XI 2027 – IV 2028** | uzupełnienia, grupa badanych po zgodzie IRB, dokumentacja ISEF | Form 4 i pokrewne |
| **V 2028** | ISEF | |

### 4.2 Twardy warunek kolejnościowy

`[wniosek, `00_PYTANIA_I_LUKI.md` B2]` **Nauka projektowania PCB musi się skończyć przed startem budowy toru analogowego, nie równolegle z nim.** To jest jedyne miejsce w harmonogramie, gdzie równoległość kosztuje więcej, niż daje.

### 4.3 Trzy rzeczy poza komputerem — bez zmian, jesień 2026

Z `PRZEKAZANIE.md` §4.3 i `DECYZJE.md`, przenoszę bez zmian, bo żadnej nie da się załatwić po mojej stronie:

1. **mail do FZT** (`konkurs@fzt.org.pl`) — czy organizator prowadzi SRC pełniące funkcję IRB; **plus pytanie o łączenie startu w Explory i EUCYS**
2. **rozmowa z dyrekcją** — powołanie komisji IRB przy szkole
3. **pisemna zgoda opiekuna** na role Adult Sponsor i Direct Supervisor

**Doszła czwarta, nowa:** regulaminy **El-Robo-Mech XII** i **OITwEiM 2026/27** ukażą się jesienią 2026 — sprawdzić daty i kategorie.

---

## 5. Co konkretnie zostaje zbudowane — lista przedmiotów

Na koniec projektu istnieją cztery przedmioty. To jest odpowiedź na §11 handbooka „co konkretnie zostaje zbudowane".

1. **Moduł potyliczny** — płytka ~5×5 cm z ADS1299 i ESP32‑S3, w obudowie drukowanej z żywicy ISO 10993, na ogniwie LiPo, z ośmioma wejściami różnicowymi i wyprowadzeniem zestawu elektrod z §2.3
2. **Wymienne wiązki elektrodowe** — kilka rozstawów i kilka położeń odniesienia, wpinane w to samo złącze. **To jest fizyczne ucieleśnienie zmiennej niezależnej projektu**
3. **Stymulator LED** z fotodiodą kontrolną, sterowany licznikiem sprzętowym
4. **Oprogramowanie** — akwizycja, FBCCA/TRCA, wyznaczanie ITR, wyprowadzanie montaży pochodnych offline. Pipeline z `analiza/` jest jego zalążkiem i już działa

### 5.2 Ryzyko, które trzeba było wpisać do budżetu, a nie do listy ryzyk

`[wniosek]` **Pierwsza własna płytka analogowa dla sygnałów mikrowoltowych rzadko działa za pierwszym razem.** Rezerwa 30% w §3.3 jest na drugą serię PCB, a harmonogram w §4.1 przewiduje v2 w marcu–kwietniu 2027. **To nie jest pesymizm — to jest jedyny sposób, żeby v2 nie wypadła w maju 2027**, czyli w miesiącu startu formalnej kampanii ISEF.
