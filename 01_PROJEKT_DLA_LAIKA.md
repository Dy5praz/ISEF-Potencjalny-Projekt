# 01 — Czym jest ten projekt, po ludzku

**Stan na 21 sierpnia 2026.**
**Po co ten plik:** żeby dało się opowiedzieć ten projekt komuś, kto nie wie nic — rodzicowi, nauczycielowi, jurorowi w pierwszej minucie rozmowy. Bez żargonu, ale bez ściemy.

---

## 1. Jedno zdanie

> **Mały przyrząd noszony z tyłu głowy odczytuje z mózgu, na co patrzysz, i zamienia to na komendę. Częścią naukową jest pomiar tego, jak bardzo urządzenie musi być duże, żeby jeszcze działało.**

Jeżeli ktoś ma czas na dwa zdania, dochodzi drugie:

> **Nie czyta myśli. Czyta reakcję mózgu na migający obraz — a to jest coś zupełnie innego i trzeba to mówić od razu.**

---

## 2. Jak to działa — od zera

### 2.1 Skąd w głowie bierze się prąd

Komórki nerwowe porozumiewają się impulsami elektrycznymi. Pojedyncza komórka daje sygnał, którego na skórze głowy w ogóle nie da się zmierzyć. Ale kiedy **dziesiątki tysięcy komórek robi to samo w tej samej chwili**, ich sygnały się dodają i na skórze pojawia się napięcie rzędu **kilkudziesięciu mikrowoltów**.

Dla skali: **około miliona razy mniej niż napięcie z paluszka AA.**

Mierzenie tego nazywa się **EEG**. Istnieje od 1924 roku, więc sam pomysł nie jest nowy.

### 2.2 Dlaczego to trudne — trzy ściany

**Czaszka rozmywa obraz.** Kość źle przewodzi prąd, więc sygnał z mózgu rozlewa się na boki, zanim dotrze do elektrody. Jak słuchanie tłumu przez ścianę: słychać, kiedy tłum krzyczy zgodnie, ale nie da się wyłowić jednej rozmowy. **Lepszy mikrofon tego nie naprawi — problem jest w ścianie.**

**Mięśnie krzyczą głośniej niż mózg.** Napięcie z pracującego mięśnia jest **od dziesięciu do tysiąca razy większe** niż sygnał z mózgu. Zaciśnij zęby — dla wzmacniacza EEG to jest jak wystrzał obok mikrofonu.

**Wszystko trzeba zmierzyć na żywym człowieku, który się rusza.**

### 2.3 Sztuczka z migającym obrazem

Skoro sygnał jest słaby i utopiony w zakłóceniach, nie da się „odczytać, o czym ktoś myśli". Trzeba się z mózgiem **umówić**. Ta umowa nazywa się **SSVEP** i działa tak:

1. Przed Tobą jest kilka przycisków. Każdy **miga z inną częstotliwością** — powiedzmy 8, 10, 12 i 15 razy na sekundę.
2. Patrzysz na ten, który chcesz wybrać.
3. Kora wzrokowa z tyłu głowy zaczyna „tykać" **w rytm tego konkretnego migania**. Dzieje się to samo, bez wysiłku, i nie da się tego nie robić.
4. Elektroda z tyłu głowy widzi to tykanie. Program sprawdza, który z czterech rytmów jest najsilniejszy.
5. To jest Twoja komenda.

**Dlaczego to działa przy słabym sygnale:** bo szukamy rytmu o **znanej z góry częstotliwości**. To jak wyławianie jednego, konkretnego tonu z hałasu — dużo łatwiejsze niż rozpoznanie dowolnego dźwięku.

**Uczciwe zastrzeżenie, które mówi się samemu, zanim ktoś zapyta:** urządzenie w praktyce wykrywa, **na co patrzysz** — tyle że odczytuje to z mózgu, a nie z oka. Dlaczego to nie jest to samo co kamerka — sekcja 6.

---

## 3. Na czym polega właściwe pytanie tego projektu

To jest najważniejsza sekcja w całym pliku i warto ją umieć opowiedzieć bez kartki.

### 3.1 Elektroda nigdy nie mierzy sama

**Napięcia nie da się zmierzyć w jednym punkcie.** Zawsze mierzy się **różnicę między dwoma punktami** — tak samo jak wysokość podaje się „nad poziomem morza", a nie samą w sobie. W EEG jeden z tych punktów nazywa się **elektrodą odniesienia**.

Przez sto lat stawiano ją tam, gdzie było wygodnie: **na płatku ucha, za uchem, na czole**. Wszystkie te miejsca łączy jedno — **są daleko od tego, co się mierzy**, i wymagają, żeby coś przez pół głowy do nich biegło. Czepek, opaska, kabel.

### 3.2 A jeżeli urządzenie ma być małe, to nie ma dokąd

**Tu zaczyna się projekt.** Jeżeli całe urządzenie ma zmieścić się w pudełku wielkości pudełka zapałek z tyłu głowy, to **elektroda odniesienia musi usiąść tuż obok tej, która mierzy** — kilka centymetrów zamiast dziesięciu.

I teraz robi się ciekawie, bo **obie elektrody widzą wtedy prawie to samo**. Odejmowanie dwóch prawie identycznych rzeczy zostawia prawie nic. **Zwarcie urządzenia może skasować sygnał razem z zakłóceniem.**

### 3.3 Pytanie, którego nikt nie zmierzył

> **Jak blisko może usiąść elektroda odniesienia, zanim sygnał się załamie? I czy ważne jest tylko to, jak blisko — czy także z której strony?**

`[fakt]` Sprawdzone w dziewięciu bazach naukowych, w trzech niezależnych grafach cytowań, w sekcjach metod 178 prac i w trzynastu rocznikach abstraktów ISEF: **nikt tego nie zmierzył jako zależności.** Porównywano po dwa albo trzy gotowe warianty — nigdy całej krzywej, nigdy pod ograniczeniem rozmiaru urządzenia.

**Dlaczego pole jest puste, skoro pytanie jest oczywiste** — i to jest dobre pytanie, które sam autor projektu zadał: bo przez sto lat **wszyscy mieli dość elektrod, żeby problem zniknął**. Przy trzydziestu elektrodach na czepku można przeliczyć sygnał tak, jakby odniesienie leżało gdziekolwiek. Przy dwóch elektrodach na małym module **nie ma czego przeliczać** — liczy się to, gdzie fizycznie postawisz elektrodę. **Pytanie robi się ważne dopiero wtedy, gdy urządzenie robi się małe.**

---

## 4. Co konkretnie zostanie zbudowane

### 4.1 Wygląd — i dlaczego są dwa

**Urządzenie gotowe:** jeden moduł z tyłu głowy, **wielkości pudełka zapałek** (~32 × 48 × 12 mm), postawiony pionowo. Dwie elektrody krytyczne są **na jego własnym spodzie**. Dwie dodatkowe idą w bok cienkimi przewodami przy skórze, po ~3,5 cm. **Cztery elektrody. Bez łuku przez głowę, bez opaski, bez kasku, bez czepka.**

**Urządzenie w czasie pomiaru:** ten sam moduł, ale **osiem elektrod, nie cztery** — plus kolejne wyprowadzenia na cienkich przewodach: za ucho, na płatek ucha, na kark i na guzowatość potyliczną tuż pod modułem. **Wygląda wtedy jak aparatura, i ma tak wyglądać.**

**Skąd ta różnica — i to jest sedno całego projektu.** Pytanie brzmi: *gdzie postawić elektrodę odniesienia*. Żeby porównać cztery jej położenia uczciwie, trzeba je zmierzyć **jednocześnie, u tej samej osoby, na tych samych próbkach**. Gdyby elektrodę **przekładać** — najpierw za ucho, potem na kark, potem obok modułu — to każdy pomiar byłby z innej chwili, a różnica wyniku niosłaby oprócz położenia elektrody także zmęczenie, wyschnięty żel i inny nastrój. **Efektu rzędu kilku punktów procentowych nikt by w tym nie zobaczył.**

Czyli: **osiem elektrod to przyrząd pomiarowy. Cztery to wyrób.** A **to, które cztery zostają, jest wynikiem tego projektu** — nie da się ich wybrać przed pomiarem, bo właśnie po to się mierzy.

### 4.2 Co jest w środku

| Warstwa | Co robi |
|---|---|
| **elektrody** | dotykają skóry przez włosy |
| **wzmacniacz** (układ ADS1299) | bierze mikrowolty i zamienia je na liczby, 24 bity dokładności |
| **mikrokontroler** (ESP32-S3) | liczy, który rytm jest najsilniejszy, i wysyła wynik bezprzewodowo |
| **bateria** | bo **żadnego kabla do gniazdka przy głowie** — to jest warunek bezpieczeństwa, nie wygody |

### 4.3 Demonstracja

Migające znaczniki są **na przedmiotach w otoczeniu**, nie na tablicy przed twarzą. Patrzysz na żarówkę — zapala się. Patrzysz na gniazdko — włącza się wentylator.

**Przedmioty są kupione, nie budowane** — poniżej 200 zł, zero godzin warsztatu. To jest reguła, nie oszczędność: **każda godzina włożona w rekwizyt jest godziną zabraną urządzeniu, a oceniane jest urządzenie.**

---

## 5. Co to realnie będzie umiało

**Umie:** wybrać jedną z kilku–kilkunastu rzeczy, na które patrzysz, w ciągu **1–3 sekund**, z dokładnością rzędu **80–95%**, bez dotykania czegokolwiek i bez mówienia.

**Nie umie i nie będzie umiało:** czytać myśli, rozpoznawać słów, działać, kiedy nie patrzysz na znacznik, ani działać u każdego — `[fakt]` u **10–30% ludzi** ta reakcja jest za słaba, żeby dało się z niej korzystać.

**Zdanie do przygotowania na pytanie „czyli to czyta w myślach?":**

> *Nie. Migający punkt wymusza w korze wzrokowej rytm o tej samej częstotliwości. Ja wykrywam ten rytm i wiem, na który punkt patrzysz. Poza tymi punktami urządzenie nie wie o Tobie nic.*

---

## 6. Pytanie, które padnie na pewno: „a czemu nie kamerka śledząca wzrok?"

**Zacznijmy od przyznania: kamerka wygrywa i zawsze będzie wygrywać.** To zmierzono — te same jedenaście osób, to samo zadanie z pięcioma przyciskami: **kamerka 28,2 bita na minutę, najlepszy interfejs mózgowy 20,9, słuchowy 3,3, dotykowy 3,4.** Kto udaje, że jest inaczej, ten kłamie albo nie sprawdził.

**Dlatego odpowiedź nie brzmi „moje jest lepsze". Brzmi tak, i ma dwie części.**

**Część pierwsza — kamerka potrzebuje oka.** Nie zadziała, jeżeli ktoś nie kontroluje powiek, ma opadającą powiekę, jest w ciemności albo ma na twarzy sprzęt medyczny. **U części osób, dla których to urządzenie jest przeznaczone, kamerka nie działa właśnie dlatego, że patrzy na oko.** Dla większości ludzi kamerka jest tańsza i lepsza — **to urządzenie nie jest dla większości ludzi.**

**Część druga, ważniejsza — ja nie mierzę sterowania, tylko elektrodę.** Wynik brzmi „elektroda odniesienia bliżej niż X centymetrów kosztuje Y punktów procentowych". **To jest fakt o sprzęcie, nie o migającym punkcie.** Przenosi się na każde noszone urządzenie EEG z tyłu głowy — także takie, które ze wzrokiem nie ma nic wspólnego. Kamerka tego nie zastąpi, bo kamerka nie jest urządzeniem EEG.

---

## 6a. Drugie pytanie, które padnie: „a czy da się to obsługiwać bez patrzenia?"

**Da się, i wiadomo dokładnie, ile to kosztuje. Cena jest wysoka.**

Sztuczka nazywa się **uwagą utajoną** — oczy stoją nieruchomo, a człowiek przenosi uwagę na coś obok, nie patrząc na to wprost. Każdy to potrafi: tak się podgląda kogoś kątem oka. Kora wzrokowa reaguje na to słabiej, ale jednak reaguje, i na tej różnicy da się zbudować sterowanie.

Ceny są trzy i wszystkie zmierzono:

1. `[fakt]` **dokładność spada o mniej więcej 20 punktów procentowych** przy samej tej zamianie, bez zmiany czegokolwiek innego (Kelly 2004)
2. `[fakt]` **liczba rzeczy do wyboru spada z kilkudziesięciu do dwóch.** Najlepszy opublikowany układ tego typu przenosi **0,17 bita na wybór**; układ sterowany wzrokiem przy czterdziestu celach — **4,69 bita**. **Dwadzieścia siedem razy mniej informacji** (Lesenfants 2014)
3. `[fakt]` **sygnał przenosi się w inne miejsce głowy** — przy patrzeniu wprost jest najsilniejszy na środku potylicy, przy uwadze utajonej przenosi się wyżej i w bok (Walter 2012). Czyli **ucieka spod urządzenia, które ma leżeć na potylicy**

**Jest jednak sztuczka, która działa lepiej i nie wymaga zmiany urządzenia.** Zamiast rozstawiać migające punkty w różnych miejscach, nakłada się **dwie migające warstwy na siebie, w jednym punkcie** — dwie chmury kropek o różnych kolorach, obracające się w przeciwne strony. Patrzysz cały czas w to samo miejsce, a wybierasz tym, **którą warstwę śledzisz uwagą.** `[fakt]` Tsinghua zmierzyła to na osiemnastu osobach: **72,6% przy dwóch możliwościach.**

**I to jest odpowiedź na kamerkę, tym razem nie słowna tylko działająca:** kamerka nie ma wtedy czego mierzyć, **bo nie ma dokąd patrzeć.** Wszystko jest w jednym punkcie.

**Dlaczego mimo to główny tryb zostaje wzrokowy:** bo daje czterdzieści możliwości zamiast dwóch i 95% zamiast 72%, a **projekt mierzy elektrodę, nie człowieka** — do pomiaru potrzebny jest najsilniejszy dostępny sygnał.

**A czego zrobić się nie da:** uciec od wzroku **całkowicie**, zostając na potylicy. Kora potyliczna **jest** korą wzrokową. Chcąc uciec zupełnie, trzeba przenieść urządzenie nad korę ruchową i czytać **wyobrażony ruch ręki** — tam wzrok jest zbędny, ale `[fakt]` **osiemdziesiąt jeden procent ludzi nie osiąga tam użytecznej dokładności** (99 osób, badanie z Grazu), a wynik zmienia się z dnia na dzień tak mocno, że **przykryłby efekt, który ten projekt mierzy**.

**I to jest cała odpowiedź:** migający znacznik to nie jest wybór estetyczny ani lenistwo, tylko **przyrząd pomiarowy**. Projekt mierzy, gdzie postawić elektrodę odniesienia — a do tego potrzebny jest sygnał o znanej częstotliwości, żeby dało się powiedzieć „wynik spadł przez elektrodę", a nie „wynik spadł, bo dziś gorszy dzień". **Wynik o elektrodzie przenosi się potem na każde urządzenie potyliczne, niezależnie od tego, czym się je steruje.**

---

## 7. Do czego to komu

Uczciwe zastosowanie: **komunikacja i sterowanie dla osób, które nie mogą mówić ani się poruszać.** To nie jest naciągnięcie — to jest funkcja tej technologii i jej główne zastosowanie od trzydziestu lat.

Ale **projekt nie udaje wyrobu medycznego.** Jest urządzeniem sterującym i pomiarowym, a jego wynik jest wynikiem inżynierskim: **jak mały może być, zanim przestanie działać.**

---

## 8. Skąd wiadomo, że to nie upadnie na tym, że ktoś już to zrobił

Krótka odpowiedź: **bo już czterokrotnie upadło i za każdym razem zostało przebudowane.**

Projekt miał cztery wcześniejsze twierdzenia. **Wszystkie zabiła literatura** — jedno praca z Imperial College, jedno praca w *PNAS* z patentem, jedno zespół z Politechniki Warszawskiej, a jedno **własna analiza cudzych danych**, która pokazała, że efekt wart dziewięciu punktów procentowych jest w rzeczywistości wart dwóch dziesiątych. Cała ta historia jest opisana w `11_EWOLUCJA.md` i **jest materiałem na rozmowę, nie wstydem** — arkusz oceny ISEF punktuje pokazanie odrzuconych wariantów.

Twierdzenie bieżące różni się od tamtych czterech jedną rzeczą: **nie mówi „jestem pierwszy" ani „jestem tańszy". Mówi „zmierzyłem, ile to kosztuje".** Takiego twierdzenia cudza publikacja nie unieważnia — najwyżej potwierdza.

---

## 9. Trzy zdania, gdyby zostało trzydzieści sekund

> **Buduję interfejs, który odczytuje z tyłu głowy, na co patrzysz, i zamienia to na komendę — dla ludzi, którzy nie mogą mówić ani się ruszać.**
>
> **Żeby taki przyrząd dało się nosić, musi być mały, a wtedy obie elektrody siedzą obok siebie i mogą skasować sygnał, który mają mierzyć.**
>
> **Mierzę, jak blisko mogą usiąść, zanim to się stanie — czego nikt dotąd nie zmierzył, bo pytanie robi się ważne dopiero wtedy, gdy urządzenie robi się małe.**
