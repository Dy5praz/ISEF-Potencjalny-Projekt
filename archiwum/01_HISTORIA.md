# 01 — Historia rozwoju technologii interfejsów neuralnych

**Zakres wg sekcji 10.A handbooka.** Inwazyjne i nieinwazyjne, od początków do sierpnia 2026.

**Status źródłowy całego pliku, zaktualizowany 15 VIII 2026 wieczorem:** kamienie milowe sprzed 2015 są w literaturze wielokrotnie powtórzone i mają status `[fakt]` w sensie „powszechnie ustalone", ale przy dacie rocznej mogą się różnić o rok między źródłami (data eksperymentu vs data publikacji). **Pozycje z linii ear-EEG, oznaczone niżej pogrubionym PMID, mają odczytane abstrakty** i tracą znacznik `[wniosek, streszczenie]`. Reszta pozostaje na indeksie.

---

## 1. Linia nieinwazyjna — EEG

**EEG (elektroencefalografia)** — pomiar różnicy potencjałów elektrycznych na powierzchni skóry głowy, pochodzącej od zsumowanej aktywności milionów neuronów kory mózgowej. Mechanizm w `02_MECHANIZMY.md`.

| Rok | Kto | Kamień milowy |
|---|---|---|
| 1924 (pomiar) / 1929 (publikacja) | Hans Berger, Jena | pierwszy zapis EEG u człowieka. Opisuje rytm alfa. `[fakt]` |
| 1973 | Jacques Vidal, UCLA | **ukuwa termin „brain–computer interface"** i pokazuje sterowanie kursorem z potencjałów wywołanych wzrokowych. Początek dziedziny jako dziedziny. `[fakt]` |
| 1983 | Gratton, Coles, Donchin | metoda regresyjnego usuwania artefaktów ocznych z osobnego kanału EOG. Do dziś w użyciu. Poprzednik: Hillyard i Galambos 1970. **Bezpośrednio istotne dla nas — patrz `04_LUKI_ZAPISANE.md`** |
| 1988 | Farwell, Donchin | **speller P300**: literowanie przez wybieranie migających znaków z matrycy. ~5 liter/min, ~0,5 bit/s. Do dziś punkt odniesienia dla komunikacji nieinwazyjnej `[wniosek, streszczenie]` |
| 1991→ | Pfurtscheller, Graz | paradygmat **wyobrażenia ruchu** oparty na desynchronizacji rytmów sensomotorycznych (ERD/ERS). Druga wielka rodzina paradygmatów obok potencjałów wywołanych |
| 2002 | Wolpaw i in. | *Brain–computer interfaces for communication and control*, Clin Neurophysiol 113:767–791. Praca definiująca pole; **stąd pochodzi wzór na ITR**, do dziś standard. `[fakt]` |
| 2015 | Chen i in., PNAS 112 | **high-speed spelling** SSVEP: do ~60 znaków/min (~12 słów/min) nieinwazyjnie. Górny koniec możliwości EEG w komunikacji `[wniosek, streszczenie]` |

## 2. Linia nieinwazyjna — forma douszna i zauszna

To jest linia, w którą wchodzi projekt użytkownika. Jest **młoda: ma kilkanaście lat.**

| Rok | Kto | Kamień milowy |
|---|---|---|
| 2012 | Looney, Kidmose i in., Imperial College / Aarhus | **koncepcja ear-EEG**: „The in-the-ear recording concept: user-centered and wearable brain monitoring". Pierwsze systematyczne zapisy z kanału słuchowego. `[fakt]` co do istnienia |
| 2012 | ci sami | odpowiedzi słuchowe wywołane z ear-EEG. Kluczowa liczba: zmiana mocy alfa przy zamknięciu oczu wynosi **152% na skalpie i 57% w uchu** `[wniosek, streszczenie, jedno źródło]` |
| 2015 | Debener i in., *Scientific Reports* 5:16743 | **cEEGrid** — dziesięć elektrod nadrukowanych na elastycznej folii w kształcie litery C wokół małżowiny. Dziesięć osób nosiło układ ≥7 h; P300 w paradygmacie oddball powtarzalny między porankiem a popołudniem, rzetelność testu-retestu r ≥ 0,74 `[wniosek, streszczenie]` |
| 2015–2016 | Kidmose i in. | „EEG Recorded from the Ear: Characterizing the Ear-EEG Method" — charakterystyka metody |
| 2016 | Mirkovic, Debener i in., *J Neural Eng* 13:066004 | porównanie cEEGrid z czapką wielokanałową w dekodowaniu uwagi słuchowej |
| **2015** | **Wang Y-T., Nakanishi, Kappel, Kidmose, Mandic i in., EMBC, PMID 26736745** | **pierwszy działający online SSVEP-BCI z ear-EEG.** Cztery klasy, **czterech badanych**: offline 82,7 ± 11,8% (okno 4 s), online 87,9 ± 12,1%, ITR 16,6 ± 6,6 bit/min. `[fakt, abstrakt odczytany]`. **Liczba badanych ma znaczenie — patrz K-031** |
| **2017** | **Kappel, Looney, Mandic, Kidmose, *BioMed Eng OnLine* 16:103, PMID 28800744** | **artefakty fizjologiczne w EEG skalpowym i dousznym, 9 badanych.** Pogorszenie SNR od artefaktów szczękowych **większe w uchu niż na skalpie**, największe w paśmie gamma. **Mrugnięcie NIE wpływa na SNR w uchu**, ruch gałek ocznych — tak. `[fakt, abstrakt odczytany]`. **Zmienia oś projektu — K-026** |
| 2018 | Ahn i in., *Electronics Letters* 54 | nauszny system SSVEP; równolegle prace Nakamury/Mandica nad ear-EEG bezprzewodowym |
| **2021** | **Lee, Shin, Lee, Lee, *Sci Data* 8:315, PMID 34930915** | **pierwszy publiczny zbiór ear-EEG pod paradygmaty sterowania.** 24 osoby, 32-kan. skalp + 14-kan. ear-EEG + EOG + IMU, ERP i SSVEP przy czterech prędkościach ruchu. `[fakt, abstrakt odczytany]`. **Obala twierdzenie z poprzedniej wersji — K-027** |
| **2022** | **Israsena, Pan-Ngum, *Front Comput Neurosci* 16:868642, PMID 35664916** | SSVEP z ear-EEG sieciami konwolucyjnymi na zbiorze publicznym: 69,21% przy treningu grupowym; ITR 6,42 bit/min przy 63,49%, wyłącznie z T7 i T8. `[fakt, abstrakt odczytany]` |
| **2023** | **Wang Z., Shi N. i in., Tsinghua, *Nature Communications* 14:4213, PMID 37452047** | **SpiralE — elektroda douszna o kontakcie konformalnym, rozwijana elektrotermicznie. 95% na 9 celach SSVEP offline; speller 40-celowy SSVEP online BEZ KALIBRACJI; 84% klasyfikacji mowy w cocktail party.** `[fakt, abstrakt odczytany]`. **Najważniejsza pozycja tej tabeli — wywraca tezę o pułapie formy dousznej, K-028** |
| **2024** | **Moumane i in., *Front Neurosci* 18:1441897, PMID 39319310** | ocena jakości sygnału systemu dousznego (elektrody suche, jeden kanał dwubiegunowy) względem 64-kanałowej czapki, **30 osób**: istotna korelacja ze skalpem w ~80% przypadków, amplituda alfy i SNR niższe w uchu. `[fakt, abstrakt odczytany]`. **Poprawka opisu — K-032** |
| 2025 | An i in., **CHI 2025**, DOI 10.1145/3706598.3714185 | **ID.EARS** — jedno ucho, elektrody suche, pięć gestów (mrugnięcia, wink L/P, zaciśnięcie zębów, żucie), >90% dokładności. Odwraca konwencję: EMG/EOG **jako sygnał, nie szum** |
| **2025** | **Ueda i in., *PLoS One* 20(4):e0321107, PMID 40198632** | **desynchronizacja mu wykrywalna z ucha, 20 badanych, pasmo 9–12,5 Hz.** `[fakt, abstrakt odczytany]`. **Zastrzeżenie: badani wykonywali ruch rzeczywisty, nie wyobrażony** — dla sterowania potrzebne jest to drugie i pozostaje `[luka]` |
| 2025 | *Scientific Data* (19 II 2025) | **320 zapisów snu ear-EEG od 30 osób**, otwarty dostęp. Największy publiczny zbiór ear-EEG, jaki znalazłem |
| 2025 | MDPI *Sensors* 25:3321 | przegląd: „The Next Frontier in Brain Monitoring: In-Ear EEG Electrodes and Their Applications" |
| 2026 | Frontiers Neurosci 20:1859327 | **„Signal-specific performance of in-ear EEG"** — 19 osób, douszny suchy vs 32-kanałowy BioSemi. Alfa spoczynkowa wychodzi, **N1-P2 nie** |
| 2026 | Frontiers Hum Neurosci, art. 1793705 | przegląd: ear-EEG a „multimodal embedded intelligence" |

**[wniosek] Wniosek z tej tabeli, ważny strategicznie — i mocniejszy po weryfikacji:** pole jest młode (14 lat), ale **nie jest puste, przyspiesza, i sięga najwyższych czasopism**. Cztery pozycje pochodzą z 2025 i 2026, jedna z Nature Communications, jedna z CHI. Rok temu ktoś opublikował na CHI urządzenie robiące przy uchu to, co użytkownik rozważał jako wariant; trzy lata temu grupa z Tsinghua opublikowała elektrodę douszną, która bije wszystkie wcześniejsze wyniki SSVEP z ucha o rząd wielkości. **Założenie „mało kto tam patrzy" jest fałszywe i było fałszywe także wtedy, gdy pisałem tę tabelę po raz pierwszy** — po prostu nie sprawdziłem.

**[wniosek] Drugi wniosek, którego nie widziałem przed weryfikacją:** postęp w tej linii przyszedł z **materiałów i mechaniki** (SpiralE — kontakt konformalny), a nie z algorytmów. To jest odwrotność wniosku nr 1 z sekcji 5, dotyczącego linii inwazyjnej. **Dla profilu użytkownika z sekcji 1 handbooka jest to wiadomość dobra**: warstwa, w której ostatnio przesunęła się granica w ear-EEG, jest warstwą jego warsztatu.

## 3. Linia inwazyjna i półinwazyjna

**ECoG (elektrokortykografia)** — elektrody na powierzchni kory, pod czaszką, ale bez wnikania w tkankę. **Mikroelektrody wewnątrzkorowe** — igły wbite w korę, rejestrujące pojedyncze neurony.

| Rok | Kto | Kamień milowy |
|---|---|---|
| ~1992–1997 | Richard Normann, Univ. of Utah | **Utah array** — matryca ~100 krzemowych igieł. Standard rejestracji wewnątrzkorowej na dwie dekady, dziś Blackrock Neurotech `[fakt]` |
| 2004–2006 | Hochberg i in., **BrainGate** | Matthew Nagle, pierwszy człowiek z wysokowydajnym interfejsem wewnątrzkorowym: sterowanie kursorem i ramieniem robota z wyobrażonego ruchu ręki. Publikacja Nature 2006 `[fakt]` |
| 2021 | Willett i in., Nature | **pismo odręczne wyobrażone** → tekst, ~90 znaków/min |
| **2023** | **Willett i in., Nature 620** | **proteza mowy: 62 słowa/min**; WER 9,1% przy słowniku 50 słów i 23,8% przy 125 000 słów. Elektrody wewnątrzkorowe |
| **2023** | **Metzger i in., Nature** | ECoG, mediana **78 słów/min**, WER 25,5% przy słowniku 1024 słów |
| 2024 | Card i in., **NEJM 391:609** | „An Accurate and Rapidly Calibrating Speech Neuroprosthesis": 99,6% trafności przy słowniku 50 słów po **30 minutach** kalibracji; 90,2% przy 125 000 słów po dalszych 1,4 h |
| 2022 | Synchron | **Stentrode** — elektroda wprowadzana naczyniowo, bez kraniotomii. Badanie COMMAND: 6 pacjentów, 12 miesięcy, zero poważnych zdarzeń niepożądanych `[wniosek, streszczenie]` |
| I 2024 | Neuralink | pierwszy człowiek (Noland Arbaugh), badanie PRIME |
| 2025–2026 | Neuralink | 12 uczestników (IX 2025) → **21 uczestników (początek 2026)**; ośrodki w USA, Kanadzie, Wielkiej Brytanii i ZEA `[wniosek, streszczenie]` |
| IV 2025 | Precision Neuroscience | **zgoda FDA 510(k)** na rejestrację śródoperacyjną do 30 dni macierzą powierzchniową Layer 7 |
| II 2026 | Precision / Johns Hopkins | sterowanie kursorem w czasie rzeczywistym i klasyfikacja mowy z macierzy powierzchniowej `[wniosek, streszczenie]` |
| 2026 | Synchron | zapowiedź badania rejestracyjnego (pivotal) pod PMA |

**[wniosek] Liczba, która ustawia całą dyskusję o „dorównywaniu inwazyjnym":** jakość sygnału rejestracji inwazyjnej jest **20 do ponad 100 razy lepsza** niż jednoczesnej rejestracji nieinwazyjnej `[wniosek, streszczenie, jedno źródło]`. Szczegóły i rozbiór, co dokładnie ta liczba znaczy — `03_SCIANY_FIZYCZNE.md` sekcja 1.

## 4. Inne modalności nieinwazyjne

| Modalność | Co mierzy | Stan na 2026 |
|---|---|---|
| **MEG** (magnetoencefalografia) | pole magnetyczne prądów neuronalnych | klasyczna wymaga ciekłego helu i ekranowanego pomieszczenia. **OPM-MEG** (magnetometry pompowane optycznie) działa w temperaturze pokojowej i jest noszalna; systemy 80-kanałowe w użyciu, prace nad 384 kanałami. W zadaniu „mind-spelling" trafność **97,7%** `[wniosek, streszczenie, jedno źródło]`. Nadal wymaga ekranowania magnetycznego — **poza zasięgiem projektu** |
| **fNIRS** (spektroskopia bliskiej podczerwieni) | natlenowanie krwi w korze | odpowiedź hemodynamiczna, opóźnienie rzędu **sekund**. Dobre do stanów, złe do szybkiego sterowania |
| **ultradźwięki funkcjonalne (fUS)** | przepływ krwi, rozdzielczość ~100 µm | wymaga okna akustycznego — w praktyce ubytku kostnego. **Nie jest w pełni nieinwazyjne u dorosłego** |
| **sEMG / silent speech** | napięcie z mięśni artykulacyjnych | **AlterEgo** (MIT Media Lab, od 2018): 92% trafności słów w 2018, deklarowane **>100 słów/min** w wersji ciągłej; IP przeniesione do Alterego AI Inc. 21 IV 2025 `[wniosek, streszczenie]`. **To nie jest sygnał mózgowy** |
| **eye tracking** | kierunek patrzenia | punkt odniesienia konkurencyjny: tanie, szybkie, dokładne. Każdy projekt sterowania musi umieć odpowiedzieć, dlaczego nie eye tracking |

---

## 5. Trzy obserwacje z historii, które mają znaczenie dla projektu

**[wniosek] 1. Ostatnie pięć lat postępu w komunikacji BCI to postęp w dekodowaniu, nie w elektrodach.** Utah array z 2023 roku (Willett) to konstrukcyjnie ta sama matryca co u Hochberga w 2006. Skok z „kursor" do „62 słowa/min" zrobiły sieci neuronowe i modele językowe. To jest argument **za** tym, żeby projekt użytkownika nie był czysto sprzętowy — i jednocześnie ostrzeżenie z sekcji 9.4 handbooka, że pole czysto algorytmiczne jest zatłoczone.

**[wniosek] 2. Forma douszna nigdy nie wygrała z czapką w przepustowości i nie po to powstała.** Cała linia z sekcji 2 to prace o wygodzie, długim noszeniu, monitoringu snu i uwagi. **Nikt w tej linii nie obiecuje bicia czapki na ITR.** To jest bezpośrednia wskazówka, jak formułować twierdzenie projektu — patrz `00_STRESZCZENIE.md` sekcja 7 punkt 1.

**[wniosek] 3. Metryka „słowa na minutę" wędruje między pracami bez wspólnej definicji.** 62 wpm Willetta (wewnątrzkorowe, z modelem językowym), 78 wpm Metzgera (ECoG, słownik 1024), >100 wpm AlterEgo (mięśnie, nie mózg), ~12 wpm Chena (EEG, znaki przeliczone na słowa). **Zestawianie ich w jednym rzędzie jest bez sensu** i to jest dokładnie ta pułapka, o której mówi sekcja 10.G handbooka. Rozbiór w `07_DEKODOWANIE.md` sekcja 5.
