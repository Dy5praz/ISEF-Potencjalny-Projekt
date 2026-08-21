# 03 — Sprzęt: co się buduje, z czego, za ile

**Stan na 21 sierpnia 2026.** Zastępuje `archiwum/15_PROJEKT.md` i `archiwum/20_ZAKUPY.md`.

---

## 1. Zasada porządkująca cały projekt

**Rejestruje się szeroko wobec jednego odniesienia odległego; montaże zwarte wyprowadza się odejmowaniem, po fakcie.**

Dlaczego to nie jest obejście: gdyby każde położenie odniesienia mierzyć w osobnej sesji, różnice między sesjami (impedancja kontaktu, zmęczenie, oświetlenie) byłyby **większe niż mierzony efekt**. Rejestracja wszystkich elektrod naraz wobec wspólnego odniesienia daje **wszystkie montaże z jednej sesji, na tych samych próbkach**.

**Konsekwencja:** liczba kanałów jest ważniejsza niż wyrafinowanie pojedynczego kanału. Stąd ADS1299 ośmiokanałowy.

---

## 2. Rozkład elektrod — osiem na głowie plus fotodioda

| Elektroda | Położenie | Odległość od Oz | Rola | Pin ADS1299 |
|---|---|---|---|---|
| 1 | **Oz** — jeden krok 10% powyżej inionu | 0 | aktywna, główna | kanał 1 |
| 2 | **O1** | ~3,5 cm w bok | aktywna, na cienkim przewodzie | kanał 2 |
| 3 | **O2** | ~3,5 cm w bok | aktywna, na cienkim przewodzie | kanał 3 |
| **4** | **POz** — jeden krok 10% **POWYŻEJ** Oz | **~3,5 cm w górę** | **odniesienie zwarte, kierunek w górę.** Główny kandydat | kanał 4 |
| **5** | **Iz** — jeden krok 10% **PONIŻEJ** Oz, czyli na inionie | **~3,5 cm w dół** | **odniesienie zwarte, kierunek w dół** — warunek porównawczy | kanał 5 |
| 6 | wyrostek sutkowaty, cienkim przewodem | ~7 cm | odniesienie „krótkie wyprowadzone" | kanał 6 |
| 7 | nad mięśniem karku, poniżej inionu | ~4,5 cm w dół | **kanał kontrolny R12** — mierzy skażenie okolicy podpotylicznej (EMG karku, ECeG) | kanał 7 |
| 8 | płatek ucha | ~10 cm | **odniesienie literaturowe i odniesienie sprzętowe rejestracji** (§2.2) | **SRB1** |
| — | **fotodioda stymulatora** | — | znacznik zapłonu bodźca, próbkowany **tym samym zegarem** (§5) | **kanał 8** |
| DRL | kark, poza obszarem pomiarowym | — | sterowanie prawą nogą, tłumienie 50 Hz | **BIAS** |

**Razem: osiem elektrod na głowie plus DRL, czyli dziewięć punktów styku** — plus fotodioda, która nie dotyka głowy. Wszystkie **naraz, w każdej sesji pomiarowej.**

`[fakt]` **Rozliczenie pinów, bo bez niego liczby się nie zgadzają:** ADS1299 ma osiem wejść różnicowych, ale elektrod na głowie jest osiem. Nie ma sprzeczności — **płatek ucha nie zajmuje wejścia, tylko pin SRB1** (odniesienie sprzętowe wspólne dla wszystkich kanałów). Zostaje siedem wejść na elektrody i **ósme wolne, przydzielone fotodiodzie.** Poprawka K-106; wcześniej fotodioda była opisana jako podłączona do „wejścia pomocniczego rejestratora", którego **własna płytka nie ma** — to była pozostałość po Cytonie.

### 2.1 Geometria: skąd biorą się te odległości

`[fakt]` W układzie 10–20 południk środkowy odmierza się w procentach **łuku nasion–inion**: Oz leży **10% powyżej inionu**, POz (10–10) **20% powyżej inionu**, Iz **na inionie**. `[wniosek]` **Krok Oz→POz i krok Oz→Iz są więc z definicji równe** — po jednym odcinku 10%.

`[luka]` **Ile to jest w centymetrach, zależy od głowy autora i nie było dotąd zmierzone.** Dla łuku 34–38 cm krok wynosi **3,4–3,8 cm**, stąd „~3,5 cm" w tabeli. **P35: zmierzyć własny łuk nasion–inion taśmą krawiecką i wpisać własną liczbę** — pięć minut, zero złotych, a wszystkie odległości w projekcie przestają być średnią z literatury.

**Poprzednia wersja tabeli podawała „Oz ~2 cm powyżej inionu" i elektrodę 5 „~2 cm poniżej Oz".** Obie liczby były błędne i, co gorsza, **niezgodne ze sobą**: ten sam krok 10% raz miał 2 cm (inion→Oz), raz 3,5 cm (Oz→POz). Skutek był poważniejszy niż sama pomyłka — patrz K-106.

### 2.2 Dlaczego wszystkie osiem muszą być na głowie jednocześnie

`[fakt]` **ADS1299 mierzy każde wejście wobec jednego wspólnego odniesienia sprzętowego (pin SRB1).** `[wniosek]` W tym projekcie tę rolę pełni **elektroda 8 (płatek ucha)** — najdalsza, więc najmniej podatna na przypadkowe zbieżności z sygnałem potylicznym.

Skutek jest taki, że **każdy montaż wyprowadza się z tej samej rejestracji przez odejmowanie, offline**:

| Warunek | Jak powstaje z zarejestrowanych kanałów |
|---|---|
| Oz wobec płatka ucha (~10 cm) | kanał 1, wprost |
| Oz wobec wyrostka sutkowatego (~7 cm) | kanał 1 − kanał 6 |
| **Oz wobec POz (~3,5 cm, w górę)** | **kanał 1 − kanał 4** |
| **Oz wobec Iz (~3,5 cm, w dół)** | **kanał 1 − kanał 5** |
| montaż trójkanałowy z odniesieniem odległym | kanały 1, 2, 3 wprost |

`[wniosek]` **To jest cały trik metodyczny tego projektu i bez ośmiu elektrod nie działa.** Gdyby elektrodę odniesienia trzeba było **przekładać** między warunkami, każdy warunek byłby z innej chwili — a wtedy różnica wyniku niosłaby, oprócz geometrii, także zmęczenie, wyschnięcie żelu, inną dyspozycję i inny poziom alfa. **Osiem elektrod naraz zamienia porównanie międzysesyjne w porównanie na tych samych próbkach**, co jest jedyną postacią, w której efekt rzędu kilku punktów procentowych da się w ogóle zobaczyć.

**Para elektrod 4 i 5 to warunek kontrolny w najczystszej postaci, jaką ten projekt ma:** **odległość równa co do konstrukcji** (dwa razy ten sam krok 10%), **przeciwny kierunek**, ta sama sesja, te same próbki, ten sam tor. Różnica jest **czystym efektem kierunku**.

`[fakt]` **To zdanie było wcześniej nieprawdziwe i K-106 je naprawia.** Przy POz 3,5 cm w górę i elektrodzie 2 cm w dół odległości różniły się o **75%** — czyli o zmienną, którą ten projekt mierzy. Kontrast „w górę wobec w dół" **niósł wtedy efekt kierunku zmieszany z efektem odległości i nie dało się ich rozdzielić.** Przeniesienie elektrody 5 na **Iz** usuwa to zmieszanie **konstrukcyjnie, a nie statystycznie**: obie pozycje są nazwanymi punktami 10–10, oddalonymi o ten sam ułamek tego samego łuku. **P36 — zatwierdzone przez autora 21 VIII 2026.**

`[wniosek]` **Dlaczego kandydat główny poszedł w górę, a nie w dół** (zmiana z 21 VIII 2026): okolica podpotyliczna ma trzech mieszkańców — mięsień karku, móżdżek reagujący na bodziec wzrokowy w paśmie beta, i gładkie pole (`05_STAN_WIEDZY.md` §6). **POz leży powyżej inionu, poza zasięgiem dwóch pierwszych.** Do tego para POz−Oz jest jedyną, dla której istnieje opublikowany wynik: **~46 bit/min przy 40 celach**.

**Rozstrzygnięcie z 21 VIII 2026 (P28a, zamknięte).** Autor dopuścił **dwa cienkie przewody w bok, do O1 i O2** — takie same jak przewód na wyrostek sutkowaty. `[wniosek]` Skutek: obudowa nie musi rozciągać się na boki, żeby objąć O1 i O2, więc **jedynym wymiarem, jaki musi zmieścić, jest pionowa para Oz–POz (~3,5 cm)** — a ta i tak siedzi na jej własnym spodzie (§4). **Gabaryt ~32×48×12 mm zostaje w mocy i nie ma już pozycji, która by go rozciągała.** Przewody boczne są jednocześnie warunkiem koniecznym wariantu C na płytce elastycznej.

### 2.3 Z jaką dokładnością trzeba te położenia odmierzyć

`[luka]` **Dokumentacja nigdy tego nie podawała** — a zmienną niezależną tego projektu jest **odległość**, więc dokładność jej odmierzenia jest dokładnością zmiennej niezależnej. Bez tej liczby wynik „−7 pp na 3,5 cm" nie ma zdefiniowanego słupka błędu w osi poziomej.

`[fakt]` **Fabregat-Sanjuan i in. 2023**, Brain Behav 13(10):e3187, **PMID 37534627**, dziesięciu operatorów, pomiar skanerem strukturalnym: błąd znakowania elektrod wynosi **1,7 mm przy odmierzaniu taśmą wzdłuż linii nasion–inion** i **12,5 mm metodą przybliżoną**.

`[wniosek]` Przy kroku 3,5 cm to jest odpowiednio **5% i 36% mierzonej odległości.** Metoda przybliżona **zjada ponad jedną trzecią zmiennej niezależnej** i jest w tym projekcie zakazana. Obowiązuje:

- każda sesja zaczyna się od **odmierzenia łuku nasion–inion taśmą** i wyznaczenia punktów procentowo, nie „mniej więcej tam, gdzie ostatnio"
- położenia **fotografowane** na początku sesji, z linijką w kadrze — materiał dowodowy do arkusza ISEF i jedyny sposób wykrycia dryfu montażu między dniami
- w wyniku podaje się **odległość ± 2 mm**, nie „3,5 cm"

**Czego w tym rozkładzie NIE ma:** elektrody szczękowej. Usunięta po pomiarze — jej sufit to **+0,6 pp** nawet w oknach najbardziej skażonych artefaktem, przy p = 0,166. Wymagała elektrody na twarzy, czyli poza modułem. **Sprzęt się przez to upraszcza.**

---

## 3. Tor sygnałowy

| Warstwa | Co robi | Gdzie leży ryzyko |
|---|---|---|
| **elektrody** | kontakt przez włosy; Ag/AgCl z żelem na etapie 1, suche na etapie 3 | **niedopasowanie impedancji** — zmierzony przez innych spadek CMRR o **26,9 dB** |
| **front-end: ADS1299** | 8 wejść różnicowych, PGA 1–24×, przetwornik 24 bit, wbudowany pomiar impedancji i obwód DRL | zasilanie, masa analogowa, ekranowanie |
| **cyfrowa: ESP32-S3** | odbiór SPI, znacznik czasu, transmisja; klasyfikacja FBCCA/TRCA na urządzeniu albo na laptopie | jitter próbkowania |

`[fakt]` **Wybór nie jest zgadywanką** — to architektura opublikowana i scharakteryzowana (arXiv 2601.01772). Jej liczby są poprzeczką dla własnego toru: **0,08 µV RMS**, jitter **0,56 µs**, dryf **< 1 ppm**, CMRR **> 112 dB**.

---

## 4. Forma urządzenia

`[wniosek]` **Rozpiętość elektrod to nie obrys bryły** — i to jest rozróżnienie, o które trzeba pilnować w każdym opisie.

| Element | Wymiar |
|---|---|
| ADS1299, obudowa TQFP-64 | 10 × 10 mm |
| moduł ESP32-S3-MINI | ~15 × 21 mm |
| ogniwo LiPo 402030 | ~30 × 20 × 4 mm |
| **płytka czterowarstwowa** | **~30 × 45 mm** |
| **całość z obudową** | **~32 × 48 × 12 mm — mniej niż pudełko zapałek** |

**Rzecz, która rozwiązuje sprawę gabarytu:** obudowa ma ~48 mm wysokości, a **odległość Oz–POz wynosi ~35 mm**. Obudowa ustawiona pionowo **mieści obie elektrody krytycznej pary na własnym spodzie** — para, na której stoi twierdzenie, **nie wymaga ani jednego przewodu**.

### 4.1 Dwie konfiguracje, których nie wolno mylić

`[fakt]` **Poprawka z 21 VIII 2026, K-105.** Do tego miejsca dokumentacja opisywała tylko jedną konfigurację i wychodziło z niej, że urządzenie ma cztery elektrody. **Ma ich osiem, ale nie zawsze.**

| | **Konfiguracja pomiarowa** — cała kampania E1–E4 | **Konfiguracja demonstracyjna** — stoisko, film, pokaz |
|---|---|---|
| **elektrody** | **8 + DRL = 9 punktów styku** | **4 + DRL = 5 punktów styku** |
| na spodzie obudowy | Oz, POz | Oz, POz, `[domysł]` DRL |
| na cienkich przewodach | O1, O2, Iz, wyrostek sutkowaty, kanał karkowy, płatek ucha, DRL — **7 wyprowadzeń** | O1, O2 — **2 wyprowadzenia** |
| po co ta nadmiarowość | **cztery położenia odniesienia naraz na tych samych próbkach** (§2.2) — bez tego nie ma pomiaru | żadnej: warunek zwycięski jest już wybrany, reszta elektrod nie ma czego mierzyć |
| jak wygląda | **jak aparatura**, i tak ma wyglądać | **jak pudełko zapałek z dwoma wąsami** |

`[wniosek]` **To rozróżnienie jest zaletą, nie usprawiedliwieniem.** Zdanie dla jurora: *„W pomiarze noszę osiem elektrod, bo porównuję cztery położenia odniesienia w jednej sesji, na tych samych próbkach. W urządzeniu zostają cztery, bo pomiar rozstrzygnął, które są potrzebne."* **Redukcja z ośmiu do czterech jest wynikiem tego projektu**, a nie kompromisem, na który trzeba się tłumaczyć.

`[luka]` Czy DRL zmieści się na spodzie obudowy razem z Oz i POz, czy musi zostać na przewodzie do karku — **do rozstrzygnięcia przy projekcie płytki** (P34). Nie wpływa na twierdzenie; wpływa na to, czy pokaz ma dwa wąsy, czy trzy.

### 4.2 Trzy architektury

| | Co to jest | Werdykt |
|---|---|---|
| A | jedna sztywna płyta 4×8 cm z elektrodami od spodu | **odrzucone** — wygląda jak karta przyklejona do głowy |
| **B** | **obudowa elektroniki + elektrody na przewodach** | **wariant v1** |
| C | sztywna wyspa na podłożu giętkim (flex-PCB), elektrody na cienkich ramionach | **cel v2, opcjonalny.** Wzorzec sprawdzony: cEEGrid, a HardwareX 2022 (PMID 36204424) opublikował gotowy projekt takiej przejściówki **dla OpenBCI** |

**Pomiar nie wymaga postaci docelowej.** Twierdzenie dotyczy geometrii elektrod, nie obudowy. Wariant B wystarcza do całej kampanii.

### 4.3 Co ten montaż mierzy w jednej sesji, a czego nie

`[wniosek]` **Rozliczenie, którego dotąd nie było, i które ujawnia nierówność między dwoma kierunkami.**

| Kierunek | Odległości dostępne **wewnątrz jednej sesji** | Co z tego wychodzi |
|---|---|---|
| **w dół / w bok** | **3,5 cm** (Iz) · **4,5 cm** (kark) · **7 cm** (wyrostek) · **10 cm** (płatek ucha) | **cztery punkty — krzywa, z której da się odczytać próg** |
| **w górę** | **3,5 cm** (POz) | **jeden punkt — progu odczytać się nie da** |

`[fakt]` To jest istotne, bo **kandydatem głównym jest kierunek w górę** (§2). Zdanie z twierdzenia — *„wyznaczam najmniejszą odległość, przy której przepustowość jeszcze się nie załamuje"* — jest **w tej chwili wykonalne w dół, a w górę nie.**

**Rozwiązanie jest już w projekcie i nie kosztuje ani złotówki: wymienne wiązki elektrodowe** (§8 poz. 2). Plan przewiduje **osiem sesji w ośmiu różnych dniach** (`04_PLAN_POMIAROWY.md`), więc wiązki rotuje się między sesjami:

- **wiązka A (podstawowa, w połowie sesji):** rozkład z §2 — cały kontrast kierunku i cała krzywa w dół, wewnątrz sesji
- **wiązka B:** elektroda 5 przeniesiona z Iz na **punkt pośredni ~1,75 cm powyżej Oz** — najkrótsza odległość w całym planie, ta, która odpowiada wprost na pytanie o moduł
- **wiązka C:** elektroda 5 przeniesiona na **Pz, ~7 cm powyżej Oz** — trzeci punkt osi pionowej

`[wniosek]` **Napięcie, które trzeba nazwać, bo inaczej wygląda na sprzeczność z §1.** §1 mówi „nie przekładać elektrod między warunkami", a to jest przekładanie. Różnica: **kontrasty krytyczne — kierunek i całą krzywą w dół — mierzy się wewnątrz sesji, na tych samych próbkach.** Wiązki B i C dokładają **punkty uzupełniające między sesjami**, a porównywalność zapewniają **kotwice: Oz, POz i płatek ucha są w każdej wiązce**, więc każdą sesję normalizuje się do jej własnego warunku POz. **Wynik z kotwicy jest wewnątrzsesyjny; wynik z punktu uzupełniającego jest międzysesyjny i raportuje się go z osobnym, szerszym przedziałem.** Mieszanie tych dwóch w jednej tabeli bez oznaczenia byłoby błędem.

---

## 5. Stymulator

**Diody LED, nie ekran.** `[fakt]` Ekran ma odświeżanie 60 albo 120 Hz i częstotliwości niebędące jego dzielnikami są odtwarzane z modulacją.

- panel LED sterowany osobnym mikrokontrolerem, częstotliwość z **licznika sprzętowego**, nie z opóźnienia programowego
- **fotodioda — WARUNEK KONIECZNY, nie udogodnienie.** Dwa zadania: dowieść, że bodziec miał deklarowaną częstotliwość, **oraz zapisać moment zapłonu, żeby okna ciąć względem bodźca, a nie względem początku pliku**
- `[wniosek]` **Wchodzi na kanał 8 ADS1299**, przez dzielnik, ze wzmocnieniem 1 (ADS1299 ustawia wzmocnienie osobno dla każdego kanału, pozostałe pracują na 24). Powód: kanał 8 jest **próbkowany tym samym zegarem co elektrody**, więc znacznik zapłonu i sygnał EEG leżą w **tej samej próbce** — bez tego trzeba zestawiać dwa strumienie i cała precyzja idzie w jitter. Na Cytonie w etapie 1 rolę tę pełni wejście AUX. **Na własnej płytce wejścia AUX nie ma i nigdy nie było w spisie — K-106**

`[fakt]` Dlaczego to jest warunek konieczny: w zbiorze Kołodzieja tego nie ma i przez to **TRCA — metoda o najwyższym ITR w dziedzinie — jest tam niedostępna**, czego nie da się naprawić żadną analizą po fakcie. Sprawdzone: faza SSVEP nie jest zsynchronizowana z oknami (R ≈ 0), TRCA daje 32–34% przy poziomie losowym 33,3%. **To najtańsza pozycja w całym zestawieniu i jedna z najważniejszych.**

**Częstotliwości: 8,0 / 9,4 / 10,8 / 12,2 / 13,6 / 15,0 / 16,4 / 17,8 Hz**, krok 1,4 Hz.

`[fakt]` **Dobór policzony, nie założony.** Kryterium: żadna z pierwszych trzech harmonicznych jednego celu nie pada bliżej niż 0,3 Hz od harmonicznej innego. Ten zestaw ma **zero kolizji** — przeliczone ponownie 21 VIII 2026, trzy harmoniczne × osiem celów, najmniejszy odstęp **0,4 Hz** (2×8,0 = 16,0 wobec celu 16,4). Zestaw całkowity 8–15 Hz z krokiem 1 Hz ma **dwie pary kolizyjne**: 3×8 = 2×12 = 24 Hz oraz 3×10 = 2×15 = 30 Hz. (Wcześniej stało tu „cztery" — ta sama rzecz policzona kierunkowo, czyli każda para dwa razy. K-106.) **Nie 7/8/9 Hz** — to pasmo rytmu alfa.

`[wniosek]` Dobór okazał się trafiony także z drugiego powodu: drugie harmoniczne wypadają w **16,0–35,6 Hz**, czyli w paśmie, w którym ECeG reaguje na bodziec wzrokowy — **co umożliwia test rozdzielający mechanizmy** (`04_PLAN_POMIAROWY.md`).

---

## 6. Bezpieczeństwo — warunek wstępny, nie pozycja na końcu

**Cokolwiek elektrycznego w kontakcie z głową: zasilanie wyłącznie bateryjne, żadnego połączenia z siecią w czasie pomiaru.**

- ogniwo litowo-polimerowe, przetwornica na ±2,5 V dla części analogowej
- **transmisja bezprzewodowa w czasie pomiaru.** Kabel USB do laptopa zasilanego z sieci jest drogą powrotną prądu i jest **zakazany w czasie noszenia**
- programowanie i ładowanie **wyłącznie przy zdjętym urządzeniu**, wpisane w procedurę

### 6.1 Padaczka fotogenna — luka znaleziona 21 VIII 2026, K-116

> **Do 21 VIII 2026 w całej dokumentacji nie było ani jednego wystąpienia słowa „padaczka".** Sekcja bezpieczeństwa opisywała wyłącznie bezpieczeństwo elektryczne — **w projekcie, którego istotą jest świecenie migającym światłem w oczy człowieka.**

`[fakt, cztery źródła: Epilepsy Foundation working group PMID 16146439, przegląd Seizure 2017, International Guidelines for Photosensitive Epilepsy, przeglądy bezpieczeństwa SSVEP-BCI]`

| | |
|---|---|
| częstość padaczki fotogennej | **~1 na 4 000** w populacji ogólnej; **3–5%** wśród osób z padaczką |
| **pasmo najbardziej prowokacyjne** | **15–25 Hz, szczyt ~18 Hz** |
| zakres w ogóle prowokacyjny | 3–60 Hz |
| czynniki nasilające | jasność > 20 cd/m², duże pole widzenia, **wysoki kontrast**, kombinacja **czerwony/niebieski** |

> `[fakt]` **Zestaw bodźców tego projektu to 8,0–17,8 Hz. Jego górny koniec leży dokładnie na szczycie pasma prowokacyjnego.**

**Standardowe środki ostrożności w interfejsach SSVEP** `[fakt]`: przesiew użytkowników · unikanie 15–25 Hz · **mały bodziec zamiast dużego pola** · **obniżony kontrast** · **automatyczne wygaszanie, gdy użytkownik odwraca wzrok**.

**Cztery skutki dla tego projektu, wszystkie wiążące:**

1. **Autor jest badanym w większości sesji.** Wywiad przed E0: napady w przeszłości, padaczka w rodzinie, **migrena z aurą**, złe reakcje na stroboskopy i gry. **Przy którymkolwiek na „tak" — rozmowa z lekarzem przed pierwszym pomiarem.**
2. **Pokaz na stoisku jest scenariuszem najgorszym**: nieznana osoba, nieznana historia medyczna, migotanie w paśmie prowokacyjnym. `[wniosek]` **Wariant „dla chętnych" wymaga pytania przesiewowego i ostrzeżenia przed włączeniem bodźca — niezależnie od procedury Human Participants**, która i tak go obejmuje (R13, `06_RYZYKA.md`).
3. **Formalnie:** to jest treść do **Risk Assessment Form (3)** i do wniosku IRB. `[wniosek]` **Komisja o to zapyta, a brak odpowiedzi jest gorszy niż odpowiedź „ryzyko istnieje i tak je ograniczam".**
4. **Napięcie projektowe, do rozstrzygnięcia, nie do zamiecenia** `[luka]`: zestaw 8,0–17,8 Hz **został dobrany pod pomiar**, żeby drugie harmoniczne wypadły w paśmie 16–35,6 Hz i umożliwiły test rozdzielający R12. **Przesunięcie zestawu w górę, poza 15–25 Hz, ten test psuje; przesunięcie w dół wpycha harmoniczne w pasmo alfa.** **Decyzja razem z wnioskiem do IRB, jesień 2026** — z opcją przycięcia samej góry zakresu.

**Środki, które nic nie kosztują i wchodzą od razu:** bodziec **mały, nie na pełnym ekranie** · **kontrast obniżony do minimum wystarczającego** · **bez kombinacji czerwony/niebieski** · **przerwy między blokami** · **wygaszanie bodźca przy odwróceniu wzroku**.

---

`[fakt]` Reguły elektryczne ISEF dotyczą **stoiska**: próg 36 V na obwodach odsłoniętych, obudowa niepalna, widoczny wyłącznik, zakaz ogniw otwartych i pakietów powyżej 100 Wh. **Projekt spełnia to bez wysiłku** — pracuje na jednostkach woltów.

---

## 7. Zakupy i budżet

### 7.1 Platforma odniesienia — jedyna pozycja z terminem

`[fakt, katalog producenta]` Cyton 8 kanałów **1 249 USD**, Ganglion 4 kanały **624,99 USD**, sam klucz USB 249 USD.

**Decyzja obowiązująca: kupić UŻYWANEGO Cytona, budżet do 1 600 zł, poszukiwania do 30 IX 2026. Jeżeli do tego terminu nie ma dobrej oferty — nowy Ganglion (~3 000–3 400 zł), nie nowy Cyton.**

**Warunki oferty używanej:** płytka **z kluczem USB** · czytelne oznaczenia **ADS1299** i **PIC32** na zdjęciu · sprzedawca dopuszcza zwrot · zasilanie bateryjne · **test odbiorczy w dniu dostawy**: zewrzeć wejścia, zmierzyć szum RMS w OpenBCI GUI, kwadrans.

**Bez AliExpress.** Przyrząd odniesienia jest jedynym miejscem, gdzie nie wolno mieć wątpliwości co do autentyczności układu scalonego.

#### 7.1a Cerelog ESP-EEG — trzeci kandydat, dopisany 21 VIII 2026

**Stan rynku sprawdzony 21 VIII 2026** `[fakt]`: **OLX Polska — zero ofert OpenBCI. eBay, filtr „używane" — zero płytek Cyton.** Jedyne pozycje używane to czepek elektrodowy (350 USD) i zestaw za 940 USD od sprzedawcy z **0% pozytywnych ocen**, niespełniający warunków odbioru z §7.1.

`[fakt, cztery źródła: strona producenta, CNX Software XII 2025, Hackster.io, Autodidacts.io]`

| | |
|---|---|
| cena | **349,99 USD** (~1 400 zł), przecena z 649,99 |
| kanały | **8 różnicowych** + bias |
| przetwornik | **ADS1299**, 24 bity, 250 SPS — **ten sam układ co Cyton** |
| zgodność | **BrainFlow, LSL, fork OpenBCI GUI** — pipeline z `analiza/` działa |
| schematy i firmware | **otwarte, `github.com/Cerelog-ESP-EEG/ESP-EEG`** |
| autor | Simon Hakimian, były inżynier sprzętowy SpaceX |
| **DRL** | **prawdziwa pętla zamknięta aktywnego biasu** |

**Co to rozwiązuje — trzy rzeczy, wszystkie realne:**

1. **Osiem kanałów za cenę linii budżetowej.** `[wniosek]` **Znika cały problem Ganglionu z K-106** — nie trzeba schodzić na węższe twierdzenie, zostają O1 i O2, zostaje górna baza porównania i kanał kontrolny R12.
2. **To jest ten sam układ, wokół którego projektujesz własną płytkę.** ADS1299 + ESP32, ze **schematem do czytania**. `[wniosek]` **P37 (nauka PCB, 35–60 h, „najgorzej oszacowana pozycja w planie, bo autor nie ma jej z czym porównać") dostaje punkt odniesienia.** Do tego ich DRL w pętli zamkniętej jest gotową odpowiedzią na **P34**.
3. **To nie jest anonimowy klon.** Nazwany autor, otwarte repozytorium, trzy niezależne omówienia w prasie technicznej. **Inna klasa ryzyka niż AliExpress** — czego zakaz z §7.1 dotyczył.

**Czego NIE rozwiązuje i co jest warunkiem zakupu:**

1. `[fakt, Autodidacts]` **Brak izolacji galwanicznej na USB.** Cytat: *„absolutely don't ever use it with a desktop computer or a laptop that is charging"*. **Skutek wiążący: pomiar wyłącznie na laptopie odłączonym od sieci, na baterii.** Wchodzi do §6 jako warunek bezpieczeństwa i **musi być opisane w formularzach Human Participants** — `09_FORMALNOSCI.md`.
2. `[fakt, Autodidacts]` **Firmware Bluetooth/WiFi niegotowy — na dziś tylko USB.** Cyton jest bezprzewodowy. Dla sesji na siedząco bez znaczenia, ale **degraduje E5** (metryki użytkowe, czas montażu) i pokaz „noszalności".
3. `[luka]` **Producent nie podaje szumu wejściowego.** Rozwiązanie jest w §7.2 i nic nie kosztuje: **szum toru mierzy się samym torem** — zewrzeć wejście, RMS z próbek. **Test odbiorczy w dniu dostawy zamyka tę lukę w kwadrans.**
4. `[wniosek]` **Brak rynku wtórnego.** Używany Cyton da się odsprzedać, tego prawdopodobnie nie. **To realnie podnosi koszt „opcji wrzesień–październik"** z §6 werdyktu, bo platforma przestaje być w pełni zbywalna.
5. `[domysł]` Mały producent, „batch #4" — ryzyko dostawy i gwarancji, wysyłka z USA z cłem po stronie odbiorcy.

**Werdykt:** `[wniosek]` **Kandydat mocniejszy niż nowy Ganglion i mocniejszy niż używany Cyton z niepewnego źródła — pod warunkiem zapisania punktu 1 do procedury bezpieczeństwa i wykonania punktu 3 w dniu dostawy.** Decyzja razem z P5, do 30 IX 2026.

**Do czego naprawdę służy:** (1) test, czy SSVEP działa u autora, **zanim istnieje własna płytka** — krytyczne, X 2026; (2) ubezpieczenie, gdyby własny tor nie zadziałał. **Nie jest punktem odniesienia twierdzenia.**

`[fakt]` **Ubezpieczenie jest pełne tylko w wersji ośmiokanałowej, i to trzeba powiedzieć wprost — K-106.** Ganglion ma **cztery kanały**, a montaż z §2 potrzebuje siedmiu naraz. Na Ganglionie zmieści się **Oz, POz, Iz i wyrostek sutkowaty wobec płatka ucha** — czyli **cały kontrast kierunku zostaje**, ale wypadają O1 i O2, a z nimi **górna z dwóch baz porównania** wymaganych przez `04_PLAN_POMIAROWY.md` (montaż wielokanałowy z odniesieniem odległym), oraz **kanał kontrolny R12**. `[wniosek]` **Ścieżka Ganglionowa nie jest równoważnym planem B, tylko planem B z węższym twierdzeniem** — mierzy kierunek i odległość, nie mierzy kosztu wobec montażu wielokanałowego. **To jest dodatkowy argument za znalezieniem używanego Cytona do 30 IX, mocniejszy niż różnica ceny.**

### 7.2 Sprzęt pomiarowy — mniej, niż się wydaje

`[fakt]` **Szum wejściowy toru mierzy się samym torem** — zwiera się wejście i liczy RMS z próbek własnego przetwornika 24-bitowego. Oscyloskop hobbystyczny ma szum własny **tysiąc razy większy** od mierzonej wielkości i do tego zadania się nie nadaje. **Przyrząd zewnętrzny jest potrzebny jako ŹRÓDŁO znanego sygnału, nie jako miernik.**

| # | Pozycja | Koszt | Konieczność |
|---|---|---|---|
| 1 | **dzielnik precyzyjny do zlutowania** (rezystory 0,1%) | **30–80 zł** | **niezbędny** — najtańsza pozycja i jedyna, gdzie dokładność jest krytyczna |
| 2 | **generator funkcyjny DDS** | 250–600 zł | **niezbędny** — CMRR, pasmo, kalibracja |
| 3 | oscyloskop | 1 200–2 500 zł | **przydatny, nie niezbędny** — pierwszy kandydat do pożyczenia |

`[luka]` Bez pożyczonego sprzętu nie da się zmierzyć **jitteru** ani potwierdzić **CMRR powyżej ~100 dB**. Do tego czasu obie liczby podawane jako katalogowe, **z jawnym zaznaczeniem**.

### 7.3 Budżet

| Pozycja | Kwota |
|---|---|
| platforma odniesienia (używany Cyton) | 1 300–1 600 zł |
| elektrody, pasta, stymulator LED, fotodioda | 300–550 zł |
| dzielnik + generator | 280–680 zł |
| własny tor (ADS1299, PCB, obudowa, elektrody) | 1 600–2 800 zł |
| **rezerwa 30% sumy pozostałych pozycji, przeznaczona na drugą serię płytek** | 1 000–1 700 zł |
| **razem** | **4 500–7 300 zł** |
| **budżet** | **8 000 zł** |
| **margines** | **700–3 500 zł** |

**Budżet się spina i zapas jest** — pod warunkiem znalezienia używanego egzemplarza do 30 IX. Przy nowym Ganglionie suma idzie do 6 000–9 000 zł i zapasu nie ma.

---

## 8. Co zostaje zbudowane — cztery przedmioty

1. **Moduł potyliczny** — płytka ~30×45 mm z ADS1299 i ESP32-S3, w obudowie z żywicy ISO 10993, na ogniwie LiPo, z ośmioma wejściami różnicowymi
2. **Wymienne wiązki elektrodowe** — kilka rozstawów i położeń odniesienia w to samo złącze. **To jest fizyczne ucieleśnienie zmiennej niezależnej**
3. **Stymulator LED** z fotodiodą kontrolną, sterowany licznikiem sprzętowym
4. **Oprogramowanie** — akwizycja, FBCCA/TRCA, ITR, wyprowadzanie montaży offline. Pipeline w `analiza/` już działa

`[wniosek]` **Pierwsza własna płytka analogowa dla sygnałów mikrowoltowych rzadko działa za pierwszym razem.** Rezerwa 30% jest na drugą serię, a harmonogram przewiduje v2 na marzec–kwiecień 2027. **To nie jest pesymizm — to jedyny sposób, żeby v2 nie wypadła w maju 2027**, czyli w miesiącu startu kampanii pod ISEF.
