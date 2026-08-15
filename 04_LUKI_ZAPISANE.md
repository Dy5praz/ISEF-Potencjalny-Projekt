# 04 — Luki zapisane w literaturze

**Zakres wg sekcji 10.D handbooka.** Sekcje „limitations", „future work", „open challenges" ze świeżych prac. Z namiarem, treścią i moją oceną, czy leży to w zasięgu warsztatu z sekcji 1 handbooka.

**To jest właściwa metoda szukania luki** — luki są opisane, nie trzeba ich zgadywać.

**Zastrzeżenie źródłowe, obowiązujące dla całego pliku:** nie otworzyłem żadnej z tych prac. Poniższe pozycje to **problemy wskazane w streszczeniach i abstraktach**, nie cytaty. Handbook żądał krótkich cytatów — **nie mogę ich podać, bo nie mam dostępu do pełnych tekstów**, a wymyślenie cudzysłowu byłoby fabrykacją źródła. Zamiast tego podaję treść problemu i dokładny namiar, żeby dało się to zweryfikować jednym otwarciem strony.

---

## 1. Luki wskazane w przeglądach ear-EEG 2025–2026

### 1.1 Przegląd: MDPI *Sensors* 25(11):3321, 2025
*„The Next Frontier in Brain Monitoring: A Comprehensive Look at In-Ear EEG Electrodes and Their Applications"*. Dostępny też jako pełny tekst w repozytorium Chalmers (publikacja 547020).

Problemy otwarte wymienione przez autorów `[wniosek, streszczenie]`:

| Problem | W zasięgu warsztatu? | Uwaga |
|---|---|---|
| **zmienność anatomiczna kanału słuchowego** | **tak** | druk 3D pod indywidualny odlew. Warstwa 2 z sekcji 9.4 handbooka |
| **optymalizacja ergonomii** | **tak** | mechanika i modelowanie — najmocniejsza strona użytkownika |
| **redukcja artefaktów ruchowych** | **tak, częściowo** | mechanika mocowania + tor analogowy |
| dobór materiałów | tak | patrz `05_RYNEK.md` sekcja 5 |
| jakość biosygnału | tak | to jest oś kandydująca |
| usuwanie artefaktów | **tak — to jest nasz punkt** | patrz sekcja 2 poniżej |
| elektronika ultraniskiej mocy | **raczej nie** | to jest teren projektowania układów scalonych |

**Ocena [wniosek]:** trzy pierwsze pozycje leżą dokładnie w przecięciu „opisane jako otwarte" i „mechanika plus elektronika". To jest najlepiej trafiony fragment całego przemiału względem profilu użytkownika.

### 1.2 Frontiers in Neuroscience 20:1859327, 2026
*„Signal-specific performance of in-ear EEG: strengths and limitations"* (wariant tytułu w abstrakcie: *„Signal-Specific Strengths and Limitations of a Fully In-Ear EEG Configuration"*).

Luka wskazana wprost: **brak standaryzacji referencji i konfiguracji elektrod w ear-EEG.** Autorzy stwierdzają, że wykrywalność sygnału zależy silnie od klasy sygnału, wielkości efektu i **geometrii rejestracji**, i formułują to jako potrzebę „configuration-aware guidance" przy projektowaniu badań `[wniosek, streszczenie]`.

**Ocena [wniosek]:** to jest luka **metodologiczna, nie sprzętowa** — a więc tania. Starannie zaprojektowane porównanie kilku konfiguracji referencji na jednym urządzeniu, z niepewnościami, jest publikowalną robotą, która **nie wymaga budżetu, tylko dyscypliny pomiarowej**. Dla projektu ma wartość podwójną: jest realnym wkładem i jednocześnie dostarcza tabeli, której wymaga arkusz oceny ISEF w sekcji Execution („testowany w wielu warunkach i próbach").

### 1.3 Frontiers in Human Neuroscience, art. 1793705, 2026
*„In-ear EEG wearables for brain activity assessment and cognitive rehabilitation: the emerging role of multimodal embedded intelligence"*.

Wyzwania wymienione: umiejscowienie elektrod, sprzężenie mechaniczno-elektryczne, odporność na ruch, efektywność energetyczna, długotrwała noszalność `[wniosek, streszczenie]`.

**„Sprzężenie mechaniczno-elektryczne"** — to jest zależność jakości sygnału od tego, jak elektroda przylega do skóry i jak zmienia się to przy ruchu. **W zasięgu, i to jest problem mechaniczny udający problem elektroniczny** — czyli dokładnie ten typ, w którym użytkownik ma przewagę nad konkurencją algorytmiczną.

### 1.4 MDPI *Micromachines* 17(7):764
*„Recent Progress in In-Ear EEG Technology and Its Emerging Real-World Applications: A Review"* — do przejrzenia po odblokowaniu sieci, nie zdążyłem ustalić treści sekcji o wyzwaniach.

---

## 2. Luka główna projektu — stan po weryfikacji zadania 4d nr 3

Pytanie zapisane w `KOREKTY.md` jako K-009 **przed sprawdzeniem**: czy sprzętowe usuwanie zakłóceń mięśniowo-ocznych w torze analogowym urządzenia przyusznego jest już zrobione.

### 2.1 Co jest zajęte

| Poziom | Stan techniki | Namiar |
|---|---|---|
| korekcja artefaktów ocznych z kanału EOG, programowo, offline | **zajęte od 1983**, technika podręcznikowa nadal w powszechnym użyciu | Gratton, Coles, Donchin, *Electroencephalogr Clin Neurophysiol* 55:468–484 (1983); poprzednik Hillyard i Galambos (1970) |
| adaptacyjne usuwanie artefaktów (filtr adaptacyjny, ANC, analiza spektrum osobliwego), cyfrowo | zajęte, aktywnie rozwijane | m.in. arXiv 2308.13371 |
| **analogowe usuwanie artefaktów ruchowych przed końcowym wzmocnieniem, w układzie scalonym** | **zajęte** — 8-kanałowy IC EEG ambulatoryjny z wewnątrzkanałową, w pełni analogową ekstrakcją i usuwaniem artefaktów ruchowych; CMRR >115 dB przy 50/60 Hz | publikacja ~2023 `[wniosek, streszczenie, jedno źródło]` |
| pętle kompensacyjne chroniące wzmacniacz przed nasyceniem artefaktem stymulacyjnym | zajęte, CMOS AFE | prace nad wzmacniaczami z modulacją chopper |
| bateryjny AFE EEG z tłumieniem artefaktów ruchu mięśni | zajęte | MDPI *Applied Sciences* 14:6886, DOI 10.3390/app14166886 |
| patent na adaptacyjny kompensator artefaktów ruchowych i ocznych w EEG | zajęte | US 5513649 |

### 2.2 Czego nie znalazłem

**Nie znalazłem pracy o analogowej kompensacji konkretnie EMG szczękowego i EOG, z dedykowanego kanału odniesienia, w urządzeniu noszonym przy uchu.**

**To nie jest dowód nieistnienia.** Przeszukanie jednym kanałem, bez IEEE Xplore i PubMed, to nie jest przegląd systematyczny. Zgodnie z błędem nr 5 z sekcji 8 handbooka **nie wolno na tym budować strategii**, dopóki nie zostanie to sprawdzone w bazach.

### 2.3 Werdykt — także w wersji „zajęte", jak żądał użytkownik

**Typ K-009 potwierdzony: pomysł w wersji ogólnej jest stary, szczelina leży wyłącznie w realizacji.** Do tego dochodzi ustalenie, którego typ nie przewidywał: **realizacja analogowa też jest zajęta**, tylko na poziomie układów scalonych i dla artefaktów ruchowych.

Co z tego wynika operacyjnie:

1. **Twierdzenie „pierwszy raz" jest niedostępne.** Nawet gdyby dalsze szukanie nic nie znalazło, obrona takiego twierdzenia przed jurorem wymagałaby przeglądu systematycznego, którego licealista nie zrobi wiarygodnie.
2. **Twierdzenie pomiarowe jest dostępne i mocniejsze.** Kształt: „w tej formie i przy tym poziomie kosztów kompensacja analogowa poprawia parametr X o Y, mierzone tak a tak, względem tego samego układu bez kompensacji". Takiego twierdzenia **nie unieważnia znalezienie cudzej pracy** — bo to jest pomiar naszego układu, a nie roszczenie o pierwszeństwo.
3. **Przesłanka merytoryczna jest mocna i pochodzi z pracy recenzowanej**: Kappel i in. 2017 (*BioMed Eng OnLine* 16:103) zmierzyli, że pogorszenie SNR od artefaktów szczękowych jest **w uchu ogólnie większe niż na skalpie** `[wniosek, streszczenie]`. Czyli problem jest w naszej formie udokumentowany jako poważniejszy niż w formie standardowej. To jest najlepsze zdanie startowe, jakie ma ten projekt.

---

## 3. Zadanie 4d nr 6 — „intencja od mózgu, wykonanie od maszyny"

Pytanie: czy jest to publikowana klasa rozwiązań i jak się ją uczciwie raportuje.

**Odpowiedź: tak, to jest uznana i nazwana klasa, o dwudziestoletniej historii. Absolutnie nie wolno jej liczyć jako innowacji.**

Nazwy w literaturze: **shared control**, **shared autonomy**, ostatnio **AI copilot**.

| Praca | Czego dotyczy |
|---|---|
| Nature Machine Intelligence 2025, *„Brain–computer interface control with artificial intelligence copilots"* | kopiloci AI współpracujący z użytkownikiem BCI; sparaliżowani uczestnicy uzyskują lepszą kontrolę kursora i ramienia |
| *J Neural Eng* 2021, DOI 10.1088/1741-2552/abf8cb | ramię robota z hybrydowym BCI nieinwazyjnym i strategią shared control |
| *Robotics and Autonomous Systems* (Elsevier, S0921889018306080) | shared control ramienia z BCI i naprowadzaniem wizyjnym |
| *Comput Struct Biotechnol J* 2023 (PMC10433001) | ciągłe shared control robota mobilnego z nawigacją autonomiczną |
| PMC4797113 | mieszanie BMI z autonomiczną robotyką wizyjną przy chwytaniu |

**Jak się to uczciwie raportuje** — i to jest odpowiedź na haczyk zapisany w sekcji 4c `00_PYTANIA_I_LUKI.md` („ile z tego to naprawdę mózg"):

Literatura porównuje **shared control przeciwko samemu BCI** na tym samym zadaniu, i raportuje obie liczby. Typowy wynik: z shared control zadania wychodzą częściej, ruch jest dokładniejszy i mniej męczący `[wniosek, streszczenie]`. Wielkość wkładu maszyny jest widoczna, bo widać obie kolumny.

**Do planu eksperymentalnego etapu 2, jako pozycja obowiązkowa:** trzy warunki na tym samym układzie —
1. sterowanie z sygnału mózgowego, bez wspomagania
2. sterowanie z wspomaganiem (wariant docelowy)
3. **układ zasilany sygnałem losowym lub zapisem z odłączonych elektrod**, z tym samym wspomaganiem

Warunek 3 jest kluczowy: pokazuje, ile zadania wykonuje sama maszyna przy zerowej informacji od użytkownika. Bez niego pytanie jurora „ile z tego to naprawdę mózg" nie ma odpowiedzi pomiarowej. **Tego nie da się dorobić po fakcie** — musi być zaplanowane od pierwszego szkicu.

---

## 4. Luka, która się właśnie zamknęła — i co z tego zostaje

**sEMG/EOG przy uchu jako źródło sterowania: zajęte.**

**ID.EARS**, CHI 2025, DOI 10.1145/3706598.3714185, An, Oh, Kim, Kim, Park, Oh. Urządzenie na jedno ucho, elektrody suche, pięć gestów rozpoznawanych w czasie rzeczywistym (mrugnięcie, wink lewy, wink prawy, zaciśnięcie zębów, żucie), **>90% dokładności** w walidacji krzyżowej. Pozycja elektrod dobrana testem tłumienia alfa (AAR). Zastosowania: sterowanie muzyką, dostępność, MR/XR, zdrowie `[wniosek, streszczenie]`.

Autorzy formułują to jako świadome odwrócenie konwencji: dotychczas EMG i EOG w ear-EEG traktowano jako szum do usunięcia, oni robią z tego sygnał.

**Co to znaczy dla nas:**
- rola 1 z sekcji 4b/C3 `00_PYTANIA_I_LUKI.md` (sEMG/EOG jako źródło sterowania) — **zamknięta**. Nie „ryzykowna", tylko zrobiona, rok temu, z demonstracją
- rola 2 (usuwanie tych sygnałów z EEG) — **nietknięta przez tę pracę**, bo idzie w przeciwną stronę
- **wartość uboczna, konkretna:** ID.EARS pokazuje, że przy uchu da się w czasie rzeczywistym **wykrywać** zaciśnięcie zębów i mrugnięcia z >90% trafnością. Dla nas to nie konkurencja, tylko **gotowy dowód wykonalności detektora**, który nasz układ i tak potrzebuje — żeby wiedzieć, kiedy kompensować. To jest cegiełka, nie przeszkoda

---

## 5. Luki w warstwie dekodowania

Rozwinięcie w `07_DEKODOWANIE.md`. Tutaj same pozycje otwarte:

| Luka | Stan | W zasięgu? |
|---|---|---|
| kalibracja międzysesyjna i międzyosobnicza | aktywnie atakowana, m.in. TFTL (PMID 39365711) deklaruje **zero prób kalibracyjnych** | **nie jako oś** — pole zatłoczone i algorytmiczne. Ostrzeżenie z sekcji 9.4 handbooka |
| brak wspólnej definicji „słów na minutę" | `07` sekcja 5 | nie jest to luka do wypełnienia, tylko pułapka do uniknięcia |
| **brak publicznych zbiorów ear-EEG do sterowania** | zbiory ear-EEG dotyczą snu i uwagi słuchowej, nie sterowania | **tak, i to jest ciekawe** — patrz niżej |
| metryki użytkowe (czas montażu, stabilność w ciągu dnia, odsetek sesji bez rekalibracji) rzadko raportowane | wskazywane jako motywacja ear-EEG, rzadko mierzone | **tak** — tanie i dobrze punktowane |

**Rozwinięcie wiersza trzeciego [wniosek]:** największy publiczny zbiór ear-EEG, jaki znalazłem, to **320 zapisów snu od 30 osób** (*Scientific Data*, 19 II 2025); drugi to cEEGrid od 98 osób do dekodowania uwagi słuchowej. **Nie znalazłem publicznego zbioru ear-EEG pod zadania sterowania.** Jeżeli to się potwierdzi, opublikowanie własnego zbioru wraz z projektem jest tanim i mocnym elementem wkładu — bo pokazuje, że praca jest weryfikowalna przez innych, co arkusze oceny punktują wprost.
</content>
