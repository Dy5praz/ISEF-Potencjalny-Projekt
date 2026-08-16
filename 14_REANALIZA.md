# 14 — Reanaliza danych Kołodziej i in. 2026

**Data:** 16 sierpnia 2026, pierwszy dzień etapu 2
**Status: to jest najważniejszy plik etapu 2. Zmienia oś projektu.**

---

## 0. Streszczenie w pięciu zdaniach

`[fakt]` Zbiór danych, na którym stoi cała oś projektu, **jest publiczny** — autorzy opublikowali go na licencji CC-BY razem z artykułem. Pobrałem go, odtworzyłem ich pipeline i **zreprodukowałem ich tabelę współczynników co do trzeciego miejsca po przecinku**, więc to, co poniżej, nie jest domysłem z abstraktu.

**Wynik: przyrost +9 pp, wokół którego zbudowaliśmy całe twierdzenie projektu, nie pochodzi od kanału szczękowego. Pochodzi od Cz, i to w całości.** Kanał szczękowy dokłada +0,1 do +0,4 pp. Sprawdzone dwoma niezależnymi klasyfikatorami.

**Drugi wynik, jeszcze ważniejszy dla formy urządzenia:** montaż zamknięty wewnątrz zwartego modułu potylicznego (elektroda odniesienia wewnątrz modułu) kosztuje **9,3–24,5 pp dokładności**, a w szczytowej przepustowości **41% ITR**, względem montażu z odległą referencją — bo różnicowanie dwóch elektrod nad korą wzrokową kasuje sam SSVEP, nie tylko zakłócenie.

**Konsekwencja: oś „analogowa kompensacja artefaktu szczękowego" traci ilościowe uzasadnienie i musi zostać wymieniona.** Co wchodzi w jej miejsce — sekcja 7. Czego nie wolno zrobić — sekcja 8.

---

## 1. Skąd dane i jak sprawdzone

`[fakt]` Pełny tekst pracy (PMC12899023) zawiera zdanie przeoczone w etapie 1:

> „The recorded EEG signals are publicly available in the database *A Database of EEG and EMG SSVEP Recordings for Artifact Analysis and Removal* (https://github.com/kolodzima/EEG_artefact_SSVEP_EMG_EOG)"

Licencja artykułu: **CC BY** (potwierdzone w rekordzie PMC OA). Repozytorium sklonowane, 72 MB, dwanaście archiwów S01–S12.

**Zawartość:** 54 pliki `.mat` (format MATLAB v7.3 = HDF5), łącznie **3240 okien jednosekundowych**. Każde okno: 256 próbek × 3 kanały potyliczne (O1, O2, Oz) plus 256 próbek × 6 kanałów pomocniczych. Kolejność kanałów pomocniczych: **Cz, Fp1, HEOG, kark, policzek, szczęka**.

**Uwaga o rozmiarze zbioru, istotna przy czytaniu wszystkich liczb niżej:** na uczestnika przypadają **trzy sesje po 60 s**, czyli **trzy minuty nagrania na osobę**. To jest mało. Cały zbiór to 54 minuty sygnału.

### 1.1 Walidacja — czy na pewno odtwarzam ich metodę

Dwie kontrole, obie zaliczone:

| Kontrola | Wynik |
|---|---|
| średnie \|β\| dla sześciu kanałów pomocniczych wobec Tabeli 9 pracy | **zgodność co do trzeciego miejsca po przecinku, wszystkie sześć kanałów** |
| moje czyszczenie regresją wobec gotowego `X_tgt_cln` w plikach autorów | **różnica względna 0,0000** |

Odtworzone \|β\|: Cz 0,416 / Fp1 0,115 / HEOG 0,136 / kark 0,097 / policzek 0,127 / szczęka 0,132 — **identyczne z Tabelą 9**.

`[wniosek]` Odtwarzam ich metodę wiernie i mam prawidłową kolejność kanałów. Wszystko poniżej jest liczone tym samym kodem.

Kod: `analiza/` w tym repozytorium, sześć skryptów, uruchamialne od zera po `pip install numpy scipy scikit-learn h5py`.

---

## 2. Wynik główny — zysk należy do Cz, nie do szczęki

Dwa niezależne tory klasyfikacji. Baza porównania: te same 3240 okien, trzy cele (7, 8, 9 Hz), poziom losowy 33,3%.

### 2.1 FBCCA — metoda standardowa w dziedzinie, bez uczenia

| Kanały pomocnicze użyte do kompensacji | Dokładność | Zysk |
|---|---|---|
| **brak (O-only)** | **73,3 ± 19,8%** | — |
| wszystkie sześć | 77,4 ± 19,9% | +4,1 pp |
| **Cz sam** | **78,0 ± 19,7%** | **+4,7 pp** |
| bez Cz (Fp1+HEOG+kark+policzek+szczęka) | 75,0 ± 21,0% | +1,7 pp |
| **tylko mięśniowe (kark+policzek+szczęka)** | **73,2 ± 21,7%** | **−0,1 pp** |
| **szczęka sama** | **73,5 ± 20,1%** | **+0,2 pp** |
| kark sam | 73,3 ± 20,1% | 0,0 pp |
| policzek sam | 73,5 ± 21,2% | +0,2 pp |
| Cz + szczęka | 78,4 ± 19,1% | +5,1 pp |

### 2.2 SVM liniowy na cechach FFT, leave-one-subject-out — pipeline autorów

| Kanały pomocnicze | Dokładność | Zysk |
|---|---|---|
| **brak (O-only)** | **65,0 ± 22,3%** | — |
| wszystkie sześć | 73,1 ± 21,5% | +8,1 pp |
| **Cz sam** | **73,2 ± 21,6%** | **+8,2 pp** |
| bez Cz | 68,6 ± 21,6% | +3,6 pp |
| **tylko mięśniowe** | **64,5 ± 21,3%** | **−0,5 pp** |
| szczęka sama | 65,3 ± 22,8% | +0,3 pp |
| kark sam | 62,2 ± 20,5% | **−2,8 pp** |
| Cz + szczęka | 73,6 ± 21,7% | +8,6 pp |

**Mój przyrost dla pełnego zestawu (+8,1 pp) zgadza się z ich publikowanym (+9,1 pp) w granicy jednego punktu procentowego.** Odtwarzam więc nie tylko współczynniki, ale i główny wynik pracy.

### 2.3 Co z tego wynika, w jednym zdaniu

`[fakt, dwa niezależne klasyfikatory, dane autorów]` **Cały mierzalny zysk pochodzi z Cz. Kanał szczękowy dokłada ponad samo Cz +0,4 pp — tyle samo w obu torach. Kanał karkowy nie dokłada nic albo szkodzi.**

To jest dokładnie ta liczba, której `PRZEKAZANIE.md` sekcja 4.2 kazała szukać jako **pierwszej rzeczy do wyciągnięcia z pełnego tekstu**: rozbicie udziału kanału szczękowego wobec karkowego. Odpowiedź: **szczęka 0,132, kark 0,097 w \|β\|, ale oba nieistotne wobec Cz = 0,416, i oba nieistotne w dokładności klasyfikacji.**

---

## 3. Dlaczego Cz działa — i dlaczego to nie jest kompensacja mięśnia

Trzy niezależne przesłanki, że rola Cz to **odniesienie i tłumienie składowej wspólnej**, a nie modelowanie artefaktu mięśniowego:

1. `[fakt, cytat z pracy]` Sami autorzy piszą, że Cz „**consistently capture global interference components** also present in occipital channels" i że ma **najniższą zmienność** (CV ≈ 0,42, przy 1,25–1,51 dla kanałów mięśniowych i ocznych). Kanał modelujący konkretny mięsień musiałby być zmienny w czasie, bo mięsień pracuje epizodycznie — Cz jest stabilny, czyli opisuje coś, co jest obecne ciągle.
2. `[fakt, źródło niezależne]` **Wu Z., Su S., *PLoS One* 9(8):e104248, 2014, PMID 25100038** — *„A dynamic selection method for reference electrode in SSVEP-based BCI"*. Cytat: *„In the past, with SSVEP-based BCI, often the potential at **'Cz'**, the average potential at all electrodes or the average mastoid potential, **were statically selected as the reference**."* Czyli **Cz jest w tej dziedzinie standardowym wyborem elektrody odniesienia**. Regresja sygnału potylicznego względem Cz jest operacyjnie bliska zmianie odniesienia z małżowiny na Cz.
3. `[fakt, pomiar własny, sekcja 5]` Gdy montaż jest różnicowy wewnątrz potylicy — czyli składowa wspólna jest usunięta sprzętowo — **regresja względem Cz przestaje pomagać i zaczyna szkodzić** (−0,9 pp). Gdyby Cz modelował mięsień, jego wartość nie zależałaby od tego, czy montaż jest różnicowy.

`[wniosek, trzy przesłanki]` Zysk +9 pp Kołodzieja to w przeważającej części **efekt referencyjny**, a nie kompensacja artefaktu mięśniowego.

**Uwaga, żeby nie przesadzić z korektą** (reguła operacyjna z `PRZEKAZANIE.md` §5): praca Kołodzieja **nie jest błędna**. Autorzy nigdzie nie twierdzą, że zysk pochodzi od szczęki — piszą, że Cz był w optymalnym zestawie u 12/12 osób i nazywają go „dominant role". **Błąd był po naszej stronie**: w `12_AUDYT.md` §1.3 zapisałem „które kanały pomocnicze działały najlepiej: **Cz i szczęka**", zrównując je, a potem cała reszta dokumentacji przeniosła z tego zdania samą szczękę. To jest korekta K-051.

---

## 4. Niespójność wewnętrzna w pracy — zapisuję, bo ją znalazłem

`[fakt]` Tekst pracy podaje: *„Cz in 12/12 participants, Fp1 in 6/12, HEOG in 6/12, jaw in 4/12, and cheek in 4/12"*. **Tabela 8 tej samej pracy daje inne liczby:**

| Kanał | Z tekstu | Policzone z Tabeli 8 |
|---|---|---|
| Cz | 12/12 | **12/12** ✔ |
| Fp1 | 6/12 | **4/12** (S05, S08, S09, S12) |
| HEOG | 6/12 | **5/12** (S01, S03, S09, S10, S12) |
| szczęka | 4/12 | **3/12** (S03, S05, S10) |
| policzek | 4/12 | **3/12** (S01, S02, S11) |

**Kierunek wniosku się nie zmienia** — Cz i tak dominuje, a kanały mięśniowe i tak są rzadkie. Zapisuję to jako rzecz zauważoną przy czytaniu, nie jako zarzut: to jest drobna niespójność redakcyjna, nie błąd wyniku. **Ale jeżeli kiedykolwiek zacytujemy „szczęka w 4/12", trzeba cytować za tekstem i wiedzieć, że tabela mówi 3/12.**

---

## 5. Wynik drugi — koszt zwartego modułu, i to jest cios w formę

To jest pomiar, którego nikt nie zamawiał, a który przesądza o konstrukcji.

**Pytanie:** moduł zwarty na potylicy nie ma dokąd wyprowadzić elektrody odniesienia — z decyzji 2 (`DECYZJE.md`, K-036) wynika brak łuku, brak zausznika, brak drugiego miejsca elektrod. **Odniesienie musi więc leżeć wewnątrz modułu**, czyli pomiar jest różnicowy między dwiema elektrodami nad korą wzrokową. Ile to kosztuje?

FBCCA, te same dane, te same okna:

| Montaż | Dokładność | Wobec 3 kanałów z odległą referencją |
|---|---|---|
| **O1+O2+Oz, odniesienie na małżowinie (jak w pracy)** | **73,3 ± 19,8%** | — |
| Oz sam, odniesienie na małżowinie | 60,8 ± 21,5% | −12,5 pp |
| O2 − Oz (~3,5 cm) | 55,0 ± 19,0% | **−18,3 pp** |
| O1 − O2 (~7 cm) | 54,2 ± 16,6% | **−19,1 pp** |
| Oz − (O1+O2)/2 (laplasjan) | 51,1 ± 17,1% | **−22,2 pp** |
| O1 − Oz (~3,5 cm) | 48,8 ± 14,0% | **−24,5 pp** |
| trzy pochodne dwubiegunowe razem | 64,0 ± 18,5% | **−9,3 pp** |

Poziom losowy: 33,3%.

`[wniosek]` **Każde różnicowanie zamknięte wewnątrz obszaru potylicznego niszczy sygnał, a nie tylko zakłócenie.** Mechanizm jest oczywisty po fakcie i jest fizyką, nie techniką: **SSVEP jest polem rozległym i gładkim nad potylicą**, więc dwie elektrody odległe o kilka centymetrów widzą prawie ten sam potencjał wywołany. Odejmowanie kasuje go razem z artefaktem.

**To bezpośrednio unieważnia jedno z założeń zapisanych w `13_PODNIESIENIE_SZANS.md` sekcja 5** („gęste próbkowanie małego obszaru zastępuje rzadkie próbkowanie dużego" — pytanie zostawione jako druga kontrybucja projektu). Odpowiedź częściowa już jest i brzmi **nie**, przy tej geometrii i tym zbiorze.

**Czego ten pomiar NIE mówi, i to jest istotne:** nie mówi, ile wynosi koszt przy odniesieniu wyprowadzonym **poza obszar aktywny, ale nadal blisko** — na wyrostek sutkowaty za uchem, na kark poniżej guzowatości potylicznej, na płatek ucha. W tym zbiorze nie ma takiego kanału. **To jest luka, którą może zamknąć wyłącznie pomiar na własnym sprzęcie** — i dlatego staje się osią projektu (sekcja 7).

---

### 5.1 Czy dłuższe okno decyzyjne odkupuje stratę zwartego modułu — częściowo

Zapisy w zbiorze są ciągłe (okna sąsiadują bez przerw, sprawdzone: `diff(idx_starts) = 256`), więc dało się je posklejać i policzyć dokładność dla okien dłuższych niż sekunda. FBCCA, trzy cele, ITR liczone wzorem Wolpawa dla `t` = długość okna:

| Okno | Odniesienie odległe | ITR | Montaż różnicowy w module | ITR | Strata |
|---|---|---|---|---|---|
| 0,5 s | 57,8% | 21,7 | 49,5% | 9,6 | −8,3 pp |
| **1,0 s** | 73,3% | **28,9** | 64,0% | **17,0** | −9,3 pp |
| 2,0 s | 82,8% | 22,6 | 74,4% | 15,2 | −8,5 pp |
| 3,0 s | 86,9% | 17,9 | 80,1% | 13,3 | −6,8 pp |
| 4,0 s | 85,9% | 12,8 | 80,4% | 10,1 | −5,5 pp |
| 5,0 s | 86,9% | 10,7 | 82,6% | 8,9 | −4,2 pp |

**Trzy rzeczy z tej tabeli:**

1. `[fakt]` **ITR ma maksimum przy oknie 1 s** i wynosi 28,9 bit/min. Autorzy podają dla SVM 27,5 bit/min przy oknie 1 s — **zgodność niezależnym torem**, kolejne potwierdzenie, że odtwarzam ich pomiar.
2. `[fakt]` **Strata modułu zwartego maleje z długością okna**: 9,3 pp przy 1 s, 4,2 pp przy 5 s. Dłuższe patrzenie częściowo odkupuje gorszy montaż — to jest sensowne, bo montaż różnicowy obniża SNR, a SNR nadrabia się czasem uśredniania.
3. `[fakt]` **Ale w ITR nie odkupuje nigdy.** W optimum każdego z montaży: 28,9 wobec 17,0 bit/min. **Moduł zwarty kosztuje 41% szczytowej przepustowości**, a wydłużanie okna obniża ITR obu montaży, więc nie jest drogą wyjścia.

`[wniosek]` **Liczba „41% szczytowego ITR" jest lepszym sformułowaniem kosztu formy niż „9 pp dokładności"** — bo dokładność zależy od okna, a szczytowe ITR jest własnością montażu. Do materiałów zgłoszeniowych idzie ta liczba, z podaniem obu okien, w których jest mierzona.


## 6. Wynik trzeci — w montażu różnicowym kompensacja nie ma czego kompensować

Test bezpośredni hipotezy, która wydawała się ratować oś projektu: „skoro moduł zwarty jest różnicowy, to może właśnie tam kanał mięśniowy zacznie się liczyć".

Kompensacja regresyjna zastosowana **przed** wyznaczeniem różnic, potem FBCCA:

| Kanały pomocnicze | Odniesienie na małżowinie | **Montaż różnicowy w module** |
|---|---|---|
| brak | 73,3% | 64,0% |
| Cz | 78,0% (**+4,6**) | 63,1% (**−0,9**) |
| szczęka | 73,5% (+0,1) | 63,3% (**−0,8**) |
| kark | 73,3% (0,0) | 61,9% (**−2,1**) |
| kark+policzek+szczęka | 73,2% (−0,1) | 62,8% (**−1,3**) |
| wszystkie sześć | 77,4% (+4,1) | 63,1% (**−1,0**) |

`[fakt]` **Hipoteza obalona.** W montażu różnicowym żaden kanał pomocniczy nie pomaga; wszystkie szkodzą. Interpretacja `[wniosek]`: różnicowanie i regresja usuwają **to samo** — składową wspólną. Po różnicowaniu nie ma już czego odejmować, a regresja zaczyna zjadać sygnał użyteczny.

**To zamyka oś projektu w wersji z `PRZEKAZANIE.md`.** Nie „osłabia" — zamyka. Kompensacja artefaktu mięśniowego, analogowa czy cyfrowa, nie ma zmierzonego zapasu do odzyskania w konfiguracji, którą wybraliśmy.

---

---

## 6A. Test kontrolny na żądanie użytkownika — czy szczęka daje dość, żeby oprzeć na niej oś

**Zarzut użytkownika, 16 VIII 2026:** *„sprawdź, czy odejmowanie »szumu« szczęki daje rzeczywiście tak dużo, aby opierać na tym wręcz jedną z osi projektu."*

**Zarzut trafia w realną słabość sekcji 2.** Uśredniałem tam po **wszystkich** oknach, w tym po oknach bez artefaktu. Artefakty u Kołodzieja były epizodami 1–2 s w losowych momentach, więc kanał szczękowy z definicji może działać tylko w części okien. Gdyby skażone było 20% okien, prawdziwy efekt zostałby w mojej tabeli **rozcieńczony pięciokrotnie** i wyglądałby na zero, nie będąc zerem.

### 6A.1 Czy w danych w ogóle jest co usuwać — tak

`[fakt]` Moc EMG szczęki (pasmo 20–100 Hz) w oknie jednosekundowym, stosunek 95. centyla do mediany: **mediana po zapisach 4,8×, zakres 1,6–29,8×**. Artefakt jest obecny i silnie epizodyczny. **Test poniżej nie jest testem pustym.**

### 6A.2 Dokładność w podziale na kwintyle mocy EMG szczęki w oknie

| Wariant | Q1 (najczystsze) | Q2 | Q3 | Q4 | **Q5 (najbardziej skażone)** |
|---|---|---|---|---|---|
| O-only | 76,9 | 75,5 | 77,0 | 74,2 | 71,5 |
| **zysk samej szczęki** | **+0,5** | **−1,2** | **+0,3** | **−0,2** | **+0,6** |
| **zysk Cz** | +3,4 | +2,5 | +2,6 | **+6,5** | **+6,9** |
| szczęka ponad Cz | −0,2 | +0,6 | +0,9 | 0,0 | +0,2 |

**To jest wynik rozstrzygający i mówi więcej, niż mówiła sekcja 2:**
- **zysk szczęki nie rośnie z poziomem artefaktu.** Gdyby kanał szczękowy modelował artefakt, Q5 musiałby odstawać. Nie odstaje
- **zysk Cz rośnie z poziomem artefaktu**, z +2,5 pp na +6,9 pp. **Czyli to Cz obsługuje skażenie mięśniowe** — co jest spójne z jego rolą: EMG szczęki rzutuje się na potylicę jako składowa w dużej mierze wspólna, a nie jako sygnał lokalny, który trzeba zmierzyć osobną elektrodą

### 6A.3 Najostrzejsza możliwa wersja testu — górny decyl skażenia

324 najbardziej skażone okna z 3240.

| Wariant | Dokładność | Zysk | SNR SSVEP | Zysk SNR |
|---|---|---|---|---|
| O-only | 71,6% | — | 2,46 dB | — |
| **O + szczęka** | **72,2%** | **+0,6 pp** | 2,59 dB | **+0,13 dB** |
| O + Cz | 77,8% | +6,2 pp | 4,01 dB | +1,54 dB |
| O + Cz + szczęka | 78,4% | +6,8 pp | 4,04 dB | +1,58 dB |

**Per osoba, w tym decylu, zysk szczęki ponad Cz:** u **dziesięciu z dwunastu osób dokładnie 0,0 pp**, u dwóch +5,6 pp. Średnia +0,93 ± 2,16 pp, **test t wobec zera: t = 1,48, p = 0,166 — nieistotne**.

`[luka]` **Uczciwie o rozdzielczości tego testu per osoba:** decyl to 18 okien na osobę, więc najmniejsza wykrywalna zmiana wynosi dokładnie 5,6 pp (jedno okno). Te dwa „+5,6 pp" to **po jednym przerzuconym oknie** i nie należy ich czytać jako efektu. Test zbiorczy na 324 oknach jest wiarygodny, rozbicie na osoby jest tylko poglądowe.

**Kontrola wewnętrzna, mocna:** trzej badani, u których praca Kołodzieja wybrała szczękę do optymalnego zestawu (**S03, S05, S10**), mają w tym teście zysk **dokładnie 0,0 pp**. `[wniosek]` Wybór szczęki przez ich procedurę doboru regresorów był **szumem selekcji** — spodziewany, skoro wybierali najlepszy z 63 zestawów na tych samych danych, na których mierzyli wynik.

### 6A.4 Czy winna jest metoda — sprawdzone, nie jest

Zanim zamknę tę oś, sprawdziłem wersję, w której **narzędzie jest inne**, bo regresja liniowa może być po prostu zła: EMG sprzęga się przez **obwiednię amplitudy**, nie liniowo. Kołodziej testował wyłącznie regresję liniową.

| Regresory | Wszystkie okna | Górny decyl |
|---|---|---|
| brak | 75,0% | 71,6% |
| szczęka, liniowo | 75,0% | 72,2% |
| szczęka, kwadrat | 75,1% | 71,3% |
| **szczęka, obwiednia Hilberta** | 74,3% | 70,7% |
| szczęka: liniowo + obwiednia | 73,8% | 71,3% |
| trzy mięśniowe, liniowo | 74,8% | 70,7% |
| **trzy mięśniowe + trzy obwiednie** | **71,5%** | **63,6%** |
| Cz | 79,4% | 77,8% |
| Cz + szczęka | 79,7% | 78,4% |

`[fakt]` **Kompensacja nieliniowa nie pomaga — szkodzi.** Najlepszy wariant szczękowy daje +0,1 pp na całości i +0,6 pp na górnym decylu, czyli **tyle samo co zwykła regresja liniowa**.

`[wniosek]` **Mechanizm tej szkody jest istotny dla projektu i wart zapamiętania:** okno ma 256 próbek, a każdy dodany regresor usuwa z sygnału jeden wymiar. Przy dziewięciu regresorach traci się 8 pp na całości i 8 pp na decylu. **Każdy kanał pomocniczy ma koszt, który jego korzyść musi najpierw pokryć.** Kanał szczękowy tego kosztu nie pokrywa.

### 6A.5 Odpowiedź na zarzut

**Nie. Kanał szczękowy nie daje dość, żeby oprzeć na nim oś projektu — i teraz jest to sprawdzone pięcioma niezależnymi sposobami**, a nie jednym uśrednieniem:

| Sposób sprawdzenia | Zysk szczęki |
|---|---|
| FBCCA, wszystkie okna | +0,2 pp |
| SVM/LOSO, wszystkie okna | +0,3 pp |
| **tylko okna najbardziej skażone (górny decyl)** | **+0,6 pp** |
| miara ciągła — SNR SSVEP, górny decyl | +0,13 dB |
| regresory nieliniowe i obwiedniowe | +0,1 do +0,6 pp |
| ponad Cz, per osoba, test t | +0,93 ± 2,16 pp, **p = 0,166** |

**Sufit dla tej osi to około 0,6 pp, przy najkorzystniejszym możliwym doborze warunków.** Twierdzenie projektu potrzebuje efektu, który przeżyje rozrzut międzyosobniczy σ ≈ 8 pp. **Ta oś zostaje zamknięta jako oś i schodzi do kontrybucji warunkowej.**

### 6A.6 Co z tego wynika dla sprzętu — jedna konkretna zmiana

**Elektroda szczękowa wychodzi z projektu.** Nie ma pomiaru, który by ją uzasadniał, a wymagała elektrody na twarzy, czyli poza modułem i wbrew wymaganiu „niewidoczne".

**Zostaje jedno wejście mięśniowe, ale przeniesione na kark** — bo tam, i tylko tam, pozostaje pytanie nierozstrzygalne na tych danych: **gdy sama elektroda odniesienia leży nad mięśniem karku, wnosi EMG do każdego kanału jednocześnie.** Kołodziej miał odniesienie na płatku ucha, więc ta sytuacja u niego nie wystąpiła i jego dane nie mogą jej rozstrzygnąć `[luka]`.

**Netto: sprzęt się upraszcza, a nie komplikuje** — jedna elektroda mniej, i to ta, która leżała najbardziej niewygodnie.

---

## 6B. TRCA — sprawdzone i okazało się niewykonalne na tym zbiorze

TRCA (task-related component analysis) to metoda, która w literaturze daje najwyższe ITR dla SSVEP, i jedyna z listy, której w §2 nie przetestowałem. Sprawdziłem ją, żeby ustalić, czy strata 9,3–24,5 pp z §5 nie jest artefaktem użycia FBCCA.

**Wynik surowy:** wszystkie montaże 32,0–34,1%, przy poziomie losowym 33,3%. **Czyli TRCA nie działa w ogóle**, a nie „nie widzi różnicy między montażami".

### Dlaczego — zdiagnozowane, nie zgadnięte

TRCA buduje szablon przez uśrednianie prób, więc wymaga, żeby **faza SSVEP była powtarzalna między próbami**. Sprawdziłem ją wprost: spójność fazy składowej o częstotliwości bodźca na elektrodzie Oz.

| Zapis | Spójność fazy R | Amplituda po uśrednieniu 60 okien / amplituda pojedynczego |
|---|---|---|
| S01, 7 Hz | 0,108 | 0,13 |
| S01, 8 Hz | 0,056 | 0,08 |
| S01, 9 Hz | 0,075 | 0,07 |
| S02, 7 Hz | 0,027 | 0,02 |
| S02, 8 Hz | 0,011 | 0,01 |
| S02, 9 Hz | 0,053 | 0,07 |

`[fakt]` **R ≈ 0, a uśrednienie 60 okien obniża amplitudę w stosunku 1/√60 ≈ 0,13** — czyli dokładnie tak, jak zachowuje się **szum o losowej fazie**. Faza SSVEP nie jest zsynchronizowana z granicami okien.

**Przyczyna** `[wniosek]`: bodziec LED był swobodnie bieżący i nie był zsynchronizowany z rejestratorem, a okna to arbitralne cięcia ciągłego nagrania. Autorzy używali cech **amplitudowych FFT**, które fazy nie potrzebują, więc ich to nie ograniczało — i dlatego ta wada zbioru nie ujawniła się w ich pracy.

### Dwie konsekwencje, obie istotne

1. `[luka]` **Strata montażu zwartego pozostaje niesprawdzona metodami szablonowymi.** Liczby 9,3–24,5 pp obowiązują dla FBCCA, CCA i cech FFT — czyli dla metod bez uczenia albo bez fazy. **Czy przeżywają pod TRCA, rozstrzygnie dopiero własny pomiar.** Zapisuję to jako otwarte i wpisuję do ryzyka R4.

2. **Twardy wymóg konstrukcyjny dla własnego stanowiska, wyprowadzony z tej porażki:** **rejestracja musi zapisywać moment zapłonu bodźca**, a okna muszą być cięte względem niego, nie względem początku pliku. Bez tego TRCA — metoda o najwyższym ITR w dziedzinie — jest **niedostępna**, i to nie da się naprawić po fakcie żadną analizą.

**Kanał fotodiody, który wpisałem do projektu jako kontrolę częstotliwości bodźca, awansuje z „dobrze mieć" na „warunek konieczny".** To jest najtańsza pozycja w całym zestawieniu materiałowym i właśnie okazała się jedną z najważniejszych.

## 7. Komplet trzech punktów wymagany przez handbook §2.2

Handbook zakazuje pisania „nie da się" bez podania trzech rzeczy naraz. Podaję.

### 7.1 Który parametr się nie spina, liczbowo

**Marginalny zysk dedykowanego kanału mięśniowego ponad to, co daje samo odniesienie:**
- montaż z odległą referencją: **+0,2 pp (FBCCA), +0,3 pp (SVM)**
- montaż zwarty, różnicowy: **−0,8 pp (FBCCA)**
- **nawet w oknach najbardziej skażonych artefaktem, przy regresorach nieliniowych: +0,6 pp** (sekcja 6A) — to jest sufit tej osi

Rozrzut międzyosobniczy w tych samych danych: **σ ≈ 8 pp**. Żeby wykryć efekt +0,4 pp przy σ = 8 pp z mocą 80% i α = 0,05, potrzeba `[wniosek, wzór na próbę sparowaną]` rzędu **3200 osób**. Projekt dysponuje **jedną** (autor) do maja 2027 i realistycznie **kilkunastoma** po powołaniu komisji IRB.

**To jest ta liczba, która się nie spina, i nie spina się o trzy rzędy wielkości.**

### 7.2 Wersja projektu, w której ten parametr jest poza pętlą

Przenieść twierdzenie z **wielkości, która okazała się mała** (marginalny zysk kanału mięśniowego) na **wielkość, która okazała się duża** (koszt zwarcia montażu: 9–24 pp, sekcja 5).

> **Nowa oś: ile przepustowości SSVEP przeżywa zejście z montażu z odległą elektrodą odniesienia do montażu mieszczącego się w module o zadanym gabarycie — i jak daleko od aktywnej okolicy potylicznej musi leżeć elektroda odniesienia, żeby różnicowanie nie kasowało potencjału wywołanego razem z zakłóceniem.**

Zmienna niezależna: **odległość i położenie elektrody odniesienia**, od ~2 cm (wewnątrz modułu) do ~10 cm (wyrostek sutkowaty, płatek ucha, kark poniżej inionu).
Zmienna zależna: **dokładność i ITR**, tym samym torem analogowym, tą samą osobą, tym samym paradygmatem.

Efekt do wykrycia: **9–24 pp**, czyli 20–60× większy niż ten, który przed chwilą odpadł. Przy σ = 8 pp i pomiarze wewnątrzosobniczym powtarzanym **to jest wykrywalne na jednej osobie**, co jest zgodne ze zwolnieniem ISEF dla badania na sobie.

### 7.3 Pomiar, który przeżywa tę zmianę

**Przeżywa w komplecie, bo to jest ten sam pomiar.** Stanowisko z decyzji C2 mierzy dokładność i ITR wg wzoru Wolpawa — zmienia się tylko to, co jest na osi poziomej wykresu: zamiast „kompensacja włączona / wyłączona" jest „położenie elektrody odniesienia". Płytka i tak miała obsłużyć kilka rozstawów (`DECYZJE.md`, pozycja 3). **Sprzęt nie zmienia się ani o jeden element.**

Dodatkowo przeżywa **zewnętrzny punkt odniesienia**, i jest mocniejszy niż poprzedni: nie cudza liczba z abstraktu, tylko **własna reanaliza cudzych surowych danych**, odtworzona co do trzeciego miejsca po przecinku, na zbiorze CC-BY, z kodem w repozytorium.

---

## 8. Czego nie wolno zrobić z tym wynikiem

1. **Nie wolno napisać, że praca Kołodzieja jest błędna.** Nie jest. Ich wynik odtworzyłem z dokładnością do 1 pp. Błędna była **nasza interpretacja ich wyniku**.
2. **Nie wolno oprzeć twierdzenia na tym, że „Cz to tylko referencja".** To jest `[wniosek]` z trzech przesłanek, nie `[fakt]`. Do materiałów zgłoszeniowych wchodzi w formie warunkowej albo wcale.
3. **Nie wolno wyrzucić kanału mięśniowego ze sprzętu.** Kosztuje jedno wejście różnicowe i jedno gniazdo. Zostaje jako **kontrybucja druga, warunkowa** — mierzona przy odniesieniu wyprowadzonym na kark, gdzie elektroda odniesienia sama siedzi na mięśniu i sama wnosi EMG. To jest jedyna konfiguracja, w której kompensacja mięśniowa ma jeszcze zmierzony sens, i **w tym zbiorze nie da się jej sprawdzić** `[luka]`.
4. **Nie wolno zgłosić samej tej reanalizy jako projektu.** To jest praca na cudzych danych, bez własnego sprzętu — dokładnie ten profil, przed którym ostrzega `HANDBOOK.md` §9.4 („projekt czysto dekodujący stawia użytkownika na tym samym polu co każdy uczestnik z doświadczeniem w uczeniu maszynowym"). Reanaliza jest **uzasadnieniem** projektu i materiałem na rubrykę `Research Problem`, nie projektem.

---

## 9. Ograniczenia tej reanalizy — czytać przed cytowaniem którejkolwiek liczby

`[luka]` Wymieniam wszystko, co osłabia powyższe:

1. **Trzy minuty nagrania na osobę, dwanaście osób, trzy cele.** To jest mały zbiór. Wszystkie liczby mają szerokie przedziały ufności, których nie liczyłem formalnie.
2. **Artefakty były wywoływane celowo** (zaciskanie szczęki, grymasy, napinanie karku, 1–2 s, losowo w trakcie stymulacji). To nie jest użycie naturalne. W użyciu naturalnym artefaktu jest mniej, więc **zapas dla jakiejkolwiek kompensacji jest jeszcze mniejszy**, nie większy — kierunek wniosku się nie odwraca.
3. **Moja implementacja FBCCA nie jest ich implementacją.** Dostaję 73,3% tam, gdzie oni podają 73,9%; przy pełnej kompensacji 77,4% wobec ich 80,1%. Różnice w doborze podpasm. **Porównania wewnątrz mojej tabeli są rzetelne, porównania mojej liczby z ich liczbą — nie.**
4. **Odległości elektrod (3,5 cm, 7 cm) to przeliczenie z układu 10–20 na głowę dorosłego**, nie pomiar. Rząd wielkości, nie wartość.
5. **Nie sprawdziłem zbioru pod kątem błędów** — przyjąłem go takim, jaki jest.
6. **TRCA sprawdzone i niewykonalne na tym zbiorze** — faza SSVEP nie jest zsynchronizowana z oknami (§6B). Wszystkie liczby w tym pliku obowiązują dla metod bez fazy: FBCCA, CCA, cechy FFT. Czy przeżywają pod TRCA — `[luka]`, do rozstrzygnięcia własnym pomiarem.
7. **Jedno źródło** dla twierdzenia, że Cz jest standardową referencją w SSVEP: Wu i Su 2014. Oznaczam zgodnie z regułą — to jest jedno źródło, nie dwa.

---

## 10. Co ta reanaliza dała projektowi, netto

| | Przed | Po |
|---|---|---|
| oś projektu | kompensacja artefaktu szczękowego, analogowo | **odległość elektrody odniesienia a przepustowość w module noszalnym** |
| zewnętrzny punkt odniesienia | +9 pp z cudzego abstraktu | **własna reanaliza cudzych surowych danych, odtworzona co do 3. miejsca** |
| wielkość efektu do wykrycia | 0,2–0,4 pp | **9–24 pp** |
| liczba osób potrzebna do wykrycia | rzędu 3000 | **jedna, powtórzeniami** |
| status kanału mięśniowego | oś projektu | kontrybucja druga, warunkowa, jedno gniazdo |
| co wiadomo o formie zwartej | nic | **kosztuje 9–24 pp i wiadomo dlaczego** |

**Cena, którą płacimy, zapisana wprost, bo handbook §11 tego wymaga:** traci się twierdzenie, które ładnie się opowiadało („mierzę mięsień i odejmuję go w analogu, zanim wzmocnię"), i traci się bezpośrednie porównanie „my analogowo kontra oni cyfrowo". W zamian dostaje się pytanie, na które **nikt nie odpowiedział** (sekcja 11) i którego wielkość efektu mieści się w zasięgu jednego licealisty z jedną płytką.

**Ta zamiana jest korzystna i nie jest zejściem o poziom w ambicji.** Zejściem byłoby utrzymanie starej osi i raportowanie +0,3 pp jako wyniku.

---

## 11. Prior art dla nowej osi — sprawdzony, zanim cokolwiek napisałem

Reguła z `PRZEKAZANIE.md` §5.1: **każda zmiana osi wymaga powtórzenia przeszukania.** Powtórzone, PubMed E-utilities, 16 VIII 2026:

| Zapytanie | Trafień |
|---|---|
| `SSVEP AND bipolar AND ("inter-electrode distance" OR "electrode spacing" OR "interelectrode")` | **0** |
| `SSVEP AND "single channel" AND (bipolar OR differential) AND occipital` | **0** |
| `("reference electrode" AND placement) AND EEG AND (wearable OR miniature OR compact)` | **0** |
| `SSVEP AND wearable AND ("electrode configuration" OR "electrode placement") AND (accuracy OR ITR)` | **0** |
| `SSVEP AND ("reference-free" OR "self-referenced" OR "local reference")` | **0** |
| `EEG AND ("electrode spacing" OR "inter-electrode distance") AND (SSVEP OR "visual evoked")` | 1 — ultragęste EEG, dekodowanie obrazów, nie to |
| `SSVEP AND ("reference electrode" OR "reference placement" OR "montage")` | 12, przejrzane tytuły |

**Najbliższa praca, jedyna trafiająca w temat:** Wu i Su 2014 (wyżej). Wybierają **algorytmicznie** najlepszą elektrodę odniesienia **z pełnego czepka**, osobno dla każdej częstotliwości. Nie pytają, jak blisko może leżeć odniesienie; nie budują sprzętu; nie dotykają gabarytu.

### 11.1 Crossref i arXiv — dołożone tego samego dnia, żeby nie powtórzyć wzorca błędu nr 1

`[fakt]` **Crossref API**, pięć zapytań bibliograficznych o odległość i położenie elektrody odniesienia w SSVEP i w noszalnym EEG. Uwaga metodyczna: Crossref dopasowuje rozmyto, więc **liczby „total" są bez znaczenia** — liczy się ranking. W czołówce każdego z pięciu zapytań **nie ma pracy o odległości elektrody odniesienia w SSVEP**. Powtórnie wychodzi ta sama pozycja co w PubMed (Wu i Su 2014). Najbliższe tematycznie i nienachodzące:
- *Quantitative Analysis of the Effect of Reference Electrode Position and Active Recording Electrode Size…*, 1992 — dotyczy **elektromiografii i przewodnictwa nerwowego**, nie EEG ani SSVEP
- *Multi-Command Real-Time Brain Machine Interface Using SSVEP: Feasibility Study for Occipital and Forehead Sensor* — porównuje **położenie elektrody czynnej**, nie odniesienia

`[fakt]` **arXiv API.** Uwaga techniczna do zapisania, bo kosztowała mnie jedną fałszywą odpowiedź: **składnia `all:"fraza w cudzysłowie"` zwraca zero trafień na każde zapytanie** i wygląda jak brak prior art. Kontrola `all:SSVEP` daje **96 prac w całym arXiv** i to jest prawdziwy rozmiar zbioru. Po poprawieniu składni:

| Zapytanie | Trafień |
|---|---|
| `all:SSVEP` (kontrola) | 96 |
| `all:SSVEP AND all:reference` | 6, żadna o elektrodzie odniesienia |
| `abs:SSVEP AND abs:wearable` | 5 |

**Jedna pozycja warta zapisania, znaleziona przy okazji:** *„In-Ear Electrode EEG for Practical SSVEP BCI"*, **arXiv 2509.15449, 18 IX 2025** — elektroda douszna wobec potylicznej, cztery częstotliwości, **pięciu badanych**, wniosek: wykonalne. To jest preprint bez recenzji na bardzo małej próbie, dotyczy **położenia elektrody czynnej**, nie odniesienia, i **nie zajmuje nowej osi**. Zapisuję, bo dotyczy formy urządzenia i bo pojawił się po zamknięciu etapu 1.

### 11.2 Werdykt

`[wniosek]` Nowa oś **nie jest zajęta w PubMed, Crossref ani arXiv**. Zgodnie z zamknięciem `12_AUDYT.md` §14 to nie jest dowód nieistnienia — to opis tego, gdzie szukałem. **Pozostaje nieprzeszukana baza patentów dla nowej osi** `[luka]`; to jest jedyna otwarta pozycja i wpisana jest jako R8 w `17_RYZYKA.md`.

---

## 12. Jak odtworzyć te liczby

```bash
git clone https://github.com/kolodzima/EEG_artefact_SSVEP_EMG_EOG.git ds
for i in $(seq -w 1 12); do unzip -q ds/S$i.zip -d un; done
pip install numpy scipy scikit-learn h5py
python3 analiza/analiza.py     # walidacja: Tabela 9 co do 3. miejsca
python3 analiza/svm_test.py    # ablacja SVM/FFT, LOSO
python3 analiza/spatial.py     # montaże przestrzenne
python3 analiza/rozstaw.py     # rozstaw i pochodne dwubiegunowe
python3 analiza/hipoteza.py    # kanały pomocnicze w montażu różnicowym
```

Ścieżkę `ROOT` w `analiza/analiza.py` ustawić na katalog `un`.
