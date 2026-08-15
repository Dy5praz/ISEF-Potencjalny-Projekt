# 00 — Streszczenie etapu 1: co z tego wynika dla projektu

**Data:** 15 sierpnia 2026, wersja druga (przebudowana)
**Zakres:** przemiał literatury wg sekcji 10 handbooka, plus 12 zadań weryfikacyjnych z `00_PYTANIA_I_LUKI.md` sekcja 4d.

Pierwsza wersja tego pliku prowadziła od znalezisk do wniosków. To był zły porządek — literatura jest materiałem, nie produktem. Ta wersja prowadzi od decyzji projektowych, a znaleziska są pod nimi jako uzasadnienie.

---

## 1. Co projekt ma robić — stan po etapie 1

Wersja, którą da się obronić po przemiale, w jednym miejscu:

> **Urządzenie zauszne wielkości aparatu słuchowego, rejestrujące EEG, z analogową kompensacją zakłóceń mięśniowo-ocznych przed wzmocnieniem, sterujące obiektem kilkoma komendami dyskretnymi.**
> **Twierdzenie jest pomiarowe:** kompensacja analogowa poprawia mierzalny parametr toru o X względem identycznego układu bez kompensacji, w warunkach, w których zakłócenia przy uchu są największe (mowa, żucie, ruch oczu).
> **Przewaga nad rynkiem leży w metryce użytkowej**, nie w przepustowości.

Cztery rzeczy zmieniły się w tym opisie względem stanu sprzed etapu 1, i każda z nich jest decyzją, nie ciekawostką.

### 1.1 Twierdzenie przestaje być o pierwszeństwie, staje się o pomiarze

**Powód:** kandydat na oś projektu jest częściowo zajęty. Usuwanie artefaktów ocznych z osobnego kanału to technika z 1983 roku. Usuwanie artefaktów **w domenie analogowej, przed wzmocnieniem** też jest zrobione — istnieje 8-kanałowy układ scalony EEG z w pełni analogową ekstrakcją i usuwaniem artefaktów ruchowych.

Nie znalazłem kompensacji konkretnie EMG szczękowego i EOG, z kanału referencyjnego, w urządzeniu przyusznym. **Ale to jest przeszukanie jednym kanałem, nie dowód nieistnienia**, i budowanie na tym strategii byłoby powtórzeniem błędu nr 5 z sekcji 8 handbooka.

**Co z tego robimy:** twierdzenie „pierwszy raz" jest niedostępne i nie warto o nie walczyć. Twierdzenie „ten układ poprawia X o Y, oto pomiar" jest dostępne, mocniejsze i **nie unieważni go znalezienie cudzej pracy w połowie 2027 roku**. Przy historii tego projektu — trzy kierunki ubite przez prior art — to jest różnica między planem odpornym a kolejnym kadłubkiem.

### 1.2 Przewaga jest w metryce użytkowej, bo w przepustowości nie da się wygrać

**Powód, liczbowo:** SSVEP z elektrod potylicznych daje ~92 bit/min. Ten sam paradygmat z ucha: 6–17 bit/min. Różnica pięcio- do piętnastokrotna i wynika z geometrii — odległości od kory i rozstawu elektrod — a nie z jakości wykonania. Żaden wzmacniacz tego nie odrobi.

**Co z tego robimy:** rozstrzygam C2 rekomendacją na **wariant 2** z sekcji 2.1 `00_PYTANIA_I_LUKI.md`. Mierzymy czas montażu, stabilność w ciągu dnia, odsetek sesji bez ponownej kalibracji, tolerancję na ruch i mówienie. To są wymiary, w których forma zauszna bije czapkę **realnie**, a nie na papierze, i są prawie nieraportowane w literaturze — czyli jest tam miejsce na wkład.

Wariant 1 („przewaga przy stałej widoczności") zostaje jako tabela towarzysząca. Jego baseline jest prawie pusty: **żaden produkt douszny na rynku nie robi sterowania** — NextSense, IDUN, Neurable mierzą sen i skupienie. Porównywać się trzeba z literaturą ear-EEG, nie z produktami.

### 1.3 Paradygmat wraca do rozstrzygnięcia — moja poprzednia rekomendacja jest podważona

**Powód:** rekomendowałem paradygmaty słuchowe, bo kora słuchowa leży blisko ucha. Praca z 2026 na 19 osobach porównująca system douszny z 32-kanałowym skalpowym podaje, że w konfiguracji dousznej **alfa spoczynkowa wychodzi pewnie, a odpowiedź słuchowa N1-P2 nie**. Do tego uwaga słuchowa ma najniższe ITR ze wszystkiego, co zebrałem: 1,9–2,1 bit/min, czyli około trzech komend na minutę.

Bliskość anatomiczna nie wystarcza — liczy się też orientacja dipola i rozstaw elektrod względem niego.

**Co z tego robimy:** SSVEP wygląda lepiej mimo większej odległości, bo daje sygnał okresowy o znanej z góry częstotliwości, który da się wyłuskać przy złym SNR. **Ale ma koszt:** wymaga patrzenia na migający obiekt, co osłabia argument „działa przy zamkniętych oczach" i wpycha nas w bezpośrednie porównanie z eye trackingiem, na które trzeba mieć odpowiedź. **Decyzja należy do etapu 2 i musi być świadoma.**

### 1.4 Wariant hybrydowy zamknięty — ale zostawia nam gotowy element

**Powód:** ID.EARS (CHI 2025) — urządzenie na jedno ucho, elektrody suche, pięć gestów rozpoznawanych w czasie rzeczywistym z ponad 90% trafnością: mrugnięcie, wink lewy, wink prawy, zaciśnięcie zębów, żucie. Autorzy wprost odwracają konwencję: EMG i EOG jako sygnał zamiast szumu.

**Co z tego robimy:** rola 1 (sEMG/EOG jako źródło sterowania) schodzi z „odłożonej" na zamkniętą. Rola 2 jest nietknięta — ta praca idzie w przeciwną stronę niż my.

**Element do wzięcia:** nasz układ musi wiedzieć, **kiedy** kompensować, czyli potrzebuje detektora zaciśnięcia szczęki i mrugnięcia. ID.EARS jest dowodem, że taki detektor przy uchu działa z trafnością >90%. To skraca nam drogę, zamiast ją zamykać.

---

## 2. Co to zmienia w kalendarzu i w decyzjach zakupowych

| Sprawa | Stan przed etapem 1 | Stan po |
|---|---|---|
| **czy zdążymy na ISEF 2028** | `[luka]` o najwyższej stawce, K-007 | **potwierdzone.** Finał X 2027 → ISEF V 2028. Teza „jeden strzał" stoi, kolizji z maturą nie ma |
| **El-Robo-Mech IV 2027** | twardy termin i zewnętrzna walidacja | **tylko wymuszony termin.** Nagrodą jest indeks na studia, laureatów było 34 — to nie jest podium z selektywnych zawodów. Termin można przesunąć bez straty strategicznej |
| **drukarka Qidi Q2** | zakup wstrzymany do weryfikacji | **nie kupować.** Wkładki douszne robi się drukiem żywicznym, nie FDM; włókno węglowe jest tu przeciwskuteczne. Otwarte: czy żywica z certyfikatem ISO 10993 jest dostępna dla amatora w Polsce |
| **badania na sobie** | `[luka]`, ryzyko dyskwalifikacji | **prawdopodobnie zwolnione** z uprzedniej zgody komisji — ale warunkiem jest brak ryzyka, a urządzenie elektryczne przy głowie może ten warunek łamać. **Jedyna pozycja o bezpośrednich konsekwencjach dyskwalifikacyjnych** |
| **opiekun naukowy** | `[luka]` | magister **nie** spełnia definicji Qualified Scientist (wymaga doktoratu), ale może być Adult Sponsor. Czy w ogóle potrzebny doktor — zależy od klasyfikacji ryzyka, patrz wyżej |

**Najpilniejsza rzecz w całej tabeli:** wiersz o badaniach na sobie. Jeżeli urządzenie elektryczne przy głowie łamie zwolnienie, to formalności muszą ruszyć **przed pierwszym pomiarem**, a nie przed finałem. To przesuwa jesień 2026 z „nauka PCB" na „nauka PCB plus papiery".

---

## 3. Czego NIE robimy — lista zamknięta

Wynika z `03_SCIANY_FIZYCZNE.md`. Każda pozycja to twierdzenie, którego nie da się obronić przy formie zausznej:

- **rozdzielczość porównywalna z inwazyjnymi** — czaszka rozmywa sygnał do ~5–9 cm i to jest ściana fizyczna
- **wyższy ITR niż czapka przy tym samym paradygmacie** — geometria, sekcja 1.2
- **sterowanie ciągłe, wielowymiarowe z jednej pozycji zausznej** — brak filtracji przestrzennej do rozdzielenia kierunków
- **działanie u 100% badanych w wyobrażeniu ruchu** — 15–30% osób nie uzyskuje kontroli niezależnie od sprzętu. **Przy grupie kilku osób jedna niedziałająca jest zdarzeniem oczekiwanym i musi być wpisana w plan z góry**, inaczej wygląda jak ukrywanie porażki
- **oś projektu w uczeniu głębokim** — benchmark z 2024 pokazuje, że metody riemannowskie biją sieci konwolucyjne przy małej liczbie kanałów i danych, czyli dokładnie w naszym reżimie. Wchodzenie na pole zatłoczone bez przewagi wydajnościowej nie ma sensu

---

## 4. Trzy rzeczy do wpisania w plan eksperymentalny już teraz

Nie da się ich dorobić po fakcie, a wszystkie trzy wynikają z tego etapu.

**4.1 Warunek kontrolny na sygnale losowym.** Przy podziale pracy z maszyną („intencja od mózgu, wykonanie od maszyny" — publikowana klasa rozwiązań, **nie liczyć jako innowacji**) juror zapyta, ile z tego to naprawdę mózg. Odpowiedź musi być pomiarowa: ten sam układ w trzech wariantach — sterowanie z sygnału, sterowanie ze wspomaganiem, oraz **układ zasilany sygnałem losowym z tym samym wspomaganiem**. Trzeci warunek pokazuje, ile zadania robi sama maszyna przy zerowej informacji od użytkownika.

**4.2 Każda liczba wydajności w dwóch wersjach.** Surowe dekodowanie i wynik z całą warstwą wspomagającą. Powód: w pracach nad protezami mowy metryka jest liczona na wyjściu całego łańcucha — surowy błąd fonemowy sieci to 19,7%, a jednocyfrowy błąd słowny robi dopiero model językowy. W benchmarku na tych samych danych neuronowych zmiana samego dekodera dała 9,7% → 5,8%. Jeżeli podamy jedną liczbę, jurorzy z dziedziny zapytają o drugą.

**4.3 Wyniki osobno dla wariantu wewnątrzsesyjnego, międzysesyjnego i międzyosobniczego.** Podanie samego wewnątrzsesyjnego jako „dokładności układu" to najczęstszy sposób zawyżania liczby w tej dziedzinie i pierwsza rzecz, o którą pyta ktoś znający temat. Sekcja 4.5 regulaminu Explory (krytycyzm wobec własnych wyników) wymaga tego wprost.

---

## 5. Status źródłowy — dlaczego część tego jest jeszcze miękka

**[fakt] Ta sesja działa w środowisku `env_01NdKrhepeQo6dVAHusCvQFj` („Projekty"), nie w `env_01USAAMBR9QZf9W8ERvrVkEA` („Projekty Full Acess").** Polityka sieciowa idzie ze środowiska sesji i sesji nie da się przenieść. Dlatego mimo poprawnie ustawionego `Full` na nowym środowisku ta sesja nadal dostaje 403 na wszystko poza rejestrami pakietów i GitHubem — sprawdzone tunelem kontenera, narzędziem WebFetch i bezpośrednim curl-em, po restarcie kontenera o 14:00.

Skutek: **żadnej pracy źródłowej nie otworzyłem.** Wszystkie liczby mają znacznik `[wniosek, streszczenie]`. Istnienie prac (tytuł, autorzy, czasopismo) jest wiarygodne, bo pochodzi z indeksu; treść i liczby wymagają potwierdzenia w oryginale.

**Co jest przez to niezamknięte:**

| # z 4d | Zadanie | Czego brakuje |
|---|---|---|
| 2 | ISEF Human Participants — **klasyfikacja ryzyka urządzenia elektrycznego** | oryginał International Rules. **Priorytet nr 1** |
| 3 | czy oś projektu zajęta | IEEE Xplore, PubMed — przegląd systematyczny |
| 10 | pełny abstrakt ENBM074 (2026) | baza abstraktów Society for Science |
| 11 | projekty neuro w finałach Explory 2016–2026 | listy finalistów |
| 12 | oba arkusze oceny ISEF | societyforscience.org |

Pozycje 1, 5, 6, 7, 8, 9 z listy 4d są zrobione.

**Żeby to domknąć:** nowa sesja założona w środowisku **„Projekty Full Acess"**. Ustawienia są dobre, chodzi wyłącznie o wybór środowiska przy zakładaniu sesji.

---

## 6. Nawigacja po pozostałych plikach

| Plik | Po co go otwierać |
|---|---|
| `02_MECHANIZMY.md` | **jeżeli coś w tym pliku jest niejasne** — tam każdy termin ma wyjaśnienie, od tego, skąd bierze się napięcie na głowie |
| `03_SCIANY_FIZYCZNE.md` | co jest fizyczne, co technologiczne, oraz **jak zmierzyć szum wzmacniacza bez oscyloskopu** |
| `04_LUKI_ZAPISANE.md` | pełna weryfikacja osi projektu (sekcja 2) i luki opisane w przeglądach |
| `06_TABELA_PARAMETROW.md` | wszystkie liczby w jednym miejscu, z kolumną „skąd ta liczba" |
| `07_DEKODOWANIE.md` | paradygmaty, metody, zbiory danych, rozbiór metryki „słów na minutę" |
| `08_KONKURENCJA_ISEF.md` | kalendarz, El-Robo-Mech, projekt referencyjny |
| `ISEF_HUMAN_PARTICIPANTS.md` | **formalności i terminarz wsteczny — najpilniejsze** |
| `KOREKTY.md` | K-001…K-018, w tym cztery błędy moje z tego etapu |
</content>
