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
