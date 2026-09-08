# 03 — Ściany: co jest fizyczne, a co technologiczne

**Zakres wg sekcji 10.C handbooka.** Dla każdego ograniczenia: kto to stwierdził, na jakiej podstawie, **pod jakimi warunkami** i — najważniejsze — czy jest fizyczne czy technologiczne.

> **AKTUALIZACJA, 15 VIII 2026 wieczorem — jedna z opisanych tu ścian okazała się nie być ścianą.**
>
> Sekcja 3 tego pliku opisywała stratę przepustowości SSVEP przy uchu jako **ograniczenie geometryczne**, czyli fizyczne dla danej formy urządzenia. Podstawą były liczby 6–17 bit/min z prac z 2015 i 2022. Po odczytaniu **Nature Communications 14:4213 (2023)** — urządzenie SpiralE, elektroda douszna o kontakcie konformalnym, **95% na 9 celach i 40-celowy speller SSVEP online bez kalibracji** — to twierdzenie się nie broni. Czynnikiem ograniczającym był **kontakt elektrody**, czyli parametr technologiczny, nie odległość od kory wzrokowej.
>
> Poprawka opisana w `KOREKTY.md` **K-028**, rozbiór w `04_LUKI_ZAPISANE.md` sekcja 1.5. Sekcja 3 poniżej jest **przepisana**, sekcja 7 skorygowana. Reszta pliku pozostaje w mocy.

Rozróżnienie działa tak: **ograniczenie fizyczne** wynika z praw przyrody i zostaje niezależnie od pieniędzy i pomysłowości. **Ograniczenie technologiczne** wynika ze stanu techniki w chwili, w której ktoś je stwierdził, i może się zdezaktualizować — wtedy jest szansą, nie ścianą. Trzecia kategoria, którą dokładam, bo pojawiła się w materiale: **ograniczenie geometryczne** — wynika z tego, gdzie postawiono elektrodę, więc jest fizyczne dla danej formy urządzenia i znika przy zmianie formy. Dla nas jest to ograniczenie fizyczne, bo forma jest wymaganiem twardym.

---

## 1. ŚCIANA FIZYCZNA — czaszka jako filtr przestrzenny

**Twierdzenie:** rozdzielczość przestrzenna EEG skalpowego wynosi około **5–9 cm** i nie da się jej poprawić poprawą sprzętu.

**Podstawa:** niska przewodność kości względem tkanek sąsiednich powoduje rozmycie potencjału; efekt opisany w literaturze przewodnictwa objętościowego i modelowania głowy `[wniosek, streszczenie, kilka źródeł zgodnych]`.

**Warunki, pod którymi to obowiązuje:** czaszka nienaruszona, elektrody na skórze. Przestaje obowiązywać przy ECoG (elektrody pod czaszką) — i to jest dokładnie ta różnica, którą kupuje się operacją.

**Status: FIZYCZNE.** Ani wzmacniacz, ani algorytm tego nie znosi. Metody typu Laplacian przestrzenny czy rekonstrukcja źródeł **wyostrzają obraz statystycznie, nie odzyskują informacji utraconej przy rozmyciu**.

**Konsekwencja dla projektu:** twierdzenie zawierające „rozdzielczość porównywalna z inwazyjnymi" jest nie do obrony. Twierdzenie zawierające „ta forma daje lepszy stosunek sygnału do szumu niż ta inna forma" — jak najbardziej.

## 2. ŚCIANA FIZYCZNA — stosunek amplitudy sygnału do zakłóceń

**Twierdzenie:** EEG ma 10–100 µV, EMG 50 µV – 30 mV, EOG do dziesiątek mV u źródła. Sygnał użyteczny jest o 1–3 rzędy wielkości mniejszy niż zakłócenia biologiczne.

**Status: FIZYCZNE co do stosunku amplitud, TECHNOLOGICZNE co do skutków.**

To rozróżnienie jest sednem kandydata na oś projektu, więc rozpisuję je dokładnie:

| Aspekt | Status | Dlaczego |
|---|---|---|
| mięsień daje sygnał ~×100 większy od mózgu | **fizyczne** | mięsień to większa i lepiej zsynchronizowana masa komórek. Nie zmieni się |
| zakłócenie mięśniowe **musi** zepsuć pomiar | **technologiczne** | zależy od konstrukcji toru i od tego, czy zakłócenie jest mierzone osobno |
| pasma EMG i EEG częściowo się pokrywają (>20 Hz) | **fizyczne** | dlatego samo filtrowanie częstotliwościowe nie wystarcza |
| nasycenie wzmacniacza kasuje sygnał bezpowrotnie | **fizyczne** | po nasyceniu informacji nie ma. Dlatego kompensacja **przed** wzmocnieniem różni się jakościowo od odejmowania po nagraniu |

**To jest właśnie ta wersja projektu, w której parametr jest poza pętlą** — w rozumieniu reguły trzech punktów z sekcji 2.2 handbooka. Nie da się zmniejszyć EMG szczęki. Da się nie dopuścić, żeby zjadło zakres dynamiczny.

## 3. ŚCIANA GEOMETRYCZNA — co słychać przy uchu. **Korekta mojego wcześniejszego rozumowania**

W sekcji 4c `00_PYTANIA_I_LUKI.md` napisałem, że rytmy sensomotoryczne z okolicy ucha „spadają prawdopodobnie do okolic szumu własnego wzmacniacza", i użyłem tego jako głównego argumentu za odczytem dyskretnym. **Ten argument był za mocny.**

**Co znalazłem — teraz w oryginale `[fakt, abstrakt odczytany]`:** Ueda, Ueno, Inoue, Sakiyama, Shiroma, Ishii, Naito, *„Detection of motor-related mu rhythm desynchronization by ear EEG"*, **PLoS One 20(4):e0321107 (2025)**, PMID 40198632. **Dwudziestu zdrowych uczestników.** Porównanie mocy rytmu mu i danych czasowo-częstotliwościowych między spoczynkiem z otwartymi oczami a ruchem prawej ręki. Wynik: istotna różnica mocy rytmu mu oraz istotne stłumienie w paśmie **9–12,5 Hz**.

**Zastrzeżenie, którego wcześniej nie zapisałem, a które zmienia zasięg tego wyniku:** badani wykonywali **rzeczywisty ruch chwytania i puszczania**, nie wyobrażenie ruchu. Desynchronizacja przy ruchu wykonanym jest silniejsza niż przy wyobrażonym `[wniosek, wiedza podręcznikowa]`. **Ta praca nie pokazuje więc, że wyobrażenie ruchu jest wykrywalne z ucha** — pokazuje, że wykrywalny jest ruch. Dla sterowania interfejsem potrzebne jest to pierwsze. Pułap jest zatem niżej, niż sugeruje sam tytuł.

**Poprawna wersja twierdzenia, z warunkami:**

| Sygnał | Dostępność przy uchu | Status |
|---|---|---|
| alfa spoczynkowa (oczy otwarte/zamknięte) | **pewna**, choć amplituda niższa; zmiana mocy 57% w uchu vs 152% na skalpie | fizycznie osiągalne |
| ERD rytmu mu przy **wykonanym** ruchu ręki | **wykrywalna**, n=20, pasmo 9–12,5 Hz | osiągalne |
| ERD rytmu mu przy **wyobrażonym** ruchu | `[luka]` — nie znalazłem pracy pokazującej to z ucha | **nierozstrzygnięte** |
| odpowiedzi kory słuchowej (N1-P2) | **nie wychodzą wiarygodnie** w konfiguracji dousznej, n=19 | patrz sekcja 3.1 |
| SSVEP (kora wzrokowa) | **działa dobrze przy dobrym kontakcie elektrody** — 9 celów 95%, speller 40-celowy online (Nat Commun 2023) | **technologiczne, nie geometryczne** — poprawka K-028 |
| sterowanie ciągłe kursorem z gęstej siatki nad korą ruchową | wymaga elektrod C3/Cz/C4 | **niedostępne w formie zausznej** — geometria |

**Argument, który zostaje w mocy po korekcie:** nie „z ucha nie widać kory ruchowej", tylko **„ciągłe, dwu- lub trójwymiarowe sterowanie wymaga gęstej siatki elektrod nad korą ruchową, a pojedyncza pozycja zauszna nie daje filtracji przestrzennej potrzebnej do rozdzielenia kierunków"**. To jest słabsze twierdzenie i uczciwsze. Ustalenie „odczyt dyskretny" zostaje, bo stoi też na czterech innych nogach (patrz tabela w sekcji 4c `00_PYTANIA_I_LUKI.md`), ale **nie wolno go uzasadniać zdaniem, które padło wcześniej.** Wpis K-014 w `KOREKTY.md`.

### 3.1 Ostrzeżenie, które psuje moją własną rekomendację paradygmatu

W rundzie drugiej rekomendowałem paradygmaty słuchowe jako „te, których generator neuronalny leży blisko ucha". Materiał tego **nie potwierdza jednoznacznie**.

*„Signal-specific performance of in-ear EEG: strengths and limitations"*, **Frontiers in Neuroscience 20:1859327 (2026), PMID 42592227** — Frei, Mainar, Fritz, Chardon, Giroud: **19 zdrowych dorosłych**, w pełni douszny system z elektrodami suchymi o generycznym dopasowaniu, porównanie **równoległe** z 32-kanałowym BioSemi. Wynik `[fakt, abstrakt odczytany]`:

- alfa spoczynkowa przy zamkniętych oczach — **wychodzi pewnie** mimo niższej amplitudy
- **odpowiedź słuchowa N1-P2 — wiarygodna tylko przy uśrednionej referencji skalpowej**; w konfiguracji dousznej wykrywalność komponentu i jego SNR spadają
- alfa podczas słuchania mowy w szumie — istotne odchylenia widoczne w EEG skalpowym, **w minimalnej konfiguracji dousznej nie wykrywane konsekwentnie**

Bliskość anatomiczna kory słuchowej nie wystarcza, bo liczy się też **orientacja dipola i rozstaw elektrod względem niego**, nie sama odległość.

**Status: sprawdzone w oryginale, ustalenie potwierdzone.** Do zapisania dodatkowo: praca była finansowana przez **Logitech S.A.**, który dostarczył badany system douszny i uczestniczył w projektowaniu badania. Dwóch współautorów było wówczas pracownikami tej firmy. **To wzmacnia wiarygodność wyników negatywnych** — producent nie ma interesu w publikowaniu, że jego urządzenie czegoś nie wykrywa. Wynik pozostaje w mocy jako argument przeciw paradygmatom słuchowym w formie dousznej.

## 4. ŚCIANA FIZYCZNA — opóźnienie hemodynamiczne

**Twierdzenie:** fNIRS i fMRI mierzą przepływ krwi, który reaguje na aktywność neuronalną z opóźnieniem **rzędu sekund**.

**Status: FIZYCZNE.** To właściwość układu naczyniowego, nie przyrządu. Skutek: te modalności nie nadają się do szybkiego sterowania, niezależnie od postępu w detektorach.

## 5. ŚCIANY TECHNOLOGICZNE — czyli miejsca, gdzie coś może się ruszyć

Tu leżą szanse. Dla każdej: kto stwierdził, że to problem, i czy jest w zasięgu warsztatu z sekcji 1 handbooka.

| Ograniczenie | Kto je stawia | Status | W zasięgu? |
|---|---|---|---|
| impedancja elektrod suchych ~100× większa niż mokrych (452 kΩ vs 4 kΩ w kanale słuchowym) | pomiary porównawcze elektrod dousznych | **technologiczne** — zależy od materiału i geometrii | **tak**, to materiały i mechanika, czyli warsztat użytkownika |
| ogromny rozrzut impedancji między osobami (odch. > średnia) | te same pomiary | **technologiczne + anatomiczne** | częściowo — indywidualne dopasowanie wkładki |
| zmienność anatomiczna kanału słuchowego | przegląd MDPI Sensors 25:3321 (2025) wymienia to jako wyzwanie otwarte | technologiczne | **tak** — druk 3D pod odlew ucha |
| artefakty ruchowe w formie noszonej | ten sam przegląd | technologiczne | **tak**, to mechanika mocowania i tor analogowy |
| brak standaryzacji referencji w ear-EEG | Frontiers 2026 | **metodologiczne**, nie techniczne | **tak** — i to jest miejsce, gdzie starannie zrobiony pomiar porównawczy ma wartość naukową |
| elektronika ultraniskiej mocy | przeglądy 2025–2026 | technologiczne | częściowo |
| konieczność kalibracji dla każdej osoby i sesji | cała literatura dekodowania | technologiczne, aktywnie atakowane | patrz `07_DEKODOWANIE.md` sekcja 4 |
| „BCI illiteracy": **15–30%** osób nie osiąga kontroli w wyobrażeniu ruchu mimo treningu | Vidaurre, Blankertz i in. | **częściowo fizjologiczne** — dotyczy paradygmatu, nie sprzętu | obejście: inny paradygmat |

**Uwaga do ostatniego wiersza, ważna dla planu eksperymentalnego:** skoro 15–30% osób nie uzyskuje kontroli w wyobrażeniu ruchu `[wniosek, streszczenie, dwa źródła zgodne co do przedziału]`, to przy badaniu na grupie kilku osób **jedna osoba niedziałająca jest zdarzeniem oczekiwanym, nie awarią**. Musi być wpisana w plan i w interpretację wyników z góry, inaczej wygląda jak ukrywanie porażki.

---

## 6. Zadanie 4d nr 8 — jak zmierzyć szum wzmacniacza bez oscyloskopu

Użytkownik nie ma sprzętu pomiarowego. Połowa twierdzenia o własnym torze analogowym to **dowód**, że jest cichy. Metoda, która nie wymaga zakupów:

**Metoda podstawowa — zwarte wejście.** Standard branżowy `[wniosek, kilka źródeł zgodnych]`: zewrzeć wejścia wzmacniacza, zmierzyć napięcie szumu na wyjściu, podzielić przez wzmocnienie. Wynik to szum sprowadzony na wejście. Zwarcie wejść usuwa okablowanie jako źródło zakłóceń, więc pomiar jest czystszy.

**Czym mierzyć bez oscyloskopu:** rolę przetwornika pełni **wejście liniowe karty dźwiękowej** (16–24 bity, pasmo do ~20 kHz, znacznie niższy szum własny niż tani oscyloskop w zakresie mikrowoltów). Analiza widmowa programowo. To standardowa praktyka w pomiarach audio i w społeczności DIY biosygnałów `[wniosek]`.

**Kalibracja skali — bez tego liczby nie znaczą nic.** Dzielnik rezystorowy z wyjścia słuchawkowego komputera: sygnał sinusoidalny o znanej amplitudzie (np. 100 mV) podzielony 10 000:1 daje 10 µV o znanej wartości. **Dwie pułapki, które trzeba obsłużyć, inaczej pomiar jest bezwartościowy:**
1. rezystory dzielnika same generują szum termiczny (Johnsona) — przy dużych rezystancjach może przewyższyć mierzony sygnał. Dzielnik projektować na **niską rezystancję od strony wyjściowej**
2. wyjście słuchawkowe ma własny szum i zniekształcenia — trzeba je zmierzyć osobno i odjąć

**Metoda kontrolna — szum rezystora jako wzorzec.** Szum termiczny rezystora daje się policzyć ze wzoru na napięcie szumu Johnsona (znany ze szkolnej fizyki statystycznej w wersji uproszczonej: zależy od temperatury, rezystancji i pasma). Mierząc szum wzmacniacza z kilkoma różnymi rezystorami na wejściu, dostaje się **niezależne sprawdzenie kalibracji** — bo wartość teoretyczna jest znana z góry. To jest ta druga i trzecia weryfikacja, której wymaga sekcja 13 handbooka, uzyskana bez kupowania czegokolwiek.

**Czego ta metoda nie da:** pomiaru CMRR i odporności na zakłócenia sieciowe w sposób akceptowalny dla laboratorium. To zostaje na wizytę w firmie brata — zasób jednorazowy, rezerwacja po VI 2027 zgodnie z sekcją 5.4 handbooka.

---

## 7. Podsumowanie — czego nie wolno obiecywać, i co zostaje

**Nie do obrony przy formie zausznej:**
- rozdzielczość przestrzenna porównywalna z rozwiązaniami inwazyjnymi — **ściana fizyczna**, sekcja 1
- sterowanie ciągłe, wielowymiarowe, z jednej pozycji zausznej — brak filtracji przestrzennej, sekcja 3
- działanie u 100% badanych w paradygmacie wyobrażenia ruchu — sekcja 5
- odpowiedzi kory słuchowej jako podstawa sterowania — sekcja 3.1, n=19, potwierdzone

**Pozycja wycofana z tej listy, `KOREKTY.md` K-028:** „ITR wyższy niż wielokanałowa czapka przy tym samym paradygmacie" **nie jest ścianą geometryczną**. Praca z Nature Communications 2023 pokazuje speller SSVEP 40-celowy online z kanału słuchowego. Ograniczeniem był kontakt elektrody, czyli parametr technologiczny — a to jest warstwa 1 i 2 z sekcji 9.4 handbooka, czyli **warsztat użytkownika**. Twierdzenie przepustowościowe wraca do rozważenia w etapie 2 i **nie wolno go odrzucać powołując się na ten plik.**

**Zostaje do wzięcia, w kolejności atrakcyjności dla tego projektu:**
1. **zakres dynamiczny toru w obecności artefaktu szczękowego przy uchu** — ograniczenie technologiczne, udokumentowane w oryginale jako **gorsze w uchu niż na skalpie** (Kappel 2017, n=9, największe w paśmie gamma), mieszczące się w najmocniejszej umiejętności użytkownika. **Uwaga: dotyczy szczęki, nie mrugnięcia — K-026**
2. **jakość i powtarzalność kontaktu elektroda–skóra** — po pracy SpiralE to jest udokumentowany czynnik decydujący o przepustowości, a nie drobiazg wykonawczy. Awansowało z pozycji 2 na najmocniejszą przesłankę w całym pliku
3. **impedancja i stabilność elektrod suchych w formie zausznej** — materiały i mechanika
4. **standaryzacja referencji w ear-EEG** — luka metodologiczna wskazana wprost przez Frontiers 2026, tania, wymaga staranności zamiast sprzętu
5. **metryki użytkowe zamiast przepustowościowych** — pole opisane jako ważne, a rzadko mierzone
