# 34 — Parametry projektu, budżet, drabinka zejść

**Data:** 18 sierpnia 2026
**Status:** obowiązujący. **Zastępuje pliki `20`–`23`**, które opisywały zamknięty kierunek łożyskowy i zostały usunięte z repozytorium (historia w gicie, commit `820a0b4` i wcześniejsze).

---

## 1. Cztery decyzje użytkownika z 18 VIII 2026

| # | Decyzja | Treść |
|---|---|---|
| 1 | **budżet** | **8 000 zł** na cały projekt |
| 2 | **czas** | **10 godzin tygodniowo** |
| 3 | **kategoria ISEF** | **EBED** — Embedded Systems. Uzasadnienie użytkownika: łatwiejsza obsada niż ENBM, a projekt **nie jest sprzedawany jako urządzenie medyczne**, więc ENBM byłoby trudniejsze do obrony |
| 4 | **poprzeczka wykonania** | **„gotowy w całości, nie prototyp"** (`30` sekcja 6a.4) — **to jest cel, nie życzenie.** Potwierdzone wprost |

**Wszystkie cztery są wiążące i nie wymagają ponownego pytania.** Pozycja „parametry `[luka]`" z `CLAUDE.md` jest tym samym zamknięta.

**Uwaga o pochodzeniu liczby 8 000:** w plikach repozytorium nigdy nie było kosztorysu dla interfejsu. Jedyne kwoty, jakie istniały, to **9 900 zł z zamkniętego kierunku łożyskowego** i **15 000 zł** wspominane jako „rząd wielkości wyobrażalny" z porzuconego projektu drona (`00_PYTANIA_I_LUKI.md` B1). `[fakt]` **Żaden plik nie został z repozytorium usunięty przed 18 VIII 2026** — sprawdzone poleceniem `git log --diff-filter=D`, wynik pusty. Liczba 8 000 pochodzi więc z rozmowy, nie z pliku, i od teraz jest zapisana tutaj.

---

## 2. Co daje 10 godzin tygodniowo — godziny do kamieni milowych

`[wniosek]` Licząc od 18 VIII 2026, bez odliczania przerw:

| Kamień milowy | Termin | Tygodnie | **Godziny** |
|---|---|---|---|
| zgłoszenie do Explory 2027 | 28 II 2027 | ~27 | **~270 h** |
| El-Robo-Mech XII, finał | ~IV 2027 | ~34 | ~340 h |
| półfinał Explory | V–VI 2027 | ~38 | **~380 h** |
| finał Explory | X 2027 | ~61 | ~610 h |
| **ISEF 2028** | V 2028 | ~90 | **~900 h** |

`[wniosek]` To jest zgodne z oszacowaniem z `11_OCENA_SZANS.md` (~350 h do wiosny 2027, ~610 h do finału, ~910 h do ISEF) — **czyli plan godzinowy się spina**, ale bez marginesu.

**Poprawka realistyczna:** z tych liczb trzeba odjąć rzędu **10–15%** na sesje egzaminacyjne, wyjazdy i tygodnie stracone. Do planowania używać **~230 h do zgłoszenia i ~330 h do półfinału**.

---

## 3. Budżet 8 000 zł — kolizja, którą trzeba rozstrzygnąć przed zakupami

`[fakt]` **OpenBCI Cyton kosztuje 1 249 USD** (zestaw: płytka, dongle USB, akumulator, etui; **elektrody nie są w zestawie**). Producent podaje, że do Europy dochodzi **cło i VAT rzędu 25%**.

`[wniosek]` Po przeliczeniu przy kursie 3,7137 zł/USD: **~4 640 zł za samą płytkę, ~5 800 zł z cłem i podatkiem**, bez elektrod i bez przesyłki.

> **To jest 58–72% całego budżetu na jeden kupiony przyrząd odniesienia.**

Pozycja P5 z README („kupić **oryginalnego** Cytona, nie klon") i decyzja o budżecie 8 000 zł **nie spinają się razem**. Trzy wyjścia, wszystkie do rozstrzygnięcia w audycie:

| Wyjście | Co daje | Co kosztuje |
|---|---|---|
| **A. Cyton wypada z projektu** | budżet wraca do 8 000 zł na budowę | traci się **zewnętrzny** punkt odniesienia; twierdzenie „ile kosztuje wygoda" **stoi nadal**, bo jego rdzeniem jest porównanie **wersji noszonej z pełnowymiarową**, obie własne (`30` sekcja 1) |
| **B. Cyton wypożyczony** | pełne porównanie bez wydatku | zależność od osoby trzeciej, `[luka]` nie wiadomo od kogo — uczelnia, koło naukowe, PB jest 15 minut od szkoły |
| **C. budżet podniesiony** | wszystko zostaje | decyzja finansowa użytkownika, poza moim zasięgiem |

`[wniosek]` **Wyjście A jest domyślne i wcale nie jest złe.** Punkt odniesienia wewnętrzny (ten sam tor, dwie postacie mechaniczne) jest mocniejszy metodologicznie niż porównanie z kupionym sprzętem, bo eliminuje różnice układu scalonego, filtrów i oprogramowania. Cyton był dodatkiem uwiarygadniającym, nie osią twierdzenia.

**Zgrubny podział 8 000 zł przy wyjściu A** — `[domysł]`, do zastąpienia prawdziwym kosztorysem po audycie:

| Pozycja | Rząd wielkości |
|---|---|
| dwie–trzy iteracje płytek PCB z montażem | 1 500–2 500 zł |
| układy scalone toru analogowego, elementy bierne, złącza | 800–1 200 zł |
| elektrody suche i materiały na nie | 500–900 zł |
| drukarka MSLA + żywica biozgodna (`05_RYNEK.md` sekcja 5.4: Liqcreate Bio-Med Clear ~456 zł/0,5 kg) | 1 200–1 800 zł |
| zestaw demonstracyjny — żarówka i gniazdko sterowane (`30` sekcja 6a.3) | do 200 zł |
| pojazd demonstracyjny i czujniki odległości do warstwy autonomii | 400–800 zł |
| zapas na błędy, przesyłki, drugie podejście | **1 000–1 500 zł** |

**Reguła: zapas nie jest opcjonalny.** Przy pierwszym projekcie PCB druga iteracja jest normą, nie porażką.

---

## 4. Kategoria EBED — co z niej wynika operacyjnie

`[fakt]` Rozbiór kategorii jest w `ISEF_ARKUSZE_OCENY.md` sekcja 4.1. Decyzja: **EBED (Embedded Systems)**, podkategorie sensoryki i przetwarzania sygnału.

`[wniosek]` Trzy skutki, które trzeba pilnować od początku, a nie przy pisaniu zgłoszenia:

1. **Sędzia jest elektronikiem, nie lekarzem.** Materiały mają prowadzić przez **tor sygnałowy, szum, pasmo, przetwornik i dekodowanie**, a nie przez fizjologię. Fizjologia jest tłem, nie treścią
2. **Nie opisywać urządzenia jako medycznego.** Ani „diagnostyczne", ani „terapeutyczne", ani „dla pacjentów" — to jest sterowanie i komunikacja, zastosowanie wspomagające. Decyzja użytkownika i zarazem osłona przed pytaniami o walidację kliniczną, których licealista nie udźwignie
3. **Procedura Human Participants obowiązuje mimo wszystko** (K-069). Kategoria nie zmienia tego, że sygnał zbiera się z człowieka. `ISEF_HUMAN_PARTICIPANTS.md` jest dokumentem czynnym

---

## 5. Poprzeczka „gotowy w całości" — co to znaczy w praktyce

Decyzja 4 mówi: na półfinał Explory (V 2027) urządzenie ma być skończone, nie prototypowe.

`[wniosek]` Operacyjnie znaczy to cztery rzeczy jednocześnie: **własna płytka w obudowie** (nie płytka stykowa), **elektrody trzymające się bez pomocy rąk**, **działanie przez całą demonstrację bez restartu**, **wynik pokazywany na żywo, nie z nagrania**.

**Mechanizm ochrony jest jeden i już zapisany:** reguła 6a.3 z `30` — do półfinału nie powstaje nic, co nie jest interfejsem. Rekwizyty się kupuje.

**Ryzyko, które ta poprzeczka tworzy:** przy ~230 h do zgłoszenia i pierwszym w życiu projekcie PCB poprzeczka jest wysoka. Dlatego istnieje drabinka poniżej.

---

## 6. Drabinka zejść pod interfejs — szkielet do zatwierdzenia w audycie

Struktura przeniesiona z zamkniętego pliku `23_RYZYKA.md` sekcja 1; treść napisana od nowa pod interfejs. `[wniosek]`, **do przetestowania w audycie** — to jest dokładnie ten element, który audyt ma rozbić, jeżeli jest życzeniowy.

| Szczebel | Zakres | Co poświęcone | Czy to nadal projekt konkursowy |
|---|---|---|---|
| **A — pełny** | wersja noszona + wersja pełnowymiarowa, ten sam tor, pełne porównanie dokładności i przepustowości w bitach, demonstracja sterowania celem | nic | tak, cel |
| **B** | jak A, ale **mniej warunków pomiarowych** (np. bez badania wpływu ruchu głowy) | część tabeli wieloczynnikowej | **tak** — twierdzenie stoi, traci jeden wymiar |
| **C** | dwie wersje sprzętu, pomiar **tylko na autorze**, bez innych badanych | uogólnienie na populację, ale **znika też cała procedura zgód dla osób trzecich** | tak, słabsze o zewnętrzną ważność |
| **D** | jedna wersja sprzętu, pełna charakteryzacja toru analogowego, dekodowanie działa, demonstracja działa | całe pytanie „ile kosztuje wygoda" | **tak** — zostaje zbudowany i zmierzony interfejs; to nadal więcej niż ma większość stawki Explory |
| **E — dno** | sam tor analogowy na własnej płytce: szum, pasmo, CMRR, kalibracja wobec przyrządu odniesienia, bez sterowania czymkolwiek | wszystko oprócz metrologii toru | **tak** — karta katalogowa własnego wzmacniacza z pomiarami jest kompletnym projektem inżynierskim |

**Reguła schodzenia, bez zmian od etapu 1:** zejście o szczebel wymaga wpisu do `KOREKTY.md` z **datą, powodem liczbowym i wskazaniem, co zostało poświęcone**. Bez wpisu zejście się nie liczy.

`[luka]` **Czego ta drabinka jeszcze nie ma:** terminu, do którego każdy szczebel musi być osiągnięty. To wchodzi razem z przeliczeniem harmonogramu pod jeden cykl (P2).

---

## 7. Struktura planu pomiarowego — szkielet do wypełnienia po audycie

Przeniesiona z `22_PLAN_POMIAROWY.md`, bo jej **układ był przenośny, a treść dotyczyła łożyska**. Siedem pozycji, które plan musi mieć:

1. **Zasada nadrzędna: warunek kontrolny na tym samym sprzęcie.** Porównuje się dwie postacie tego samego toru, nie dwa różne urządzenia
2. **Wielkości mierzone** — dokładność klasyfikacji, przepustowość w bitach na wskazanie, czas do decyzji, szum toru, CMRR. `[luka]` lista do domknięcia
3. **Warunki** — randomizacja kolejności, kontrbalansowanie, replikacja sesji, poprawka na wielokrotne porównania (rzemiosło z ENBM074, `CLAUDE.md`)
4. **Budżet niepewności** — skąd bierze się rozrzut i ile go wnosi każde źródło
5. **Test mechanizmu** — eksperyment rozdzielający, dlaczego wersja noszona wypada gorzej: mniej elektrod, gorszy kontakt czy większy artefakt ruchowy
6. **Co by znaczyło, że projekt się nie udał** — kryterium zapisane z góry, przed pomiarem
7. **Dziennik** — codzienny, datowany, bo jest dowodem samodzielności i materiałem do aplikacji na studia

---

## 8. Co zniknęło z repozytorium 18 VIII 2026

Usunięte jako opis zamkniętego kierunku łożyskowego: **`20_PROJEKT.md`, `21_PLAN_BUDOWY.md`, `22_PLAN_POMIAROWY.md`, `23_RYZYKA.md`.** Wszystko przenośne z nich siedzi w sekcjach 6 i 7 powyżej. Pliki są w historii gita, gdyby kiedyś okazały się potrzebne.

**Łożysko magnetyczne z self-sensingiem** zostaje w dokumentacji **jako jedna linijka w `24_ODRZUCONE_KANDYDATY.md`** — rozważane 17 VIII 2026, porzucone tego samego dnia decyzją użytkownika na rzecz powrotu do interfejsu.
