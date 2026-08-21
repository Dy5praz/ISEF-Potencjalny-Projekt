# 04 — Plan pomiarowy

**Stan na 21 sierpnia 2026.** Co mierzone, ile prób, jakie zakresy zmiennych, jaka niepewność.

**Zasada nadrzędna:** wszystko poniżej ma być **zapisane przed pierwszym pomiarem i raportowane w całości**, także to, co wyjdzie źle. `[fakt]` Wybieranie po fakcie metryki, która wypadła najlepiej, jest wymienione w Załączniku nr 1 regulaminu Explory jako naruszenie standardów etycznych.

---

## 1. Rejestracja twierdzeń z góry

Zapisuję **dwa** twierdzenia. Oba będą raportowane niezależnie od wyniku. Główne wskazuję dopiero po pierwszej pełnej sesji, i **wskazanie też jest odnotowane z datą**.

| | **T1 — główne** | **T2 — towarzyszące** |
|---|---|---|
| treść | przepustowość SSVEP zależy monotonicznie od odległości elektrody odniesienia od aktywnej okolicy potylicznej; istnieje odległość progowa, poniżej której przepustowość gwałtownie spada | montaż wewnątrz modułu ma krótszy czas założenia i mniejszy dryf jakości sygnału w ciągu dnia niż montaż z odniesieniem odległym |
| metryka | dokładność, ITR (Wolpaw), z jawnymi N, P, t | czas montażu, dryf impedancji i SNR w ciągu dnia, odsetek sesji bez rekalibracji |
| przewidywanie z góry | spadek **9–24 pp** przy zejściu z odniesienia odległego do zwartego (`12_REANALIZA.md` §5) | brak przewidywania ilościowego `[luka]` — pole nieraportowane |
| co obala | brak monotoniczności albo spadek < 3 pp na całym zakresie | brak różnicy w czasie montażu |
| ograniczenie formalne | brak | **nie wolno wiązać z wyspaniem ani zmęczeniem** — to jest zmienna ludzka i łamie zwolnienie ISEF dla badania na sobie (`11_EWOLUCJA.md`, `09_FORMALNOSCI.md` §1.1) |

**Twierdzenie warunkowe T3** (kontrybucja druga, uruchamiane tylko jeśli E4 pokaże efekt): kompensacja EMG karku z dedykowanego kanału poprawia przepustowość **wtedy i tylko wtedy**, gdy elektroda odniesienia leży nad mięśniem — czyli w konfiguracji wymuszonej przez gabaryt. **W danych publicznych nie da się tego sprawdzić** (`12_REANALIZA.md` §8 pkt 3).

> **Zawężenie T3 po teście z §6A pliku `14`, 16 VIII 2026.** Kanał **szczękowy** wypadł z projektu — jego sufit to +0,6 pp nawet w oknach najbardziej skażonych i przy regresorach nieliniowych, przy p = 0,166. **T3 dotyczy wyłącznie EMG karku w konfiguracji z odniesieniem nad mięśniem** i tylko dlatego przeżywa, że tej konfiguracji cudze dane nie zawierają. **Przewidywanie z góry dla T3 brzmi: efektu nie będzie.** Zapisuję to teraz, żeby wynik negatywny był wynikiem, a nie porażką.

---

---

---

## 1B. Przewidywanie ilościowe zapisane z góry

**Dopisane 21 VIII 2026.** To jest rejestracja twierdzenia w mocniejszej postaci niż „spodziewam się spadku": **krzywa z wzorem i parametrem wziętym z cudzych pomiarów.**

`[wniosek, wyprowadzenie z opublikowanych długości fali — NIE pomiar]` Pole SSVEP ma strukturę falową: fale biegnące o **λ > 15–20 cm**, propagujące się **potylica → przedczołowie**, czyli wzdłuż osi Oz–POz (Srinivasan i in. 2006, PMID 16544207, 110 elektrod; Thorpe i in. 2007, PMID 17671957). Dla pary elektrod odległej o `d` **wzdłuż osi propagacji** amplituda różnicy wynosi:

> **`|2 · sin(π·d/λ)|`** względem amplitudy pojedynczej elektrody

| d | λ = 15 cm | λ = 20 cm |
|---|---|---|
| 2,0 cm | 0,81 | 0,62 |
| **3,5 cm (Oz–POz)** | **1,34** | **1,04** |
| 7,0 cm | 1,99 | 1,78 |

**Trzy przewidywania, wszystkie do sprawdzenia tym planem:**

1. **strata zależy od `d/λ`, nie od samego `d`** — więc **musi zmieniać się z częstotliwością bodźca**. Zestaw 8,0–17,8 Hz przechodzi przez trzy różne reżimy falowe
2. **optimum odległości przy `d ≈ λ/2`** (7–10 cm, poza modułem); przy 3,5 cm jest się na ~70% maksimum, przy 2 cm na ~40%
3. **kierunek daje efekt większy niż odległość** — para 3,5 cm wzdłuż osi bije parę 7 cm w poprzek

`[luka]` Model jednofalowy jest **najprostszym możliwym**, nie kompletnym — nie obejmuje źródeł lokalnych, rozmycia przez czaszkę ani zanieczyszczeń z R12.

## 1C. Test rozdzielający mechanizmy — koszt jedna kolumna

**Raportować SNR osobno dla częstotliwości podstawowej f₀ i dla drugiej harmonicznej 2f₀, przy każdym położeniu odniesienia.**

Dwa mechanizmy dają różne przewidywania:

- **gładkie pole** kasuje podstawową i harmoniczne podobnie → strata **niezależna od częstotliwości**
- **zanieczyszczenie odniesienia sygnałem z móżdżku** (R12) siedzi w paśmie beta → strata **wyraźnie większa dla drugiej harmonicznej**

`[luka]` **Na danych Kołodzieja testu wykonać się nie da** — przy bodźcach 7/8/9 Hz drugiej harmonicznej praktycznie nie ma (SNR −0,04 do +0,16 dB we wszystkich montażach). Zestaw 8,0–17,8 Hz daje harmoniczne w paśmie **16,0–35,6 Hz** i test umożliwia.

`[fakt, pomiar własny, `analiza/harmoniczne.py`]` Co już wiadomo: **montaż zwarty kosztuje 2,7–3,6 dB SNR w prążku bodźca.**


## 1D. Eksperyment E0 — przesiew, PIERWSZY POMIAR W CAŁYM PROJEKCIE

**Dodany 16 VIII 2026 po pytaniu użytkownika, czy da się rozpoznać ryzyko R1 łatwiej niż pełną kampanią. Da się.**

`[fakt, dwa niezależne zespoły]` **Velut i in., *Imaging Neuroscience* 4, 2026** oraz **Thielen, *Biomed Phys Eng Express* 11(4), 2025 (PMID 40494367)** wskazują zgodnie te same predyktory skuteczności BCI: **amplituda międzyszczytowa flash-VEP**, **korelacja między epokami**, **moc pasma alfa** (oraz θ i δ).

| Krok | Czas | Co daje |
|---|---|---|
| alfa spoczynkowa: 2 min oczy zamknięte + 2 min otwarte | 4 min | stosunek mocy α |
| flash-VEP: ~200 pojedynczych błysków, uśrednienie | ~8 min | amplituda międzyszczytowa, korelacja między epokami |
| krótka próba SSVEP, 3 cele, 60 prób | ~5 min | odpowiedź bezpośrednia, przedział ±9 pp |

**Razem ~20 minut przy pierwszym uruchomieniu kupionej platformy, październik 2026.**

**Próg zapisany z góry:** jeżeli krótka próba SSVEP da poniżej **50%** przy trzech celach (poziom losowy 33,3%) **oraz** amplituda flash-VEP będzie w dolnym zakresie — uruchamiamy plan awaryjny R1, czyli przyspieszamy powołanie komisji IRB, żeby móc mierzyć na kimś innym.

`[luka]` Oba źródła dotyczą **c-VEP**, nie SSVEP. Wspólnota predyktorów jest `[wniosek]` — oba paradygmaty stoją na odpowiedzi kory wzrokowej na bodziec migający.

**Trzecie źródło o skali problemu:** *Streamlining cVEP Paradigms*, Brain Sciences 15(6):549, 2025, **38 badanych** — po redukcji liczby elektrod z 16 do 6 pipeline **przestaje działać u znacznej części osób**. `[wniosek]` W naszym reżimie (mało kanałów, mały moduł) odsetek osób nieskutecznych jest **wyższy** niż ogólne 10–30%. To jest główny argument za wykonaniem E0 przed czymkolwiek innym.

## 2. Eksperyment E1 — charakterystyka toru, bez człowieka

**Po co osobno:** dopóki tor nie jest zmierzony na stole, każdy wynik z głowy jest nierozstrzygalny. To jest też rubryka `Execution` arkusza inżynierskiego w czystej postaci.

| Wielkość | Metoda | Wartość odniesienia | Ile powtórzeń |
|---|---|---|---|
| szum wejściowy RMS | wejścia zwarte przez 10 kΩ, pasmo 0,5–45 Hz, 60 s | **0,08 µV RMS** (arXiv 2601.01772) | 10 zapisów, różne dni |
| CMRR | ten sam sygnał na oba wejścia, 50 Hz, amplituda 1 V | **>112 dB**; spadek o **26,9 dB** przy niedopasowaniu impedancji | 5, plus seria z celowym niedopasowaniem |
| **CMRR wobec niedopasowania impedancji** | rezystor szeregowy 0 / 5 / 10 / 20 / 50 kΩ na jednym wejściu | odtworzyć krzywą spadku | 5 na punkt |
| jitter próbkowania | sygnał prostokątny z generatora, odchylenie standardowe odstępów | 0,56 µs | 3 zapisy po 10 min |
| dryf | 8 h zapisu ze zwartym wejściem | < 1 ppm | 2 |
| pasmo i wzmocnienie | sygnał sinusoidalny 0,1–100 Hz, krok 1/3 oktawy | — | 3 przebiegi |

**Punkt krytyczny:** krzywa CMRR wobec niedopasowania impedancji jest **jedynym pomiarem E1, który wchodzi bezpośrednio do twierdzenia**. Elektrody suche na owłosionej potylicy mają różne impedancje, a to jest miejsce, w którym — wg pomiaru cudzego zespołu — układ się wywraca. Krzywa mówi, jaką tolerancję impedancji musi zapewnić konstrukcja elektrody.

> **POPRAWKA, 16 VIII 2026 — K-072.** Pierwotnie stało tu: *„E1 wymaga generatora i przyrządu o szumie własnym poniżej mierzonego"*. **To nieprawda dla najważniejszego pomiaru E1.** Szum wejściowy mierzy się **samym torem** — zwarte wejście, RMS z próbek własnego przetwornika 24-bitowego; oscyloskop hobbystyczny ma szum własny tysiąc razy większy od mierzonej wielkości i do tego zadania się nie nadaje. **Przyrząd zewnętrzny jest potrzebny jako ŹRÓDŁO znanego sygnału, nie jako miernik.**
>
> **Co z tego realnie trzeba kupić:** dzielnik precyzyjny do samodzielnego zlutowania (rezystory 0,1%, **30–80 zł — jedyne miejsce, gdzie dokładność jest krytyczna**) oraz generator funkcyjny ze średniej półki (250–600 zł; jego własny szum przy pomiarze CMRR jest sygnałem wspólnym i tłumi się razem z nim). Rozbiór: **`03_SPRZET.md` §4**.
>
> `[luka]` Bez pożyczonego sprzętu nie da się zmierzyć **jitteru próbkowania** ani potwierdzić CMRR powyżej ~100 dB. To jest właściwe zastosowanie zasobu „brat", luty 2027, na gotową płytkę v1. Do tego czasu obie liczby podajemy jako katalogowe, z jawnym zaznaczeniem.

---

## 3. Eksperyment E2 — główny: odległość odniesienia a przepustowość

### 3.1 Konstrukcja, i dlaczego taka

**Wszystkie warunki są rejestrowane jednocześnie, w jednej sesji, i wyprowadzane odejmowaniem po fakcie.**

Osiem elektrod (`03_SPRZET.md` §2.3) rejestruje się wobec wspólnego odniesienia na płatku ucha. Montaże o krótszym odniesieniu powstają offline jako różnice kanałów. **Jedna sesja daje pełny zestaw warunków na tych samych próbkach.**

Dlaczego to jest ważne, a nie kosmetyczne: sesje różnią się impedancją kontaktu, oświetleniem i stanem badanego. Gdyby każdy montaż mierzyć osobno, różnica między sesjami byłaby większa niż mierzony efekt i wynik byłby bezwartościowy. **To jest ta sama konstrukcja, która pozwoliła policzyć §5 pliku `14` na cudzych danych, i tam zadziałała.**

**Warunek kontrolny, którego nie wolno pominąć:** montaż zwarty musi zostać **na końcu zmierzony fizycznie**, na rzeczywistym module z odniesieniem wewnątrz, nie tylko wyprowadzony odejmowaniem. Wyprowadzenie offline zakłada, że tor jest liniowy i że nie ma nasycenia — a jednym z argumentów za kompensacją analogową jest właśnie to, że nasycenie istnieje. **Zgodność pomiaru fizycznego z wyprowadzeniem offline jest osobnym, raportowanym wynikiem.**

> **UZUPEŁNIENIE 18 VIII 2026 — P15a, `05_STAN_WIEDZY.md` §2.2.** Porównanie prowadzi się **wobec dwóch baz naraz, nie jednej**: (1) montaż wielokanałowy z odniesieniem odległym — górna granica; (2) **pojedynczy kanał z odniesieniem odległym — dolna granica**. Powód: `[fakt]` Li i in. 2025 (PMID 40566767) zmierzyli, że montaż dwubiegunowy POz−Oz **bije** pojedynczy kanał Oz z odniesieniem na czole (**68,25% wobec 37,65%** przy oknie 3 s), podczas gdy reanaliza Kołodzieja pokazuje, że dwubiegunowy **przegrywa** z montażem trzykanałowym z odniesieniem odległym (48,8–64,0% wobec 73,3%). **Obie liczby są prawdziwe i dotyczą różnych porównań.** Bez drugiej bazy własny wynik da się przedstawić jako sprzeczny z opublikowaną pracą, choć sprzeczny nie będzie. Koszt: zero — obie bazy wyprowadza się offline z tej samej rejestracji (`03_SPRZET.md` §2.1).

### 3.2 Zmienne

| | |
|---|---|
| **niezależna główna, DWUWYMIAROWA** | **odległość** odniesienia od Oz: **~2, ~3,5, ~7, ~10 cm** — **oraz KIERUNEK: w górę (POz) wobec w dół (podpotyliczny), przy zbliżonej odległości.** Zmienione 21 VIII 2026 (P27, `05_STAN_WIEDZY.md`). `[wniosek]` Para **POz** i **„2 cm poniżej Oz"** to warunek kontrolny w najczystszej postaci, jaką ten projekt ma: zbliżona odległość, przeciwny kierunek, ta sama sesja, te same próbki, ten sam tor — różnica jest **czystym efektem kierunku** |
| **niezależna druga** | długość okna decyzyjnego **t = 0,5 / 1 / 2 / 3 / 4 s** — wyprowadzana z tych samych zapisów |
| **niezależna trzecia** | liczba i rozstaw elektrod aktywnych: 1, 2, 3 kanały; rozstaw ~2 i ~4 cm (E3) |
| **zależne** | dokładność klasyfikacji, **ITR wg Wolpawa**, SNR w paśmie bodźca, impedancja kontaktu przed i po sesji |
| **kontrolowane** | oświetlenie pomieszczenia, odległość od panelu, pora dnia w oknie 2 h, ten sam preparat skóry |
| **rejestrowane, nieanalizowane pod T1** | temperatura, wilgotność, czas od założenia |

**Bodziec:** osiem celów. Częstotliwości **nie w paśmie 7–9 Hz** — tam leży rytm alfa, który zawyża poziom bazowy i mieszał się z artefaktami u Kołodzieja.

**Zestaw wybrany: 8,0 / 9,4 / 10,8 / 12,2 / 13,6 / 15,0 / 16,4 / 17,8 Hz**, krok 1,4 Hz. Weryfikacja rzeczywistej częstotliwości: **fotodioda w kanale pomocniczym**, każda sesja.

**Tabela kolizji harmonicznych — policzona, nie założona.** Kryterium: żadna z pierwszych trzech harmonicznych jednego celu nie może paść bliżej niż 0,3 Hz od którejkolwiek z pierwszych trzech harmonicznych innego celu.

| Zestaw | Kolizji | Min. odstęp podstawowych |
|---|---|---|
| **8,0…17,8 krok 1,4 Hz (wybrany)** | **0** | **1,400 Hz** |
| 8,1…15,8 krok 1,1 Hz | 0 | 1,100 Hz |
| 9,0…14,6 krok 0,8 Hz | 2 | 0,800 Hz |
| 8…15 krok 1,0 Hz (całkowite) | **4** | 1,000 Hz |
| 8,0…15,8 krok 1,114 Hz | 4 | 1,114 Hz |

**Wniosek:** częstotliwości całkowite ze stałym krokiem 1 Hz są najgorszym możliwym wyborem — 3×8 = 2×12 = 24 Hz i 3×10 = 2×15 = 30 Hz. **Krok 1,4 Hz od 8,0 Hz jest czysty.** Drugi rozstaw bez kolizji (krok 1,1 Hz) trzymam jako zapasowy, gdyby górne 17,8 Hz okazało się dla oczu męczące.

### 3.3 Ile prób — policzone, nie oszacowane

**Test:** McNemar dla par (ta sama próba, dwa montaże).

| Efekt do wykrycia | Odsetek par niezgodnych | **Liczba prób** |
|---|---|---|
| 9 pp (przewidywanie z `14`) | 14% | **134** |
| 9 pp | 19% | 182 |
| 9 pp | 29% | 279 |
| 5 pp (ostrożnie) | 10% | 312 |
| 5 pp | 15% | 469 |

α = 0,05 dwustronnie, moc 80%.

**Przyjmuję 240 prób na sesję.** Pokrywa efekt 9 pp z zapasem przy każdym realistycznym odsetku niezgodności i połowicznie pokrywa 5 pp.

**Długość okna decyzyjnego — wybrana pomiarem, nie odczuciem.** Na danych Kołodzieja policzyłem dokładność i ITR dla okien 0,5–5 s (`12_REANALIZA.md` §5.1). **ITR ma wyraźne maksimum przy oknie 1 s** (28,9 bit/min przy trzech celach) i spada dla okien dłuższych, mimo że dokładność dalej rośnie. Dodatkowo: **strata montażu zwartego maleje z długością okna** (9,3 pp przy 1 s → 4,2 pp przy 5 s), więc długość okna jest **zmienną, która wchodzi w interakcję z badanym efektem** i musi być analizowana, a nie ustalona raz.

**Decyzja:** rejestrujemy epoki **2 s**, a okna 0,5 / 1 / 1,5 / 2 s wyprowadzamy z nich offline. Główna liczba raportowana przy oknie, które maksymalizuje ITR — **z podaniem całej krzywej**, nie samego maksimum.

**Struktura sesji:**
- 8 celów × 30 powtórzeń = **240 prób**
- próba: 2 s stymulacji + 1,5 s przerwy z sygnałem docelowym = 3,5 s
- 240 × 3,5 s = **14 min czystego czasu**, plus przerwa 2 min co 60 prób → **~22 min sesji**
- kolejność celów **losowa, zrównoważona** (każdy cel tyle samo razy w każdej ćwiartce sesji)

**Liczba sesji: 8, w ośmiu różnych dniach.** Po co osiem, skoro 240 prób wystarcza statystycznie: bo **zmienność między dniami jest osobnym wynikiem**, a nie szumem do uśrednienia. Osiem dni daje przedział na tę zmienność i zasila twierdzenie T2.

**Razem:** 8 sesji × 240 prób = **1920 prób na każdy montaż**, wszystkie z tych samych zapisów.

### 3.4 Niepewność — jak podawana

`[fakt, wzór]` ITR Wolpaw: `B = log₂N + P·log₂P + (1−P)·log₂((1−P)/(N−1))`, ITR = B · 60/t.

**Konwencja `t`, deklarowana raz i niezmienna** (zakaz z `archiwum/06_TABELA_PARAMETROW.md` §0 pkt 2): `t` = **czas stymulacji plus przerwa**, czyli 3,5 s przy oknie 2 s. Podawane będą obie liczby: ITR „przy oknie" i ITR „przy pełnym cyklu". **Nigdy jedna bez drugiej.**

Niepewność dokładności: przedział Wilsona. Niepewność ITR: **propagacja przez wzór z krańców przedziału P**, plus bootstrap 10 000 losowań po próbach.

Skala niepewności przy N = 8, t = 2 s, P = 0,85:

| Liczba prób | Przedział P | **ITR i jego przedział** |
|---|---|---|
| 60 | ±9,0 pp | 59,1 [45,9; 75,2] bit/min |
| 120 | ±6,4 pp | 59,1 [49,5; 70,0] |
| **240** | **±4,5 pp** | **59,1 [52,2; 66,6]** |
| 1920 (osiem sesji) | ±1,6 pp | 59,1 [56,7; 61,6] |

**Wniosek do zapisania na plakacie:** przy 60 próbach przedział ITR ma szerokość 29 bit/min. **Każda liczba ITR podana bez liczby prób jest bez znaczenia** — łącznie z liczbami w cudzych pracach, których nie audytujemy, ale wobec których nie zamierzamy być gorsi.

### 3.5 Zakres oczekiwanych wartości — żeby nie zawyżać oczekiwań

`[fakt, przeliczone wzorem Wolpawa]`

| N celów | t | P = 0,70 | P = 0,85 | P = 0,95 |
|---|---|---|---|---|
| 3 | 1 s | 24,2 | 49,5 | 74,9 |
| **8** | **2 s** | **38,3** | **59,1** | **77,2** |
| 8 | 1 s | 76,6 | 118,1 | 154,4 |
| 12 | 1 s | 100,0 | 147,4 | 187,5 |

Kalibracja oczekiwań z `METODA.md` §3: **dolna półka w recenzowanej literaturze to 70% przy trzech celach** (Kołodziej, zespół uczelniany). **Nie zakładaj, że pierwsze uruchomienie da górną półkę.** Pierwsza własna sesja, która da 60% przy ośmiu celach, jest sukcesem, nie porażką.

---

## 4. Eksperyment E3 — rozstaw elektrod aktywnych

Druga mierzona kontrybucja z `archiwum/13_PODNIESIENIE_SZANS.md` §5, **zmieniona po reanalizie**: pytanie „czy gęste próbkowanie małego obszaru zastępuje rzadkie próbkowanie dużego" dostało już częściową odpowiedź na cudzych danych i brzmi ona **nie** (`12_REANALIZA.md` §5).

**Co zostaje do zmierzenia:** czy strata jest funkcją **rozstawu elektrod aktywnych**, czy wyłącznie **odległości odniesienia**. Reanaliza tych dwóch nie rozdziela, bo w tamtym zbiorze były tylko trzy elektrody potyliczne.

- rozstaw elektrod aktywnych: ~2 cm i ~4 cm, przy **stałym** odniesieniu na płatku ucha
- jeżeli strata zależy głównie od odniesienia, a nie od rozstawu aktywnych — **moduł zwarty jest uratowany, pod warunkiem wyprowadzenia samego odniesienia**, i to jest konkretny, projektowy wynik
- koszt: zero dodatkowego sprzętu, wiązki i tak są wymienne

---

## 5. Eksperyment E4 — kompensacja EMG karku, warunkowa i z przewidywaniem negatywnym

**Uruchamiany tylko wtedy, gdy E2 pokaże, że użyteczne odniesienie leży nad mięśniem karku** (~4 cm poniżej Oz). Wtedy — i tylko wtedy — elektroda odniesienia sama wnosi EMG do każdego kanału, i kompensacja ma zmierzony sens.

| Warunek | Co porównywane |
|---|---|
| A | odniesienie nad karkiem, bez kompensacji |
| B | odniesienie nad karkiem, kompensacja cyfrowa z kanału 7 (regresja, metoda Kołodzieja) |
| B2 | jw., ale regresor obwiedniowy zamiast liniowego — sprawdzony na cudzych danych i **tam nie pomagał** |
| C | odniesienie nad karkiem, **kompensacja analogowa przed wzmocnieniem** |
| D | odniesienie na płatku ucha, bez kompensacji — górna granica |

**Zadanie z wywołanym artefaktem** wzorowane na protokole Kołodzieja: epizody 1–2 s napięcia mięśni karku, w losowych momentach stymulacji. **Plus warunek bez wywoływania artefaktu**, którego u Kołodzieja nie było i którego brak jest ograniczeniem tamtej pracy.

**Analiza obowiązkowo warunkowana poziomem artefaktu, nie uśredniana po całości.** To jest lekcja z §6A pliku `14`: uśrednienie po wszystkich oknach rozcieńcza efekt epizodyczny i może pokazać zero tam, gdzie zera nie ma. Dokładność i SNR raportowane **w kwintylach mocy EMG w oknie**, tak jak tam.

**Próg decyzyjny zapisany z góry:** jeżeli B − A < 3 pp **w górnym kwintylu skażenia**, kompensacja **nie wchodzi do projektu jako kontrybucja** i zostaje opisana jako zmierzony wynik negatywny. Wynik negatywny z liczbą jest raportowalny i punktowany w rubryce `Execution`; wynik negatywny przemilczany jest naruszeniem standardów etycznych Explory.

---

## 6. Eksperyment E5 — metryki użytkowe (wariant 2 z decyzji C2)

Schodzi do tabeli towarzyszącej, ale **jest mierzony**, bo kosztuje tylko dyscyplinę zapisu.

| Wielkość | Metoda | Uwaga formalna |
|---|---|---|
| czas montażu | stoper, od wyjęcia z pudełka do pierwszej poprawnej klasyfikacji | zwolnione |
| dryf SNR w ciągu dnia noszenia | pomiar co 60 min, 6 h | **zwolnione** |
| dryf impedancji kontaktu | wbudowany obwód ADS1299, co 60 min | zwolnione |
| odsetek sesji bez rekalibracji | model z sesji 1 stosowany do sesji 2…8 | zwolnione |
| **wpływ wyspania i zmęczenia** | — | **NIE ROBIMY.** Zmienna ludzka, łamie zwolnienie ISEF dla badania na sobie |

**Granica jest cienka i trzymamy ją świadomie teraz, a nie odkrywamy w marcu 2028.**

---

## 7. Badani, zgody, terminy

| Faza | Kto | Podstawa formalna |
|---|---|---|
| do V 2027 (prace rozwojowe) | **wyłącznie autor** | zwolnienie dla badania na sobie |
| V 2027 – IV 2028 (kampania ISEF) | autor; grupa **dopiero po powołaniu komisji IRB przy szkole** | K-022 |
| grupa | docelowo 10–15 osób, świadome zgody, przy niepełnoletnich zgody opiekunów | Form 4 i pokrewne |

`[fakt]` **Kampania formalna pod ISEF startuje w maju 2027** — okno 12 miesięcy to styczeń 2027 – maj 2028 (K-023, potwierdzone na trzech rocznikach w K-046). Wszystko wcześniejsze liczy się bez ograniczeń na Explory i El-Robo-Mech.

**Wielkość próby dla grupy:** przy σ ≈ 8 pp między osobami (z danych Kołodzieja) i efekcie 9 pp, próba sparowana wewnątrzosobniczo wymaga `[wniosek]` **rzędu 8–10 osób** dla mocy 80%. **Piętnaście osób daje zapas na odrzucone zapisy.** To jest liczba osiągalna w szkole i nie jest wąskim gardłem — wąskim gardłem jest powołanie komisji.

---

## 8. Zarządzanie danymi i uczciwość analizy

1. **Surowe zapisy nie są nigdy nadpisywane.** Każda sesja: plik surowy, plik metadanych (impedancje, oświetlenie, godzina, wersja sprzętu i oprogramowania), zapis fotodiody
2. **Kod analizy w repozytorium, wersjonowany.** Pipeline z `analiza/` jest zalążkiem i jest już zwalidowany wobec publikacji
3. **Dobór hiperparametrów klasyfikatora wyłącznie na sesjach 1–2**, potem zamrożony. Sesje 3–8 to zbiór testowy i nie wolno go dotknąć przed zamrożeniem
4. **Wszystkie warunki raportowane**, także te, które wypadły źle. Lista warunków jest w tym pliku i jest datowana
5. **Dziennik postępu budowy z wersjonowanymi zdjęciami** — `METODA.md` §4.13 wskazuje to jako normę dokumentacyjną silnych wpisów inżynierskich w Explory, i jest to tańsze niż tabele pomiarowe na plakacie

---

## 9. Czego ten plan nie obejmuje — zgłaszam jawnie

`[luka]`

1. **Sprzęt pomiarowy do E1 nieustalony** — bez niego charakterystyka toru będzie niepełna (R3)
2. **Nie ma planu na wypadek, gdyby SSVEP u autora był słaby.** Rozrzut międzyosobniczy w danych Kołodzieja to 40–96% dokładności bazowej; **S08 miał 40%**. Jeżeli autor okaże się takim przypadkiem, cały plan jednoosobowy się sypie. **Pierwszy pomiar w torze A, jesienią 2026, jest testem tego ryzyka i musi być wykonany zanim powstanie płytka** — wpisane jako R1
3. **TRCA i metody z uczeniem wewnątrzosobniczym nieprzetestowane** — mogą zmienić obraz z `14`
4. **Crossref i arXiv nieprzeszukane dla nowej osi** — tylko PubMed (`12_REANALIZA.md` §11)
5. **Nie ma pomiaru widoczności urządzenia.** Test na stoisku „gdzie ono jest" jest **ankietą opinii publicznej o wynalazku i wymaga uprzedniej zgody komisji IRB** (`11_EWOLUCJA.md` decyzja 3). Albo procedura zgody, albo pomysł odpada — nie wolno tego zrobić spontanicznie
