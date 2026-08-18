# Concept of Operations (ConOps) — Modularny dron inspekcyjno-poszukiwawczo-ratowniczy

*Wersja próbna. Projekt konkursowy (Explory, El-Robo-Mech), horyzont: zgłoszenie w 2-3 klasie liceum.*

*Ostatnia aktualizacja: 16 lipca 2026 — dodano Etap 2.5, opcjonalny i warunkowy upgrade modułu akustycznego: lekka sieć neuronowa do separacji sygnału docelowego od szumu silnika/otoczenia, trenowana metodą progresywnie rosnącej trudności na realnych nagraniach z Etapów 1–2 (augmentowanych realnymi nagraniami szumu, nie czysto syntetycznym miksem), uruchamiana na tym samym Raspberry Pi co reszta pipeline'u, bez dodatkowego modułu sprzętowego. Warunek wejścia: zakończony i zbenchmarkowany Etap 2. Cel: gotowe przed zgłoszeniem do Explory, w razie potrzeby dokończone jako rozszerzenie na ISEF. Zmiany w sekcjach 2, 7, 9, 10.

Poprzednia aktualizacja: 15 lipca 2026 — moduł akustyczny doprecyzowany po trzeciej rundzie przeglądu literatury (pięć dodatkowych źródeł, w tym DroneAudioset NeurIPS 2025); dodano battery bay jako osobny standard szybkiej wymiany zasilania (XT60/XT90 sztywno montowane w układzie blind-mate, ergonomia jak w bateriach DJI, bez custom styków nożowych). Zmiany: źródłowanie progu SNR/F1 (cztery przedziały zamiast dwóch), źródłowanie liczby 5–12 dB, dodane odniesienie do architektury Sky-Ear, explicit protokół testu ROI-beamforming w Etapie 1, wzmocnione uzasadnienie testu pozycji mikrofonu w Etapie 2, doprecyzowana ocena dowodów dla gwizdka, nowa sekcja battery bay w sekcji 2, z odpowiadającymi zmianami w sekcjach 8, 9, 10.*

## 1. Cel i zakres dokumentu

Dokument opisuje koncepcję działania (ConOps) modularnej platformy bezzałogowej łączącej stały tor detekcji (wizja + termowizja) z wymiennym zestawem czujników misji, sterowanej autonomicznym automatem stanów działającym w zasięgu wzroku operatora (VLOS). System ma pełnić dwie role operacyjne na jednej platformie sprzętowej: wsparcie poszukiwawczo-ratownicze (warstwa wiarygodności/wartości społecznej) oraz ochronę obiektów prywatnych (warstwa komercyjna).

## 2. Przegląd systemu

**Platforma**: multirotor klasy 7", rama częściowo r-PETG CF, ramiona składane.

**Kontroler lotu**: klasa Pixhawk/ArduPilot, zamontowany na stałe, centralnie — nie w module wymiennym.

**Sensor stały (nie wymienny)**: Luxonis OAK-D Lite + detekcja on-device (YOLOv8/v11) + autorski pipeline fuzji termo-RGB. Zamontowany trwale na płatowcu, ponieważ automat stanów wymaga jego dostępności w każdym locie niezależnie od zamontowanego modułu misji.

**Payload bay (standard złączy wymiennych, sensory misji)**: magnesy (samocentrowanie) + piny pogo (prąd/dane) + kołki pozycjonujące + gniazdo stożkowe + wtórny zatrzask + uszczelki. Auto-identyfikacja modułu przez chip EEPROM (I2C). Cel: wymiana <30 s bez narzędzi, mocowanie blisko środka masy. Zaprojektowany pod niskoprądowe moduły misji (rząd pojedynczych A) — niewystarczający elektrycznie dla zasilania platformy (patrz battery bay poniżej).

**Battery bay (standard szybkiej wymiany zasilania)**: fizycznie i elektrycznie odrębny od payload bay — inna klasa prądowa wymaga innego doboru komponentów niż piny pogo. Dla 7-calowca w konfiguracji 6S szczytowy pobór podczas dynamicznych manewrów sięga rzędu 80–120 A łącznie (4 silniki), przelotowo 15–25 A. Elektrycznie: sprawdzone złącza bagnetowe (XT60/XT90), nie custom styki nożowe — zamontowane sztywno (nie na swobodnym przewodzie) po obu stronach, tak by wsunięcie baterii na prowadnicach automatycznie domykało połączenie (blind-mate), bez ręcznego wpinania wtyczki. To ta sama zasada ergonomiczna co w bateriach DJI, zrealizowana tańszym i powszechnie dostępnym złączem — cel: brak widocznych, luźnych przewodów przy wymianie, cała trasa kabla biegnie wewnątrz tacki/ramy między złączem a ESC. Mechanicznie: bateria w sztywnej tacce (druk 3D lub laminat) z prowadnicami wymuszającymi jedyną poprawną orientację wsunięcia, dwupunktowy zatrzask mechaniczny wymagający świadomego działania do zwolnienia — masa pakietu i przeciążenia w locie SAR wykluczają poleganie wyłącznie na sile magnetycznej. Tolerancje montażu wymagają dopracowania (przesunięcie rzędu mm może uniemożliwić domknięcie złącza) — warto zaprojektować niewielki luz/sprężynowanie w jednej osi mocowania jako margines na niedoskonałości druku/montażu. Osobna magistrala danych (UART/I2C), prowadzona tym samym mechanizmem sztywnego montażu, do ciągłej telemetrii BMS (napięcie ogniw, temperatura, prąd) — inny wymóg niż statyczny EEPROM auto-ID modułów misji, bo tu dane muszą płynąć stale, nie tylko przy starcie. Umiejscowienie gniazda niezależne od tego, który moduł misji jest aktualnie zamontowany w payload bay, i możliwie blisko środka masy platformy, bo bateria pozostaje pojedynczym najcięższym komponentem (typowo 30–40% masy startowej). Interlock programowy: FC blokuje możliwość zwolnienia zatrzasku (lub przynajmniej wyraźnie ostrzega) gdy system jest uzbrojony lub w locie.

**Moduły wymienne**:

- **Akustyczny (pasywny)** — architektura trójwarstwowa, kolejność wdrożenia = kolejność rosnącej złożoności:
  1. *Front-end RPM/BPF-informed*: tablica mikrofonów MEMS (docelowo ICS-43434 lub równoważne) na wysięgniku 300–600 mm pod kadłubem, skierowana ku ziemi — pozycja najlepiej potwierdzona w literaturze jako kompromis między korelacją z referencją RPM a ekspozycją na strumień zaśmigłowy. Filtracja tonalnej składowej szumu silnika z telemetrii DSHOT (ESC), osłona przeciwwietrzna (redukcja szumu wiatru, dominującego <300 Hz).
  2. *Selektywny beamforming sterowany ROI*: nasłuch ograniczony do sektora przestrzennego wskazanego przez sensor stały (fuzja termo-RGB), zamiast pełnego skanowania 360°. Dwa niezależne mechanizmy korzyści: (a) redukcja ego-noise własnego drona przez ograniczenie apertury poszukiwań, (b) odrzucenie zakłóceń od innych obecnych ludzi (ratownicy, chaos otoczenia) — realny problem w gruzowisku/akcji ratunkowej, nie tylko szum silnika.
  3. *Sekwencyjna, wieloprzelotowa fuzja namiarów*: dron zbiera namiary DOA z kolejnych, niekoniecznie tożsamych zdarzeń impulsywnych podczas kilku przelotów/zmian pozycji w okolicy ROI, zakładając nieruchomość źródła (ranna/uwięziona ofiara), i triangułuje jego pozycję. Zgodność wytriangulowanej pozycji z ROI termicznym służy jako bramka pewności odróżniająca ofiarę od innych osób w terenie. Adaptacja metod bearing-only tracking i acoustic SLAM z robotyki mobilnej — oryginalny wkład to integracja z ROI termicznym i telemetrią RPM na tanim, hobbystycznym 7-calowcu, nie własny wynalazek podstaw matematycznych.

  *Cel sygnałowy*: dźwięk impulsywny generowany przez człowieka bez sprzętu (krzyk, wołanie, klaskanie, pukanie). Świadomie nie: mowa ciągła (zbyt trudna przy realnym SNR wg literatury — patrz sekcja 6), ani gwizdek ratunkowy (odrzucony — patrz sekcja 6).

  *Upgrade opcjonalny (Etap 2.5)*: lekka sieć neuronowa trenowana krzywą rosnącej trudności (najpierw czysty sygnał, potem z szumem silnika, potem z szumem otoczenia) na realnych nagraniach z Etapu 1–2, augmentowanych metodą nakładania realnych nagrań szumu silnika/otoczenia na realne nagrania sygnału docelowego — analogicznie do publikowanych protokołów augmentacji audio w robotyce (nakładanie nagranych dźwięków otoczenia i silnika na nagrania demonstracji). Uruchamiana na tym samym Raspberry Pi co reszta pipeline'u z Etapu 1 — bez dodatkowego modułu sprzętowego. Warunkowe względem harmonogramu: wymaga ukończonego i zbenchmarkowanego Etapu 1–2 (działający dron, własne nagrania z pozycji docelowej mikrofonu), więc realistycznie możliwe dopiero po domknięciu rdzenia. Cel nie jest wcześniej deklarowaną liczbą poprawy — wynik ablacji (z siecią / bez sieci, na tym samym zbiorze testowym co reszta Etapu 0–2) raportowany taki, jaki faktycznie wyjdzie. Nowatorstwo tego elementu nie leży w samej separacji szumu silnika od sygnału ofiary — to zjawisko jest już ilościowo udokumentowane w literaturze (rotor-aware NCM: do ~28 dB; multichannel Wiener + GMM: 5–12 dB) — tylko w zmierzonym działaniu tej separacji na tanim sprzęcie pokładowym, zintegrowanym z ROI-beamformingiem, na własnej platformie.

  *Upgrade opcjonalny (Etap 3)*: rotor-aware noise covariance matrix estimation (do ~20–28 dB redukcji szumu wirników w nagraniach in-flight) — bardziej wymagający implementacyjnie niż prosty filtr referencyjny (wielokanałowa estymacja PSD), nie pierwszy wybór.

  *Nowatorstwo*: potwierdzone trzykrotnie, niezależnymi rundami przeglądu literatury — brak opublikowanego pipeline'u łączącego RPM-informed front-end + ROI-constrained beamforming + sekwencyjną fuzję namiarów na małej platformie UAV. Poszczególne elementy istnieją osobno i są dobrze udokumentowane; integracja i benchmark na tanim sprzęcie hobbystycznym są oryginalnym wkładem. Najbliższym istniejącym wzorcem dwustopniowej architektury (lekka detekcja → pełna lokalizacja) jest Sky-Ear (Hong i wsp., 2026), który dzieli pipeline na etapy Sentinel (detekcja dźwięku ofiary) i Responder (pełna wielokanałowa lokalizacja) dla oszczędności energii i obliczeń — koncepcyjnie zbieżne z podziałem na warstwy 1–2 vs. warstwę 3 poniżej, ale nieprzetestowane na małej platformie hobbystycznej.

  W środowisku leśnym wymaga dodatkowej warstwy adaptacyjnego progu szumu otoczenia (wiatr, fauna) obok filtracji RPM.

- **Sejsmiczny (eksploracyjny, drugorzędny)**: sonda/geofon sprzęgana z podłożem po lądowaniu (wzorzec: landing-leg-as-spike, za ASAD/seismic drone), rozważana jako uzupełnienie dla scenariusza B (gruzowisko), gdzie dźwięk powietrzny silnie się tłumi. Literatura nie dokumentuje pełnego łańcucha UAV-ląduje→sprzęga sondę→wykrywa pukanie ofiary — to kierunek na Etap 2/3, nie flagowa zdolność Etapu 1. Potencjalna przewaga koncepcyjna nad obecną praktyką naziemną (geostereophony): separacja przestrzenna zamiast wymogu całkowitej ciszy całego zespołu ratowniczego podczas nasłuchu.

- PM2.5 / jakość powietrza.

- Roadmap (niebudowane w tym cyklu): bioakustyka szkodników (rolnictwo), bioakustyka dzikiej przyrody/wykrywanie nielegalnej wycinki (środowisko).

**Rozszerzenie sensora stałego — Airborne Optical Sectioning (AOS)**: dla środowisk z gęstym baldachimem leśnym automat stanów wyzwala autonomiczny przelot integrujący wiele ujęć termowizyjnych z różnych pozycji, komputerowo redukując okluzję listowia. Adaptacja opublikowanej metody (Johannes Kepler University), nie własny wynalazek.

## 3. Interesariusze

| Rola | Podmiot | Charakter relacji |
|---|---|---|
| Walidacja polowa / wiarygodność | Grupy Poszukiwawczo-Ratownicze przy OSP, Centrum Poszukiwań Osób Zaginionych KGP | Partnerstwo edukacyjne, ćwiczenia szkoleniowe — nie rynek komercyjny |
| Komercjalizacja (docelowo) | Operatorzy ochrony obiektów prywatnych (segment: mniejsi gracze wobec Seris/Securitas/IRONSKY) | Licencjonowanie IP jako najbardziej dostępna ścieżka startowa |
| Mentor/opiekun merytoryczny | Nauczyciel fizyki (I LO Białystok) | Kanał instytucjonalny dla kontaktów zewnętrznych, w tym z partnerami walidacyjnymi |
| Konkursy | Explory (primary), El-Robo-Mech (lokalny, Politechnika Białostocka), ISEF (stretch, zależny od ścieżki afiliacji) | — |

## 4. Scenariusze operacyjne

### Scenariusz A — poszukiwanie osoby zaginionej, teren otwarty/leśny (scenariusz podstawowy)
1. Start w trybie szerokiego skanu: sensor stały (termo-RGB) przeszukuje obszar wg wzorca siatki.
2. Anomalia termalna/wizualna → automat stanów przełącza w tryb bliskiej inspekcji.
3. Jeśli baldachim leśny ogranicza linię widzenia: autonomiczny przelot AOS integrujący wiele ujęć.
4. Moduł akustyczny (jeśli zamontowany) potwierdza sygnał życia: selektywny beamforming ograniczony do sektora ROI wykrywa zdarzenie impulsywne (wołanie, klaśnięcie, pukanie); sekwencyjna fuzja namiarów z kolejnych przelotów podnosi pewność, że źródło pokrywa się z wykrytym kandydatem, odróżniając go od innych osób obecnych w terenie (np. ratowników).
5. Pozycja przekazywana zespołowi naziemnemu.

### Scenariusz B — konstrukcja zawalona / gruzowisko (scenariusz rozszerzony, mniej dostępny do walidacji)
Jak wyżej, z tą różnicą, że okluzja jest nieregularna (gruz, pył) zamiast systematyczna (baldachim) — AOS mniej istotny, fuzja termo-RGB i akustyka pozostają głównymi sensorami. Dźwięk powietrzny jest tu silniej tłumiony niż w terenie otwartym (spójne z literaturą USAR) — moduł sejsmiczny (eksploracyjny) jako uzupełnienie po lądowaniu w pobliżu ROI.

### Scenariusz C — ochrona obiektu prywatnego (nocny patrol autonomiczny)
1. Autonomiczny patrol obwodowy obiektu (fabryka, magazyn, plac budowy).
2. Anomalia akustyczna (wybicie szyby, cięcie, manipulacja) lub termalna (intruz, przegrzewający się sprzęt) → automat stanów przełącza w tryb bliskiej inspekcji.
3. Alarm do operatora/centrum monitoringu z potwierdzeniem wieloczujnikowym (redukcja liczby fałszywych alarmów względem pojedynczego sensora).

## 5. Tryby pracy (automat stanów)

Wszystkie tryby operują w zasięgu wzroku operatora (VLOS). Pełna autonomia BVLOS jest świadomie wyłączona z zakresu — niedostępna prawnie dla operatora niepełnoletniego bez autoryzacji ULC, i nie jest wymagana do żadnego z opisanych scenariuszy.

| Stan | Wyzwalacz wejścia | Sensor wiodący |
|---|---|---|
| Szeroki skan | Start misji | Fuzja termo-RGB |
| Inspekcja bliska — teren otwarty | Anomalia wykryta | Fuzja termo-RGB + akustyka (selektywny beamforming na ROI) |
| Inspekcja bliska — baldachim leśny | Anomalia wykryta + niska pewność sygnału termalnego | AOS + akustyka (selektywny beamforming na ROI) |
| Weryfikacja wieloprzelotowa | Zdarzenie akustyczne impulsywne wykryte w sektorze ROI | Sekwencyjna fuzja namiarów (repozycjonowanie + DOA + IMU) |
| Potwierdzenie/alarm | Sygnał potwierdzony wieloma modalnościami | Zgłoszenie do operatora |

## 6. Świadomie poza zakresem

- **Antena z metalu ciekłego (galinstan)** — zbyt konceptowa, łatwo zastępowalna.
- **Napęd alternatywny (EAD/jonowy, cyklokoptery)** — fizycznie nierealny do latania w dostępnym budżecie czasu.
- **Pełna autonomia BVLOS** — nielegalna do zademonstrowania przez operatora niepełnoletniego.
- **Sonar aktywny jako główny sensor detekcji** — gorszy zasięg, gorsza efektywność energetyczna względem nasłuchu pasywnego; nie penetruje materiału, tylko geometrię powierzchni. Rozważany wyłącznie jako drugorzędna funkcja nawigacyjna (unikanie kolizji w pyle/ciemności), nie jako wykrywacz ofiar.
- **Zastosowanie graniczne (ochrona granicy polsko-białoruskiej)** — wykluczone trwale. Powody: (a) aktywna, prawnie wiążąca strefa ograniczonego ruchu lotniczego wzdłuż granicy (EP R130, cyklicznie odnawiana), praktycznie uniemożliwiająca legalny lot; (b) zamówienia dla służb granicznych to zamknięty procurement obronny, nie rynek dostępny dla licealisty; (c) udokumentowany, poważny wzorzec szkody (wychłodzenie osób ukrywających się przed wykryciem termicznym, krytyka praktyk nadzoru w tym rejonie) czyni ulepszenia w kierunku przełamywania kontrmiar termicznych i wykrywania grup nieakceptowalnymi niezależnie od deklarowanego odbiorcy końcowego.
- **Rynek transportu/logistyki jako flagowa innowacja** — po weryfikacji trzy kolejne próby (akustyczne wykrywanie samolotów, precyzyjne lądowanie GPS-denied, autonomiczna wymiana ładunku na stacji dokującej) okazały się już skomercjalizowane lub opatentowane. Transport pozostaje w portfolio jako integracja znanych technik, nie jako nośnik nowości.
- **Gwizdek ratunkowy jako flagowy cel akustyczny** — rozważony i odrzucony. Techniczne uzasadnienie (pasmo 2–4 kHz powyżej dominującej energii szumu rotora) było mocne, ale zależność od wyposażenia ofiary czyniłaby flagową zdolność systemu zbyt sytuacyjną wobec faktycznego celu (wykrywanie ludzi, nie tylko osób z gwizdkiem). Dowody na skuteczność tego pasma są mocniejsze niż pierwotnie sformułowano — norma ISO 12402-8:2020 wymaga >100 dB(A) @ 5 m przy częstotliwości 2±1 kHz, a komercyjne gwizdki (np. Fox 40) osiągają 115–120 dB — co nie zmienia decyzji o odrzuceniu jako celu flagowego, ale wzmacnia zasadność utrzymania go jako drugorzędnego/opcjonalnego celu wykrywania w Etapie 3.
- **Mowa ciągła jako podstawowy cel sygnałowy** — rozważona i odrzucona na obecnym etapie. Literatura (DREGON, DroneAudioset, FKIE) konsekwentnie pokazuje, że lokalizacja mowy pozostaje trudna przy realnym SNR drona (F1 spada do 0,26–0,31 poniżej −30 dB nawet z sieciami neuronowymi); dźwięk impulsywny jest łatwiejszym, lepiej udokumentowanym celem. Mowa ciągła pozostaje jako stretch goal w Etapie 3, nie cel podstawowy.

## 7. Plan walidacji i metryki

**Ścieżka wdrożeniowa modułu akustycznego** (kolejność potwierdzona niezależnie dwoma rundami przeglądu literatury):

1. *Etap 0 — walidacja offline, koszt zerowy*: implementacja i test filtra RPM-referencyjnego oraz detektora zdarzeń impulsywnych na gotowych zbiorach z ground truth RPM (DREGON) i najbogatszym zbiorze SAR-specyficznym (DroneAudioset, NeurIPS 2025). Cel: replikacja rzędu 5–12 dB poprawy SNR znanej z literatury (Wang i wsp., 2024, multichannel Wiener + GMM post-filtering, *Applied Acoustics* — poprawa ~5/8/12 dB przy warunkach wejściowych 0/−5/−10 dB), zanim zakupiony zostanie jakikolwiek sprzęt.
2. *Etap 1 — tani sprzęt, bench test*: tablica MEMS (ICS-43434 lub ReSpeaker) + Raspberry Pi + ODAS; test na uziemionym dronie z kręcącymi się śmigłami i głośnikiem odtwarzającym wzorcowy sygnał (krzyk/klaśnięcie/pukanie) w znanych kątach i dystansach. Równolegle, test warstwy 2 (selektywny beamforming sterowany ROI) wg protokołu z literatury (Li i wsp., 2025; Grondin i wsp., 2020; Ortigoso-Narro i wsp., 2025): stacjonarny demonstrator łączący sensor termo-RGB z tablicą 4–8 MEMS, wspólna kalibracja extrinsic, steering na bbox wykrytego człowieka; metryki ograniczone do (a) zysku SIR/SNR po zawężeniu sektora, (b) odsetka poprawnych triggerów akustycznych w obrębie ROI, (c) błędu azymutu namiaru względem środka ROI.
3. *Etap 2 — oryginalny wkład pomiarowy*: własny pomiar różnicy SNR między pozycją mikrofonu nad/pod/na zawieszeniu na WŁASNYM dronie — literatura potwierdza kierunek (nad = lepiej), ale nie podaje wartości liczbowej specyficznej dla konkretnej platformy. To zaostrzone w 2025 r. przez DroneAudioset (Gupta i wsp., NeurIPS 2025), który pokazuje, że pozycja pod dronem bez odpowiedniego ekranowania/dystansu daje wyraźnie gorszy SI-SDR z powodu bezpośredniej ekspozycji na strumień zaśmigłowy — podnosi to wagę tego testu, nie zmienia obecnej decyzji projektowej (wysięgnik pod kadłubem pozostaje punktem startowym do weryfikacji, nie założeniem). Równolegle: własna krzywa błąd-dystans dla dźwięku impulsywnego generowanego przez człowieka (dostępna literatura ma taką krzywą tylko dla petard/eksplozji, nie dla krzyku).
4. *Etap 2.5 — opcjonalny, warunkowy upgrade*: trening lekkiej sieci klasyfikującej/maskującej na spektrogramie, metodą progresywnie rosnącej trudności, na nagraniach z Etapu 1–2 augmentowanych realnymi nagraniami szumu (nie na czysto syntetycznym miksie). Trening odbywa się w tle, równolegle do pozostałych prac, na tym samym Raspberry Pi co reszta pipeline'u — bez dodatkowego modułu sprzętowego. Ewaluacja obowiązkowo na tym samym zbiorze testowym co baseline klasyczny z Etapu 0–2 — inaczej porównanie nie ma wartości dowodowej. Warunek wejścia: zakończony i zbenchmarkowany Etap 2. Jeśli nie uda się dokończyć przed zgłoszeniem do Explory, wynik pozostaje poza materiałem zgłoszeniowym i jest dopracowywany do ISEF jako rozszerzenie, nie zastąpienie rdzenia.
5. *Etap 3 — jeśli czas pozwoli*: rotor-aware NCM (do ~28 dB) i/lub sekwencyjna fuzja namiarów pod realnym ego-noise drona, jako upgrade nad działającym rdzeniem z Etapów 0–2.

**Progi decyzyjne** (DroneAudioset, Gupta i wsp., 2025 — detekcja dźwięków wokalnych wg przedziału SNR): > −10 dB → F1 ≈ 0,87, wysoka pewność detekcji; −20 do −10 dB → F1 ≈ 0,84, nadal dobra; −30 do −20 dB → F1 spada do ≈ 0,42, wyraźna degradacja; < −30 dB → F1 ≈ 0,26–0,31, nawet zaawansowane metody zawodzą — priorytetem staje się zmiana pozycji mikrofonu, nie dalsza praca nad algorytmem.

**Zasięg detekcji — jawnie nieustalony.** Dostępna literatura podaje dobre krzywe błąd-dystans dla źródeł o wysokiej energii (petardy, eksplozje — do ok. 150 m), ale żadna nie dotyczy bezpośrednio krzyku/wołania z drona w warunkach terenowych. Nie zakładać konkretnej liczby przed własnym pomiarem w Etapie 1–2.

**Zbierane**: czas do wykrycia sygnału vs. standardowe przeszukanie wzrokowo-termalne; dokładność namiaru kierunkowego (błąd w stopniach); poprawa SNR (dB) po filtracji RPM-referencyjnej; niepewność pozycji po sekwencyjnej fuzji namiarów (m), w funkcji liczby przelotów i baseline'u; zasięg wykrycia w metrach w warunkach ćwiczeń; wskaźnik fałszywych alarmów/pominięć w scenariuszu kontrolowanym; pokrycie obszaru na jednostkę czasu; ustrukturyzowana opinia ratowników (użyteczność, zaufanie, gotowość ponownego użycia).

**Wykluczone z raportowania**: jakikolwiek wskaźnik "% uratowanych osób", statystyki przeżywalności, ekstrapolacje na liczbę potencjalnie uratowanych istnień. Każda liczba opisywana jawnie jako pochodząca z warunków ćwiczeń szkoleniowych, nie akcji ratunkowej.

## 8. Ograniczenia i założenia

- Operator wymaga certyfikacji dron. kategorii otwartej (min. A1/A3) do samodzielnych lotów podczas ćwiczeń z partnerem.
- System działa wyłącznie w zasięgu wzroku operatora (VLOS).
- Budżet masy/mocy platformy 7" wymaga przeliczenia po doliczeniu wszystkich modułów (fuzja + akustyka + AOS + PM2.5) oraz mechanizmu battery bay (styki nożowe + zatrzask ważą więcej niż prosty pasek + złącze XT60) — możliwe, że wymagana będzie rama 8–10".
- Kontakt z partnerami instytucjonalnymi (OSP/GPR, uczelnia) prowadzony przez kanał szkolny/mentora, nie samodzielnie przez niepełnoletniego operatora.
- Moduł akustyczny nie rozpoznaje tożsamości/roli mówiącego (ofiara vs ratownik) przez analizę głosu — odróżnienie odbywa się wyłącznie przez zgodność przestrzenną z ROI termicznym, nie przez klasyfikację akustyczną mówcy.
- Sekwencyjna triangulacja wieloprzelotowa zakłada nieruchomość źródła dźwięku między przelotami — założenie zasadne dla rannej/uwięzionej ofiary, nieprawdziwe dla źródła w ruchu.

## 9. Ryzyka

| Ryzyko | Wpływ | Mitygacja |
|---|---|---|
| Eksplozja zakresu (zbyt wiele modułów naraz) | Wysoki — żaden element nie zostanie w pełni zbenchmarkowany | Priorytet: rdzeń modułowy + jeden flagowy moduł w pełni dopracowany, reszta jako roadmap |
| Trudność techniczna modułu akustycznego | Wysoki, ale obniżony przez etapowość — architektura trójwarstwowa gwarantuje częściową, samodzielnie działającą zdolność nawet jeśli zaawansowane etapy się nie domkną | Wczesne prototypowanie od Etapu 0 (offline, zero kosztu), jawne raportowanie częściowych wyników jeśli benchmark się nie domknie na czas |
| Brak zweryfikowanego zasięgu detekcji dla docelowego sygnału (krzyk/wołanie) | Średni — dostępne dane dotyczą innych źródeł (petardy, gwizdek), nie bezpośrednio celu systemu | Pomiar własny w Etapie 1–2 jako priorytet, nie założenie na podstawie cudzych wyników |
| Sekwencyjna triangulacja wieloprzelotowa niezweryfikowana pod silnym ego-noise 7-calowca | Średni — adaptacja metody (acoustic SLAM) z warunków o nieznanym poziomie szumu | Traktować jako warstwę podnoszącą pewność, nie gwarantowaną zdolność; raportować jako taką przed jury |
| Etap 2.5 trenowany głównie na miksach syntetycznych zamiast realnych nagraniach z własnej platformy | Średni — sieć nauczy się cech symulatora, nie realnego szumu strugi zaśmigłowej przy mikrofonie | Nagrania bazowe wyłącznie z Etapu 1–2 (własna platforma, docelowa pozycja mikrofonu); symulator tylko do skalowania ilości, nie jako jedyne źródło danych treningowych |
| Zależność walidacji polowej od dostępności partnera instytucjonalnego | Średni | Plan B: udział jako obserwator/uczestnik istniejących manewrów (np. cykl "Nadzieja") zamiast organizowania własnego ćwiczenia |
| Ambicje komercyjne/patentowe jako rozproszenie uwagi | Niski przy świadomym sekwencjonowaniu | Traktowane jako nadbudowa na działającym rdzeniu, nie cel równoległy |
| Precyzja mechaniczna blind-mate złącza battery bay (XT60/XT90 sztywno montowane) | Średni — złe wykonanie prowadnic/tolerancji uniemożliwia domknięcie złącza lub daje słaby styk (przegrzanie); to problem precyzji mocowania sprawdzonego złącza, nie projektowania nowego | Iteracyjne prototypowanie tacki i prowadnic w druku 3D, test wielokrotnego wsuwania przed pierwszym lotem, niewielki float sprężynowy w jednej osi jako margines na tolerancje |

## 10. Mapa drogowa

**Etap 1 (rdzeń)**: payload bay + auto-ID, battery bay (XT60/XT90 sztywno montowane w układzie blind-mate, prowadnice, zatrzask dwupunktowy), sensor stały (fuzja termo-RGB), automat stanów podstawowy, moduł akustyczny do poziomu działającego, zbenchmarkowanego prototypu (Etapy 0–2 planu walidacji akustycznej: front-end RPM + selektywny beamforming ROI + własny pomiar pozycji mikrofonu i krzywej zasięgu).

**Etap 2 (rozszerzenie)**: AOS dla środowiska leśnego, moduł PM2.5, sekwencyjna fuzja namiarów pod realnym ego-noise, moduł sejsmiczny (eksploracyjny), walidacja trwałości battery bay po wielokrotnych cyklach wymiany, dziennik iteracji od dnia pierwszego, docelowo własna płytka PCB (magistrala BMS i payload bay).

**Etap 2.5 (opcjonalny, warunkowy)**: trening i ewaluacja sieci neuronowej do separacji sygnału docelowego od szumu silnika/otoczenia, na Raspberry Pi z Etapu 1, równolegle do prac nad AOS/PM2.5/modułem sejsmicznym. Warunek wejścia: zbenchmarkowany Etap 2. Cel: gotowe przed zgłoszeniem do Explory; jeśli harmonogram się nie domknie, dokończone jako rozszerzenie na ISEF.

**Etap 3 (walidacja i zgłoszenie)**: rotor-aware NCM jako upgrade akustyczny (jeśli czas pozwoli), udział w ćwiczeniach z partnerem poszukiwawczo-ratowniczym (druga połowa horyzontu czasowego), zgłoszenie do Explory/El-Robo-Mech, rozważenie ścieżki ISEF.

**Poza horyzontem konkursowym**: licencjonowanie IP standardu złącza i modułu akustycznego, rozważenie zgłoszenia patentowego (UPRP), roadmap rolnictwo/środowisko jako dowód generalizowalności architektury.
