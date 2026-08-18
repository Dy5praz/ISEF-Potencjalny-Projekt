# 25 — Audyt w bazach niedostępnych. Wynik: oś jest zajęta szerzej, niż podawałem

**Data:** 16 sierpnia 2026, wieczorem
**Zlecenie użytkownika:** *„Spróbuj jeszcze raz sprawdzić w tych niedostępnych bazach danych czy interfejs nadal się trzyma. Jak znowu cię zablokuje, obejdź jakoś. Chcę mieć odpowiedź z tamtąd."*

**Odpowiedź w jednym zdaniu: obszedłem, dostałem odpowiedź, i jest ona zła — oś projektu jest badana od co najmniej 2005 roku, a ja jej nie widziałem, bo szukałem własnymi słowami zamiast słowami dziedziny.**

---

## 1. Czego nie udało się obejść, i mówię to wprost

| Baza | Wynik |
|---|---|
| **OpenAlex** | **HTTP 429 nadal.** Pięć prób z narastającym odczekiwaniem (3, 6, 12, 24, 48 s), pula „polite" z adresem kontaktowym w nagłówku i w parametrze. **Nie przeszedł ani jeden request** |
| **Semantic Scholar** | **HTTP 429 nadal**, trzy próby z odczekiwaniem do 20 s |
| scholar.archive.org | „Rate limit reached" |
| Scilit | HTTP 403 |

> **POPRAWKA 18 VIII 2026 — K-088.** Powód niedostępności OpenAlex nazwałem tu błędnie. `[fakt, odpowiedź API odczytana 18 VIII 2026]` OpenAlex zwraca: *„Insufficient budget. This request costs $0.001 but you only have $0 remaining. Resets at midnight UTC. Need more? Add funds at openalex.org/pricing"* — czyli **wyczerpany darmowy budżet w modelu płatnym, nie limit adresu**. Obejściem nie jest inna sieć, tylko **klucz API albo odczekanie do północy UTC**; Semantic Scholar (HTTP 429) też wydaje klucze. **Obie bazy są dostępne za darmo po założeniu klucza** — do zrobienia przy następnym przeszukaniu prior art.

`[fakt]` **To jest limit nałożony na adres tego środowiska, nie brak dostępu do treści.** Nie da się tego obejść inaczej niż z innej sieci — i **nie zamierzam próbować obejść limitu podszywaniem się**, bo to jest ta sama kategoria co fałszowanie danych.

**Obszedłem inaczej: przez indeksy, które pokrywają ten sam korpus i puszczają.**

| Baza | Status | Co pokrywa |
|---|---|---|
| **OpenAIRE** | **działa** | repozytoria uczelniane, prace dyplomowe i doktorskie, literatura europejska — **czyli dwie z luk, które sam zgłosiłem w `21_ODPOWIEDZI.md` §1.3** |
| DOAJ | działa | czasopisma otwarte |

**OpenAIRE zna 3 649 prac o SSVEP** — dla porównania arXiv zna 96. To jest realna baza, nie namiastka.

---

## 2. Pułapka składniowa — druga tego dnia

Pierwsze cztery zapytania do OpenAIRE dały **zero trafień**. Wyglądało to jak potwierdzenie, że oś jest wolna.

`[fakt]` **Kontrola pokazała, że to nieprawda.** Parametr `keywords` w OpenAIRE wymaga **wszystkich słów naraz**:

| Zapytanie | Trafień |
|---|---|
| `SSVEP` | **3 649** |
| `SSVEP electrode` | 184 |
| `SSVEP reference electrode distance` | **0** |
| `steady-state visual evoked potential electrode montage wearable occipital` | **0** |

**Czyli długie zapytanie zwraca zero niezależnie od tego, co jest w literaturze.** To jest dokładnie ta sama pułapka co w arXiv (`14_REANALIZA.md` §11.1), tylko w innym API. **Gdybym nie uruchomił kontroli, zapisałbym „OpenAIRE potwierdza, że oś jest wolna" — i byłby to fałsz wynikający z mojej składni.**

**Reguła, która z tego zostaje na stałe:** **każde „zero trafień" wymaga kontroli pozytywnej** — zapytania, o którym wiadomo, że musi coś zwrócić. Bez tego zero nic nie znaczy.

---

## 3. Co znalazłem po poprawieniu składni

Zapytania krótkie, terminami dziedziny.

| Rok | Praca | Dlaczego istotna |
|---|---|---|
| **2005** | *Lead selection for SSVEP-based brain-computer interface* | dobór odprowadzeń — nasze pytanie, sprzed dwudziestu lat |
| **2010** | ***A comparison of monopolar and bipolar EEG recordings for SSVEP detection***, EMBC, PMID 21096910 | **bezpośrednio nasza zmienna** |
| **2015** | *Monopolar and Bipolar Electrode Settings for SSVEP-Based BCI* | jw. |
| **2015** | *Impact of electrode positions and harmonic frequency components in SSVEP-based BCIs* | wpływ pozycji elektrod na wynik |
| **2019/2020** | *Assessment of high-frequency SSVEP from below-the-hairline areas*, PMID 31881401 | **SSVEP zza uszu (TP9/TP10)** — nasza forma urządzenia |
| **2021** | *Effect of Channel and Reference Selection on a Non-occipital SSVEP* | **dobór elektrody odniesienia** |
| **2025** | *Boosting Spatial Properties of Single-Flicker SSVEP via Laplacian Electrodes* | geometria laplasjanowa |
| **2026** | ***Cross-region neural signal reconstruction to lift electrode placement constraints in SSVEP BCIs***, npj Biomedical Innovations, PMID 42527436 | **nasze zdanie problemowe, dosłownie, w tytule** |

### 3.1 Praca z 2010 — odczytana w oryginale

`[fakt, abstrakt odczytany]` Pięciu badanych, bodźce 13/14/15/16 Hz. Porównanie: **dwa kanały dwubiegunowe (O1−P3 i O2−P4)** wobec **sześciu kanałów jednobiegunowych odniesionych do Fz**.

> „In average, the monopolar recordings present accuracy in classification of **74.5%** against an **80.1%** for bipolar recordings. It was found that **bipolar recording are better than monopolar recordings** for detection of SSVEP."

**Na pierwszy rzut oka to zaprzecza mojemu wynikowi z §5 pliku `14`, gdzie montaż dwubiegunowy kosztował 9–24 pp.** Zaprzeczenie jest jednak pozorne i różnica jest pouczająca:

| | Ich montaż | Mój montaż |
|---|---|---|
| dwubiegunowy | **O1−P3, O2−P4** — potylica wobec **ciemienia** | O1−Oz, O2−Oz, O1−O2 — **wszystkie trzy nad korą wzrokową** |
| jednobiegunowy | odniesienie **Fz** (czoło, elektroda czynna, łapie artefakt oczny) | odniesienie **płatek ucha** (miejsce względnie obojętne) |

`[wniosek]` **Obie obserwacje są zgodne z jednym mechanizmem: liczy się nie „dwubiegunowy kontra jednobiegunowy", tylko czy elektroda odniesienia leży WEWNĄTRZ pola SSVEP, czy poza nim.** P3 leży na skraju pola — różnicowanie zachowuje sygnał. Oz leży w środku — różnicowanie go kasuje. Fz jest daleko, ale sam zbiera zakłócenia.

**To jest dobra wiadomość dla mechanizmu i zła dla twierdzenia o nowości.** Mechanizm się broni; ale pytanie „jak dobrać odprowadzenia i odniesienie dla SSVEP" jest zadawane od dwudziestu lat, a ja pisałem rano, że jest niezajęte.

### 3.2 Praca z 2026 — nasze zdanie problemowe w cudzym tytule

`[fakt, abstrakt odczytany]` *npj Biomedical Innovations*, PMID 42527436. Pierwsze zdanie abstraktu:

> „SSVEP-based BCIs rely on **occipital EEG recordings, which are infeasible in many clinical scenarios**, restricting SSVEP-BCI access"

Rozwiązują to **inaczej niż my** — siecią neuronową rekonstruującą sygnał potyliczny z elektrod czołowych, 20 użytkowników, poprawa dekodowania do 33,47%. **Nie jest to nasza metoda.** Ale **jest to nasz problem, nazwany w 2026 roku w czasopiśmie z portfolio Nature.**

**Skutek praktyczny:** juror znający dziedzinę może zapytać *„a czemu nie robisz tego, co DSTF-Net"*. Odpowiedź musi być gotowa i brzmi: bo tamto wymaga sieci trenowanej na parach sygnałów i nie odpowiada na pytanie o gabaryt urządzenia. Ale **pytanie padnie**.

---

## 4. Co z osi zostaje, uczciwie

**Nie znalazłem — nadal — pomiaru przepustowości jako funkcji ciągłej odległości elektrody odniesienia, przy jawnym ograniczeniu gabarytowym, na jednej platformie, z raportowanym ITR.** Prace z §3 porównują **dyskretne montaże** (dwa albo trzy warianty), nie serię odległości.

**Ale muszę postawić obok tego swój dzisiejszy bilans:**

| Kiedy | Twierdziłem | Po sprawdzeniu |
|---|---|---|
| rano | oś szczękowa: pole zajęte, ale nasz kształt wolny | zysk 0,3 pp — oś upadła |
| południe | nowa oś: **niezajęta w pięciu bazach**, ryzyko 10–15% | — |
| wieczorem | — | **badana od 2005, siedem prac, dwie wprost o naszej zmiennej** |

`[wniosek]` **Moje „nie znalazłem" okazało się dziś niewiarygodne trzy razy.** Przyczyna za każdym razem ta sama i teraz nazwana: **szukałem własnym słownictwem.** Dziedzina mówi „monopolar versus bipolar", „lead selection", „channel and reference selection", „electrode placement constraints" — a ja pytałem o „reference electrode distance" i „inter-electrode distance". **Zapytanie zbudowane na własnym sformułowaniu problemu znajduje tylko tych, którzy sformułowali go tak samo.**

**Uczciwa liczba, zrewidowana:** prawdopodobieństwo, że wąska wersja osi (seria odległości pod ograniczeniem gabarytu) jest już gdzieś opublikowana — **25–40%**, nie 10–15%. Podnoszę, bo trzy razy dziś się myliłem w tę samą stronę, a nie mam podstaw sądzić, że za czwartym razem trafiłem.

---

## 5. Wniosek, który jest ważniejszy od samej osi

**Trzy projekty. Trzy osie. Wszystkie trzy okazały się zajęte, gdy przeszukać je słownictwem dziedziny.**

- **dron**: „integracja i benchmark" — sam ConOps przyznaje, że elementy istnieją osobno
- **orteza**: teza 1 zajęta (przyznane), teza 2 w polu czynnie badanym (ICORR 2025, Sensors 2025 — K-073)
- **interfejs**: oś szczękowa martwa (K-089), oś odległości odniesienia badana od 2005 (ten plik)

`[wniosek]` **To nie jest pech ani seria złych wyborów. Tak wygląda literatura, kiedy się ją naprawdę przeszuka.** Dla licealisty twierdzenie „nikt tego nie zrobił" jest praktycznie niedostępne — nie dlatego, że pomysły są słabe, tylko dlatego, że dziedzina ma dwadzieścia lat i tysiące zespołów.

**I to jest moment, żeby powiedzieć rzecz, którą powinienem był powiedzieć rano zamiast trzeciej rundy szukania dziury:**

`[fakt, `ISEF_ARKUSZE_OCENY.md`]` **W arkuszu inżynierskim ISEF nie ma rubryki „nowość".** Jest **Research Problem (10)**, **Design and Methodology (15)**, **Execution (20)**, **Creativity & Potential Impact (20)** i **Presentation (35)**. Kryteria Explory też jej nie mają — jest „innowacyjność / wkład w state-of-the-art" za 10 punktów na 40 w półfinale i nic w finale.

**Czyli optymalizowaliśmy pod kryterium, które waży najwyżej 10 punktów na 100, i trzy razy pod nie przebudowywaliśmy projekt.**

**Co waży naprawdę:** wykonanie, metodyka, testowanie w wielu warunkach i **prezentacja, która sama jest warta 35 punktów** — czyli więcej niż Research Problem, Design i Creativity razem wzięte, i więcej niż jakakolwiek różnica między naszymi trzema projektami.

---

## 6. Co z tego wynika dla decyzji

**Oś nie musi być niezajęta. Musi być mierzalna, wykonalna i uczciwie postawiona.** Nasza taka jest, po przeformułowaniu:

> *nie „nikt nie zbadał, jak odległość odniesienia wpływa na przepustowość", tylko: „porównania montaży dla SSVEP publikowano od 2005 roku, zawsze dla dwóch–trzech wariantów dyskretnych; mierzę tę zależność jako funkcję ciągłą, pod ograniczeniem gabarytu urządzenia noszalnego, i podaję ITR"*

To jest twierdzenie słabsze niż to, które napisałem rano, i **wymaga cytowania siedmiu prac z §3 zamiast przemilczenia ich**. Ale jest prawdziwe, obronne przed jurorem znającym dziedzinę, i **nie zmienia ani jednego elementu sprzętu ani planu pomiarowego**.

**Czego to nie zmienia:** `15_PROJEKT.md`, `16_PLAN_EKSPERYMENTALNY.md`, `20_ZAKUPY.md`, `24_PLAN_DZIALANIA.md` — wszystkie zostają. Zmienia się **jedno zdanie twierdzenia** i **sekcja o stanie wiedzy**, która staje się dłuższa i lepsza.

**Czego to nie przesądza:** wyboru między interfejsem a ortezą. Oba są teraz w tej samej sytuacji — pomiar w polu częściowo zajętym. Rozstrzygnięcie pozostaje tam, gdzie było w `22_POROWNANIE.md` §4: **kto może być badanym** i **co pokaże E0 w październiku**.
