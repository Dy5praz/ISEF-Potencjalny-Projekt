# 11 — Ewolucja projektu. Co, kiedy i dlaczego się zmieniło

**Stan na 21 sierpnia 2026.**

**Po co ten plik.** Historia tego projektu była dotąd rozrzucona po kilkunastu plikach, w których poprawki grały większą rolę niż to, co obowiązuje. Tutaj jest cała, w jednym miejscu, po kolei — **żeby główne pliki mogły opisywać wyłącznie stan bieżący.**

**Jak czytać.** To jest opowieść, nie rejestr. Rejestr błędów co do jednego wpisu jest w `KOREKTY.md` (K-001…K-101). Tutaj chodzi o to, **jakie badanie co obaliło i jaką decyzję podjął autor** — bo ta historia jest sama w sobie materiałem na rozmowę z jurorem. `[fakt]` Arkusz inżynierski ISEF punktuje **„exploration of alternatives"** w rubryce `Design and Methodology` (15 pkt), a Explory §7 pkt 2d daje **10 pkt na 40** za znajomość dotychczasowych badań. **Odrzucone warianty są materiałem punktowanym, nie wstydem.**

---

## Mapa w jednym akapicie

Projekt zaczął się jako **dron**, potem był **ortezą kolanową**, potem **interfejsem neuralnym z czterema twierdzeniami naraz**. Trzy z tych czterech twierdzeń zabiła literatura w ciągu jednego dnia. Czwarte — kompensacja artefaktu szczękowego — zabiła **reanaliza cudzych danych, którą wykonałem sam** i która pokazała, że efekt, na którym wszystko stało, wynosi 0,2 punktu procentowego zamiast dziewięciu. Z gruzów została **jedna zmienna, której nikt nie zmierzył: gdzie postawić elektrodę odniesienia**. Po drodze projekt na jeden dzień przestał być interfejsem (było **łożysko magnetyczne**), po czym wrócił decyzją autora. Ostatnie pięć dni to audyt, który dwa razy ogłosił twierdzenie za martwe i dwa razy się z tego wycofał po przeczytaniu pełnych tekstów zamiast abstraktów.

---

# CZĘŚĆ I — ZANIM POWSTAŁ INTERFEJS

## 1. Dron — pierwszy kierunek, porzucony przed dokumentacją

**Co to było.** `[fakt]` ConOps zachował się w `archiwum/dron_ConOps.md`.

**Dlaczego padł.** Prior art sprawdzony **po** zbudowaniu strategii, nie przed. Okazało się, że wszystkie elementy istnieją osobno, a twierdzenie brzmiało *„integracja i benchmark"* — co **nie jest twierdzeniem naukowym**. Sam ConOps to przyznawał.

**Co po sobie zostawił.** Punkt odniesienia dla budżetu: **~15 000 zł jako „rząd wielkości wyobrażalny"** — wyraźnie nie jako limit. Oraz niewykorzystaną decyzję zakupową o drukarce.

## 2. Orteza kolanowa — drugi kierunek

**Dlaczego padła.** Po sprawdzeniu stanu techniki z twierdzenia zostawało **wyłącznie „taniej"**, co nie jest twierdzeniem naukowym. Późniejsze sprawdzenie (K-073) pokazało, że **akt zgonu w handbooku dotyczył tylko połowy projektu** — teza pierwsza była zajęta, teza druga leżała w polu czynnie badanym (ICORR 2025, Sensors 2025). Kierunek został zamknięty, ale z niewłaściwym uzasadnieniem.

## 3. Wniosek metodyczny, który przetrwał oba

`[wniosek]` **Twierdzenie „taniej" i twierdzenie „zintegrowałem" nie są twierdzeniami naukowymi.** To ustalenie przeżyło wszystkie późniejsze zwroty i jest jedynym powodem, dla którego twierdzenie bieżące ma postać pomiarową.

---

# CZĘŚĆ II — INTERFEJS, WERSJA PIERWSZA: CZTERY TWIERDZENIA

Do 15 sierpnia 2026 projekt miał **cztery kandydujące twierdzenia naraz**. Audyt adwersaryjny (`archiwum/12_AUDYT.md`) zabił trzy w jeden dzień.

## 4. „Tani interfejs SSVEP o wysokiej przepustowości" — MARTWE

**Co zabiło.** `[fakt]` **Teversham, Wong, Hsieh, Rapeaux, Troiani, Savolainen, Zhang, Maslik, Constandinou** (Imperial College London), *„Development of an Ultra Low-Cost SSVEP-based BCI Device for Real-Time On-Device Decoding"*, **EMBC 2022, PMID 36086083**.

**Dwadzieścia funtów. 95,56% dokładności. 102 bit/min. Na ESP32.** To jest **więcej** niż 92,35 bit/min z pracy, którą ustawiłem jako poprzeczkę, i za ułamek kosztu.

**Co się okazało po przeczytaniu pełnego tekstu, trzy miesiące później** (K-094): to jest **urządzenie edukacyjno-popularyzatorskie do masowego rozdawania**, a nie przyrząd pomiarowy. Cytat z ich abstraktu: *„a financially and operationally accessible device that can be deployed on a **mass scale to facilitate education and public engagement**"*. Nie mierzy niczego w funkcji czegokolwiek i nie podaje charakterystyki toru.

**Co z tego zostało dla projektu — i to jest zysk, nie strata.** `[wniosek]` **Ryzyko techniczne projektu jest przez tę pracę obniżone, a nie podniesione.** Skoro 100 bit/min osiągnięto na sprzęcie za £20, to cel przepustowościowy **nie wymaga instytutu**. Wymaga poprawnej implementacji filter-bank CCA i przyzwoitego kontaktu elektrod.

## 5. „Mały suchy czujnik przez włosy na potylicy" — MARTWE, na najwyższym poziomie

**Co zabiło.** `[fakt]` **Kim H., Kim J.H., Lee Y.J. i in.** (Georgia Tech, Yonsei, Hanyang), *„Motion artifact-controlled micro-brain sensors between hair follicles"*, **PNAS 122(15):e2419304122, 15 IV 2025, PMID 40193612**. Mikroczujniki wsuwane między mieszki włosowe, **najniższa opublikowana gęstość impedancji kontaktu (0,03 kΩ·cm⁻²)**, noszenie do 12 h, 96,4% dokładności podczas biegu. **Plus zgłoszenie patentowe w toku.**

**Co się okazało po przeczytaniu pełnego tekstu** (K-094): montaż **O1, O2 i Pz, z Pz jako elektrodą odniesienia** — nieruchomą. Tor **kupiony**, własna jest wyłącznie elektroda. **Dwa bodźce.** ITR nie podane.

**Co z tego zostało:**
- **elektroda jest problemem rozwiązanym i zamkniętym patentowo.** Konkurowanie z formowaniem replikacyjnym UV i cięciem laserem femtosekundowym przy budżecie 8 000 zł nie jest możliwe **i nie jest potrzebne**. Elektrodę robi się dobrze i **nie sprzedaje jako wynalazku**
- **Pz działa jako odniesienie** — punkt do widełek
- **„96,4%" przy dwóch celach to sufit ~17 bit/min**, czyli mniej niż para POz−Oz. Najlepszy istniejący przykład na to, dlaczego **nigdy nie podaje się dokładności bez liczby celów**

## 6. „Kanał pomocniczy do usuwania artefaktów mięśniowych" — ZROBIONE OSIEM MIESIĘCY WCZEŚNIEJ, W WARSZAWIE

**Co zabiło.** `[fakt]` **Kołodziej M., Majkowski A., Wiszniewski P.** (Wydział Elektryczny Politechniki Warszawskiej), *„Improved SSVEP Classification Through EEG Artifact Reduction Using Auxiliary Sensors"*, **Sensors 26(3):917, 31 I 2026, PMID 41682433**.

Elektrody czynne O1, O2, Oz — nasze umiejscowienie. Kanały pomocnicze Cz, Fp1, HEOG oraz **mięśniowe: kark, policzek, szczęka**. Dwunastu badanych. Zysk: **+9,1 pp** dokładności.

**To była najgroźniejsza z trzech**, bo trafiała w samą oś projektu i pochodziła od zespołu z kompetencjami sprzętowymi, w dodatku 350 km stąd.

## 7. Co zostało po pierwszym audycie

Projektowi została **jedna** rzecz: luka, którą **autorzy pracy warszawskiej wypisali sami** w sekcji prac przyszłych:

> „identification of a minimal electrode set (…) provides a foundation for designing **low-channel, wearable SSVEP–BCI systems in which artifact reduction is addressed already at the signal acquisition stage**."

**To zdanie opisuje projekt użytkownika cudzą ręką** i przez cztery miesiące było jego głównym uzasadnieniem.

---

# CZĘŚĆ III — DZIEŃ, W KTÓRYM WŁASNA ANALIZA ZABIŁA WŁASNĄ OŚ

## 8. Zbiór danych był publiczny i podany w tej samej pracy

**16 sierpnia 2026.** `[fakt]` Pełny tekst pracy warszawskiej zawiera zdanie przeoczone przy pierwszym czytaniu:

> „The recorded EEG signals are **publicly available** in the database (…) github.com/kolodzima/EEG_artefact_SSVEP_EMG_EOG"

**Zbiór, na którym stała cała oś projektu, był do pobrania jednym poleceniem.** Przeoczenie zostało zapisane jako **K-090** z regułą: znacznik „pełny tekst odczytany" wolno postawić tylko po przeczytaniu **sekcji o dostępności danych**.

## 9. Reanaliza — i wynik, którego nikt nie zamawiał

Zbiór pobrany, pipeline autorów odtworzony, **tabela ich współczynników zreprodukowana co do trzeciego miejsca po przecinku**. Dopiero wtedy dało się zapytać, **skąd naprawdę pochodzi ich +9 pp**.

`[fakt, dwa niezależne klasyfikatory]`

| Kanał pomocniczy | Zysk dokładności |
|---|---|
| **Cz sam** | **+4,7 pp** (FBCCA), **+8,2 pp** (SVM) |
| **szczęka sama** | **+0,2 pp**, **+0,3 pp** |
| kark sam | 0,0 pp, **−2,8 pp** |

**Cały mierzalny zysk pochodził z Cz — czyli z elektrody na czubku głowy, pełniącej rolę odniesienia — a nie z kanału mięśniowego.**

**Skąd wziął się błąd.** W audycie zapisałem *„które kanały pomocnicze działały najlepiej: **Cz i szczęka**"*, zrównując je jednym zdaniem, **a potem cała dokumentacja przeniosła z tego zdania samą szczękę**. Autorzy nigdy nie twierdzili, że zysk pochodzi od szczęki — nazywali Cz *„dominant role"*. **Błąd był po naszej stronie.** K-089.

## 10. Zarzut użytkownika, który przyspieszył koniec tej osi

**Decyzja autora, 16 VIII, cytat:** *„sprawdź, czy odejmowanie »szumu« szczęki daje rzeczywiście tak dużo, aby opierać na tym wręcz jedną z osi projektu."*

**Zarzut trafiał w realną słabość pierwszej analizy** — uśredniała po wszystkich oknach, także tych bez artefaktu, co rozcieńczyłoby prawdziwy efekt. Sprawdzone **pięcioma niezależnymi sposobami**:

| Sposób | Zysk szczęki |
|---|---|
| FBCCA, wszystkie okna | +0,2 pp |
| SVM/LOSO | +0,3 pp |
| **tylko okna najbardziej skażone artefaktem** | **+0,6 pp** |
| SNR SSVEP, górny decyl | +0,13 dB |
| regresory nieliniowe i obwiedniowe | +0,1 do +0,6 pp |
| ponad Cz, per osoba, test t | **p = 0,166, nieistotne** |

**Sufit tej osi to +0,6 pp, przy najkorzystniejszym możliwym doborze warunków**, wobec rozrzutu międzyosobniczego σ ≈ 8 pp. Żeby wykryć taki efekt, trzeba by **rzędu 3 200 osób**. Projekt dysponuje jedną.

**Decyzja konstrukcyjna:** elektroda szczękowa wychodzi z projektu. **Sprzęt się przez to upraszcza**, a nie komplikuje.

## 11. Drugi wynik reanalizy — ten, który stworzył projekt bieżący

Przy okazji padło pytanie, którego nikt nie zadawał: **moduł zwarty nie ma dokąd wyprowadzić odniesienia. Ile to kosztuje?**

| Montaż | Dokładność |
|---|---|
| O1+O2+Oz, odniesienie na małżowinie | **73,3%** |
| trzy pochodne dwubiegunowe razem | 64,0% (**−9,3 pp**) |
| O1 − Oz (~3,5 cm) | 48,8% (**−24,5 pp**) |

**A w przepustowości: montaż zwarty kosztuje 41% szczytowego ITR.**

`[wniosek]` **Efekt do wykrycia urósł z 0,2 pp na 9–24 pp — czyli od dwudziestu do stukrotnie.** Z wielkości wymagającej trzech tysięcy osób zrobiła się wielkość wykrywalna **na jednej osobie powtórzeniami**. To jest moment, w którym powstał projekt bieżący.

## 12. Decyzje autora z 16 sierpnia

| Decyzja | Treść |
|---|---|
| **5 — oś projektu** | **wariant C:** osi nie zamykać teraz, sprzęt obsłuży obie, wybór po pierwszych własnych pomiarach. Cytat: *„Faktyczny nacisk wyjdzie wraz z pomiarami."* |
| **6 — odniesienie za uchem** | **zgoda** na wyprowadzenie odniesienia cienkim przewodem na wyrostek sutkowaty. Zakres pomiarowy rośnie z 2–4 cm na **2–10 cm** |

---

# CZĘŚĆ IV — DZIEŃ WAHANIA

## 13. Sześć projektów w jeden dzień, wszystkie odrzucone

**17 sierpnia 2026.** Kierunek interfejsowy chwilowo zamknięty. Powstało siedem propozycji: **aktywne łożysko magnetyczne z self-sensingiem** (rozpisane najgłębiej), kamera akustyczna, tomografia mionowa, obrazowanie fali milimetrowej, badanie zmęczeniowe wydruków, maszyna na cyklu termicznym, enkoder indukcyjny na PCB.

**Wszystkie padły.** Rejestr: `archiwum/29_ODRZUCONE_KIERUNKI.md`.

## 14. Wniosek metodyczny — najważniejsza rzecz z tego dnia

`[wniosek]` **Kandydaci padali, bo szukałem nieobsadzonego problemu. To jest błąd strukturalny: problemy ważne ekonomicznie są z definicji obsadzone**, bo ważność przyciąga finansowanie.

Kształt, który przeżywa:

> **znany problem + znane rozwiązanie + konkretna wariacja inżynierska, której efektu nikt nie zmierzył, porównywana wewnętrznie: mój układ z X wobec mojego układu bez X.**

`[fakt]` **Arkusz inżynierski ISEF nie ma rubryki nowości.** Explory §7 pkt 2a dopuszcza *„innowacyjny **i/lub** wnosi dodatkową wartość"*. **Optymalizowałem pod kryterium, które waży najwyżej 10 punktów na 100, i trzy razy pod nie przebudowywałem projekt.** K-075.

## 15. Powrót — decyzja autora z 17 VIII

Uzasadnienie jego słowami: cel „bardzo wysokie miejsce na ISEF" uznany za nieosiągalny przy jego budżecie, kontaktach, kompetencjach i czasie; **interfejs ma realny potencjał i jest w zasięgu**. Werdykt ostateczny.

**Trzy decyzje z tego samego wieczoru, obowiązujące do dziś:**

1. **liczba pojedyncza** — projekt jest indywidualny, zakaz „my" i „nasz" w materiałach (K-070)
2. **mowa syntetyczna wypada z demonstracji** — kolizja z projektem referencyjnym ENBM074. **Metryka w bitach, nigdy słowa na minutę** (K-071)
3. **do półfinału nie powstaje nic, co nie jest interfejsem** — rekwizyty się kupuje (K-072)

## 16. Cztery parametry, 18 VIII

**budżet 8 000 zł** · **10 godzin tygodniowo** · **kategoria ISEF EBED** · **poprzeczka „gotowy w całości, nie prototyp"**.

---

# CZĘŚĆ V — PIĘĆ DNI AUDYTU

## 17. Praca, która zabiła twierdzenie w brzmieniu ogólnym

**18 sierpnia.** Twierdzenie brzmiało wtedy **„ile kosztuje wygoda"**. Zabiła je praca, której żadne wcześniejsze przeszukanie nie mogło zobaczyć, **bo literatura chińska nie była nigdy przeszukiwana** (K-077).

`[fakt]` **Li X., Cao X., Wang J. i in.** (CAS Shenzhen, Uniwersytet Hongkoński, Uniwersytet Makau), **Sheng Wu Yi Xue Gong Cheng Xue Za Zhi 42(3):464–472, VI 2025, PMID 40566767**, po chińsku: noszalny interfejs SSVEP, 10 osób, **40 celów, 94,10%, ITR 115,25 bit/min**, i zdanie kluczowe — *„**no significant difference** compared to the dataset collected under the laboratory condition"*.

**Czyli: „ile kosztuje wygoda" ma opublikowaną odpowiedź i brzmi ona „statystycznie nic".**

## 18. Wycofanie się z werdyktu po przeczytaniu pełnego tekstu

**Tego samego dnia po południu**, po odczytaniu pełnego tekstu chińskiego zamiast abstraktu (K-092):

> „配置8通道电极帽记录枕叶脑电图（POz、PO3、PO4、PO5、PO6、Oz、O1和O2），**参考电极和接地电极放置于前额**"

**Czepek ośmiokanałowy rozpięty od POz do O2, odniesienie i masa na czole, elektrody mokre, 121 g.** Ich zmienną niezależną jest **czas przygotowania** — całe zakładanie w trzy minuty, bez regulacji impedancji. Warunkiem kontrolnym **cudzy publiczny zbiór**, nie własny układ.

`[wniosek]` **Wspólne jest hasło. Eksperyment nie jest wspólny w żadnym punkcie.** Twierdzenie zostało **zawężone**, nie porzucone.

**Z tej lekcji powstała procedura tożsamości** (`METODA.md`): siedem pytań, z pełnego tekstu, werdykt jednym z trzech słów — **tożsamy / sąsiedni / niezwiązany**. Zastosowana wstecz do **pięciu** prac, które zabiły osie: **wszystkie okazały się sąsiednie, żadna tożsama.**

## 19. Pytanie autora, które ujawniło lukę w audycie

**Cytat, 21 VIII:** *„dlaczego potylica jest tak często omijana, trochę to podejrzliwe. Skoro ledwo kto to tyka, to musi być jakiś powód."*

**Pytanie trafne i było dziurą.** Audyt sprawdzał **czy** ktoś to zmierzył, nigdy **dlaczego nie**. Odpowiedź, z trzech źródeł:

1. `[fakt]` **Yao i in., Brain Topography 2019, PMID 31037477** — problem odniesienia jest *„**unsettled** (…) inspires unceasing debate"*, *„no point on the body fulfills this condition"*, *„**more than ten references are used**"*. Dziedzina rozwiązuje go **obliczeniowo** (REST, średnia po elektrodach) — a **wszystkie te metody wymagają wielu elektrod**. Przy dwóch kanałach nie działają i pytanie wraca jako konstrukcyjne
2. `[fakt]` **Choi i in., EMBC 2006, PMID 17946448** — *„**most conventional studies do not much consider about the location of the reference electrode**"*. Luka nazwana cudzą ręką dwadzieścia lat temu
3. `[fakt]` **Joyce i Rossion 2005, PMID 16214404** — położenie odniesienia zmienia mierzony sygnał **pierwszorzędowo**: N170 i VPP to ten sam generator widziany przez dwa odniesienia

**Zła wiadomość, którą to samo pytanie wywlekło:** okolica podpotyliczna **nie jest elektrycznie cicha**. Mięsień karku (Goncharova 2003 — EMG największe na obrzeżu czaszki, z pikami w paśmie beta), **móżdżek** (Todd i in. 2018 — elektrody nad tylnym dołem czaszki, a *„visual stimulation (…) increasing the high-frequency power (…) including in **beta (14–30 Hz)**"*), i samo gładkie pole. **Ryzyko R12.**

## 20. Obawa autora o wygląd urządzenia — i co z niej wyszło

**Cytat, 21 VIII:** *„badanie z wynikiem mówiącym, że urządzenie na potylicy musi mieć gabaryty pudełka, aby solidnie działać nie brzmi tak dobrze."*

**Obawa okazała się nieuzasadniona, ale dopiero po przeliczeniu wszystkiego na jedną metrykę.** Wcześniej liczby leżały w trzech różnych postaciach i nie dawały się porównać.

**Kluczowa liczba:** para dwubiegunowa **POz−Oz, jeden kanał, dwie elektrody 3,5 cm od siebie** — **~46 bit/min przy 40 celach**, czyli **2,6 raza więcej niż najlepszy opublikowany układ zauszny**. Para na wyrostkach sutkowatych, ta sama zwartość: **2,5 bit/min**. **Osiemnastokrotna różnica wewnątrz kategorii „montaż zwarty".**

`[wniosek]` **Nie załamuje się zwartość. Załamuje się kierunek.**

## 21. Dziura w planie, którą to ujawniło

`[fakt]` Plan elektrod miał **wszystkie cztery kandydatury na odniesienie skierowane w dół albo w bok. Ani jednej w górę.**

**Skąd:** zbiór warszawski zawiera tylko O1, Oz i O2, a te leżą **na jednej linii poprzecznej**. **W tamtych danych nie ma ani jednej pary pionowej.** Reanaliza mogła zmierzyć wyłącznie pary poziome, wszystkie wypadły źle — i plan **przyjął „montaż zwarty jest zły" jako własność świata, choć była to własność zbioru.** K-099.

**Poprawka za zero złotych:** odniesienie zwarte przeniesione na **POz, ~3,5 cm powyżej Oz**; wariant w dół zostaje jako **warunek porównawczy dla kierunku**. Zmienna główna staje się **dwuwymiarowa: odległość oraz kierunek**.

## 22. Mechanizm — ostatnie znalezisko

Przeszukanie **sekcji metod** zamiast abstraktów (K-101) wyciągnęło dwie prace, których dziewięć wcześniejszych rund nie widziało.

`[fakt]` **Srinivasan, Bibi, Nunez 2006, PMID 16544207** (110 elektrod) i **Thorpe, Nunez, Srinivasan 2007, PMID 17671957**: pole SSVEP ma **strukturę falową** — fale biegnące o **λ > 15–20 cm** propagujące się **potylica → przedczołowie**, czyli **wzdłuż osi Oz–POz**.

Stąd wzór: dla pary odległej o `d` wzdłuż osi propagacji amplituda różnicy wynosi **`|2·sin(πd/λ)|`**. Przy d = 3,5 cm i λ = 15–20 cm daje to **1,04–1,34** — sygnał **zachowany**. Para w poprzek osi ma różnicę faz ≈ 0 i **kasuje**.

`[wniosek]` **Jeden wzór tłumaczy wszystkie sześć opublikowanych punktów, w tym trzy o przeciwnych znakach.** Hipoteza kierunku przestała być domysłem.

---

# CZĘŚĆ VI — CO Z TEGO ZOSTAŁO

## 22a. Dwa rozstrzygnięcia z 21 sierpnia

**Pierwsze — gabaryt domknięty.** Autor dopuścił **dwa cienkie przewody w bok, do O1 i O2** (P28a). Znaczenie tej zgody jest większe, niż wygląda: dopóki O1 i O2 musiały leżeć pod obudową, obudowa musiała mieć **~7 cm szerokości**, żeby je objąć — i to ona, a nie elektronika, wymuszała płaską płytę wielkości karty płatniczej z K-100. Po zgodzie **jedynym wymiarem, jaki obudowa musi zmieścić, jest pionowa para Oz–POz**, a ta ma 3,5 cm i siedzi na jej własnym spodzie. **Gabaryt ~32×48×12 mm przestał być życzeniem i stał się konsekwencją rozkładu elektrod.**

**Drugie — pytanie o sterowanie wzrokiem.** Autor zapytał, czy migający znacznik jest realnym limitem interfejsu potylicznego, i czy da się go obejść zmianą miejsca, czy potrzeba już inwazyjnego. **Pytanie okazało się luką w dokumentacji, nie w projekcie** (K-104): koszt rezygnacji ze wzroku jest w literaturze zmierzony od 2004 roku, a w plikach nie było ani jednej liczby na ten temat — bo pole nazywa to **„independent BCI"**, a nie żadnym z terminów, których używały wcześniejsze przeszukania. **Czwarte z rzędu zero trafień wywołane własnym słownictwem.**

Odpowiedź na samo pytanie brzmi: **tak, wzrok jest limitem tego miejsca na głowie, i nie, nie potrzeba do jego obejścia inwazyjnego — potrzeba innego miejsca na głowie, a to rozbija i moduł, i pomiar.** Rozbiór z liczbami: `05_STAN_WIEDZY.md` §7.

**Przy okazji tego przeszukania wypłynęła siódma praca do cytowania** — **Fodor 2025, PMID 40563723** (K-103). Jedyna z siedmiu, której **jedynym celem było zmniejszenie montażu** — i która mimo to zostawiła odniesienie na Cz, na przewodzie. To jest pierwszy w tym projekcie **pozytywny** dowód istnienia luki: nie „nie znalazłem nikogo", tylko „widać, gdzie kończy się uwaga pola". Druga rzecz z tej samej pracy trafiła na listę ryzyk jako **R13**: montaż zredukowany **przestał działać całkowicie u 15 z 38 osób**, a średnia dokładność mimo to **wzrosła do 98%** — bo liczona jest tylko z tych, u których cokolwiek działało.

---

## 22b. Zarzut o kamerkę i przegląd siedmiu paradygmatów, 21 sierpnia

Autor wrócił do sprawy wzroku po raz drugi tego samego dnia, z zarzutem sformułowanym ostrzej: *„argument za kamerką jest poważny i bardzo łatwo narusza projekt. A bronienie się, że urządzenie jest głównie do pomiaru, no trochę odbiera mu wagi."*

**Zarzut był trafny i moja poprzednia odpowiedź go zaniżała.** Zdanie *„SSVEP jest przyrządem pomiarowym, nie produktem"* jest prawdziwe, ale **jako jedyna obrona przyznaje zarzutowi rację i tylko odsuwa go na bok** — a przy okazji odbiera projektowi jego własny filar, czyli to, że powstaje urządzenie.

Przegląd objął **wszystkie siedem znanych nieinwazyjnych sposobów sterowania**. Dał dwie liczby, których w projekcie nie było, i jedno rozwiązanie.

**Liczba pierwsza — kamerka wygrywa i zawsze będzie.** Na tych samych jedenastu osobach: kamerka 28,2 bit/min, najlepszy interfejs mózgowy 20,9, słuchowy 3,3, dotykowy 3,4. **Udawanie, że jest inaczej, byłoby przegraną u pierwszego jurora, który to sprawdzi.**

**Liczba druga — SSVEP działa u największej liczby ludzi ze wszystkich paradygmatów.** 96,2% osób powyżej 80% dokładności i **nikt poniżej 60%**, wobec **19%** dla wyobrażenia ruchu. Przejście na sterowanie „intencją", o które autor pytał, **zamieniłoby urządzenie działające u wszystkich na działające u jednego na pięciu** — i to niezależnie od wszystkich innych kosztów.

**Rozwiązanie: jedna opcja z siedmiu zabija zarzut o kamerkę, nie ruszając w projekcie niczego.** Dwie nałożone na siebie migające powierzchnie w jednym punkcie, wybierane uwagą przy nieruchomym oku (Tsinghua 2010, 72,6% przy dwóch klasach). **Kamerka nie ma wtedy czego mierzyć, bo nie ma dokąd patrzeć**, a moduł, elektrody, tor i metryka zostają nietknięte. Wpisane jako **E6**, 11–15 h razem z treningiem i programem bodźcowym — **P38, czeka na decyzję autora.**

**Reguła, która z tego została:** zarzut, na który jest jedna odpowiedź, jest zarzutem otwartym. **Zamyka go dopiero druga odpowiedź w postaci demonstracji, a nie argumentu.**

---

## 23. Cmentarz twierdzeń

| Twierdzenie | Co je zabiło | Kiedy |
|---|---|---|
| dron: „integracja i benchmark" | prior art sprawdzony po fakcie | przed dokumentacją |
| orteza: „taniej" | stan techniki | przed 15 VIII |
| „tani interfejs o wysokim ITR" | Imperial College, £20 i 102 bit/min | 15 VIII |
| „elektroda sucha przez włosy" | PNAS 2025 plus patent | 15 VIII |
| „kanał pomocniczy do artefaktów" | Politechnika Warszawska, osiem miesięcy wcześniej | 15 VIII |
| **„kompensacja szczęki w analogu"** | **własna reanaliza: +0,2 pp zamiast +9 pp** | **16 VIII** |
| „gęste próbkowanie zastępuje rzadkie" | własna reanaliza: −18 do −24 pp | 16 VIII |
| **„ile kosztuje wygoda"** | **Li i in. 2025, po chińsku: „no significant difference"** | **18 VIII** |

## 24. Co przeżyło i dlaczego

> **Mierzę, o ile spada dokładność i przepustowość interfejsu SSVEP, gdy elektroda odniesienia musi zmieścić się w module noszonym na potylicy zamiast leżeć w miejscu standardowym, i wyznaczam najmniejszą odległość odniesienia od kory wzrokowej, przy której przepustowość jeszcze się nie załamuje — na jednym własnym torze analogowym, tą samą osobą, tym samym paradygmatem.**

**Pięć powodów, dla których to przeżyło wszystko, co zabiło resztę:**

1. **nie jest twierdzeniem o pierwszeństwie**, więc cudza publikacja go nie unieważnia — degraduje z „nowe" na „potwierdzone niezależnie"
2. **nie ma wyniku, który by je obalił** — jest tylko wynik, który zmienia jego znak
3. **ma warunek kontrolny wewnętrzny**: ten sam tor, ta sama osoba, dwa położenia elektrody
4. **ma przewidywanie ilościowe zapisane z góry**, z wzorem i parametrem z cudzych pomiarów
5. **efekt jest o dwa rzędy wielkości większy** niż ten, który odpadł: 9–24 pp zamiast 0,2 pp

## 25. Wzorce błędów, które kosztowały najwięcej

`[wniosek]` Sto jeden korekt układa się w **pięć wzorców**, i wszystkie są tym samym błędem w różnych przebraniach:

1. **redukcja czegoś złożonego do jednego zdania, a potem praca na tym zdaniu zamiast na oryginale** — „Cz i szczęka" → sama szczęka (K-089); dwie tezy ortezy → jedna (K-073)
2. **wniosek z abstraktu tam, gdzie pełny tekst był o jedno zapytanie** — K-090, K-092, K-094
3. **„zero trafień" bez kontroli pozytywnej** — arXiv, OpenAIRE, CQVIP, Europe PMC. **Cztery razy, i za każdym razem zero pochodziło od narzędzia** (K-093, K-101)
4. **szukanie własnym słownictwem zamiast słownictwem dziedziny** — i w niewłaściwej sekcji pracy (K-074, K-101)
5. **wpis do rejestru błędów bez poprawki w plikach** — K-080

**Reguła, która z nich wszystkich wynika, i jest w `METODA.md`:** *zanim uznasz pole za puste, sprawdź, czy patrzysz we właściwe miejsce właściwymi słowami — i czy Twoje narzędzie w ogóle działa.*

---

## 26. Gdzie leżą oryginały

Wszystko powyżej jest skrótem. **Pełne wersje są w `archiwum/`** i w historii gita — nic nie zostało usunięte. Rejestr błędów co do wpisu: **`KOREKTY.md`**, K-001…K-101.
