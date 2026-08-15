# 02 — Jak to właściwie działa

**Zakres wg sekcji 10.B handbooka.** Mechanizm fizyczny każdej klasy rozwiązań. Każdy termin użyty pierwszy raz dostaje wyjaśnienie. Zakładam fizykę i matematykę szkolną, zero terminologii neurofizjologicznej.

> **Status źródłowy, 15 VIII 2026 wieczorem:** to jest **jedyny plik treściowy, którego nie weryfikowałem źródłowo w sesji drugiej.** Powód: zawiera głównie wyjaśnienia mechanizmów fizycznych (przewodnictwo objętościowe, dipol prądowy, impedancja kontaktu), które są wiedzą podręcznikową, a nie liczbami, na których coś stoi. Ryzyko błędu jest przez to niższe, ale **nie zerowe** — liczby w sekcji 3.1 nadal mają znacznik `[wniosek, streszczenie]` i to nie jest ozdobnik.
>
> Jedna poprawka merytoryczna została naniesiona niżej, w sekcji 3.1 — dotyczy tego, które zakłócenie faktycznie przeszkadza przy uchu.

---

## 1. Skąd w ogóle bierze się napięcie na głowie

**Neuron** to komórka nerwowa. W spoczynku utrzymuje różnicę potencjałów między wnętrzem a zewnętrzem błony komórkowej, rzędu −70 mV — jak mała naładowana bateria. Utrzymuje ją, wypompowując jony (naładowane atomy, głównie sodu Na⁺ i potasu K⁺) na zewnątrz i do środka.

Kiedy neuron dostaje sygnał od sąsiadów, w błonie otwierają się kanały jonowe i jony **płyną** przez błonę. Płynące jony to prąd elektryczny. Prąd płynący przez ośrodek o niezerowej oporności wytwarza wokół siebie rozkład potencjału — dokładnie tak, jak w zadaniu ze szkolnej elektrostatyki.

**Kluczowy szczegół, bez którego reszta nie ma sensu.** Pojedynczy neuron daje na skórze głowy sygnał **nieodróżnialny od zera**. To, co mierzy EEG, powstaje przez zsumowanie wkładów od dziesiątek tysięcy do milionów neuronów naraz. Żeby suma nie znikła, muszą być spełnione dwa warunki:

1. **Neurony muszą być ustawione równolegle.** Neurony piramidowe w korze mózgowej stoją prostopadle do jej powierzchni jak drzewa w lesie — ich pola się dodają. Gdyby były ustawione losowo, sumowałyby się do zera.
2. **Muszą działać jednocześnie.** Aktywność zsynchronizowana daje sygnał. Ta sama liczba neuronów pracujących niezależnie daje szum.

**Dipol** — układ dwóch przeciwnych ładunków blisko siebie. Aktywny fragment kory zachowuje się jak dipol prądowy: prąd wpływa w jednym miejscu drzewka neuronu, wypływa w drugim.

**Wniosek, do którego będziemy wracać:** EEG mierzy **zsynchronizowaną aktywność dużych, równolegle ustawionych populacji neuronów**. Nie mierzy „myśli". Nie mierzy pojedynczych komórek. To ograniczenie fizyczne, nie techniczne.

---

## 2. Co się dzieje po drodze z kory do elektrody — przewodnictwo objętościowe

**Przewodnictwo objętościowe (volume conduction)** — rozpływanie się prądu przez wszystkie tkanki między źródłem a elektrodą: płyn mózgowo-rdzeniowy, oponę twardą, **czaszkę**, skórę.

Czaszka to najważniejszy element tego łańcucha, bo ma **przewodność elektryczną o rząd wielkości mniejszą** niż tkanki wokół niej. Kość jest tu warstwą izolującą.

Skutki, obydwa istotne:

**a) Tłumienie amplitudy.** Sygnał na skalpie jest wielokrotnie mniejszy niż nad samą korą. Porównania jednoczesnych rejestracji inwazyjnych i nieinwazyjnych podają, że jakość sygnału inwazyjnego jest **20 do ponad 100 razy lepsza** `[wniosek, streszczenie, jedno źródło]`.

**b) Rozmycie przestrzenne** — i to jest efekt gorszy od tłumienia. Kość o niskiej przewodności działa jak **filtr dolnoprzepustowy w przestrzeni**: rozmazuje potencjał, zanim ten dotrze do skóry. Praktyczna rozdzielczość przestrzenna EEG skalpowego to **około 5–9 cm** `[wniosek, streszczenie]`.

Analogia, która oddaje sedno: EEG to nasłuchiwanie tłumu przez ścianę. Słychać, kiedy tłum krzyczy zgodnie. Nie da się wyłowić pojedynczej rozmowy, bo ściana zmieszała wszystko, zanim dźwięk dotarł do ucha. **Lepszy mikrofon tego nie naprawi — problem jest w ścianie.**

Dodatkowo rozmycie działa silniej na wysokie częstotliwości: składowe o różnych fazach nakładają się i częściowo wygaszają. Dlatego z EEG dobrze widać rytmy poniżej ~30 Hz, a powyżej robi się trudno.

---

## 3. Klasy rozwiązań i mechanizm każdej z nich

### 3.1 EEG — elektrody na skórze głowy

Mierzy się **różnicę potencjałów między dwiema elektrodami** (bo napięcie zawsze jest różnicą — nie ma czegoś takiego jak potencjał bezwzględny elektrody). Jedna z nich to zwykle **referencja** — punkt odniesienia wspólny dla wszystkich kanałów, często płatek ucha lub wyrostek sutkowaty (kostny guzek za uchem).

Amplitudy, do zapamiętania, bo cały projekt się wokół nich kręci `[wniosek, dwa źródła zgodne co do rzędu]`:

| Sygnał | Typowa amplituda | Stosunek do EEG |
|---|---|---|
| **EEG** | 10–100 µV (skrajnie 15–150 µV) | ×1 |
| **EOG**, ruch gałki ocznej | do 30–40 **mV** u źródła; na skórze głowy setki µV | ×10–100 |
| **EMG**, mięsień | 50 µV – 30 **mV** | ×10–1000 |

**To jest fizyczne jądro problemu projektu.** Sygnał użyteczny jest 10–100 razy mniejszy niż zakłócenia, które siedzą tuż obok, a przy uchu — bezpośrednio pod elektrodą.

> **POPRAWKA, 15 VIII 2026 — `KOREKTY.md` K-026. Amplituda u źródła nie przekłada się wprost na to, co przeszkadza przy uchu.**
>
> Powyższa tabela mówi o amplitudach **u źródła**. Ale to, ile zakłócenie psuje pomiar, zależy jeszcze od tego, **jak daleko od elektrody leży jego źródło i jak zorientowany jest jego dipol**. Kappel i in. (2017, 9 badanych, abstrakt odczytany) zmierzyli to bezpośrednio dla elektrod usznych:
>
> | Zakłócenie | Wpływ na SNR w uchu | Wpływ na SNR na skalpie |
> |---|---|---|
> | **zaciśnięcie szczęki (EMG)** | **duży, największy w paśmie gamma** | mniejszy niż w uchu |
> | **mrugnięcie (EOG)** | **żaden** | istotny, w pasmach delta i theta |
> | ruch gałek ocznych (EOG) | istotny | istotny |
>
> Czyli: **mimo że mrugnięcie ma ogromną amplitudę u źródła, przy uchu nie przeszkadza.** Gałka oczna jest za daleko, a jej dipol źle zorientowany względem pary elektrod usznych. Mięsień skroniowy i żwacz leżą natomiast tuż pod elektrodą.
>
> **To jest dobra ilustracja tego, po co w ogóle jest ten plik:** z samej tabeli amplitud wyszedł błędny wniosek, że trzeba kompensować oba zakłócenia. Mechanizm — odległość i orientacja dipola — mówi co innego i został potwierdzony pomiarem.

**Elektroda mokra vs sucha.** Mokra używa żelu przewodzącego wypełniającego nierówności naskórka. Sucha dotyka skóry bezpośrednio: wygodniejsza, ale ma **znacznie większą impedancję kontaktu** (opór zespolony na styku elektroda–skóra). Zmierzone dla elektrod w kanale słuchowym przy ~50 Hz `[wniosek, streszczenie, jedno źródło]`:

| Typ | Impedancja |
|---|---|
| mokra srebrna | **4 kΩ** (odch. 3 kΩ) |
| sucha srebrna | **452 kΩ** (odch. 737 kΩ) |
| sucha z tlenku irydu (IrO₂) | **435 kΩ** (odch. 515 kΩ) |

Różnica **stukrotna**, a odchylenie standardowe większe od średniej — czyli między osobami i między założeniami urządzenia rozrzut jest ogromny. Dlaczego to boli: wysoka impedancja źródła plus prąd polaryzacji wejścia wzmacniacza daje dodatkowy szum, a niedopasowanie impedancji między elektrodą sygnałową a referencyjną **psuje tłumienie sygnału wspólnego** (patrz 3.2).

### 3.2 Tor analogowy — dlaczego to jest osobna dziedzina

**Wzmacniacz różnicowy** wzmacnia różnicę napięć między dwoma wejściami, a to, co na obu wejściach jednakowe, powinien wyciąć. To „jednakowe" to głównie **50 Hz z sieci elektrycznej**, które na ciele człowieka indukuje się z amplitudą o rzędy wielkości większą niż EEG.

**CMRR (common-mode rejection ratio)** — miara, jak dobrze wzmacniacz tłumi to, co wspólne. Podawana w decybelach. Dobre układy EEG: **>115 dB przy 50/60 Hz**, klasyczny układ ze sprzężeniem „prawej nogi" (RLD) daje 80–100 dB `[wniosek, streszczenie]`.

**Szum własny wzmacniacza sprowadzony na wejście** — gdyby wzmacniacz miał wejścia zwarte, na wyjściu i tak coś widać; dzieli się to przez wzmocnienie i dostaje liczbę porównywalną z amplitudą sygnału. Punkt odniesienia branżowy: układ **ADS1299** Texas Instruments, 8 kanałów, 24 bity, szum wejściowy **1,0 µV międzyszczytowo w paśmie 70 Hz**, CMRR −120 dB `[fakt — parametr katalogowy, potwierdzony w trzech niezależnych opisach]`. Ten sam układ siedzi w OpenBCI Cyton.

Porównanie: EEG ma 10–100 µV, szum toru ~1 µV. **Zapas jest jedno- do dwucyfrowy, nie tysiąckrotny.** Stąd waga tego, żeby nie zmarnować go na zakłócenia.

**Zakres dynamiczny i nasycenie** — i to jest punkt, na którym stoi kandydat na oś projektu. Wzmacniacz ma skończony zakres napięć wejściowych. Jeżeli wzmocnimy 30 razy sygnał zawierający EEG (50 µV) i EMG szczęki (5 mV), to na wyjściu EMG zajmie cały zakres i **EEG zostanie zgubione, zanim dotrze do przetwornika**. Odjęcie zakłócenia programowo **po** nagraniu już go nie odzyska: informacja przepadła przy nasyceniu. Odjęcie **przed** wzmocnieniem — odzyskuje. To jest realna, fizyczna różnica między kompensacją analogową a cyfrową, nie kosmetyka.

Literatura potwierdza wagę tego wprost: filtrowanie zakłóceń przed pierwszym stopniem wzmocnienia jest konieczne, żeby chronić wzmacniacz przed nasyceniem artefaktami mięśniowymi `[wniosek, streszczenie]`.

### 3.3 Forma douszna i zauszna

Trzy warianty geometryczne:
- **in-ear** — elektrody na wkładce w kanale słuchowym
- **around-ear / cEEGrid** — elastyczna folia z elektrodami wokół małżowiny
- **behind-ear** — element za małżowiną, wielkości aparatu słuchowego (**to jest forma docelowa użytkownika**)

Mechanizm jest ten sam co w EEG skalpowym. Zmienia się **geometria**, i to zmienia wszystko:

1. **Odległość do źródła.** Kora słuchowa leży w płacie skroniowym, kilka centymetrów od kanału słuchowego — blisko. Kora ruchowa leży na szczycie głowy — daleko. Kora wzrokowa z tyłu — daleko.
2. **Rozstaw elektrod.** Elektrody oddalone o 2 cm rejestrują mniejszą różnicę potencjałów niż oddalone o 15 cm, bo bliskie punkty na skalpie mają podobny potencjał. Mniejszy rozstaw = mniejszy sygnał przy tym samym szumie toru.
3. **Sąsiedztwo mięśni.** Mięsień skroniowy przebiega dokładnie tam, gdzie siadają elektrody uszne. Kappel i in. 2017 zmierzyli, że pogorszenie SNR od artefaktów szczękowych jest **w uchu większe niż na skalpie** `[wniosek, streszczenie]`.
4. **Liczba kanałów.** Ograniczona geometrią. Większość metod filtracji przestrzennej poprawia się z liczbą kanałów — mniej kanałów to słabsze narzędzia w warstwie dekodowania.

### 3.4 ECoG i mikroelektrody wewnątrzkorowe

**ECoG** — elektrody położone na powierzchni kory, pod czaszką. Czaszka wypada z toru, więc znika i tłumienie, i rozmycie: amplitudy wielokrotnie większe, rozdzielczość przestrzenna milimetrowa zamiast centymetrowej.

**Mikroelektrody wewnątrzkorowe** (Utah array) — igły wbite na ~1,5 mm w korę, rejestrujące potencjały czynnościowe **pojedynczych neuronów**. Najwyższa jakość informacji, jaka jest osiągalna. Cena: kraniotomia, ryzyko infekcji i degradacja sygnału w czasie (tkanka glejowa otacza elektrodę).

**Stentrode** (Synchron) — elektroda wprowadzana przez żyłę, jak stent kardiologiczny, i rozpierana w naczyniu biegnącym nad korą ruchową. Kompromis: brak kraniotomii, sygnał gorszy niż ECoG, lepszy niż EEG.

### 3.5 Modalności niepotencjałowe

| Metoda | Wielkość mierzona | Fizyka | Ograniczenie |
|---|---|---|---|
| **MEG** | pole magnetyczne prądów neuronalnych | pole rzędu femtotesli — miliardy razy słabsze od ziemskiego | wymaga ekranowania magnetycznego. OPM-MEG zdjęło ciekły hel, nie zdjęło ekranowania |
| **fNIRS** | pochłanianie światła bliskiej podczerwieni przez hemoglobinę | mierzy **przepływ krwi**, nie aktywność elektryczną | odpowiedź hemodynamiczna opóźniona o **sekundy**. Fizyczne, nie do obejścia |
| **fUS** | doppler przepływu krwi | rozdzielczość ~100 µm | czaszka odbija ultradźwięki; wymaga okna kostnego |
| **sEMG** | napięcie z mięśni | ten sam mechanizm co EEG, ale źródłem jest mięsień | **to nie jest sygnał z mózgu** |

### 3.6 Eye tracking — punkt odniesienia, o który zapyta juror

Kamera + oświetlacz podczerwony, śledzenie odbicia rogówkowego i źrenicy. Dokładność ułamka stopnia, opóźnienie milisekundy, cena od kilkuset złotych.

**Każdy projekt sterowania interfejsem neuralnym musi mieć gotową odpowiedź na pytanie „dlaczego nie kamerka".** Odpowiedzi, które się bronią: działa przy zamkniętych oczach, działa u osób bez kontroli ruchów gałek, nie wymaga linii widzenia, działa w ciemności i pod powieką. Odpowiedź, która się nie broni: „bo interfejs neuralny brzmi lepiej".

---

## 4. Paradygmaty — jak z sygnału robi się komenda

Fizyka mówi, co da się zmierzyć. **Paradygmat** mówi, co użytkownik ma zrobić, żeby dało się to odróżnić od tła. Pełne omówienie w `07_DEKODOWANIE.md`; tutaj sam mechanizm.

| Paradygmat | Co robi użytkownik | Co widać w sygnale | Gdzie na głowie |
|---|---|---|---|
| **SSVEP** | patrzy na migający obiekt (np. 10 Hz) | kora wzrokowa zaczyna „grać" tą samą częstotliwością i jej wielokrotnościami | potylica |
| **P300** | czeka na rzadki, istotny bodziec wśród częstych | dodatni garb ~300 ms po bodźcu | ciemieniowo |
| **wyobrażenie ruchu** | wyobraża sobie ruch ręką, nie ruszając nią | spadek mocy rytmu ~8–13 Hz nad przeciwną półkulą (ERD) | kora ruchowa, czyli szczyt głowy |
| **uwaga słuchowa / ASSR** | skupia się na jednym z dwóch dźwięków | wzmocnienie odpowiedzi na dźwięk wybrany | skroń, **blisko ucha** |
| **wyobrażona mowa** | wyobraża sobie wypowiadanie słowa | słabo określone wzorce; nieinwazyjnie bardzo trudne | — |

**ERD (event-related desynchronization)** — spadek mocy rytmu, kiedy dana okolica kory zaczyna pracować. Brzmi odwrotnie do intuicji: pracująca kora daje **mniej** rytmu, bo neurony przestają działać zgodnie i zaczynają niezależnie. Wraca punkt z sekcji 1: EEG widzi synchronizację, więc rozsynchronizowanie widzi jako ciszę.

---

## 5. Podsumowanie — trzy zdania, z których wynika reszta projektu

1. **EEG mierzy zsumowaną, zsynchronizowaną aktywność dużych populacji neuronów, przefiltrowaną przestrzennie przez czaszkę.** Rozdzielczość ~5–9 cm jest ograniczeniem fizycznym.
2. **Sygnał użyteczny (10–100 µV) jest 10–100 razy mniejszy niż zakłócenia mięśniowe i oczne**, które przy uchu leżą bezpośrednio pod elektrodą — i tam są większym problemem niż na skalpie.
3. **Miejsce elektrody decyduje, jakie sygnały są dostępne.** Przy uchu blisko jest kora słuchowa; kora ruchowa i wzrokowa są daleko. Tego nie zmienia żaden wzmacniacz ani algorytm — to jest geometria.
