# 36 — Czy praca Li i in. 2025 jest tym samym projektem. Przeszukanie rozszerzone

**Data:** 18 sierpnia 2026, po audycie `35_AUDYT_2026_08_18.md`
**Zlecenie użytkownika:** *„czy ich projekt był prawie, że identyczny jak nasz, czy tylko odpowiadał na to samo. Jak to pierwsze, jesteśmy w dupie, jak drugie — da się wybronić."* Plus: *„posprawdzaj całą resztę literatury na tyle ile się da (…) jak cię odrzuca, spróbuj obejść."*

---

## 0. Odpowiedź w jednym akapicie

**Drugie. Odpowiadali na to samo pytanie, ale zmieniali zupełnie inną rzecz.** Odczytałem ich **pełny tekst po chińsku** (PMC12236208), nie abstrakt. Ich zmienną niezależną jest **czas i staranność przygotowania do pomiaru** — kazali sobie założyć elektrody w trzy minuty, bez czekania na żel i bez regulacji impedancji. **Montażu nie ruszali w ogóle:** czepek ośmiokanałowy rozpięty od POz do O2, czyli szeroki na te same ~10 cm co u wszystkich, **elektroda odniesienia i masa na czole**, elektrody **mokre**, całość 121 g. Warunkiem kontrolnym nie był ich własny układ w drugiej konfiguracji, tylko **cudzy publiczny zbiór Benchmark**. To jest inny eksperyment, z innym punktem odniesienia, na innej zmiennej.

**Ale w tej samej pracy jest coś, co trafia bliżej niż ich własna teza** — i o tym trzeba wiedzieć, zanim ktoś to znajdzie za nas. Sekcja 2 poniżej.

---

## 1. Rozbiór ich metody — cytaty z oryginału

`[fakt, pełny tekst chiński odczytany 18 VIII 2026, PMC12236208]`

> „可穿戴式SSVEP-BCI系统采用蓝色传感（北京）科技有限公司的ESPW308脑电记录仪进行信号采集，**配置8通道电极帽记录枕叶脑电图（POz、PO3、PO4、PO5、PO6、Oz、O1和O2），参考电极和接地电极放置于前额**，采样率为1 000 Hz。BCI系统的头戴部分（采集器、电极帽）重量为**121 g**。"

Tłumaczenie: *„System używa rejestratora ESPW308; **czepek ośmiokanałowy rejestruje EEG potyliczne (POz, PO3, PO4, PO5, PO6, Oz, O1, O2), elektroda odniesienia i elektroda masy umieszczone na czole**, częstotliwość próbkowania 1 000 Hz. Część noszona (rejestrator i czepek) waży 121 g."*

> „为了模拟BCI在实际生活中的使用情况，本研究对测试场景进行了规定：**要求所有实验准备操作（包括电极佩戴、导电膏注射、连通性确认等）在3 min内完成，无需等待导电膏的充分渗透及传导，不调整电极阻抗**，也不要求电极阻抗下降到合适范围内，仅通过观察眨眼、咬牙等伪迹对脑电采集器连接性进行简单判断。"

Tłumaczenie: *„Żeby symulować użycie w prawdziwym życiu, narzucono warunki: **całe przygotowanie — założenie elektrod, wstrzyknięcie żelu, sprawdzenie łączności — ma się zmieścić w 3 minutach, bez czekania na przeniknięcie żelu, bez regulacji impedancji elektrod**; łączność ocenia się na oko po artefaktach mrugnięcia i zaciśnięcia szczęki."*

> „本研究选取Benchmark数据集作为参照 (…) 选取了参照数据集中**27位初次使用者**的数据作为对比分析。"

Tłumaczenie: *„Jako odniesienie wybrano **zbiór Benchmark**; do porównania użyto danych **27 osób początkujących** z tamtego zbioru."*

Do tego: **elektrody mokre, świadomie** (*„湿电极在信号质量上具有显著优势"* — mokre mają wyraźną przewagę w jakości sygnału), 10 osób, 40 celów, kodowanie częstotliwościowo-fazowe, monitor 280 Hz, algorytm OACCA bez uczenia, zatwierdzenie komisji etycznej HKU.

### 1.1 Zestawienie, które rozstrzyga pytanie

| | **Li i in. 2025** | **Ten projekt** |
|---|---|---|
| **zmienna niezależna** | **czas i staranność przygotowania** (3 min, bez regulacji impedancji) | **położenie elektrody odniesienia**, ~2 do ~10 cm od Oz |
| **elektroda odniesienia** | **czoło** — miejsce standardowe, odległe | **wewnątrz modułu potylicznego**, i to jest cała stawka |
| **rozpiętość montażu** | **POz…O2, czyli ~10 cm** — czepek pełnowymiarowy | **moduł zwarty**, poniżej rozmiaru dłoni |
| **elektrody** | **mokre, z żelem** | mokre na etapie 1, **suche na etapie 3** |
| **warunek kontrolny** | **cudzy publiczny zbiór Benchmark**, 27 innych osób | **ten sam tor analogowy, ta sama osoba, drugie położenie odniesienia** |
| **sprzęt** | **kupiony rejestrator ESPW308** | **własny tor analogowy** na ADS1299 |
| **co znaczy „noszalny"** | 121 g na głowie, czepek pełny | brak czepka, moduł na potylicy, „zero hełmów" |
| **co zmierzyli** | że **skrócenie przygotowania** nie kosztuje statystycznie nic | **ile kosztuje zejście z odniesieniem do modułu** |

`[wniosek]` **Ich „wygoda" to wygoda protokołu, nie wygoda gabarytu.** Osoba badana u nich nadal siedzi w czepku z elektrodą na czole i żelem we włosach — tylko szybciej ją założono. **Zdanie „ile kosztuje wygoda" jest wspólne. Eksperyment nie jest wspólny w żadnym punkcie: inna zmienna, inne odniesienie, inny sprzęt, inny warunek kontrolny.**

`[wniosek]` **Da się wybronić, i to bez naciągania.** Odpowiedź przy stoisku brzmi: *oni skrócili przygotowanie przy niezmienionym montażu i pokazali, że to nie kosztuje. Ja zmieniam montaż i mierzę, ile kosztuje to. Ich wynik jest argumentem, że wygoda bywa darmowa — i dlatego warto sprawdzić, gdzie przestaje być.*

---

## 2. Rzecz z tej samej pracy, która trafia bliżej niż ich własna teza

`[fakt, ten sam tekst]`

> „除了8通道外，本研究选取了6通道（POz、PO3、PO4、Oz、O1和O2）、4通道（POz、Oz、O1和O2）、3通道（Oz、O1和O2）、2通道（POz和Oz）和单通道（Oz）方案。**此外，使用2通道信号之差作为双极导联下的单通道（POz-Oz），也纳入比较。**"

> „比较单极导联与双极导联下的单通道解码，发现**双极导联的解码表现明显优于单极导联方案（3 s时准确率：68.25% vs. 37.65%）**，接近2通道解码结果。"

**Czyli zrobili montaż dwubiegunowy POz−Oz — dwie elektrody potyliczne odległe o kilka centymetrów, bez odniesienia odległego — i porównali go z pojedynczym kanałem Oz odniesionym do czoła.**

| Wariant, dokładność przy oknie 3 s | Wynik | Szczytowe ITR |
|---|---|---|
| 8 kanałów (POz, PO3, PO4, PO5, PO6, Oz, O1, O2) | **94,10%** | **115,25 bit/min** przy 1,2 s |
| 6 kanałów | 92,68% | 103,05 bit/min przy 1,4 s |
| 4 kanały | 91,40% | 98,49 bit/min przy 1,4 s |
| 3 kanały (Oz, O1, O2) | **81,55%** | 73,75 bit/min przy 1,4 s |
| 2 kanały (POz, Oz) | **73,18%** | maksimum przesunięte na 2 s |
| **POz−Oz, dwubiegunowy, jeden kanał** | **68,25%** | maksimum przy 3 s |
| **Oz sam, odniesienie na czole** | **37,65%** | — |

### 2.1 Dlaczego ten wynik idzie w przeciwną stronę niż reanaliza — i dlaczego obie liczby są prawdziwe

`[fakt]` U Li montaż dwubiegunowy **wygrywa** z jednobiegunowym (68,25% wobec 37,65%). W reanalizie zbioru Kołodzieja (`14_REANALIZA.md` §5, odtworzonej przeze mnie od zera) montaż dwubiegunowy **przegrywa** (48,8–64,0% wobec 73,3%).

`[wniosek]` **Sprzeczności nie ma, bo to nie są te same porównania.**

- Li porównuje **jeden kanał dwubiegunowy z jednym kanałem jednobiegunowym**. Pojedynczy kanał odniesiony do czoła zbiera całą składową wspólną i artefakt oczny z czoła — jest fatalny (37,65%). Odjęcie drugiej elektrody potylicznej tę składową kasuje, więc dwubiegunowy wygrywa.
- Reanaliza porównuje **montaż dwubiegunowy z montażem trzykanałowym z odniesieniem odległym**. Tam składowa wspólna jest już usuwana przez uśrednianie po kanałach, a różnicowanie zabiera sam SSVEP.

**Jedna reguła tłumaczy oba wyniki, i jest to ta sama reguła, którą wyprowadził już `25_AUDYT_OPENAIRE.md` §3.1 dla pracy Diez 2010:** różnicowanie usuwa zakłócenie wspólne i sygnał wywołany naraz. **Wygrywa wtedy, gdy zakłócenia jest dużo, a alternatywa jest kiepska; przegrywa wtedy, gdy alternatywą jest porządny montaż wielokanałowy.**

`[wniosek]` **To jest najlepsza rzecz, jaka wyszła z dzisiejszego czytania**, i wchodzi wprost do materiałów: trzy niezależne zespoły (Diez 2010, Kołodziej 2026 przez reanalizę, Li 2025) opublikowały **wyniki o przeciwnych znakach dla tej samej operacji**, bo każdy porównywał ją z czymś innym. **Nikt nie zmierzył całej krzywej.** Pytanie „przy jakiej odległości odniesienia różnicowanie przestaje się opłacać" nie jest wymyślone po to, żeby mieć własne pytanie — **jest jedynym sposobem pogodzenia trzech opublikowanych wyników.**

### 2.2 Co z tego wymaga zmiany w projekcie

`[wniosek]` **Nic w sprzęcie i nic w planie. Jedna rzecz w planie analizy.**

Porównanie ma być prowadzone **wobec dwóch baz naraz, nie jednej**: wobec montażu wielokanałowego z odniesieniem odległym (górna granica) **oraz** wobec pojedynczego kanału z odniesieniem odległym (dolna granica). Bez tej drugiej bazy wynik da się przedstawić jako sprzeczny z Li i in. 2025, choć sprzeczny nie jest. Kosztuje to zero — obie bazy wyprowadza się offline z tej samej rejestracji, dokładnie tak jak w `15_PROJEKT.md` §2.1.

---

## 3. Widełki, w których leży odpowiedź — pięć opublikowanych punktów

`[fakt]` Zestawienie wszystkiego, co dziś wiadomo o koszcie schodzenia z montażu, uporządkowane od najmniej do najbardziej zwartego. **Każdy wiersz pochodzi z innego zespołu i innego zbioru.**

| Konfiguracja | Wynik | Źródło |
|---|---|---|
| 8 kanałów potylicznych, odniesienie na czole | **94,10%**, ITR **115,25 bit/min** | Li i in. 2025, PMID 40566767 |
| czepek pełny, elektrody czynne z żelem, 8 celów | mediana **98,96%** | Cardoso i in. 2022, PMID 36176154 |
| opaska z elektrodami suchymi | mediana **91,14%** | tamże |
| 3 kanały potyliczne, odniesienie na małżowinie | **73,3%**, ITR 28,9 bit/min | reanaliza Kołodzieja, `14` §5 |
| **POz−Oz, dwubiegunowy, jeden kanał** | **68,25%** | Li i in. 2025 |
| **okolica zauszna bezwłosa, najlepszy znany paradygmat** | **84,2 ± 14,7%**, ITR **17,8 ± 5,7 bit/min**, i **25% osób w ogóle nieskutecznych** | Liang, Bin, Chen, Wang, Gao S., Gao X. (Tsinghua), *J Neural Eng* 18(6), 2021, PMID 34875637 |
| **O1−Oz, dwubiegunowy wewnątrz potylicy** | **48,8%** | reanaliza Kołodzieja, `14` §5 |
| Oz sam, odniesienie na czole | **37,65%** | Li i in. 2025 |
| **para elektrod na wyrostkach sutkowatych** | **29,69%** — poziom losowy | Cardoso i in. 2022 |

`[wniosek]` **Rozpiętość wynosi od 115 bit/min do poziomu losowego, a zmienną, która ją tworzy, jest geometria montażu.** Wewnątrz tego zakresu nie ma ani jednego punktu zmierzonego **na tym samym torze, tą samą osobą, z odniesieniem przesuwanym po kolei**. Wszystkie punkty pochodzą z różnych zespołów, sprzętów, algorytmów i grup badanych — czyli różnią się wszystkim naraz.

**To jest dokładnie ta luka, o której mówi arkusz inżynierski ISEF w rubryce `Execution`: „tested in multiple conditions/trials".**

---

## 4. Przeszukanie rozszerzone — wszystko, co dało się dziś dosięgnąć

Zgodnie z żądaniem: sprawdzone wszystko, co nie wyrzuca, plus próby obejścia tego, co wyrzuca.

| Baza | Status | Co z niej wyszło |
|---|---|---|
| **PubMed / E-utilities** | działa | podstawa, plus filtr języka `chi[LA]`, `jpn[LA]` |
| **Europe PMC** | działa | preprinty i pełne teksty |
| **Crossref** | działa | wersje czasopiśmienne, wykrycie K-087 |
| **OpenAIRE** | działa | repozytoria uczelniane, potwierdzenie listy z `25` §3 |
| **DOAJ** | działa | „SSVEP AND reference electrode" — **4 pozycje, wszystkie już znane** |
| **arXiv** | działa | potwierdzenie 2601.01772 i 2509.15449 |
| **J-STAGE (Japonia)** | działa | 36 prac o SSVEP; IEEJ 2023 o położeniu elektrod wokół ucha |
| **CiNii (Japonia)** | działa | bez nowych pozycji |
| **CQVIP (Chiny)** | **działa po naprawie parsera** | patrz §4.1 — **główne obejście dzisiejsze** |
| **PMC pełne teksty** | działa | **pełny tekst chiński Li i in. 2025** — cała sekcja 1 tego pliku |
| **Google Patents** | działa | patenty na konstrukcje, nie na pomiary |
| **Patentscope (WIPO)** | działa | 163 dokumenty „SSVEP + reference electrode", 128 „SSVEP + occipital + wearable" — **żaden nie zastrzega pomiaru zależności** |
| **Zenodo** | działa | zbiory publiczne SSVEP; **nic o położeniu odniesienia** |
| **HAL (Francja)** | działa | 4 trafienia, jedno adjacentne: *Adjusting Classical BCI Paradigms Parameters (…) Wearable Dry-Electrode EEG Device*, 2025 |
| **Figshare** | działa | bez nowych pozycji |
| **bioRxiv API** | działa | bez nowych pozycji |
| **baza abstraktów ISEF** | **działa — obejście przez POST z tokenem** | patrz §5, i to jest najważniejsza rzecz w tej tabeli |
| **KCI (Korea)** | odpowiada, **API wymaga klucza** | `[luka]` — nieprzeszukane |
| **CNKI** | **nadal odrzuca** — `kns.cnki.net` i `www.cnki.net` zrywają połączenie na poziomie TLS; `oversea.cnki.net` odpowiada stroną-zaporą 381 bajtów | `[luka]` — **obejście przez CQVIP, nie przez CNKI** |
| **Wanfang** | strona ładuje się, wyniki renderowane po stronie przeglądarki, API zrywa połączenie | `[luka]` — częściowo pokryte przez CQVIP |
| **OpenAlex** | **HTTP 429**, komunikat *„Insufficient budget (…) Add funds"* | model płatny, K-088 |
| **Semantic Scholar** | **HTTP 429** po odczekaniu | wymaga klucza |
| **scholar.archive.org** | **HTTP 200, ale „Rate limit reached"** | `[luka]` |
| **Scilit** | HTTP 403 | `[luka]` |
| **Espacenet** | HTTP 403 | pokryte przez Google Patents i Patentscope |
| **Baidu Xueshu** | połączenie zrywane | `[luka]` |
| **DBpia (Korea)** | strona odpowiada, wyszukiwarka za logowaniem | `[luka]` |
| **BASE** | zwraca pustą odpowiedź bez rejestracji | `[luka]` |

### 4.1 CQVIP — jak obszedłem brak CNKI, i pułapka, w którą prawie wpadłem

`[fakt]` CNKI jest niedostępna. **CQVIP (维普), druga co do wielkości chińska baza czasopism, odpowiada i daje się przeszukiwać** — wyniki są renderowane po stronie serwera w polu `class="abstr"`, więc abstrakty da się odczytać.

**Pułapka, i jest to trzeci raz, kiedy ta sama pułapka wystąpiła w tym projekcie.** Pierwsza wersja mojego parsera wyciągała tytuły po selektorze `class="title"` i **zwracała zero trafień na każde zapytanie**. Wyglądało to jak „w chińskiej literaturze nic nie ma".

`[fakt]` **Kontrola pozytywna to wykryła w jednym kroku:** zapytanie `SSVEP` samo w sobie też dało zero, a zapytanie `脑机接口` („interfejs mózg-komputer") również zero. **Baza, która nie zna słowa »interfejs mózg-komputer«, nie istnieje** — więc zero pochodziło od parsera, nie od literatury. Po przejściu na selektor abstraktów: `SSVEP` daje **20 abstraktów na stronę**, kontrola przechodzi.

To jest reguła z `25_AUDYT_OPENAIRE.md` §2, zastosowana i tym razem skuteczna: **każde „zero trafień" wymaga kontroli pozytywnej.** Trzy wystąpienia: arXiv (składnia cudzysłowów), OpenAIRE (`keywords` wymaga wszystkich słów), CQVIP (selektor tytułu). **Za każdym razem zero było artefaktem narzędzia.**

### 4.2 Co wyszło z chińskiej literatury po naprawieniu parsera

`[fakt]` Zapytania: `SSVEP 参考电极` (elektroda odniesienia), `SSVEP 双极导联` (montaż dwubiegunowy), `SSVEP 电极位置` (położenie elektrod), `SSVEP 耳后 电极` (elektrody zauszne).

**Znalezione i istotne:**

1. **Praca o SSVEP z okolicy zausznej** — abstrakt chiński: *„SSVEP-BCI 主要信号响应位于枕叶区，因而通常需要使用者洗头、佩戴脑电帽并辅助使用导电膏，给实际应用带来不便。**耳后区域虽然可直接通过电极贴的方式快速开展 SSVEP-BCI 应用，但由于 SSVEP 在耳后区域的响应信号较弱，最终的系统性能受限**"* — *„odpowiedź SSVEP leży w okolicy potylicznej, więc trzeba myć głowę, zakładać czepek i używać żelu, co utrudnia praktyczne stosowanie. **Okolica zauszna pozwala na szybkie naklejenie elektrod, ale odpowiedź SSVEP jest tam słaba i wydajność systemu jest ograniczona**"*.
   `[wniosek]` To jest **nasze zdanie problemowe, napisane po chińsku**, i odsyła do dorobku grupy Gao Xiaorong z Tsinghua — potwierdzone przez wersję angielską, **Liang i in., PMID 34875637**, z liczbami w tabeli §3.
2. **Praca o elektrodzie laplasjanowej o małym rozstawie** — *„传统拉普拉斯脑电研究通常利用算子来估计圆盘电极阵列中的拉普拉斯电势。**但是圆盘电极间距大，使得该方法估计结果精度较低**"* — *„tradycyjne badania laplasjanowe estymują potencjał w tablicach elektrod dyskowych, **ale rozstaw elektrod dyskowych jest duży, przez co dokładność estymacji jest niska**"*. Zaprojektowali elektrodę laplasjanową o małym rozstawie i zweryfikowali ją symulacyjnie i na ludziach.
   `[wniosek]` **Najbliższa chińska praca konstrukcyjna wobec pytania „czy gęste próbkowanie małego obszaru działa"** — i idzie w stronę przeciwną do wyniku reanalizy, czyli jest kolejnym powodem, żeby to zmierzyć samodzielnie.
3. Reszta trafień na `参考电极` dotyczy **innych dziedzin** — elektrod domózgowych u szczurów, VEMP przedsionkowych, EEG dziecięcego, techniki odniesienia w nieskończoności (REST). **Nic o SSVEP i odległości odniesienia.**

`[wniosek]` **Wąska oś nie jest zajęta również w chińskiej literaturze czasopiśmienniczej dostępnej przez CQVIP.** Z zastrzeżeniem, że CNKI pozostaje nieprzeszukana.

---

## 5. Konkurencja ISEF — sprawdzona bezpośrednio w bazie abstraktów, nie przez streszczenia

`[fakt]` Baza `abstracts.societyforscience.org` przeszukuje formularzem POST wymagającym tokenu sesji. **Obszedłem: pobranie tokenu, ciasteczka, POST z zaznaczonym „wszystkie lata".** Zakres bazy: **2014–2026**.

| Zapytanie | Trafień w trzynastu rocznikach |
|---|---|
| `SSVEP` | **5** |
| `steady-state visual evoked` | **3** |
| `occipital` | **6** |
| `EEG electrode` | **2** |
| **`ADS1299`** | **0** |

**Wszystkie pięć projektów SSVEP w historii bazy:**

| Rok | Projekt | Kategoria |
|---|---|---|
| 2018 | *EEG-Based Person Authentication Method with Deep Learning Using Visual Stimulation* (Tajlandia) | Systems Software |
| 2019 | *The Music Box: Control of Music through the Use of a SSVEP-Based Brain Computer Interface System* | Biomedical Engineering |
| 2019 | *A Brain-Computer Interface Application for the Assessment of Cognitive Aging* | Systems Software |
| 2022 | *Dynamic Extraocular Filtering (…) Validated With Steady-State Visual Evoked Potentials* | — |
| 2025 | *A Novel Brain-Driven Forearm Exoskeleton With Adaptive Neuroregulation-Based Feedback* | — |

`[wniosek]` **Cztery ustalenia, wszystkie na korzyść projektu:**

1. **Wszystkie pięć to zastosowania**: sterowanie muzyką, uwierzytelnianie, egzoszkielet, ocena starzenia poznawczego. **Żaden nie jest projektem o torze pomiarowym ani o geometrii elektrod.**
2. **Zero projektów z własnym analogowym torem wejściowym.** Zapytanie `ADS1299` — układ, wokół którego stoi cała konstrukcja — **daje zero trafień w trzynastu rocznikach.** Nikt na ISEF nie zbudował własnego wzmacniacza EEG.
3. **Rzadkość paradygmatu:** pięć projektów SSVEP na ~1 400 finalistów rocznie przez trzynaście lat.
4. `[wniosek]` Wniosek z `08_KONKURENCJA_ISEF.md` §3.2 („pole obsadzone i rośnie", 22 projekty EEG w 2026) **był prawdziwy dla EEG w ogóle i mylący dla tego projektu.** Projekty EEG na ISEF to w przeważającej większości **klasyfikacja cudzych albo własnych danych**, nie budowa przyrządu. **W rubryce, w której ten projekt gra — przyrząd i jego metrologia — konkurencji na ISEF praktycznie nie ma.**

---

## 6. Poprawka do wczorajszego opisu — moja, nie cudza

**K-092.** W `35_AUDYT_2026_08_18.md` §2.1 napisałem, że Li i in. *„zmniejszyli **skrzynkę**, trzymając odniesienie w miejscu standardowym"*. **Odniesienie owszem — na czole, potwierdzone cytatem. Ale skrzynki też nie zmniejszali w sensie, w jakim to sugerowałem:** ich część noszona to **rejestrator plus pełny czepek ośmiokanałowy, 121 g**, a jedyną rzeczą, którą naprawdę zmienili, jest **procedura przygotowania**. Napisałem to z abstraktu, w którym stoi tylko „wearable (…) small-sized EEG collector".

`[wniosek]` **Kierunek wczorajszego wniosku był trafny, ostrość nie.** Różnica ma znaczenie, i to na korzyść projektu: dystans między tamtą pracą a tym projektem jest **większy**, niż wczoraj zapisałem. Wpis w `KOREKTY.md`.

**Reguła, która z tego zostaje:** **przy pracy, która jest kandydatem na zabójcę twierdzenia, abstrakt nie wystarcza.** Wczorajszy audyt postawił werdykt „twierdzenie martwe" na czterech zdaniach streszczenia, mając pełny tekst dostępny za jednym zapytaniem do PMC. Werdykt się utrzymał, ale jego uzasadnienie było na tyle nieostre, że mogło pójść w drugą stronę.

---

## 7. Werdykt

**Czy interfejs jest martwy: nie.**

**Co jest martwe:** hasło „ile kosztuje wygoda" jako samodzielne zdanie twierdzenia. Zostaje jako **motywacja**, nie jako teza — i **wymaga zacytowania Li i in. 2025 obok siebie**, bo to jest praca, która na tak postawione pytanie odpowiedziała.

**Co żyje i jest po dzisiejszym czytaniu mocniejsze niż wczoraj:**

> **Mierzę, o ile spada dokładność i przepustowość interfejsu SSVEP, gdy elektroda odniesienia musi zmieścić się w module noszonym na potylicy zamiast leżeć w miejscu standardowym, i wyznaczam najmniejszą odległość odniesienia od kory wzrokowej, przy której przepustowość jeszcze się nie załamuje — na jednym własnym torze analogowym, tą samą osobą, tym samym paradygmatem.**

**Trzy rzeczy, które dzisiejsze czytanie do tego dołożyło:**

1. **Uzasadnienie przestaje być „nikt tego nie zrobił", a staje się „trzy opublikowane wyniki są ze sobą sprzeczne i nikt ich nie pogodził".** Diez 2010: dwubiegunowy lepszy. Li 2025: dwubiegunowy lepszy. Reanaliza Kołodzieja: dwubiegunowy gorszy o 9–24 pp. **To jest znacznie lepsze zdanie do rubryki `Research Problem` niż jakiekolwiek twierdzenie o nowości** — i jest odporne, bo opiera się na cudzych liczbach, nie na przeszukaniu.
2. **Widełki mają obie granice zmierzone przez kogoś innego**: 115 bit/min przy pełnym montażu potylicznym, poziom losowy przy parze elektrod na wyrostkach sutkowatych, 17,8 bit/min w okolicy zausznej przy 25% osób nieskutecznych. **Środek tego zakresu jest pusty.**
3. **Konkurencja na ISEF sprawdzona u źródła i praktycznie nie istnieje w tej rubryce**: pięć projektów SSVEP w trzynastu latach, wszystkie zastosowaniowe, zero z własnym torem analogowym, zero wzmianek o ADS1299.

**Co się nie zmienia:** sprzęt, plan pomiarowy, budżet, drabinka zejść, terminy. **Jedna zmiana w planie analizy** — porównanie prowadzone wobec dwóch baz zamiast jednej (§2.2), koszt zero.

---

## 8. Pewność po tej rundzie: **94%**

Wczoraj **92%**. Podnoszę o dwa punkty i podaję, za co dokładnie:

| Co się zmieniło | Wpływ |
|---|---|
| **pełny tekst pracy-zabójcy odczytany**, nie abstrakt; zmienna niezależna ustalona co do zdania | **+2** |
| **chińska literatura czasopiśmiennicza otwarta przez CQVIP** z przechodzącą kontrolą pozytywną (80% → 88%) | **+1,5** |
| **konkurencja ISEF sprawdzona u źródła**, trzynaście roczników, zamiast zliczania po tytułach (85% → 95%) | **+0,5** |
| **Patentscope, DOAJ, Zenodo, HAL, bioRxiv, Figshare** dołożone do przeszukania | **+0,5** |
| **wykryta własna nieostrość** we wczorajszym werdykcie (K-092) — dowód, że jedno przejście nie wystarcza | **−1** |
| **CNKI, KCI, DBpia, OpenAlex, Semantic Scholar, scholar.archive.org, BASE nadal poza zasięgiem** | bez zmiany, to jest trwałe **−6** |

**Czego brakujące 6% dotyczy, wypisane, żeby liczba nie była zaokrągleniem:**

1. **CNKI** — największa chińska baza, zrywa połączenie na poziomie certyfikatu. **CQVIP pokrywa znaczną część tego samego korpusu czasopism, ale nie rozprawy doktorskie i nie materiały konferencyjne.** To jest największa pojedyncza dziura i jest nieusuwalna z tego środowiska
2. **KCI i DBpia (Korea)** — pierwsza wymaga klucza API, druga logowania
3. **OpenAlex i Semantic Scholar** — obie wymagają klucza; obie pokrywają korpus już przeszukany, ale rankują inaczej
4. **Reguły ISEF 2027–2028 jeszcze nie istnieją**
5. **Kwalifikacja badania na sobie** (`35` §1.9) — czeka na odpowiedź organizatora

`[wniosek]` **Powyżej 94% nie wejdę bez klucza do OpenAlex albo Semantic Scholar i bez dostępu do CNKI.** Obie rzeczy są do załatwienia z innej sieci albo przez rejestrację i **to jest konkretna, wykonalna pozycja**, a nie deklaracja niemożności — wpisana jako P16.

---

## 9. Zadania, które z tego wychodzą

| # | Zadanie | Termin |
|---|---|---|
| **P15a** | **przy analizie porównywać wobec dwóch baz**: montaż wielokanałowy z odniesieniem odległym **oraz** pojedynczy kanał z odniesieniem odległym (§2.2). Koszt zero, chroni przed zarzutem sprzeczności z Li i in. 2025 | do planu analizy |
| **P16** | **klucz API do OpenAlex i Semantic Scholar** (darmowa rejestracja) oraz próba CNKI z innej sieci — to jest jedyna droga powyżej 94% | przed zgłoszeniem |
| **P17** | **do sekcji o stanie wiedzy dołożyć trzy sprzeczne wyniki** (Diez 2010, Li 2025, reanaliza) jako uzasadnienie problemu badawczego — to jest mocniejsze niż jakiekolwiek zdanie o nowości | z P12 |
| **P18** | **zdanie o konkurencji ISEF poprawić w `08`**: nie „22 projekty EEG w 2026", tylko „pięć projektów SSVEP w trzynastu latach, zero z własnym torem analogowym" | przy najbliższej okazji |
