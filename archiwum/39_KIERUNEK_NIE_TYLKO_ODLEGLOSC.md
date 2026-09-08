# 39 — Urządzenie nie musi być pudełkiem. Kierunek odniesienia, nie tylko odległość

**Data:** 21 sierpnia 2026
**Obawa użytkownika:** *„im urządzenie będzie lepsze, tym lepiej się je ogląda. (…) badanie z wynikiem mówiącym, że urządzenie na potylicy musi mieć gabaryty pudełka, aby solidnie działać nie brzmi tak dobrze."*

**Obawa jest uzasadniona i miała podstawy w tym, co dotąd zapisano.** Ale po przeliczeniu opublikowanych wyników na wspólną metrykę wychodzi, że **przesłanka „zwarty znaczy słaby" jest fałszywa** — i że **plan pomiarowy ma konkretną dziurę, która tę fałszywą przesłankę podtrzymywała.**

---

## 0. Odpowiedź w trzech zdaniach

**Pojedynczy kanał dwubiegunowy POz−Oz — dwie elektrody odległe o ~3,5 cm, obie na potylicy, bez żadnego odniesienia odległego — daje przy czterdziestu celach około 46 bit/min.** To jest **2,6 raza więcej** niż najlepszy opublikowany układ zauszny i mniej więcej tyle, co **pełny czepek żelowy przy ośmiu celach**.

**Co się załamuje, to nie zwartość — to kierunek.** Para pozioma na wyrostkach sutkowatych daje 2,5 bit/min. Para pionowa nad korą wzrokową daje 46. **Ta sama zwartość, dwudziestokrotna różnica.**

**A plan pomiarowy testuje wyłącznie kierunek gorszy** — wszystkie cztery kandydatury na odniesienie idą w dół albo w bok. Poprawka kosztuje zero.

---

## 1. Wszystko, co opublikowano, przeliczone na jedną metrykę

Dotąd liczby leżały w trzech różnych postaciach: dokładność przy różnej liczbie celów, ITR przy różnych oknach, procenty bez podanego N. **Nie dawały się porównać** — i przez to obraz wyglądał gorzej, niż jest.

Przeliczenie na **bit/min wg wzoru Wolpawa**, z jawnym N, P i t. `[wniosek]` Liczby oznaczone gwiazdką **policzyłem sam z ich dokładności** — nie są to wartości podane przez autorów.

| Konfiguracja | N | P | t [s] | **bit/min** |
|---|---|---|---|---|
| Li 2025: 8 kanałów potylicznych, odniesienie na czole | 40 | 0,941 | 1,75 | **160,7\*** |
| Li 2025: 4 kanały | 40 | 0,914 | 1,95 | **136,8\*** |
| Li 2025: 3 kanały (Oz, O1, O2) | 40 | 0,816 | 1,95 | **112,5\*** |
| Cardoso 2022: czepek żelowy, elektrody czynne | 8 | 0,990 | 3,55 | **48,8\*** |
| **Li 2025: POz−Oz dwubiegunowy, JEDEN kanał** | **40** | **0,682** | **3,55** | **46,3\*** |
| Cardoso 2022: opaska z elektrodami suchymi | 8 | 0,911 | 3,55 | **39,2\*** |
| Kołodziej: 3 kanały, odniesienie na małżowinie, okno 1 s | 3 | 0,733 | 1,00 | **28,9** |
| Li 2025: Oz sam, odniesienie na czole | 40 | 0,377 | 3,55 | **18,1\*** |
| **Liang 2021: okolica zauszna, najlepszy paradygmat** | 12 | 0,842 | — | **17,8** (podane w pracy) |
| Kołodziej: montaż zwarty różnicowy, okno 1 s | 3 | 0,640 | 1,00 | **16,9** |
| **Cardoso 2022: para na wyrostkach sutkowatych** | 8 | 0,297 | 3,55 | **2,5\*** |

### 1.1 Co z tej tabeli wynika, a czego nie widać w samych procentach

`[wniosek]` **Trzy rzeczy, z których żadna nie była widoczna, dopóki liczby leżały w różnych jednostkach:**

1. **„96,4% przy dwóch celach" z PNAS nie ma w tej tabeli, bo przy dwóch celach maksimum teoretyczne to jeden bit na próbę.** Przy oknie 3,55 s daje to sufit **~17 bit/min** — czyli **mniej niż POz−Oz**, przy elektrodach robionych laserem femtosekundowym. To jest najlepsza ilustracja zasady „nigdy dokładność bez N" (`06_TABELA_PARAMETROW.md` §0).
2. **Zwarty montaż pionowy bije wszystkie układy „wygodne"** — zauszny, sutkowaty, opaskę suchą.
3. **Rozstrzał wewnątrz kategorii „montaż zwarty" wynosi od 2,5 do 46,3 bit/min**, czyli **osiemnastokrotność**. Kategoria „zwarty" nie ma jednej wartości — i to jest właśnie powód, dla którego pytanie projektu ma sens.

---

## 2. Dziura w planie, którą to ujawnia — i jest konkretna

`[fakt]` `15_PROJEKT.md` §2.3, tabela ośmiu wejść. Kandydaci na elektrodę odniesienia:

| Wejście | Położenie | Kierunek od Oz |
|---|---|---|
| 4 | ~2 cm **poniżej** Oz | **w dół** |
| 5 | ~4 cm **poniżej** Oz, nad mięśniem karku | **w dół** |
| 6 | wyrostek sutkowaty (za uchem) | **w bok i w dół** |
| 8 | płatek ucha | **w bok i w dół** |

`16_PLAN_EKSPERYMENTALNY.md` §3.2 zapisuje zmienną główną jako *„odległość elektrody odniesienia od Oz: ~2, ~4, ~7, ~10 cm (kolejno: wewnątrz modułu, poniżej inionu nad karkiem, wyrostek sutkowaty, płatek ucha)"*.

`[wniosek]` **Wszystkie cztery kandydatury idą w dół albo w bok. Ani jedna nie idzie w górę.** A w dół leżą dokładnie trzej mieszkańcy z ryzyka **R12**: mięsień karku, móżdżek reagujący na bodziec wzrokowy w paśmie beta, i przejście poniżej inionu.

**Skąd się ta dziura wzięła — i to jest pouczające.** `[fakt]` Zbiór Kołodzieja zawiera **wyłącznie O1, Oz i O2**, a te trzy punkty leżą w układzie 10–20 **na jednej linii poprzecznej**, ~10% powyżej inionu. **W tamtych danych nie istnieje ani jedna para pionowa.** Reanaliza z `14` §5 mogła więc zmierzyć wyłącznie pary poziome — i wszystkie wypadły źle (−18 do −24 pp). Plan elektrod został zbudowany na tym wyniku i **odziedziczył ograniczenie zbioru danych jako założenie o świecie.**

**Li i in. 2025 mieli POz** — czyli punkt leżący **bezpośrednio powyżej Oz na południku środkowym** — i ich para pionowa wypadła nieporównanie lepiej.

## 2.1 Hipoteza, która z tego wynika, i dlaczego jest fizycznie sensowna

`[wniosek, do sprawdzenia pomiarem — nie fakt]` **Liczy się nie tylko odległość odniesienia, ale kierunek względem gradientu pola SSVEP.**

Pole SSVEP nad potylicą jest rozległe i gładkie, ale **nie jest jednorodne**: ma maksimum nad korą wzrokową i opada ku górze, w stronę ciemienia. Para **pionowa** (Oz z POz) leży wzdłuż tego spadku, więc różnica dwóch elektrod **zachowuje część sygnału**. Para **pozioma** (O1 z O2) leży w poprzek, przez oś symetrii — obie elektrody widzą prawie to samo, więc różnica **kasuje sygnał**.

To jest zgodne z każdym punktem, który mam:

| Para | Orientacja | Wynik |
|---|---|---|
| POz−Oz (Li 2025) | **pionowa**, wzdłuż spadku | **46,3 bit/min\*** |
| O1−O2 (reanaliza) | **pozioma**, w poprzek symetrii | 54,2% wobec 73,3% |
| O1−Oz, O2−Oz (reanaliza) | **skośna**, blisko poziomej | 48,8% i 55,0% |
| para sutkowata (Cardoso) | **pozioma**, całkowicie poza polem | **2,5 bit/min\*** |

> **WZMOCNIONE 21 VIII 2026 — `40` §4.** Hipoteza kierunku przestaje być domysłem z czterech rozrzuconych punktów. `[fakt, PMID 16544207 i 17671957, 110 elektrod]` Pole SSVEP ma **strukturę falową**: fale biegnące o **λ > 15–20 cm** propagujące się **potylica → przedczołowie**, czyli **wzdłuż osi Oz–POz**. Dla pary odległej o `d` wzdłuż tej osi amplituda różnicy wynosi **`|2·sin(πd/λ)|`** — przy d = 3,5 cm i λ = 15–20 cm daje to **1,04–1,34**, czyli sygnał **zachowany**, a para w poprzek osi ma różnicę faz ≈ 0 i **kasuje**. **Jeden wzór tłumaczy wszystkie sześć opublikowanych punktów.**

`[luka]` **Nikt tego nie zmierzył jako zmiennej.** Wszystkie cztery punkty pochodzą z czterech różnych prac, sprzętów i grup badanych — czyli różnią się wszystkim naraz. **To jest dokładnie ten sam problem, który uzasadnia całe twierdzenie projektu, tylko w drugim wymiarze.**

---

## 3. Poprawka do planu — koszt zerowy

**Osiem wejść zostaje, zmieniają się położenia czterech.** Nie dochodzi ani jeden element, ani jedna złotówka, ani jedna sesja.

| Wejście | Było | **Ma być** | Po co |
|---|---|---|---|
| 1 | Oz | Oz | aktywna, bez zmian |
| 2 | O1 | O1 | aktywna, bez zmian |
| 3 | O2 | O2 | aktywna, bez zmian |
| **4** | ~2 cm poniżej Oz | **POz — ~3,5 cm POWYŻEJ Oz** | **odniesienie zwarte pionowe.** Kierunek, który u Li dał 46 bit/min. Nad owłosioną skórą, **powyżej inionu, poza zasięgiem karku i móżdżku** |
| **5** | ~4 cm poniżej Oz, nad karkiem | **~2 cm poniżej Oz, w obrębie modułu** | **odniesienie zwarte w dół** — zachowane jako **warunek porównawczy dla kierunku**, bez schodzenia poniżej inionu |
| 6 | wyrostek sutkowaty | wyrostek sutkowaty | bez zmian, odniesienie wyprowadzone |
| **7** | nad mięśniem karku | **nad mięśniem karku, poniżej inionu** | **zostaje jako kanał kontrolny R12** — mierzy to, czym skażone jest odniesienie schodzące w dół, i **pozwala rozstrzygnąć, czy w dół jest gorzej** |
| 8 | płatek ucha | płatek ucha | odniesienie literaturowe, górna granica |

**Zmienna główna z `16` §3.2 przestaje być jednowymiarowa:**

> **odległość odniesienia od Oz: ~2, ~3,5, ~7, ~10 cm — ORAZ kierunek: w górę (POz) wobec w dół (podpotyliczny), przy zbliżonej odległości**

`[wniosek]` **Para POz i „2 cm poniżej Oz" to warunek kontrolny w najczystszej postaci, jaką ten projekt może mieć:** zbliżona odległość, przeciwny kierunek, ta sama sesja, te same próbki, ten sam tor. Różnica między nimi jest **czystym efektem kierunku**, bez żadnej zmiennej ubocznej.

---

## 4. Co to robi z obawą użytkownika

**Obawa:** wynik brzmiący „musi być pudełko" źle się ogląda.

`[wniosek]` **Po tej poprawce najbardziej prawdopodobny wynik nie brzmi tak.** Jeżeli hipoteza kierunku się potwierdzi, zdanie końcowe brzmi:

> **POPRAWKA 21 VIII 2026 — K-100.** Sformułowanie „naklejka wielkości karty płatniczej" niżej **opisuje rozpiętość elektrod jako bryłę i jest mylące**. `[wniosek]` Realna obudowa to **~32×48×12 mm, mniej niż pudełko zapałek**, a **odległość Oz–POz (~35 mm) mieści się na jej własnym spodzie** — krytyczna para nie wymaga ani jednego przewodu. Rozbiór: `40_GABARYT_MECHANIZM_I_DOMKNIECIE.md` część I.

> **Moduł potyliczny musi być wydłużony w pionie, nie duży.** Para elektrod odległa o ~3,5 cm wzdłuż osi góra-dół zachowuje przepustowość, para o tej samej odległości w poprzek — nie. Urządzenie jest **naklejką wielkości karty płatniczej**, a nie pudełkiem.

**A jeżeli się nie potwierdzi**, zdanie brzmi:

> Kierunek nie ma znaczenia, liczy się sama odległość, i wynosi ona co najmniej X cm.

`[wniosek]` **Oba wyniki są dobre do pokazania, i to jest własność, którą twierdzenie miało od początku** (`17_RYZYKA.md` R4: „nie ma wyniku, który by je unieważnił, jest tylko wynik, który zmienia jego znak"). **Zmieniło się to, że wariant korzystny stał się znacznie bardziej prawdopodobny** — bo dotąd plan mierzył wyłącznie kierunek, w którym wszystko wypada źle.

**Uczciwie o tym, czego to nie załatwia:** `[luka]` nie wiem, czy POz zmieści się w module przy ograniczeniu z decyzji 3 („żadnej konstrukcji zbliżającej się do opaski przechylonej na tył głowy"). **Oz do POz to ~3,5 cm w górę po owłosionej skórze** — `[wniosek]` naklejka albo sztywna płytka tej wysokości mieści się w granicy, ale **to jest decyzja użytkownika, nie moja.** Pytanie do rozstrzygnięcia: czy moduł ~4×8 cm ustawiony pionowo na potylicy nadal spełnia warunek „zero hełmów".

---

## 5. Semantic Scholar — odblokowany, bez klucza

`[fakt, 21 VIII 2026]` Użytkownik zacytował dokumentację: *„Most Semantic Scholar endpoints are available to the public without authentication, but they are rate-limited (…) Requests may also be **further throttled during periods of heavy use**"*. **Ponowna próba przeszła za pierwszym razem, HTTP 200.**

`[wniosek]` **Wcześniejsze HTTP 429 było chwilowym dławieniem, nie brakiem uprawnień** — i przez trzy dni zapisywałem w dokumentacji, że baza jest niedostępna, zamiast spróbować ponownie następnego dnia. **K-098.**

**Wyszukiwanie pełnotekstowe w Semantic Scholar jest więc dostępne od zaraz i bez klucza.** Zapytania o oś (`SSVEP reference electrode distance information transfer rate`, 546 trafień; `compact EEG electrode montage inter-electrode distance evoked potential`) **nie przyniosły ani jednej pozycji o zależności przepustowości od położenia odniesienia** — potwierdzenie zgodne z pozostałymi ośmioma bazami.

**Pozycja P16a (wniosek o klucz) schodzi z listy jako niepotrzebna.** Klucz podnosi limity, ale limity nie były problemem.

---

## 6. Zadania

| # | Zadanie | Termin |
|---|---|---|
| **P26** | **przenieść wejście 4 z „2 cm poniżej Oz" na POz (~3,5 cm powyżej)** w `15_PROJEKT.md` §2.3; wejście 5 na „2 cm poniżej Oz" jako warunek kierunkowy | zrobione w tym pliku |
| **P27** | **zmienna główna dwuwymiarowa** w `16_PLAN_EKSPERYMENTALNY.md` §3.2: odległość **oraz kierunek** | zrobione w tym pliku |
| **P28** | **pytanie do użytkownika:** czy moduł wydłużony pionowo (~4×8 cm, Oz do POz) mieści się w granicy z decyzji 3 | **do rozstrzygnięcia** |
| **P29** | do materiałów: **tabela z §1** jako przeliczenie stanu wiedzy na jedną metrykę. To jest gotowy materiał na rubrykę `Research Problem` i na plakat | z P12 |
| ~~P16a~~ | ~~klucz do Semantic Scholar~~ — **niepotrzebny, baza działa bez klucza** | zamknięte |
