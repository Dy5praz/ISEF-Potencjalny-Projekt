# 20 — PROJEKT. Aktywne łożysko magnetyczne z estymacją położenia bez czujników

**Data:** 17 sierpnia 2026
**Status:** projekt wybrany, etap 2 otwarty
**Poprzedni kierunek (interfejs neuralny):** zamknięty decyzją użytkownika. Nie kasuję plików 00–13 — przemiał literatury i cała metodyka audytu zostają jako dorobek i jako wzorzec postępowania.

---

## 0. Jedno zdanie

**Budujesz aktywne łożysko magnetyczne — wirnik trzymany w powietrzu polem magnetycznym, bez żadnego kontaktu — a potem mierzysz, ile dokładnie tracisz, kiedy wyrzucisz z niego czujniki położenia i zastąpisz je samą cewką wykonawczą.**

Rok pierwszy: zbudować i scharakteryzować. Rok drugi: wyrzucić czujniki i zmierzyć koszt.

---

## 1. Co to jest, dla kogoś kto tego nie zna

`[fakt]` **Łożysko** to element, który pozwala wałowi się obracać i trzyma go na miejscu. Zwykłe łożysko to kulki albo film oleju — czyli kontakt, tarcie, zużycie, smar.

`[fakt]` **Aktywne łożysko magnetyczne** (ang. *active magnetic bearing*, AMB) trzyma wał w powietrzu elektromagnesami. Zero kontaktu, zero tarcia, zero smaru, zero zużycia. Używa się ich tam, gdzie kontakt jest niedopuszczalny albo prędkości są za wysokie dla łożysk tocznych: pompy turbomolekularne (próżnia), sprężarki bezolejowe w chłodnictwie przemysłowym, magazyny energii w kole zamachowym, sprężarki gazu na rurociągach.

`[fakt]` **Dlaczego to jest problem sterowania, a nie mechaniki.** Elektromagnes zawsze *przyciąga*. Siła rośnie, gdy szczelina maleje — czyli im bliżej wirnik podejdzie, tym mocniej jest ciągnięty. To jest układ **z natury niestabilny**: bez ciągłej korekty wirnik przykleja się do stojana w ułamku sekundy. Stabilność bierze się wyłącznie z pętli sprzężenia zwrotnego, która tysiące razy na sekundę mierzy położenie i koryguje prąd.

> **Termin:** *sprzężenie zwrotne* — układ mierzy własny wynik i na tej podstawie poprawia własne działanie. Tu: mierzy, gdzie jest wirnik, i zmienia prąd tak, żeby wrócił na środek.

`[fakt]` Z tego wynika, że **każda sterowana oś potrzebuje własnego czujnika położenia** — z własnym torem analogowym, własnym okablowaniem, własnym mocowaniem i własną kalibracją. W maszynie z dwoma łożyskami promieniowymi i jednym osiowym to jest pięć czujników.

## 2. Skąd bierze się pytanie badawcze

`[fakt]` Istnieje klasa rozwiązań nazywana **self-sensing** albo *sensorless AMB*: zamiast osobnego czujnika wykorzystuje się **samą cewkę elektromagnesu jako czujnik**. Indukcyjność cewki zależy od szczeliny powietrznej — im bliżej wirnik, tym większa indukcyjność. Mierząc prąd i napięcie na cewce, którą i tak się steruje, da się wyliczyć położenie wirnika.

> **Termin:** *indukcyjność* — miara tego, jak bardzo cewka opiera się zmianom prądu. Zależy od geometrii obwodu magnetycznego, więc zależy od tego, gdzie jest wirnik.

`[fakt]` To nie jest pomysł nowy i nie udaję, że jest. Kierunek ma własną literaturę przeglądową — *„Displacement Self-Sensing Active Magnetic Bearing Drives — An Overview"* (2025) — oraz prace o wstrzykiwaniu sygnału wysokoczęstotliwościowego, o estymacji z pomiaru prądu stałego i o algorytmach demodulacji.

`[fakt]` **I ta literatura sama wypisuje, co jest nierozwiązane.** Z przeglądu i z prac źródłowych, cztery pozycje:

| Opisane ograniczenie | Co znaczy |
|---|---|
| ograniczona dokładność, odporność i dynamika estymacji | estymowane położenie jest gorsze niż mierzone i nie wiadomo z góry o ile |
| przesunięcie fazowe wnoszone przez filtry w torze demodulacji | filtry potrzebne do wyciągnięcia sygnału opóźniają go, a opóźnienie w pętli zjada **zapas stabilności** |
| sprzężenie estymaty położenia z prądem roboczym, nasycenie magnetyczne | przy dużym obciążeniu rdzeń się nasyca, indukcyjność przestaje zależeć od szczeliny w ten sam sposób i estymata kłamie |
| sprzężenie skrośne między osiami, prądy wirowe | to, co dzieje się w jednej osi, wchodzi w pomiar drugiej |

> **Termin:** *zapas stabilności* — o ile można pogorszyć układ (dodać opóźnienie, zwiększyć wzmocnienie), zanim zacznie się rozbujać zamiast wracać do równowagi. Mierzy się go w decybelach i stopniach i **jest to liczba, nie odczucie**.

**To jest właściwa metoda szukania tematu i jest zgodna z sekcją 10.D handbooka: luki są opisane, nie trzeba ich zgadywać.**

---

## 3. Twierdzenie projektu

Zapisane w kształcie, który przeżył audyt poprzedniego projektu — **twierdzenie pomiarowe z punktem odniesienia wewnętrznym**, nie twierdzenie o pierwszeństwie.

> **Na jednym i tym samym stanowisku, self-sensing kosztuje X µm szumu położenia, Y N/mm osiągalnej sztywności zamkniętej pętli i Z dB zapasu wzmocnienia względem tego samego stanowiska z czujnikami prądów wirowych na płytce drukowanej. Dominującym ogranicznikiem jest [zmierzone], i [nie] daje się go usunąć przez [zmierzoną interwencję].**

**Cztery własności tego twierdzenia, każda wyprowadzona z konkretnego błędu z przeszłości:**

1. **Nie może zginąć od cudzej publikacji.** Porównanie jest wewnętrzne: mój układ z czujnikami vs mój układ bez czujników. Ktokolwiek opublikuje cokolwiek o self-sensingu, moja liczba dalej jest moją liczbą. To jest dokładnie ten tryb śmierci, który zabił drona, ortezę i STM.
2. **Nie zawiera słowa „pierwszy"** i nie będzie zawierać (K-044).
3. **Każdy wynik jest wynikiem.** Jeżeli self-sensing wypadnie gorzej — to jest wynik i jest zgodny z literaturą. Jeżeli wypadnie lepiej, niż zapowiada literatura — to jest wynik mocniejszy. Jeżeli w ogóle nie zadziała, a powód zostanie zmierzony i wskazany — **to nadal jest wynik**, bo ograniczenie jest opisane jako otwarte.
4. **Wymaga zbudowania przedmiotu.** Nie da się tego zrobić na cudzych danych z laptopa.

---

## 4. Dlaczego to, a nie sześć innych rzeczy

Zabiłem sześciu kandydatów, zanim doszedłem do tego. Pełny rejestr z powodami: **`24_ODRZUCONE_KANDYDATY.md`**. Skrót powodu, dla którego padły: szukałem nieobsadzonego **problemu**, a problemy ważne ekonomicznie są z definicji obsadzone — jeden z kandydatów zginął, bo Fraunhofer IZFP opublikował to samo pięć miesięcy temu i dwa dni przed tą sesją wszedł z tym w próby przemysłowe.

**Ten projekt jest wybrany na kryteriach, które faktycznie punktują, a nie na nowości.**

`[fakt]` Arkusz inżynierski ISEF: Research Problem 10, Design and Methodology 15, Execution 20, Creativity & Potential Impact 20, Presentation 35 (Poster 10 + Interview 25). **Nie ma w nim kryterium „czy to jest nowe względem literatury światowej".** Wytyczne dla jurorów każą oceniać kreatywność przez *research outcomes and analysis*.

`[fakt]` Regulamin Explory §7 pkt 2a: *„Projekt jest innowacyjny, nowatorski **i/lub wnosi dodatkową wartość** w dotychczasowy stan wiedzy"*.

### Punkty kalibracyjne, do których się odnoszę

`[fakt]` **ENBM079 (2026): domowe EEG poniżej 11 USD na kanał, 52% trafności przy zadaniu dwuklasowym — trzecia nagroda ISEF, 1 200 USD.** Projekt bez nowości, z wynikiem ledwie nad rzutem monetą.

`[fakt]` **Przejrzane 21 projektów finałowych Explory 2026: żaden nie łączy zbudowanego sprzętu z rygorem pomiarowym.** Projekty z mentorami akademickimi mają rygor bez urządzenia; projekty inżynierskie mają urządzenie bez pomiarów z niepewnościami.

`[wniosek]` **To jest luka pozycyjna, nie tematyczna, i ten projekt trafia w nią wprost.** Układ regulacji produkuje dane, których nie da się podrobić i których nikt na tych konkursach nie pokazuje: charakterystyki Bodego zamkniętej pętli, krzywe sztywności dynamicznej, odpowiedzi skokowe, zapasy stabilności. Licealista z **własnoręcznie zmierzoną charakterystyką Bodego własnego układu** jest w innej kategorii rozmowy niż licealista z działającym gadżetem.

### Sprawdzone przesłanki wykonalności

| Przesłanka | Status |
|---|---|
| lewitacja z aktywnym sterowaniem jest osiągalna w warunkach dydaktycznych | `[fakt]` MIT publikował tanie zestawy projektowe maglev do kursu sterowania dla studentów III–IV roku; położenie mierzone czujnikiem Halla SS495, zestawy montowane przez studentów |
| tani czujnik położenia o rozdzielczości mikrometrowej istnieje | `[fakt]` czujnik prądów wirowych za **~20 USD, rozdzielczość 7 µm**, zastosowany do sterowania położeniem w jednoosiowym AMB |
| czujnik da się zrobić na płytce drukowanej | `[fakt]` *„Design and Optimisation of a PCB Eddy Current Displacement Sensor"*; osobno: rezonansowy indukcyjny czujnik przemieszczenia dla AMB, oraz czujniki indukcyjne na PCB o rozdzielczości **5 µm** |
| pole ma świeży przegląd z wypisanymi lukami | `[fakt]` przegląd strategii sterowania AMB (2025) oraz przegląd self-sensing AMB (2025) |

`[wniosek]` **Ryzyko „nie da się zbudować" jest niskie, a to jest ryzyko dominujące w całym przedsięwzięciu** — nie ocena jurorska. Poprzedni plan miał `P(cokolwiek działającego)` na poziomie 70–85% przy jednym roku; tutaj poziom zerowy (jedna oś, lewitacja pionowa) jest udokumentowanym ćwiczeniem studenckim, a nie zgadywanką.

---

## 5. Co konkretnie powstaje

### 5.1 Stanowisko

| Zespół | Opis | Rola |
|---|---|---|
| **wirnik** | wał stalowy z pakietem blach, masa rzędu 0,2–0,5 kg | obiekt sterowania |
| **stojan promieniowy** | 4 albo 8 biegunów elektromagnetycznych, sterowane parami różnicowo | człon wykonawczy |
| **czujniki położenia** | **własne płytki z cewkami prądów wirowych** + scalony przetwornik indukcyjności; dwie osie, po dwa kanały | pomiar odniesienia (rok 1) |
| **stopień mocy** | mostki półmostkowe MOSFET z pomiarem prądu, jeden na cewkę | wykonanie |
| **sterownik** | mikrokontroler z szybkim przetwornikiem A/C, pętla rzędu 10–20 kHz | mózg |
| **napęd obrotu** | mały silnik BLDC ze sprzęgłem albo napęd bezstykowy | obroty do badań przy wirowaniu |
| **łożyska zapasowe** | zwykłe łożyska ślizgowe z luzem większym niż szczelina magnetyczna | bezpieczeństwo przy zaniku sterowania |
| **osłona** | poliwęglan | bezpieczeństwo, wymóg regulaminowy obu konkursów |

`[wniosek]` **Projektowanie płytek jest w tym projekcie osią, nie dodatkiem** — czujnik prądów wirowych *jest* płytką drukowaną, a stopień mocy i tor pomiaru prądu to układy analogowe, w których liczy się szum i pasmo. To realizuje ustalenie z sekcji 1 handbooka („PCB do nauczenia się, z prowadzeniem") jako ścieżkę główną projektu, a nie jako koszt wejścia.

### 5.2 Co robi rok drugi

Ten sam wirnik, ten sam stojan, ten sam stopień mocy. **Zmienia się wyłącznie źródło informacji o położeniu:** zamiast płytek czujnikowych — estymacja z tętnienia prądu w cewce wykonawczej.

Dwie ścieżki estymacji do porównania:
1. **z nachylenia tętnienia PWM** — w każdym cyklu modulacji prąd narasta z nachyleniem d*i*/d*t* = *U*/*L*, a *L* zależy od szczeliny. Nie wymaga dodatkowego sygnału
2. **ze wstrzykiwania sygnału wysokoczęstotliwościowego** i demodulacji — wymaga filtrów, czyli wnosi opóźnienie, czyli uderza dokładnie w opisane ograniczenie nr 2

`[wniosek]` **Porównanie tych dwóch ścieżek na jednym stanowisku jest osobną, samodzielną wartością** — literatura opisuje obie, ale zestawienie ich na identycznym sprzęcie z tym samym regulatorem jest tym rodzajem pracy, którego zespoły uczelniane nie robią, bo publikują jedną metodę naraz.

---

## 6. Podział na dwa lata — zgodność z Form 7

`[fakt]` Regulamin ISEF wymaga dla projektu kontynuowanego formularza **Continuation/Research Progression Projects Form (7)**, wykazania, że rok kolejny jest *„new and different"* i pokazuje *„significant progress"*. Wprost zakazane: *„Repetition of a previous study that reflects no changes but simply retests or increases sample size is not permitted."*

**Ten podział spełnia wymóg, bo to są dwa różne pytania, nie jedno pytanie zmierzone dwa razy:**

| | **Rok 1** (Explory 2027 → ISEF 2028) | **Rok 2** (Explory 2028 → ISEF 2029) |
|---|---|---|
| **pytanie** | Jaką charakterystykę da się osiągnąć i zmierzyć na samodzielnie zbudowanym AMB z własnymi czujnikami na PCB? | Ile kosztuje usunięcie czujników i **co konkretnie** jest ogranicznikiem? |
| **aparatura** | stojan + wirnik + płytki czujnikowe + regulator | ten sam sprzęt, tor pomiaru położenia zastąpiony estymatorem |
| **wynik** | komplet charakterystyk: szum położenia, sztywność statyczna i dynamiczna, pasmo, tłumienie zakłóceń, pobór mocy — w funkcji prędkości obrotowej i obciążenia | różnica wszystkich powyższych, plus wskazanie mechanizmu dominującego przez eksperymenty rozdzielające |
| **co jest nowe w roku 2** | — | inna zasada pomiaru, inny estymator, inne pytanie, inne zmienne niezależne |

---

## 7. Kategorie i pozycjonowanie

### 7.1 ISEF: **EBED — Embedded Systems**

`[fakt]` Podkategorie EBED: Circuits, Internet of Things, Microcontrollers, Networking and Data Communications, Optics, **Sensors**, **Signal Processing**. Projekt, którego produktem jest tor pomiarowy, stopień mocy i estymator, należy tam wprost.

`[fakt]` Liczby z bazy abstraktów, rocznik 2026: **EBED 49 projektów, 21 nagrodzonych (43%)**; ENBM 98 projektów, 39 nagrodzonych (40%). Nagród jest proporcjonalnie do zgłoszeń, więc odsetek się nie zmienia — ale **konkuruje się z połową liczby ludzi**.

`[fakt]` Jurorzy są przydzielani według **podkategorii**, nie kategorii. W EBED przy stoisku stanie ktoś, kto potrafi przeczytać charakterystykę Bodego.

`[luka]` **Nie policzyłem kategorii ETSD** (Engineering Technology: Statics and Dynamics), która ma podkategorię *Control Theory* i też jest poprawnym miejscem. Do policzenia w bazie abstraktów przed zgłoszeniem — pozycja w `23_RYZYKA.md`.

### 7.2 Explory: SDG 9, obszar Gospodarka i Bezpieczeństwo

`[fakt]` Finał Explory to **TOP 5 w każdym z czterech obszarów**, a obszar wybiera się samemu przez wskazanie celu SDG przy zgłoszeniu (§4 pkt 4). Konkuruje się więc z ~30 projektami w obszarze, nie z całą stawką 133.

`[fakt]` Skład finału 2026 wg obszarów: „Człowiek i Społeczeństwo" — najgęstszy, tam idą projekty biologiczne z mentorami akademickimi. **„Gospodarka i Bezpieczeństwo" — najsłabszy technicznie**, top 5 stanowiły system nawadniania, zabezpieczenie roweru i beton siarkowy.

**Rekomendacja: SDG 9 — „Innowacyjność, przemysł, infrastruktura".** Uzasadnienie uczciwe, nie naciągane: łożyska magnetyczne eliminują smar i zużycie, czyli usuwają przestoje serwisowe i skażenie olejem z maszyn przepływowych; barierą ich upowszechnienia w **małych** maszynach jest koszt i złożoność podsystemu czujników. Projekt mierzy, ile da się z tego podsystemu wyciąć.

`[wniosek]` Odruchem byłoby SDG 7 (energia, bo brak tarcia) i obszar Klimat i Środowisko. **Nie warto tam iść** — to jest obszar gęstszy, a argument energetyczny jest słabszy niż wygląda: straty w łożyskach tocznych małych maszyn są małe w bilansie całej maszyny. **SDG 9 jest uczciwszy i trafia w słabszy obszar.**

---

## 8. Czego ten projekt nie ma i mówię to teraz

- **Nie ma narracji medycznej ani „ratujemy ludzi".** W rubryce oddziaływania społecznego Explory (10 z 30 punktów w finale) to jest realny koszt wobec projektów o szczepionkach i zanieczyszczeniu wód. Rekompensata jest w dwóch pozostałych rubrykach, gdzie działający przedmiot z pomiarami bije wszystko, co widziałem na listach finałowych.
- **Nie ma nowości względem literatury światowej i nie będzie jej udawał.** Self-sensing AMB to pole z własnym przeglądem z 2025 roku.
- **Nie jest tanie w czasie.** To jest projekt na dwa lata i nie da się go zrobić w pół roku — patrz `21_PLAN_BUDOWY.md`.
- `[luka]` **Nie wiem, czy istnieje opublikowana praca zestawiająca obie ścieżki estymacji na identycznym stanowisku.** Sprawdzenie tego to pierwsza pozycja etapu literaturowego w `21_PLAN_BUDOWY.md` faza 0. **Nie buduję na założeniu, że nie istnieje** — twierdzenie projektu jest tak skonstruowane, że istnienie takiej pracy go nie unieważnia.

---

## 9. Co to zdejmuje z poprzedniego planu

| Ryzyko poprzedniego projektu | Status tutaj |
|---|---|
| **Human Participants, komisja IRB przy szkole, zgody** | **znika w całości** — zero badanych, zero ludzi, zero formularzy 4/5 |
| badanie na sobie i warunek „brak zmiennej ludzkiej" | znika |
| nazwany konkurent z terminem (grupa z PW) | znika; nikt nie może unieważnić pomiaru wewnętrznego |
| „czy artefakt jest w ogóle dość duży, żeby było co kompensować" | znika; sygnał położenia to setki mikrometrów, nie mikrowolty |
| zależność od kupionego sprzętu odniesienia (OpenBCI) | znika; odniesieniem jest własna płytka czujnikowa |
| konkurencja tematyczna na ISEF (22 projekty EEG w 2026) | znika; w EBED 2026 zero projektów o łożyskach magnetycznych `[luka]` — do policzenia |

**Doszło jedno ryzyko, którego wcześniej nie było: wirujący element.** Obsługa w `23_RYZYKA.md` sekcja 5.
