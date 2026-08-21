# 37 — Procedura sprawdzania tożsamości projektu. Rozbiór czterech prac, które wcześniej zabiły osie

**Data:** 21 sierpnia 2026
**Zlecenie użytkownika:** *„Wprowadź procedurę, gdzie jak wykryjesz korelację tematu z innym badaniem, sprawdź czy projekty są identyczne. (…) sprawdź te 3-4 badania, które wcześniej ubiły sporą część projektu i prawie sprawiły, że się poddałem."* Plus: instrukcja dojścia do baz wymagających klucza, plus obejścia reszty.

**Zastrzeżenie użytkownika, przyjęte:** *„pytania i celu nie zmieniamy"*. Nic poniżej nie zmienia twierdzenia z `35` §4.2 ani planu. To jest sprawdzenie, czy coś z tych prac da się **odzyskać**, a nie kolejna runda przebudowy.

---

## CZĘŚĆ I — PROCEDURA

## 1. Skąd się wzięła i jaki błąd naprawia

`[fakt]` Dwa razy w tym projekcie ogłosiłem twierdzenie za martwe na podstawie **zbieżności tematu**, nie zbieżności eksperymentu:

- **K-089**: „Cz i szczęka działały najlepiej" → cała dokumentacja przeniosła z tego samą szczękę i zbudowała na niej oś. Reanaliza pokazała, że szczęka daje **+0,2 pp**, a nie +9 pp
- **K-092**: praca Li i in. 2025 ogłoszona za zabójcę twierdzenia na podstawie czterech zdań abstraktu. Pełny tekst pokazał, że ich zmienną jest **czas przygotowania**, a nie geometria montażu, i że **odniesienie mają na czole**

W obu wypadkach koszt sprawdzenia wynosił jedno zapytanie. W obu wypadkach nie sprawdziłem, bo temat się zgadzał i to wyglądało na wystarczający powód.

`[wniosek]` **Zbieżność tematu nie jest zbieżnością projektu.** Pytanie „ile kosztuje wygoda" zadaje w tej dziedzinie każdy; eksperyment, który na nie odpowiada, jest u każdego inny. Procedura poniżej rozdziela te dwie rzeczy mechanicznie.

## 2. Kiedy się uruchamia

**Zawsze, gdy zachodzi którakolwiek z trzech rzeczy:**

1. znajduję pracę, której **tytuł, zdanie problemowe albo abstrakt** brzmi jak opis tego projektu
2. mam zamiar napisać gdziekolwiek, że jakieś twierdzenie jest **zajęte, martwe albo zrobione**
3. ktoś — użytkownik, juror, recenzent — pyta *„czym to się różni od X"*

**Nie uruchamia się** przy zwykłym odnotowaniu pozycji w stanie wiedzy. Do tego wystarczy abstrakt.

## 3. Siedem pytań. Odpowiedź „nie wiem" liczy się jak „różne"

Wypełnia się **z pełnego tekstu**, nie z abstraktu. Jeżeli pełnego tekstu nie ma — patrz §5.

| # | Pytanie | Dlaczego rozstrzyga |
|---|---|---|
| **1** | **Co było ich zmienną niezależną?** Co dokładnie zmieniali między warunkami? | To jest jądro. Dwie prace o „koszcie wygody" mogą zmieniać czas przygotowania i geometrię montażu — i wtedy nie mają ze sobą nic wspólnego |
| **2** | **Wobec czego porównywali?** Warunek kontrolny na tym samym sprzęcie, cudzy zbiór, czy liczba z literatury? | Porównanie z cudzym zbiorem to inna klasa twierdzenia niż porównanie wewnętrzne |
| **3** | **Gdzie leżała elektroda odniesienia i masa?** Wypisać z nazwy. | W tym projekcie to jest **zmienna główna**. Jeżeli u nich była nieruchoma, ich praca osi nie zajmuje |
| **4** | **Jaki sprzęt: kupiony czy własny?** Jeżeli własny — czy podali metrologię toru (szum, CMRR, jitter)? | Rozdziela projekt konstrukcyjny od zastosowaniowego |
| **5** | **Ile celów, ile osób, jaka metryka?** Dokładność bez liczby celów jest nieporównywalna. | 96% przy dwóch celach to mniej informacji niż 94% przy czterdziestu |
| **6** | **Co autorzy sami nazywają swoim wkładem?** Cytat ze streszczenia wkładu albo z konkluzji. | Autorzy wiedzą, o czym jest ich praca, lepiej niż tytuł |
| **7** | **Co wymieniają jako pracę przyszłą albo ograniczenie?** | Tu leżą luki opisane cudzą ręką — najtańsze uzasadnienie problemu badawczego, jakie istnieje |

**Werdykt, trzy możliwe i tylko trzy:**

- **TOŻSAMY** — ta sama zmienna niezależna **i** ta sama klasa warunku kontrolnego. Wtedy twierdzenie jest zajęte i trzeba je zmienić
- **SĄSIEDNI** — wspólne pytanie, inna zmienna albo inny warunek kontrolny. **Wtedy praca staje się cytatem i punktem odniesienia, a nie zagrożeniem.** To jest przypadek wszystkich pięciu prac z części II
- **NIEZWIĄZANY** — wspólne tylko słowa kluczowe

## 4. Reguła obowiązkowa: co zrobić z pracą „sąsiednią"

`[wniosek]` To jest część, której brakowało i przez którą dwa razy straciłem tydzień na przebudowę.

**Praca sąsiednia nie jest stratą — jest zyskiem, i trzeba z niej wyjąć trzy rzeczy:**

1. **liczbę do widełek** — ich wynik jest punktem na tej samej osi, którego nie trzeba samemu mierzyć
2. **odpowiedź na pytanie jurora** „czemu nie robisz tego, co oni" — sformułowaną i zapisaną **w chwili znalezienia pracy**, nie przed konkursem
3. **zdanie do sekcji o stanie wiedzy** — `[fakt]` regulamin Explory §7 pkt 2d daje **10 pkt na 40** za znajomość dotychczasowych badań, czyli tyle samo co kryterium innowacyjności

## 5. Gdy pełnego tekstu nie ma — kolejność prób, sprawdzona

Kolejność wyprowadzona z tego, co realnie zadziałało 18 i 21 VIII 2026:

1. **PMC przez efetch, nie przez stronę.** `eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=<PMCID bez liter>&retmode=xml`. `[fakt]` Strona `pmc.ncbi.nlm.nih.gov` potrafi zwrócić **reCAPTCHA**, a efetch na ten sam artykuł oddaje **pełny XML** — tak odczytano pracę PNAS 2025
2. **Europe PMC po DOI** — `search?query=DOI:"..."&resultType=core`. Znajduje też **preprinty** (identyfikatory `PPR...`)
3. **Semantic Scholar, rekord pracy** — pole `openAccessPdf` **wskazuje preprint dla pracy zamkniętej**. `[fakt]` Tak wyszło, że konferencyjna praca Imperial College ma preprint na bioRxiv
4. **OpenAlex, rekord pracy** — `best_oa_location` i `locations` podają wszystkie znane kopie otwarte
5. **repozytorium uczelni przez API DSpace** — `<domena>/server/api/discover/search/objects?query=...`. Strona jest aplikacją przeglądarkową i nic nie odda; API oddaje JSON. Tak przeszukano Spiral (Imperial College)
6. **abstrakt z OpenAlex** — pole `abstract_inverted_index`, do odwrócenia jednym słownikiem. Działa dla prac zamkniętych, których abstraktu nie ma w PubMed

**Jeżeli po tych sześciu krokach pełnego tekstu nadal nie ma:** werdykt zapisuje się jako **`[wniosek]` z jawną adnotacją, że stoi na abstrakcie**, i **nie wolno na nim oprzeć decyzji o zmianie twierdzenia.**

## 6. Nowe narzędzie, które ta procedura dostaje — przeszukiwanie po cytowaniach

`[fakt, sprawdzone 21 VIII 2026]` **Wyszukiwanie w OpenAlex i Semantic Scholar jest płatne albo zablokowane, ale pojedyncze rekordy i graf cytowań są darmowe:**

| Punkt końcowy | Status |
|---|---|
| `api.openalex.org/works?search=…` albo `?filter=…` | **HTTP 429**, *„Insufficient budget"* |
| **`api.openalex.org/works/doi:<DOI>`**, **`/works/pmid:<PMID>`** | **działa** — a rekord zawiera `related_works` i `referenced_works` |
| `api.semanticscholar.org/graph/v1/paper/search` | **HTTP 429** |
| **`…/paper/DOI:<DOI>/citations`** oraz **`/references`** | **działa** |

`[wniosek]` **To jest ważniejsze niż samo obejście limitu.** Przeszukiwanie po słowach kluczowych zawiodło w tym projekcie trzy razy, zawsze z tego samego powodu: **szukałem własnym słownictwem** (K-074). **Graf cytowań nie zależy od słownictwa.** Jeżeli ktokolwiek zrobiłby pomiar przepustowości w funkcji położenia odniesienia, prawie na pewno zacytowałby jedną z dwóch prac, które to porównanie kiedykolwiek zrobiły.

**Test wykonany od razu, i jest to najmocniejszy dowód, jaki ten projekt ma na niezajętość osi:**

| Praca | Cytowań | Czy któreś dotyczy odległości odniesienia |
|---|---|---|
| **Wu i Su 2014**, *A Dynamic Selection Method for Reference Electrode in SSVEP-Based BCI* | **16** w dwanaście lat | **żadne.** Wszystkie o algorytmach, filtrach przestrzennych, doborze częstotliwości, neurofeedbacku |
| **Diez i in. 2010**, *A comparison of monopolar and bipolar EEG recordings for SSVEP detection* | **23** w szesnaście lat | **żadne.** Wysokoczęstotliwościowy SSVEP, wózki, VR, uczenie głębokie, zmęczenie wzrokowe |

`[wniosek]` **Dwie jedyne prace, które kiedykolwiek porównały montaże dla SSVEP, mają razem 39 cytowań i ani jednej kontynuacji w tę stronę.** To nie jest „nie znalazłem" — to jest „pole zostało otwarte dwa razy i dwa razy nikt nie wszedł".

**Skutek dla ryzyka R5** (`17_RYZYKA.md`, „ktoś publikuje tę samą oś przed nami"): `[fakt]` **praca Kołodziej i in. 2026 ma po siedmiu miesiącach jedno cytowanie**, i jest nim koreański speller, nie kontynuacja sprzętowa. **Obniżam R5 z 10–20% na 5–10%.**

---

## CZĘŚĆ II — ROZBIÓR CZTERECH PRAC, KTÓRE ZABIŁY WCZEŚNIEJSZE OSIE

Procedura z §3 zastosowana wstecz. **Wynik zbiorczy: żadna z nich nie jest tożsama; wszystkie cztery są sąsiednie, i z każdej da się coś wyjąć.**

---

## 7. Imperial College 2022 — „interfejs za £20 robi 102 bit/min"

**Teversham J., Wong S., Hsieh B., Rapeaux A., Troiani F., Savolainen O., Zhang Y., Maslik M., Constandinou T.G.** — *Development of an Ultra Low-Cost SSVEP-based BCI Device for Real-Time On-Device Decoding*, **EMBC 2022, PMID 36086083**. `[fakt]` Praca zamknięta; **preprint bioRxiv 10.1101/2022.01.29.478203**, znaleziony przez pole `openAccessPdf` w rekordzie Semantic Scholar. Sama bioRxiv blokuje ten adres (Cloudflare 1015), abstrakt odczytany przez Europe PMC (`PPR448246`).

**Co zabiła:** twierdzenie „zbudowałem tani interfejs SSVEP o wysokiej przepustowości" (`12_AUDYT.md` §1.1).

| # | Pytanie | Odpowiedź |
|---|---|---|
| 1 | zmienna niezależna | `[luka]` **żadnej porównawczej.** To jest praca konstrukcyjna: budują urządzenie i podają jego wynik |
| 2 | warunek kontrolny | **brak wewnętrznego.** Wynik podany bezwzględnie |
| 3 | odniesienie i masa | `[luka]` **nie wynika z abstraktu**, pełny tekst niedostępny |
| 4 | sprzęt | **własny, ESP32**, dekodowanie na urządzeniu, ~£20 |
| 5 | cele / osoby / metryka | `[luka]` liczby celów **abstrakt nie podaje**; 95,56 ± 3,74%, ITR 102 bit/min, msCCA i gCCA, *„with modest calibration"* |
| 6 | wkład wg autorów | cytat: *„intended to offer a **financially and operationally accessible device that can be deployed on a mass scale to facilitate education and public engagement** in the domain of EEG sensing and neurotechnologies"* |
| 7 | praca przyszła | `[luka]` |

**Werdykt: SĄSIEDNI.** `[wniosek]` Punkt 6 rozstrzyga i jest to rzecz, której wcześniej nie odczytałem: **to jest urządzenie edukacyjno-popularyzatorskie do masowego rozdawania**, a nie przyrząd pomiarowy. Nie mierzy niczego w funkcji czegokolwiek, nie podaje charakterystyki toru, nie zmienia montażu.

**Co z tego wyjmuję — i to jest najlepszy zysk z całej tej części:**

1. **To jest dowód wykonalności, nie zagrożenie.** `[fakt]` Cel przepustowościowy rzędu 100 bit/min osiągnięto **na mikrokontrolerze za £20**. Ryzyko techniczne całego projektu jest przez tę pracę **obniżone**, i tak jest już zapisane w `12_AUDYT.md` §3
2. **Odpowiedź na pytanie jurora „czemu Twój sprzęt kosztuje więcej niż ich za £20":** bo tamto urządzenie ma dowieść, że da się tanio; to ma **zmierzyć zależność**, a do pomiaru potrzeba ośmiu kanałów rejestrowanych jednocześnie i znanej charakterystyki toru — czego tamto nie podaje
3. `[luka]` **Liczby celów nie znam**, więc **zakaz porównywania własnego ITR z ich 102 bit/min** bez tej liczby. Wpisuję jako regułę, bo ITR bez N jest nieporównywalny (`06_TABELA_PARAMETROW.md` §0)

---

## 8. PNAS 2025 — „mikroczujniki między włosami, 96,4%"

**Kim H., Kim J.H., Lee Y.J. i in.** (Georgia Tech, Yonsei, Hanyang), *PNAS* 122(15):e2419304122, **PMID 40193612**. `[fakt]` **Pełny tekst odczytany** — strona PMC zwróciła reCAPTCHA, efetch oddał kompletny XML.

**Co zabiła:** twierdzenie o konstrukcji elektrody suchej przez włosy (`12_AUDYT.md` §1.2).

| # | Pytanie | Odpowiedź |
|---|---|---|
| 1 | zmienna niezależna | **rodzaj elektrody** (mikroczujnik wobec kubkowej z żelem) oraz **poziom ruchu** (stanie, marsz 3 km/h, bieg 6 km/h) |
| 2 | warunek kontrolny | **na tym samym sprzęcie i jednocześnie** — cytat: *„Commercial gold-cup electrodes and microsensors are attached and inserted into the scalp of the occipital-parietal lobe **simultaneously**"*. Rzemiosło wzorowe |
| 3 | **odniesienie i masa** | cytat: *„positioned at **O1, O2, and Pz** (…) with **Pz serving as the reference channel**"*. **Odniesienie nieruchome, na ciemieniu, poza modułem** |
| 4 | sprzęt | **kupiony** — *„a wireless biopotential measurement device was attached to the behind of the neck"*. Własna jest **elektroda**, nie tor |
| 5 | cele / osoby / metryka | **dwa bodźce** (odwrócenie wzoru plus zmiana rozmiaru); dokładność 99,2 / 97,5 / 92,5% (stanie / marsz / bieg), średnio **96,4%**; **ITR nie podane** |
| 6 | wkład wg autorów | wytwarzanie: formowanie replikacyjne UV, cięcie laserem femtosekundowym, pionowe powlekanie wirowe polimerem; impedancja **0,03 kΩ·cm⁻²**, noszenie do **12 h**; demonstracja rozmowy wideo w AR |
| 7 | ograniczenia | drgania okularów AR psują wywołanie SSVEP przy biegu |

**Werdykt: SĄSIEDNI, i to odleglejszy, niż zakładałem.** `[wniosek]` To jest praca **materiałowo-wytwórcza**. Zmienną jest elektroda, tor jest kupiony, **odniesienie nieruchome na Pz**, metryki przepustowościowej nie ma w ogóle.

**Co z tego wyjmuję:**

1. **Pz jako odniesienie działa i to jest kolejny punkt widełek.** Ciemię jest **poza polem SSVEP, ale blisko** — dokładnie ten obszar, o który pyta projekt. `[wniosek]` Trzy prace, trzy różne odniesienia poza modułem: **czoło** (Li 2025), **Cz** (Yan 2026), **Pz** (Kim 2025), plus **małżowina** (Kołodziej) i **wyrostki sutkowate** (Yan 2026, grupa pacjentów). Wszystkie działają. **Nikt nie zszedł poniżej — i to jest cała stawka projektu**
2. **96,4% przy dwóch celach to znacznie mniej informacji, niż brzmi.** `[wniosek]` Przy dwóch celach poziom losowy wynosi 50%. **Do materiałów: nigdy nie zestawiać własnej dokładności z cudzą bez podania N** — ta praca jest tego najlepszym przykładem i nadaje się na przykład w rozmowie z jurorem
3. **Elektroda jest problemem rozwiązanym i zamkniętym patentowo** (deklaracja konfliktu interesów wymienia zgłoszenie patentowe). `[wniosek]` To potwierdza decyzję z `12_AUDYT.md`: **elektrodę robi się dobrze i nie sprzedaje jako wynalazku.** Konkurowanie z formowaniem UV i laserem femtosekundowym przy budżecie 8 000 zł nie jest możliwe i nie jest potrzebne

---

## 9. Politechnika Warszawska 2026 — „kanał pomocniczy usuwa artefakt"

**Kołodziej M., Majkowski A., Wiszniewski P.**, *Sensors* 26(3):917, **PMID 41682433**, PMC12899023.

**Co zabiła:** oś „analogowa kompensacja artefaktu szczękowego" (`12_AUDYT.md` §1.3, potem `14_REANALIZA.md`).

**Ta praca ma najgłębszy możliwy rozbiór, jaki ten projekt kiedykolwiek zrobi:** jej zbiór danych jest publiczny (CC BY), **pipeline odtworzony od zera i zweryfikowany co do trzeciego miejsca po przecinku** — dwukrotnie, przez dwie niezależne sesje (`14_REANALIZA.md`, potwierdzenie w `35_AUDYT_2026_08_18.md` §0.1). Siedem pytań procedury jest tam odpowiedziane pomiarem, nie lekturą.

**Co dokładam dzisiaj — jedną rzecz, i jest istotna dla ryzyka:**

`[fakt, graf cytowań Semantic Scholar, 21 VIII 2026]` **Praca ma jedno cytowanie.** Jest nim *A Cheonjiin Layout Mental Speller* (PMID 41978050) — koreański speller, nie kontynuacja sprzętowa.

`[wniosek]` `12_AUDYT.md` §4.1 nazwał tę grupę **„nazwanym konkurentem z terminem"** i uznał za najwyższe ryzyko projektu, bo sami wskazali w pracy przyszłej *„low-channel, wearable SSVEP–BCI systems in which artifact reduction is addressed already at the signal acquisition stage"*. Siedem miesięcy później: **zero nowych prac tych autorów w PubMed** (sprawdzone imiennie 18 VIII) i **jedno cytowanie ich pracy, niezwiązane**. **R5 schodzi z 10–20% na 5–10%.**

**Co wyjmuję dodatkowo:** ich zdanie o pracy przyszłej **nadal jest najlepszym cytowalnym uzasadnieniem problemu, jakie ten projekt ma** — bo opisuje projekt użytkownika słowami cudzych recenzowanych autorów. Nie zmieniło się nic poza tym, że po siedmiu miesiącach nikt za tym zdaniem nie poszedł.

---

## 10. Arpaia i in. 2023 — „jeden kanał różnicowy, elektrody suche, 80–95%"

**Arpaia P. i in.** (Neapol), *J Vis Exp*, **PMID 37486136**. `[fakt]` Praca zamknięta; abstrakt odzyskany z pola `abstract_inverted_index` w OpenAlex.

| # | Pytanie | Odpowiedź |
|---|---|---|
| 1 | zmienna niezależna | **czas stymulacji** — *„classification accuracy was between 80%-95% on average **depending on the stimulation time**"* |
| 2 | warunek kontrolny | **brak wewnętrznego** |
| 3 | odniesienie | `[luka]` — wiadomo tylko, że kanał jest **różnicowy**, więc odniesienie leży blisko elektrody czynnej |
| 4 | sprzęt | **wszystko kupione** — komercyjny rejestrator EEG plus okulary XR |
| 5 | cele / osoby | ikony na wyświetlaczu, liczby celów abstrakt nie podaje; **20 osób** |
| 6 | wkład wg autorów | *„a user-friendly, low-cost BCI was built by **integrating** extended reality glasses with a **commercially available** EEG device"* — integracja gotowych elementów |
| 7 | zastosowanie | inspekcja przemysłowa, rehabilitacja w ADHD i autyzmie |

**Werdykt: SĄSIEDNI.** `[wniosek]` To jest praca **integracyjna** — dokładnie ten typ twierdzenia, który zabił projekt drona (`29_ODRZUCONE_KIERUNKI.md`: *„integracja i benchmark"*). Nie ma tam własnego sprzętu, warunku kontrolnego ani zmiennej geometrycznej. **Cytowań: 1.**

**Co wyjmuję:**

1. **Pojedynczy kanał różnicowy z elektrodami suchymi daje 80–95% na dwudziestu osobach.** To jest **punkt widełek po stronie zwartej** i jedyny na dwudziestu badanych. `[luka]` bez liczby celów nieporównywalny wprost — do ustalenia, jeżeli kiedykolwiek pełny tekst będzie dostępny
2. **Kontrast, który warto mieć przygotowany:** ta sama okolica, ten sam typ montażu, a wyniki w literaturze rozrzucone od **29,69%** (Cardoso 2022, para na wyrostkach sutkowatych) przez **68,25%** (Li 2025, POz−Oz) po **80–95%** (ta praca). `[wniosek]` **Rozrzut czterdziestu punktów procentowych dla „montażu zwartego" jest sam w sobie argumentem, że zmienna nie jest zmierzona** — bo gdyby była, taki rozrzut byłby wyjaśniony

---

## 11. Dokładka — praca, która najbardziej straszyła tytułem

**Yan W., Luo Q., Du C. i in.** (Xi'an Jiaotong University), *Cross-region neural signal reconstruction to **lift electrode placement constraints** in SSVEP brain-computer interfaces*, **npj Biomedical Innovations**, 2026, **PMID 42527436**, PMC13421537. `[fakt]` **Pełny tekst odczytany przez efetch.**

`25_AUDYT_OPENAIRE.md` §3.2 zapisał ją jako *„nasze zdanie problemowe, dosłownie, w cudzym tytule"* i ostrzegał, że **pytanie o nią padnie**. Rozbieram, żeby odpowiedź istniała.

| # | Pytanie | Odpowiedź |
|---|---|---|
| 1 | zmienna niezależna | **obszar akwizycji**: czoło zamiast potylicy, z rekonstrukcją sieciową |
| 2 | warunek kontrolny | **linie bazowe algorytmiczne**, poprawa maks. **33,47%** dekodowania |
| 3 | **odniesienie i masa** | grupa źródłowa: **Cz odniesienie, FPz masa**; grupa pacjentów: **odniesienie i masa na wyrostkach sutkowatych**, pięć elektrod naklejanych na czole |
| 4 | sprzęt | **kupiony** (ZhenTec NT1) plus własny układ naklejany dla pacjentów leżących |
| 5 | cele / osoby | **cztery cele** (8/9/10/11 Hz), 5 s wpatrywania; 12 osób źródłowych, 20 nowych, w tym **8 pacjentów po urazie mózgu** |
| 6 | wkład wg autorów | **DSTF-Net** — rekonstrukcja sygnału potylicznego z czołowego siecią neuronową |
| 7 | **problem, który nazywają** | cytat: *„supine positioning (…) **occipital bone defects** (…) postoperative cranial fixation devices frequently interfere with electrode placement. These clinical constraints effectively preclude occipital EEG acquisition"* |

**Werdykt: SĄSIEDNI, i jest to najdalszy z całej piątki.** `[wniosek]` **Ich ograniczenie jest medyczne, nasze jest gabarytowe.** Oni **rezygnują z potylicy** i odtwarzają ją siecią; projekt **zostaje na potylicy** i pyta, jak blisko może leżeć odniesienie. Zbieżny jest wyłącznie zwrot „electrode placement constraints".

**Co wyjmuję — i to jest zysk większy niż z pozostałych czterech razem:**

1. **Gotowa odpowiedź na pytanie jurora, sformułowana teraz:** *DSTF-Net rozwiązuje przypadek, w którym potylicy nie da się użyć w ogóle — pacjent leży, ma ubytek kości albo stabilizator. Wymaga sieci uczonej na parach sygnałów czołowych i potylicznych. Mój problem jest inny: potylica jest dostępna, tylko urządzenie musi być małe. Na to sieć nie odpowiada, bo pytanie brzmi, gdzie postawić elektrodę, a nie jak odtworzyć sygnał, którego nie ma.*
2. **Cytat, który uzasadnia wagę problemu ręką autorów z czasopisma z portfolio Nature:** *„To the best of our knowledge, **no existing studies have addressed this critical technical barrier** despite its urgent u[rgency]"*. `[wniosek]` Ograniczenia umiejscowienia elektrod są w 2026 roku nazwane **otwartym problemem** w takim czasopiśmie. **Projekt nie musi udowadniać, że pytanie jest ważne — wystarczy je zacytować**
3. **Dwa kolejne punkty do widełek odniesienia: Cz i wyrostki sutkowate**, oba działające

---

## 12. Bilans części II

| Praca | Werdykt | Co zabiła | Co z niej odzyskane |
|---|---|---|---|
| Imperial College 2022 | **sąsiedni** | „tani interfejs o wysokim ITR" | dowód wykonalności 100 bit/min na sprzęcie hobbystycznym; to urządzenie **edukacyjne**, nie pomiarowe |
| PNAS 2025 | **sąsiedni** | „elektroda sucha przez włosy" | **Pz działa jako odniesienie**; wzorzec rzemiosła (dwa typy elektrod jednocześnie); przestroga o dokładności bez N |
| Politechnika Warszawska 2026 | **sąsiedni**, rozebrany pomiarem | „kanał pomocniczy" | zdanie o pracy przyszłej jako uzasadnienie; **R5 spada do 5–10%** |
| Arpaia 2023 | **sąsiedni** | wspierała „tani noszalny" | punkt widełek: jeden kanał różnicowy, 80–95%, 20 osób |
| Yan i in. 2026 | **sąsiedni**, najdalszy | straszyła tytułem | **cytat, że problem jest otwarty**, z czasopisma Nature; dwa punkty widełek; gotowa odpowiedź dla jurora |

`[wniosek]` **Żadna z pięciu prac nie jest tożsama i żadna nie zmienia twierdzenia.** Czterech z pięciu nie znałem od strony metody — znałem je z abstraktów. **Wszystkie pięć trzymają odniesienie nieruchomo**, w pięciu różnych miejscach poza modułem: czoło, Cz, Pz, małżowina, wyrostek sutkowaty. **Żadna nie zeszła z odniesieniem do wnętrza obszaru potylicznego i nie zmierzyła, ile to kosztuje.**

---

## CZĘŚĆ III — DOSTĘP DO BAZ

## 13. Klucze API — co zrobić, krok po kroku

**Wszystkie trzy są darmowe.** Poniżej dokładnie tyle, ile trzeba zrobić. `[luka]` **Nie zakładam kont w Twoim imieniu** — wymagają Twojego adresu i zgody na regulamin.

### 13.1 Semantic Scholar — najważniejszy, bo odblokowuje wyszukiwanie

- **gdzie:** `semanticscholar.org/product/api` → przycisk **„Request an API key"**
- **co podać:** adres e-mail, nazwa organizacji (wystarczy nazwa szkoły), krótki opis zastosowania. Wystarczy jedno zdanie po angielsku: *„Literature review for a high-school science-fair engineering project on EEG electrode montages."*
- **ile trwa:** `[domysł]` od jednego dnia do kilku; klucz przychodzi mailem
- **co daje:** `/paper/search` przestaje zwracać 429, czyli **wraca pełne wyszukiwanie po słowach kluczowych** w bazie obejmującej ~200 mln prac
- **co z nim zrobić:** wkleić mi go w rozmowie **albo** dopisać do pliku `.env` w repozytorium i powiedzieć, że jest. Nagłówek to `x-api-key`

### 13.2 OpenAlex — najprostszy, bo bez wniosku

`[fakt]` Komunikat, który dostaję: *„Insufficient budget. This request costs $0.001 but you only have $0 remaining. Resets at midnight UTC."* Czyli **pula darmowa jest wyczerpana dla adresu tego środowiska**, nie dla Ciebie.

- **wariant darmowy, bez żadnego konta:** `[fakt]` **pojedyncze rekordy działają już teraz** (`/works/doi:…`, `/works/pmid:…`) i to jest dokładnie to, na czym stoi §6. Do wyszukiwania jednak potrzeba puli
- **gdzie po klucz:** `openalex.org/pricing` → plan darmowy z rejestracją; alternatywnie **pula „polite"** działa dla adresów, które nie wyczerpały limitu, po dopisaniu `mailto=<twój@email>` do zapytania
- **`[luka]` czego nie wiem:** czy rejestracja podniesie limit dla **adresu tego środowiska**, czy dla konta. Jeżeli jest wiązana z adresem sieciowym, klucz nie pomoże i zostaje wariant z §13.4

### 13.3 KCI — baza koreańska

- **gdzie:** `open.kci.go.kr` → **OpenAPI** → rejestracja i wniosek o `key`
- **`[luka]`** interfejs jest po koreańsku i **nie wiem, czy rejestracja jest otwarta dla osób spoza Korei**. To jest najmniej pilna pozycja z trzech — grupy koreańskie publikują SSVEP głównie po angielsku, więc PubMed i Crossref je łapią
- **priorytet: najniższy.** Nie robić przed Semantic Scholar

### 13.4 Wariant bez żadnych kluczy — i to jest realna alternatywa

`[wniosek]` Jeżeli zakładanie kont okaże się męczące: **odpal jedno zapytanie z domowego internetu.** Limity OpenAlex i bioRxiv są nałożone na **adres sieciowy tego środowiska**, nie na Ciebie. Wejście z telefonu na `openalex.org` i wpisanie hasła w wyszukiwarkę da ten sam wynik co API — tylko trzeba by mi przekleić tytuły.

**Rekomendacja, jedna:** **zrób tylko Semantic Scholar.** Jest darmowy, wniosek to trzy pola, a odblokowuje jedyną rzecz, której naprawdę brakuje — wyszukiwanie pełnotekstowe po słowach kluczowych w największym indeksie. OpenAlex i KCI zostawić.

## 14. Obejścia znalezione 21 VIII 2026 — dopisane do zestawu

| Blokada | Obejście | Status |
|---|---|---|
| **PMC zwraca reCAPTCHA** | `efetch.fcgi?db=pmc&id=<numer bez PMC>&retmode=xml` | **działa** — tak odczytano PNAS 2025 |
| **OpenAlex: wyszukiwanie płatne** | rekord po `doi:` albo `pmid:` jest darmowy; `related_works` i `referenced_works` dają nawigację | **działa** |
| **Semantic Scholar: `/search` 429** | `/paper/<id>/citations` i `/references` bez klucza | **działa** — dwa najmocniejsze wyniki §6 |
| **praca konferencyjna zamknięta** | rekord Semantic Scholar, pole `openAccessPdf` — wskazuje preprint | **działa** — tak znaleziono preprint Imperial College |
| **abstraktu brak w PubMed** | OpenAlex, `abstract_inverted_index`, odwrócenie słownikiem | **działa** — tak odzyskano abstrakt Arpaia 2023 |
| **repozytorium uczelni to aplikacja przeglądarkowa** | API DSpace: `/server/api/discover/search/objects?query=` | **działa** — Spiral (Imperial College) |
| **bioRxiv** | brak | **HTTP 429, Cloudflare 1015** — adres zablokowany na twardo |
| **CORE** | brak | **HTTP 403** |
| **CNKI** | CQVIP jako namiastka (`36` §4.1) | **CNKI nadal zrywa TLS** |

---

## 15. Co z tego wchodzi do zadań

| # | Zadanie | Termin |
|---|---|---|
| **P19** | **procedura z §3 obowiązuje od teraz** przy każdym „to jest zajęte" — siedem pytań, z pełnego tekstu, werdykt jednym z trzech słów | od zaraz |
| **P20** | **przeszukiwanie po grafie cytowań** (§6) wchodzi do zestawu obok zapytań słownikowych; kontrolę na Wu/Su 2014 i Diez 2010 **powtarzać co pół roku** — jeżeli pojawi się cytowanie o montażu, to jest sygnał wczesny | co pół roku |
| **P16a** | **klucz do Semantic Scholar** — jedyna pozycja z §13, którą warto robić | gdy będzie chwila |
| **P21** | **do banku odpowiedzi na pytania jurora** wpisać trzy gotowe: o DSTF-Net (§11), o urządzeniu za £20 (§7), o dokładności bez podanego N (§8) | trening IX 2027 |
| **P22** | `17_RYZYKA.md` **R5 obniżone do 5–10%** na podstawie grafu cytowań; przeliczyć przy najbliższym przeglądzie ryzyk | zrobione w tym pliku |
