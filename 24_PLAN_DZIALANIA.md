# 24 — Plan działania krok po kroku

**Założony:** 16 sierpnia 2026
**Zasada prowadzenia:** pozycja zrobiona zostaje **przekreślona**, nie usunięta, i dostaje datę. Nic z tej listy nie znika — dzięki temu widać, ile już zrobiono, i można wrócić do tego, co odpadło i dlaczego.

**Legenda:** `[ ]` do zrobienia · `[x]` zrobione · `[~]` w toku · `[!]` blokuje inne pozycje
**Kto:** **JT** — użytkownik · **AI** — do zrobienia w sesji

---

## Cel nadrzędny — wpisany 16 VIII 2026

**Studia za granicą, najpewniej w Stanach. Explory i ISEF są środkiem, nie celem.** Dorobek (urządzenie + odtwarzalne badanie + preprint) ma ~50–60% i leży pod kontrolą autora; wyjazd na ISEF ~14% i zależy od jury. **Priorytet ustawiać pod dorobek.** ISEF maj 2028 wypada przed aplikacjami jesienią 2028, więc oba zdążą.

**Zasada pracy: zaczynaj od tego, co punktują arkusze oceny, nie od polowania na lukę** (K-075).

---

## Kamień milowy 0 — sierpień 2026 (TERAZ)

- [x] ~~Reanaliza danych Kołodzieja, walidacja pipeline'u wobec publikacji~~ — **16 VIII** · AI
- [x] ~~Zmiana osi projektu, prior art w pięciu bazach~~ — **16 VIII** · AI
- [x] ~~Pięć punktów handbooka §11: projekt, twierdzenie, plan, szanse, ryzyka~~ — **16 VIII** · AI
- [x] ~~Test kanału szczękowego na żądanie użytkownika~~ — **16 VIII** · AI
- [x] ~~Decyzje 5 i 6 (oś: wariant C; przewód odniesienia za ucho: zgoda)~~ — **16 VIII** · JT
- [x] ~~Ocena ConOps drona i ortezy, porównanie, noty~~ — **16 VIII** · AI
- [x] ~~Audyt w bazach wcześniej niedostępnych; oś zajęta od 2005; K-074~~ — **16 VIII** · AI
- [x] ~~Zmiana hierarchii celów i zasady „od arkuszy"; K-075~~ — **16 VIII** · JT + AI
- [ ] **Przeczytać `14_REANALIZA.md` w całości** — reszta dokumentów z niego wynika · JT

---

## Kamień milowy 1 — wrzesień 2026: papiery i zakupy

**Cel etapu: mieć sprzęt w domu i uruchomione procedury formalne przed październikiem.**

### Formalności — wszystkie trzy równolegle, żadna nie czeka na inną

- [ ] **[!] Mail do FZT** (`konkurs@fzt.org.pl`), dwa pytania w jednym: czy organizator prowadzi SRC pełniące funkcję komisji IRB dla polskich uczestników ISEF, oraz czy start w Explory można łączyć z EUCYS · JT
- [ ] **[!] Rozmowa z dyrekcją o komisji IRB.** Skład: nauczyciel inny niż opiekun + dyrektor lub wicedyrektor + pielęgniarka szkolna lub psycholog. **Nie odkładać, nawet jeśli wyda się niepotrzebna** — to jest plan awaryjny na R1 i najdłuższy proces w całym harmonogramie · JT
- [ ] **Pisemna zgoda opiekuna szkolnego** na role Adult Sponsor i Direct Supervisor. Magister wystarcza · JT

### Zakupy — kolejność ma znaczenie

- [ ] **[!] Szukanie używanego Cytona**, budżet do 1 600 zł. Kanały: eBay (filtr „zwroty akceptowane"), OLX, forum OpenBCI, grupy studenckie i koła naukowe na uczelniach technicznych · JT
- [ ] **Mail do `sales@openbci.com`**: czy jest dystrybutor w UE i czy cena dla Polski jest z opłaconym cłem. Jedno pytanie, może skasować 1 000 zł różnicy · JT
- [ ] **Decyzja o platformie do 30 IX.** Jeśli nie ma dobrej oferty używanej — nowy Ganglion, **nie** nowy Cyton · JT
- [ ] elektrody kubkowe Ag/AgCl, pasta przewodząca, panel LED, sterownik, **fotodioda** · JT
- [ ] rezystory 0,1% na dzielnik precyzyjny + generator funkcyjny DDS (280–680 zł) · JT

### Praca merytoryczna

- [ ] **Baza patentów dla nowej osi** — ostatnia nieprzeszukana pozycja, R8 · AI
- [ ] **Dziennik budowy założony od dnia pierwszego** — zdjęcia wersjonowane, także nieudanych · JT

---

## Kamień milowy 2 — październik 2026: PRZESIEW E0

**To jest najważniejszy punkt w całym planie. Rozstrzyga R1 i rozstrzyga, który projekt jest właściwy.**

- [ ] **[!] Uruchomienie platformy, test odbiorczy** — zwarte wejścia, pomiar szumu RMS. Kwadrans. Robić **w dniu dostawy**, żeby ewentualna reklamacja zmieściła się w oknie · JT
- [ ] **[!] E0 — przesiew, ~20 minut** · JT
  - [ ] alfa spoczynkowa: 2 min oczy zamknięte + 2 min otwarte
  - [ ] flash-VEP: ~200 pojedynczych błysków, uśrednienie
  - [ ] krótka próba SSVEP: 3 cele, 60 prób
- [ ] **Rozstrzygnięcie R1 wpisane do `17_RYZYKA.md` z datą i liczbami** · AI
  - próg: poniżej **50%** przy trzech celach **oraz** niska amplituda flash-VEP → uruchamiamy plan awaryjny
- [ ] **Pierwsze własne zapisy z potylicy**, odtworzenie liczby z literatury · JT

### Rozwidlenie po E0

- [ ] **jeśli E0 dobre** → dalej interfejsem, kamień milowy 3
- [ ] **jeśli E0 złe** → decyzja: badanie kogoś innego (wymaga IRB, patrz kamień 1) albo **przejście na ortezę** (`22_POROWNANIE.md` §4.2, `23_NOTY.md` §3.2) · JT

---

## Kamień milowy 3 — listopad–grudzień 2026: nauka PCB i tor B

- [ ] **Nauka projektowania PCB — musi się skończyć przed startem budowy toru**, nie równolegle · JT
- [ ] Pomiar toru kupionej platformy metodą z arXiv 2601.01772 (zwarte wejście, szum RMS) — tabela: nasz szum wobec 0,08 µV RMS · JT
- [ ] Dokończenie toru B na danych publicznych: krzywa dokładność–czas, wybór okna decyzyjnego · AI
- [ ] Projekt płytki v1, zamówienie · JT
- [ ] **[!] Do 31 XII: wybór osi**, jeśli własnych pomiarów nadal nie ma (R11) · JT

---

## Kamień milowy 4 — styczeń–luty 2027: własny tor

- [ ] Montaż i uruchomienie płytki v1 · JT
- [ ] **E1 — charakterystyka toru bez człowieka**: szum RMS, dryf, pasmo, wzmocnienie, kalibracja skali dzielnikiem · JT
- [ ] **Zasób „brat"** — pożyczenie przyrządów na jitter i CMRR powyżej 100 dB. **Zaplanowany właśnie na teraz, nie wcześniej** · JT
- [ ] **[!] 28 II 2027 — ZGŁOSZENIE DO EXPLORY.** Projekt nie musi być ukończony · JT
- [ ] **Wskazanie obszaru Człowiek i Społeczeństwo w formularzu** (cel SDG: 3 albo 10) · JT — **poprawione 18 VIII 2026, K-081.** Stało tu „SDG 9 i obszar Gospodarka i Bezpieczeństwo"; rekomendacja wycofana w `30` §4.3

---

## Kamień milowy 5 — marzec–kwiecień 2027: prototyp

- [ ] Płytka v2 po błędach v1 — **wpisana w plan, nie doproszona** (R7) · JT
- [ ] Obudowa drukowana z żywicy ISO 10993, elektrody suche · JT
- [ ] **Zwolnienie awaryjne i kontrola bezpieczeństwa**: zasilanie wyłącznie bateryjne, brak połączenia z siecią w czasie pomiaru · JT
- [ ] El-Robo-Mech / OITwEiM — dry-run prezentacji · JT
- [ ] Regulaminy El-Robo-Mech XII i OITwEiM sprawdzone, gdy się ukażą · AI

---

## Kamień milowy 6 — maj 2027: START KAMPANII ISEF

**Od tej daty liczy się okno 12 miesięcy (K-023, potwierdzone na trzech rocznikach w K-046).**

- [ ] **E2 — pomiar główny**: odległość odniesienia 2 / 4 / 7 / 10 cm, 8 celów, 240 prób na sesję, 8 sesji w 8 różnych dniach · JT
- [ ] **E3 — rozstaw elektrod czynnych** przy stałym odniesieniu · JT
- [ ] **E5 — metryki użytkowe**: czas montażu, dryf w ciągu dnia, odsetek sesji bez rekalibracji. **Bez wyspania i zmęczenia** — to zmienna ludzka i łamie zwolnienie · JT
- [ ] Kontrola: montaż zwarty zmierzony **fizycznie**, nie tylko wyprowadzony odejmowaniem · JT
- [ ] Hiperparametry klasyfikatora **zamrożone po sesjach 1–2**; sesje 3–8 to zbiór testowy · JT
- [ ] **E4 warunkowo** — kompensacja EMG karku, tylko jeśli użyteczne odniesienie wypadło nad mięśniem. Przewidywanie z góry: efektu nie będzie · JT

---

## Kamień milowy 7 — maj–czerwiec 2027: półfinał Explory

**Wąskie gardło całego lejka: 16% przejścia. Tu wygrywa się albo przegrywa całość.**

- [ ] **Wideo jako produkt pierwszej klasy, nie formalność.** Urządzenie na głowie i działający efekt **w pierwszych dziesięciu sekundach** · JT
- [ ] Plakat wg zasad z ConOps ortezy §10B: **bez wykresów**, zdjęcia, plansza „pokolenia urządzenia", jedna–dwie liczby wyniku · JT
- [ ] Wykresy i tabele **do segregatora na stoisku**, na pytania jurora · JT
- [ ] **Plebiscyt „Bilet na Finał"** — materiał gotowy **pierwszego dnia głosowania**. Próg w 2026: 904 głosy · JT
- [ ] **Ćwiczenie prezentacji.** `23_NOTY.md` §4.1: to jest wyżej punktowana inwestycja niż druga wersja płytki · JT

---

## Kamień milowy 8 — lato–jesień 2027: finał

- [ ] Kampania dokończona, dane kompletne · JT
- [ ] Grupa badanych po powołaniu komisji IRB, 10–15 osób · JT
- [~] **Preprint z reanalizy** — **WSTRZYMANY decyzją użytkownika 16 VIII 2026.** Oznaczony jako **pierwsza pozycja do podjęcia przy powrocie w nowej rozmowie** (`26_PRZEKAZANIE_ETAP3.md` §1). Materiał gotowy w ~80% · JT + AI
- [ ] **20–23 X 2027 — FINAŁ EXPLORY, GDYNIA** · JT

---

## Kamień milowy 9 — listopad 2027 – maj 2028: ISEF

- [ ] Dokumentacja ISEF: Form 4 i pokrewne, Research Plan · JT
- [ ] Wybór kategorii: **EBED**, podkategoria Circuits albo Signal Processing (`13_PODNIESIENIE_SZANS.md` §1) · JT
- [ ] Abstrakt, limit 250 słów, **bez słowa „pierwszy"** (K-044) · JT + AI
- [ ] **Prezentacja po angielsku — 35 punktów na 100** · JT
- [ ] **maj 2028 — ISEF** · JT

---

## Rzeczy stałe, przez cały czas trwania projektu

- [ ] **Monitorowanie konkurencji co dwa miesiące** — PubMed po `Kolodziej M`, `Majkowski A`, plus zapytania o odległość odniesienia · AI
- [ ] **Dziennik budowy** — zdjęcia każdej wersji, w tym nieudanych · JT
- [ ] **Surowe zapisy nigdy nie nadpisywane**, każda sesja z plikiem metadanych · JT
- [ ] **`KOREKTY.md` prowadzony** — każdy złapany błąd dostaje wpis · AI

---

## Pozycje zamknięte — zostają dla historii

- [x] ~~R11: czy użytkownik odrzuca zmianę osi~~ — **wariant C, 16 VIII**
- [x] ~~R8: prior art w Crossref i arXiv~~ — **niezajęte, 16 VIII.** Zostaje baza patentów
- [x] ~~Czy kanał szczękowy uzasadnia oś~~ — **nie, sufit +0,6 pp, p = 0,166**
- [x] ~~Czy TRCA zmienia obraz~~ — **niewykonalne na cudzym zbiorze, faza niezsynchronizowana**
- [x] ~~Ile kosztuje OpenBCI~~ — **1 249 USD za Cyton, K-071**
- [x] ~~Jaki oscyloskop do pomiaru mikrowoltów~~ — **żaden, K-072.** Mierzy własny przetwornik
- [x] ~~Czy orteza i dron są lepsze~~ — **`22_POROWNANIE.md`, `23_NOTY.md`**
- [x] ~~Czy oś trzyma się w bazach, które blokowały~~ — **nie; badana od 2005, K-074**
- [x] ~~Czy zaczynać od luki, czy od arkuszy~~ — **od arkuszy, decyzja użytkownika 16 VIII, K-075**

---

## Trzy rzeczy, które mogą wywrócić ten plan

| Kiedy | Co | Gdzie opisane |
|---|---|---|
| **X 2026** | E0 wypada źle → zmiana projektu albo zależność od IRB | `22_POROWNANIE.md` §4.2 |
| **II–IV 2027** | płytka v1 i v2 nie osiągają użytecznego szumu → pomiary na sprzęcie kupionym | R2 |
| **XI 2026** | własny pomiar rozmija się z przewidywaniem 9–24 pp → twierdzenie odwraca znak | R4 |

**Żadna z nich nie kończy projektu.** Każda ma zapisany plan awaryjny w `17_RYZYKA.md`.
