# 05 — Stan wiedzy. Co zmierzono, czego nie, i gdzie leży luka

**Stan na 21 sierpnia 2026.** Materiał źródłowy do rubryki `Research Problem` arkusza ISEF (10 pkt) oraz do kryterium Explory §7 pkt 2d — *„zna dotychczasowe badania"* — **które daje 10 punktów na 40, czyli tyle samo, co innowacyjność.**

**Zasada tego pliku:** każda liczba z podanym N, P i t. Historia przeszukania i błędów po drodze: `11_EWOLUCJA.md` i `METODA.md`.

---

## 1. Wszystko opublikowane, przeliczone na jedną metrykę

Dotąd liczby leżały w trzech postaciach — dokładność przy różnej liczbie celów, ITR przy różnych oknach, procenty bez podanego N — i **nie dawały się porównać**.

`[wniosek]` Pozycje z gwiazdką **przeliczyłem z ich dokładności wzorem Wolpawa**; nie są to wartości podane przez autorów.

| Konfiguracja | N | P | t [s] | **bit/min** |
|---|---|---|---|---|
| Li 2025: 8 kanałów potylicznych, odniesienie na czole | 40 | 0,941 | 1,75 | **160,7\*** |
| Li 2025: 4 kanały | 40 | 0,914 | 1,95 | **136,8\*** |
| Li 2025: 3 kanały (Oz, O1, O2) | 40 | 0,816 | 1,95 | **112,5\*** |
| Imperial College 2022: własne urządzenie za £20, ESP32 | `[luka]` N nieznane | 0,956 | — | **102** (podane) |
| Cardoso 2022: czepek żelowy, elektrody czynne | 8 | 0,990 | 3,55 | **48,8\*** |
| **Li 2025: POz−Oz dwubiegunowy, JEDEN kanał** | **40** | **0,682** | **3,55** | **46,3\*** |
| Cardoso 2022: opaska z elektrodami suchymi | 8 | 0,911 | 3,55 | **39,2\*** |
| Kołodziej 2026: 3 kanały, odniesienie na małżowinie, okno 1 s | 3 | 0,733 | 1,00 | **28,9** |
| Li 2025: Oz sam, odniesienie na czole | 40 | 0,377 | 3,55 | **18,1\*** |
| **Liang 2021: okolica zauszna, najlepszy paradygmat** | 12 | 0,842 | — | **17,8** (podane) |
| Kołodziej 2026: montaż zwarty różnicowy, okno 1 s | 3 | 0,640 | 1,00 | **16,9** |
| PNAS 2025: mikroczujniki między włosami | **2** | 0,964 | 3,55 | **13,1\*** (sufit dla 2 celów: 16,9) |
| **Cardoso 2022: para na wyrostkach sutkowatych** | 8 | 0,297 | 3,55 | **2,5\*** |

### 1.1 Trzy rzeczy, których nie widać w samych procentach

1. **Rozstrzał wewnątrz kategorii „montaż zwarty" wynosi od 2,5 do 46,3 bit/min — osiemnastokrotność.** Kategoria nie ma jednej wartości.
2. **Zwarta para pionowa bije wszystkie układy „wygodne"** — zauszny, sutkowaty, opaskę suchą.
3. **„96,4%" z *PNAS* przy dwóch celach daje 13,1 bit/min — mniej informacji niż 68,25% przy czterdziestu, które dają 46,3.** To jest praktyczny powód zakazu podawania dokładności bez N.

`[fakt]` **Poprawka z 21 VIII 2026, K-107.** Wiersz *PNAS* stał tu wcześniej jako **„~17 (sufit)"** i był **jedynym w tabeli, który podawał inną wielkość niż pozostałe dwanaście**: nie przepustowość przy zmierzonej dokładności, tylko **kres górny dla dwóch celów** (1 bit na wybór ÷ 3,55 s = 16,9 bit/min), osiągalny dopiero przy 100%. Przy ich rzeczywistych 96,4% wychodzi **13,1 bit/min**. Obie liczby są teraz w wierszu, opisane. **Różnica jest istotna dla wniosku 3: przewaga czterdziestu celów nad dwoma jest 3,5-krotna, nie 2,7-krotna.**

---

## 2. Siedem prac, które trzeba znać i cytować

Wszystkie przeszły **procedurę tożsamości** (`METODA.md` §2). **Werdykt dla wszystkich: sąsiedni — wspólne pytanie, inny eksperyment. Żadna nie jest tożsama.**

| Praca | Co zrobili | Gdzie mieli odniesienie | Dlaczego to nie jest ten projekt |
|---|---|---|---|
| **Li X. i in. 2025**, Sheng Wu Yi Xue Gong Cheng Xue Za Zhi 42(3), **PMID 40566767**, po chińsku | noszalny SSVEP-BCI, 10 osób, 40 celów, 94,10%, 115,25 bit/min, *„no significant difference"* wobec warunków laboratoryjnych | **czoło** | zmienną jest **czas przygotowania** (3 min, bez regulacji impedancji), nie geometria. Czepek 8-kanałowy POz…O2, elektrody mokre, 121 g. Warunek kontrolny to **cudzy zbiór Benchmark** |
| **Cardoso i in. 2022**, ICORR, **PMID 36176154** | czepek / opaska żelowa / opaska sucha / para sutkowata, 10 osób, 8 celów, plus czas montażu i zadowolenie | zmienne, w każdym urządzeniu inne | porównuje **gotowe urządzenia**, nie położenie odniesienia. Ale daje **dolny punkt widełek: 29,69%, poziom losowy** |
| **Liang, Bin, Chen, Wang, Gao, Gao 2021** (Tsinghua), J Neural Eng 18(6), **PMID 34875637** | SSVEP z **okolicy zausznej bezwłosej**, nowy paradygmat, 16 osób: 74,6% → **84,2%**, ITR 14,2 → **17,8 bit/min**, odsetek zdatnych 58,3% → 75% | zauszna | rezygnuje z potylicy. **Dolna granica widełek dla formy „wygodnej"** — i pokazuje, że **25% osób jest tam nieskutecznych** |
| **Kim H. i in. 2025**, PNAS 122(15), **PMID 40193612** | mikroczujniki między mieszkami włosowymi, impedancja 0,03 kΩ·cm⁻², 12 h noszenia, demonstracja AR | **Pz**, nieruchome | praca **materiałowo-wytwórcza**; tor kupiony; **dwa cele**; ITR nie podane. Elektroda jest problemem rozwiązanym i opatentowanym |
| **Kołodziej, Majkowski, Wiszniewski 2026** (PW), Sensors 26(3):917, **PMID 41682433** | redukcja artefaktów kanałami pomocniczymi, 12 osób, 3 cele, +9,1 pp | **małżowina** | **dane publiczne, reanalizowane w tym projekcie od zera.** Zysk pochodzi z Cz, nie z kanału mięśniowego |
| **Yan W. i in. 2026** (Xi'an Jiaotong), npj Biomedical Innovations, **PMID 42527436** | rekonstrukcja sygnału potylicznego z czołowego siecią DSTF-Net, 12 + 20 osób, 4 cele, poprawa do 33,47% | **Cz**, u pacjentów **wyrostki sutkowate** | ograniczenie **medyczne** (pacjent leżący, ubytek kości potylicznej), nie gabarytowe. **Rezygnują z potylicy** |
| **Fodor, Cantürk, Heisenberg, Volosyak 2025** (Rhine-Waal), Brain Sci 15(6):549, **PMID 40563723** | c-VEP, **38 osób online**, redukcja montażu **16 → 6 elektrod** (PO3, POz, PO4, O1, Oz, O2), cztery cele; ITR 49,33 → 37,79 → **48,39 bit/min** po douczeniu | **Cz**, masa AFz — **nieruchome we wszystkich trzech warunkach** | zmienną jest **liczba elektrod czynnych**, nie położenie odniesienia. **Odniesienie zostało na czubku głowy, na przewodzie** — czyli praca najsilniej umotywowana wygodą montażu **i tak nie ruszyła tej elektrody** |


`[wniosek]` **Wszystkie siedem trzymają odniesienie nieruchomo, w pięciu różnych miejscach poza modułem: czoło, Cz, Pz, małżowina, wyrostek sutkowaty. Żadna nie zeszła z odniesieniem do wnętrza obszaru potylicznego i nie zmierzyła, ile to kosztuje.**

`[fakt]` **Fodor 2025 jest z tych siedmiu najmocniejszym argumentem za istnieniem luki**, bo to jedyna praca, której **jedynym celem było zmniejszenie montażu** — i która mimo to zostawiła odniesienie na Cz. Rozbiór wg procedury tożsamości (`METODA.md` §2) w `KOREKTY.md` K-103. **Werdykt: sąsiedni.**

---

## 3. Trzy opublikowane wyniki o przeciwnych znakach

**To jest najmocniejsze uzasadnienie problemu, jakie ten projekt ma** — bo opiera się na cudzych liczbach, a nie na przeszukaniu.

| Praca | Co porównała | Werdykt o montażu dwubiegunowym |
|---|---|---|
| **Diez i in. 2010**, EMBC, **PMID 21096910** | O1−P3 i O2−P4 wobec 6 kanałów odniesionych do Fz, 5 osób | **lepszy: 80,1% wobec 74,5%** |
| **Li i in. 2025** | POz−Oz wobec Oz z odniesieniem na czole, 40 celów | **lepszy: 68,25% wobec 37,65%** |
| **reanaliza danych Kołodzieja** (`analiza/`) | pochodne dwubiegunowe wobec 3 kanałów z odniesieniem na małżowinie | **gorszy: 48,8–64,0% wobec 73,3%** |

`[wniosek]` **Sprzeczności nie ma — to nie są te same porównania.** Dwubiegunowy wygrywa, gdy alternatywą jest jeden kiepski kanał obciążony składową wspólną; przegrywa, gdy alternatywą jest porządny montaż wielokanałowy. **Nikt nie zmierzył krzywej pomiędzy, a to jest jedyny sposób pogodzenia tych trzech wyników.**

---

## 4. Mechanizm: pole SSVEP ma strukturę falową

`[fakt]` **Srinivasan R., Bibi F.A., Nunez P.L.**, Brain Topography 18(3):167–187, 2006, **PMID 16544207** — **110 elektrod**, migotanie 3–30 Hz:

> „the spatial distribution of SSVEP power is **strongly dependent on the input frequency**"
> „**Laplacian SSVEPs are sensitive to small changes (1–2 Hz) in the input frequency at occipital and parietal electrodes indicating distinct local sources**"
> „In the upper alpha band (…) **long-wavelength (>15 cm) traveling waves propagating from occipital to prefrontal electrodes**"

`[fakt]` **Thorpe, Nunez, Srinivasan 2007**, Stat Med 26(21), **PMID 17671957** — fale biegnące **λ > 20 cm** w górnym paśmie alfa, w paśmie beta **fale stojące**.

`[wniosek]` **Trzy skutki:**

1. **Wyjaśnia, dlaczego laplasjan w ogóle działa.** Gdyby pole było jednorodne, różnicowanie kasowałoby wszystko. Montaż zwarty **kasuje składową długofalową i zostawia lokalną**
2. **Kierunek propagacji jest znany i pokrywa się z osią projektu** — potylica → przedczołowie, czyli wzdłuż Oz–POz
3. **Daje wzór** (`02_TWIERDZENIE.md` §4), który tłumaczy wszystkie sześć punktów z §1 i trzy sprzeczne wyniki z §3

---

## 5. Dlaczego pole jest puste — odpowiedź z trzech źródeł

Pytanie zadane przez autora: *skoro ledwo kto to tyka, musi być jakiś powód.*

**Odpowiedź: bo przez sto lat nikt nie musiał tego pytania zadawać.**

1. `[fakt]` **Yao D. i in., Brain Topography 32(4):530–549, 2019, PMID 31037477** (praca twórcy techniki REST): problem odniesienia jest *„**unsettled** (…) inspires unceasing debate"*, *„no point on the body fulfills this condition"*, *„**more than ten references are used** (…) This diversity **seriously undermines the reproducibility**"*. Dziedzina rozwiązuje go **obliczeniowo** — REST, średnia po elektrodach, połączone sutkowate. **Wszystkie te metody wymagają wielu elektrod** (PMID 26305167: *„the importance of using a **high-density montage**"*). **Przy dwóch kanałach nie działają i pytanie wraca jako konstrukcyjne**
2. `[fakt]` **Choi S.H. i in., EMBC 2006, PMID 17946448**: *„**most conventional studies do not much consider about the location of the reference electrode**"*. Luka nazwana cudzą ręką dwadzieścia lat temu
3. `[fakt]` **Joyce i Rossion, Clin Neurophysiol 116(11), 2005, PMID 16214404**: położenie odniesienia zmienia mierzony sygnał **pierwszorzędowo** — N170 i VPP okazują się tym samym generatorem widzianym przez dwa różne odniesienia

`[wniosek]` Standardem zostały płatek ucha i wyrostek sutkowaty nie dlatego, że ktoś zmierzył, o ile są lepsze od bliższych, tylko dlatego, że są **bezpieczne** — nad kością, daleko od mięśni, poza obszarem czynnym. **Nic nie kosztują dopiero wtedy, gdy urządzenie ma czepek.**

---

## 6. Zła wiadomość: okolica podpotyliczna nie jest cicha

Trzech nazwanych mieszkańców miejsca, w którym musiałaby usiąść elektroda odniesienia skierowana **w dół**:

1. `[fakt, PMID 12948787]` **mięśnie karku** — Goncharova i in. 2003, 25 osób, 64 elektrody: *„EMG contamination is greatest at the **periphery of the scalp**"*, a widmo EMG ma *„**peaks in the beta frequency range that resemble EEG beta peaks**"*
2. `[fakt, PMID 29886131]` **móżdżek** — Todd, Govender, Colebatch 2018: elektrody nad tylnym dołem czaszki (CB1/CB2, ~5% poniżej PO9/PO10) rejestrują ECeG, a *„**visual stimulation (…) increasing the high-frequency power in CB electrodes, including in beta (14–30 Hz)**"*. **Odniesienie może samo nieść sygnał reagujący na bodziec, w paśmie drugich harmonicznych SSVEP**
3. `[fakt, pomiar własny]` **gładkie pole SSVEP** — montaż zwarty kosztuje **2,7–3,6 dB SNR** w prążku bodźca (`analiza/harmoniczne.py`)

**To jest ryzyko R12** i **główny powód, dla którego kandydat na odniesienie zwarte poszedł w górę (POz), a nie w dół.**

---

## 7. Sterowanie wzrokiem — gdzie leży granica i ile kosztuje jej przekroczenie

**Po co to tu jest:** to jest pytanie, które juror zada, i jedyne pytanie o paradygmat, na które trzeba mieć liczby, a nie zdanie.

### 7.1 Dlaczego SSVEP z potylicy jest z natury sterowany wzrokiem

`[fakt]` Kora potyliczna **jest** korą wzrokową, a jej mapa jest retinotopowa z powiększeniem korowym: dołek środkowy siatkówki zajmuje w niej udział nieproporcjonalnie duży wobec swojej powierzchni. `[fakt]` **Zhou, Hu, Yu, Li 2021** (PMID 34970111, 25 osób, mimośród 0,75°–13,90°): amplituda SSVEP **maleje monotonicznie z mimośrodem** bodźca względem punktu fiksacji. Skierowanie oka na bodziec jest więc **najsilniejszą modulacją, jaka jest w tym miejscu głowy dostępna nieinwazyjnie** — nie jest wyborem projektowym, tylko konsekwencją anatomii.

### 7.2 Cztery drogi wyjścia i ich zmierzony koszt

| Droga | Co zmienia | Zmierzony koszt | Werdykt dla tego projektu |
|---|---|---|---|
| **uwaga utajona** (covert attention) — oko nieruchome, uwaga przesunięta | usuwa zależność od ruchu oczu, **nie od wzroku** | **Kelly i in. 2004** (PMID 17271364): dokładność **spada o ~20 pp** przy samej zamianie jawnej na utajoną. **Lesenfants i in. 2014** (PMID 24838215, Liège): **2 klasy**, 24 osoby zdrowe, offline 85 ± 2%, **online 74 ± 13%**; **0,173 bit na wybór** wobec 4,687 bit u Li 2025 — **27-krotnie mniej informacji na wybór**, niezależnie od czasu okna | **realna, ale to inny wyrób.** Do zapisania jako wariant, nie do zbudowania |
| **RIFT** — znakowanie częstotliwością niewidoczną (rapid invisible frequency tagging) | usuwa **widoczne migotanie**, projektor 1 440 Hz, migotanie 56 i 60 Hz | **Brickwedde i in. 2022** (PMID 36228894) | usuwa zarzut estetyczny, **nie usuwa zależności od wzroku.** Wymaga projektora 1 440 Hz — poza budżetem |
| **zmiana miejsca na głowie** — wyobrażenie ruchu, słuch, dotyk | usuwa wzrok całkowicie | wyobrażenie ruchu: 70–85% przy dwóch klasach u osób wyszkolonych, **15–30% nie opanowuje tego wcale**; sygnał leży nad korą czuciowo-ruchową, nie nad potylicą | **rozbija i moduł, i pomiar.** Odrzucone — patrz §7.3 |
| **inwazyjne** | usuwa wzrok, daje setki bitów na minutę | — | poza zakresem: kategoria ISEF, wiek autora, badani ludzie |

`[fakt]` **Walter, Quigley, Andersen, Mueller 2012** (PMID 22579858) dokłada rzecz, która przesądza sprawę dla **tego** urządzenia: przy uwadze jawnej największa amplituda SSVEP wypada **na środkowych elektrodach potylicznych**, przy utajonej — **na przeciwstronnych ciemieniowo-potylicznych**. `[wniosek]` **Przejście na uwagę utajoną przesuwa sygnał spod modułu.** Moduł zbudowany wokół Oz przestaje wtedy stać w najlepszym miejscu — czyli droga „covert" nie tylko kosztuje 20 pp, ale **podważa sens umieszczenia elektroniki na potylicy.**

### 7.3 Dlaczego to nie jest ograniczenie tego projektu

`[wniosek]` **SSVEP jest w tym projekcie przyrządem pomiarowym, nie produktem.** Twierdzenie (`02_TWIERDZENIE.md`) dotyczy **geometrii elektrody odniesienia**; SSVEP został wybrany, bo jest jedynym paradygmatem, który daje **powtarzalny sygnał o znanej częstotliwości** — a więc metrykę SNR w prążku, która pozwala przypisać zmianę wyniku położeniu elektrody, a nie dyspozycji dnia. Wyobrażenie ruchu tego nie ma: jego **zmienność między sesjami przewyższa mierzony efekt geometrii**, więc zamiana paradygmatu **uniemożliwiłaby pomiar, dla którego projekt istnieje**.

`[wniosek]` Wniosek praktyczny: **zależność od wzroku zostaje, jest opisana w ograniczeniach, i jest opisana liczbami cudzych prac.** Odpowiedź jurorowi — `02_TWIERDZENIE.md` §7, pytanie czwarte.

---

## 8. Konkurencja na ISEF — sprawdzona u źródła

`[fakt]` Baza abstraktów Society for Science, **trzynaście roczników 2014–2026**, przeszukana formularzem:

| Zapytanie | Trafień |
|---|---|
| `SSVEP` | **5** |
| `steady-state visual evoked` | 3 |
| `occipital` | 6 |
| `EEG electrode` | 2 |
| **`ADS1299`** | **0** |

Wszystkie pięć projektów SSVEP to **zastosowania** — sterowanie muzyką, uwierzytelnianie, egzoszkielet, ocena starzenia poznawczego.

`[wniosek]` **Żaden nie dotyczy toru pomiarowego ani geometrii elektrod, i nikt w trzynastu latach nie zbudował na ISEF własnego wzmacniacza EEG.** Projekty EEG na ISEF to w przeważającej większości **klasyfikacja danych**, nie budowa przyrządu. **W rubryce, w której gra ten projekt, konkurencji praktycznie nie ma.**

---

## 9. Wykonalność — potwierdzona cudzą opublikowaną konstrukcją

`[fakt]` **arXiv 2601.01772** (grupa Chin-Teng Lina, UTS Sydney), *„Design and Quantitative Evaluation of an Embedded EEG Instrumentation Platform for Real-Time SSVEP Decoding"* — **dokładnie architektura tego projektu**: ESP32-S3 + ADS1299, 8 kanałów, CCA na urządzeniu.

**Ich zmierzone parametry są poprzeczką dla własnego toru:**

| Wielkość | Ich wynik |
|---|---|
| szum przy zwartym wejściu | **0,08 µV RMS** |
| jitter próbkowania | **0,56 µs** |
| dryf długoterminowy | **< 1 ppm** |
| CMRR | **> 112 dB** |
| spadek CMRR przy niedopasowaniu impedancji | **26,9 dB** |
| wynik online | 99,17%, ITR 27,66 bit/min |

`[wniosek]` **Ryzyko techniczne projektu jest przez tę pracę obniżone**: architektura jest opublikowana i scharakteryzowana, więc pytanie nie brzmi „czy się da", tylko „czy dowiozę". **Odbiera to jednocześnie jakąkolwiek nowość samej konstrukcji** — i dlatego twierdzenie dotyczy pomiaru, a nie sprzętu.

---

## 10. Czego nie sprawdzono i sprawdzić się nie da

`[luka]` **CNKI** — największa chińska baza, blokuje ten adres na poziomie aplikacji (HTTP 418). Chińskie rozprawy doktorskie i materiały konferencyjne pozostają poza zasięgiem. **To jest największa pojedyncza dziura** i tym istotniejsza, że **to właśnie z literatury chińskiej wyszła praca, która zabiła poprzednie brzmienie twierdzenia.** `[domysł]` ryzyko, że siedzi tam praca o odległości odniesienia: **3–6%**.

`[luka]` **KCI i DBpia** (Korea) — za kluczem i logowaniem. **BASE** — blokada adresu IP. **CORE**, **Scilit**, **bioRxiv**, **Espacenet** — 403/502/Cloudflare.

**Zdanie, które wchodzi do materiałów zgłoszeniowych i nie wolno go skracać:**

> **Nie ma tego w dziewięciu bazach naukowych, trzech niezależnych grafach cytowań, sekcjach metod 178 prac i trzynastu rocznikach abstraktów ISEF.**

`[fakt]` **Przeszukanie dowodzi obecności, nigdy nieobecności.** Zdanie „nikt tego nie zmierzył" jest skrótem, który w materiałach musi mieć powyższą postać pełną — inaczej jest twierdzeniem o pierwszeństwie, a te są w tym projekcie zakazane.
