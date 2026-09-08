# 22 — Ocena ConOps drona i ortezy oraz porównanie z interfejsem

**Data:** 16 sierpnia 2026
**Materiał:** `dron_ConOps.md` (wersja 16 VII 2026) i `orteza_ConOps.md` (wersja 0.1, 8 VIII 2026), oba przesłane przez użytkownika.
**Metoda:** te same sześć kryteriów, które przeżył interfejs.

---

## 0. Rzecz, którą trzeba powiedzieć przed oceną

**Oba dokumenty są lepsze warsztatowo niż dokumentacja interfejsu sprzed etapu 2.** Mają znaczniki pewności (`[D]`/`[W]`/`[L]`), rejestr korekt, jawną sekcję „świadomie poza zakresem", metryki zapisane przed pomiarem i obowiązkową ablację. ConOps ortezy ma **jedenaście wpisów w rejestrze korekt** — czyli dokładnie tę dyscyplinę, którą w tym repozytorium prowadzimy jako `KOREKTY.md`.

`[wniosek]` To znaczy dwie rzeczy. Po pierwsze: **te projekty nie padły przez niechlujstwo**, więc ich obituaria trzeba traktować poważnie, a nie odruchowo podważać. Po drugie: **sekcje 10A i 10B ConOps ortezy zawierają ustalenia o Explory, których nasze repozytorium nie ma w tej rozdzielczości** i które są przenośne na interfejs niezależnie od werdyktu — patrz §5.

---

## 1. Znalezisko, które zmienia ocenę ortezy

**Akt zgonu ortezy w `HANDBOOK.md` §7 dotyczył wyłącznie tezy 1** — sprzęgła i sterowanego punktu zaczepienia. Jest tam wymienione: sprzęgło-sprężyna w kolanie opublikowane wielokrotnie, wersja magnetoreologiczna z lutego 2026, zmienny punkt zazębienia w IEEE TBME, automatyczne przełączanie trybu, komercyjnie Ottobock C-Brace. **Sam ConOps to przyznaje** w rejestrze korekt, wpis 3, i przeformułowuje tezę na koszt plus pomiar plus integrację.

**Ale ConOps ma drugą tezę, której nikt nigdy nie zaudytował** — sprawność przeniesienia momentu przez interfejs orteza–kończyna. Cytat z dokumentu:

> *„Trzy niezależne zespoły, ten sam problem, trzy różne obejścia. **Żaden nie podaje, jaki procent zadanego momentu faktycznie dociera do stawu.**"*

To jest **twierdzenie pomiarowe o kształcie, który przeżył audyt przy interfejsie**: nie o pierwszeństwie, z wynikiem niezależnym od konkretnej konstrukcji. Autor ConOps sam nazywa je najmocniejszym elementem projektu i ma rację co do kształtu.

### 1.1 Sprawdziłem. Teza 2 jest zajęta w stopniu, którego ConOps nie zakłada

`[fakt, Europe PMC, 16 VIII 2026]` Pięć zapytań o sprawność przeniesienia momentu, straty na tkance miękkiej i mechanikę interfejsu człowiek–egzoszkielet. Dwie prace trafiają wprost:

**a) *Human-Interface Dynamics of Knee Exoskeletons with Lateral and Anteroposterior Attachment*, ICORR 2025, PMID 40644288.**

Cytat: *„backdrivable actuators are coupled by mechanical interfaces to soft tissues of the human body that together introduce resonator dynamics that can **delay or diminish the torque assistance**. Low interface stiffness and uncompensated dynamics can cause **inefficient power delivery to the user**"*.

**Dziesięciu badanych, kolano, pomiary quasi-statyczne i charakterystyka częstotliwościowa**, porównanie dwóch geometrii mocowania, wynik liczbowy: nowy interfejs jest o **85,7% sztywniejszy** (p<0,01).

**b) *Quantification of the Mechanical Properties in the Human-Exoskeleton Upper Arm Interface*, Sensors 2025, PMID 40807771.**

Cytat: *„the human-exoskeleton interaction remains poorly understood, and the mechanical properties of the pHEI are **not well characterized**. Therefore, we present a **novel methodology to precisely characterize** pHEI interaction stiffnesses"*. **Dwudziestu jeden badanych**, obciążanie w trzech osiach aparaturą elektromechaniczną, pełny tensor sztywności z liczbami: 2,1 N/mm wzdłuż osi ramienia, 4,5 N/mm prostopadle, 0,2 N·m/° obrotowo.

### 1.2 Uczciwa ocena, bez przesady w żadną stronę

**Czego te prace NIE robią:** żadna nie podaje jednej liczby „procent zadanego momentu docierający do stawu kolanowego" dla ortezy w klasie kosztowej konsumenckiej. Sformułowanie tezy 2 dosłownie — jako procentu — pozostaje `[luka]` nieodnalezione.

**Czego dowodzą:** problem jest **nazwany, badany i mierzony**, na kolanie, z aparaturą lepszą niż domowa, na próbach 10 i 21 osób, w 2025 roku. To nie jest luka, której nikt nie zauważył — to jest **czynne pole badawcze**.

`[wniosek]` **Teza 2 spada z „nikt tego nie zmierzył" na „mierzą to zespoły z aparaturą i próbą, a konkretnej liczby dla taniej ortezy kolanowej nie opublikowano".** To wciąż jest twierdzenie do obrony, ale nie jest to twierdzenie, które ktoś zostawił leżące.

**Uwaga o przesadzaniu z korektą** (reguła z `PRZEKAZANIE.md` §5, złamana przeze mnie trzykrotnie w etapie 1): nie twierdzę, że teza 2 jest martwa. Twierdzę, że **jest o klasę słabsza, niż zakłada ConOps**, i że przy jej obronie trzeba te dwie prace zacytować i powiedzieć wprost, czym się od nich różnimy.

---

## 2. Orteza — ocena po kryteriach

| Kryterium | Ocena |
|---|---|
| **twierdzenie pomiarowe czy o pierwszeństwie** | teza 1: **martwa**, przyznane w samym ConOps. Teza 2: pomiarowa, właściwy kształt, **ale pole zajęte** (§1) |
| **wielkość efektu wobec rozrzutu** | **mocna strona.** Redukcja aktywności mięśnia czworogłowego to efekt rzędu dziesiątek procent; Spring Loaded raportuje ponad 40% odciążenia, Roam 46% redukcji bólu. **Nie grozi tu wynik zerowy** |
| **sterowalność** | **średnia.** Mechanika i elektronika w rękach autora, ale krytyczna niewiadoma (siła zwolnienia obciążonej zapadki) jest pytaniem fizycznym, nie decyzyjnym |
| **czy istnieje wynik unieważniający** | tak, i jest dobrze zaplanowany: test zapadki w sierpniu za kilkaset złotych, przed jakimkolwiek zakupem. **To jest wzorcowe** |
| **zgodność regulaminowa** | **najsłabszy punkt — patrz §2.1** |
| **realność 21 miesięcy, 10 h/tydz., solo** | **dobra.** Zakres zawężony do jednego trybu świadomą decyzją (sekcja 8 ConOps). Koszt rzędu 1 500–3 000 zł, czyli **taniej niż interfejs** |

### 2.1 Bariera, której ConOps nie wycenia dostatecznie wysoko

**Autor nie może być własnym badanym w sensie naukowym.**

ConOps ustala grupę docelową jako osoby ze zwyrodnieniem stawu kolanowego, które wstają, ale z bólem, i wskazuje realny przypadek w rodzinie. **Siedemnastolatek bez zwyrodnienia stawu, zakładający tę ortezę, nie mierzy niczego, co dotyczy problemu** — jego mięsień czworogłowy i tak pracuje w zakresie, w którym nie boli.

`[fakt, `ISEF_HUMAN_PARTICIPANTS.md`]` Zwolnienie ISEF dla badania na sobie znika w momencie, w którym badanym jest ktokolwiek inny. ConOps to widzi (sekcja 13.1, ryzyko „brak zgody IRB" oznaczone jako **krytyczne, nieodwracalne**) — ale traktuje jako pozycję proceduralną.

**To nie jest pozycja proceduralna. To jest zależność od osób trzecich na ścieżce krytycznej, od pierwszego dnia:**
- komisja IRB przy szkole (trzy osoby, w tym pracownik medyczny) — **przed pierwszym pomiarem na ojcu czy dziadku**
- fizjoterapeuta, i to **przed projektowaniem mechaniki**, bo ConOps sam ustala go jako źródło wymagań (sekcja 10A)
- członek rodziny z realnym zwyrodnieniem, dostępny wielokrotnie przez wiele miesięcy

**Porównanie z interfejsem jest tu bezlitosne:** kampania interfejsu do maja 2027 biegnie **w całości na autorze**, w wersji zwolnionej z papierologii. U ortezy nie ma odpowiednika tej ścieżki. Ryzyko R6 z naszego rejestru, które u interfejsu jest planem awaryjnym, u ortezy jest **warunkiem wstępnym**.

### 2.2 Co bym poprawił w ortezie

1. **Przenieść IRB i fizjoterapeutę z „ryzyk" na „kamienie milowe zerowe".** Jeżeli w listopadzie 2026 nie ma komisji, projekt nie ma jak zmierzyć swojej głównej metryki i trzeba to wiedzieć w listopadzie, nie w marcu.
2. **Przeformułować tezę 2 z „procentu" na „porównanie geometrii mocowania".** Praca ICORR 2025 pokazuje, że **różnica między dwoma sposobami mocowania jest mierzalna i duża** (85,7% sztywności). To jest wielkość, którą da się zmierzyć tanio, wewnątrzosobniczo, i która nie wymaga aparatury z pracy o tensorze sztywności. **Twierdzenie porównawcze zamiast bezwzględnego** — dokładnie ta sama operacja, którą wykonaliśmy na interfejsie.
3. **Dodać ablację geometrii do listy metryk.** ConOps ma ablację sprzęgła (włączone/wyłączone); brakuje ablacji mocowania, a to jest teraz najciekawsza zmienna.
4. **Zamknąć pytanie o zapadkę przed czymkolwiek innym** — ConOps to planuje i to jest jedyny element, którego bym nie ruszał.
5. **Rozstrzygnąć kategorię ISEF.** ConOps zostawia otwarte ENBM kontra ROBO. Nasze liczby: **ENBM 98 projektów, EBED 49, ROBO 61**. Orteza w EBED nie wejdzie; realnie ENBM albo ETSD.

---

## 3. Dron — ocena po kryteriach

### 3.1 Akt zgonu jest trafny i sam ConOps go zawiera

Diagnoza z ConOps ortezy, sekcja wstępna: *„przyczyną odrzucenia była niemożność obrony deklarowanej zdolności (akustyka docierała po termowizji, czyli **potwierdzała zamiast wykrywać**)"*.

**Sprawdziłem to w dokumencie drona i diagnoza się potwierdza w trzech miejscach niezależnie:**
- warstwa 2 architektury akustycznej to *„nasłuch ograniczony do sektora przestrzennego **wskazanego przez sensor stały** (fuzja termo-RGB)"*
- scenariusz A, krok 4: *„Moduł akustyczny (jeśli zamontowany) **potwierdza** sygnał życia"*
- automat stanów: tryb akustyczny ma wyzwalacz *„anomalia wykryta"*, czyli wejście zależne od termowizji

`[wniosek]` **Flagowa zdolność jest podporządkowana zdolności, którą kupuje się gotową.** Zdejmij ograniczenie do ROI i wracasz do nasłuchu 360° pod własnym hałasem wirników, gdzie literatura cytowana w tym samym dokumencie podaje **F1 = 0,26–0,31 poniżej −30 dB**. To jest ta sama ściana, tylko widziana od drugiej strony.

### 3.2 Drugi, niezależny zabójca: zakres

ConOps wymienia jako budowane w jednym cyklu: payload bay z auto-identyfikacją, battery bay z blind-mate, fuzję termo-RGB na OAK-D Lite, **trójwarstwowy** moduł akustyczny, AOS, moduł sejsmiczny, PM2.5, sieć neuronową w etapie 2.5, automat stanów, docelowo własne PCB.

**To jest pięć projektów.** Jedna osoba, 10 h tygodniowo. **Sam ConOps stawia „eksplozję zakresu" na pierwszym miejscu w tabeli ryzyk** — i słusznie, ale mitygacja („priorytet: rdzeń plus jeden flagowy moduł") nie została odzwierciedlona w mapie drogowej, która nadal wymienia wszystko.

Do tego koszt: platforma 7-calowa, OAK-D Lite, kamera termowizyjna, Raspberry Pi, tablica MEMS. `[domysł]` rząd **6 000–12 000 zł**, przy czym sama termowizja jest pozycją, której nie da się kupić tanio.

### 3.3 Sterowalność — najniższa z trzech projektów

Walidacja polowa zależy od OSP i GPR, od pogody, od certyfikacji A1/A3, od ograniczenia VLOS i od dostępności ćwiczeń. **ConOps sam wpisuje plan B: „udział jako obserwator istniejących manewrów".** To znaczy, że najważniejszy element dowodowy leży poza kontrolą autora.

### 3.4 Co bym poprawił — i tu jest rzecz najciekawsza w całej tej ocenie

**W dronie siedzi projekt, który przeżyłby audyt, i nie jest nim dron.**

ConOps, etap 2 planu walidacji, zawiera dwa zdania, które są zgłoszeniem luki przez samego autora:

> *„własny pomiar różnicy SNR między pozycją mikrofonu nad/pod/na zawieszeniu na WŁASNYM dronie — literatura potwierdza kierunek (nad = lepiej), ale **nie podaje wartości liczbowej specyficznej dla konkretnej platformy**"*

> *„własna krzywa błąd-dystans dla dźwięku impulsywnego generowanego przez człowieka (**dostępna literatura ma taką krzywą tylko dla petard/eksplozji, nie dla krzyku**)"*

**To jest twierdzenie pomiarowe o właściwym kształcie:** zmienna niezależna to położenie mikrofonu i odległość, zmienna zależna to SNR i błąd namiaru, punkt odniesienia zewnętrzny istnieje (DroneAudioset, NeurIPS 2025), a wynik jest niezależny od tego, czy zbuduje się modułową platformę.

**Operacja, którą bym wykonał, jest dokładnie tą samą, którą wykonaliśmy na interfejsie:** wyrzucić payload bay, battery bay, AOS, sejsmikę, PM2.5, sieć neuronową i automat stanów. Zostawić **dron, tablicę mikrofonów i jedno pytanie: ile SNR kosztuje położenie mikrofonu i jak daleko słychać krzyk pod hałasem wirników.**

`[wniosek]` Taki projekt jest wykonalny solo, mieści się w budżecie, ma zewnętrzny punkt odniesienia i **nie zależy od tego, czy akustyka wykrywa, czy potwierdza** — bo mierzy warunki, w jakich w ogóle cokolwiek słychać. **To jest realna alternatywa i zapisuję ją jako żywą, a nie jako pocieszenie.**

Czego nadal nie rozwiązuje: zależności od pogody i przestrzeni do latania, oraz tego, że hałas wirników jest zjawiskiem, na które autor ma ograniczony wpływ konstrukcyjny.

---

## 4. Porównanie trzech projektów

| Kryterium | **Interfejs** | **Orteza** | **Dron (zredukowany)** |
|---|---|---|---|
| twierdzenie | pomiarowe, pole **niezajęte w 5 bazach** (ryzyko 10–15%) | pomiarowe, ale pole **czynnie badane**, N=10 i N=21 w 2025 | pomiarowe, luka **przyznana przez literaturę** |
| wielkość efektu | 9–24 pp, zmierzona na cudzych danych | dziesiątki procent, **największa z trzech** | `[luka]` nieznana, do zmierzenia |
| **kto może być badanym** | **autor, zwolnienie ISEF** | **NIE autor** — wymaga IRB i osoby chorej | autor plus manekin/głośnik |
| sterowalność | wysoka | średnia | **niska** — pogoda, partnerzy, przepisy |
| ryzyko główne | **R1: 20–30%, że SSVEP nie działa u autora** | brak dostępu do badanych i do fizjoterapeuty | zależność od warunków zewnętrznych |
| koszt | 4 500–7 300 zł | **1 500–3 000 zł** | 6 000–12 000 zł |
| demonstracja przy stoisku | migający panel, kursor na ekranie | **juror zakłada i wstaje z krzesła** — najmocniejsza z trzech | wideo z ćwiczeń |
| kategoria ISEF | **EBED, 49 projektów, zero EEG** | ENBM, 98 projektów | ROBO albo EBED |
| konkurencja w Explory | 1 projekt EEG na 133, zero w finałach | 1 urządzenie wspomagające w całej stawce 2026 | drony są częste |
| stan zaawansowania dziś | **reanaliza gotowa, kod działa** | ConOps v0.1, zero pomiarów | ConOps, zero pomiarów |

### 4.1 Werdykt

**Interfejs zostaje faworytem, ale przewaga jest węższa, niż powiedziałbym przed przeczytaniem ConOps ortezy, i wynika z innego powodu, niż bym zgadywał.**

**Nie wygrywa nowością.** Po dzisiejszym sprawdzeniu obie osie pomiarowe — nasza i teza 2 ortezy — leżą w polach częściowo zajętych, z podobnym marginesem.

**Nie wygrywa demonstracją.** Orteza wygrywa przy stoisku i wygrywa wyraźnie. Juror, który zakłada urządzenie i czuje różnicę przy wstawaniu, jest mocniejszym argumentem niż kursor sterowany wzrokiem, a `HANDBOOK.md` §4.13 mówi wprost, że 7 na 10 Nagród Głównych poszło do konstrukcji.

**Wygrywa jednym: tym, kto może być badanym.**

Kampania interfejsu biegnie na autorze, w wersji zwolnionej z uprzedniej zgody komisji. Orteza tej ścieżki nie ma — jej główna metryka wymaga osoby ze zwyrodnieniem stawu, czyli **komisji IRB, zgód i dostępności osoby trzeciej przez wiele miesięcy, zanim padnie pierwsza liczba**. Przy jednym strzale i kalendarzu do maja 2028 to jest różnica między projektem, który rusza w październiku, a projektem, który rusza wtedy, gdy zbierze się komisja.

**Drugi powód, słabszy, ale realny: przewaga czasowa.** Interfejs ma zrobiony kawałek pracy naukowej — reanalizę z odtworzonymi liczbami i działającym kodem. Orteza ma nierozstrzygniętą niewiadomą mechaniczną, która może ją zabić w sierpniu. To nie jest argument merytoryczny, tylko wycena ryzyka pozostałego.

### 4.2 Warunek, który odwróciłby ten werdykt

**Jeżeli przesiew E0 w październiku pokaże, że SSVEP u Ciebie nie działa** — interfejs traci swoją jedyną przewagę, bo wtedy on też potrzebuje komisji IRB i cudzych głów. **W tym scenariuszu orteza staje się mocniejszym projektem**, bo ma większy efekt, niższy koszt i lepszą demonstrację, a obie ścieżki są wtedy tak samo zależne od komisji.

`[wniosek]` **To jest kolejny powód, żeby E0 wykonać jako pierwszy pomiar w projekcie i nie odkładać go.** Nie tylko rozstrzyga R1 — **rozstrzyga, który z dwóch projektów jest właściwy.**

### 4.3 Czego nie rekomenduję

**Nie rekomenduję prowadzenia dwóch projektów równolegle.** Handbook mówi, że każda dołożona funkcja odbiera czas jakości wykonania; to samo dotyczy dołożonego projektu. Przy 10 h tygodniowo i pracy w pojedynkę dwa projekty to dwa niedokończone.

**Nie rekomenduję wskrzeszania drona w wersji z ConOps.** W wersji zredukowanej do pomiaru akustycznego jest to projekt żywy, ale trzeci w kolejce i z najniższą sterowalnością.

---

## 5. Co przenoszę z ConOps ortezy do naszego projektu, niezależnie od werdyktu

Sekcje 10A i 10B tamtego dokumentu zawierają ustalenia o Explory, których nasze repozytorium nie ma w tej rozdzielczości. Trzy wchodzą od razu:

1. **Plakat bez wykresów.** Przegląd 29 projektów finałowych 2026: wzorcowa dokumentacja pomiarowa występuje w biologii i chemii, a dla projektu inżynierskiego odpowiednikiem sekcji metodologicznej jest **dziennik postępu budowy**. Wykresy i tabele idą do segregatora na stoisku, na pytania jurora — bo „znajomość zastosowanych metod" jest oceniana z rozmowy. **Nasze `13_PODNIESIENIE_SZANS.md` tego nie mówi wprost.**
2. **Fotografowanie wersji nieudanych.** U MAPPER-a jeden z trzech wniosków był negatywny i to czyta się jako rzetelność mocniej niż tabela. **Wchodzi do naszego dziennika budowy jako reguła, nie jako opcja.**
3. **Liczby nakładu zamiast pomiarów na plakacie** — liczba godzin, liczba wersji, liczba cykli bez uszkodzenia.

Jedno zastrzeżenie do punktu 1, ważne dla nas: **na ISEF pomiary są obowiązkowe** i ConOks ortezy sam to zaznacza. Reguła „bez wykresów" dotyczy plakatu na Explory, nie stoiska w Stanach.
