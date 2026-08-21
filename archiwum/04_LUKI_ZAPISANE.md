# 04 — Luki zapisane w literaturze

**Zakres wg sekcji 10.D handbooka.** Sekcje „limitations", „future work", „open challenges" ze świeżych prac. Z namiarem, treścią i moją oceną, czy leży to w zasięgu warsztatu z sekcji 1 handbooka.

**To jest właściwa metoda szukania luki** — luki są opisane, nie trzeba ich zgadywać.

**Status źródłowy, 15 VIII 2026 wieczorem.** Poprzednia wersja tego pliku nie miała otwartej ani jednej pracy i mówiła to wprost. Ta wersja została zbudowana na **abstraktach odczytanych z PubMed** (dostęp przez E-utilities NCBI) plus przeglądzie systematycznym opisanym w sekcji 2. Przy każdej pozycji zaznaczam, czy odczytałem abstrakt, czy tylko namiar. **Pełnych tekstów za paywallem nadal nie mam** — to dotyczy IEEE i części Elsevier — i tam, gdzie to ma znaczenie, mówię o tym przy twierdzeniu.

---

## 1. Luki wskazane w przeglądach ear-EEG 2025–2026

### 1.1 Przegląd: MDPI *Sensors* 25(11):3321, 2025, PMID 40968884
*„The Next Frontier in Brain Monitoring: A Comprehensive Look at In-Ear EEG Electrodes and Their Applications"*. `[fakt]` Pozycja istnieje, indeksowana w PubMed, data 25 V 2025.

Problemy otwarte wymienione przez autorów `[wniosek, streszczenie — pełnego tekstu nie otwierałem]`:

| Problem | W zasięgu warsztatu? | Uwaga |
|---|---|---|
| **zmienność anatomiczna kanału słuchowego** | **tak** | druk 3D pod indywidualny odlew. Warstwa 2 z sekcji 9.4 handbooka |
| **optymalizacja ergonomii** | **tak** | mechanika i modelowanie — najmocniejsza strona użytkownika |
| **redukcja artefaktów ruchowych** | **tak, częściowo** | mechanika mocowania + tor analogowy |
| dobór materiałów | tak | patrz `05_RYNEK.md` sekcja 5 — **luka zamknięta**, K-035 |
| jakość biosygnału | tak | to jest oś kandydująca |
| usuwanie artefaktów | **tak — to jest nasz punkt** | patrz sekcja 2 poniżej |
| elektronika ultraniskiej mocy | **raczej nie** | to jest teren projektowania układów scalonych |

**Ocena `[wniosek]`:** trzy pierwsze pozycje leżą w przecięciu „opisane jako otwarte" i „mechanika plus elektronika". **Ta ocena zyskała mocne wsparcie z nieoczekiwanej strony** — patrz sekcja 1.5 o pracy SpiralE, gdzie właśnie jakość kontaktu mechanicznego okazała się czynnikiem przełomowym.

### 1.2 Frontiers in Neuroscience 20:1859327, 2026, PMID 42592227 — **ABSTRAKT ODCZYTANY**
*„Signal-specific performance of in-ear EEG: strengths and limitations"*, Frei, Mainar, Fritz, Chardon, Giroud.

**[fakt] Metoda, dokładnie:** **19 zdrowych dorosłych**, w pełni douszny system o generycznym dopasowaniu, z elektrodami suchymi, porównywany **równolegle** z 32-kanałowym skalpowym BioSemi. Trzy klasy sygnału: alfa spoczynkowa (oczy otwarte/zamknięte), słuchowe potencjały wywołane (kompleks N1-P2), oraz ERSP alfa podczas słuchania mowy w szumie.

**[fakt] Wyniki, wiernie:**
- alfa spoczynkowa przy zamkniętych oczach — **wychodzi pewnie**, mimo obniżonej amplitudy bezwzględnej
- N1-P2 — **wiarygodne tylko przy uśrednionej referencji skalpowej**; w konfiguracji dousznej i w konfiguracjach adaptowanych spada wykrywalność komponentu i jego SNR
- alfa podczas mowy w szumie — istotne odchylenia w EEG skalpowym w warunkach mniej trudnych, **w minimalnej konfiguracji dousznej nie wykrywane konsekwentnie**

Konkluzja autorów: wykrywalność zależy silnie od **klasy sygnału, wielkości efektu i geometrii rejestracji**, stąd potrzeba „configuration-aware guidance".

**[fakt] Konflikt interesów, który trzeba znać:** praca finansowana przez **Logitech S.A.**, dwóch współautorów było wówczas pracownikami Logitecha, a firma dostarczyła badany system douszny i uczestniczyła w projektowaniu badania. **To czyni wyniki negatywne bardziej wiarygodnymi, nie mniej** — producent nie ma interesu w publikowaniu, że jego urządzenie czegoś nie wykrywa.

**Ocena `[wniosek]`:** to jest luka **metodologiczna, nie sprzętowa**, a więc tania. Starannie zaprojektowane porównanie kilku konfiguracji referencji na jednym urządzeniu, z niepewnościami, jest robotą wymagającą **dyscypliny pomiarowej zamiast budżetu**. Dla projektu ma wartość podwójną: jest realnym wkładem i dostarcza tabeli, której wymaga sekcja Execution arkusza inżynierskiego ISEF („tested in multiple conditions/trials").

### 1.3 Frontiers in Human Neuroscience, art. 1793705, 2026, PMID 42088716
*„In-ear EEG wearables for brain activity assessment and cognitive rehabilitation: the emerging role of multimodal embedded intelligence"*. `[fakt]` Pozycja istnieje.

Wyzwania wymienione `[wniosek, streszczenie]`: umiejscowienie elektrod, **sprzężenie mechaniczno-elektryczne**, odporność na ruch, efektywność energetyczna, długotrwała noszalność.

„Sprzężenie mechaniczno-elektryczne" to zależność jakości sygnału od tego, jak elektroda przylega do skóry i jak to się zmienia przy ruchu. **W zasięgu, i jest to problem mechaniczny udający problem elektroniczny** — czyli dokładnie ten typ, w którym użytkownik ma przewagę nad konkurencją algorytmiczną.

### 1.4 Pozycje z tej samej linii, dołożone po przeszukaniu PubMed

Wszystkie `[fakt]` co do istnienia, abstrakty odczytane:

- **PMID 41114004**, *„Hearables: Bioelectronics technological challenges and opportunities"*, *Wearable Technologies* 2025 — przegląd wprost o wyzwaniach technologicznych klasy urządzeń, w którą wchodzi projekt. **Pozycja do przeczytania w całości w etapie 2.**
- **PMID 41631479**, *„Wireless in-ear EEG system for auditory brain-computer interface applications in adolescents"*, *Biomed Phys Eng Express*, 3 II 2026 — bezprzewodowy douszny system BCI **testowany na nastolatkach**. Istotne, bo grupa wiekowa zgadza się z planowaną grupą badanych.
- **PMID 41337113**, *„Synchronized EEG with two galvanically-separated miniature wireless behind-the-ear EEG sensors"*, EMBC 2025 — **dwa oddzielone galwanicznie moduły zauszne**. To jest bezpośrednio wariant rozłożony z `09_UMIEJSCOWIENIE.md` sekcja 5b, w wersji bez łuku: zamiast przewodu — synchronizacja bezprzewodowa. **Rozwiązuje problem tryboelektryczny i antenowy, który zapisałem jako koszt wariantu rozłożonego.** Do przeczytania przed decyzją o geometrii.
- **PMID 39338748**, *„Detection of Movement-Related Brain Activity Associated with Hand and Tongue Movements from Single-Trial Around-Ear EEG"*, *Sensors* 2024 — aktywność ruchowa wykrywana z pojedynczej próby, z okolicy wokółusznej.

### 1.5 Praca, która zmienia obraz całej dziedziny — i której nie miałem

**[fakt, abstrakt odczytany] Wang Z., Shi N. i in., *„Conformal in-ear bioelectronics for visual and auditory brain-computer interfaces"*, Nature Communications 14:4213 (2023), DOI 10.1038/s41467-023-39814-6, PMID 37452047.** Tsinghua University.

Urządzenie **SpiralE**: elektroda douszna, która **rozwija się spiralnie wzdłuż przewodu słuchowego pod wpływem pobudzenia elektrotermicznego**, żeby zapewnić kontakt konformalny (dopasowany do kształtu, na całej powierzchni).

Wyniki wg abstraktu:
- **95% dokładności offline** w klasyfikacji SSVEP z **9 celami**
- udane pisanie fraz w **40-celowym spellerze SSVEP online, bez kalibracji**
- 84% dokładności klasyfikacji mowy naturalnej w warunkach cocktail party
- obserwacja uboczna: SSVEP douszne wykazują wyraźną tendencję do **drugiej harmonicznej**, co autorzy interpretują jako możliwy wkład w badanie rozkładów przestrzennych harmonicznych

**Dlaczego to jest najważniejsza pozycja w tym pliku i dlaczego wywraca ustalenia — `KOREKTY.md` K-028:**

Przez cały etap 1 liczba „SSVEP z ucha to 6–17 bit/min" służyła jako **ściana** i na niej stała rekomendacja odejścia od twierdzenia przepustowościowego. Te liczby pochodziły z prac z **2015** (n=4) i **2022**. SpiralE pokazuje, że przy dobrym kontakcie mechanicznym forma douszna obsługuje speller 40-celowy online — czyli przepustowość o rząd wielkości wyższą.

**Czynnikiem decydującym okazał się kontakt elektrody, nie odległość od kory wzrokowej.** A kontakt elektrody to warstwy 1 i 2 z sekcji 9.4 handbooka: materiały, mechanika, dopasowanie kształtu — **warsztat użytkownika**.

To działa w obie strony i trzeba widzieć obie:
- **za:** pułap formy dousznej jest znacznie wyżej, niż zakładałem, i leży w warstwie, w której użytkownik jest mocny. Wariant twierdzenia przepustowościowego **wraca do rozważenia**
- **przeciw:** grupa z Tsinghua z aktuacją elektrotermiczną w Nature Communications to nie jest konkurencja, którą się pobija budżetem licealisty. Pole jest obsadzone poważnie

**Do przeczytania w całości w etapie 2** — praca jest w otwartym dostępie (PMC10349124), więc to jest wykonalne bez opłat. **Do czasu przeczytania nie budować na niej twierdzeń liczbowych** poza tymi z abstraktu.

---

## 2. Luka główna projektu — po PRZEGLĄDZIE SYSTEMATYCZNYM

Pytanie zapisane w `KOREKTY.md` jako K-009 **przed sprawdzeniem**: czy sprzętowe usuwanie zakłóceń mięśniowo-ocznych w torze analogowym urządzenia przyusznego jest już zrobione.

Poprzednia sesja przeszukała **jeden kanał** i sama napisała, że to nie jest dowód nieistnienia. Ta sekcja jest wynikiem przeszukania właściwego.

### 2.0 Jak przeszukiwałem — żeby dało się to powtórzyć i podważyć

Baza: **PubMed przez E-utilities NCBI**, 15 VIII 2026. PubMed indeksuje *IEEE Transactions on Biomedical Circuits and Systems* i *IEEE TBME*, co sprawdziłem empirycznie — obie czasopisma pojawiły się w wynikach — więc **kanał obejmuje literaturę układową, nie tylko medyczną**.

| Zapytanie | Trafień |
|---|---|
| `(ear-EEG OR "in-ear EEG" OR "around-ear" OR cEEGrid) AND artifact*` | 22 |
| `(analog OR analogue) AND (artifact* cancel* OR artifact* remov* OR artifact* suppress*) AND EEG AND (front-end OR amplifier OR "analog front end")` | 6 |
| `EEG AND (EMG OR EOG) AND reference channel AND (adaptive filter OR cancellation) AND (hardware OR analog OR circuit)` | **0** |
| `(ear-EEG OR hearable OR "behind the ear") AND (analog front-end OR amplifier OR ASIC OR circuit design)` | 48 |
| `jaw clench* AND EEG AND artifact` | 4 |

**Czego to przeszukanie nadal nie obejmuje, i mówię to wprost:** IEEE Xplore w całości (część materiałów konferencyjnych nie trafia do PubMed), baz patentowych, oraz literatury nieanglojęzycznej. **To jest lepsze przeszukanie niż poprzednie, ale nadal nie jest przeglądem systematycznym w sensie metodologicznym** i nie wolno na jego podstawie twierdzić, że czegoś nie ma.

### 2.1 Co jest zajęte — stan po weryfikacji

| Poziom | Stan techniki | Namiar | Status |
|---|---|---|---|
| korekcja artefaktów ocznych z kanału EOG, programowo, offline | **zajęte od 1983**, technika podręcznikowa nadal w użyciu | Gratton, Coles, Donchin, *Electroencephalogr Clin Neurophysiol* 55:468–484 (1983); poprzednik Hillyard i Galambos (1970) | `[fakt]` co do istnienia i daty |
| adaptacyjne usuwanie artefaktów cyfrowo (filtr adaptacyjny, ANC, SSA) | zajęte, aktywnie rozwijane | m.in. arXiv 2308.13371; PMID 41335679 (2025, dwustopniowe uczenie głębokie) | `[fakt]` |
| **analogowe wykrywanie i kompensacja artefaktów RUCHOWYCH w urządzeniu noszonym** | **zajęte** | **Dabbaghian i in., IEEE TBioCAS 13(6):1141–1151 (2019), PMID 31443050** | **`[fakt]`, abstrakt odczytany** |
| analogowy front-end o tłumieniu artefaktów stymulacyjnych | zajęte | PMID 31151118 — 4 nV/√Hz AFE do LFP podczas DBS | `[fakt]` |
| **analogowa kompensacja offsetu i pojemności pasożytniczych w urządzeniu ZAUSZNYM** | **zajęte, 2026** | **Kim i in., IEEE TBioCAS 20(2):313–327 (2026), PMID 41370143** | **`[fakt]`, abstrakt odczytany** |
| bateryjny AFE EEG z tłumieniem artefaktów mięśniowych | zajęte | MDPI *Appl Sci* 14:6886 | `[wniosek, namiar]` |
| patent na adaptacyjny kompensator artefaktów ruchowych i ocznych | zajęte | US 5513649 | `[wniosek, namiar]` |

**Poprawki do poprzedniej wersji (`KOREKTY.md` K-029):** pozycja opisywana wcześniej jako „8-kanałowy IC EEG, publikacja ~2023, CMRR >115 dB" to w rzeczywistości **Dabbaghian 2019**, i nie jest to układ scalony, tylko **opaska na elastycznym podłożu poliimidowym** (8 kanałów, wzmocnienie 260 V/V, pasmo DC–300 Hz, masa 9,2 g z baterią, elektrody suche bezkontaktowe). **Parametru CMRR >115 dB w tym źródle nie ma** i był mu przypisany błędnie.

**Nowa pozycja, której poprzednia sesja nie znalazła — i jest bliżej niż wszystko inne:** Kim i in. 2026, **behind-the-ear**, plaster, układ scalony w procesie 0,18 µm BCD, 8 kanałów ExG plus PPG, GSR, BioZ i 2 kanały stymulacji, z **adaptacyjną kompensacją offsetu** (architektura OCAP) i **kompensacją pojemności pasożytniczych**. Impedancja wejściowa 2,5 GΩ.

**Ale to nie jest to samo, co nasza oś, i różnica jest konkretna:** Kim kompensuje **offset elektrody i pasożytnicze pojemności** — czyli wolnozmienne i statyczne zakłócenia toru. Nie kompensuje **artefaktu biologicznego z osobnego kanału odniesienia**. To są różne problemy.

### 2.2 Czego nie znalazłem — i co ten brak znaczy

**Nie znalazłem pracy o analogowej kompensacji artefaktu szczękowego, z dedykowanego kanału odniesienia, przed przetwornikiem, w urządzeniu przyusznym.**

Zapytanie skrojone dokładnie pod to — `EEG AND (EMG OR EOG) AND reference channel AND (adaptive filter OR cancellation) AND (hardware OR analog OR circuit)` — dało **zero trafień w PubMed**.

**Jak to czytać, uczciwie:** zero trafień w jednym zapytaniu w jednej bazie to sygnał, nie dowód. Zapytania z operatorem `AND` na pięciu członach są kruche — wystarczy, że autorzy nazwali to inaczej. **Ale w połączeniu z tym, że przeszukanie 48 prac o front-endach przyusznych nie ujawniło niczego takiego, sygnał jest umiarkowanie mocny.**

### 2.3 Werdykt — z jedną zmianą kierunkową, której się nie spodziewałem

**Typ K-009 potwierdzony:** pomysł w wersji ogólnej jest stary, szczelina leży wyłącznie w realizacji. Realizacja analogowa też jest częściowo zajęta — dla artefaktów ruchowych (2019) i dla offsetu w formie zausznej (2026).

**Zmiana kierunkowa, `KOREKTY.md` K-026 — i jest to najważniejsza rzecz w tym pliku dla samego projektu:**

Odczytałem w oryginale abstrakt **Kappel, Looney, Mandic, Kidmose, *„Physiological artifacts in scalp EEG and ear-EEG"*, BioMed Eng OnLine 16:103 (2017), PMID 28800744**, na którym stała cała przesłanka projektu. **Dziewięciu badanych**, artefakty generowane w warunkach kontrolowanych, wpływ mierzony jako pogorszenie SNR odpowiedzi ASSR.

> „Artifacts related to jaw muscle contractions were present all over the scalp and in the ear, with the highest SNR deteriorations in the gamma band. **The SNR deterioration for jaw artifacts were in general higher in the ear compared to the scalp.** **Whereas eye-blinking did not influence the SNR in the ear**, it was significant for all groups of scalps electrodes in the delta and theta bands. Eye movements resulted in statistical significant SNR deterioration in both frontal, temporal and ear electrodes."

I we wnioskach: „ear-EEG was **more prone to jaw related artifacts and less prone to eye-blinking artifacts** compared to state-of-the-art scalp based systems."

**Trzy rzeczy z tego wynikają:**

1. **Przesłanka dla szczęki jest mocniejsza, niż ją stawiałem.** Potwierdzona w oryginale, na 9 osobach, z podanym pasmem (gamma) i metryką (SNR odpowiedzi ASSR). To jest najlepsze zdanie startowe, jakie ma ten projekt, i teraz jest cytowalne.
2. **Przesłanka dla mrugnięcia jest fałszywa.** Mrugnięcie **nie pogarsza SNR w uchu**. Kompensowanie go byłoby rozwiązywaniem problemu, którego w tej formie urządzenia nie ma. Pisałem „EMG szczęki i EOG" jako parę przez cały etap 1 — to było nieuprawnione.
3. **Zostaje ruch gałek ocznych** — nie mrugnięcie — który pogarsza SNR także na elektrodach usznych.

**Poprawna wersja osi projektu:**

> analogowa kompensacja **artefaktu szczękowego** w torze przed wzmocnieniem, w urządzeniu przyusznym, z ruchem gałek ocznych jako kanałem drugorzędnym

zamiast dotychczasowego „artefaktów mięśniowo-ocznych" traktowanych łącznie.

**To upraszcza układ, a nie komplikuje.** Detektor mrugnięcia, który wg sekcji 4 mieliśmy wziąć z ID.EARS jako gotową cegiełkę, **nie jest potrzebny**. Potrzebny jest detektor zaciśnięcia szczęki — a ID.EARS dostarcza dowodu wykonalności także dla niego.

**Co zostaje bez zmian:** twierdzenie „pierwszy raz" jest niedostępne i nie warto o nie walczyć. Twierdzenie pomiarowe — „w tej formie i przy tym poziomie kosztów kompensacja analogowa poprawia parametr X o Y, mierzone tak a tak, względem tego samego układu bez kompensacji" — jest dostępne, mocniejsze i **nie unieważni go znalezienie cudzej pracy w połowie 2027**.

---

## 3. Zadanie 4d nr 6 — „intencja od mózgu, wykonanie od maszyny"

Pytanie: czy jest to publikowana klasa rozwiązań i jak się ją uczciwie raportuje.

**Odpowiedź bez zmian: tak, to jest uznana i nazwana klasa, o dwudziestoletniej historii. Nie wolno jej liczyć jako innowacji.**

Nazwy w literaturze: **shared control**, **shared autonomy**, ostatnio **AI copilot**.

| Praca | Czego dotyczy | Status |
|---|---|---|
| *Brain–computer interface control with artificial intelligence copilots*, **Nat Mach Intell (2025)**, s42256-025-01090-y | kopiloci AI współpracujący z użytkownikiem BCI; sparaliżowani uczestnicy uzyskują lepszą kontrolę kursora i ramienia | `[wniosek, namiar]` |
| *J Neural Eng* 2021, DOI 10.1088/1741-2552/abf8cb, PMID 33862607 | ramię robota z hybrydowym BCI nieinwazyjnym i shared control | `[wniosek, namiar]` |
| *Robotics and Autonomous Systems*, S0921889018306080 | shared control ramienia z BCI i naprowadzaniem wizyjnym | `[wniosek, namiar]` |
| *Comput Struct Biotechnol J* 2023, PMC10433001 | ciągłe shared control robota mobilnego z nawigacją autonomiczną | `[wniosek, namiar]` |

**Jak się to uczciwie raportuje** — odpowiedź na haczyk z sekcji 4c `00_PYTANIA_I_LUKI.md` („ile z tego to naprawdę mózg"):

Literatura porównuje **shared control przeciwko samemu BCI** na tym samym zadaniu i raportuje obie liczby `[wniosek, streszczenie]`. Wielkość wkładu maszyny jest widoczna, bo widać obie kolumny.

**Do planu eksperymentalnego etapu 2, jako pozycja obowiązkowa — trzy warunki na tym samym układzie:**
1. sterowanie z sygnału mózgowego, bez wspomagania
2. sterowanie ze wspomaganiem (wariant docelowy)
3. **układ zasilany sygnałem losowym albo zapisem z odłączonych elektrod**, z tym samym wspomaganiem

Warunek 3 pokazuje, ile zadania wykonuje sama maszyna przy zerowej informacji od użytkownika. **Tego nie da się dorobić po fakcie.**

**Wzmocnienie tej pozycji, nowe:** abstrakt projektu referencyjnego ENBM074 (2026), odczytany w całości (`08` sekcja 2), pokazuje dokładnie taką strukturę na najwyższym poziomie: warunek kontrolny na tym samym sprzęcie, 111 prób randomizowanych i kontrbalansowanych, replikacja na drugiej grupie, oraz **test mechanizmu przez podwójną dysocjację**, a nie tylko test wyniku. To jest wzorzec metodologiczny do skopiowania — i akurat jego kopiowanie sekcja 9.2 handbooka dopuszcza, bo zakaz dotyczy rozwiązania, nie rzemiosła.

---

## 4. Luka, która się zamknęła — i co z tego zostaje

**sEMG/EOG przy uchu jako źródło sterowania: zajęte, i to dłużej, niż sądziłem.**

**ID.EARS**, CHI 2025, DOI 10.1145/3706598.3714185. Urządzenie na jedno ucho, elektrody suche, pięć gestów w czasie rzeczywistym (mrugnięcie, wink lewy, wink prawy, zaciśnięcie zębów, żucie), **>90% dokładności**. Autorzy odwracają konwencję: EMG i EOG jako sygnał zamiast szumu. `[wniosek, streszczenie — CHI nie jest indeksowane w PubMed, pełnego tekstu nie otwierałem]`

**Nowa pozycja, cofająca datę o dekadę `[fakt, abstrakt odczytany]`:** *„A supplementary system for a brain-machine interface based on jaw artifacts for the bidimensional control of a robotic arm"*, **PLoS One 2014, PMID 25390372**. Artefakty szczękowe jako sygnał sterujący ramieniem robota — **jedenaście lat przed ID.EARS**.

**Co to znaczy:** rola 1 (sEMG/EOG jako źródło sterowania) nie jest „zamknięta rok temu", tylko **zamknięta od dawna i domknięta rok temu w formie dousznej**. Status bez zmian: nie wchodzimy tam. Ale to jest kolejny przykład na to, że pierwsze przeszukanie pokazuje najświeższą pracę, a nie najwcześniejszą — i że data pierwszeństwa wymaga osobnego szukania.

**Rola 2 (usuwanie tych sygnałów z EEG) nietknięta przez obie prace** — idą w przeciwną stronę.

**Element do wzięcia, doprecyzowany po K-026:** nasz układ musi wiedzieć, **kiedy** kompensować, czyli potrzebuje detektora **zaciśnięcia szczęki**. ID.EARS jest dowodem, że taki detektor przy uchu działa z trafnością >90%. Detektor mrugnięcia — niepotrzebny, patrz sekcja 2.3.

---

## 5. Luki w warstwie dekodowania

Rozwinięcie w `07_DEKODOWANIE.md`. Tutaj same pozycje otwarte, **z jedną pozycją wykreśloną**.

| Luka | Stan | W zasięgu? |
|---|---|---|
| kalibracja międzysesyjna i międzyosobnicza | aktywnie atakowana, m.in. TFTL (PMID 39365711) deklaruje zero prób kalibracyjnych | **nie jako oś** — pole zatłoczone i algorytmiczne. Ostrzeżenie z sekcji 9.4 handbooka |
| brak wspólnej definicji „słów na minutę" | `07` sekcja 5 | nie jest to luka do wypełnienia, tylko pułapka do uniknięcia |
| ~~brak publicznych zbiorów ear-EEG do sterowania~~ | **TWIERDZENIE OBALONE — patrz niżej** | — |
| metryki użytkowe (czas montażu, stabilność, odsetek sesji bez rekalibracji) rzadko raportowane | wskazywane jako motywacja ear-EEG, rzadko mierzone | **tak** — tanie i dobrze punktowane w sekcji Execution |
| standaryzacja referencji i konfiguracji w ear-EEG | wskazana wprost jako luka w Frontiers 2026, sekcja 1.2 | **tak** — najlepiej trafiona pozycja w całym pliku |

### 5.1 Twierdzenie obalone: publiczny zbiór ear-EEG do sterowania ISTNIEJE

Poprzednia wersja tego pliku twierdziła: „**nie znalazłem publicznego zbioru ear-EEG pod zadania sterowania**. Istniejące dotyczą snu i uwagi słuchowej" — i proponowała, żeby opublikowanie własnego zbioru uczynić elementem wkładu projektu.

**[fakt, abstrakt odczytany] To jest nieprawda.** Lee Y-E., Shin G-H., Lee M., Lee S-W., *„Mobile BCI dataset of scalp- and ear-EEGs with ERP and SSVEP paradigms while standing, walking, and running"*, **Scientific Data 8:315 (2021)**, DOI 10.1038/s41597-021-01094-4, PMID 34930915.

Zawartość: **24 uczestników**, **32-kanałowy EEG skalpowy + 14-kanałowy ear-EEG + 4-kanałowy EOG + 9-kanałowe IMU** (czoło, oba kostki). Cztery prędkości: stanie, wolny marsz, szybki marsz, lekki bieg (0 / 0,8 / 1,6 / 2,0 m/s). Dla każdej prędkości **dwa paradygmaty BCI: ERP i SSVEP**. Jakość sygnału walidowana jakościowo i ilościowo dla każdej prędkości.

**Dlaczego ta pomyłka była kosztowna, a jej naprawa jest prezentem — `KOREKTY.md` K-027:**

To nie jest zbiór „przypadkiem pasujący". Ma **równoległy EOG i pomiar ruchu**, czyli dokładnie pod pytanie o artefakty i stabilność przy ruchu, na którym stoi oś projektu. Konsekwencje:

- teza „opublikowanie własnego zbioru jest tanim elementem wkładu" — **osłabiona**. Pole nie jest puste, więc to nie jest wyróżnik. Zostaje jako dobra praktyka, nie jako argument
- **można pracować nad warstwą dekodowania, zanim powstanie jakikolwiek sprzęt.** Jesień 2026 nie musi być wyłącznie nauką PCB. Warstwa 4 z sekcji 9.4 handbooka da się rozwijać równolegle, na cudzych danych, za darmo
- daje **punkt odniesienia dla własnego urządzenia**: te same paradygmaty, znany zbiór, uczciwe porównanie „mój sprzęt wobec zbioru referencyjnego"
- `[luka]` **licencji tego zbioru nie sprawdziłem.** *Scientific Data* publikuje w otwartym dostępie, ale licencja danych bywa inna niż licencja artykułu. Do sprawdzenia przed użyciem — wymaga tego zarówno sekcja 4.5 regulaminu Explory, jak i etyka ISEF

### 5.2 Drugi zbiór, dołożony

**[fakt]** *„Electrophysiological Characterisation of Commercial Ear-EEG Devices"*, EMBC 2025, PMID 41336899. Charakterystyka **komercyjnych** urządzeń dousznych — czyli gotowy materiał do `05_RYNEK.md` i do baselineu wariantu 1 twierdzenia, którego wcześniej brakowało. Do przeczytania w etapie 2.
