# 03 — Sprzęt: co się buduje, z czego, za ile

**Stan na 21 sierpnia 2026.** Zastępuje `archiwum/15_PROJEKT.md` i `archiwum/20_ZAKUPY.md`.

---

## 1. Zasada porządkująca cały projekt

**Rejestruje się szeroko wobec jednego odniesienia odległego; montaże zwarte wyprowadza się odejmowaniem, po fakcie.**

Dlaczego to nie jest obejście: gdyby każde położenie odniesienia mierzyć w osobnej sesji, różnice między sesjami (impedancja kontaktu, zmęczenie, oświetlenie) byłyby **większe niż mierzony efekt**. Rejestracja wszystkich elektrod naraz wobec wspólnego odniesienia daje **wszystkie montaże z jednej sesji, na tych samych próbkach**.

**Konsekwencja:** liczba kanałów jest ważniejsza niż wyrafinowanie pojedynczego kanału. Stąd ADS1299 ośmiokanałowy.

---

## 2. Rozkład elektrod — osiem wejść

| Wejście | Położenie | Rola |
|---|---|---|
| 1 | **Oz** (~2 cm powyżej inionu) | aktywna, główna |
| 2 | **O1** | aktywna |
| 3 | **O2** | aktywna |
| **4** | **POz — ~3,5 cm POWYŻEJ Oz, na południku środkowym** | **odniesienie zwarte, kierunek w górę.** Główny kandydat |
| **5** | **~2 cm poniżej Oz, w obrębie modułu** | **odniesienie zwarte, kierunek w dół** — warunek porównawczy dla kierunku |
| 6 | wyrostek sutkowaty, cienkim przewodem | odniesienie „krótkie wyprowadzone", ~7 cm |
| 7 | nad mięśniem karku, **poniżej inionu** | **kanał kontrolny R12** — mierzy, czym skażona jest okolica podpotyliczna (EMG karku, ECeG) |
| 8 | płatek ucha | **odniesienie literaturowe**, ~10 cm, górna granica |
| DRL | kark, poza obszarem pomiarowym | sterowanie prawą nogą, tłumienie 50 Hz |

**Para wejść 4 i 5 to warunek kontrolny w najczystszej postaci, jaką ten projekt ma:** zbliżona odległość, **przeciwny kierunek**, ta sama sesja, te same próbki, ten sam tor. Różnica jest **czystym efektem kierunku**.

`[wniosek]` **Dlaczego kandydat główny poszedł w górę, a nie w dół** (zmiana z 21 VIII 2026): okolica podpotyliczna ma trzech mieszkańców — mięsień karku, móżdżek reagujący na bodziec wzrokowy w paśmie beta, i gładkie pole (`05_STAN_WIEDZY.md` §6). **POz leży powyżej inionu, poza zasięgiem dwóch pierwszych.** Do tego para POz−Oz jest jedyną, dla której istnieje opublikowany wynik: **~46 bit/min przy 40 celach**.

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

**Rzecz, która rozwiązuje sprawę gabarytu:** obudowa ma ~48 mm wysokości, a **odległość Oz–POz wynosi ~35 mm**. Obudowa ustawiona pionowo **mieści obie elektrody krytycznej pary na własnym spodzie** — para, na której stoi twierdzenie, **nie wymaga ani jednego przewodu**. Na przewodach zostają tylko O1 i O2, po ~3,5 cm w bok.

**Trzy architektury:**

| | Co to jest | Werdykt |
|---|---|---|
| A | jedna sztywna płyta 4×8 cm z elektrodami od spodu | **odrzucone** — wygląda jak karta przyklejona do głowy |
| **B** | **obudowa elektroniki + elektrody na przewodach** | **wariant v1** |
| C | sztywna wyspa na podłożu giętkim (flex-PCB), elektrody na cienkich ramionach | **cel v2, opcjonalny.** Wzorzec sprawdzony: cEEGrid, a HardwareX 2022 (PMID 36204424) opublikował gotowy projekt takiej przejściówki **dla OpenBCI** |

**Pomiar nie wymaga postaci docelowej.** Twierdzenie dotyczy geometrii elektrod, nie obudowy. Wariant B wystarcza do całej kampanii.

---

## 5. Stymulator

**Diody LED, nie ekran.** `[fakt]` Ekran ma odświeżanie 60 albo 120 Hz i częstotliwości niebędące jego dzielnikami są odtwarzane z modulacją.

- panel LED sterowany osobnym mikrokontrolerem, częstotliwość z **licznika sprzętowego**, nie z opóźnienia programowego
- **fotodioda w wejściu pomocniczym rejestratora — WARUNEK KONIECZNY, nie udogodnienie.** Dwa zadania: dowieść, że bodziec miał deklarowaną częstotliwość, **oraz zapisać moment zapłonu, żeby okna ciąć względem bodźca, a nie względem początku pliku**

`[fakt]` Dlaczego to jest warunek konieczny: w zbiorze Kołodzieja tego nie ma i przez to **TRCA — metoda o najwyższym ITR w dziedzinie — jest tam niedostępna**, czego nie da się naprawić żadną analizą po fakcie. Sprawdzone: faza SSVEP nie jest zsynchronizowana z oknami (R ≈ 0), TRCA daje 32–34% przy poziomie losowym 33,3%. **To najtańsza pozycja w całym zestawieniu i jedna z najważniejszych.**

**Częstotliwości: 8,0 / 9,4 / 10,8 / 12,2 / 13,6 / 15,0 / 16,4 / 17,8 Hz**, krok 1,4 Hz.

`[fakt]` **Dobór policzony, nie założony.** Kryterium: żadna z pierwszych trzech harmonicznych jednego celu nie pada bliżej niż 0,3 Hz od harmonicznej innego. Ten zestaw ma **zero kolizji**; częstotliwości całkowite z krokiem 1 Hz mają **cztery** (3×8 = 2×12 = 24 Hz). **Nie 7/8/9 Hz** — to pasmo rytmu alfa.

`[wniosek]` Dobór okazał się trafiony także z drugiego powodu: drugie harmoniczne wypadają w **16,0–35,6 Hz**, czyli w paśmie, w którym ECeG reaguje na bodziec wzrokowy — **co umożliwia test rozdzielający mechanizmy** (`04_PLAN_POMIAROWY.md`).

---

## 6. Bezpieczeństwo — warunek wstępny, nie pozycja na końcu

**Cokolwiek elektrycznego w kontakcie z głową: zasilanie wyłącznie bateryjne, żadnego połączenia z siecią w czasie pomiaru.**

- ogniwo litowo-polimerowe, przetwornica na ±2,5 V dla części analogowej
- **transmisja bezprzewodowa w czasie pomiaru.** Kabel USB do laptopa zasilanego z sieci jest drogą powrotną prądu i jest **zakazany w czasie noszenia**
- programowanie i ładowanie **wyłącznie przy zdjętym urządzeniu**, wpisane w procedurę

`[fakt]` Reguły elektryczne ISEF dotyczą **stoiska**: próg 36 V na obwodach odsłoniętych, obudowa niepalna, widoczny wyłącznik, zakaz ogniw otwartych i pakietów powyżej 100 Wh. **Projekt spełnia to bez wysiłku** — pracuje na jednostkach woltów.

---

## 7. Zakupy i budżet

### 7.1 Platforma odniesienia — jedyna pozycja z terminem

`[fakt, katalog producenta]` Cyton 8 kanałów **1 249 USD**, Ganglion 4 kanały **624,99 USD**, sam klucz USB 249 USD.

**Decyzja obowiązująca: kupić UŻYWANEGO Cytona, budżet do 1 600 zł, poszukiwania do 30 IX 2026. Jeżeli do tego terminu nie ma dobrej oferty — nowy Ganglion (~3 000–3 400 zł), nie nowy Cyton.**

**Warunki oferty używanej:** płytka **z kluczem USB** · czytelne oznaczenia **ADS1299** i **PIC32** na zdjęciu · sprzedawca dopuszcza zwrot · zasilanie bateryjne · **test odbiorczy w dniu dostawy**: zewrzeć wejścia, zmierzyć szum RMS w OpenBCI GUI, kwadrans.

**Bez AliExpress.** Przyrząd odniesienia jest jedynym miejscem, gdzie nie wolno mieć wątpliwości co do autentyczności układu scalonego.

**Do czego naprawdę służy:** (1) test, czy SSVEP działa u autora, **zanim istnieje własna płytka** — krytyczne, X 2026; (2) ubezpieczenie, gdyby własny tor nie zadziałał. **Nie jest punktem odniesienia twierdzenia.**

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
| **rezerwa 30% na drugą serię płytek** | 1 000–1 700 zł |
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
