# 21 — Odpowiedzi na pytania użytkownika, 16 sierpnia 2026

Pytania o prior art, definicję sukcesu, przesiew pod kątem R1, granicę interfejsów nieinwazyjnych i o to, czy projekt jest wart zachodu.

---

## 1. Czy naprawdę sprawdziłem, czy ktoś nie zmierzył tego, co robimy

**Odpowiedź krótka: sprawdziłem pięć baz i jedną dołożyłem dzisiaj po Twoim pytaniu. Osi nikt nie zajął. Dwie bazy pozostają niesprawdzone i mówię, które.**

### 1.1 Co przeszukałem dla NOWEJ osi

| Baza | Kiedy | Wynik |
|---|---|---|
| **PubMed** (E-utilities) | 16 VIII, rano | 7 zapytań, pięć po **0 trafień**; najbliższa praca: Wu i Su 2014 |
| **Crossref** | 16 VIII | 5 zapytań bibliograficznych, w czołówce nic o odległości odniesienia |
| **arXiv** | 16 VIII | 96 prac o SSVEP w całym arXiv, żadna o elektrodzie odniesienia |
| **Google Patents** | 16 VIII | 5 zapytań; trafienia to eye tracking, zestawy nagłowne, ogólne BCI. **Nic o odległości odniesienia** |
| **Europe PMC** | **16 VIII, po Twoim pytaniu** | **baza, której wcześniej nie użyłem** — 4 zapytania, dwie pozycje wymagające sprawdzenia, obie sprawdzone niżej |

### 1.2 Dwie pozycje, które Europe PMC wyrzuciła i które musiałem przeczytać

**a) *Streamlining cVEP Paradigms: Effects of a Minimized Electrode Montage on BCI Performance*, Brain Sciences 15(6):549, 2025, PMID 40563723.**

To jest najbliższa praca, jaką znalazłem w którejkolwiek bazie. **38 badanych, badanie online**, redukcja liczby elektrod z 16 do 6.

Cytat z wniosków: *„for a substantial number of participants, the classification pipeline **fails** after electrode removal, highlighting individual differences"*.

**Czy zajmuje naszą oś: nie.** Trzy różnice:
- pytają o **liczbę elektrod czynnych**, my o **odległość elektrody odniesienia**. To są różne zmienne — u nich odniesienie było stałe
- paradygmat **cVEP**, nie SSVEP
- nie dotykają gabarytu urządzenia ani konstrukcji

**Ale jest to praca, którą trzeba cytować i której wynik nas dotyczy:** potwierdza niezależnie, że **redukcja montażu wywraca pipeline u części osób**, co jest dokładnie mechanizmem, który zmierzyłem na danych Kołodzieja i który zasila R1. **Dopisuję do bibliografii.**

**b) *A systematic evaluation of EEG electrode geometry for enhanced signals*, Sci Rep 16:18493, 2026, PMID 42000827.**

Tytuł brzmiał niepokojąco blisko. **Po przeczytaniu: „geometria elektrody" znaczy tam kształt pojedynczej elektrody** — nanostrukturalne złote elektrody suche w kształcie szpilek, impedancja ~300 kΩ przy 100 Hz, SNR SSVEP 1,27 dB wobec 1,30 dB dla mokrych Ag/AgCl. **To jest materiałoznawstwo elektrody, nie rozmieszczenie przestrzenne.** Nie zajmuje osi; potwierdza natomiast, że nisza „elektroda sucha" jest zatłoczona — czyli to, co audyt etapu 1 ustalił w sekcji 1.2.

### 1.3 Czego NIE sprawdziłem — mówię wprost

`[luka]` **OpenAlex i Semantic Scholar odmówiły ponownie, HTTP 429**, tak samo jak w etapie 1. To jest limit zapytań nałożony na adres tego środowiska, nie brak dostępu. **To są dwie duże bazy i ich brak jest realną dziurą.**

Dalej nieprzeszukane: **IEEE Xplore bezpośrednio** (pokryty pośrednio przez Crossref), **Scopus i Web of Science** (płatne), **literatura nieanglojęzyczna**, **prace dyplomowe i doktorskie**, **pełne teksty zastrzeżeń patentowych**.

### 1.4 Uczciwa liczba

`[wniosek]` Prawdopodobieństwo, że dokładnie ten pomiar — **przepustowość SSVEP w funkcji odległości elektrody odniesienia, w kontekście gabarytu urządzenia noszalnego** — jest już opublikowany i go przeoczyłem: **rzędu 10–15%**.

Dlaczego nie mniej: dwie duże bazy nieprzeszukane, a pytanie jest na tyle naturalne, że ktoś mógł je zadać przy okazji innej pracy i schować odpowiedź w rysunku pomocniczym, gdzie żadne zapytanie tytułowe go nie znajdzie.

Dlaczego nie więcej: pięć baz, w tym patentowa, dało zero trafień na wprost zadane pytanie, a najbliższe znalezione prace pytają konsekwentnie o **liczbę elektrod czynnych**, nie o odniesienie.

**I to jest powód, dla którego twierdzenie projektu nie zawiera słowa „pierwszy" (K-044) i zawierać nie będzie.** Przy twierdzeniu pomiarowym te 10–15% nie jest ryzykiem egzystencjalnym — degraduje wynik z „nowy" na „potwierdzony niezależnie".

### 1.5 Twoja narracja — jest lepsza niż moja

Zaproponowałeś: *„chciałem zbudować nieinwazyjny i wygodny interfejs, ale po drodze postanowiłem odpowiedzieć na pytanie: ile kosztuje nas realna wygoda?"*

**To jest mocniejsze niż to, co miałem w `15_PROJEKT.md`**, z trzech powodów:
1. **wyjaśnia, skąd wzięło się pytanie** — czyli daje rubryce `Research Problem` motywację, a nie tylko lukę w literaturze
2. **jest uczciwe wobec historii projektu** — pytanie faktycznie wzięło się z ograniczenia konstrukcyjnego, nie z przeglądu literatury
3. **jurorowi od elektroniki (EBED) mówi od razu, że to jest pytanie inżynierskie o kompromis**, a nie praca o mózgu

Jedno zastrzeżenie: samo „ile kosztuje wygoda" to opis **kosztu**. Do abstraktu musi dojść człon dodatni — **„…i gdzie leży najmniejszy gabaryt, który jeszcze działa"**. Rozbiór tego napięcia: `19_SZANSE_PO_ZMIANIE.md` §3.

---

## 2. Co znaczy „wymierny sukces konkursowy"

**Uczciwie: używałem tego określenia zbyt swobodnie i nigdy go nie zdefiniowałem.** Definiuję teraz.

**Wymierny sukces = wynik, który da się wpisać w jednym zdaniu do CV i który potwierdza osoba trzecia.** Nie „nauczyłem się projektować PCB", tylko coś, co ma nazwę, datę i wystawcę.

Liczba 63% z `19_SZANSE_PO_ZMIANIE.md` obejmuje **sumę** tych zdarzeń:

| Zdarzenie | Waga w CV |
|---|---|
| kwalifikacja do półfinału Explory (~150 ze ~300 zgłoszeń) | **niska** — to nie jest wyróżnienie, to przejście pierwszego sita |
| **finał Explory (21 projektów w kraju)** | **średnia** |
| nagroda finansowa Explory | wysoka |
| **wyjazd na ISEF jako reprezentant Polski** | **bardzo wysoka** |
| nagroda na ISEF | najwyższa |
| laureat OITwEiM (olimpiada, przywileje rekrutacyjne w PL) | wysoka w Polsce, **niska za granicą** |
| miejsce na El-Robo-Mech | niska — 34 laureatów (K-016) |

**Rozbicie tych 63% jest nierówne i to jest ważne przy Twoim pytaniu 6:** największą część tej liczby stanowią zdarzenia z dolnej części tabeli. **Sam półfinał Explory nie jest osiągnięciem, którym można wypełnić rubrykę w amerykańskim formularzu.**

**Wobec Twojego celu właściwe liczby są trzy, nie jedna:**

| | Prawdopodobieństwo | Po uwzględnieniu R1 (×0,8) |
|---|---|---|
| finał Explory | 42% | **34%** |
| **wyjazd na ISEF** | 17% | **14%** |
| **nagroda na ISEF** | 11% | **9%** |

---

## 3. Czy da się łatwiej rozpoznać, czy należysz do tych 10–30%

**Tak, i literatura z ostatnich dwóch lat mówi konkretnie czym.** To była dobra intuicja — pytanie jest badane wprost.

### 3.1 Co znaleziono

`[fakt]` **Velut, Thielen, Chevallier, Corsi, Dehais, *Imaging Neuroscience* 4, 2026** — *„Neurophysiological screening of individual variability for robust decoding in c-VEP-based BCI"*. 24 badanych. Pięć predyktorów odróżniających osoby o wysokiej skuteczności (>90%) od niskiej:

1. **korelacja między epokami** (R ≈ 0,80 u dobrych)
2. **amplituda międzyszczytowa flash-VEP** — odpowiedź na pojedynczy błysk
3. **większa moc pasma α**
4. większa moc pasma θ
5. niższa moc pasma δ

`[fakt]` **Thielen, *Biomed Phys Eng Express* 11(4), 2025, PMID 40494367** — niezależnie: *„Four flash-VEP features were found to significantly…"* przewidywać zmienność skuteczności. Badał też tętno, zmienność tętna i uwagę trwałą.

**Dwa niezależne zespoły wskazują na to samo: charakterystyka odpowiedzi na pojedynczy błysk plus moc alfa spoczynkowej.**

### 3.2 Co to znaczy praktycznie — przesiew na 20 minut

Zamiast pełnej sesji BCI (240 prób, ~22 min plus montaż i kalibracja), wykonać:

| Krok | Czas | Co mierzy |
|---|---|---|
| alfa spoczynkowa: 2 min oczy zamknięte, 2 min otwarte | **4 min** | stosunek mocy α; predyktor nr 3 |
| flash-VEP: ~200 pojedynczych błysków, uśrednienie | **~8 min** | amplituda międzyszczytowa; predyktory 1 i 2 |
| krótka próba SSVEP, 3 cele, 60 prób | **~5 min** | odpowiedź bezpośrednia |

**Około 20 minut przy pierwszym włączeniu sprzętu.** Wszystkie trzy pomiary są wykonalne na kupionej platformie w październiku 2026 i nie wymagają nic ponad to, co i tak kupujemy.

### 3.3 Zastrzeżenia, żeby tego nie przecenić

`[luka]` Oba źródła dotyczą **c-VEP**, nie SSVEP. Predyktory są prawdopodobnie wspólne, bo oba paradygmaty stoją na odpowiedzi kory wzrokowej na bodziec migający — ale to jest `[wniosek]`, nie fakt.

`[wniosek]` **Przesiew nie zastępuje pomiaru, tylko go przyspiesza.** Jeżeli wyjdzie źle, i tak trzeba zrobić pełną próbę SSVEP, zanim uznamy sprawę za rozstrzygniętą. Jego wartość polega na tym, że przy dobrym wyniku **zdejmuje niepewność już w październiku**, zamiast trzymać ją do lutego.

**Trzecie, niezależne potwierdzenie skali problemu:** praca cVEP z 38 badanymi (PMID 40563723) mówi, że po redukcji liczby elektrod pipeline **przestaje działać u znacznej części osób**. Czyli w naszym reżimie — mało kanałów, mały moduł — odsetek „nieskutecznych" jest **wyższy** niż ogólne 10–30%. To jest argument za tym, żeby przesiew zrobić w pierwszej kolejności.

**Wchodzi do `16_PLAN_EKSPERYMENTALNY.md` jako E0 i staje się pierwszym pomiarem w całym projekcie.**

---

## 4. Dlaczego jesteśmy ograniczeni do paradygmatów i gdzie leży granica

To jest najlepsze pytanie z całej listy, bo dotyka tego, czego projekt **nie** może obiecać.

### 4.1 Dlaczego paradygmat jest w ogóle potrzebny

**Termin: paradygmat** — narzucony z góry scenariusz, w którym użytkownik robi coś umownego (patrzy na migające pole, wyobraża sobie ruch ręki), żeby mózg wytworzył sygnał **duży, znany z góry i powtarzalny**.

`[fakt]` Elektroda na skórze głowy mierzy **zsumowany potencjał milionów neuronów**, przefiltrowany przez czaszkę. Czaszka jest **filtrem dolnoprzepustowym przestrzennie** — rozmywa obraz. Skutki:
- **amplituda:** jednostki do dziesiątek mikrowoltów, przy szumie własnym toru rzędu 0,1 µV i artefaktach mięśniowych o rząd większych niż sygnał
- **rozdzielczość przestrzenna:** centymetry. Nie widać pojedynczych neuronów ani małych skupisk
- **stosunek sygnału do szumu w pojedynczej próbie: poniżej jedności.** Sygnał wyłania się dopiero przez uśrednianie albo filtrację dopasowaną

**Dlatego „intencja" nie jest sygnałem, który da się odczytać.** Intencja to rozłożony wzorzec aktywności, którego EEG nie rozdziela przestrzennie. Paradygmat jest **sztuczką**: SSVEP działa, bo kora wzrokowa dosłownie wchodzi w rezonans z częstotliwością migania, więc szukamy **wąskiego prążka o znanej częstotliwości** — a to da się wyłuskać z szumu, którego jest więcej niż sygnału.

**To nie jest ograniczenie sprzętu. To ograniczenie fizyczne** w rozumieniu `03_SCIANY_FIZYCZNE.md` — lepszy wzmacniacz go nie znosi.

### 4.2 Co potrafią wersje inwazyjne i dlaczego

Elektroda w korze albo na jej powierzchni jest **przy źródle**: amplitudy miliwoltowe, rozdzielczość poniżej milimetra, dostęp do konkretnych obszarów (ruchowego, mowy). Dlatego inwazyjne interfejsy dekodują **próbę mówienia** wprost, bez paradygmatu, w tempie kilkudziesięciu słów na minutę.

**Różnica nie jest w algorytmie. Jest w tym, ile informacji dociera do przetwornika.**

### 4.3 Gdzie naprawdę stoi dekodowanie intencji nieinwazyjnie

Sprawdziłem literaturę z lat 2025–2026, bo pytanie zasługuje na aktualną odpowiedź, a nie na obiegową.

`[fakt]` **d'Ascoli, Bel, Rapin, Banville, Benchetrit, Pallier, King (Meta AI + CNRS), *Nature Communications* 16:10521, 26 XI 2025, PMID 41298362** — *„Towards decoding individual words from non-invasive brain recordings"*. **Siedem publicznych zbiorów plus dwa własne, 723 osoby, pięć milionów słów, trzy języki.**

Wnioski autorów, cytuję sens wiernie:
- **MEG dekoduje się lepiej niż EEG**, a **czytanie lepiej niż słuchanie**
- skuteczność rośnie z ilością danych treningowych i z uśrednianiem przy testowaniu
- tytuł brzmi *„Towards"*, a autorzy nazywają rzecz **otwartym wyzwaniem**

**Dwie rzeczy, które trzeba z tego wyciągnąć:**
1. **To jest dekodowanie słów SŁYSZANYCH ALBO CZYTANYCH, nie pomyślanych.** Bodziec jest znany eksperymentatorowi. To bliżej „czy mózg zareagował na to słowo" niż „co ten człowiek chce powiedzieć"
2. **MEG to nie jest urządzenie noszalne** — wymaga ekranowanej komory albo czujników optycznie pompowanych. Poza zasięgiem tego projektu i poza zasięgiem produktu

`[fakt]` **Mowa wyobrażona z EEG** — dwa przeglądy z 2026 roku (PMID 42198020, Sensors; PMID 42294101, Front Hum Neurosci). Obraz: pole jest **niejednorodne**, prace różnią się celem dekodowania i rozmiarem słownika tak bardzo, że autorzy przeglądu postulują, żeby **przestać traktować „mowę wyobrażoną" jako jeden problem**. Wymieniane ograniczenia: sygnał słaby, zaszumiony i niestacjonarny, zbiory małe i niestandaryzowane, metryki nieporównywalne.

`[wniosek]` **Przekład na Twoje pytanie: dekodowanie intencji nieinwazyjnie istnieje, ale w zamkniętych, małych słownikach i przy przepustowości niższej niż SSVEP.** Gdybyśmy poszli tą drogą, wylądowalibyśmy w polu, gdzie nawet duże zespoły nie mają powtarzalnych wyników, z urządzeniem wielkości aparatu słuchowego i jednym licealistą. **To jest droga do projektu bez wyniku.**

### 4.4 Realna granica dla nieinwazyjnego — liczby

| | Przepustowość | Uwaga |
|---|---|---|
| SSVEP, laboratorium, wysoka gęstość elektrod | **100–300 bit/min** | wymaga wpatrywania się w migający ekran |
| SSVEP, elektrody suche, 8 kanałów | 70–120 bit/min | Xing 2018, Imperial 2022 |
| SSVEP, 3 cele, zespół uczelniany | **27,5 bit/min** | Kołodziej 2026 — dolna półka literatury |
| mowa wyobrażona z EEG | **małe zamknięte słowniki** | brak powtarzalnych metryk |
| inwazyjne dekodowanie mowy | **60–80 słów/min** | bez paradygmatu, bez migania |

**Ograniczenie, które zostaje na zawsze:** żeby wyciągnąć sygnał spod szumu, potrzeba **czasu uśredniania**. To wiąże przepustowość z czasem w sposób, którego żadna elektronika nie obejdzie. Widać to wprost w naszym własnym pomiarze: ITR ma maksimum przy oknie 1 s i spada dla dłuższych — dokładność rośnie, ale wolniej niż czas (`14_REANALIZA.md` §5.1).

### 4.5 Jedyne legalne obejście, i warto je znać

**Projekt referencyjny ENBM074 obszedł ten sufit nie fizyką, tylko zmianą zadania** — rozstrzyganie intencji zamiast literowania (`08_KONKURENCJA_ISEF.md`). Zamiast wyciskać więcej bitów z mózgu, **zmniejszył liczbę bitów potrzebnych do wykonania zadania**.

`[wniosek]` To jest realna droga i handbook zabrania nam nią iść — nie dlatego, że jest zła, tylko dlatego, że byłaby wariantem cudzego rozwiązania (`HANDBOOK.md` §9.2). **Zapisuję ją jako znaną i świadomie nieużytą**, żeby nikt w przyszłej sesji nie „odkrył" jej ponownie.

---

## 5. Warto?

**Krótko: tak, ale nie z powodu, dla którego pytasz — i to jest ważniejsze niż samo „tak".**

### 5.1 Twarde liczby wobec Twojego celu

| Wynik | Prawdopodobieństwo (z R1) |
|---|---|
| wyjazd na ISEF | **14%** |
| jakakolwiek nagroda na ISEF | **9%** |
| miejsce I–II w kategorii ISEF | **2,4%** |

`[domysł — to nie jest moja dziedzina i oznaczam to wyraźnie]` Status finalisty ISEF jest rozpoznawalnym wyróżnieniem w rekrutacji amerykańskiej; nagroda w kategorii jest wyraźnie mocniejsza. Ale **nie jestem ekspertem od rekrutacji zagranicznej i nie należy traktować mojej oceny wagi tych wyróżnień jako wiarygodnej.**

**Gdyby projekt miał sens tylko przy wygranej, odpowiedź brzmiałaby: nie warto.** 2,4% to nie jest plan na przyszłość. To jest los na loterię.

### 5.2 Dlaczego mimo to uważam, że warto

**Bo najcenniejszy produkt tego projektu nie jest wynikiem konkursu i powstaje z prawdopodobieństwem znacznie wyższym niż 14%.**

Po dwudziestu jeden miesiącach, **nawet przy porażce w każdym konkursie**, istnieje:
- **zbudowany przyrząd pomiarowy** własnego projektu, ze zmierzoną charakterystyką
- **reanaliza cudzej pracy z jej surowych danych**, odtwarzająca opublikowane liczby co do trzeciego miejsca po przecinku i pokazująca, że powszechna interpretacja tego wyniku jest błędna
- **kampania pomiarowa z zarejestrowanymi z góry twierdzeniami**, raportowana w całości razem z wynikami negatywnymi

`[wniosek]` To jest opis **samodzielnie prowadzonych badań**, a nie opis udziału w konkursie. Dla rekrutacji zagranicznej — i dla Ciebie za dwa lata — to jest inna kategoria niż dyplom.

**I jedna rzecz konkretna, dostępna od zaraz:** reanaliza z `14_REANALIZA.md` **już istnieje**, opiera się na danych na licencji CC-BY, ma odtwarzalny kod i mówi coś nieoczywistego o opublikowanej pracy. `[domysł]` To jest materiał na **krótki preprint** — arXiv albo bioRxiv — możliwy do złożenia w ciągu kilku miesięcy, **całkowicie niezależnie od sprzętu, konkursu i tego, czy SSVEP u Ciebie działa**. Licealista z preprintem to nie jest to samo co licealista z projektem.

### 5.3 Kiedy powiedziałbym „nie warto"

Trzy warunki, i żaden nie zachodzi:

1. **gdyby 4 500–7 300 zł było realnym obciążeniem dla domu** — to jest pytanie do Ciebie, nie do mnie, i nie znam odpowiedzi
2. **gdyby te 10 h tygodniowo wypierały coś o pewniejszym zwrocie** — najbliższy kandydat to olimpiady dające indeks w Polsce. **Ale OITwEiM startuje z tego samego projektu** (`13_PODNIESIENIE_SZANS.md` §7), więc to nie jest wybór, tylko dokładka
3. **gdyby projekt kolidował z maturą** — nie koliduje. ISEF maj 2028, matura maj 2029

### 5.4 Rzecz, którą zmieniłbym w Twoim sposobie myślenia o tym

Piszesz o „sukcesie wartym tyle, żeby móc realnie myśleć o studiach za granicą". **Ten projekt ma 14% szans dać taki sukces w postaci dyplomu i jakieś 50–60% szans dać go w postaci dorobku.** Druga liczba jest cztery razy większa i mniej zależy od jury.

`[wniosek]` **Optymalizuj pod dorobek, a wynik konkursowy traktuj jako premię.** Praktycznie to znaczy: preprint z reanalizy, dziennik budowy z wersjonowanymi zdjęciami, dane i kod publicznie — **i to są rzeczy w 100% pod Twoją kontrolą**, w przeciwieństwie do werdyktu dwudziestoosobowego jury w Gdyni.

To jest zresztą ten sam wniosek, który wyszedł z oceny w trzech wymiarach (`19_SZANSE_PO_ZMIANIE.md` §5): **nowa oś projektu wygrywa nie prawdopodobieństwem, tylko sterowalnością.** Ta sama zasada zastosowana do całej strategii daje ten sam wynik.

### 5.5 Jedno zdanie na koniec

**Warto — pod warunkiem, że budujesz to dla dorobku, a startujesz w konkursach po drodze. Odwrotna kolejność ma 2,4% szans i nie ma planu awaryjnego.**
