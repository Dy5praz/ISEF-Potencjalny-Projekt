# DECYZJE — cztery rzeczy, które czekały na Ciebie

**Data:** 15 sierpnia 2026, po zamknięciu etapu 1
**Status: TRZY Z CZTERECH ROZSTRZYGNIĘTE 15 VIII wieczorem.**

## Odpowiedzi

| # | Decyzja | Rozstrzygnięcie |
|---|---|---|
| **1** | C2 — w czym „lepsze od komercyjnych" | **OTWARTA.** Zawężona do wariantów 2 i 3. Propozycja wyjścia z wahania: sekcja „Domknięcie decyzji 1" niżej |
| **2** | umiejscowienie elektrod | **ZAMKNIĘTA: moduł zwarty na potylicy.** Zgoda na geometrię jako zmienną mierzoną, ale weryfikacja pokazała, że drugie miejsce elektrod **pogarsza** wynik. Bez łuku, bez zausznika. `KOREKTY.md` K-036 |
| **3** | skala gabarytu | **ZATWIERDZONA**, z Twoim zastrzeżeniem wpisanym jako granica twarda: **żadnej konstrukcji zbliżającej się do opaski przechylonej na tył głowy** |
| **4** | E1 — kalendarz | **PRZYJĘTY.** Wchodzi do handbooka jako obowiązujący |

**Komisja IRB i formalności:** użytkownik zgłasza, że nie będzie z tym problemu. Pozycja schodzi z listy ryzyk.

---

## Domknięcie decyzji 1 — propozycja, nie rozstrzygnięcie

Wahasz się między wariantem 2 (metryka użytkowa) a 3 (przepustowość). **Nie musisz teraz wybierać, i uważam, że nie powinieneś** — z tego samego powodu, dla którego zgodziłeś się nie wybierać umiejscowienia założeniem.

**Te dwa warianty wykluczają się w abstrakcie, nie w laboratorium.** Abstrakt na ISEF ma 250 słów i musi mieć jedno twierdzenie. Ale kampania pomiarowa mierzy ten sam układ — pod wariant 3 potrzeba dokładności i liczby komend na minutę, pod wariant 2 tych samych sesji, tylko rozłożonych w czasie i powtórzonych. **Nakład to nie dwie kampanie, tylko jedna dłuższa.**

**Propozycja:** zapisać oba twierdzenia w planie eksperymentalnym **przed pierwszym pomiarem**, zbierać dane pod oba, a wybrać główne dopiero wtedy, gdy będzie widać, która liczba wyszła mocniej.

**Warunek, bez którego to jest nadużycie, a nie strategia:** oba muszą być zapisane z góry i **oba muszą być raportowane**. Wybieranie po fakcie metryki, która wypadła najlepiej, i przemilczenie drugiej, ma w nauce nazwę i jest jednym z tych zachowań, które Załącznik nr 1 regulaminu Explory wymienia wprost jako naruszenie (krytycyzm wobec własnych wyników). Pokazujemy obie, jedną nazywamy główną.

**Co przemawia za każdym, w skrócie:**

| | Wariant 2 — metryka użytkowa | Wariant 3 — przepustowość |
|---|---|---|
| za | pole praktycznie nieraportowane; nie da się przegrać z cudzą liczbą | jest z czym porównywać; liczba jest zrozumiała dla każdego jurora |
| przeciw | juror może uznać metrykę za skrojoną pod wynik | grupa z Tsinghua opublikowała w 2023 wynik z ucha, którego się nie pobije |
| haczyk | **metryki zależne od Twojego stanu (wyspanie, zmęczenie) łamią zwolnienie ISEF dla badania na sobie** — dryf sygnału w czasie noszenia wolno mierzyć, wpływ wyspania nie | brak |

Rozwinięcie dla laika: `10_PROJEKT_DLA_LAIKA.md` sekcja 6.

---

**Poniżej materiał, na którym te decyzje zapadły. Zostaje jako dokumentacja ścieżki decyzyjnej — arkusz inżynierski ISEF punktuje wprost `exploration of alternatives`.**

Pełne rozbiory zostają w plikach źródłowych — odsyłam przy każdej pozycji.

---

## Decyzja 1 — C2: w czym urządzenie ma być „lepsze od komercyjnych"

**Źródło:** `00_STRESZCZENIE.md` sekcja 1.2, `06_TABELA_PARAMETROW.md` sekcja 5, `00_PYTANIA_I_LUKI.md` sekcja 2.1

**Dlaczego to wraca do Ciebie:** w porannej wersji rozstrzygnąłem to rekomendacją na wariant 2. Rekomendacja stała na zdaniu „w przepustowości nie da się wygrać, bo SSVEP z ucha to 6–17 bit/min wobec ~92 z potylicy, i to jest geometria". **Ta liczba była nieaktualna o osiem lat** — praca z Nature Communications 2023 pokazuje z kanału słuchowego speller 40-celowy online bez kalibracji. Rekomendację wycofałem (`KOREKTY.md` K-028). Nie stawiam nowej, bo poprzednią postawiłem na niesprawdzonej liczbie i to jest dokładnie ten błąd, który kosztował ten projekt najwięcej.

### Trzy warianty, stan po weryfikacji

| | Wariant 1: przewaga przy stałej widoczności | Wariant 2: metryka użytkowa | Wariant 3: przepustowość |
|---|---|---|---|
| **twierdzenie brzmi** | „przy formie, której nie widać, osiągam X, gdzie dotychczasowe rozwiązania niewidoczne osiągają Y" | „montaż w sekundach, stabilność przez dzień, brak rekalibracji — tam, gdzie czapkę zdejmuje się po 20 minutach" | „ta forma sprzętowa osiąga ITR, którego nie osiągają inne rozwiązania w tej formie" |
| **baseline** | literatura ear-EEG. **Doszła pozycja, której nie miałem:** charakterystyka elektrofizjologiczna urządzeń komercyjnych, EMBC 2025 | prawie pusty — te metryki są **realnie nieraportowane** | literatura ear-EEG, w tym SpiralE |
| **status po etapie 1** | **wykonalny**, baseline słaby ale nie pusty | **wykonalny**, najwięcej wolnego miejsca | **wrócił do gry**, K-028 |
| **główne ryzyko** | juror zapyta „a czapka robi więcej" — i będzie miał rację | juror może uznać metrykę za skrojoną pod wynik | konkurencja: grupa z Tsinghua, Nature Communications |
| **ograniczenie formalne** | brak | **jest, i było przeoczone** — patrz niżej | brak |

### Ograniczenie, które doszło i dotyczy tylko wariantu 2

`[fakt, regulamin ISEF 2026–2027]` Zwolnienie dla badania na sobie obowiązuje pod dwoma warunkami: brak zagrożenia zdrowia **oraz brak wprowadzenia zmiennej ludzkiej**. Regulamin wymienia jako przykłady zmiennej ludzkiej wprost: `amount of sleep`, `strength or endurance of tester`.

| Co chcesz zmierzyć | Czy zwolnione |
|---|---|
| dryf jakości sygnału w ciągu dnia noszenia | **tak** |
| czas montażu, odsetek sesji bez rekalibracji | **tak** |
| jak wynik zależy od tego, ile spałeś / jak jesteś zmęczony | **nie** — wymaga zgody komisji IRB |

Wariant 2 da się zrobić w całości w wersji zwolnionej, ale **granica jest cienka i trzeba ją trzymać świadomie przy pisaniu planu eksperymentalnego**, a nie odkryć w marcu 2028. Rozbiór: `ISEF_HUMAN_PARTICIPANTS.md` sekcja 1.1.

### Czego ta decyzja NIE przesądza

Wariantów nie trzeba wybierać rozłącznie. Jeden jest **osią twierdzenia** (to, co idzie do abstraktu i na plakat), pozostałe mogą być tabelą towarzyszącą. Abstrakt ISEF ma limit **250 słów** i nie wolno w nim odwoływać się do cudzych prac poza minimum — to praktycznie wymusza, żeby oś była jedna.

**Czego potrzebuję od Ciebie: który wariant jest osią.** Reszta ustawi się sama.

---

## Decyzja 2 — umiejscowienie elektrod

**Źródło:** `09_UMIEJSCOWIENIE.md` w całości, szczególnie sekcje 3, 4 i 5b

**Stan:** decyzja otwarta od `KOREKTY.md` K-019 — potraktowałem formę „za uchem, wielkości aparatu słuchowego" jak wymaganie wejściowe, podczas gdy było Twoją odpowiedzią na wymaganie, a nie samym wymaganiem.

**Co się zmieniło po weryfikacji:** argument za potylicą **osłabł**. Opierał się na tym, że ucho oddaje 5–15× przepustowości. Po pracy SpiralE wiadomo, że duża część tej straty to **jakość kontaktu elektrody**, a nie odległość od kory wzrokowej. Potylica nadal daje silniejszy sygnał u źródła, ale nie jest to już argument rozstrzygający.

**Moja rekomendacja — bez zmian, i po K-028 jeszcze mocniejsza:**

> **Nie wybierać teraz. Zbudować jeden tor analogowy ze złączem i dwie wiązki elektrodowe — zauszną i zauszno-potyliczną. Ten sam paradygmat, ten sam wzmacniacz, ta sama osoba, dwie geometrie, pomiar.**

Cztery powody:
1. **zamienia moją pomyłkę w wynik** — decyzja podjęta założeniem zostaje podjęta pomiarem
2. **różnica, o którą się spieramy, jest dokładnie tym, co ten eksperyment mierzy** — a po K-028 nikt z nas nie wie, ile ona wynosi
3. **punktuje wprost** w rubryce Execution arkusza inżynierskiego ISEF: `prototype has been tested in multiple conditions/trials`
4. **zabezpiecza przed porażką jednej gałęzi** — jeżeli łuk przez tył głowy okaże się nie do opanowania szumowo, zostaje wariant zwarty plus pomiar pokazujący dlaczego

**Koszt:** złącze w torze analogowym to dodatkowe miejsce na zakłócenia i rezystancję przejścia. Trzeba je wybrać świadomie i zmierzyć jego wpływ osobno. Znany problem, nie niespodzianka.

**Pozycja, którą warto sprawdzić przed decyzją:** praca EMBC 2025 o **dwóch oddzielonych galwanicznie miniaturowych modułach zausznych z synchronizacją bezprzewodową** (PMID 41337113). To jest wariant rozłożony **bez przewodu**, czyli bez efektu tryboelektrycznego i bez anteny na 50 Hz — czyli bez głównego kosztu, który zapisałem przy wariancie rozłożonym. Nie czytałem jej w całości.

**Czego potrzebuję od Ciebie: zgody na tę drogę albo wskazania jednej geometrii.** Jeżeli zgoda — reszta jest planem, nie decyzją.

---

## Decyzja 3 — skala gabarytu: zatwierdzić albo poprawić

**Źródło:** `06_TABELA_PARAMETROW.md` sekcja 4, `09_UMIEJSCOWIENIE.md` sekcja 5a

**Dlaczego to w ogóle wymaga Twojej zgody:** handbook każe zrobić kolumnę „czy widać, że użytkownik to ma na sobie", ale nie podaje progu. **Bez progu ta kolumna jest opinią, a opinii nie da się porównać między wierszami tabeli.** Ty rozstrzygnąłeś 15 VIII, że kryterium to **gabaryt, nie widoczność** („może być nawet widoczne… pod warunkiem, że będą mniejsze, a nie cała stacja pomiarowa"). Poniżej to samo zapisane operacyjnie.

| Przechodzi | Nie przechodzi |
|---|---|
| moduł do rozmiaru aparatu słuchowego lub słuchawki dousznej | cokolwiek wielkości pudełka |
| kilka takich modułów, także z tyłu głowy, także widocznych | konstrukcja przechodząca **nad czubkiem głowy albo przez czoło** |
| cienki przewód lub łuk między modułami, przy głowie | pasek pod brodą, opaska czołowa |
| łączna masa noszona rzędu kilkudziesięciu gramów | plecak, pasek, moduł zewnętrzny na kablu |
| — | **cokolwiek typu hełm — granica twarda, powtórzona przez Ciebie dwa razy** |

**Kolejność ustępstw przy konflikcie**, wg Twojej odpowiedzi („jak już nic ci nie wyjdzie, to w pierwszej kolejności tnij trochę na niewidoczności"):
1. gabaryt i widoczność
2. wygoda długiego noszenia
3. **nigdy: konstrukcja typu hełm**

**Jedna rzecz do wykreślenia, i jest to nowe ustalenie formalne.** W `06` sekcja 4 zaproponowałem, żeby widoczność mierzyć testem na stoisku: zdjęcie osoby w urządzeniu i pytanie do widza „gdzie ono jest". `[fakt]` Regulamin ISEF traktuje to jako **ankietę opinii publicznej o wynalazku i wymaga uprzedniej zgody komisji IRB**: *„This includes surveys conducted regarding potential use or opinions of the invention or consumer product by the general public."* Nie wolno tego zrobić spontanicznie przy stoisku. Albo procedura zgody, albo pomysł odpada.

**Czego potrzebuję od Ciebie: „tak" na tabelę powyżej, albo poprawka w konkretnym wierszu.** To jest pięć sekund, a odblokowuje kolumnę w tabeli porównawczej.

---

## Decyzja 4 — E1: potwierdzenie korekty K-001

**Źródło:** `00_PYTANIA_I_LUKI.md` sekcja 1.1, `KOREKTY.md` K-001

**Rzecz do potwierdzenia:** handbook w sekcji 3 podawał „do działającego prototypu ~14 miesięcy (El-Robo-Mech)". To błąd arytmetyczny. Poprawny rozkład:

| Kamień milowy | Data | Od 14 VIII 2026 |
|---|---|---|
| zamknięcie okna zgłoszeń Explory | 28 II 2027 | ~6,5 mies. |
| **działający prototyp, konkurs wiosenny** | ~IV 2027 | **~8 mies.** |
| półfinał Explory | V–VI 2027 | ~9–10 mies. |
| **start kampanii pomiarowej pod ISEF** | **V 2027** | **~9 mies.** |
| finał krajowy, Gdynia | X 2027 | ~14 mies. |
| ISEF | V 2028 | ~21 mies. |

Czternaście miesięcy to dystans do **finału krajowego**, nie do prototypu. Margines do pierwszego twardego terminu sprzętowego jest o **43% krótszy**, niż podawał handbook.

**Co doszło po weryfikacji regulaminu ISEF:** wiersz „start kampanii pomiarowej" jest nowy. Reguła 12 miesięcy brzmi inaczej, niż zakładał handbook — nie ma w niej liczby 18 (`KOREKTY.md` K-023). Okno to **styczeń 2027 – maj 2028**, z dowolnym ciągłym blokiem dwunastu miesięcy w środku. Praktycznie: **wszystko przed majem 2027 to prace rozwojowe** (liczą się na Explory i na konkurs wiosenny bez ograniczeń), a formalna kampania pod ISEF zaczyna się w maju 2027.

**Czego potrzebuję od Ciebie: potwierdzenia, że przyjmujesz tę tabelę jako kalendarz roboczy.** Jeżeli tak, wchodzi do handbooka jako obowiązująca i przestaję ją powtarzać.

---

## Poza decyzjami — trzy rzeczy do zrobienia poza komputerem

Żadnej z nich nie da się załatwić po mojej stronie. Wszystkie na jesień 2026, w tej kolejności:

1. **Mail do FZT** (`konkurs@fzt.org.pl`): czy organizator prowadzi SRC pełniące funkcję komisji IRB dla polskich uczestników ISEF. **Jedno pytanie, które może skasować punkt 2.**
2. **Rozmowa z dyrekcją szkoły**: czy da się powołać komisję IRB w składzie **nauczyciel inny niż opiekun projektu + dyrektor lub wicedyrektor + pielęgniarka szkolna lub psycholog**. Wymagane, żeby przebadać kogokolwiek poza sobą. Najdłuższy proces w całym harmonogramie formalnym i jedyny zależny od osób trzecich.
3. **Pisemna zgoda opiekuna szkolnego** na role Adult Sponsor i Direct Supervisor. Magister wystarcza na obie (`KOREKTY.md` K-020, K-021). Tanie, bez terminu, zdejmuje ryzyko.

Rozbiór formalności: `ISEF_HUMAN_PARTICIPANTS.md`.

---

## Czego świadomie nie rozstrzygam

**Paradygmat** (SSVEP kontra słuchowy kontra wyobrażenie ruchu) — należy do etapu 2 i zależy od decyzji 1 i 2. Stan przesłanek: SSVEP wygląda najlepiej i po K-028 wygląda znacznie lepiej niż rano; paradygmaty słuchowe są podważone pomiarem na 19 osobach (N1-P2 nie wychodzi w konfiguracji dousznej); wyobrażenie ruchu z ucha jest `[luka]` — praca o rytmie mu badała **ruch rzeczywisty, nie wyobrażony**.

**Kategoria ISEF** (ENBM kontra EBED) — do etapu 2, wymaga sprawdzenia liczby zgłoszeń w obu kategoriach, bo nagród jest proporcjonalnie do zgłoszeń. Sygnał: w ENBM 2026 startowało kilka projektów EEG naraz; EBED ma podkategorie **Sensors** i **Signal Processing**, gdzie ten sam układ ocenia juror od elektroniki, a nie od medycyny. Rozbiór: `ISEF_ARKUSZE_OCENY.md` sekcja 4.1.
