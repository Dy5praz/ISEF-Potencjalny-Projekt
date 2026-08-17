# 24 — Kandydaci odrzuceni przy wyborze projektu

**Data:** 17 sierpnia 2026
**Po co:** żeby nikt — łącznie ze mną w następnej sesji — nie zaproponował tego ponownie bez nowego argumentu. Ten plik pełni tę samą rolę co sekcja 7 handbooka dla poprzednich kierunków.

**Metoda:** każdy kandydat sprawdzony w stanie techniki **zanim** cokolwiek na nim zbudowałem. To jest bezpośrednia konsekwencja błędu nr 5 z sekcji 8 handbooka — założenia luki zamiast jej sprawdzenia.

---

## 1. Akustyczna kamera do wykrywania nieszczelności sprężonego powietrza

**Pomysł:** tablica mikrofonów MEMS + beamforming + kamera; lokalizacja i kwantyfikacja nieszczelności w instalacjach sprężonego powietrza.

**Motywacja była mocna** — `[fakt]` wg Departamentu Energii USA i Compressed Air Challenge nieszczelności marnują **20–30% wydajności sprężarki**; w źle utrzymanych zakładach 35% i więcej.

**ODRZUCONY.** `[fakt]` Fluke ma **opublikowaną metodę Leak Rate Quantification** dla kamer akustycznych, z whitepaperem, opartą na klasyfikacji typu nieszczelności i dopasowaniu sygnatury do danych laboratoryjnych. Do tego w 2025 ukazała się praca *„Development and testing of a low-cost ultrasonic leak detector"*, a kwantyfikacja przez ultradźwięk i termografię jest opisana wcześniej. Komercyjnie: Fluke ii900, FOTRIC TD2e (64 mikrofony), HIKMICRO AI76 (136), CRYSOUND (200).

**Co by zostało: „taniej".** To nie jest twierdzenie naukowe — dokładnie ten sam powód, dla którego padła orteza kolanowa (handbook sekcja 7).

**Co warto zapamiętać z tej ścieżki:** `[fakt]` powyżej ~3 bar nadciśnienia poziom ultradźwięku nasyca się mimo rosnącego przepływu. Ładne ograniczenie fizyczne, przydatne gdzie indziej.

---

## 2. Charakteryzacja rozrzutu fazowego tanich mikrofonów MEMS w paśmie ultradźwiękowym

**Pomysł:** zmierzyć amplitudę i fazę tanich mikrofonów PDM w paśmie 20–80 kHz, użyć kalibracji per-egzemplarz do poprawy beamformingu.

**ODRZUCONY na dwóch niezależnych podstawach.** `[fakt]` Politechnika w Eindhoven opublikowała *„Characterization of MEMS microphone sensitivity and phase distributions with applications in array processing"* — z liczbami: przedziały ufności 95% wynoszą ±0,39 dB dla czułości i ±0,82° dla fazy. `[fakt]` Przesłanka „tanie mikrofony poza specyfikacją" też pada: TDK/InvenSense sprzedaje katalogowo mikrofony **ICS-41350 (do 40 kHz)** i **ICS-41352 (do 85 kHz)**.

---

## 3. Fototermiczna identyfikacja czarnych tworzyw sztucznych

**Pomysł był najlepszy z całej listy i dlatego opisuję go najdokładniej.** Sortowniki NIR nie widzą czarnych tworzyw, bo sadza pochłania promieniowanie bliskiej podczerwieni — czarne opakowania idą na składowisko. Odwrócenie problemu: oświetlić modulowanym światłem i patrzeć, **jak szybko ciepło się rozchodzi**. Różne polimery mają różną dyfuzyjność cieplną, a sadza, która psuje metodę optyczną, **pomaga metodzie cieplnej**, bo zapewnia równomierne pochłanianie.

**Problem jest realny i udokumentowany** `[fakt]`: sadza pochłania NIR, czarne tworzywa są niewidoczne dla sorterów optycznych i trafiają na składowiska albo do spalarni. Kierunki badane przez innych: MWIR 3–5 µm (hiperspektralnie), photon up-conversion, spektroskopia THz z uczeniem maszynowym, oraz pigmenty wykrywalne w NIR.

**ODRZUCONY.** `[fakt]` **Fraunhofer IZFP robi dokładnie to.** *„Active thermography enables black plastic sorting"* — RECYCLING magazine, 4 III 2026: taśma, grzejnik promiennikowy, kamera termowizyjna, sieć neuronowa. Materiał K-online opisuje to samo. **14 VIII 2026 — trzy dni przed tą sesją — ukazała się informacja o wejściu tej technologii w próby przemysłowe.**

**Powód odrzucenia nie brzmi „zajęte".** Twierdzenie dałoby się postawić pomiarowo i przeżyłoby audyt. Powód brzmi: **juror wpisze hasło w wyszukiwarkę i w trzydzieści sekund znajdzie instytut Fraunhofera z tym samym nagłówkiem i świeższą datą.** To jest zła pozycja na rozmowę wartą 25 punktów.

---

## 4. Jednopikselowy obrazowacz SWIR (DMD + fotodioda InGaAs + compressed sensing)

**Pomysł:** zastąpić matrycę SWIR za 200 000 zł jedną fotodiodą i modulatorem przestrzennym; zastosowanie — identyfikacja tworzyw.

**ODRZUCONY, choć budżetowo się spinał.** `[fakt]` Fotodiody InGaAs są tanie (Hamamatsu G6854-01 ~77 GBP, G9820 ~62 GBP). `[fakt]` Ale technika jest opublikowana (*Single Pixel SWIR Imaging using Compressed Sensing*; *Dual Single Pixel Imaging in SWIR*, 2020), modulatory DMD w wersji NIR są **produktem katalogowym Texas Instruments** (DLP2010NIR, DLP4500NIR), a sortowanie SWIR tworzyw jest komercyjne (Specim).

**Dodatkowo ryzyko wykonawcze wysokie:** justowanie optyki plus wzmacniacz transimpedancyjny małoprądowy to dwie nowe dziedziny naraz, żadna nie jest mocną stroną użytkownika.

**Ciekawostka techniczna do zapamiętania** `[fakt]`: odbicie od DMD w bliskiej podczerwieni ma silną zależność kierunkową przez dyfrakcję — jest o tym praca w *Applied Optics* z 2026 wraz z metodą łagodzenia filtrami germanowymi.

---

## 5. Tablica magnetometrów do diagnostyki ogniw litowo-jonowych

**ODRZUCONY.** `[fakt]` Pole zajęte i dobrze finansowane: przegląd w *Advanced Energy Materials* (2025), praca o skalowalnym mapowaniu pola dla ogniw pouch z tablicą 4×4 (*Applied Sciences*, 2026), patent US 12276703, oraz grupy pracujące magnetometrami pompowanymi optycznie. Konkurencja dysponuje sprzętem, którego licealista nie kupi.

---

## 6. Enkoder indukcyjny na płytce drukowanej

**ODRZUCONY jako oś projektu.** `[fakt]` Komercja dojrzała (Renishaw: dokładność ±40 sekund kątowych przy 23 bitach), akademia ma prototypy PCB (12,8 µm w obrębie jednej podziałki, rozdzielczość 0,7 µm), a otwartoźródłowo istnieje enkoder pojemnościowy o dokładności rzędu 1 stopnia. Zostaje „taniej". Demonstracja przy stoisku: żadna.

**Nie jest całkiem martwy** — technika pomiaru indukcyjnego wróciła do projektu jako **czujnik położenia w wybranym stanowisku**, gdzie jest narzędziem, a nie twierdzeniem.

---

## 7. Wniosek metodyczny, ważniejszy od samej listy

Sześciu kandydatów padło, bo szukałem **nieobsadzonego problemu**. To jest błąd strukturalny: **problemy ważne ekonomicznie są z definicji obsadzone**, bo ważność ekonomiczna przyciąga finansowanie.

Kształt, który przeżył audyt w poprzednim projekcie, był inny:

> **znany problem + znane rozwiązanie + konkretna wariacja inżynierska, której efektu nikt nie zmierzył, porównywana wewnętrznie: mój układ z X wobec mojego układu bez X.**

`[fakt]` Arkusz inżynierski ISEF **nie ma kryterium nowości względem literatury**; regulamin Explory §7 pkt 2a dopuszcza alternatywę *„innowacyjny **i/lub** wnosi dodatkową wartość"*.

**Wybrany projekt (`20_PROJEKT.md`) jest zbudowany w tym kształcie i został wybrany na kryteriach, które faktycznie punktują — wykonalność, demonstracja, głębokość pomiaru, obsada kategorii, podział na dwa pytania — a nie na nowości.**
