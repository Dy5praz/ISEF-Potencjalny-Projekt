# 15 — Nauka dziedziny od zera

**Założony 21 sierpnia 2026 na wniosek autora:** *„poświęćmy ten czas (…) na najzwyczajniej naukę o dziedzinie, bo no jestem zielony. (…) połowy terminów nie kumam (np. co to do cholery Cz??)"*

`[wniosek]` **To jest właściwa decyzja i właściwy moment — przed wydaniem 1 400 zł i przed nauką PCB.** Arkusz ISEF daje **25 punktów na 100 za rozmowę**, w której pytają o *„understanding interpretation and limitations"*. **Nie da się obronić projektu na słowach, których się nie rozumie** — i żadna liczba tego nie nadrobi.

**Zasada tego pliku: każdy termin dostaje wyjaśnienie po polsku, po ludzku, i pokazane jest, GDZIE w tym projekcie występuje.**

---

## 1. Nazwy elektrod — czyli „co to do cholery Cz"

### 1.1 Skąd biorą się te nazwy

`[fakt]` To jest **układ 10–20**, międzynarodowy standard od lat 50. Nazwa bierze się stąd, że elektrody rozstawia się co **10% albo 20%** odległości między punktami na czaszce — **a nie co tyle a tyle centymetrów.** Powód jest prosty: głowy mają różne rozmiary, a procenty skalują się same.

**Trzy punkty odniesienia na czaszce, wszystkie wyczuwalne palcem:**

| Nazwa | Gdzie |
|---|---|
| **nasion** | wgłębienie między czołem a nosem, między brwiami |
| **inion** | **guzek z tyłu głowy**, u podstawy czaszki — namacaj, jest wyraźny |
| punkty przeduszne | tuż przed uszami |

### 1.2 Jak czytać nazwę

**Litera = okolica mózgu:**

| | |
|---|---|
| **F** | frontal — czołowa |
| **C** | central — środkowa |
| **P** | parietal — ciemieniowa |
| **O** | **occipital — potyliczna. Tu siedzi kora wzrokowa i tu jest cały Twój projekt** |
| T | temporal — skroniowa |
| Fp | frontopolar — sam przód czoła |
| **PO** | między P a O |
| **I** | przy inionie |

**Cyfra = strona:** **nieparzysta = lewa** · **parzysta = prawa** · **„z" (od „zero") = linia środkowa**

> ### Czyli: **Cz = Central + linia środkowa = dokładnie czubek głowy.**
> **Oz = Occipital + środek = tył głowy, nad korą wzrokową.**
> **O1 = potyliczna lewa · O2 = potyliczna prawa · POz = między ciemieniową a potyliczną, na środku · Iz = przy samym inionie.**

### 1.3 Łańcuch na linii środkowej — i skąd biorą się Twoje 3,5 cm

Idąc od czoła do tyłu głowy, po środku:

```
nasion → 10% → Fpz → 20% → Fz → 20% → Cz → 20% → Pz → 20% → Oz → 10% → inion
```

Suma: 10+20+20+20+20+10 = **100%**. `[fakt]` Typowy łuk nasion–inion u dorosłego to **~36 cm**, więc 10% ≈ **3,6 cm**.

**POz** leży w rozszerzeniu tego układu **10% powyżej Oz**. **Iz** — 10% poniżej Oz, czyli przy inionie.

> `[wniosek]` **I stąd bierze się cała geometria Twojego urządzenia:**
>
> **Oz → POz = 10% łuku ≈ 3,5 cm** (para „w górę")
> **Oz → Iz = 10% łuku ≈ 3,5 cm** (para „w dół", symetryczna — poprawka K-106)
>
> **Twoja zmienna niezależna to nie „3,5 centymetra". To jeden krok układu 10–20 w górę wobec jednego kroku w dół.** Dlatego zadanie **P35** brzmi „zmierz taśmą własny łuk nasion–inion" — **żeby przeliczyć swoje procenty na swoje centymetry.** Pięć minut, zero złotych, i dopiero po nim wiadomo, ile u Ciebie naprawdę wynosi „3,5 cm".

### 1.4 Elektrody występujące w tym projekcie i u konkurencji

| Nazwa | Gdzie | Gdzie się pojawia |
|---|---|---|
| **Oz** | tył głowy, środek, nad korą wzrokową | **Twoja elektroda główna** |
| **POz** | 3,5 cm nad Oz | **Twój kandydat na odniesienie „w górę"** |
| **Iz** | przy inionie, 3,5 cm pod Oz | **odniesienie „w dół", warunek porównawczy** |
| **O1, O2** | potylica lewa i prawa, ~3,5 cm w bok | kanały czynne, dwa cienkie przewody |
| **Cz** | **czubek głowy** | **odniesienie u Kołodzieja i u Fodora. To jego zysk odkryła reanaliza** |
| Pz | ciemieniowa, środek | odniesienie w pracy PNAS |
| wyrostek sutkowaty | kość za uchem | odniesienie „daleko", ~7 cm |
| małżowina / płatek ucha | ucho | odniesienie w pracy warszawskiej, ~10 cm |

---

## 2. Skąd w ogóle bierze się sygnał

**Neuron pracuje elektrycznie.** Pojedynczy jest za słaby, żeby go z zewnątrz usłyszeć. Ale kora ma **komórki piramidowe ustawione równolegle**, jak włosy uczesane w jedną stronę — i kiedy **miliony z nich robią to samo w tym samym momencie**, ich pola się dodają i sumę da się zmierzyć **na skórze głowy**.

**Trzy konsekwencje, które rządzą całym projektem:**

1. **Sygnał jest mikroskopijny.** EEG to **10–100 µV** (mikrowoltów). Paluszek AA ma 1,5 V, czyli **1 500 000 µV**. **Mierzysz coś dwadzieścia tysięcy razy mniejszego niż bateryjka** — dlatego wzmacniacz jest trudny i dlatego szum toru w ogóle jest tematem.
2. **Czaszka rozmywa.** Kość przewodzi prąd źle, więc ostry obrazek z kory dociera na skórę **rozmazany na kilka centymetrów**. Stąd „gładka plama" i stąd problem: dwie bliskie elektrody widzą prawie to samo.
3. **EEG widzi tylko to, co zsynchronizowane.** Dlatego SSVEP działa tak dobrze: bodziec **wymusza synchronizację** i cała okolica zaczyna „bić" w jego rytm.

**Objętościowe przewodzenie (volume conduction)** — termin, który pada w Twojej dokumentacji: to właśnie ten fakt, że prąd rozpływa się przez tkanki i **elektroda zbiera sumę z okolicy, nie punkt.**

---

## 3. Odniesienie — serce Twojego projektu

### 3.1 Napięcia nie ma. Jest różnica

**To jest najważniejsze zdanie w całej tej dziedzinie:** **nie istnieje „napięcie w punkcie".** Napięcie jest zawsze **różnicą między dwoma punktami**. Woltomierz ma dwie sondy nie przez przypadek.

**Więc każdy kanał EEG to para:** elektroda **czynna** i elektroda **odniesienia** (referencyjna). Zapis „Oz" naprawdę znaczy „Oz **minus** coś".

> `[wniosek]` **I tu jest Twoje twierdzenie w jednym zdaniu: skoro zawsze mierzysz różnicę, to KAŻDY wynik zależy od tego, gdzie postawisz drugą elektrodę. A urządzenie noszone nie ma dokąd jej postawić.**

### 3.2 Trzy słowa, które będą wracać

| Termin | Co znaczy |
|---|---|
| **montaż jednobiegunowy** (monopolarny) | wszystkie elektrody czynne wobec **jednego wspólnego odniesienia**, zwykle daleko (ucho, sutek, czoło) |
| **montaż dwubiegunowy** (bipolarny) | **para obok pary** — każdy kanał to różnica dwóch bliskich elektrod. **To jest montaż zwarty z Twojego projektu**, np. POz−Oz |
| **masa / bias / DRL** | **trzecia** elektroda, która nie mierzy — **ustala potencjał odniesienia całego układu wobec ciała** i tłumi zakłócenia wspólne. DRL = *driven right leg*, nazwa z EKG, gdzie siedziała na prawej nodze. **Cerelog ma ją w pętli zamkniętej** — stąd P34 |

### 3.3 Re-referencing — sztuczka, na której stoi cała reanaliza

`[fakt]` Skoro kanał to różnica, a rejestrujesz **wszystkie** elektrody wobec **jednego** dalekiego odniesienia, to **każdy inny montaż da się policzyć potem, odejmowaniem.**

> (Oz − ucho) − (POz − ucho) = **Oz − POz**

**Ucho się skraca.** Dlatego E2 rejestruje osiem elektrod naraz wobec płatka ucha i **wyprowadza z tego wszystkie warunki offline** — te same próbki, ta sama sesja, zero różnic między sesjami. `[wniosek]` **To nie jest kosmetyka, tylko powód, dla którego pomiar w ogóle ma sens** — inaczej różnica między dniami byłaby większa niż mierzony efekt.

**CAR** (*common average reference*) — inny wariant: odniesieniem jest **średnia ze wszystkich elektrod**. Wymaga wielu elektrod, więc w module z dwiema nie działa — i to jest jeden z powodów, dla których pole jest puste.

---

## 4. SSVEP

**Steady-State Visual Evoked Potential** — potencjał wywołany wzrokowy stanu ustalonego.

**Po ludzku:** patrzysz na coś, co miga **10 razy na sekundę** → Twoja kora wzrokowa zaczyna „bić" **10 razy na sekundę** → widać to w EEG jako **wyraźny prążek przy 10 Hz**.

**Dlaczego to jest genialne do interfejsu:** cztery lampki migają z różną częstotliwością, patrzysz na jedną, a komputer sprawdza, **który prążek urósł**. Nie musi zgadywać, czego chcesz — **zna z góry częstotliwości, których szuka.**

**Terminy, które z tego wynikają:**

| Termin | Znaczenie |
|---|---|
| **f₀ (podstawowa)** | częstotliwość migania, np. 10 Hz |
| **harmoniczne** | **wielokrotności**: 2f₀ = 20 Hz, 3f₀ = 30 Hz. Kora odpowiada też na nie — **i to jest darmowa dodatkowa informacja.** Twój test rozdzielający R12 stoi właśnie na porównaniu f₀ z 2f₀ |
| **entrainment / wciągnięcie** | samo zjawisko podłapywania rytmu przez korę |
| **alfa** | naturalny rytm **8–12 Hz**, silny nad potylicą **przy zamkniętych oczach**. Bywa mylony z SSVEP i dlatego zestaw częstotliwości dobiera się z głową |
| **independent BCI** | interfejs **niewymagający kierowania wzroku** — termin, którego brak w słowniku kosztował ten projekt czwarte „zero trafień" (K-104) |

---

## 5. Od sygnału do liczby

| Termin | Po ludzku | Gdzie u Ciebie |
|---|---|---|
| **próbkowanie / sampling rate** | ile razy na sekundę zapisujesz wartość. Zbiór Kołodzieja: **256 Hz** | `FS = 256.0` w kodzie |
| **twierdzenie Nyquista** | żeby zobaczyć częstotliwość X, musisz próbkować **szybciej niż 2X**. Przy 256 Hz widzisz do 128 Hz — z zapasem | |
| **FFT / widmo** | rozkłada sygnał na **składowe częstotliwości**. Zamiast „napięcie w czasie" masz „ile jest czego" | wykrywanie prążka SSVEP |
| **filtr pasmowy** (bandpass) | przepuszcza tylko wybrany zakres | 20–100 Hz do wykrywania EMG szczęki |
| **filtr zaporowy** (notch) | **wycina 50 Hz z sieci energetycznej** — największe zakłócenie w każdym EEG | |
| **SNR** | **stosunek sygnału do szumu**, w decybelach. O ile prążek góruje nad tłem | „montaż zwarty kosztuje 2,7–3,6 dB" |
| **CCA** | *canonical correlation analysis* — sprawdza, **jak bardzo Twój sygnał pasuje do czystej sinusoidy** o zadanej częstotliwości. Wygrywa ta, która pasuje najlepiej | podstawowa metoda dekodowania |
| **FBCCA** | *filter bank* CCA — to samo, ale **osobno dla f₀, 2f₀, 3f₀**, potem sumuje. **Wykorzystuje harmoniczne, więc bije zwykłe CCA** | metoda główna w `analiza.py` |
| **TRCA** | metoda **uczona na Tobie** — sama znajduje najlepsze wagi dla kanałów. Mocniejsza, ale **wymaga znajomości momentu zapłonu bodźca** | sprawdzona, na tamtym zbiorze niewykonalna |
| **regresja / czyszczenie** | „ile z kanału pomocniczego siedzi w moim sygnale" — i **odjęcie tego** | tym mierzyłeś szczękę i Cz |
| **okno decyzyjne** | ile sekund patrzysz, zanim padnie decyzja. **Dłużej = dokładniej, ale wolniej** | krzywa 0,5–5 s |

---

## 6. Miary — i dlaczego bity, nie procenty

**Dokładność** — ile procent decyzji trafnych. **Bezużyteczna bez podania, ile było celów.**

**Poziom losowy:** przy 3 celach zgadywanie daje **33%**, przy 40 celach — **2,5%**. Dlatego 73% przy trzech celach i 73% przy czterdziestu to **zupełnie różne osiągnięcia.**

**ITR** (*information transfer rate*) — **przepustowość w bitach na minutę**, wzór Wolpawa. Łączy trzy rzeczy naraz: **liczbę celów (N), dokładność (P) i czas na decyzję (t)**.

> `[fakt]` Dlatego praca w *PNAS* z **96,4%** daje **13 bit/min** (bo miała **2 cele**), a układ z **68%** daje **46 bit/min** (bo miał **40**). **To jest cały powód zakazu podawania dokładności bez N.**

---

## 7. Statystyka, której już używasz

| Termin | Po ludzku |
|---|---|
| **p-value** | *„gdyby efektu nie było, jak często sam przypadek dałby wynik tak duży?"* **p = 0,166 znaczy: co szósty raz. Za często, żeby w to uwierzyć.** **Nie znaczy „efekt na 16,6% istnieje"** |
| **istotność** | umowny próg, zwykle p < 0,05 |
| **wielokrotne porównania** | **im więcej testów, tym pewniej coś wypadnie „istotnie" przez przypadek.** Robisz 32 testy przy p < 0,05 → średnio **1,6 fałszywego alarmu** za darmo |
| **Holm–Bonferroni** | poprawka: **zaostrza próg** proporcjonalnie do liczby testów |
| **FDR** | łagodniejsza poprawka: nie „zero fałszywych", tylko „**najwyżej 10% odkryć fałszywe**". Do rodzin eksploracyjnych |
| **moc testu** | szansa, że **wykryjesz efekt, który naprawdę jest**. Standard: 80% |
| **wielkość efektu** | **jak duży** jest efekt — bo „istotny" nie znaczy „duży" |
| **test McNemara** | test dla **par tak/nie na tych samych danych**: „ile okien poprawiło się, a ile popsuło". **Twój test główny** |
| **LOSO** | *leave-one-subject-out*: uczysz na jedenastu osobach, testujesz na dwunastej. **Uczciwy, bo nie testuje na tym, na czym się uczył** |
| **szum selekcji** | wybierasz najlepszy z 63 zestawów **na tych samych danych, na których mierzysz wynik** → wygrywa przypadek. **Dokładnie to zrobili autorzy ze szczęką** |

---

## 8. Sprzęt

| Termin | Po ludzku |
|---|---|
| **ADC / przetwornik** | zamienia napięcie na liczbę. **ADS1299 ma 24 bity** = ponad 16 mln poziomów |
| **wzmacniacz pomiarowy** | wzmacnia **różnicę** dwóch wejść, ignorując to, co wspólne |
| **CMRR** | **jak dobrze ignoruje to, co wspólne** (np. 50 Hz z sieci, które łapią oba przewody). Podaje się w dB, **im więcej tym lepiej**; dobry tor: >100 dB |
| **szum wejściowy** | **jak bardzo tor szumi sam z siebie**, przy zwartym wejściu. Poprzeczka: **0,08 µV RMS** |
| **RMS** | „średnia wielkość" sygnału zmiennego |
| **impedancja kontaktu** | **jak dobrze elektroda trzyma się skóry**. Zła impedancja psuje CMRR — stąd żel |
| **jitter** | **drżenie momentu próbkowania**. Przy SSVEP boli, bo liczy się faza |
| **izolacja galwaniczna** | **brak drogi prądu** między urządzeniem a siecią. **Cerelog jej nie ma na USB** — stąd zakaz laptopa w ładowarce |
| **fotodioda** | czujnik światła — **patrzy na Twoją migającą lampkę i zapisuje, kiedy naprawdę mrugnęła.** Bez tego nie znasz momentu zapłonu, a bez niego nie ma TRCA |

---

## 9. Kolejność nauki i po co Ci co

| # | Blok | Kiedy | Po co konkretnie |
|---|---|---|---|
| **1** | **§1 nazwy elektrod** | **najpierw, jeden wieczór** | bez tego nie rozumiesz własnego twierdzenia |
| **2** | **§3 odniesienie** | zaraz potem | **to JEST Twój projekt** |
| **3** | §4 SSVEP + §6 miary | wrzesień | pierwsze pytanie każdego jurora |
| **4** | **§5 przetwarzanie, w tym FFT** | wrzesień | **żeby uruchomić reanalizę samodzielnie przed preprintem** |
| **5** | §7 statystyka | październik | preprint i obrona liczb |
| **6** | §8 sprzęt | X–XI, przy nauce PCB | projekt płytki |

`[wniosek]` **Bloki 1–2 to jeden wieczór i po nim przestajesz być zielony w tym, co najważniejsze.** Reszta rozkłada się na dwa miesiące i **nie koliduje z niczym.**

---

## 10. Filmy

`[luka]` **Nie oglądałem ich — nie mam takiej możliwości.** Dobierałem po tytule, dacie i renomie kanału. **Jeżeli któryś okaże się słaby, powiedz — wypada z listy.**

### Obowiązkowy, jeden

**3Blue1Brown — „But what is the Fourier Transform? A visual introduction"** (21 min)
https://www.youtube.com/watch?v=spUNpyF58BY

`[wniosek]` **Jeżeli obejrzysz tylko jeden film z tej listy, to ten.** FFT jest narzędziem, na którym stoi całe wykrywanie SSVEP, a ten film tłumaczy je **obrazkami, bez wzorów**, przez nawijanie wykresu na okrąg. Po polsku są napisy automatyczne.

### DIY, czyli to, o co Ci chodziło

**Backyard Brains** — kanał: https://www.youtube.com/user/backyardbrains/videos
Neuronaukowcy robiący eksperymenty w domu, tanim sprzętem, **łącznie z EEG i falą alfa.** Dokładnie duch „nie potrzeba instytutu za milion". Mają też **gotowe opisy eksperymentów** na backyardbrains.com/experiments/eeg — w tym pomiar własnej alfy.

**„Making a Brain Computer Interface in My Garage"** (lipiec 2025)
https://www.youtube.com/watch?v=5YxrpcqkTYA
Ktoś buduje interfejs od zera w garażu. **Najbliższe temu, co Ty robisz.**

**„Controlling Electronics with my Mind! | EEG Brain Computer Interface"**
https://www.youtube.com/watch?v=6iQqklu2fg0
Sterowanie diodami przez EEG — krótkie, konkretne, widać efekt.

### Praktyczne, na później

**sentdex — „Brain Computer Interface w/ Python and OpenBCI"**
https://www.youtube.com/watch?v=Dgo7F-lpyYE
Odczyt EEG w Pythonie. **Do obejrzenia dopiero, gdy będziesz miał Cereloga w rękach** — wcześniej to abstrakcja.

`[wniosek]` **Kolejność: 3Blue1Brown → Backyard Brains → garaż → reszta.** Pierwsze dwa dają fundament, trzeci daje ochotę.
