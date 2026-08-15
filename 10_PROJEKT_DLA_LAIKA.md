# 10 — Czym właściwie jest ten projekt, po ludzku

**Data:** 15 sierpnia 2026, po zamknięciu etapu 1 i po Twoich czterech decyzjach
**Po co ten plik:** żeby dało się opowiedzieć ten projekt komuś, kto nie wie nic — rodzicowi, nauczycielowi, jurorowi w pierwszej minucie rozmowy. Bez żargonu, ale bez ściemy.

---

## 1. Jedno zdanie

> **Mały przyrząd noszony z tyłu głowy, który odczytuje z mózgu, na co patrzysz, i zamienia to na komendę dla urządzenia — a jego częścią naukową jest układ elektroniczny, który usuwa zakłócenie od zaciskania szczęki, zanim zdąży ono zepsuć pomiar.**

Jeżeli ktoś ma czas na dwa zdania, dochodzi drugie:

> **Nie czyta myśli. Czyta reakcję mózgu na migający obraz — a to jest coś zupełnie innego i trzeba to mówić od razu.**

---

## 2. Jak to działa — od zera

### 2.1 Skąd w głowie bierze się prąd

Komórki nerwowe w mózgu porozumiewają się impulsami elektrycznymi. Pojedyncza komórka daje sygnał, którego na skórze głowy w ogóle nie da się zmierzyć — jest za mały. Ale kiedy **dziesiątki tysięcy komórek robi to samo w tej samej chwili**, ich sygnały się dodają i na skórze głowy pojawia się napięcie rzędu **kilkudziesięciu mikrowoltów**.

Dla skali: to jest **około miliona razy mniej niż napięcie z paluszka AA**.

Mierzenie tego nazywa się **EEG** (elektroencefalografia). Istnieje od 1924 roku, więc sam pomysł nie jest niczym nowym.

### 2.2 Dlaczego to takie trudne

Trzy rzeczy stoją na drodze i warto je znać, bo z nich wynika cały projekt:

**Czaszka rozmywa obraz.** Kość źle przewodzi prąd, więc sygnał z mózgu, zanim dotrze do elektrody, rozlewa się na boki. Efekt jest taki, jakby słuchać tłumu przez ścianę: słychać, kiedy tłum krzyczy zgodnie, ale nie da się wyłowić jednej rozmowy. **Lepszy mikrofon tego nie naprawi — problem jest w ścianie.** To ograniczenie fizyczne i nikt go nie obejdzie bez operacji.

**Mięśnie krzyczą głośniej niż mózg.** Napięcie z pracującego mięśnia jest **od dziesięciu do tysiąca razy większe** niż sygnał z mózgu. Zaciśnij zęby — dla wzmacniacza EEG to jest jak wystrzał obok mikrofonu.

**Wszystko trzeba zmierzyć na żywym człowieku, który się rusza.**

### 2.3 Na czym polega sztuczka z migającym obrazem

Skoro sygnał jest słaby i utopiony w zakłóceniach, nie da się po prostu „odczytać, o czym ktoś myśli". Trzeba się z mózgiem **umówić** — i to jest właśnie to, co w tej dziedzinie nazywa się **paradygmatem**.

Nasza umowa nazywa się **SSVEP** i działa tak:

1. Na ekranie są cztery przyciski. Każdy **miga z inną częstotliwością** — powiedzmy 8, 10, 12 i 15 razy na sekundę.
2. Patrzysz na ten, który chcesz wybrać.
3. Kora wzrokowa z tyłu głowy zaczyna „tykać" **w rytm tego konkretnego migania**. To dzieje się samo, bez wysiłku, i nie da się tego nie robić.
4. Elektroda z tyłu głowy widzi to tykanie. Program szuka w sygnale rytmu 8, 10, 12 albo 15 Hz i sprawdza, który jest najsilniejszy.
5. To jest Twoja komenda.

**Dlaczego akurat to działa przy słabym sygnale:** bo szukamy rytmu o **znanej z góry częstotliwości**. To jak wyławianie jednego, konkretnego tonu z hałasu — dużo łatwiejsze niż rozpoznanie dowolnego dźwięku. Zakłócenia są rozłożone po wszystkich częstotliwościach, a nasz sygnał siedzi w jednym, wąskim miejscu.

**Uczciwe zastrzeżenie, które trzeba mówić samemu, zanim ktoś zapyta:** to znaczy, że urządzenie w praktyce wykrywa, **na co patrzysz** — tyle że odczytuje to z mózgu, a nie z oka. O tym, dlaczego to nie jest to samo co kamerka śledząca wzrok, jest sekcja 5.

---

## 3. Co konkretnie zostanie zbudowane — po decyzjach z 15 VIII

### 3.1 Wygląd

**Jeden mały moduł z tyłu głowy**, w okolicy potylicy — tam, gdzie kora wzrokowa. Wielkości mniej więcej aparatu słuchowego. Bez kabla do drugiego modułu, bez łuku przez głowę, bez opaski, bez kasku.

To jest wynik weryfikacji z 15 VIII, i wyszedł korzystnie: sprawdzałem, czy rozłożenie elektrod na dwa miejsca (potylica plus za uchem) daje lepszy sygnał. **Nie daje — daje gorszy.** Trzy niezależne prace pokazują, że dla SSVEP najlepsza jest **referencja lokalna**: jedna elektroda w środku i kilka wokół niej, w odległości 2–3 cm. Czyli jeden zwarty przedmiot, a nie konstrukcja przez pół głowy.

Rzadko się zdarza, żeby wygoda i fizyka wskazywały to samo. Tutaj wskazują.

### 3.2 Co jest w środku, warstwami

| Warstwa | Co to jest | Po co |
|---|---|---|
| **elektrody** | metalowe pazurki przechodzące między włosami do skóry | dotknąć skóry przez włosy bez żelu. Wzór jest opisany w literaturze: średnica 14 mm, osiem „palców" po 6 mm |
| **wzmacniacz** | własna płytka drukowana | sygnał z elektrod ma mikrowolty. Trzeba go wzmocnić, nie dokładając własnego szumu |
| **układ kompensacji** | **to jest część naukowa projektu** | usuwa zakłócenie od szczęki **zanim** trafi do wzmacniacza — patrz 3.3 |
| **przetwornik i radio** | scalak zamieniający napięcie na liczby, plus Bluetooth | wysłać do komputera |
| **program** | rozpoznaje, który rytm jest najsilniejszy | zamienić sygnał na komendę |
| **obudowa** | druk żywiczny, materiał z certyfikatem kontaktu ze skórą | ma się trzymać na głowie i nie uczulać |

### 3.3 Na czym polega właściwy wynalazek — i dlaczego to nie jest „jeszcze jedno EEG"

Domowej roboty EEG zbudowało już wielu ludzi. Samo to nie jest osiągnięciem — na ISEF 2026 taki projekt (ENBM079, koszt poniżej 11 dolarów na kanał) dostał **trzecią nagrodę**, więc poprzeczka jest znana.

Nasze twierdzenie jest węższe i mierzalne:

> **Przy uchu i z tyłu głowy największym zakłóceniem jest zaciskanie szczęki. Jeżeli zmierzy się je osobną elektrodą i odejmie od sygnału w układzie elektronicznym — zanim sygnał zostanie wzmocniony — to pomiar wychodzi lepiej. O ile lepiej: oto liczba.**

**Dlaczego odejmowanie „przed", a nie „po", jest istotne, a nie kosmetyczne.** Wzmacniacz ma zakres — jak głośnik, który przy zbyt mocnym sygnale zaczyna charczeć. Kiedy zaciskasz zęby, zakłócenie jest tak duże, że **wypycha wzmacniacz poza zakres**, a wtedy sygnał z mózgu w tym momencie **przestaje istnieć**. Nie jest zabrudzony — jest skasowany. Żaden program nie odzyska czegoś, czego nie ma. Jeżeli natomiast odejmiemy zakłócenie **wcześniej**, wzmacniacz nigdy nie wychodzi poza zakres i sygnał przeżywa.

To jest różnica między „wyczyścić nagranie" a „nagrać czysto".

**Przesłanka, na której to stoi, i jest ona zmierzona przez kogoś innego:** praca Kappela i współpracowników z 2017 roku (9 badanych) mierzyła, jak bardzo różne zakłócenia psują sygnał w uchu i na czubku głowy. Wynik: **zakłócenie od szczęki jest w uchu gorsze niż na skalpie**. Czyli problem, który chcemy rozwiązać, jest w naszej formie urządzenia **udokumentowany jako poważniejszy niż w formie standardowej**. To jest najlepsze zdanie startowe, jakie ten projekt ma.

**Rzecz, którą trzeba zapisać, bo poprawiła projekt:** przez cały etap 1 pisałem „zakłócenia mięśniowo-oczne", zakładając, że trzeba kompensować i szczękę, i mruganie. Odczytanie tej pracy w oryginale pokazało, że **mruganie w tym miejscu głowy w ogóle nie przeszkadza** — gałka oczna jest za daleko. Do skompensowania jest jedna rzecz, nie dwie. Układ się przez to upraszcza.

---

## 4. Co to realnie będzie umiało

### 4.1 Umie

**Wybrać jedną komendę z kilku, patrząc na nią, mniej więcej co 1–4 sekundy.**

Ile komend — to jest do zmierzenia, nie do obiecania. Widełki z literatury dla porządnie zrobionych układów SSVEP: **od 4 do 12 komend przy dokładności powyżej 90%**, a w wersjach z profesjonalnym sprzętem znacznie więcej. Praca, która pokazuje 12 komend, 93% trafności i okno 1-sekundowe **na elektrodach suchych**, istnieje (Xing i in., *Scientific Reports* 2018).

Co da się z tym zrobić w praktyce:

- **sterować pojazdem albo robotem** — cztery komendy to lewo, prawo, jazda, stop
- **sterować kursorem komputera** — nie ciągle, ale przez zadawanie kierunku: „jedź w prawo" i kursor jedzie sam, aż go zatrzymasz. To się nazywa sterowanie prędkością i jest normalną, działającą techniką
- **obsługiwać menu** — włącz, wyłącz, głośniej, ciszej. Istnieje praca pokazująca **38 komend do sterowania domem, 96,9% trafności, na jednym kanale**
- **działać u osoby, która nie może się ruszać ani mówić**, ale panuje nad wzrokiem

**Uczciwie o tempie — poprawione 15 VIII wieczorem, `KOREKTY.md` K-039.** Miałem tu wcześniej zdanie „cztery komendy na minutę to tempo pilota do telewizora". **To była pomyłka o rząd wielkości** — pomyliłem liczbę komend w alfabecie z tempem ich wydawania.

Liczby prawdziwe, z pracy odczytanej w oryginale (Xing i in., *Scientific Reports* 2018, jedenastu badanych, **elektrody suche**): **12 celów, okno 1-sekundowe, 93,2% trafności, przepustowość 92,35 bit/min**. To odpowiada **rzędowi 30–40 wyborów na minutę**.

To już nie jest tempo pilota do telewizora. To jest tempo, przy którym da się realnie sterować i przy którym twierdzenie przepustowościowe ma sens.

### 4.2 Nie umie i nie będzie umiało

Ta lista jest ważniejsza od poprzedniej, bo obietnica, której nie da się dotrzymać, kosztuje więcej niż skromna obietnica dotrzymana.

| Czego nie robi | Dlaczego |
|---|---|
| **nie czyta myśli** | mierzy zsynchronizowaną reakcję dużych grup komórek na znany bodziec. Myśl nie ma znanej częstotliwości |
| **nie zamienia myślanych słów na tekst** | nieinwazyjnie to jest na granicy możliwości i robią to zespoły akademickie z elektrodami wszczepionymi do mózgu |
| **nie działa przy zamkniętych oczach** | SSVEP wymaga patrzenia na coś migającego. To jest realny koszt tego paradygmatu i trzeba go mówić, nie chować |
| **nie daje płynnego sterowania w dwóch osiach naraz** (jak myszką) | to wymaga gęstej siatki elektrod nad korą ruchową, czyli czapki. Wyklucza to wymaganie „bez kasków" |
| **nie dorówna rozdzielczością rozwiązaniom wszczepianym** | czaszka rozmywa sygnał do 5–9 cm. **Ściana fizyczna** |
| **nie zadziała u wszystkich** | u 15–30% ludzi część paradygmatów EEG nie działa niezależnie od jakości sprzętu. Przy grupie kilku osób **jedna niedziałająca jest zdarzeniem oczekiwanym** i musi być wpisana w plan z góry, inaczej wygląda jak ukrywanie porażki |
| **nie diagnozuje niczego** | to nie jest urządzenie medyczne i regulamin ISEF zabrania uczniom diagnozowania |

### 4.3 Zdanie, które trzeba mieć przygotowane

Ktoś zapyta: *„czyli to czyta w myślach?"*

> **Nie. Umawiam się z mózgiem, że cztery przyciski będą migać z różną prędkością, a kora wzrokowa sama zacznie tykać w rytm tego, na który patrzę. Ja odczytuję to tykanie. Mózg nie mówi mi, co myślisz — mówi mi, na czym skupiłeś wzrok.**

---

## 5. Pytanie, które padnie na pewno: „a czemu nie kamerka śledząca wzrok?"

To jest najostrzejsze pytanie do tego projektu i trzeba mieć na nie odpowiedź lepszą niż wykręt. Śledzenie wzroku kamerą jest tańsze, szybsze i dokładniejsze. Trzy uczciwe odpowiedzi:

1. **Kamerka wymaga kamerki skierowanej na twarz.** Urządzenie noszone na sobie działa wszędzie, także w ciemności i bez ustawiania sprzętu naprzeciwko.
2. **SSVEP działa również wtedy, gdy oko jest nieruchome, a uwaga przesunięta.** Skupienie uwagi na obiekcie w polu widzenia bez patrzenia wprost na niego też generuje odpowiedź, tylko słabszą. Kamerka tego nie widzi w ogóle. `[wniosek, do zmierzenia w naszym układzie — to jest dobry kandydat na własny eksperyment]`
3. **Ten sam sprzęt otwiera się na paradygmaty, których wzrok nie obsługuje** — na przykład wykrywanie stanu skupienia albo senności, gdzie nie ma na co patrzeć.

**Czego odpowiadać nie wolno:** że jest lepsze. W czystym zadaniu „wybierz przycisk patrząc na niego" kamerka wygrywa i udawanie, że jest inaczej, kosztuje wiarygodność.

---

## 6. Dwa warianty, między którymi jeszcze się wahasz

Zdolność urządzenia jest w obu taka sama. Różni się **to, co twierdzimy i co mierzymy** — a to decyduje o tym, jak wygląda plan eksperymentalny.

| | **Wariant 2: metryka użytkowa** | **Wariant 3: przepustowość** |
|---|---|---|
| **twierdzenie po ludzku** | „to się zakłada w kilka sekund, działa cały dzień i nie trzeba go co chwilę kalibrować — w odróżnieniu od czapki, którą zdejmuje się po dwudziestu minutach" | „ta konstrukcja przepuszcza tyle a tyle komend na minutę, przy tej dokładności, w tej formie" |
| **co trzeba zmierzyć** | czas montażu, dryf jakości sygnału w ciągu dnia, ile sesji działa bez ponownej kalibracji, odporność na ruch i mówienie | dokładność i liczbę komend na minutę, w kilku konfiguracjach, z niepewnościami |
| **konkurencja w literaturze** | **prawie nikt tego nie mierzy**, mimo że wszyscy podają to jako powód robienia takich urządzeń | zmierzone wielokrotnie, jest z czym porównywać, ale i jest z kim przegrać |
| **ryzyko** | juror może uznać, że metryka jest dobrana pod wynik | grupa z Tsinghua opublikowała w 2023 w Nature Communications wynik z ucha, którego się nie pobije |
| **haczyk formalny** | **jest:** mierzenie, jak wynik zależy od Twojego zmęczenia albo wyspania, jest wg regulaminu ISEF „zmienną ludzką" i wymaga zgody komisji. Dryf sygnału w czasie noszenia — wolno | brak |
| **ile pracy** | więcej sesji, dłużej, nudniej | mniej sesji, ale każda staranniejsza |

**Rzecz, która może rozwiązać ten dylemat i której nie widziałem, dopóki nie zebrałem tego w tabelę:** te dwa warianty **nie wykluczają się w laboratorium, tylko w abstrakcie**. Abstrakt na ISEF ma **250 słów** i musi mieć jedno twierdzenie. Ale kampania pomiarowa może zebrać dane pod oba, bo mierzy ten sam układ, tylko dłużej.

**Czyli: decyzję można odłożyć do momentu, w którym będą pierwsze wyniki** — i wtedy wybrać ten wariant, w którym liczba wyszła mocniej. To nie jest unik. To jest ta sama logika, którą przyjąłeś przy umiejscowieniu: nie wybierać założeniem tego, co można wybrać pomiarem.

**Warunek, żeby to było uczciwe:** oba warianty muszą być zaplanowane **z góry**, przed pierwszym pomiarem, i oba muszą być raportowane. Wybieranie po fakcie tej metryki, która wyszła najlepiej, i przemilczenie reszty ma w nauce nazwę i jest nadużyciem. Zapisujemy obie z góry, pokazujemy obie, jedną nazywamy główną.

---

## 7. Skąd wiadomo, że to nie jest kolejny pomysł, który upadnie na tym, że ktoś już to zrobił

Trzy poprzednie kierunki tego projektu zginęły na tym, że rzecz była już opublikowana. Tym razem sprawdzenie zostało zrobione **przed** budowaniem strategii, nie po.

**Co jest zajęte, wprost:**
- sam pomysł odejmowania zakłócenia z osobnej elektrody — **od 1983 roku**
- analogowe usuwanie zakłóceń od **ruchu** w urządzeniu noszonym — od 2019
- analogowa kompensacja **offsetu** w urządzeniu zausznym — 2026
- sterowanie **samą** szczęką i mruganiem przy uchu — 2014 i 2025
- tanie domowe EEG z interfejsem — wielokrotnie, ostatnio trzecia nagroda na ISEF 2026
- elektroda douszna z kontaktem dopasowanym do kanału — 2023, Nature Communications
- badanie elektrod suchych — publiczny zbiór na **102 osobach**

**Czego nie znalazłem:** analogowej kompensacji **konkretnie zakłócenia szczękowego, z osobnej elektrody, przed wzmocnieniem, w urządzeniu noszonym**.

**I to jest właśnie powód, dla którego twierdzenie projektu brzmi „o ile lepiej", a nie „pierwszy raz".** Bo „nie znalazłem" nie znaczy „nie ma", a twierdzenie o pierwszeństwie upada w chwili, gdy ktoś znajdzie jedną pracę. Twierdzenie pomiarowe — „mój układ z kompensacją wobec mojego układu bez kompensacji, oto liczba i niepewność" — **jest prawdziwe niezależnie od tego, co jeszcze istnieje na świecie**. Nikt go nie unieważni w połowie 2027 roku.

To jest jedyna forma twierdzenia, która przy historii tego projektu ma sens.
