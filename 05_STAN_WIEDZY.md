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

## 7. Czym sterować urządzeniem — siedem opcji, koszty, decyzja

**Po co ta sekcja istnieje:** zarzut *„po co to komu, skoro kamerka śledząca wzrok zrobi to samo"* jest poważny i nie da się go zbyć. Ta sekcja odpowiada na niego liczbami, a przy okazji przechodzi **wszystkie** znane nieinwazyjne sposoby sterowania interfejsem, nie tylko wzrokowe. Przegląd z 21 VIII 2026.

---

### 7.1 Najpierw uczciwie: kamerka wygrywa i zawsze będzie wygrywać

`[fakt]` **Halder, Takano, Kansaku 2018** (PMID 29928196) — jedyne w literaturze bezpośrednie porównanie **czterech sposobów sterowania na tych samych jedenastu osobach, w tym samym zadaniu pięciu wyborów**:

| Sposób sterowania | Dokładność | Czas wyboru | **ITR** |
|---|---|---|---|
| **kamerka śledząca wzrok** | **100%** | 5,1 s | **28,2 bit/min** |
| P300 wzrokowy (BCI) | 88% | 4,8 s | 20,9 bit/min |
| P300 słuchowy (BCI) | 70% | 19,9 s | **3,3 bit/min** |
| P300 dotykowy (BCI) | 71% | 18,0 s | **3,4 bit/min** |

`[wniosek]` **Żaden interfejs mózg–komputer nie bije kamerki u osoby, która panuje nad wzrokiem — i nie chodzi o to, żeby bił.** Ucieczka od wzroku kosztuje **sześciokrotność** wobec najlepszego BCI wzrokowego i **ośmiokrotność** wobec kamerki. To jest cena, którą pole płaci świadomie i od trzydziestu lat, **za jedną rzecz: żeby urządzenie działało wtedy, gdy oko nie działa.**

**Zdanie do wygłoszenia, i jest mocniejsze od dotychczasowego:**

> *Kamerka jest szybsza i tańsza, i tak zostanie. Ja nie konkuruję z kamerką o użytkownika, który panuje nad wzrokiem — konkuruję o tego, który nie panuje, i tam kamerka daje zero. A rzecz, którą mierzę, dotyczy elektrody, nie sposobu sterowania: przenosi się na każde noszone urządzenie EEG, także takie, które ze wzrokiem nie ma nic wspólnego.*

---

### 7.2 Druga liczba, która ustawia całą resztę: u ilu ludzi to w ogóle działa

`[fakt]` Trzy badania jednej grupy (g.tec), ten sam styl, duże próby — **jedyne miejsce w literaturze, gdzie paradygmaty porównano pod względem odsetka ludzi zdatnych:**

| Paradygmat | N osób | **80–100% dokładności** | nie działa wcale |
|---|---|---|---|
| **SSVEP** — Guger 2012, PMID 23181009 | 53 | **96,2%** | **0% — nikt poniżej 60%** |
| **P300** — Guger 2009, PMID 19545601 | 100 | **89%** | < 3% |
| **wyobrażenie ruchu** — Guger 2003, PMID 12899258 | 99 | **19%** | ~7% poniżej 60% |

`[wniosek]` **SSVEP jest paradygmatem, który działa u największej liczby ludzi z wszystkich znanych — i wyprzedza wyobrażenie ruchu pięciokrotnie w paśmie użytecznej dokładności.** Każda zamiana paradygmatu na „intencyjny" jest więc jednocześnie **zamianą urządzenia działającego u wszystkich na urządzenie działające u jednego na pięciu.** Ta liczba wraca w każdej opcji poniżej i jest dla projektu ważniejsza niż ITR, bo od niej zależy, czy pokaz w ogóle wyjdzie (R13).

---

### 7.3 Siedem opcji — co to jest, plusy, minusy, koszt dla projektu

#### Opcja 1. Zostaje jak jest: SSVEP sterowany wzrokiem

**Co to jest:** migający znacznik, patrzysz na niego, urządzenie rozpoznaje częstotliwość.

| Plusy | Minusy |
|---|---|
| **działa u 100% ludzi** (Guger 2012) | **kamerka robi to szybciej** |
| najwyższa przepustowość w całym polu: **46–160 bit/min** | migotanie widoczne i męczące |
| sygnał o znanej częstotliwości → **metryka SNR w prążku**, na której stoi cały pomiar | zależy od kontroli wzroku |
| zero treningu, ~5 minut kalibracji | |

**Koszt zmiany: zero.** To jest stan bieżący.

---

#### Opcja 2. Uwaga nieprzestrzenna na nakładających się powierzchniach — **REKOMENDOWANA jako dodatek**

**Co to jest:** dwie grupy kropek o różnych kolorach obracają się w przeciwne strony **w tym samym miejscu ekranu**, migając z dwiema różnymi częstotliwościami. Patrzysz cały czas w ten sam punkt, a wybierasz **umysłem, którą z dwóch nałożonych powierzchni śledzisz.** SSVEP przy odpowiedniej częstotliwości rośnie.

`[fakt]` **Zhang, Maye, Gao X., Hong, Engel, Gao S. 2010** (Tsinghua + UKE Hamburg, PMID 20083864), 18 osób, trzy dni treningu online: **72,6 ± 16,1% przy dwóch klasach**, poprawa u **8 z 18** osób. Sygnał rejestrowany **nad okolicą ciemieniową i potyliczną**.

| Plusy | Minusy |
|---|---|
| **kamerka przestaje mieć czego mierzyć** — oba bodźce są w tym samym punkcie, więc kierunek wzroku nie niesie informacji. **Jedyna opcja, która ten zarzut zabija, a nie osłabia** | **dwie klasy** — z czterdziestu celów zostają dwa |
| **ten sam sprzęt, te same elektrody, ten sam potok analizy.** Zmienia się wyłącznie bodziec i instrukcja | **72,6%**, i to po trzech dniach treningu |
| **sygnał zostaje SSVEP** → metryka SNR w prążku działa, więc **pomiar geometrii odniesienia przeżywa bez zmian** | poprawa tylko u **8 z 18** osób |
| daje **drugi reżim SNR** do zmierzenia tej samej zależności — a strata odniesienia mierzona przy niskim SNR jest **bardziej informatywna** niż przy wysokim | wymaga **ekranu**, nie panelu LED |

**Koszt dla projektu:** `[wniosek]` **mały i policzalny.** Jeden dodatkowy program bodźcowy plus **dwie sesje pomiarowe** (~4 h). Konflikt z decyzją „diody LED, nie ekran" (§3 `03_SPRZET.md`) rozwiązuje się warunkiem: **w tym jednym warunku wolno użyć ekranu, ale wyłącznie z częstotliwościami będącymi dokładnymi dzielnikami odświeżania** — przy 120 Hz to **10, 12 i 15 Hz** — a fotodioda i tak weryfikuje bodziec. **Twierdzenie się nie zmienia. Moduł się nie zmienia. Elektrody się nie zmieniają.**

**Czego to NIE daje:** urządzenia użytkowego. Dwie klasy przy 72,6% to jest **dowód możliwości i materiał na film**, nie sposób sterowania żarówką.

---

#### Opcja 3. RSVP — wszystko w jednym punkcie, po kolei

**Co to jest:** litery albo ikony pokazują się **jedna po drugiej w tym samym miejscu**, szybko. Czekasz na swoją. Mózg reaguje falą P300 na tę właściwą.

`[fakt]` **Acqualagna i Blankertz 2013** (PMID 23466266): 30 symboli, **wszystkie 12 osób opanowało**, 94,8% dokładności, 1,43 symbolu/min → **6,2 bit/min**. **Lin i in. 2018** (PMID 29463870), potrójny RSVP: **20,3 bit/min** przy 79%, 10 s na znak, **na obszarze 90 × 195 pikseli** — wielkości ekraniku zegarka. **Chennu i in. 2013** (PMID 23895406): RSVP klasyfikuje się **tak samo dobrze** jak klasyczna matryca, ale jest **wyraźnie wolniejszy**; matryca opiera się na wzrokozależnych VEP, **RSVP wyłącznie na niezależnym od przestrzeni P300b**.

| Plusy | Minusy |
|---|---|
| **całkowicie niezależne od kierunku wzroku** — kamerka bezużyteczna | **sygnał przenosi się na ciemię (Pz), nie potylicę** |
| **działa u wszystkich** (12/12 u Acqualagny) | 6–20 bit/min, czyli **2–8× mniej** niż SSVEP zwarty |
| trzydzieści celów, nie dwa | wymaga skupienia i jest męczące |
| mieści się na ekranie zegarka | |

**Koszt dla projektu:** `[wniosek]` **duży i strukturalny.** P300b ma maksimum na **Pz — ~10,5 cm powyżej inionu**, czyli **poza modułem potylicznym**. Moduł musiałby urosnąć z pary Oz–POz (3,5 cm) do pasa Oz–Pz — **z pudełka zapałek w pasek wzdłuż tyłu głowy**. Do tego P300 jest odpowiedzią **jednorazową, bez znanej częstotliwości**, więc **metryka SNR w prążku znika i cały aparat pomiarowy trzeba zbudować od nowa.** **Twierdzenie o geometrii przeżywa, ale pomiar trzeba przeprojektować, a moduł powiększyć.**

---

#### Opcja 4. Uwaga utajona przestrzenna — **REKOMENDACJA PO POPRAWCE, mocniejsza od opcji 2**

**Co to jest:** bodźce w różnych miejscach, jak zwykle, **oko nieruchomo w punkcie fiksacji pośrodku**, a wybór następuje przez przesunięcie **uwagi**, nie spojrzenia.

`[fakt]` **Poprawka z 21 VIII 2026, K-109.** Ta opcja stała tu wcześniej jako odrzucona, z uzasadnieniem *„kamerka nadal działa, bo bodźce są w różnych miejscach"*. **To było błędne rozumowanie.** Kamerka odczytuje **kierunek patrzenia**, a przy uwadze utajonej kierunek patrzenia **jest stały przez cały czas i identyczny dla każdego wyboru**. Kamerka ma więc **zero informacji o wyborze** — dokładnie tak samo jak przy nałożonych powierzchniach. **Zarzut o kamerkę znika tu równie skutecznie, a reszta bilansu wypada lepiej.**

**Liczby, w kolejności powstawania:**

| Praca | Układ | Wynik |
|---|---|---|
| **Kelly i in. 2004** (PMID 17271364) | jawna wobec utajonej, ten sam układ | **−20 pp** — górna granica kary, **sprzed dwudziestu dwóch lat** |
| **Zhang i in. 2010** (PMID 20083864) | nałożone powierzchnie, 2 klasy, 3 dni treningu | 72,6 ± 16,1% |
| **Lesenfants i in. 2014** (PMID 24838215) | 2 klasy, online, pacjenci LIS | 74 ± 13% |
| **Egan i in. 2017** (PMID 28513478) | hybryda SSVEP + alfa **+ P300** | **+9 pp** z samego dołożenia trzeciej cechy |
| **Zhang i in. 2021, EMBC** (PMID 34892414) | **kodowanie fazowe jednej częstotliwości**, 2 stymulatory 15 Hz w przeciwfazie, **9 osób bez żadnego doświadczenia z BCI, bez treningu** | **88,4 ± 8%**, i autorzy piszą wprost, że to *„otwiera drogę do znacznie większej liczby celów"* |

| Plusy | Minusy |
|---|---|
| **kamerka pokonana** — oczy stoją, więc nie ma czego śledzić | `[luka]` 88,4% to **symulacja trybu online offline**, 9 osób, dwie klasy |
| **ten sam sprzęt, ten sam typ bodźca, ten sam SSVEP** — metryka i pomiar bez zmian | sceptyk może powiedzieć „a może zerknął" — odpowiada na to **wideo oczu** w pokazie |
| **88,4% u osób bez treningu** wobec 72,6% po trzech dniach — **nowsza metoda usuwa główny koszt opcji 2** | `[fakt]` **Walter i in. 2012** (PMID 22579858): maksimum przenosi się na **przeciwstronne ciemieniowo-potyliczne** — czyli na **O1, O2 i POz**, które są w montażu, ale nie na Oz |
| **skaluje się na więcej niż dwa cele**, w przeciwieństwie do nałożonych powierzchni | powyżej ~4 celów pole tego nie zbadało — `[luka]` |
| bodziec da się zrobić na **panelu LED**, bez ekranu | |

**Koszt dla projektu: taki sam jak opcji 2, a wynik lepszy.** Moduł, elektrody, tor i metryka bez zmian; **odpada trzydniowy trening i odpada wymóg ekranu.**

---

#### Opcja 5. Intencje ruchowe — wyobrażenie ruchu

**Co to jest:** wyobrażasz sobie ruch prawej ręki albo stopy. Nad korą ruchową spada moc rytmu mu. Żadnego bodźca zewnętrznego — to jest interfejs „aktywny", czyli najbliższy potocznemu „sterowaniu myślą".

`[fakt]` Guger 2003 (PMID 12899258), 99 osób: **tylko 19% osiąga 80–100%**; ~93% przekracza 60%, co przy dwóch klasach jest blisko przypadku.

| Plusy | Minusy |
|---|---|
| **żadnego bodźca — sterujesz, kiedy chcesz**, nie kiedy urządzenie miga | **działa u jednego na pięciu** w paśmie użytecznym |
| brzmi najlepiej ze wszystkiego, i to nie jest bez znaczenia na stoisku | dwie–cztery klasy, dni treningu |
| niezależne od wzroku, słuchu i dotyku | **sygnał leży nad korą czuciowo-ruchową — C3, C4, Cz, czyli na czubku głowy** |

**Koszt dla projektu: całkowity.** `[wniosek]` **Moduł potyliczny przestaje mieć rację bytu**, bo nad potylicą nie ma czego mierzyć. Znika też metryka: rytm mu nie ma znanej częstotliwości bodźca, a jego **zmienność między sesjami przewyższa efekt geometrii, który projekt mierzy** — więc **pomiar staje się niewykonalny**, nie tylko trudniejszy. **To nie jest zmiana paradygmatu, to jest inny projekt.**

---

#### Opcja 6. Intencje językowe — mowa wewnętrzna

**Co to jest:** wypowiadasz słowo w myślach, urządzenie je rozpoznaje. To jest to, co ludzie mają na myśli, mówiąc „czytanie myśli".

`[fakt]` Przegląd systematyczny **Alzahrani, Banjar, Mirza 2024** (PMID 39771903, pełny tekst przejrzany): klasyfikacja binarna **~60%**, najlepsze zgłoszone podejście **ponad 72%**, wieloklasowo **45–60%**.

| Plusy | Minusy |
|---|---|
| najbardziej naturalne, gdyby działało | **60% przy dwóch klasach to jest 0,03 bita na wybór — praktycznie zero informacji** |
| bardzo aktywne pole badawcze | z EEG powierzchniowego **nie działa i nikt nie twierdzi, że działa** |

**Koszt dla projektu: całkowity, plus ryzyko wiarygodności.** `[wniosek]` Projekt licealny obiecujący dekodowanie mowy wewnętrznej z EEG **przegrywa u pierwszego jurora, który zna liczby.** **Odrzucone.**

---

#### Opcja 7. Zmysł inny niż wzrok — słuch i dotyk

**Co to jest:** dźwięki w słuchawkach albo wibracje na palcach zamiast migających świateł. P300 albo odpowiedź ustalona (SSSEP — dotykowy odpowiednik SSVEP, przegląd: **Petit, Rouillard, Cabestaing 2021**, PMID 34725311).

`[fakt]` Halder 2018 (ta sama tabela co §7.1): słuchowy **3,3 bit/min**, dotykowy **3,4 bit/min**. `[fakt]` Dekodowanie uwagi słuchowej („na którego mówcę patrzę uchem") jest polem żywym, ale to **dwie klasy i 56,3% przy oknie 1 s** dla modelu niezależnego od osoby (AADNet 2025, PMID 40633040) — narzędzie dla aparatów słuchowych, nie kanał sterujący.

| Plusy | Minusy |
|---|---|
| **całkowicie niezależne od wzroku** — jedyna rodzina, o której da się to powiedzieć bez zastrzeżeń | **3,3–3,4 bit/min: ośmiokrotnie mniej niż kamerka, czternastokrotnie mniej niż SSVEP zwarty** |
| działa u osób niewidomych | wibratory albo słuchawki na stałe na ciele — **gorszy gabaryt niż to, co projekt odrzucił** |
| SSSEP zachowuje logikę „znanej częstotliwości" | sygnał nad korą czuciową i słuchową — **znowu nie nad potylicą** |

**Koszt dla projektu: całkowity.** Moduł potyliczny znika, twierdzenie o geometrii potylicznej znika razem z nim.

---

### 7.4 Zestawienie i decyzja

| Opcja | Kamerka przestaje być zarzutem? | Moduł potyliczny przeżywa? | Pomiar geometrii przeżywa? | Ile celów | Koszt |
|---|---|---|---|---|---|
| 1. SSVEP wzrokiem (stan bieżący) | nie | **tak** | **tak** | **40** | zero |
| **4. Uwaga utajona przestrzenna** | **TAK** | **tak** | **tak** | **2, realnie do 4** | **11–15 h** |
| 2. Uwaga nieprzestrzenna, nakładane powierzchnie | **tak** | tak | tak | **2, i nie więcej** | 11–15 h + ekran + 3 dni treningu |
| 3. RSVP | tak | nie — moduł rośnie do Pz | nie — trzeba zbudować od nowa | 30 | duży |
| 5. Wyobrażenie ruchu | tak | **nie** | **nie** | 2–4 | inny projekt |
| 6. Mowa wewnętrzna | tak | **nie** | **nie** | — | inny projekt + ryzyko |
| 7. Słuch, dotyk | tak | **nie** | **nie** | do 36 | inny projekt |

`[wniosek]` **Dwie opcje z siedmiu zabijają zarzut o kamerkę, nie ruszając ani modułu, ani elektrod, ani metryki, ani twierdzenia — 4 i 2.** Wszystkie pozostałe, które usuwają wzrok, **usuwają razem z nim potylicę**, a z potylicą całą podstawę projektu.

**Z tych dwóch lepsza jest opcja 4**, bo skaluje się na więcej niż dwa cele, nie wymaga trzydniowego treningu, nie wymaga ekranu i ma nowszy, wyższy wynik odniesienia (88,4% u osób nieprzeszkolonych wobec 72,6% po treningu).

### 7.5 Dlaczego liczba celów bije dokładność — i na tym stoi kompromis

`[fakt, przeliczone wzorem Wolpawa]` Zarzut *„rezygnacja z 90% celów boli"* jest słuszny co do odczucia, ale **kierunek naprawy jest inny, niż się wydaje: nie podnosić dokładności, tylko dokładać cele.**

| Konfiguracja utajona | bit na wybór | ITR przy oknie 5 s |
|---|---|---|
| 2 cele, 72,6% (Zhang 2010, po 3 dniach) | 0,153 | **1,8 bit/min** |
| 2 cele, 88,4% (kodowanie fazowe 2021) | 0,482 | **5,8 bit/min** |
| **4 cele, 78%** | **0,891** | **10,7 bit/min** |
| **4 cele, 85%** | 1,152 | **13,8 bit/min** |
| 8 celów, 70% | 1,277 | **15,3 bit/min** |

`[wniosek]` **Cztery cele przy 78% dają prawie dwukrotnie więcej niż dwa cele przy 88%, i sześciokrotnie więcej niż konfiguracja Zhanga.** Osiem celów przy 70% bije wszystko powyżej. **Wzór Wolpawa karze małą liczbę celów mocniej, niż nagradza wysoką dokładność** — dlatego drabinka 2 → 4 → 8 jest właściwą strategią, a zatrzymanie się na dwóch było moim błędem projektowym, nie ograniczeniem paradygmatu.

**Rekomendacja po poprawce:** zostawić SSVEP wzrokowy jako paradygmat główny i dołożyć E6 — uwagę utajoną przestrzenną, z drabinką 2 → 4 → 8 celów.

> **Stan decyzji (P38): ODŁOŻONA 21 VIII 2026.** Projekt idzie w wersji podstawowej. Gotowy plan E6, wraz z terminami powrotu do decyzji — **§7.6 poniżej**.

---

### 7.6 Gotowy plan warunku E6 — ODŁOŻONY 21 sierpnia 2026

> **Stan: odłożone, nie odrzucone.** Decyzja autora z 21 VIII 2026, cytat: *„Szczerze, nie wiem. Zachowaj to w jakimś dokumencie, na razie zostajemy przy wersji podstawowej."*
>
> **Co obowiązuje:** projekt idzie w wersji podstawowej — **SSVEP sterowany wzrokiem, czterdzieści celów, jeden tryb.** Warunku E6 **nie ma w `04_PLAN_POMIAROWY.md`, nie ma w harmonogramie i nie wchodzi do żadnych materiałów.**
>
> **Po co ten plan tu leży:** żeby decyzja dała się podjąć później **bez powtarzania przeglądu**. Wszystko poniżej jest gotowe do uruchomienia w dniu, w którym autor powie „tak".
>
> **Kiedy wrócić — trzy wyzwalacze, którykolwiek pierwszy:**
> 1. **31 III 2027**, przy produkcji materiału półfinałowego — **ostatni moment**, w którym scenę bez wzroku da się nakręcić przed półfinałem. Po tej dacie E6 przestaje mieć wartość demonstracyjną na sezon 2027
> 2. **po dry-runie na El-Robo-Mech (IV 2027)** — jeżeli zarzut o kamerkę padnie od kogoś z zewnątrz, to jest sygnał, że sama odpowiedź słowna nie wystarcza
> 3. **jeżeli E0 (X 2026) wypadnie bardzo dobrze** — mocna własna odpowiedź SSVEP obniża ryzyko, że tryb utajony nie zadziała, i zmienia rachunek
>
> **Koszt odłożenia: zero.** E6 nie dzieli niczego ze ścieżką główną — nie zmienia modułu, elektrod, toru, metryki ani twierdzenia. **Jedyne, co odłożenie zabiera, to czas** — 11–15 h, które w maju–czerwcu 2027 są, ale tylko dzięki przeniesieniu materiału półfinałowego na marzec–kwiecień.

#### Plan warunku E6, gotowy do uruchomienia

**Po co:** odpowiedzieć na zarzut *„po co to, skoro kamerka"* **działającą demonstracją zamiast argumentu**, oraz zmierzyć tę samą zależność od geometrii odniesienia **w drugim, trudniejszym reżimie SNR**. Rozbiór siedmiu paradygmatów: §7.3 powyżej.

**Paradygmat, wersja obowiązująca po poprawce z 21 VIII 2026 (K-109): uwaga utajona przestrzenna.** Bodźce w kilku miejscach wokół **nieruchomego punktu fiksacji pośrodku**; oko stoi w środku przez cały czas, wybór następuje przez przesunięcie **uwagi**. `[fakt]` Wzorzec: **Zhang i in. 2021, EMBC, PMID 34892414** — kodowanie fazowe jednej częstotliwości (15 Hz w przeciwfazie), **88,4 ± 8% u dziewięciu osób bez żadnego doświadczenia z BCI i bez treningu**.

**Dlaczego to, a nie nałożone powierzchnie** (poprzednia wersja tej sekcji): kamerka odczytuje **kierunek patrzenia**, a przy uwadze utajonej kierunek patrzenia jest **stały i identyczny dla każdego wyboru** — więc kamerka jest pokonana tak samo, a poza tym odpada **trzydniowy trening**, odpada **wymóg ekranu** (bodziec robi się na panelu LED) i **znika sufit dwóch celów**. Rozbiór: `05_STAN_WIEDZY.md` §7.3 opcja 4 i §7.5.

### Drabinka celów — bo liczba celów bije dokładność

`[fakt, przeliczone]` **4 cele przy 78% dają 10,7 bit/min, a 2 cele przy 88% tylko 5,8.** Wzór Wolpawa karze małą liczbę celów mocniej, niż nagradza wysoką dokładność. Dlatego E6 **nie zatrzymuje się na dwóch celach**:

| Krok | Cele | Kryterium przejścia dalej |
|---|---|---|
| **E6a** | **2** (lewo–prawo) | dokładność **> 70%** → idź dalej |
| **E6b** | **4** (góra, dół, lewo, prawo) | **ITR wyższy niż w E6a** → idź dalej |
| **E6c** | **8** | **ITR wyższy niż w E6b** → zostaw jako wynik |

**Zatrzymanie następuje na kroku, po którym ITR przestaje rosnąć** — i to jest wynik do zaraportowania, a nie porażka. `[luka]` Powyżej czterech celów **pole tego nie zbadało**, więc E6c jest wejściem w niezbadane, z odpowiednio ostrożnym opisem.

**Wariant zapasowy:** jeżeli sceptyk zakwestionuje, czy oko naprawdę stało, **wraca wariant z nałożonymi powierzchniami** (Zhang 2010, dwie chmury kropek obracające się w przeciwne strony w jednym punkcie, 72,6%) — tam zerknąć **nie ma dokąd**. Kosztuje ekran i trzy dni treningu, więc jest zapasem, nie planem.

**Dlaczego to nie rusza niczego w projekcie:**

| Element | Czy się zmienia |
|---|---|
| moduł, obudowa, gabaryt | **nie** |
| rozkład elektrod (`03_SPRZET.md` §2) | **nie** |
| tor analogowy, ADS1299, fotodioda | **nie** |
| metryka: SNR w prążku, ITR wzorem Wolpawa | **nie** — sygnał pozostaje SSVEP o znanej częstotliwości |
| twierdzenie i jego zmienna niezależna | **nie** |
| bodziec i instrukcja dla badanego | **tak — to jest cała zmiana** |

**Odstępstwo, które trzeba zapisać:** `[fakt]` bodziec wymaga **ekranu**, a `03_SPRZET.md` §5 nakazuje diody LED. **Warunek dopuszczenia: wyłącznie częstotliwości będące dokładnymi dzielnikami odświeżania ekranu** — przy 120 Hz są to **10, 12 i 15 Hz** — plus **obowiązkowa weryfikacja fotodiodą**, tak jak w warunku głównym. Poza tymi częstotliwościami warunek jest nieważny.

**Rozmiar — poprawiony 21 VIII 2026, poprzednie oszacowanie było zaniżone (K-108a):**

| Pozycja | Godziny |
|---|---|
| napisanie programu bodźcowego (dwie obracające się chmury kropek, dwie częstotliwości) | `[domysł]` **4–8 h** |
| **trzy sesje treningowe** — Zhang i in. prowadzili **trzydniowy trening online**, bez niego wynik 72,6% nie powstał | **~3 h** |
| dwie sesje pomiarowe, po 120 prób, dwie klasy | **~4 h** |
| **razem** | **11–15 h** |

`[fakt]` **Wcześniej stało tu „dwie sesje, ~4 h" — pominąłem trening, który u Zhanga był warunkiem uzyskania wyniku.** Poprawione.

`[wniosek]` **Gdzie te godziny są:** w miejscu zwolnionym przez przeniesienie materiału półfinałowego z maja–czerwca na marzec–kwiecień (K-107, budżet godzin w `07_HARMONOGRAM.md`) — tamta poprawka zwolniła w maju–czerwcu **~45–70 h**. **E6 mieści się w niej z zapasem, ale tylko dlatego, że tamta poprawka została wykonana.** Program bodźcowy pisze się wcześniej, w slocie pracy merytorycznej.

**Przewidywanie zapisane z góry:** `[domysł]` dokładność **75–88% przy dwóch celach** i **65–80% przy czterech**; **strata z tytułu zwarcia odniesienia będzie WIĘKSZA niż w warunku wzrokowym**, bo modulacja uwagą jest słabsza od modulacji fiksacją, więc ten sam ubytek SNR zjada większą część zapasu. **Jeżeli strata okaże się mniejsza — to jest wynik przeciwny do przewidywania i raportuje się go w całości.**

**Kryterium zaniechania:** jeżeli po dwóch sesjach dokładność w kroku E6a nie przekroczy **70% przy dwóch celach**, warunek zamyka się wynikiem negatywnym *„u autora ten tryb nie działa"* i **nie jest powtarzany.** `[wniosek]` Ryzyko jest **niższe niż w poprzedniej wersji planu**: kodowanie fazowe dało 88,4% u **osób bez treningu**, więc nie ma tu progu wejścia w postaci trzech dni ćwiczeń.

##### Jak wyglądałaby demonstracja

**Problem do rozwiązania nie jest techniczny, tylko dramaturgiczny:** dwie klasy przy 72% same z siebie wyglądają gorzej niż czterdzieści przy 95%. **Siła tego trybu nie leży w tym, co potrafi, tylko w tym, czego kamerka przy nim nie potrafi** — a to widać dopiero w zestawieniu. Dlatego pokaz jest **jednym ciągiem z czterech scen**, a nie osobną atrakcją.

**Scena 1 — tryb wzrokowy, ~30 s.** Jak dotąd: spojrzenie na żarówkę ją zapala, spojrzenie na gniazdko uruchamia wentylator. Szybko i płynnie. `[wniosek]` **Juror w tym momencie myśli „ładne, ale kamerka zrobi to samo" — i ma rację.**

**Scena 2 — wyprzedzenie zarzutu, ~10 s.** Zarzut wypowiada **autor, nie juror**:
> *Kamerka jest szybsza. Zmierzono to na jedenastu osobach w tym samym zadaniu: kamerka 28,2 bita na minutę, najlepszy interfejs mózgowy 20,9. Teraz drugi tryb.*

**Scena 3 — tryb bez wzroku, ze świadkiem, ~60 s.** Na stole **krzyżyk fiksacji pośrodku i cztery migające pola wokół niego** — góra, dół, lewo, prawo. Obok — **telefon na statywie, pokazujący zbliżenie na oczy autora na żywo.** Autor patrzy **w krzyżyk i tylko w krzyżyk**, przez całą scenę. Zapowiada kolejno „góra", „prawo", „dół" — i za każdym razem włącza się inne urządzenie. **Oczy przez cały czas stoją w tym samym punkcie.**

> `[wniosek]` **To jest cała demonstracja.** Juror widzi na drugim ekranie, że **oczy stoją w jednym punkcie** — a mimo to za każdym razem włącza się co innego. **Kamerka patrzy na te same nieruchome oczy i nie ma z czego odczytać wyboru. Urządzenie odczytuje.** Im więcej celów w tej scenie, tym mocniej: przy czterech **przypadek daje 25%**, a widz liczy to sam.

**Scena 4 — cena, podana samemu, ~10 s.**
> *W tym trybie mam cztery cele zamiast czterdziestu i około osiemdziesięciu procent zamiast dziewięćdziesięciu pięciu. To jest cena rezygnacji ze wzroku i jest zmierzona. Kara podana w literaturze w 2004 roku wynosiła dwadzieścia punktów procentowych — sprawdzam, ile z niej zostało po dwudziestu latach lepszych metod odczytu.*

**Dlaczego kamera na oczy, a nie prawdziwy okulograf.** `[wniosek]` Telefon pokazujący oczy kosztuje zero, nie wymaga oprogramowania, i — najważniejsze — **juror weryfikuje go własnymi oczami.** Prawdziwy okulograf wprowadzałby pytanie *„a skąd wiemy, że był dobrze skalibrowany"*, czyli zamieniałby dowód na kolejną rzecz do uwierzenia.

**Wersja filmowa na półfinał:** **ekran dzielony** — po lewej zbliżenie na nieruchome oczy, po prawej plama i przełączająca się żarówka. Obie rzeczy jednocześnie, **w pierwszych dziesięciu sekundach filmu** (reguła z `07_HARMONOGRAM.md`, kamień milowy 7).

**Plan awaryjny, jeżeli tryb u autora nie zadziała.** `[fakt]` U Zhanga poprawiło się **8 z 18 osób**, więc szansa jest z grubsza pół na pół. Wtedy **scena 3 zostaje, ale z wynikiem negatywnym**: *„u mnie ten tryb dał X procent, poniżej progu — to jest wynik, który raportuję"*. `[fakt]` Z analizy stawki finałowej 2026 (`08_KONKURSY.md` §3.1 pkt 4): **raportowanie wyników negatywnych obok pozytywnych robi jeden projekt w całej stawce.** To jest przewaga wiarygodnościowa do wzięcia za darmo — i jedyny znany mi pokaz, który **działa także wtedy, gdy się nie udał.**

**Zasada wiążąca:** **sceny 3 nie wolno obiecać w żadnym materiale przed wykonaniem E6.** Do filmu i na plakat wchodzi dopiero po pomiarze, z własną liczbą.

**Koszt sprzętowy pokazu: zero złotych** — tablet albo laptop i telefon na statywie już są.

**Czego E6 NIE jest:** nie jest urządzeniem użytkowym i nie zastępuje trybu głównego. **Tryb wzrokowy zachowuje wszystkie czterdzieści celów — nic nie jest oddawane.** Urządzenie ma **dwa biegi**: szybki, gdy oko działa, i wolniejszy, gdy nie działa. Do materiałów zgłoszeniowych E6 wchodzi jako warunek dodatkowy, **nigdy jako główny wynik**.

**Drugi wynik, który E6 daje przy okazji, i który jest ciekawszy od samego pokazu:** `[fakt]` kara za przejście z uwagi jawnej na utajoną została zmierzona w **2004 roku i wyniosła −20 pp**. `[fakt]` W 2021 kodowanie fazowe dało **88,4% u osób nieprzeszkolonych**, co sugeruje, że kara zmalała — ale **nikt tego nie zmierzył wprost na jednym torze i jednej osobie**. E6 mierzy dokładnie to: **na tym samym sprzęcie, tą samą osobą, tym samym paradygmatem** — czyli w tej samej formie, w jakiej postawione jest twierdzenie główne. `[wniosek]` **To zamienia E6 ze słabszego trybu w drugi, mały wynik pomiarowy.**

---

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
