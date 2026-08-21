# METODA — jak się w tym projekcie sprawdza literaturę

**Stan na 21 sierpnia 2026.** Ten plik zastępuje metodę z `archiwum/12_AUDYT.md` i rozdziały o przeszukiwaniu z `archiwum/25_AUDYT_OPENAIRE.md`, `archiwum/37_*`, `archiwum/40_*`.

**Po co istnieje:** przeszukanie literatury zawiodło w tym projekcie **cztery razy**, zawsze z tego samego powodu i zawsze dając fałszywe „zero trafień". Poniżej jest wszystko, co z tych czterech razy wynikło.

---

## 1. Audyt adwersaryjny — zasada nadrzędna

**Próbuj zabić projekt, nie obronić.** Każde twierdzenie traktuj jako hipotezę do obalenia. Trzy przejścia:

1. **spójność wewnętrzna** — czy dokumentacja mówi jedno
2. **literatura i patenty** — czy cudzy wynik unieważnia twierdzenie
3. **wykonalność** — czy budżet, godziny i regulaminy się spinają

---

## 2. Procedura tożsamości — zanim napiszesz, że coś jest zajęte

**Uruchamia się zawsze, gdy:** znajdujesz pracę brzmiącą jak opis tego projektu; masz zamiar napisać, że coś jest **zajęte, martwe albo zrobione**; ktoś pyta *„czym to się różni od X"*.

**Nie uruchamia się** przy zwykłym odnotowaniu pozycji w stanie wiedzy — do tego wystarczy abstrakt.

### 2.1 Siedem pytań, z pełnego tekstu

| # | Pytanie | Dlaczego rozstrzyga |
|---|---|---|
| 1 | **Co było ich zmienną niezależną?** | Jądro sprawy. Dwie prace o „koszcie wygody" mogą zmieniać czas przygotowania i geometrię montażu — i nie mają wtedy ze sobą nic wspólnego |
| 2 | **Wobec czego porównywali?** | Warunek kontrolny na tym samym sprzęcie to inna klasa twierdzenia niż porównanie z cudzym zbiorem |
| 3 | **Gdzie leżała elektroda odniesienia i masa?** | W tym projekcie to jest **zmienna główna**. Jeżeli u nich była nieruchoma, osi nie zajmują |
| 4 | **Sprzęt kupiony czy własny?** Podali metrologię toru? | Rozdziela projekt konstrukcyjny od zastosowaniowego |
| 5 | **Ile celów, ile osób, jaka metryka?** | Dokładność bez liczby celów jest nieporównywalna |
| 6 | **Co autorzy sami nazywają swoim wkładem?** | Wiedzą to lepiej niż tytuł |
| 7 | **Co wymieniają jako pracę przyszłą albo ograniczenie?** | Tu leżą luki opisane cudzą ręką |

**Werdykt — jedno z trzech słów, nic pośredniego:**

- **TOŻSAMY** — ta sama zmienna niezależna **i** ta sama klasa warunku kontrolnego → twierdzenie zajęte, trzeba je zmienić
- **SĄSIEDNI** — wspólne pytanie, inna zmienna albo inny warunek → **praca staje się cytatem, nie zagrożeniem**
- **NIEZWIĄZANY** — wspólne tylko słowa kluczowe

**Odpowiedź „nie wiem" liczy się jak „różne".**

### 2.2 Obowiązkowy wyciąg z pracy „sąsiedniej"

`[wniosek]` To jest część, której brak dwa razy kosztował tydzień przebudowy. **Praca sąsiednia nie jest stratą — z każdej wyjmuje się trzy rzeczy:**

1. **liczbę do widełek** — ich wynik jest punktem na tej samej osi, którego nie trzeba mierzyć samemu
2. **odpowiedź na pytanie jurora „czemu nie robisz tego, co oni"** — sformułowaną **w chwili znalezienia pracy**, nie przed konkursem
3. **zdanie do sekcji o stanie wiedzy** — `[fakt]` regulamin Explory §7 pkt 2d płaci za to **10 pkt na 40**

---

## 3. Przeszukiwanie — trzy kanały, nie jeden

### 3.1 Kanał pierwszy: słownictwo dziedziny, nie własne

`[fakt]` Trzy razy w tym projekcie zapytanie zbudowane na własnym sformułowaniu problemu dało „zero trafień", a pole było zajęte. Dziedzina mówi **„monopolar versus bipolar"**, **„lead selection"**, **„channel and reference selection"**, **„electrode placement constraints"** — a nie „reference electrode distance".

**Zawsze dołożyć: filtr języka.** `chi[LA]`, `jpn[LA]` w PubMed. **Praca, która zabiła poprzednie brzmienie twierdzenia, była po chińsku i znalazła się jednym zapytaniem, którego nikt wcześniej nie wykonał.**

### 3.2 Kanał drugi: właściwa sekcja pracy, nie abstrakt

`[fakt]` **Położenie elektrody odniesienia podaje się w sekcji metod i prawie nigdy w abstrakcie.** Dziewięć rund przeszukania szukało tej informacji tam, gdzie z definicji jej nie ma.

**Europe PMC pozwala przeszukiwać sekcje osobno:**

| Pole | `SSVEP` daje | Uwaga |
|---|---|---|
| zapytanie zwykłe | 3 038 | |
| `ABSTRACT:"…"` | 1 493 | |
| **`METHODS:"…"`** | **861** | **właściwe narzędzie do aparatury** |
| `BODY:"…"` | 1 928 | |
| ~~`FULL_TEXT:"…"`~~ | **0** | **pole nie istnieje** — zwraca zero na każde zapytanie |

### 3.3 Kanał trzeci: graf cytowań, bo nie zależy od słownictwa

`[fakt]` **Wyszukiwanie w OpenAlex jest płatne, ale rekordy i relacje są darmowe. W Semantic Scholar wyszukiwanie bywa chwilowo dławione, ale działa.**

| Punkt końcowy | Status |
|---|---|
| `api.openalex.org/works?search=` / `?filter=` | **429, „Insufficient budget"** |
| **`api.openalex.org/works/doi:<DOI>` i `/works/pmid:<PMID>`** | **działa** — rekord zawiera `related_works` i `referenced_works` |
| **`api.semanticscholar.org/graph/v1/paper/search`** | **działa**, bez klucza; 429 znaczy chwilowe dławienie |
| **`…/paper/PMID:<PMID>/citations` i `/references`** | **działa** |
| **`opencitations.net/index/coci/api/v1/citations/<DOI>`** | **działa** (po przekierowaniu) — trzeci niezależny graf |

**Test, który ten kanał umożliwił, a którego dziesięć rund zapytań słownikowych nie dało:**

| Praca | Cytowań | Ile o geometrii montażu |
|---|---|---|
| Wu i Su 2014 — dobór elektrody odniesienia dla SSVEP | **16** w dwanaście lat | **zero** |
| Diez i in. 2010 — jednobiegunowy wobec dwubiegunowego | **23** w szesnaście lat | **zero** |

`[wniosek]` **Pole otwarto dwa razy i dwa razy nikt nie wszedł.** To jest mocniejsze zdanie niż jakiekolwiek „nie znalazłem".

**Do wykonania co pół roku:** ponowić obie kontrole. **Nowe cytowanie dotyczące montażu jest sygnałem wczesnym.**

---

## 4. Reguła, która obowiązuje bezwzględnie: kontrola pozytywna

**Każde „zero trafień" wymaga zapytania, o którym wiadomo, że musi coś zwrócić — i to PRZED zapytaniem właściwym.**

`[fakt]` **Cztery wystąpienia w tym projekcie, za każdym razem zero pochodziło od narzędzia, nie od literatury:**

| Gdzie | Na czym polegała pułapka |
|---|---|
| **arXiv** | składnia `all:"fraza w cudzysłowie"` zwraca zero na każde zapytanie |
| **OpenAIRE** | parametr `keywords` wymaga **wszystkich słów naraz** — długie zapytanie zawsze daje zero |
| **CQVIP** | wyniki są w polu `class="abstr"`, nie w selektorze tytułu |
| **Europe PMC** | pole `FULL_TEXT:` **nie istnieje** |

**Kontrola musi być zapytaniem o nazwę dziedziny w języku bazy.** Baza, która nie zna słowa „脑机接口", nie istnieje.

---

## 5. Gdy pełnego tekstu nie ma — kolejność prób

1. **PMC przez efetch, nie przez stronę.** `eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=<PMCID bez liter>&retmode=xml`. `[fakt]` Strona `pmc.ncbi.nlm.nih.gov` potrafi zwrócić **reCAPTCHA**, a efetch na ten sam artykuł oddaje **pełny XML**
2. **Europe PMC po DOI** — `search?query=DOI:"…"&resultType=core`. Znajduje też preprinty (`PPR…`)
3. **Semantic Scholar, rekord pracy** — pole `openAccessPdf` **wskazuje preprint dla pracy zamkniętej**
4. **OpenAlex, rekord pracy** — `best_oa_location` i `locations`
5. **repozytorium uczelni przez API DSpace** — `<domena>/server/api/discover/search/objects?query=…`. Strona jest aplikacją przeglądarkową i nic nie odda; API oddaje JSON
6. **abstrakt z OpenAlex** — pole `abstract_inverted_index`, do odwrócenia słownikiem. Działa dla prac zamkniętych

**Jeżeli po tych sześciu krokach nadal nie ma:** werdykt zapisuje się jako `[wniosek]` **z jawną adnotacją, że stoi na abstrakcie**, i **nie wolno na nim oprzeć decyzji o zmianie twierdzenia.**

---

## 6. Trzy klasy blokady — rozróżniać, nie mylić

| Kod | Znaczy | Co robić |
|---|---|---|
| **403 / 401** | brak uprawnień | **zapisać jako blokadę** |
| **429** | **dławienie** | **ponowić następnego dnia**, dopiero potem zapisywać |
| **000, błąd TLS, 418** | nieosiągalne albo blokada antybotowa | zapisać jako blokadę z opisem próby |

`[fakt]` Semantic Scholar był przez trzy dni zapisany w czterech plikach jako niedostępny na podstawie 429. **Działa bez klucza.**

**Czego nie robić:** nie obchodzić blokad podszywaniem się. **To jest ta sama kategoria co fałszowanie danych.**

---

## 7. Stan dostępu do baz, 21 sierpnia 2026

**Działają:** PubMed (E-utilities), Europe PMC (z `METHODS:`/`BODY:`), Crossref, OpenAIRE, DOAJ, arXiv, J-STAGE, CiNii, **CQVIP** (chińska), Semantic Scholar, OpenAlex (rekordy), OpenCitations, Unpaywall, Google Patents, Patentscope WIPO, Zenodo, HAL, Figshare, **baza abstraktów ISEF** (POST z tokenem sesji).

**Zablokowane, z opisem próby:**

| Baza | Co próbowano | Wynik |
|---|---|---|
| **CNKI** | cztery hosty, TLS 1.2, pominięcie weryfikacji certyfikatu, pełne nagłówki przeglądarki, `zh-CN` | **HTTP 418** — blokada antybotowa |
| **BASE** | różne UA | *„Access denied for IP address…"* |
| **bioRxiv** | trzy adresy, dwa UA, odczekanie | Cloudflare **1015** |
| **CORE** | v3 z przekierowaniem | **502** |
| **Scilit** | API i strona | **403** |
| **KCI, DBpia** (Korea) | OpenAPI, strona | klucz / logowanie |
| **Espacenet** | — | **403** (pokryte przez Google Patents i Patentscope) |

`[wniosek]` **CNKI jest największą pojedynczą dziurą** — i tym istotniejszą, że to z literatury chińskiej wyszła praca, która zabiła poprzednie brzmienie twierdzenia. **Jedyna droga: jedno zapytanie z innej sieci.**

---

## 8. Znaczniki pewności — obowiązują w każdym pliku

`[fakt]` — sprawdzone w źródle pierwotnym, z podaniem którego
`[wniosek]` — wyprowadzone z faktów, z widocznym rozumowaniem
`[domysł]` — oszacowanie, z podanym błędem
`[luka]` — wiadomo, że się nie wie

**Każda liczba, na której cokolwiek stoi: 2–3 niezależne źródła.** Jedno źródło — oznaczone przy twierdzeniu, nie w przypisie. **Zgodność trzech streszczeń nie jest weryfikacją.**

**Hierarchia przy sprzeczności:** dokument regulaminowy > publikacja recenzowana > preprint > materiał prasowy > blog.

---

## 9. Reguła, której złamanie kosztowało najwięcej

**Wpis do `KOREKTY.md` nie jest zamknięty, dopóki `grep` po poprawianej liczbie albo frazie nie zwróci samych miejsc poprawionych.**

`[fakt]` Nagrody SDG: błąd zapisano jako **K-059**, a liczba 7 500 zł przetrwała w trzech plikach jeszcze trzy dni. **Rejestr błędów bez poprawki w plikach jest inwentarzem, nie naprawą.**
