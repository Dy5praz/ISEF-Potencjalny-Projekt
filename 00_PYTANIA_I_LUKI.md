# 00 — Pytania i luki przed etapem 1

**Data:** 15 sierpnia 2026
**Podstawa:** HANDBOOK.md, sekcja 14 („przeczytaj drugi raz i wypisz wszystko, co niejasne, sprzeczne albo czego brakuje")
**Status:** dokument otwarty, aktualizowany

Oznaczenia pewności wg sekcji 0 handbooka: `[fakt]` / `[wniosek]` / `[domysł]` / `[luka]`.

---

## 0. Blokada operacyjna — do rozstrzygnięcia jako pierwsza

**[fakt] To środowisko nie ma dostępu wychodzącego do sieci poza rejestrami pakietów i backendem wyszukiwarki.**

Zweryfikowane bezpośrednim testem, 15 VIII 2026. Tunel HTTPS zwracany z kodem 403 dla wszystkich sprawdzonych domen:

| Domena | Wynik | Do czego potrzebna |
|---|---|---|
| `isef.net` | zablokowana | abstrakty projektów ISEF, w tym ENBM074 |
| `abstracts.societyforscience.org` | zablokowana | oficjalna baza abstraktów |
| `societyforscience.org` | zablokowana | International Rules, arkusze oceny, Human Participants |
| `explory.pl` | zablokowana | regulamin, listy finalistów 2016–2026 |
| `arxiv.org`, `export.arxiv.org` | zablokowana | preprinty |
| `pubmed.ncbi.nlm.nih.gov` | zablokowana | literatura recenzowana |
| `nature.com`, `frontiersin.org`, `link.springer.com` | zablokowane | literatura recenzowana |
| `doi.org`, `api.crossref.org`, `openalex.org` | zablokowane | rozstrzyganie i weryfikacja cytowań |
| `scholar.google.com` | zablokowana | wyszukiwanie |
| `en.wikipedia.org` | zablokowana | nawet materiał orientacyjny |

Działa wyłącznie wyszukiwarka, która zwraca **listę linków i streszczenie wygenerowane przez inny model**. Nie mogę otworzyć źródła i sprawdzić, czy mówi to, co mu przypisuję.

### Dlaczego to blokuje etap 1, a nie tylko go spowalnia

Reguła trzech punktów z sekcji 2.2 handbooka, zastosowana do tego twierdzenia:

1. **Parametr, który się nie spina:** liczba źródeł możliwych do otwarcia i zweryfikowania = **0**. Sekcja 13 wymaga 2–3 niezależnych źródeł na każdą liczbę, na której cokolwiek się opiera, oraz sprawdzenia, że źródło istnieje i mówi to, co mu przypisuję.
2. **Wersja pracy, w której ten parametr jest poza pętlą:** przemiał literatury wykonany w środowisku z dostępem wychodzącym. Treść i wnioski etapu 1 nie zależą od tego, gdzie fizycznie zostanie wykonany.
3. **Pomiar, który przeżywa tę zmianę:** cały etap 1 bez zmian w zakresie.

Gdybym mimo to napisał pliki `/01`–`/08` na samych streszczeniach wyszukiwarki, powstałby dokładnie **błąd nr 5 z sekcji 8 handbooka**: strategia i oceny szans zbudowane na niesprawdzonym założeniu. Przy przeglądzie literatury, którego całym celem jest ustalenie, co już zrobiono, to nie jest błąd kosmetyczny — to unieważnia wynik.

### Co trzeba zrobić

Środowisko zdalne Claude Code ma politykę sieciową wybieraną przy jego tworzeniu. Trzeba je odtworzyć lub edytować z polityką dopuszczającą ruch wychodzący. Dokumentacja: `code.claude.com/docs/en/claude-code-on-the-web`.

**Minimalna lista domen, jeżeli polityka jest typu allowlist:**

```
societyforscience.org, abstracts.societyforscience.org, isef.net
explory.pl, shotx.explory.pl, fzt.org.pl
arxiv.org, export.arxiv.org, biorxiv.org, medrxiv.org
pubmed.ncbi.nlm.nih.gov, ncbi.nlm.nih.gov, pmc.ncbi.nlm.nih.gov
doi.org, api.crossref.org, api.openalex.org, openalex.org
nature.com, frontiersin.org, link.springer.com, sciencedirect.com
ieeexplore.ieee.org, iopscience.iop.org, mdpi.com, journals.physiology.org
openbci.com, emotiv.com, choosemuse.com, gtec.at, wearablesensing.com,
neurable.com, cognixion.com, nextsense.io, neuroelectrics.com
en.wikipedia.org
```

**Wariant awaryjny, gdyby zmiana polityki była niemożliwa:** etap 1 wykonany w aplikacji czatowej z dostępem do sieci, a wynik wrzucony tutaj jako pliki. Gorszy, bo rozbija dokumentację na dwa miejsca wbrew sekcji 2.2, ale wykonalny.

**Do czasu odblokowania robię wszystko, co nie zależy od sieci** — czyli ten plik, `KOREKTY.md` i strukturę repozytorium.

---

## 1. Błędy i rozbieżności znalezione w samym handbooku

Zapisane też w `KOREKTY.md`.

### 1.1 [fakt] Błąd arytmetyczny w sekcji 3, z konsekwencją operacyjną

Handbook, sekcja 3: „Do działającego prototypu ~14 miesięcy (El-Robo-Mech)".

Liczone od 14 VIII 2026 do ~15 IV 2027 to **8 miesięcy**, nie 14. Czternaście miesięcy to dystans do finału krajowego Explory (X 2027). Dwadzieścia jeden do ISEF (V 2028) — ta liczba jest poprawna.

Poprawny rozkład:

| Kamień milowy | Data | Od 14 VIII 2026 |
|---|---|---|
| zamknięcie okna zgłoszeń Explory | 28 II 2027 | ~6,5 mies. |
| El-Robo-Mech, działający prototyp | ~IV 2027 | **~8 mies.** |
| półfinał Explory | V–VI 2027 | ~9–10 mies. |
| finał krajowy, Gdynia | X 2027 | ~14 mies. |
| ISEF | V 2028 | ~21 mies. |

**Dlaczego to ma znaczenie:** handbook w tym samym zdaniu ostrzega „nie licz sześciu". Faktyczny margines do pierwszego twardego terminu sprzętowego jest o 43% krótszy, niż podaje dokument. Przy projekcie wymagającym nauczenia się projektowania PCB od zera to nie jest różnica kosmetyczna.

### 1.2 [wniosek] Luka z sekcji 4.2 jest domknięta i można ją skreślić

Handbook: „[luka] Dokładna data kwalifikacji dla edycji 2027 — do zweryfikowania".

Reguła podana w tej samej sekcji: Data Kwalifikacji edycji 2026 to 1 I 2005 i przesuwa się o rok co edycję → edycja 2027 to **1 I 2006**. Użytkownik wchodzi we IX 2026 w drugą klasę liceum czteroletniego, czyli rocznik ok. 2010. Spełnia z zapasem czterech lat.

Ta luka nie wymaga weryfikacji przed etapem 1. Zostaje jako drobiazg do potwierdzenia przy samym zgłoszeniu.

### 1.3 [wniosek] Sekcja 5.3 miesza dwa etapy w jednej liczbie

Handbook: „~300 zgłoszeń → ~3 miejsca w reprezentacji, rzędu 1%".

Arytmetycznie zgodne, ale jako wskaźnik decyzyjny mylące, bo skleja trzy różne sita o bardzo różnej sterowalności. Rozbicie na podstawie liczb z sekcji 4.11:

| Przejście | Liczby | Szansa warunkowa |
|---|---|---|
| zgłoszenie → półfinał | ~300 → do 150 | ~50% |
| półfinał → finał | 150 → 21–26 | ~14–17% |
| finał → reprezentacja ISEF | 21–26 → ~3 projekty | ~12–14% |

To zmienia obraz strategiczny. Pierwsze sito jest szerokie — kwalifikacja to nie jest wąskie gardło. **Wąskie gardło jest w przejściu półfinał → finał**, i to jest etap oceniany wg kryteriów z sekcji 4.7 etap II: innowacyjność, jakość prezentacji, znajomość metod, znajomość dotychczasowych badań. Trzy z czterech to kryteria zależne od przemiału literatury, nie od sprzętu.

Konsekwencja dla priorytetów: etap 1 nie jest przygotowaniem do właściwej pracy. Etap 1 **jest** bezpośrednio punktowany w najwęższym miejscu lejka.

### 1.4 [luka, wysoka stawka] Który finał Explory wysyła na ISEF 2028

Handbook zakłada w sekcji 3, że finał krajowy X 2027 wyłania reprezentację na ISEF V 2028. Nigdzie nie ma tego potwierdzonego cytatem z regulaminu.

Alternatywa, której nie da się wykluczyć bez sprawdzenia: laureaci finału X 2027 jadą na ISEF 2029, a reprezentacja na ISEF 2028 została już wyłoniona na GEW 20–23 X 2026. Jeżeli tak, cała teza „jeden strzał" z sekcji 3 się zmienia — bo wtedy właściwym celem jest ISEF 2029, co koliduje z maturą maj 2029, i decyzja o sensowności całego przedsięwzięcia wygląda inaczej.

**To jest pytanie o najwyższej stawce w całym dokumencie i pierwsze do sprawdzenia po odblokowaniu sieci.** Odstęp finał → ISEF wynosi przy założeniu handbooka 7 miesięcy, co jest wiarygodne [domysł], ale wiarygodne to nie to samo co sprawdzone.

### 1.5 [luka] Reguła 12/18 miesięcy nie jest wpisana w kalendarz

Handbook, sekcja 5.4: maksymalnie 12 miesięcy ciągłych badań, zakaz danych starszych niż 18 miesięcy przed ISEF. Sekcja 5.4 zaleca rezerwowanie zasobów jednorazowych „po czerwcu 2027".

Przy ISEF ~połowa maja 2028:
- 18 miesięcy wstecz → **~listopad 2026**
- okno 12 miesięcy ciągłych kończące się przy ISEF → **~maj 2027 – maj 2028**

Te dwie liczby dają różne najwcześniejsze daty startu kampanii i handbook nie rozstrzyga, jak się składają. Bez oryginalnego tekstu International Rules nie da się tego domknąć.

**Konsekwencja, którą handbook pomija:** przy oknie maj 2027 – maj 2028 wszystkie pomiary pokazane na El-Robo-Mech (IV 2027) i w półfinale Explory (V–VI 2027) wypadają **przed** oknem albo na jego krawędzi i trzeba je powtórzyć. Finał Explory (X 2027) mieści się w oknie. To nie jest problem — to pozycja harmonogramowa, która musi być wpisana w plan jako powtórzenie kampanii, a nie odkryta w marcu 2028.

### 1.6 [wniosek] Skład jury z sekcji 4.10 dotyczy edycji 2026, nie naszej

Handbook wyciąga z niego wniosek „korzystne dla projektu na styku elektroniki i neurotechnologii". Nasza edycja to 2027 i skład będzie inny. Składy jury bywają stabilne między edycjami [domysł], ale wniosek jest zbudowany na danych o jedną edycję za wczesnych i sam handbook zaznacza, że 15 z 17 nazwisk pochodzi z jednego źródła.

Nie kasuję tego wniosku — obniżam mu status z przesłanki strategicznej do obserwacji.

### 1.7 [fakt] Liczba „65 słów na minutę" nie ma statusu źródłowego

Handbook, sekcja 9.2, podaje ją jako „twierdzenie wg relacji użytkownika". Sam projekt ENBM074 i jego autorka są oznaczone `[fakt]`, ale liczby 65 i 3 wpm nie są oznaczone wcale.

Zapisuję jawnie: **65 wpm i 3 wpm to `[domysł]` do czasu odczytania pełnego abstraktu.** Handbook sam ostrzega w tej samej sekcji, żeby nie opierać na tym fizyki. Kolumna „skąd ta liczba" musi istnieć w `/06_TABELA_PARAMETROW.md`.

Weryfikacja częściowa, którą udało się zrobić samą wyszukiwarką [wniosek, jedno źródło pośrednie]: projekt ENBM074 i tytuł zgadzają się z opisem w handbooku, autorka to uczeń Nashua High School South w New Hampshire, kwalifikacja przez New Hampshire Science & Engineering Expo. Pełnego abstraktu nie odczytałem — `isef.net` i baza abstraktów są zablokowane.

Uwaga formalna: handbook konsekwentnie pisze o autorce w rodzaju żeńskim, jedno ze znalezionych źródeł wtórnych używa rodzaju męskiego. Nie mam pewnego ustalenia i do czasu potwierdzenia będę pisał neutralnie („osoba autorska", „autorstwo projektu"). To nie ma znaczenia merytorycznego, ale nie chcę powielać nieustalonego szczegółu.

---

## 2. Sprzeczności i niedopowiedzenia w samym zleceniu

To nie są rzeczy do sprawdzenia w literaturze. To są rzeczy, które musi rozstrzygnąć użytkownik, bo są decyzjami, nie faktami.

### 2.1 [wniosek] „Lepszy od komercyjnych" i „zero hełmów" prawdopodobnie się wykluczają w postaci koniunkcji

Sekcja 9.1 stawia dwa wymagania obok siebie: wynik lepszy od rozwiązań komercyjnych oraz twarde wymaganie łatwości noszenia (forma douszna/zauszna, zero hełmów, zero kabli na wierzchu).

Fizyka, która za tym stoi — i to jest ograniczenie fizyczne, nie technologiczne, więc nie zniknie:

- amplituda EEG na skórze głowy maleje z odległością od źródła korowego, a przewodnictwo objętościowe rozmywa sygnał przestrzennie
- forma douszna i zauszna umieszcza elektrody nad korą skroniową i w znacznej odległości od kory ruchowej i potylicznej, gdzie mieszkają najsilniejsze i najlepiej zbadane sygnały sterujące (rytmy sensomotoryczne, odpowiedzi wzrokowe)
- mniejszy rozstaw elektrod to mniejsza różnica potencjałów na parze i gorszy stosunek sygnału do szumu przy tym samym torze analogowym
- liczba kanałów w formie dousznej jest ograniczona geometrią, a większość metod filtracji przestrzennej (CSP i pokrewne) poprawia się z liczbą kanałów

**Wniosek:** przy tym samym paradygmacie sterowania forma niewidoczna daje **gorsze** ITR niż komercyjna czapka wielokanałowa. Nie da się jednocześnie być lepszym w przepustowości i radykalnie mniej widocznym, jeżeli mierzy się to tą samą miarą.

**To nie znaczy, że kierunek odpada** — znaczy, że twierdzenie projektu musi być zbudowane inaczej niż „lepszy". Możliwe kształty twierdzenia, które przeżywają tę fizykę:

1. **Przewaga przy stałej widoczności.** „Przy formie, której nie widać, osiągam X, gdzie dotychczasowe rozwiązania niewidoczne osiągają Y." Baseline to komercyjne rozwiązania douszne/zauszne, nie czapki. Uczciwe i obronne.
2. **Przewaga w metryce użytkowej, nie przepustowościowej.** Czas montażu, stabilność w ciągu dnia, odsetek udanych sesji bez ponownej kalibracji, tolerancja na ruch. Tu forma niewidoczna może realnie wygrywać z czapką, bo czapkę zdejmuje się po dwudziestu minutach.
3. **Przewaga w iloczynie.** Metryka złożona typu „użyteczna przepustowość × czas, przez jaki użytkownik faktycznie to nosi". Ryzykowna — juror może uznać ją za metrykę skrojoną pod wynik.

Wariant 1 albo 2 wygląda na obronny [wniosek]. Wariant 3 wymagałby bardzo mocnego uzasadnienia.

**To jest decyzja użytkownika i musi paść przed końcem etapu 1**, bo determinuje, co w ogóle mierzę w `/06_TABELA_PARAMETROW.md`.

### 2.2 [luka] Nie ma decyzji, co system ma robić

Sekcja 8 punkt 9 handbooka: „Produkt to zdolność: coś, co po projekcie da się zrobić, a wcześniej się nie dało. Pomiar jest dowodem, nie celem."

Nigdzie nie pada, jaka to zdolność. Kandydaci mają radykalnie różne konsekwencje:

| Zdolność | Paradygmat | Elektrody | Kategoria ISEF | Trudność |
|---|---|---|---|---|
| komunikacja osoby niemówiącej (literowanie/mowa) | P300, SSVEP, wyobrażona mowa | dużo, potylica/skroń | ENBM | bardzo wysoka |
| sterowanie dyskretne, kilka komend | wyobrażenie ruchu, SSVEP | mało, kora ruchowa/potylica | EBED lub ENBM | średnia |
| ciągłe sterowanie (kursor, protetyka) | wyobrażenie ruchu | dużo, kora ruchowa | ROBO lub ENBM | wysoka |
| monitoring stanu (senność, uwaga, napad) | pasma spoczynkowe | mało, forma douszna wystarcza | BMED lub ENBM | niska–średnia |

Handbook implicite zakłada komunikację, bo takim projektem jest precedens z 9.2 — ale sekcja 9.2 jednocześnie zakazuje kopiowania tamtego podejścia i celowania w tamten wynik. **Zostawienie tego niedopowiedzianym to prosta droga do przypadkowego wejścia w wariant, którego handbook zakazuje.**

To jest luka nr 1 do zamknięcia. Etap 1 dostarczy do niej materiału (co jest realnie osiągalne w formie dousznej), ale wybór należy do użytkownika.

### 2.3 [luka] Nie wiadomo, czy „interfejs neuralny" znaczy wyłącznie EEG

Sekcja 7 odnotowuje „MMG vs sEMG — odrzucony, użytkownik: zbyt medyczne". Sekcja 10.A każe jednocześnie uwzględnić w przeglądzie sEMG i silent speech typu AlterEgo.

Rozstrzygnięcie ma duże konsekwencje, bo sEMG z okolicy twarzy i szyi ma amplitudę o rzędy wielkości większą niż EEG, jest łatwiejszy do ukrycia w formie zausznej i jest znacznie mniej wymagający dla toru analogowego. Jeżeli jest dopuszczalny jako **kanał pomocniczy** w układzie hybrydowym, otwiera to przestrzeń projektową, która przy czystym EEG jest zamknięta.

Odrzucenie z sekcji 7 dotyczyło sEMG jako **osi projektu** w innym kontekście. Nie czytam go jako zakazu użycia sEMG jako składnika — ale nie zgaduję. Pytanie w sekcji 4 poniżej.

### 2.4 [luka] „Zero hełmów" nie ma definicji operacyjnej

Sekcja 10.F każe zrobić kolumnę „czy widać, że użytkownik to ma na sobie", ale nie ma progu. Bez progu ta kolumna jest opinią, a opinii nie da się porównać między wierszami tabeli.

Przypadki graniczne, które trzeba rozstrzygnąć:
- opaska bez widocznych kabli, elektronika w środku (klasa Muse) — przechodzi czy nie?
- coś schowanego całkowicie pod włosami
- coś wyglądającego jak słuchawki douszne lub nauszne
- czapka, w którą wszyto elektrody
- element za uchem wielkości aparatu słuchowego

### 2.5 [wniosek] Zależność El-Robo-Mech nie jest rozstrzygnięta, a ustawia cały kalendarz

Sekcja 3 traktuje kwiecień 2027 jako twardy termin działającego prototypu. Sekcja 6 mówi, że nie wiadomo, czy interfejs neuralny w ogóle się tam kwalifikuje, bo to konkurs robotyczno-mechatroniczny.

Jeżeli nie kwalifikuje, twardy termin z kwietnia 2027 znika i harmonogram rozluźnia się o kilka miesięcy — albo trzeba znaleźć zamiennik dający zewnętrzną walidację, którą sekcja 4.13 wskazuje jako realny wyróżnik. To pytanie trzeba rozstrzygnąć wcześnie, bo od niego zależy, czy pierwszy twardy termin sprzętowy jest za 8 miesięcy, czy za 14.

---

## 3. Czego brakuje do oceny wykonalności czegokolwiek

Handbook sam wskazuje budżet i laboratorium (sekcja 1). Dokładam pozycje, bez których ocena wykonalności też nie wyjdzie.

| Brak | Dlaczego blokuje |
|---|---|
| **budżet** | wskazany w handbooku; bez tego nie da się ocenić żadnego wariantu sprzętowego |
| **godziny tygodniowo** | handbook liczy miesiące, nigdzie nie liczy godzin. 8 miesięcy po 4 h/tydz. to 140 h — na naukę PCB od zera plus budowę toru analogowego niskoszumnego to jest mało. Po 15 h/tydz. to 500 h i zupełnie inna rozmowa |
| **sprzęt pomiarowy** | tor analogowy dla EEG wymaga pomiaru szumu na poziomie mikrowoltów. Bez oscyloskopu o niskim szumie własnym albo karty pomiarowej nie da się **udowodnić**, że front-end działa — a dowód jest połową twierdzenia |
| **dostęp do laboratorium** | sekcja 1; dodatkowo zasób jednorazowy wg sekcji 5.4, więc wymaga zaplanowania, nie zużycia przypadkiem |
| **opiekun naukowy / Qualified Scientist** | sekcja 5.5 wskazuje, że ISEF prawdopodobnie tego wymaga przy badaniach z udziałem ludzi. Brat kończący studia inżynierskie [domysł] nie spełnia definicji Qualified Scientist. To ryzyko formalne, nie merytoryczne, i dyskwalifikuje niezależnie od jakości projektu |
| **kto będzie badanym** | badanie na sobie a badanie na niepełnoletnich kolegach to inne formularze, inne terminy i inna wielkość próby. Wielkość próby determinuje, czy twierdzenie da się w ogóle statystycznie obronić |
| **drukarka 3D — status** | handbook pisze „planowana / nabywana". Forma douszna i zauszna to warstwa 2 z sekcji 9.4 i bez druku iteracje trwają tygodniami zamiast dni |

---

## 4. Pytania — wszystkie naraz

Zgodnie z sekcją 2.2: grupami, konkretne, po wykonaniu tego, co dało się wykonać bez odpowiedzi.

### Grupa A — środowisko pracy (blokuje etap 1)

**A1.** Czy możesz zmienić politykę sieciową środowiska, czy mam przyjąć wariant awaryjny z sekcji 0 i przenieść przemiał literatury do aplikacji czatowej?

### Grupa B — zasoby (blokują ocenę wykonalności)

**B1.** Budżet: jaki rząd wielkości i czy jest jednorazowy, czy rozłożony na miesiące?
**B2.** Ile godzin tygodniowo realnie, osobno dla roku szkolnego i dla wakacji?
**B3.** Jaki sprzęt pomiarowy masz pod ręką, a jaki możesz pożyczyć przez brata? Konkretnie: oscyloskop (jaki), generator, zasilacz laboratoryjny, multimetr, karta pomiarowa, stacja lutownicza z regulacją.
**B4.** Drukarka 3D — kiedy realnie, jaka technologia?
**B5.** Czy jest ktoś, kto może wystąpić jako opiekun naukowy z tytułem — nauczyciel, znajomy z uczelni, ktoś przez brata?

### Grupa C — zakres twierdzenia (blokuje etap 2, ale odpowiedź kształtuje etap 1)

**C1.** Jaką **zdolność** ma dawać urządzenie? Tabela w 2.2 — który wiersz, albo inny?
**C2.** W czym konkretnie ma być „lepsze od komercyjnych"? Patrz 2.1 — wariant 1 (przewaga przy stałej widoczności), wariant 2 (metryka użytkowa), czy coś innego? Jeżeli nie masz zdania, powiedz to i podam rekomendację po etapie 1, ale wtedy etap 1 musi zebrać dane pod wszystkie warianty i będzie dłuższy.
**C3.** Czy sygnał musi pochodzić z mózgu, czy dopuszczasz układ hybrydowy z sEMG/EOG jako kanałem pomocniczym? Patrz 2.3.
**C4.** Kto będzie badanym: tylko ty, czy także inne osoby? Jeżeli inne — pełnoletnie czy nie?

### Grupa D — granice formy

**D1.** „Zero hełmów" — rozstrzygnij przypadki graniczne z 2.4. Wystarczy: przechodzi / nie przechodzi przy każdym.
**D2.** Czy dopuszczalne jest, żeby urządzenie było widoczne, ale wyglądało jak coś innego (słuchawki, aparat słuchowy), czy ma być niewidoczne?

### Grupa E — potwierdzenia do handbooka

**E1.** Potwierdzasz korektę 1.1 (8 miesięcy do El-Robo-Mech, nie 14)?
**E2.** Czy wiesz skądkolwiek, który finał Explory wysyła na ISEF 2028 (punkt 1.4)? Jeżeli nie, sprawdzam to jako pierwsze po odblokowaniu sieci — ale jeżeli masz kontakt do organizatora, to jest szybsza droga niż regulamin.
**E3.** Liczby 65 i 3 wpm z sekcji 9.2 — skąd je masz? Z abstraktu, z relacji, ze strony konkursu? To zmienia ich status źródłowy.

---

## 4b. Odpowiedzi użytkownika — 15 VIII 2026

### A1 — środowisko

**Decyzja: zmieniamy politykę sieciową.** Praca w aplikacji czatowej odrzucona jako niedająca odpowiedniego poziomu.

Ustalone z dokumentacji [fakt, źródło: `code.claude.com/docs/en/cloud-environments`]: środowisko chmurowe ma pole **Network access** o czterech poziomach — **None**, **Trusted** (obecny; wyłącznie rejestry pakietów, GitHub, SDK chmurowe), **Full** (dowolna domena), **Custom** (własna lista, opcjonalnie z domyślną).

Ścieżka: `claude.ai/code` → przycisk z ikoną chmurki nad polem wiadomości → najechać na środowisko → zębatka → pole **Network access** → **Full**. Przy wariancie **Custom** trzeba zaznaczyć „Also include default list of common package managers" i wkleić listę z sekcji 0.

Zmiana nie działa wstecz na już uruchomioną sesję — wymagana nowa sesja w tym środowisku.

### B — zasoby

**B1. Budżet:** nieustalony świadomie. Decyzja użytkownika: najpierw opracowanie, potem ocena kosztu. Rząd 15 000 zł z porzuconego projektu drona jako informacja o tym, co było wyobrażalne — **nie jako limit i nie jako założenie**.

**B2. Czas: 10 h/tydzień na spokojnie, z zapasem w górę.** Przeliczenie:

| Do czego | Tygodni | Godzin przy 10 h/tydz. |
|---|---|---|
| El-Robo-Mech, IV 2027 | ~35 | **~350 h** |
| finał Explory, X 2027 | ~61 | ~610 h |
| ISEF, V 2028 | ~91 | **~910 h** |

[wniosek] Budżet czasowy nie jest wąskim gardłem. Wąskim gardłem jest kolejność: nauka projektowania PCB musi się skończyć przed startem budowy toru analogowego, nie równolegle z nim.

**B3–B5:** bez odpowiedzi. Sprzęt pomiarowy, drukarka 3D i opiekun naukowy nadal `[luka]`. B5 (opiekun) pozostaje ryzykiem formalnym o wysokiej stawce — patrz sekcja 3.

### C1 — zdolność: sterowanie dyskretne

**Decyzja: sterowanie, nie komunikacja.** Uzasadnienie użytkownika: komunikacja wchodzi w pole ENBM074 i wymusza pobicie tamtego wyniku, czego sekcja 9.2 handbooka zakazuje.

[wniosek] Argument jest mocniejszy, niż został postawiony: komunikacja to najgęściej obsadzony poddział dziedziny w ogóle, więc konkurencją są laboratoria akademickie, nie pojedynczy projekt licealny.

**Rekomendacja przyjęta: dyskretne, nie ciągłe.**

| | Dyskretne | Ciągłe |
|---|---|---|
| co produkuje | jedna z N komend co kilka sekund | wartość odświeżana kilkadziesiąt razy na sekundę |
| metryka | dokładność klasyfikacji + ITR, standardowe | brak jednej standardowej |
| elektrody | mało, zgodne z „zero hełmów" | gęsta siatka nad korą ruchową, czyli czapka |
| trening użytkownika | krótki | bardzo długi |
| ryzyko niesterowalne | małe | [wniosek, do weryfikacji] „BCI illiteracy" — u części osób nie działa niezależnie od jakości sprzętu |
| zejście o poziom w dół | 8 komend → 4 komendy | brak czystego zejścia |
| pokaz na stoisku | ~30 s | trudny |

**Ostrzeżenie zapisane:** granica sterowanie/komunikacja jest płynna. Sterowanie dyskretne z dużą liczbą komend degeneruje się w wybieranie liter z menu, czyli w komunikację. Granicy pilnuje treść twierdzenia projektu, nie konstrukcja urządzenia. Do pilnowania świadomie przez cały etap 2.

### C3 — sEMG / EOG dopuszczone, ale w roli drugiej

Użytkownik nie znał tych skrótów. Wyjaśnienie i rozstrzygnięcie:

- **sEMG** (elektromiografia powierzchniowa) — napięcie z pracujących mięśni pod elektrodą. Przy uchu głównie mięsień skroniowy, czyli zaciskanie szczęki.
- **EOG** (elektrookulografia) — gałka oczna jest stałym dipolem elektrycznym (przód dodatni, tył ujemny), więc ruch oka zmienia napięcie na skórze wokół oczodołu. Mrugnięcie daje sygnał bardzo duży.

[wniosek, rzędy wielkości do potwierdzenia w etapie 1] EEG na skórze głowy: jednostki do ~100 µV. EOG: kilkanaście do kilkuset razy więcej. sEMG: jeszcze więcej. Stąd znacznie niższe wymagania wobec toru analogowego.

**Rozstrzygnięcie — dwie role, różne ryzyko:**

1. **Jako źródło sterowania — odłożone, nie odrzucone.** To nie są sygnały mózgowe. Urządzenie sterowane szczęką i okiem nie jest interfejsem neuralnym, tylko czytnikiem grymasów, i jury znające dziedzinę wyłapie to przy stoisku. Zderza się ze standardami etycznymi Explory (sekcja 4.5, krytycyzm wobec własnych wyników). Uczciwe postawienie jest możliwe wyłącznie jako jawnie hybrydowy układ — klasa uznana i publikowana — ale wtedy nie wolno tego sprzedawać jako interfejsu mózgowego. Do sprawdzenia w etapie 1: stan literatury hybrydowej.
2. **Jako kanał odniesienia do usuwania zakłóceń z EEG — przyjęte.** Przy uchu największe rejestrowane sygnały to właśnie szczęka i oko; zagłuszają EEG. Osobny kanał mierzący wyłącznie te zakłócenia pozwala je odjąć **w torze analogowym**, sprzętowo.

[domysł] Rola 2 siedzi w warstwie 3 z sekcji 9.4 handbooka (tor analogowy front-endu), czyli w najmocniejszej umiejętności użytkownika, i daje twierdzenie wymagające zbudowania płytki — czyli takie, którego nie powtórzy ktoś z laptopem i publicznym zbiorem danych. To jest kandydat na oś projektu, ale wymaga potwierdzenia w etapie 1, że nie jest to rozwiązane i opublikowane.

---

## 4c. Runda druga — 15 VIII 2026

### C1 (powrót) — ciągłe vs dyskretne, rozstrzygnięcie

Użytkownik: „ciągłe brzmi lepiej i w coś takiego celowałem. No chyba, że z dyskretnym da się osiągnąć podobny efekt, kosztem większej ilości pracy."

**Odpowiedź: da się, i rozstrzygnięcie polega na rozdzieleniu dwóch warstw, które w pytaniu są sklejone.**

1. **odczyt sygnału** — dyskretny czy ciągły
2. **ruch sterowanego obiektu** — skokowy czy płynny

Warstwy są niezależne. Dyskretny odczyt + płynny ruch to normalna, działająca kombinacja.

**Dlaczego odczyt ciągły zderza się z twardym wymaganiem „zero hełmów":**

[wniosek, do policzenia w etapie 1] Ciągłe sterowanie z EEG opiera się w praktyce na rytmach sensomotorycznych, których źródło leży w korze ruchowej — pozycje C3/Cz/C4 układu 10–20, czyli linia ucho–wierzch–ucho. Z okolicy ucha to jest kilkanaście centymetrów przez kość skroniową. Amplituda tam spada prawdopodobnie do okolic szumu własnego wzmacniacza.

Reguła trzech punktów z sekcji 2.2 handbooka:
1. **parametr:** pozycja elektrody względem źródła korowego; odległość ucho ↔ kora ruchowa
2. **wersja poza pętlą:** paradygmaty, których generator neuronalny leży blisko ucha — uwaga słuchowa, słuchowy oddball; kora słuchowa siedzi w płacie skroniowym kilka cm od kanału słuchowego. Te paradygmaty są z natury dyskretne
3. **pomiar, który to przeżywa:** dokładność klasyfikacji i ITR — ta sama metryka w obu wariantach, więc twierdzenie pozostaje porównywalne

**Jak uzyskać efekt ciągły przy odczycie dyskretnym:**

- **sterowanie prędkością zamiast pozycją** — komenda ustawia kierunek, obiekt jedzie sam do następnej komendy. Cztery komendy co ~2 s wystarczają do gładkiego ruchu
- **podział pracy z maszyną** — mózg podaje intencję („weź kubek"), maszyna wykonuje część płynną. [wniosek, do potwierdzenia w etapie 1] uznana i publikowana klasa rozwiązań, **nie liczyć jako innowacji**

**Gdzie leży „większa ilość pracy", o którą pytał użytkownik:** w mechanice i układzie sterowania budowanego obiektu, nie w algorytmie. Dla profilu z sekcji 1 handbooka to przesunięcie korzystne.

**Haczyk do obsłużenia od pierwszego szkicu:** im więcej pracy wykonuje maszyna, tym mocniejsze będzie pytanie jurora „ile z tego to naprawdę mózg". Odpowiedź musi być pomiarowa — ten sam układ na sygnale losowym i na sygnale z głowy, porównanie. **To jest element planu eksperymentalnego, nie dodatek**; nie da się go dorobić po fakcie.

**Ustalenie: odczyt dyskretny, zachowanie sterowanego obiektu ciągłe.**

### C3 (powrót) — typ przed weryfikacją, zapisany świadomie

Użytkownik przyjął rolę 2 (kanał odniesienia do usuwania zakłóceń) i poprosił o sprawdzenie, czy nie jest to powszechne, powołując się na wcześniejsze wpadki z rzekomą innowacyjnością.

**Typ zapisany przed sprawdzeniem, żeby nie było niejasności co do tego, kiedy powstał:**

[domysł, mocny] W wersji ogólnej to jest znane i stare — usuwanie zakłóceń ocznych przez osobny kanał odniesienia to technika podręcznikowa z okolic lat 80. Jeżeli tak, samo „dokładam kanał referencyjny" **nie przejdzie kryterium innowacyjności w półfinale**.

[domysł] Możliwa wąska szczelina: nie sam pomysł, lecz realizacja **sprzętowa, w torze analogowym, przed przetwornikiem, w urządzeniu noszonym przy uchu**. Standardowo odejmuje się programowo, po nagraniu. Różnica niebłaha — zakłócenie usunięte przed wzmocnieniem nie zjada zakresu dynamicznego wzmacniacza. Ale to szczelina, nie otwarte pole.

**Zadanie na etap 1, priorytet wysoki:** rozstrzygnąć to twardo, z podaniem wyniku również w wersji „zajęte".

### B3 — brak sprzętu pomiarowego

Stan: brak czegokolwiek pod pomiary interfejsów neuralnych.

[wniosek] Nie blokuje, ale wymaga planu, bo połowa twierdzenia o własnym torze analogowym to **dowód**, że jest cichy.

| Pomiar | Czym | Status |
|---|---|---|
| szum własny wzmacniacza, sprowadzony na wejście | zwarcie wejść + nagranie własnym urządzeniem; komputer wystarczy | [wniosek] metoda standardowa, do potwierdzenia |
| sygnał wzorcowy o znanej amplitudzie µV | dzielnik rezystorowy z wyjścia słuchawkowego komputera | [wniosek] do potwierdzenia, w tym szum i zniekształcenia źródła |
| niezależne potwierdzenie na sprzęcie klasy laboratoryjnej | firma brata | **zasób jednorazowy, rezerwacja po VI 2027** wg sekcji 5.4 handbooka |

### B4 — drukarka 3D, wymaganie prawdopodobnie się odwraca

Stan: wybrana Qidi Q2 pod porzucony projekt drona, uzasadniona materiałami trudnymi (PA12-CF). Użytkownik pyta, czy nadal są potrzebne.

[wniosek, do potwierdzenia w etapie 1] **Prawdopodobnie nie, i wymaganie odwraca się co do kierunku.** Dron potrzebował sztywności, wytrzymałości i odporności termicznej. Urządzenie noszone przy uchu potrzebuje odwzorowania kształtu, gładkiej powierzchni, bezpieczeństwa kontaktu ze skórą i miejscami miękkości.

[wniosek] Obudowy aparatów słuchowych i wkładek dousznych wykonuje się przemysłowo drukiem żywicznym (SLA/MSLA), nie FDM: FDM zostawia warstwy zbierające zabrudzenia, słabo odwzorowuje drobne krzywizny i ma ubogą ofertę materiałów z certyfikatem kontaktu ze skórą. Włókno węglowe jest tu przeciwskuteczne — ścierne i sztywne.

**Rekomendacja: wstrzymać zakup.** Przy formie dousznej/zausznej właściwy zestaw to tania drukarka żywiczna plus ewentualnie zwykły FDM, łącznie taniej niż jedna Q2. Q2 pozostaje sensowna, jeżeli dron kiedyś wróci, ale to osobna decyzja.

**Zadanie na etap 1:** materiały do kontaktu ze skórą, ich certyfikaty i dostępność dla amatora.

### B5 / C4 — opiekun i badania na ludziach

Stan: opiekun dostępny w szkole, stopień magistra. Badania na start na sobie, rozszerzenie na grupę przed finałem Explory. Użytkownik zakłada, że badania sprzed zgody komisji można powtórzyć po jej uzyskaniu.

[wniosek] Założenie o powtórzeniu jest poprawne — to standardowa droga i handbook opisuje ją w sekcji 5.4.

**Dwie pozycje `[luka]`, priorytet wysoki, do pliku `ISEF_HUMAN_PARTICIPANTS.md`:**

1. ISEF rozróżnia kilka ról dorosłego opiekuna o różnych progach — od wymagającej wyłącznie pełnoletności po wymagającą stopnia doktora. **Która rola obowiązuje przy urządzeniu elektronicznym w kontakcie z głową — nieustalone.** Magister może wystarczyć. Nie zgaduję, bo błąd tutaj dyskwalifikuje.
2. **Czy badanie na samym sobie jest zwolnione z obowiązku zgody komisji przed rozpoczęciem — nieustalone.** Zgoda komisji i zgoda badanego to dwa różne wymogi i zwolnienie z drugiego nie oznacza zwolnienia z pierwszego.

**Konsekwencja harmonogramowa, wynikająca z planu C4:** dane zebrane przed zgodą komisji przepadają dla ISEF. Skoro rozszerzenie na grupę ma nastąpić przed finałem Explory (X 2027), **zgoda komisji musi być wcześniej niż ta kampania**. Formalności idą przed pomiarami na grupie, nie po nich.

### D1 / D2 — granica „zero hełmów"

| Forma | Werdykt |
|---|---|
| element za uchem wielkości aparatu słuchowego | **przechodzi** |
| opaska na głowę, nawet bez widocznych kabli | **raczej odpada**, użytkownik zaznaczył wahanie |
| pozostałe przypadki graniczne z sekcji 2.4 | nierozstrzygnięte |

[wniosek] Werdykt jest spójny z ustaleniem C1: forma zausznej wielkości aparatu słuchowego i tak wyklucza elektrody nad korą ruchową, więc odczyt ciągły odpada niezależnie od tego rozstrzygnięcia.

### Pytania nadal otwarte

- **C2** — w czym konkretnie „lepsze od komercyjnych". Zostawione otwarte decyzją użytkownika. Etap 1 zbiera dane pod warianty 1 i 2 z sekcji 2.1
- **D1 przypadki graniczne** — coś schowanego pod włosami, coś wyglądającego jak słuchawki, czapka z wszytymi elektrodami
- **E1, E2, E3** — potwierdzenia do handbooka

Zamknięte w rundzie drugiej: B2, B3, B4, B5, C1, C3, C4, D2 i D1 częściowo.

---

## 4d. Lista zadań weryfikacyjnych wyniesiona z rund 1–2

Do wykonania w etapie 1, w tej kolejności.

| # | Do sprawdzenia | Dlaczego priorytet | Plik docelowy |
|---|---|---|---|
| 1 | który finał Explory wyłania reprezentację na ISEF 2028 | pod tym stoi cała teza „jeden strzał" | `08` + `KOREKTY` |
| 2 | ISEF Human Participants: role opiekuna i ich progi; czy badanie na sobie wymaga zgody komisji przed startem; wymogi wobec urządzeń elektrycznych w kontakcie z człowiekiem | dyskwalifikacja na technikalium | `ISEF_HUMAN_PARTICIPANTS.md` |
| 3 | czy sprzętowe usuwanie zakłóceń mięśniowo-ocznych w torze analogowym urządzenia dousznego jest już zrobione | pod tym stoi kandydat na oś projektu | `04` |
| 4 | amplituda rytmów sensomotorycznych w pozycjach usznych i zausznych, liczby | domyka argument, że odczyt ciągły wymusza hełm | `03` |
| 5 | paradygmaty działające przy uchu: uwaga słuchowa, oddball słuchowy, SSVEP — realne ITR i dokładności | wyznacza pułap tego, co obiecujemy | `07` |
| 6 | czy „intencja od mózgu, wykonanie od maszyny" jest publikowaną klasą rozwiązań i jak się ją uczciwie raportuje | żeby nie sprzedać znanego jako nowe | `04` + `07` |
| 7 | materiały do druku w kontakcie ze skórą, certyfikaty, dostępność dla amatora; SLA vs FDM dla wkładek | decyzja zakupowa czeka | `05` |
| 8 | metoda pomiaru szumu wzmacniacza bez oscyloskopu; źródło wzorcowe µV z karty dźwiękowej | bez tego nie ma dowodu na tor analogowy | `03` |
| 9 | El-Robo-Mech: regulamin 2027, data, czy interfejs się kwalifikuje; alternatywy | ustawia, czy pierwszy twardy termin to 8 czy 14 miesięcy | `08` |
| 10 | pełny abstrakt ENBM074 | żeby nie wejść przypadkiem w zakazaną ścieżkę | `08` |
| 11 | projekty neuro/EEG/BCI w finałach Explory 2016–2026, liczby | weryfikacja argumentu z sekcji 9.3 handbooka | `08` |
| 12 | oba arkusze oceny ISEF w całości | sekcja 5.2 handbooka | osobny plik |

---

## 5. Co robię po odpowiedziach

Etap 1 w całości, wszystkie pliki `/00`–`/08` plus `/ZRODLA.md`, bez przerywania na potwierdzenia — zgodnie z sekcją 14 handbooka.

Odpowiedzi z grup C i D nie blokują startu przemiału, ale bez nich etap 1 musi pokryć szerszy zakres, więc potrwa dłużej. Odpowiedzi z grupy A blokują całkowicie.
