# KOREKTY — rejestr błędów i poprawek

Zgodnie z sekcją 2.2 handbooka. Każdy wyłapany błąd ląduje tutaj z datą, treścią i poprawką.

Format wpisu: data | źródło błędu | co było źle | poprawka | kto wyłapał

---

## 2026-08-15

### K-001 — błąd arytmetyczny w handbooku, sekcja 3

**Co było źle:** „Do działającego prototypu ~14 miesięcy (El-Robo-Mech)".

**Poprawka:** od 14 VIII 2026 do ~15 IV 2027 jest **8 miesięcy**. Czternaście miesięcy to dystans do finału krajowego Explory w X 2027. Liczba 21 miesięcy do ISEF jest poprawna, 6,5 miesiąca do zamknięcia zgłoszeń też.

**Konsekwencja:** margines do pierwszego twardego terminu sprzętowego jest o 43% krótszy, niż podaje handbook, przy projekcie wymagającym nauki projektowania PCB od zera.

**Kto wyłapał:** Claude Code, przy drugim czytaniu wg sekcji 14.

---

### K-002 — luka z sekcji 4.2 była domknięta w tym samym akapicie

**Co było źle:** „[luka] Dokładna data kwalifikacji dla edycji 2027 — do zweryfikowania" postawiona zaraz po podaniu reguły, która ją rozstrzyga.

**Poprawka:** reguła przesunięcia o rok daje 1 I 2006 dla edycji 2027. Użytkownik, rocznik ok. 2010, spełnia z zapasem czterech lat. Luka schodzi z listy priorytetów do drobiazgu potwierdzanego przy zgłoszeniu.

**Kto wyłapał:** Claude Code.

---

### K-003 — sekcja 5.3 skleja trzy sita w jedną liczbę

**Co było źle:** „~300 zgłoszeń → ~3 miejsca w reprezentacji, rzędu 1%" użyte jako wskaźnik decyzyjny.

**Poprawka:** rozbicie na szanse warunkowe: zgłoszenie → półfinał ~50%, półfinał → finał ~14–17%, finał → reprezentacja ~12–14%.

**Konsekwencja strategiczna:** wąskie gardło jest w przejściu półfinał → finał, ocenianym w trzech czwartych po kryteriach zależnych od znajomości literatury i jakości prezentacji, nie po sprzęcie. Etap 1 nie jest przygotowaniem do właściwej pracy — jest bezpośrednio punktowany w najwęższym miejscu lejka.

**Kto wyłapał:** Claude Code.

---

### K-004 — liczby 65 i 3 wpm bez oznaczenia pewności

**Co było źle:** sekcja 9.2 oznacza projekt ENBM074 i autorstwo jako `[fakt]`, ale kluczowe liczby (~65 słów/min wobec ~3) nie mają żadnego znacznika, mimo że pochodzą z relacji ustnej.

**Poprawka:** obie liczby dostają status `[domysł]` do czasu odczytania pełnego abstraktu. W `/06_TABELA_PARAMETROW.md` musi istnieć kolumna „skąd ta liczba".

**Kto wyłapał:** Claude Code.

---

### K-005 — wniosek o składzie jury oparty na danych o edycję za wczesnych

**Co było źle:** sekcja 4.10 wyciąga wniosek „korzystne dla projektu na styku elektroniki i neurotechnologii" ze składu jury edycji 2026, podczas gdy nasza edycja to 2027. Ten sam handbook zaznacza, że 15 z 17 nazwisk pochodzi z jednego źródła.

**Poprawka:** wniosek zachowany, ale zdegradowany z przesłanki strategicznej do obserwacji. Nie budować na nim żadnej decyzji.

**Kto wyłapał:** Claude Code.

---

### K-006 — reguła 12/18 miesięcy nie została przełożona na daty

**Co było źle:** sekcja 5.4 podaje regułę i zaleca rezerwowanie zasobów jednorazowych „po czerwcu 2027", ale nie wylicza okna i nie sprawdza, co się z nim zderza.

**Poprawka:** przy ISEF ~V 2028 osiemnaście miesięcy wstecz to ~XI 2026, a okno dwunastu miesięcy ciągłych kończące się przy ISEF to ~V 2027 – V 2028. Handbook nie rozstrzyga, jak te dwie reguły się składają — do sprawdzenia w oryginale International Rules.

**Konsekwencja pominięta w handbooku:** pomiary pokazane na El-Robo-Mech (IV 2027) i w półfinale Explory (V–VI 2027) wypadają przed oknem albo na jego krawędzi i będą wymagały powtórzenia. Finał Explory (X 2027) mieści się w oknie. To pozycja harmonogramowa do wpisania w plan, nie niespodzianka na marzec 2028.

**Kto wyłapał:** Claude Code.

---

### K-007 — założenie, że finał X 2027 wysyła na ISEF V 2028, nie jest sprawdzone

**Co było źle:** cała teza „jeden strzał" z sekcji 3 stoi na tym założeniu, nigdzie niepopartym cytatem z regulaminu.

**Poprawka:** przeklasyfikowane na `[luka]` o najwyższej stawce. Jeżeli reprezentacja na ISEF 2028 została wyłoniona już na GEW X 2026, właściwym celem jest ISEF 2029 i cała ocena sensowności przedsięwzięcia wygląda inaczej.

**Status:** do sprawdzenia jako pierwsze po odblokowaniu dostępu do sieci.

**Kto wyłapał:** Claude Code.

---

### K-008 — nierozstrzygnięty rodzaj gramatyczny przy autorstwie ENBM074

**Co było źle:** handbook konsekwentnie używa rodzaju żeńskiego („autorka", „wygrała"). Jedno znalezione źródło wtórne używa rodzaju męskiego. Nie mam ustalenia.

**Poprawka:** do czasu potwierdzenia piszę neutralnie. Bez znaczenia merytorycznego, ale nie powielam nieustalonego szczegółu o realnej osobie.

**Kto wyłapał:** Claude Code.

---

### K-009 — typ zapisany przed weryfikacją, żeby nie dało się go później naciągnąć

**Czego dotyczy:** pomysł użycia sEMG/EOG jako kanału odniesienia do sprzętowego usuwania zakłóceń z EEG przy uchu.

**Zapis:** przed jakimkolwiek sprawdzeniem oceniam, że w wersji ogólnej technika jest znana i stara (korekcja artefaktów ocznych przez osobny kanał, lata 80.), a ewentualna szczelina leży wyłącznie w realizacji analogowej przed przetwornikiem w urządzeniu noszonym.

**Po co ten wpis:** sekcja 8 handbooka, błąd nr 5 — założenie luki zamiast jej sprawdzenia, a potem budowa strategii na założeniu. Data i treść typu są zapisane, więc po weryfikacji nie da się go przesunąć w żadną stronę.

**Kto zażądał sprawdzenia:** użytkownik, wprost, powołując się na wcześniejsze wpadki z rzekomą innowacyjnością.

**ROZSTRZYGNIĘCIE, 15 VIII 2026 (etap 1):** typ trafny co do kierunku, **zbyt optymistyczny co do szerokości szczeliny**. Wersja ogólna zajęta od 1983 (Gratton, Coles, Donchin). Dodatkowo — czego typ nie przewidywał — **realizacja analogowa też jest zajęta**, na poziomie układów scalonych, dla artefaktów ruchowych. Nie znalazłem kompensacji analogowej EMG/EOG z kanału referencyjnego w urządzeniu przyusznym, ale przeszukanie jednym kanałem nie jest dowodem nieistnienia. Pełny rozbiór: `04_LUKI_ZAPISANE.md` sekcja 2. Konsekwencja: **twierdzenie projektu nie może brzmieć „pierwszy raz", musi brzmieć jako pomiar.**

---

### K-010 — ciągłe vs dyskretne sterowanie było źle postawionym wyborem, także przeze mnie

**Co było źle:** w rundzie pierwszej przedstawiłem sterowanie ciągłe i dyskretne jako alternatywę na jednej osi. To sklejało dwie niezależne warstwy: sposób odczytu sygnału i sposób poruszania się sterowanego obiektu.

**Poprawka:** warstwy są niezależne. Odczyt dyskretny z płynnym ruchem obiektu (sterowanie prędkością, podział pracy z maszyną) daje efekt, którego użytkownik chciał, bez elektrod nad korą ruchową.

**Konsekwencja:** dopiero po rozdzieleniu widać właściwy argument — to nie „ciągłe jest trudniejsze", tylko „ciągły odczyt wymusza hełm", co zderza się z twardym wymaganiem z sekcji 9.1 handbooka. Argument jest mocniejszy i innego rodzaju niż ten, który podałem najpierw.

**Kto wyłapał:** użytkownik, pytaniem „czy z dyskretnym da się osiągnąć podobny efekt, kosztem większej ilości pracy". Odpowiedź brzmiała tak, a pytanie ujawniło, że moje pierwsze postawienie sprawy było niepełne.

---

### K-011 — wymaganie materiałowe dla drukarki odziedziczone z porzuconego projektu

**Co było źle:** wybór Qidi Q2 uzasadniony materiałami trudnymi (PA12-CF) pochodzi z projektu drona, porzuconego w poprzednim cyklu. Przeniesienie tego wymagania na projekt urządzenia dousznego nie zostało zakwestionowane przez nikogo, łącznie ze mną w rundzie pierwszej.

**Poprawka:** [wniosek] wymaganie prawdopodobnie odwraca się co do kierunku — potrzebne jest odwzorowanie kształtu i bezpieczeństwo kontaktu ze skórą, nie sztywność i odporność termiczna. Zakup wstrzymany do weryfikacji w etapie 1.

**Kto wyłapał:** użytkownik, prosząc o zbadanie tematu zamiast potwierdzenia wyboru.

---

## 2026-08-15, etap 1

### K-012 — WYCOFANA. Patrz K-018

**Treść pierwotna:** twierdziłem, że kod `ENBM074` w sekcji 9.2 handbooka jest błędny, bo należy do projektu „Synthetic DNA Engineering With ICOR" (Rishab Jain, ISEF 2022).

**Status: wycofana 15 VIII 2026.** Kod jest prawidłowy dla edycji 2026. Mój wniosek był błędny — szczegóły i przyczyna w K-018.

---

### K-013 — K-007 zamknięte na korzyść handbooka

**Czego dotyczy:** założenia z sekcji 3 handbooka, że finał Explory w X 2027 wyłania reprezentację na ISEF V 2028. K-007 przeklasyfikował to na `[luka]` o najwyższej stawce.

**Rozstrzygnięcie:** wzorzec potwierdzony — **finał w październiku roku N → ISEF w maju roku N+1**. Explory 2025 → ISEF 2026 (Phoenix); Explory 2026 (finał 21–23 X 2026) → ISEF 2027. Zatem edycja użytkownika: finał X 2027 → **ISEF V 2028**.

**Potwierdzenie krzyżowe:** skład reprezentacji na ISEF 2026 (Pająk; Sułek; Truszczyńska i Duszyńska) to **3 projekty i 4 osoby** — dokładnie liczba podana niezależnie w sekcji 4.9 handbooka.

**Konsekwencja:** teza „jeden strzał" stoi, kolizja z maturą 2029 nie występuje. **Alternatywa z punktu 1.4 `00_PYTANIA_I_LUKI.md` odpada.**

**Co zostaje:** cytat z regulaminu edycji 2027. Powyższe pochodzi ze stron organizatora, nie z dokumentu regulaminowego.

**Kto wyłapał:** Claude Code, etap 1.

---

### K-014 — mój argument „odczyt ciągły wymusza hełm" był za mocny

**Co było źle:** w sekcji 4c `00_PYTANIA_I_LUKI.md` napisałem, że amplituda rytmów sensomotorycznych przy uchu „spada prawdopodobnie do okolic szumu własnego wzmacniacza", i **uczyniłem z tego główny argument** za odczytem dyskretnym.

**Poprawka:** istnieje praca *„Detection of motor-related mu rhythm desynchronization by ear EEG"* (PLOS One 2025) o tym, że desynchronizacja mu **jest wykrywalna z ucha**. Ear-EEG opisywane jest jako porównywalne ze skalpowym dla źródeł blisko ucha.

**Wersja poprawna, słabsza i uczciwsza:** nie „z ucha nie widać kory ruchowej", tylko **„ciągłe, wielowymiarowe sterowanie wymaga gęstej siatki elektrod nad korą ruchową, a pojedyncza pozycja zauszna nie daje filtracji przestrzennej potrzebnej do rozdzielenia kierunków"**.

**Co zostaje w mocy:** ustalenie „odczyt dyskretny, zachowanie obiektu ciągłe" — bo stoi na czterech innych nogach (metryka standardowa, krótki trening, czyste zejście o poziom w dół, pokaz na stoisku). **Zmienia się uzasadnienie, nie decyzja.**

**Dlaczego to ważne:** tego argumentu użytkownik miałby użyć przed jurorem znającym dziedzinę. W wersji sprzed korekty zostałby obalony jednym cytatem.

**Kto wyłapał:** Claude Code, etap 1, na własnym rozumowaniu z rundy drugiej.

---

### K-015 — moja rekomendacja paradygmatów słuchowych jest podważona

**Co było źle:** w rundzie drugiej rekomendowałem paradygmaty słuchowe (uwaga słuchowa, oddball słuchowy) jako „te, których generator neuronalny leży blisko ucha" — czyli jako naturalny wybór dla formy zausznej.

**Poprawka:** praca *„Signal-specific performance of in-ear EEG: strengths and limitations"* (Front Neurosci 20:1859327, 2026; 19 osób, douszny suchy vs 32-kanałowy BioSemi) podaje, że w konfiguracji dousznej **alfa spoczynkowa wychodzi pewnie, a odpowiedź słuchowa N1-P2 nie**. Do tego uwaga słuchowa ma najniższe ITR w całej zebranej tabeli: **1,89–2,08 bit/min**.

**Wniosek przeciwny do mojego pierwotnego:** dla sterowania w formie zausznej **SSVEP wygląda lepiej niż paradygmaty słuchowe** (6–17 bit/min z ucha), mimo większej odległości od kory wzrokowej — bo sygnał okresowy o znanej częstotliwości daje się wyłuskać przy złym SNR, a ERP nie.

**Czego to nie przesądza:** SSVEP wymaga patrzenia na migający obiekt, co osłabia argument „działa przy zamkniętych oczach" i zbliża do konkurencji z eye trackingiem. **Wybór paradygmatu należy do etapu 2 i ma być świadomy, nie odziedziczony po mojej rekomendacji z rundy drugiej.**

**Kto wyłapał:** Claude Code, etap 1.

---

### K-016 — handbook skleja dwie różne role El-Robo-Mech

**Co było źle:** sekcja 6 handbooka przypisuje El-Robo-Mech rolę „zewnętrznej walidacji, której projektowi brakowało", powołując się na ustalenie z sekcji 4.13 o podium z niezależnych zawodów.

**Poprawka:** ustalenia dla edycji XI (2025/2026): zgłoszenia do 25 III 2026, finał 15–16 IV 2026, tematyka od mechaniki po inżynierię biomedyczną (**interfejs neuralny kwalifikuje się**), nagrodą jest **indeks na studia**, laureatów w edycji **34**.

**Konsekwencja:** to nie jest podium z selektywnych zawodów. El-Robo-Mech zachowuje wartość jako **wymuszony termin** i tani dry-run prezentacji; **nie zachowuje wartości jako zewnętrzna walidacja** w rozumieniu sekcji 4.13. To są dwie różne role.

**Skutek dla kalendarza:** termin kwiecień 2027 zostaje, ale jako **samonarzucony**, nie jako wymóg strategiczny — więc można go przesunąć bez straty, gdyby kolidował z sensowną kolejnością prac.

**Pozycja otwarta:** alternatywne konkursy dające realną walidację zewnętrzną — nieprzeszukane, kierunki w `08_KONKURENCJA_ISEF.md` sekcja 4.1.

**Kto wyłapał:** Claude Code, etap 1.

---

### K-017 — rola sEMG/EOG jako źródła sterowania jest zajęta

**Czego dotyczy:** roli 1 z sekcji 4b/C3 `00_PYTANIA_I_LUKI.md` — sEMG/EOG jako źródło sterowania, „odłożone, nie odrzucone".

**Ustalenie:** **ID.EARS**, CHI 2025, DOI 10.1145/3706598.3714185. Urządzenie na jedno ucho, elektrody suche, pięć gestów w czasie rzeczywistym (mrugnięcie, wink lewy, wink prawy, zaciśnięcie zębów, żucie), **>90% dokładności**. Autorzy formułują to jako świadome odwrócenie konwencji: EMG i EOG jako sygnał zamiast szumu.

**Poprawka statusu:** rola 1 przechodzi z „odłożona" na **zamkniętą**. Nie „ryzykowna" — zrobiona, rok temu, z demonstracją, na topowej konferencji od interakcji człowiek–komputer.

**Rola 2 (kanał odniesienia do usuwania zakłóceń) nietknięta** — ID.EARS idzie w przeciwną stronę.

**Wartość uboczna, konkretna:** ID.EARS jest gotowym dowodem, że przy uchu da się wykrywać zaciśnięcie zębów i mrugnięcia w czasie rzeczywistym z >90% trafnością. Nasz układ takiego detektora i tak potrzebuje, żeby wiedzieć, kiedy kompensować. To cegiełka, nie przeszkoda.

**Kto wyłapał:** Claude Code, etap 1.

---

### K-018 — podważyłem prawidłowy kod projektu, łamiąc regułę, którą sam zapisałem

**Co było źle:** w K-012 uznałem kod `ENBM074` z sekcji 9.2 handbooka za błędny. Podstawą była strona projektu „Synthetic DNA Engineering With ICOR" (Rishab Jain, ISEF **2022**) o tym samym kodzie.

**Dlaczego to nie wynika:** w tym samym wpisie napisałem, że **kody ISEF są numerowane w obrębie edycji i używane ponownie co roku**. Skoro tak, to kod z 2022 nie mówi nic o kodzie z 2026. Zignorowałem własną przesłankę w akapicie, w którym ją postawiłem.

**Co pogarsza sprawę:** wyszukiwarka podała wprost, że `ENBM074` w edycji 2026 to praca o interfejsach nieinwazyjnych. **Nadpisałem poprawną informację ze źródła własnym błędnym wnioskiem** — czyli zrobiłem coś gorszego niż brak weryfikacji.

**Poprawka:** kod `ENBM074` jest **prawidłowy dla edycji 2026**. K-012 wycofana. Handbook i `08_KONKURENCJA_ISEF.md` przywrócone.

**Reguła operacyjna, która z tego zostaje:** kody projektów ISEF cytować **wyłącznie z rocznikiem** — `ENBM074 (2026)`. Kod bez rocznika jest niejednoznaczny i to jest jedyna prawdziwa treść, jaka wyszła z całej tej pomyłki.

**Kto wyłapał:** użytkownik, wskazując, że sprawdzał tegoroczną edycję i że sam sobie zaprzeczyłem.

---

### K-019 — potraktowałem rozwiązanie designowe jak wymaganie wejściowe

**Co było źle:** przez cały etap 1 projektowałem pod formę „za uchem, wielkości aparatu słuchowego", traktując ją jako ograniczenie nienaruszalne. Wpisałem ją do `CLAUDE.md` jako ustalenie wiążące i wyprowadziłem z niej oś projektu, wybór paradygmatu i kształt twierdzenia.

**Na czym polega błąd:** rzeczywiste wymaganie użytkownika brzmi **„niewidoczne albo nierozpoznawalne jako sprzęt, wygodne, zero hełmów"**. „Za uchem" to jedna z możliwych **odpowiedzi** na to wymaganie, podana przy okazji rozstrzygania przypadków granicznych D1/D2. Zamieniłem odpowiedź na założenie i nigdy nie postawiłem pytania „gdzie ma być interfejs", ani nie porównałem kandydujących miejsc.

**Koszt tego błędu, liczbowo:** umiejscowienie zauszne oddaje **5–15× przepustowości** dla SSVEP względem potylicy (16,6 wobec ~92 bit/min). Przez cały etap 1 opisywałem to jako ścianę fizyczną projektu, podczas gdy jest to **konsekwencja niepostawionej decyzji**. Ściana jest prawdziwa dla ucha; nie jest prawdziwa dla urządzenia niewidocznego jako takiego.

**Dodatkowa obserwacja, która wyszła dopiero przy rozbiorze:** rzecz schowana pod włosami z tyłu głowy ma widoczność **stopnia 0**, czyli **lepszą niż aparat słuchowy** (stopień 1). Wymaganie „zero hełmów" nie tylko nie wyklucza potylicy — potylica może je spełniać lepiej.

**Poprawka:** decyzja o umiejscowieniu **otwarta**, analiza w `09_UMIEJSCOWIENIE.md`, cztery pytania postawione użytkownikowi. Wpis w `CLAUDE.md` o formie zausznej traci status ustalenia wiążącego do czasu rozstrzygnięcia.

**Ustalenie, które przeżywa:** wykluczenie elektrod nad korą ruchową (C3/Cz/C4) — te wymagają czapki przy każdym scenariuszu.

**Sprzężenie, które trzeba było zauważyć wcześniej:** miejsce i oś projektu nie są niezależne. Kompensacja artefaktów szczękowych ma sens **dlatego**, że urządzenie jest przy uchu. Przy potylicy oś trzeba wyprowadzić od nowa (kontakt przez włosy, odporność na ruch) — obie mają pokrycie w literaturze jako problemy otwarte.

**Kto wyłapał:** użytkownik, dwoma uwagami — pytaniem „skoro na potylicy mamy większą przepustowość, nie łatwiej to tam przenieść" oraz wprost: „zakładasz i sam uzupełniasz luki designowe, zamiast jasno spytać".

---

## 2026-08-15, sesja druga — weryfikacja w oryginałach

Wszystkie poniższe wpisy powstały przez **otwarcie źródła**, nie przez streszczenie. Przy każdym podaję, co konkretnie zostało odczytane.

### K-020 — Qualified Scientist NIE wymaga doktoratu

**Co było źle:** `ISEF_HUMAN_PARTICIPANTS.md` sekcja 2 podawała próg „stopień doktora w dziedzinie badań" jako definicję Qualified Scientist i wyprowadzała z tego, że opiekun-magister go nie spełnia, a użytkownik „musi zorganizować doktora".

**Poprawka, cytat z oryginału** (*International Rules 2026–2027*, sekcja *Roles & Responsibilities*): „Earned a doctoral/professional degree in a scientific discipline related to student's area of research **AND/OR** Individual with **extensive experience and expertise** in the student's area of research".

**Konsekwencja:** próg jest alternatywą, nie koniunkcją. Brat pracujący w firmie produkującej precyzyjną elektronikę mieści się w drugim członie `[wniosek]`. Ryzyko formalne z sekcji 3 `00_PYTANIA_I_LUKI.md` schodzi z wysokiego na średnie.

**Kto wyłapał:** Claude Code, sesja druga, przy odczytaniu oryginału.

---

### K-021 — rola nazywa się Direct Supervisor i nie wymaga niczego

**Co było źle:** pisałem o „Designated Supervisor" jako roli wyznaczanej przez Qualified Scientist i będącej „jego przedłużeniem".

**Poprawka:** rola nazywa się **Direct Supervisor (DS)**. Kwalifikacje wg oryginału: „Does not need an advanced degree", musi znać projekt i przyjąć potrzebne szkolenie, „**May also serve as the Adult Sponsor** for the project". DS jest wymagany m.in. wtedy, gdy QS nie jest lokalny.

**Konsekwencja:** opiekun szkolny ze stopniem magistra obsadza jednocześnie Adult Sponsor i Direct Supervisor. Nie potrzeba trzech osób tam, gdzie wystarczy jedna.

---

### K-022 — nie wiedziałem, że IRB trzeba POWOŁAĆ, a nie znaleźć

**Co było źle:** cała poprzednia wersja `ISEF_HUMAN_PARTICIPANTS.md` traktowała „zgodę komisji" jak procedurę u instytucji zewnętrznej, którą się uruchamia. Nigdzie nie pytałem, kto tę komisję stanowi.

**Poprawka:** dla projektu prowadzonego w szkole i w domu IRB **musi zostać powołane przy szkole**, a jego skład jest w regulaminie określony co do zawodu: edukator (inny niż Adult Sponsor), dyrektor lub wicedyrektor, oraz **pracownik medyczny lub ochrony zdrowia psychicznego** (dopuszczeni m.in.: pielęgniarka, psycholog, licencjonowany pracownik socjalny). Do tego zakaz konfliktu interesów: opiekun projektu ani krewny nie mogą w niej zasiadać.

**Dlaczego to poważniejsze niż wygląda:** to nie jest formularz, to są trzy osoby, które ktoś musi zebrać. Pozycja harmonogramowa na jesień 2026, nie na wiosnę 2027.

**Pozycja otwarta, którą to rodzi:** czy FZT prowadzi SRC pełniące funkcję IRB dla polskich uczestników. Jedno pytanie mailem, może skasować całą procedurę.

---

### K-023 — reguły „18 miesięcy" nie ma w regulaminie ISEF

**Co było źle:** handbook, sekcja 5.4: „Maksymalnie 12 miesięcy ciągłych badań, **zakaz wykorzystywania badań wykonanych wcześniej niż 18 miesięcy przed ISEF**". Na tym stał cały K-006 i ostrzeżenie, że pomiary z wiosny 2027 „będą wymagały powtórzenia".

**Poprawka, dwa cytaty z rocznika 2026–2027:** „may not include research performed **before January 2026**" oraz „judged only on laboratory experiment/data collection performed over **12 continuous months beginning no earlier than January 2026 and ending May 2027**".

Reguła jest zakotwiczona w kalendarzu, nie w odstępie od imprezy. **Liczby osiemnaście w oryginale nie ma.**

**Przełożenie na nasz rocznik** `[wniosek, wzorzec z jednego rocznika]`: okno **styczeń 2027 – maj 2028**, z dowolnym ciągłym blokiem 12 miesięcy w środku.

**Konsekwencja, łagodniejsza niż K-006:** nie „wszystko trzeba powtórzyć", tylko „formalna kampania pod ISEF startuje w maju 2027". Wcześniejsze prace są pracami rozwojowymi i na Explory oraz El-Robo-Mech liczą się bez ograniczeń, bo tamte konkursy reguły czasowej nie mają — sprawdzone w regulaminie Explory, nie ma tam żadnego takiego zapisu.

**K-006 pozostaje w mocy co do istnienia problemu, traci moc co do dat.**

---

### K-024 — Presentation to 35 pkt, ale plakat to tylko 10 z nich

**Co było źle:** `08_KONKURENCJA_ISEF.md` sekcja 5 wyciągała wniosek „Presentation to 35 ze 100 punktów — więcej niż wykonanie i więcej niż kreatywność" i wiązała to z ustaleniem o dziennikach postępu i plakatach.

**Poprawka:** sekcja V dzieli się na **Poster 10 pkt** i **Interview 25 pkt**. Plakat jest wart mniej niż metodologia i dwa razy mniej niż wykonanie.

**Wniosek zmieniony:** to nie plakat jest niedoszacowany, tylko **rozmowa z jurorem**, i jest to najwyżej punktowana pojedyncza pozycja w całym arkuszu. Trening polega na opowiadaniu o projekcie ludziom, nie na projektowaniu grafiki. Pełny rozbiór: `ISEF_ARKUSZE_OCENY.md`.

---

### K-025 — projekt referencyjny zdobył DRUGIE miejsce, nie „Grand Award" bez określenia

**Co było źle:** handbook sekcja 9.2 i `08` sekcja 2 podawały „Grand Award, Regeneron ISEF 2026" bez miejsca, co czytało się jak pierwsza nagroda.

**Poprawka, z bazy abstraktów Society for Science:** ENBM074 (2026), Kharade, Ameya, Nashua High School South, NH — **Second Award of $2,400** w kategorii Biomedical Engineering. Pierwsze miejsca w ENBM 2026 (po 6 000 USD) zdobyły ENBM062 i ENBM075T, projekty o zupełnie innej tematyce.

**Co przy okazji zostało zamknięte:** pełny abstrakt odczytany. **Liczby 65 i 3 wpm są prawdziwe i pochodzą wprost z abstraktu** — K-004 rozstrzygnięty na korzyść handbooka, znacznik `[domysł]` zdjęty. Pełny tekst i rozbiór: `08_KONKURENCJA_ISEF.md` sekcja 2.

---

### K-026 — mrugnięcie NIE jest problemem przy uchu. Oś projektu wymaga przeformułowania

**Czego dotyczy:** kandydata na oś projektu — analogowej kompensacji artefaktów **mięśniowo-ocznych** przy uchu (rola 2 z sekcji 4b/C3 `00_PYTANIA_I_LUKI.md`).

**Co było źle:** przez cały etap 1 pisałem „EMG szczęki **i** EOG" jako jedną parę zakłóceń do skompensowania, powołując się na Kappel 2017 jako przesłankę dla obu.

**Poprawka, z abstraktu oryginału** (Kappel, Looney, Mandic, Kidmose, *BioMed Eng OnLine* 16:103, 2017, 9 badanych):

> „Artifacts related to jaw muscle contractions were present all over the scalp and in the ear … The SNR deterioration for jaw artifacts were **in general higher in the ear compared to the scalp**. **Whereas eye-blinking did not influence the SNR in the ear**, it was significant for all groups of scalps electrodes in the delta and theta bands. Eye movements resulted in statistical significant SNR deterioration in both frontal, temporal and ear electrodes."

I wprost we wnioskach: „ear-EEG was **more prone to jaw related artifacts and less prone to eye-blinking artifacts** compared to state-of-the-art scalp based systems."

**Co z tego wynika, i jest to zmiana kierunkowa:**

1. **Przesłanka dla szczęki jest mocniejsza, niż ją stawiałem** — potwierdzona w oryginale, na 9 osobach, mierzona jako pogorszenie SNR odpowiedzi ASSR, największe w paśmie gamma.
2. **Przesłanka dla mrugnięcia jest fałszywa.** Mrugnięcie przy uchu nie psuje SNR. Kompensowanie go byłoby rozwiązywaniem problemu, którego w tej formie urządzenia nie ma.
3. **Zostaje ruch gałek ocznych** (nie mrugnięcie), który pogarsza SNR także na elektrodach usznych.

**Poprawna wersja osi:** „analogowa kompensacja artefaktów **szczękowych**, z ruchem gałek ocznych jako kanałem drugorzędnym" — a nie „mięśniowo-ocznych" traktowanych łącznie.

**Dlaczego to ma znaczenie praktyczne:** upraszcza układ. Detektor mrugnięcia, który wg `04` sekcja 4 mieliśmy wziąć z ID.EARS jako gotową cegiełkę, **nie jest do tego potrzebny**. Potrzebny jest detektor zaciśnięcia szczęki. To jest mniej pracy, nie więcej.

**Dlaczego to jest ten sam błąd co poprzednio:** postawiłem mocne twierdzenie o dwóch zakłóceniach, mając w ręku streszczenie, które mówiło tylko o jednym. Wzorzec z sekcji 5 `PRZEKAZANIE.md`, czwarta odsłona.

---

### K-027 — publiczny zbiór ear-EEG do zadań sterowania ISTNIEJE

**Co było źle:** `04_LUKI_ZAPISANE.md` sekcja 5 i `07_DEKODOWANIE.md` sekcja 7 twierdziły: „**nie znalazłem publicznego zbioru ear-EEG pod zadania sterowania**. Istniejące dotyczą snu i uwagi słuchowej", i budowały na tym propozycję, żeby opublikowanie własnego zbioru uczynić elementem wkładu projektu.

**Poprawka:** Lee, Shin, Lee, Lee, *„Mobile BCI dataset of scalp- and ear-EEGs with ERP and SSVEP paradigms while standing, walking, and running"*, **Scientific Data 8:315 (2021)**, DOI 10.1038/s41597-021-01094-4, PMID 34930915. Zawartość: **24 osoby, 32-kanałowy EEG skalpowy + 14-kanałowy ear-EEG + 4-kanałowy EOG + 9-kanałowe IMU**, dwa paradygmaty BCI (ERP i SSVEP), cztery prędkości ruchu: stanie, wolny marsz, szybki marsz, lekki bieg (0 / 0,8 / 1,6 / 2,0 m/s).

**Dlaczego to jest gorsze niż zwykła pomyłka:** to nie jest zbiór „przy okazji pasujący". To jest zbiór z **równoległym EOG i pomiarem ruchu**, czyli dokładnie pod pytanie o artefakty i stabilność przy ruchu, na którym stoi oś projektu.

**Ale to jest prezent, nie cios.** Konsekwencje:
- teza „opublikowanie własnego zbioru jest tanim elementem wkładu" — **osłabiona**, bo pole nie jest puste
- **można pracować nad dekodowaniem, zanim powstanie sprzęt.** Zbiór ma ear-EEG, SSVEP, ERP i ruch. Cała warstwa 4 z sekcji 9.4 handbooka da się rozwijać jesienią 2026 równolegle z nauką PCB, bez czekania na własne urządzenie
- daje **punkt odniesienia dla własnego sprzętu** — te same paradygmaty, znany zbiór, porównanie

---

### K-028 — SSVEP z ucha osiąga znacznie więcej, niż podawałem. Nature Communications 2023

**Co było źle:** liczba „SSVEP z ucha to 6–17 bit/min" była powtarzana w `06`, `07`, `09` i `00_STRESZCZENIE.md` jako pułap formy dousznej, i na niej stała teza o „5–15× stracie względem potylicy" oraz cała rekomendacja C2 na wariant 2 (metryka użytkowa zamiast przepustowościowej).

**Poprawka:** Wang Z., Shi N. i in., *„Conformal in-ear bioelectronics for visual and auditory brain-computer interfaces"*, **Nature Communications 14:4213 (2023)**, DOI 10.1038/s41467-023-39814-6, PMID 37452047. Urządzenie **SpiralE** — elektroda douszna rozwijająca się spiralnie wzdłuż przewodu słuchowego pod wpływem pobudzenia elektrotermicznego, dla zapewnienia kontaktu konformalnego. Wyniki wg abstraktu: **95% dokładności offline w klasyfikacji SSVEP z 9 celami** oraz **udane pisanie fraz w 40-celowym spellerze SSVEP online bez kalibracji**; do tego 84% dokładności klasyfikacji mowy naturalnej w warunkach cocktail party.

**Skala pomyłki:** 40-celowy speller online bez kalibracji to przepustowość o rząd wielkości wyższa niż 16,6 bit/min, na którym opierałem cały wniosek. Liczby 6–17 bit/min pochodziły z prac **2015 i 2022** i opisywały stan techniki sprzed ośmiu i trzech lat, a ja podawałem je jako ograniczenie formy.

**Co się przez to zmienia:**
- teza „w przepustowości z ucha nie da się wygrać" — **obalona co do formy dousznej jako takiej**, nie tylko osłabiona jak w `00_STRESZCZENIE.md` sekcja 1.2
- rekomendacja C2 na wariant 2 (metryka użytkowa) **wymaga przeliczenia od nowa**, bo była uzasadniona liczbą, która okazała się nieaktualna
- **czynnikiem decydującym okazał się kontakt elektrody z kanałem słuchowym**, nie odległość od kory wzrokowej. To jest warstwa 1 i 2 z sekcji 9.4 handbooka, czyli **warsztat użytkownika** — mechanika, materiały, dopasowanie kształtu
- jednocześnie: elektroda z aktuacją elektrotermiczną, wykonana na Tsinghua i opublikowana w Nature Communications, jest **poważną konkurencją w tej samej niszy**. Pole nie jest puste i nie jest amatorskie

**Dlaczego to najpoważniejszy wpis w tej sesji:** liczba, która nie została sprawdzona w oryginale, przez cały etap 1 służyła jako **ściana fizyczna** i na jej podstawie odrzuciłem cały wariant twierdzenia. To jest błąd nr 5 z sekcji 8 handbooka w najczystszej postaci — ocena wystawiona na niesprawdzonym założeniu.

---

### K-029 — praca o analogowym usuwaniu artefaktów: zły rok, zła klasa urządzenia

**Co było źle:** `04_LUKI_ZAPISANE.md` sekcja 2.1 opisywała stan techniki jako „**8-kanałowy IC EEG ambulatoryjny** z wewnątrzkanałową, w pełni analogową ekstrakcją i usuwaniem artefaktów ruchowych; CMRR >115 dB przy 50/60 Hz", z datą „publikacja ~2023 `[wniosek, streszczenie, jedno źródło]`".

**Poprawka:** Dabbaghian, Yousefi, Fatmi, Shafia, Kassiri, *„A 9.2-g Fully-Flexible Wireless Ambulatory EEG Monitoring and Diagnostics Headband With Analog Motion Artifact Detection and Compensation"*, **IEEE Trans Biomed Circuits Syst 13(6):1141–1151 (2019)**, PMID 31443050.

Trzy rzeczy były przekręcone: rok (**2019**, nie ~2023), klasa urządzenia (**opaska na elastycznym podłożu poliimidowym**, nie układ scalony), i przypisany parametr — **CMRR >115 dB nie występuje w tym źródle**. Parametry podane w abstrakcie: wzmocnienie 260 V/V, pasmo DC–300 Hz, masa 9,2 g z baterią, elektrody suche bezkontaktowe.

**Co zostaje w mocy:** teza, że analogowe usuwanie artefaktów **ruchowych** jest zajęte. Jest, i to od 2019.

**Co się zmienia:** to nie jest praca o kompensacji z kanału odniesienia i nie dotyczy artefaktów szczękowych. Szczelina z K-009 jest odrobinę szersza, niż wynikało z błędnego opisu.

---

### K-030 — CMRR układu ADS1299 to −110 dB, nie −120 dB

**Co było źle:** `06_TABELA_PARAMETROW.md` sekcja 2 podawała „CMRR ADS1299: −120 dB" ze statusem „parametr katalogowy, trzy niezależne opisy — najpewniejsza liczba w tym pliku".

**Poprawka, ze strony producenta (Texas Instruments):** CMRR **−110 dB**. Szum wejściowy **1 µV p-p przy paśmie 70 Hz** — ta liczba jest potwierdzona i pozostaje bez zmian. Rozdzielczość 24 bity, wzmocnienie programowane 1–24, 250 SPS – 16 kSPS.

**Dlaczego ten wpis jest pouczający mimo drobnej skali:** to była liczba oznaczona jako **najpewniejsza w całym pliku**, na podstawie „trzech niezależnych opisów" — i była błędna o 10 dB. Zgodność trzech streszczeń nie jest weryfikacją, jeżeli wszystkie trzy przepisują od siebie.

---

### K-031 — 16,6 bit/min pochodzi z badania na czterech osobach

**Czego dotyczy:** liczby „SSVEP douszne, online: 87,9 ± 12,1%, ITR 16,6 ± 6,6 bit/min", używanej w `06`, `07` i `09`.

**Weryfikacja:** liczby są **poprawne co do wartości** — Wang Y-T., Nakanishi, Kappel, Kidmose, Mandic, Wang Y., Cheng, Jung, EMBC 2015, PMID 26736745. Offline 82,71 ± 11,83% przy oknie 4 s, online 87,92 ± 12,10%, ITR 16,60 ± 6,55 bit/min, cztery klasy.

**Czego brakowało:** **badanie objęło czterech uczestników.** Odchylenie standardowe rzędu 12 punktów procentowych przy n=4 oznacza, że ta liczba jest orientacyjna, a nie ustalona. Nigdzie tego nie zapisałem, a podawałem tę liczbę jako punkt odniesienia dla całej formy dousznej.

**Reguła operacyjna, która z tego zostaje:** przy każdej liczbie z literatury podawać **liczbę badanych**. Bez niej liczba nie znaczy tego, co się wydaje, że znaczy — dokładnie tak, jak wymaga sekcja 10.G handbooka wobec naszych własnych liczb.

---

### K-032 — Front Neurosci 2024: „~80%" dotyczy czego innego, niż napisałem

**Co było źle:** `06` sekcja 2 i `01` sekcja 2 podawały „wykrywalność alfa w zapisie dousznym: ~80% zapisów".

**Poprawka, z abstraktu** (Moumane i in., *Front Neurosci* 18:1441897, 2024, PMID 39319310, **30 uczestników**): „In around 80% of cases, **cross-correlation analysis between in-ear and scalp signals** … revealed significant correlations with scalp EEG (p < 0.01)". To jest odsetek przypadków z istotną korelacją między sygnałem dousznym a skalpowym, a **nie** odsetek zapisów, w których wykryto alfę.

**Co przy okazji potwierdzone i przydatne:** mniejsza amplituda alfy i nieco niższy SNR w uchu niż na skalpie; oraz — istotne dla osi projektu — „intermittent signal alterations were noticed in the in-ear recordings during nap sessions, **attributed to movements of the head and facial muscles**".

---

### K-033 — konkurencja EEG na ISEF rośnie szybko, i mam na to liczby

**Czego dotyczy:** sekcji 6 `08_KONKURENCJA_ISEF.md`, gdzie ryzyko konkurencyjne na ISEF było oznaczone jako „realne i udokumentowane" na podstawie jednego projektu.

**Ustalenie:** przeszukanie bazy abstraktów Society for Science, słowo kluczowe „EEG", rocznik po roczniku:

| Rok | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | **2026** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| projektów | 7 | 5 | 8 | 14 | 10 | 12 | 11 | 7 | 7 | 10 | 8 | 15 | **22** |

Dla frazy „brain-computer interface": 0 do 5 rocznie, w 2026 — **5**.

**Wniosek:** liczba projektów EEG na ISEF **potroiła się w dwa lata** (8 → 15 → 22). W samym ENBM 2026 obok projektu referencyjnego startowały m.in. ENBM079 (tani EEG z otwartym BCI, trzecia nagroda) i ENBM042 (nieinwazyjny interfejs dwukierunkowy). To nie jest nisza.

---

### K-034 — Explory: pole neuro jest niemal puste, i mam na to liczby

**Czego dotyczy:** zadania 4d nr 11 i argumentu użytkownika z sekcji 9.3 handbooka, dotąd niezweryfikowanego.

**Ustalenie:** lista wszystkich projektów **półfinałowych Explory 2026** (`glosuj.explory.pl`, plebiscyt „Bilet na Finał") liczy **133 pozycje**. Projektów opartych na EEG: **jeden** — „Aletheia — Rozpoznawanie emocji za pomocą EEG i AI". Do finału **nie przeszedł**. W oficjalnej liście finalistów 2026 (`Wyniki_Polfinal_2026.pdf`, 21 projektów) **nie ma ani jednego projektu EEG ani BCI**. W finale 2025 (22 projekty) również nie ma.

**Wniosek: argument użytkownika z sekcji 9.3 handbooka jest potwierdzony liczbowo** — ~0,75% zgłoszeń półfinałowych, zero w finale, w dwóch kolejnych edycjach.

**Ale wniosek strategiczny jest odwrotny do intuicyjnego** i wart zapisania: skoro sito jest w Explory (K-003), a konkurencja tematyczna jest na ISEF (K-033), to **projekt konkuruje o wejście z projektami z zupełnie innych dziedzin, a o nagrodę — z projektami z tej samej**. To są dwa różne zadania i optymalizacja pod nie nie jest ta sama.

---

### K-035 — żywica z certyfikatem ISO 10993 jest dostępna dla amatora. Luka zamknięta

**Czego dotyczy:** `05_RYNEK.md` sekcja 5.3, `[luka]` blokująca decyzję zakupową od rundy drugiej: „nie ustaliłem, czy istnieje żywica z certyfikatem ISO 10993-5/-10 dostępna dla osoby prywatnej w Polsce, w rozsądnej cenie, do zwykłej drukarki MSLA".

**Odpowiedź: tak, istnieje.** **Liqcreate Bio-Med Clear** — deklarowana zgodność z ISO 10993-5 (cytotoksyczność), ISO 10993-10 (uczulenie) i ISO 10993-23 (podrażnienie), przeznaczona dla **zwykłych desktopowych drukarek MSLA/LCD/DLP** wymienionych z nazwy: Phrozen, Elegoo, Creality3D, Anycubic. Dostępna w polskich sklepach (2B3D, 3DUV), rząd ceny **456 zł za 0,5 kg**.

**Konsekwencja:** obejście z sekcji 5.3 (kupna silikonowa końcówka douszna na wydrukowanym korpusie) **przestaje być konieczne**, choć pozostaje sensowne jako wariant tańszy i wygodniejszy. Rekomendacja „wstrzymać zakup Qidi Q2, kupić tanią drukarkę żywiczną" jest teraz kompletna: znany jest zarówno sprzęt, jak i materiał.

**Warunek, którego nie wolno pominąć:** biozgodność deklarowana jest **po obróbce końcowej zgodnej z wytycznymi producenta** (mycie, doświetlanie). Wydruk niedomyty nie jest biozgodny niezależnie od tego, co pisze na butelce.

---

## 2026-08-15, sesja druga — po decyzjach użytkownika

### K-036 — „większy rozstaw elektrod to większy zysk i jest on fizyczny" jest NIEPRAWDĄ dla SSVEP

**Co było źle:** `09_UMIEJSCOWIENIE.md` sekcja 5b, tabela porównawcza wariantu zwartego i rozłożonego. Wpisałem tam, że przy wariancie rozłożonym „amplituda różnicowa **duża. To jest główny zysk i on jest fizyczny**", a przy zwartym — „mała, bo bliskie punkty na skalpie mają podobny potencjał". Z tego wyprowadziłem, że wariant rozłożony (potylica ↔ wyrostek sutkowaty) ma przewagę sygnałową nad modułem zwartym.

**Dlaczego to nie wynika:** pomyliłem **amplitudę** z **stosunkiem sygnału do szumu**. Większy rozstaw rzeczywiście daje większą amplitudę różnicową — ale referencja położona daleko zbiera też **nieskorelowany szum i zakłócenia**, których referencja bliska nie zbiera, bo one są dla obu elektrod wspólne i odejmują się. O klasyfikacji decyduje SNR, nie amplituda.

**Trzy źródła, wszystkie w tę samą stronę:**

1. **Zhang, Valsecchi, Gegenfurtner, Chen, *„Laplacian reference is optimal for steady-state visual-evoked potentials"*, J Neurophysiol 130(3):557–568 (2023), PMID 37492903.** Systematyczne porównanie czterech metod referencji — monopolarnej, uśrednionej po wszystkich elektrodach, **uśrednionych wyrostków sutkowatych** i **laplasjanowej** — na **siedmiu zbiorach** (cztery własne, trzy publiczne). Wynik: **referencja laplasjanowa daje najwyższy SNR i najlepszą powtarzalność między sesjami**. Referencja na wyrostkach sutkowatych — czyli dokładnie wariant rozłożony — wypada gorzej.
2. **Diez, Mut, Laciar, Avila, *„A comparison of monopolar and bipolar EEG recordings for SSVEP detection"*, EMBC 2010, PMID 21096910.** Pięciu badanych, cztery częstotliwości. Zapis **bipolarny z bliskich par** (O1–P3, O2–P4) dał **80,1%** trafności wobec **74,5%** dla zapisu monopolarnego z referencją odległą (Fz).
3. **Luo i in., *„Boosting Spatial Properties of Single-Flicker SSVEP via Laplacian Electrodes"*, EMBC 2025, PMID 41335820.** Trzecie, niezależne potwierdzenie kierunku.

**Poprawna wersja:** dla SSVEP **optymalna jest referencja lokalna** — elektroda czynna w miejscu maksimum sygnału minus średnia z kilku elektrod otaczających, w odległości rzędu 2–3 cm. Cytat z Zhang 2023: referencja laplasjanowa „is especially advantageous for SSVEP experiments where short preparation time is preferred as it requires only data from the maximally activated electrode and **a few surrounding electrodes**".

**Konsekwencja, i jest ona wprost korzystna dla projektu:**

Wariant rozłożony z łukiem przez tył głowy do zausznika **nie ma przewagi sygnałowej, którą mu przypisywałem** — ma za to wszystkie swoje koszty: przewód jako antena na 50 Hz i źródło artefaktu tryboelektrycznego, złącze w torze, dwa punkty mocowania, oraz kształt, który użytkownik odrzucił jako zbliżający się do opaski.

**Moduł zwarty na potylicy z układem laplasjanowym jest jednocześnie lepszy sygnałowo, prostszy konstrukcyjnie i zgodny z ograniczeniem gabarytowym.** Trzy rzeczy naraz, co się rzadko zdarza.

**Kto wyłapał:** użytkownik, poleceniem „zweryfikuj czy elektrody w 2 miejscach aż tak dużo zmieniają. Jak nie, to lecimy dalej z potylicą". Odpowiedź: **nie zmieniają, zmieniają na gorsze.** Intuicja była trafna.

---

### K-037 — licencje trzech kluczowych zbiorów danych: sprawdzone, wszystkie CC-BY 4.0

**Czego dotyczy:** `[luka]` postawionej w `07_DEKODOWANIE.md` sekcja 7 i `04` sekcja 5.1 — „licencji nie sprawdziłem dla żadnego zbioru, przed użyciem czegokolwiek licencja musi być sprawdzona".

**Sprawdzone bezpośrednio na stronach PMC:**

| Zbiór | Licencja | Gdzie leżą dane |
|---|---|---|
| Lee i in. 2021, ear-EEG + skalp, ERP i SSVEP w ruchu, 24 osoby | **CC-BY 4.0** | skrypty: `github.com/youngeun1209/MobileBCI_Data` |
| **Zhu i in. 2021, wearable SSVEP, 102 osoby, elektrody mokre I suche** | **CC-BY 4.0** | **FigShare 10.6084/m9.figshare.13560281** oraz `bci.med.tsinghua.edu.cn/download.html` |
| Wang Z., Shi N. i in. 2023, SpiralE, Nature Communications | **CC-BY 4.0** | Zenodo 10.5281/zenodo.7748035; **surowe EEG tylko na życzenie u autorów** |

**CC-BY 4.0 oznacza: wolno używać, przetwarzać i publikować wyniki, pod warunkiem podania autorstwa.** To wystarcza zarówno wobec standardów etycznych Explory (Załącznik nr 1), jak i wobec wymogu ISEF o poszanowaniu własności intelektualnej. **Luka zamknięta.**

---

### K-038 — istnieje drugi publiczny zbiór, trafiony w projekt jeszcze lepiej niż pierwszy

**Czego dotyczy:** uzupełnienia K-027.

**Zbiór:** Zhu, Jiang, Dong, Gao, Wang, *„An Open Dataset for Wearable SSVEP-Based Brain-Computer Interfaces"*, **Sensors 21(4):1256 (2021)**, PMID 33578754.

**Zawartość: 102 osoby**, 8 kanałów, zadanie SSVEP z **12 celami**, po 10 kolejnych bloków — **osobno elektrodami mokrymi i osobno suchymi**, dla każdej osoby.

**Dlaczego to jest ważniejsze niż zbiór z K-027 dla tego konkretnego projektu:**

Projekt zmierza do modułu potylicznego z **elektrodami suchymi**, paradygmat **SSVEP**, kilka–kilkanaście komend. Ten zbiór to dokładnie to zadanie, na **102 osobach**, z gotowym porównaniem sucha-mokra wykonanym przez kogoś innego. Daje:

1. **punkt odniesienia dla własnej elektrody** — „moja sucha elektroda wobec suchej i mokrej ze zbioru na 102 osobach" jest twierdzeniem znacznie mocniejszym niż „moja elektroda działa"
2. **materiał do pracy nad dekodowaniem od zaraz**, bez żadnego sprzętu
3. **realistyczne widełki**, czego się spodziewać po elektrodach suchych, zanim cokolwiek zostanie zbudowane

**Uwaga do zapisania, bo działa w drugą stronę:** skoro istnieje publiczny zbiór 102 osób z porównaniem elektrod suchych i mokrych, to **twierdzenie „zbadałem elektrody suche" jest zajęte**. Nasze twierdzenie musi dotyczyć **konkretnej konstrukcji elektrody albo konkretnego toru analogowego**, mierzonego przeciwko temu zbiorowi — nie samego faktu, że elektrody suche zbadano.

---

### K-039 — „cztery komendy na minutę" to była moja pomyłka, i to ona popchnęła decyzję użytkownika

**Co było źle:** `10_PROJEKT_DLA_LAIKA.md` sekcja 4.1. Napisałem najpierw poprawnie — „wybrać jedną komendę z kilku, patrząc na nią, **mniej więcej co 1–4 sekundy**" — a trzy akapity niżej: „**cztery komendy na minutę** to nie jest szybkie pisanie. To jest tempo pilota do telewizora". **Te dwa zdania sobie przeczą.** Komenda co 1–4 s to **15–60 komend na minutę**, nie cztery.

**Skąd wzięła się ta pomyłka:** z sekcji 4c `00_PYTANIA_I_LUKI.md`, gdzie napisałem „**cztery komendy** co ~2 s wystarczają do gładkiego ruchu". Tam „cztery komendy" oznaczało **rozmiar alfabetu** — lewo, prawo, jazda, stop. Zamieniłem rozmiar alfabetu na tempo.

**Liczby poprawne, z pracy odczytanej w oryginale:** Xing i in., *Scientific Reports* 8:14708 (2018), PMID 30279463 — **12 celów, elektrody suche typu pazurkowego, okno 1-sekundowe, 93,2% trafności, ITR 92,35 bit/min**, jedenastu badanych. To odpowiada **rzędowi 30–40 wyborów na minutę**.

**Dlaczego ten wpis jest poważny mimo prostoty błędu:** użytkownik podjął na tej podstawie decyzję C2, uzasadniając ją wprost: *„4 komendy na minutę to naprawdę średnio. I to bardzo."* **Reagował na liczbę, którą podałem błędnie, zaniżoną o rząd wielkości.** Decyzja o wyborze wariantu przepustowościowego pozostaje w mocy i jest sensowna — ale została podjęta na złej przesłance i to musi być zapisane.

**Reguła operacyjna:** nie mieszać **liczby komend** (rozmiar alfabetu, N we wzorze Wolpawa) z **tempem** (wyborów na minutę) ani z **przepustowością** (bit/min). To są trzy różne wielkości i w tym pliku pomyliłem dwie z nich.

---

### K-040 — moja własna korekta K-028 była przesadzona. SpiralE to 2,2×, nie rząd wielkości

**Co było źle:** w K-028 napisałem, że praca SpiralE daje wynik „**o rząd wielkości** powyżej wszystkiego, co wcześniej raportowano z ucha", i że „40-celowy speller online bez kalibracji to przepustowość o rząd wielkości wyższa niż 16,6 bit/min". Oparłem to na **abstrakcie**, w którym podano liczbę celów, ale nie podano ITR.

**Poprawka, z pełnego tekstu** (Nature Communications 14:4213, PMC10349124, odczytany w całości):

> „the decoding accuracies of the in-ear channels are 95% in the offline 9-target SSVEP task and **75% in the online 40-target SSVEP task without training**. The **Information Transfer Rate (ITR) reaches 36.86 ± 15.53 bits/min**, which is the highest to those reported in the previous ear EEG results"

**Czyli: 36,86 bit/min, nie „rząd wielkości powyżej 16,6".** To jest **około 2,2×** — poprawa realna i największa w tej niszy, ale nie skokowa. Dokładność w zadaniu 40-celowym to **75%**, nie 95%; liczba 95% dotyczy 9 celów offline.

**Czego to nie zmienia:** wniosek jakościowy K-028 stoi — o wyniku zdecydowała **jakość kontaktu elektrody**, a nie odległość od kory wzrokowej, i liczby 6–17 bit/min nie są sufitem formy dousznej. Decyzja o potylicy (K-036) była podjęta na innej przesłance i pozostaje słuszna.

**Co to zmienia, i jest to korzystne:** po wyborze potylicy **projekt nie konkuruje ze SpiralE**. Punkt odniesienia dla wariantu przepustowościowego to **Xing 2018: 92,35 bit/min na elektrodach suchych**, a nie 36,86 bit/min z ucha. Potylica daje ~2,5× najlepszego opublikowanego wyniku z ucha — i to jest argument za tą decyzją, a nie przeciw.

**Czego się z tego uczę, i jest to nieprzyjemne:** przesadziłem w korekcie, która sama była korektą przesady w drugą stronę. Najpierw zaniżyłem pułap formy dousznej na streszczeniach z 2015 i 2022, potem zawyżyłem go na abstrakcie z 2023. **Obie pomyłki miały to samo źródło: liczba czytana bez pełnego tekstu.** Dopiero trzecie podejście, z pełnym tekstem, dało wartość, którą można cytować.

---

## 2026-08-15, audyt całkowity etapu 1

### K-042 — przeniosłem oś projektu z ucha na potylicę wbrew własnemu zapisowi

**Co było źle:** `09_UMIEJSCOWIENIE.md` sekcja 4 mówi wprost: *„Przeniesienie na potylicę nie unieważnia projektu, ale **wymaga wyprowadzenia osi od nowa** — nie da się jej przenieść mechanicznie, bo problem szczęki tam nie dominuje."* Po decyzji o potylicy (K-036) **przeniosłem oś mechanicznie** i wpisałem „kompensacja artefaktu szczękowego" do `DECYZJE.md` jako wkład własny, nie sprawdzając, czy przesłanka Kappela (mierzona dla ucha) obowiązuje na potylicy.

**Jak się to skończyło:** przeniesienie okazało się **przypadkowo trafne** — Kołodziej i in. 2026 mierzyli na O1/O2/Oz i ustalili, że kanał szczękowy jest jednym z dwóch najskuteczniejszych kanałów pomocniczych. Ale trafność wyszła z cudzej pracy, nie z mojego rozumowania, i gdyby wyszło inaczej, oś projektu byłaby zbudowana na przesłance z innego miejsca na głowie.

**Reguła:** kiedy własny dokument mówi „to wymaga wyprowadzenia od nowa", to nie jest uwaga stylistyczna.

---

### K-043 — trzy kandydujące twierdzenia projektu są zajęte. Pełny rozbiór: `12_AUDYT.md`

**1. „Tani interfejs SSVEP o wysokim ITR"** — Teversham i in., Imperial College, EMBC 2022, PMID 36086083: **~£20, ESP32, 95,56% dokładności, ITR 102 bit/min**. Więcej niż Xing 2018 przy ułamku kosztu.

**2. „Mały suchy czujnik przez włosy na potylicy"** — Kim i in., Georgia Tech, ***PNAS* 122(15):e2419304122 (2025)**, PMID 40193612: mikroczujniki między mieszkami włosowymi, **96,4% SSVEP bez treningu, także podczas chodzenia i biegu**, 12 h noszenia, najniższa raportowana gęstość impedancji kontaktu, **zgłoszenie patentowe w toku**.

**3. „Kanał pomocniczy do usuwania artefaktów z potylicznego SSVEP"** — **Kołodziej, Majkowski, Wiszniewski, Politechnika Warszawska, *Sensors* 26(3):917, 31 I 2026**, PMID 41682433: O1/O2/Oz plus kanały pomocnicze (Cz, Fp1, HEOG, kark, policzek, **szczęka**), regresja liniowa, 12 osób, **+9,1 pp (SVM) i +9,9 pp (CNN)**; najskuteczniejsze kanały to **Cz i szczęka**.

**Co przeżyło:** redukcja artefaktu **na etapie akwizycji** — wskazana jako przyszła praca przez samych autorów pozycji 3, cytat w `12_AUDYT.md` sekcja 2.1. Przeszukanie pod analogową kompensację w torze: **zero trafień**.

---

### K-044 — nazwany konkurent z terminem

`[wniosek]` Grupa z Wydziału Elektrycznego Politechniki Warszawskiej **sama wskazała redukcję artefaktów na etapie akwizycji jako następny krok**, w pracy ze stycznia 2026. Ma kompetencje i motywację, żeby to zrobić.

**Najbardziej prawdopodobny scenariusz utraty pierwszeństwa to publikacja tej grupy w latach 2026–2027.** Ryzyko rzędu dziesiątek procent, nie jednostek.

**Skutek operacyjny, wiążący:** w żadnym materiale zgłoszeniowym nie może paść słowo **„pierwszy"**. Twierdzenie zostaje pomiarowe i przeżywa cudzą publikację jako niezależne potwierdzenie na własnym sprzęcie.

---

### K-045 — konflikt Cz: najlepsze rozwiązanie leży poza dopuszczalną formą

`[fakt]` Kołodziej i in. ustalili, że najskuteczniejsze kanały pomocnicze to **Cz i szczęka**. **Cz to wierzchołek głowy** — a ograniczenie gabarytowe z decyzji 3 wyklucza konstrukcje nad czubkiem głowy.

Trzy wyjścia: zrezygnować z Cz i przyjąć mniejszy zysk (ile — nieznane); znaleźć zamiennik bliżej potylicy; albo **zmierzyć, ile korzyści przeżywa bez Cz**.

`[wniosek]` Trzecie jest osobnym, publikowalnym pytaniem — „ile z redukcji artefaktów da się uzyskać przy ograniczeniu do elektrod mieszczących się w module noszonym" — i jest bezpośrednio o wykonalność formy, czyli o rzecz, na której użytkownikowi zależy od początku.

---

### K-046 — reguła 12 miesięcy: ekstrapolacja zamieniona na wzorzec

**Czego dotyczy:** K-023 opierał się na jednym roczniku (2026–2027) i przenosił regułę na nasz rok jako `[wniosek]`.

**Sprawdzone w oryginałach trzech roczników:** ISEF **2024** — „may not include research performed before **January 2023**", okno „**January 2023 – May 2024**". ISEF **2025** — „before **January 2024**", okno „**January 2024 – May 2025**". ISEF **2027** — „before **January 2026**", okno „**January 2026 – May 2027**".

**Wzorzec stabilny na trzech rocznikach: styczeń roku poprzedzającego ISEF – maj roku ISEF.** Okno dla ISEF 2028 to **I 2027 – V 2028** i przestaje to być ekstrapolacja. Kampanię pod ISEF startować w maju 2027 — bez zmian, ale teraz na twardej podstawie.

---

### K-047 — WYCOFUJĘ K-029 w części. Pierwsza sesja miała rację

**Co było źle — w mojej korekcie, nie w oryginale:** w K-029 uznałem, że opis „8-kanałowy IC EEG ambulatoryjny z w pełni analogową ekstrakcją i usuwaniem artefaktów ruchowych, ~2023" jest błędny, i „poprawiłem" go na *„A 9,2-g Fully-Flexible Wireless Ambulatory EEG Monitoring and Diagnostics Headband"* (2019) — twierdząc, że to nie jest układ scalony i że rok jest zły.

**Poprawka, z Crossref:** obie prace istnieją i są różne, tej samej grupy (laboratorium H. Kassiriego):
- Dabbaghian, Yousefi, Fatmi, Shafia, Kassiri, **TBioCAS 13(6):1141–1151 (2019)** — opaska na elastycznym podłożu
- **Dabbaghian A., Kassiri H., *„An 8-Channel Ambulatory EEG Recording IC With In-Channel Fully-Analog Real-Time Motion Artifact Extraction and Removal"*, IEEE TBioCAS, 2023, DOI 10.1109/tbcas.2023.3289159** — **układ scalony, ośmiokanałowy, 2023**
- oraz ISCAS 2020, ten sam kierunek, IC bez ADC

**Pierwsza sesja opisała to poprawnie.** Mój błąd polegał na znalezieniu pierwszej pracy o zbliżonym tytule i uznaniu, że to ta sama.

**Co z K-029 zostaje w mocy:** wyłącznie zastrzeżenie, że **parametru CMRR >115 dB nie zweryfikowałem** w żadnej z tych prac. Reszta wycofana.

**Wzorzec, który trzeba nazwać:** to trzeci przypadek w tej sesji, gdy przesadziłem w korekcie — po K-040 (zawyżenie wyniku SpiralE na podstawie abstraktu) i po tym wpisie. **Koryguję zbyt pewnie, na pierwszym znalezionym dopasowaniu.** Reguła: przed skorygowaniem cudzego namiaru sprawdzić, czy autorzy nie mają kilku prac o zbliżonym tytule i czy różnica nie jest realna.

**Konsekwencja merytoryczna dla projektu:** analogowa kompensacja artefaktów **ruchowych** jest zajęta mocniej, niż wynikało z mojej korekty — na poziomie układu scalonego, 2023. **Nasza oś dotyczy artefaktu mięśniowego, nie ruchowego, i to rozróżnienie staje się przez to ważniejsze**, a nie mniej ważne. Do wypowiedzenia wprost przed jurorem.

---

## 2026-08-15, plan podniesienia szans (wolna ręka wg sekcji 11 handbooka)

### K-048 — nie policzyłem wielkości kategorii ISEF, a to była największa dźwignia projektu

**Co było źle:** w `ISEF_ARKUSZE_OCENY.md` sekcji 4.1 i w `08` sekcji 6 zapisałem „rozważyć kategorię EBED zamiast ENBM" i **odłożyłem to do etapu 2 jako rzecz wymagającą sprawdzenia liczby zgłoszeń**. Sprawdzenie zajęło jedno zapytanie do bazy abstraktów.

**Liczby, rocznik 2026:**

| Kategoria | Projektów | Z nagrodą | Odsetek | Z „EEG" |
|---|---|---|---|---|
| ENBM | **98** | 39 | 40% | **6** |
| **EBED** | **49** | 21 | **43%** | **0** |
| ROBO | 61 | 22 | 36% | kilka |

**EBED ma o połowę mniejszą stawkę, wyższy odsetek nagrodzonych i zero konkurencji tematycznej.** Podkategorie (Circuits, Sensors, Signal Processing) pasują do projektu, którego wkładem jest tor analogowy, lepiej niż ENBM.

**Konsekwencja liczbowa:** warunkowe szanse na ISEF rosną z 30–40% na 35–45% dla Grand Award i z 12–18% na 15–20% dla miejsca I–II. **To jest największa zmiana szans w całym projekcie i nie kosztuje ani złotówki, ani godziny pracy.**

**Dlaczego to jest błąd, a nie tylko zaniedbanie:** zapisałem „do sprawdzenia w etapie 2" przy pozycji, która wymagała jednego zapytania i zmieniała ocenę całego przedsięwzięcia. **Odkładanie taniego sprawdzenia o dużej stawce jest tym samym błędem co budowanie na niesprawdzonym założeniu**, tylko wolniejszym.

---

### K-049 — ustawiłem projektowi punkt odniesienia, którego nie da się osiągnąć

**Co było źle:** w `DECYZJE.md` wpisałem jako punkt odniesienia dla wariantu przepustowościowego **Xing 2018, 92,35 bit/min**.

**Dlaczego to błąd taktyczny:** Xing to Instytut Półprzewodników Chińskiej Akademii Nauk z własną technologią elektrod pazurkowych, a Imperial College osiąga 102 bit/min. **Ustawianie tej poprzeczki gwarantuje przegraną w porównaniu, którego żaden regulamin nie wymaga.**

**Poprawka:** punkt odniesienia **wewnętrzny i podwójny** — ten sam układ bez kompensacji (twierdzenie o wkładzie) oraz kupiony OpenBCI (twierdzenie o sensie własnego sprzętu). Liczby z literatury idą do tabeli kontekstowej. Jedynym zewnętrznym odniesieniem, do którego porównujemy się wprost, zostaje **Kołodziej i in. 2026 (+9 pp cyfrowo)**, bo mierzy to samo zjawisko.

---

### K-050 — przyjmuję zarzut użytkownika o zaniżaniu szans w Explory

**Zarzut:** *„z twojej matematyki wynika, że wszystkie finałowe mają podobne szanse"*, przy bezpośredniej obserwacji użytkownika, że wzorcowy był **jeden** projekt inżynierski na 21 finałowych.

**Zarzut trafny.** `P(reprezentacja | finał) = 25%` przy bazie 14% było założeniem ostrożnościowym („lepszy od średniej, niedominujący"), a nie wnioskiem z danych.

**Dane za wyższą liczbą:** wszystkie trzy kryteria finału (§7 pkt 3) sprzyjają działającemu urządzeniu — doskonałość wykonania z rekwizytami i prototypem, praktyczna stosowalność, oddziaływanie społeczne; oraz **7 z 10 Nagród Głównych w latach 2016–2025 to projekty inżynieryjno-konstrukcyjne**.

**Dane trzymające poniżej 60%:** reprezentacja na ISEF 2026 to **dwa projekty biologiczne i jeden materiałowy, zero elektroniki** — sygnał, że siła inżynierska nie przekłada się wprost na wybór do reprezentacji.

**Podniesione z 25% na 40%.** Pełne przeliczenie: `13_PODNIESIENIE_SZANS.md` sekcja 8.

---

# SESJA 17 VIII 2026 — zmiana kierunku projektu

### K-051 — szukałem nieobsadzonego problemu zamiast nieobsadzonego pomiaru

**Co było źle:** przy wyborze nowego projektu przez sześciu kolejnych kandydatów stosowałem filtr „czy ten problem jest już zajęty". Sześć razy odpowiedź brzmiała „tak" — bo **problemy ważne ekonomicznie są z definicji zajęte**, ważność ekonomiczna przyciąga finansowanie. Kandydat nr 3 (fototermiczna identyfikacja czarnych tworzyw) padł, bo Fraunhofer IZFP opublikował to samo w marcu 2026 i trzy dni przed sesją wszedł z tym w próby przemysłowe.

**Dlaczego to błąd, a nie pech:** filtr był niezgodny z wnioskiem z własnego audytu etapu 1. Kształt, który tam przeżył trzy przejścia, brzmiał: **znany problem + znane rozwiązanie + konkretna wariacja, której efektu nikt nie zmierzył, porównywana wewnętrznie.** Arkusz inżynierski ISEF nie ma kryterium nowości względem literatury, a regulamin Explory §7 pkt 2a dopuszcza alternatywę „innowacyjny **i/lub** wnosi dodatkową wartość".

**Poprawka:** kryterium wyboru to wykonalność, demonstracja, głębokość pomiaru, obsada kategorii i podział na dwa pytania — **nie nowość**. Pełny rejestr sześciu odrzuconych: `24_ODRZUCONE_KANDYDATY.md`.

---

### K-052 — teza „jeden strzał" była mocniejsza, niż pozwalają fakty

**Co było źle:** sekcja 3 handbooka twierdzi, że cykl 2027→2028 jest jedyny użyteczny, bo następny koliduje z maturą. Cała strategia stała na tym zdaniu.

**Co sprawdzone:** `[fakt]` matura obowiązkowa (polski, matematyka, język obcy) wypada **4–6 maja**; rozszerzenia są rozłożone od 7 do 21 maja. ISEF odbywa się konsekwentnie **9–16 maja** (2025: 10–16 V Columbus; 2026: 9–15 V Phoenix).

**Czyli: matura obowiązkowa nie koliduje z ISEF.** Kolidują wyłącznie te rozszerzenia, które wypadną w tygodniu ISEF-u. Do tego istnieje **termin dodatkowy w czerwcu**, przyznawany przez dyrektora OKE na udokumentowany wniosek.

**Czego to nie znosi** `[luka]`: przepis mówi o przyczynach **losowych lub zdrowotnych**, a zaplanowany wyjazd trudno tak nazwać. **Nie zakładam, że termin dodatkowy zostanie przyznany** — to jest pytanie do OKE, do zadania jesienią 2028, nie w kwietniu 2029.

**Skutek:** cykl dwuletni (dwa podejścia do Explory: 2027 i 2028) jest wykonalny, a nie wykluczony. `[fakt]` Explory nie ma reguły 12 miesięcy, a formularz wprost pyta o zgłoszenie w poprzednich edycjach. ISEF obsługuje kontynuację formularzem 7, wymagając, żeby rok kolejny był „new and different" i pokazywał „significant progress"; samo powtórzenie badania z większą próbą jest **zakazane**.

---

### K-053 — nie sprawdziłem najtańszej rzeczy o największej stawce dla celu nadrzędnego

**Co było źle:** cel nadrzędny użytkownika to studia w USA. Przez całą pracę nad projektem ani razu nie sprawdziłem, ile takie studia kosztują i czy są finansowo osiągalne — a to jest przesłanka, na której stoi sens całego przedsięwzięcia.

**Co sprawdzone:** `[fakt]` **MIT prowadzi rekrutację need-blind i pokrywa 100% udokumentowanej potrzeby finansowej także dla obcokrajowców** — jest jedną z dziewięciu uczelni w USA, które robią jedno i drugie. Od roku akademickiego 2025/26 studenci z rodzin o dochodzie **poniżej 200 000 USD rocznie studiują bez czesnego**.

**Znaczenie:** MIT jest finansowo **najłatwiejszą**, a nie najtrudniejszą z amerykańskich opcji. Większość uczelni z górnej półki jest wobec obcokrajowców need-aware, czyli tam brak środków realnie obniża szanse przyjęcia.

**Reguła operacyjna, która z tego zostaje:** sprawdzać przesłanki celu nadrzędnego, nie tylko przesłanki zadania bieżącego. To jest ten sam wzorzec co K-048 — odkładanie taniego sprawdzenia o dużej stawce.

---

### K-054 — pisałem w liczbie mnogiej o projekcie, który ma jednego autora

**Co było źle:** w całej sesji używałem form „my", „nasz", „zaciągnąłem nas". Projekt jest **indywidualny i jego autorem jest użytkownik**; rola modelu jest doradcza.

**Dlaczego to nie jest kwestia stylu:** `[fakt]` Regulamin Explory, Załącznik nr 1, opiera standardy etyczne na Kodeksie Etyki Pracownika Naukowego PAN; reguły ISEF wymagają, żeby praca była własna, a udział osób trzecich jawnie deklarowany. Liczba mnoga w materiałach idących do jury **zaciemnia autorstwo**, a to jest kategoria, w której obie imprezy dyskwalifikują.

**Poprawka:** liczba pojedyncza w dokumentacji projektu i we wszystkich materiałach zgłoszeniowych. Wpisane do `30_POWROT_DO_INTERFEJSU.md` sekcja 6a.1 jako reguła.

---

### K-055 — zaprojektowałem demonstrację, która wchodziła wprost na ścieżkę zakazaną w sekcji 9.2 handbooka

**Co było źle:** zaproponowałem makietę przyłóżkową, w której urządzenie **wypowiada syntetyczną mową całe zdania** wybrane jednym wskazaniem. To jest ten sam rejestr co projekt referencyjny ENBM074 (2026): rozstrzyganie intencji z małego zbioru w zastosowaniu komunikacyjnym.

**Kto to złapał:** użytkownik, słowami „oj powoli nas ciągnie to w kierunku projektu Kharade".

**Co jest gorsze od samego błędu:** `08_KONKURENCJA_ISEF.md` sekcja 2.3 **przewidywała ten dryf co do słowa** — „»sterowanie dyskretne z ośmioma komendami« a »rozstrzyganie intencji z ośmiu możliwości« to jest ta sama rzecz opisana dwoma językami". Ostrzeżenie było zapisane, przeczytane w tej samej sesji i mimo to złamane.

**Poprawka:** mowa syntetyczna wypada. Zostaje sterowanie fizycznymi przedmiotami (decyzja C1). Metryka: **dokładność i przepustowość w bitach, nigdy słowa na minutę** — to jest jedyna linia trzymająca granicę.

**Ustalenie przy okazji, z abstraktu:** słowo „paradygmat" w tytule tamtej pracy dotyczy **poziomu zadania, nie poziomu sygnału**. `[luka]` Jakiego paradygmatu sygnałowego użyto, abstrakt nie podaje i nie ustaliłem tego w sieci. `[wniosek]` Warunek kontrolny opisany jako „conventional speller" i baseline 3 wpm wskazują, że warstwa detekcji była standardowa i dobrze znana.

---

### K-056 — projektowałem demonstrację wymagającą budowania rekwizytów

**Co było źle:** makieta przyłóżkowa oznaczała godziny warsztatu, które nie idą w interfejs. Użytkownik postawił warunek, żeby interfejs przyszedł na półfinał **w całości, a nie jako prototyp** — a wtedy każda godzina włożona w rekwizyt działa przeciw temu warunkowi.

**Poprawka:** **obiekty demonstracyjne kupowane, nigdy budowane.** Żarówka i gniazdko sterowane bezprzewodowo, poniżej 200 zł, zero godzin warsztatu.

**Efekt uboczny, korzystny:** `[wniosek]` kupiony, rozpoznawalny przedmiot jest **lepszym dowodem uczciwości** niż zbudowany. Przy własnej makiecie pierwsze pytanie brzmi „co jest w środku"; przy żarówce ze sklepu nie pada.

---

# SESJA 17 VIII 2026 — analiza stawki finałowej Explory 2026

### K-057 — liczby lejka Explory były zaniżone w mianowniku

**Co było źle:** wszystkie moje oszacowania stały na „~300 zgłoszeń". `[fakt]` Oficjalna informacja prasowa FZT z 1 VI 2026: **377 projektów zgłoszonych**, ponad 130 w półfinale, **20 w finale plus 1 z plebiscytu**.

**Skutek:** przejście zgłoszenie → półfinał to **~34%, nie 44%**. Pierwsze sito jest ostrzejsze, niż zakładałem.

---

### K-058 — podałem błędny skład obszaru „Poza kategoriami"

**Co było źle:** `13_PODNIESIENIE_SZANS.md` wymieniał tam nanokompozyt, szczepionkę przeciw Salmonelli i fagi T7. **Wszystkie trzy są na liście rezerwowej.**

**Prawidłowy skład:** BioShield, ReakcjON, kwercetyna, **Kolano Pneumatyczne, SADE**.

**Dlaczego to ma znaczenie merytoryczne, a nie tylko porządkowe:** poprawka **potwierdza** ustalenie, które bez niej wisiało w powietrzu — najlepiej oprzyrządowany plakat całej stawki (nanokompozyt: SEM, XRD, TGA, hipertermia magnetyczna, słupki błędu) jest na rezerwie, a plakat z jednym renderem CAD i ankietą szkolną (Kolano Pneumatyczne) jest finalistą **w tym samym obszarze**.

---

### K-059 — nagrody SDG są niższe i jest ich mniej, niż zakładały wszystkie pliki

**Co było źle:** handbook i ściągawka podawały **3 × 7 500 zł** i rozstrzygały rozbieżność „regulamin 7500 vs ABC 5000" na korzyść regulaminu.

**Co jest:** `[fakt]` informacja prasowa z 1 VI 2026 — **3 × 5 000 zł**, w obszarach Człowiek i Społeczeństwo, Klimat i Środowisko, Gospodarka i Bezpieczeństwo.

**Rzecz istotniejsza od kwoty:** **obszar „Poza kategoriami" nie ma nagrody SDG.** Wybór tego obszaru oznacza utratę prawa do niej w ogóle — czego żaden wcześniejszy plik nie uwzględniał przy analizie wyboru obszaru.

---

### K-060 — zabiłem kandydata, który wszedł do finału Explory

**Co było źle:** odrzuciłem kamerę akustyczną do wykrywania nieszczelności argumentem „zostaje tylko »taniej«, Fluke ma opublikowaną metodę kwantyfikacji".

**Co się okazało:** `[fakt]` **ALP — Acoustic Leak Positioning**, Julia Biały (solo), ZSME Tarnów: czujniki MEMS na rurze, FFT, przetwarzanie na brzegu, **91% skuteczności klasyfikacji**, autorskie oprogramowanie CAD. **Finalista Explory 2026**, 23 punkty w mojej skali, szóste miejsce na 21.

**Na czym polegał błąd:** zastosowałem filtr skalibrowany pod arkusz ISEF do decyzji, która rozstrzyga się na Explory. To dwa różne sita o różnych kryteriach i **filtr z jednego nie przenosi się na drugie**.

---

### K-061 — zawyżałem własne oszacowanie noty finałowej

**Co było źle:** oceniałem projekt użytkownika po zmianach na **26–29 punktów na 30**.

**Po zobaczeniu stawki:** górny koniec to **25 punktów** (kwantowe wspomaganie fotowoltaiki, BIO-VOLT). Zrównanie się z nimi jest realne, wyraźne pobicie nie.

**Poprawka: 25–27 z treningiem prezentacyjnym, 24–26 bez.** Skutek dla `P(Nagroda Główna | finał)`: z 18% na **~15–19%**.

---

### K-062 — praca całej sesji wylądowała na gałęzi niewidocznej dla nowej rozmowy

**Co się stało:** cała praca z 17 VIII 2026 została zacommitowana na `claude/isef-engineering-project-pjunzg`, podczas gdy `origin/main` stała na commicie z 15 VIII. Nowa sesja użytkownika otworzyła `main` i **nie zobaczyła ani jednego pliku z tej sesji** — brakowało listy uczelni, zadań, analizy stawki i wszystkich korekt.

**Kto to złapał:** użytkownik, słowami „zgłaszasz mi, że nie masz pełnej listy uczelni (…) Może znowu błąd z gałęzią czy czymś?".

**Dlaczego to jest błąd, a nie techniczna drobnostka:** `CLAUDE.md` zawiera regułę „commituj na tę gałąź, na której wylądowałeś, i nie zajmuj użytkownika gałęziami". Zastosowałem ją literalnie i **nie sprawdziłem, czy gałąź, na której wylądowałem, jest tą, którą otworzy następna sesja.** Efekt: dokumentacja, która miała przetrwać przeniesienie do nowej rozmowy, nie przetrwała — czyli zawiodła w jedynym zadaniu, do którego istnieje.

**Poprawka:** gałęzie zsynchronizowane. **Reguła operacyjna: przy zamykaniu sesji sprawdzić `git diff --name-status origin/main HEAD` i zsynchronizować, jeżeli cokolwiek jest tylko na gałęzi roboczej.**

**Rzecz do zapamiętania szerzej:** dokumentacja niewidoczna dla następnej sesji nie jest dokumentacją. Wpisanie czegoś do pliku nie kończy zadania — kończy je sprawdzenie, że plik jest tam, gdzie ktoś go otworzy.

---

## 2026-08-17, noc

### K-063 — terminy OITwEiM w plikach są z wygasłej edycji, a nowa ma etap, o którym nikt nie wiedział

**Co było źle:** `08_KONKURENCJA_ISEF.md` sekcja 4.1, `13_PODNIESIENIE_SZANS.md` i `21_PLAN_BUDOWY.md` opisywały olimpiadę jednym terminem — „prace i wideo do ~20 IV". To był termin **edycji 2025/2026** i on nie obowiązuje.

**Co jest:** `[fakt]` regulamin edycji **2026/2027** jest opublikowany (PZSWiR, lipiec 2026) i ma inny kalendarz: **rejestracja Komitetu Szkolnego do 31 X 2026**, wyniki etapu szkolnego do 9 I 2027, prace do okręgu do 27 II 2027, wyniki okręgu do 13 III 2027, **praca i wideo z prototypem do 27 III 2027**, wyniki finału do 15 V 2027.

**Dlaczego to jest błąd kosztowny, a nie porządkowy:** bez zarejestrowanego Komitetu Szkolnego uczeń **nie startuje w ogóle**, a termin rejestracji wypada **dwa i pół miesiąca od dziś**. Plan zakładał zajęcie się olimpiadą wiosną 2027 — przy takim planie olimpiada odpadłaby bezgłośnie jesienią 2026, a dowiedzielibyśmy się o tym w kwietniu.

**Poprawka druga, mniejsza:** `08` pisał „konkurs ogólnopolski, **indywidualny**". Regulamin dopuszcza **zespoły 2–3-osobowe**, także międzyszkolne. Dla tego projektu bez znaczenia (jest indywidualny), ale opis konkurencji był fałszywy: w finale 2026 zdecydowana większość prac to zespoły.

**Skutek dla harmonogramu:** termin działającego prototypu przesuwa się z maja 2027 (półfinał Explory) na **27 III 2027**, czyli o sześć tygodni w lewo. Do wpisania przy przeliczaniu planu pod jeden cykl.

**Gdzie to teraz mieszka:** `33_KONKURSY_ROZBIEGOWE.md` sekcje 2 i 5.

---

### K-064 — przenosiłem noty ze skali Explory na konkursy, które oceniają czym innym

**Co było źle:** w rozmowie o El-Robo-Mech operowałem notami z `31_ANALIZA_STAWKI_2026.md` tak, jakby były miarą ogólnej jakości projektu.

**Co się okazało:** `[fakt]` **Stacja SKA** — u mnie 22 punkty i **dziesiąte miejsce na 21** w skali Explory — **wygrała El-Robo-Mech 2026** (I miejsce ex aequo) i zdobyła **II miejsce w OITwEiM**. `[fakt]` **ALP** (u mnie 23 pkt) — **III miejsce w OITwEiM**.

**Na czym polegał błąd:** ten sam co K-060, tylko w drugą stronę. Explory ocenia oddziaływanie społeczne i zrozumiałość dla laika; El-Robo-Mech i OITwEiM oceniają kompletność wykonania, wartość użytkową, nakład pracy i — w olimpiadzie — nowość i estetykę dokumentacji. **Skala z jednego sita nie mierzy drugiego.**

**Konsekwencja, która działa na korzyść projektu:** jury El-Robo-Mech to czterech pracowników naukowych politechniki i dwóch inżynierów z przemysłu. Tam własny tor analogowy i budżet niepewności czytają się bez tłumaczenia — czyli **te dwa konkursy stoją bliżej arkusza ISEF niż Explory**.

---

### K-065 — El-Robo-Mech nazywany „lekką akredytacją" — nie jest żadną

**Co było źle:** rozważanie konkursu w kategorii „lekka akredytacja". K-016 mówił to już jakościowo; teraz są liczby.

**Liczby edycji XI:** `[fakt]` ponad 20 zgłoszeń → **15 prac w finale** → **14 prac nagrodzonych, 34 laureatów**. Przejście do finału ~75%, nagroda dla ~93% finalistów.

**Poprawka:** El-Robo-Mech nie odróżnia. Jego wartość to **dry-run przed jury technicznym i wymuszony termin** — i ta wartość jest realna. Wartość akredytacyjna: zero, w szczególności zerowa wobec celu „studia w USA", bo nagrodą jest indeks jednej polskiej uczelni.

**Odróżnienie od olimpiady:** OITwEiM przy ~63 pracach na finale przyznaje **10 tytułów laureata w kraju**. To jest odróżnienie realne i to jest jedyna pozycja z tej trójki, która czyta się w amerykańskiej rubryce „Honors".

---

### K-066 — „przywileje rekrutacyjne laureata OITwEiM" pisane bez sprawdzenia

**Co było źle:** `08` sekcja 4.1, `11_OCENA_SZANS.md` i `13` uzasadniały wybór olimpiady zdaniem o „przywilejach rekrutacyjnych", traktując je jak fakt.

**Co jest w regulaminie:** `[fakt]` regulamin mówi wyłącznie o **zaświadczeniu** wydanym wg rozporządzenia MENiS z 29 I 2002 (Dz.U. 2020 poz. 1036) oraz o tytule „Młodego Innowatora". Konkretne ulgi rekrutacyjne ustalają **uchwały senatów poszczególnych uczelni** i nie zostały sprawdzone.

**Poprawka:** pozycja oznaczona `[luka]` w `33_KONKURSY_ROZBIEGOWE.md` sekcja 4.2. Przy celu „studia w USA" i tak drugorzędna — argumentem za olimpiadą jest tytuł krajowy i wymuszony termin, nie polskie punkty rekrutacyjne.

---

### K-067 — nazwałem sito europejskie „łagodniejszym", nie sprawdziwszy, czym ono rekrutuje

**Co było źle:** w sekcji 2.8.3 pliku `32` napisałem, że TU Delft ma „sito rekrutacyjne nieporównanie łagodniejsze niż amerykańskie", i zbudowałem na tym rekomendację Europy jako planu awaryjnego. Zdanie było postawione na wskaźniku przyjęć, bez sprawdzenia **kryteriów**.

**Kto to złapał:** użytkownik, słowami „europejskie uczelnie z tego co kojarzę niezbyt sobie cenią osiągnięcia typu ISEF. Bardziej ich interesuje egzamin".

**Co jest:** `[fakt]` TU Delft prowadzi na aerospace **numerus fixus (440 miejsc)** i selekcję złożoną z **dwóch testów** — Academic Aptitude Assessment i Selection Exam (online, pod nadzorem, wyłącznie wielokrotny wybór, z matematyki, fizyki i wstępu do lotnictwa) — przeliczanych na jeden wynik i numer w rankingu. **W procedurze nie ma CV, listu motywacyjnego ani portfolio.** `[fakt]` ETH Zurych wymaga od polskiej matury **egzaminu wstępnego po niemiecku** plus certyfikatu językowego, a zdający wchodzi rok później.

**Na czym polegał błąd:** porównywałem dwa sita po jednej liczbie (odsetek przyjęć), zamiast po tym, **co każde z nich mierzy**. Amerykańskie mierzy między innymi dorobek; europejskie mierzy egzamin. Dla kandydata z mocnym projektem i przeciętnym wynikiem egzaminu sito europejskie jest **trudniejsze**, nie łatwiejsze. Ta sama klasa błędu co K-060 i K-064: **filtr z jednego konkursu przeniesiony na drugi bez sprawdzenia kryteriów.** Trzeci raz.

**Poprawka merytoryczna, ważniejsza od samego sprostowania:** wartość tego projektu jest **asymetryczna geograficznie** — w USA przelicza się na przyjęcie, w stypendiach za osiągnięcia na pieniądze, w Europie kontynentalnej **na nic formalnie**. To wzmacnia zasadę pierwszeństwa z sekcji 4 pliku `32`: przy kolizji o czas **projekt ustępuje maturze i SAT**, bo matura jest jedyną walutą w wariancie europejskim.

**Reguła do zapamiętania:** zanim nazwę jakiekolwiek sito łatwiejszym, mam sprawdzić, **co ono punktuje**, a nie ilu przepuszcza.

---

### K-068 — liczba „3–4× wyższy wskaźnik przyjęć" nie istnieje jako dana i wychodzi z dokumentacji

**Co było źle:** `32_STUDIA_USA.md` sekcja 3 nosiła od 17 VIII zapis `[domysł, źródło słabe]` o tym, że finaliści ISEF mają 3–4× wyższy wskaźnik przyjęć, a laureaci 5–6×, z adnotacją „do zweryfikowania". **Zostawienie liczby w pliku z etykietą „słabe źródło" jest półśrodkiem** — po kilku tygodniach etykieta blednie, a liczba zostaje.

**Co ustalono przy zamykaniu pozycji R5:** `[fakt]` twierdzenie występuje wyłącznie w materiałach firm doradztwa rekrutacyjnego, bez wskazania źródła pierwotnego. Society for Science publikuje fact sheety ISEF i wyróżnienia absolwentów — **nie publikuje statystyk rekrutacyjnych**. Żadna uczelnia nie podaje wskaźnika przyjęć w rozbiciu na osiągnięcia kandydatów. To samo dotyczy krążącej liczby „23% przyjętych na MIT startowało w konkursach naukowych".

**Poprawka:** liczba **wykreślona**, nie oznaczona. Zastąpiona jedynymi twardymi danymi, jakie istnieją — sekcja C7 Common Data Set, odczytana z oryginalnego PDF-u Caltechu (2024/2025): **extracurricular activities „Important", talent/ability „Considered"**, przy „Very Important" dla trudności programu, wyników testów, esejów, rekomendacji i oceny charakteru.

**Reguła:** liczby, której nie da się doprowadzić do źródła pierwotnego, nie zostawia się w dokumentacji z ostrzeżeniem. Się ją usuwa i zapisuje, dlaczego.
