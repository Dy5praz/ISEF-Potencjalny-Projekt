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

## 3. Budżet 8 000 zł wobec platformy odniesienia — sprawa BYŁA już rozstrzygnięta

**Korekta z 18 VIII 2026 wieczorem, po odzyskaniu gałęzi `claude/etap-2-v9dtnt` (K-076).** Pierwsza wersja tej sekcji ogłaszała „kolizję budżetową", której nie ma — bo decyzja zakupowa zapadła **16 sierpnia** i jest zapisana w **`20_ZAKUPY.md`**. Poniżej stan faktyczny, przepisany z tamtego pliku.

`[fakt, katalog producenta odczytany 16 VIII 2026]` Ceny OpenBCI: **Cyton 8 kanałów — 1 249 USD**, Cyton + Daisy 16 kanałów — 2 499 USD, **Ganglion 4 kanały — 624,99 USD**, sam klucz USB — 249 USD, czepek Ultracortex — 1 399,99 USD.

`[wniosek]` Nowy Cyton to **6 000–6 800 zł** z wysyłką, cłem i VAT — i **to jest wariant odrzucony**, nie zalecany.

**Decyzja obowiązująca, z `20_ZAKUPY.md` sekcja 3.1:**

> **Kupić używanego Cytona, budżet do 1 600 zł, poszukiwania do 30 IX 2026. Jeżeli do tego terminu nie ma dobrej oferty — kupić nowego Ganglion (~3 000–3 400 zł), nie nowego Cytona.**

Lista warunków, które musi spełnić oferta używana (płytka **z kluczem USB**, czytelne oznaczenia ADS1299 i PIC32, sprzedawca z prawem zwrotu, zasilanie bateryjne, kwadransowy test odbiorczy przez zwarcie wejść i pomiar szumu RMS) — w `20_ZAKUPY.md`. Płytki z AliExpress odradzone: przyrząd odniesienia jest jedynym miejscem, gdzie nie wolno mieć wątpliwości co do autentyczności układu scalonego.

`[wniosek]` **Przy 1 600 zł platforma odniesienia zjada 20% budżetu 8 000 zł, nie 72%.** Kolizji nie ma; jest termin — **30 IX 2026** — i to jest jedyna pilna pozycja zakupowa w całym projekcie.

**Do czego ta platforma naprawdę służy** (`20_ZAKUPY.md` sekcja 2, trzy funkcje, dwie prawdziwe):

1. **test R1 — czy SSVEP działa u autora w ogóle**, jeszcze zanim istnieje własna płytka. Krytyczne, termin X 2026
2. **ubezpieczenie**, gdyby własny tor analogowy nie zadziałał
3. ~~„baseline komercyjny" do twierdzenia~~ — **wycofane już 16 VIII**: OpenBCI to płytka badawczo-hobbystyczna bez obudowy i elektrod, więc porównanie z nią nie jest porównaniem z rynkiem

`[wniosek]` Punkt 3 był tym, co wcześniej wpisano do README jako „punkt odniesienia: kupiony OpenBCI Cyton". **Twierdzenie „ile kosztuje wygoda" stoi na porównaniu wewnętrznym — wersja noszona wobec pełnowymiarowej, ten sam tor.** Cyton jest narzędziem kontrolnym i ubezpieczeniem, nie osią.

**Reszta budżetu** — pełne rozbicie jest w `15_PROJEKT.md` sekcja 3 i `20_ZAKUPY.md` sekcja 5, tam gdzie powstało 16 VIII. Suma bez nowego Cytona mieściła się w przedziale **5 700–8 800 zł**, czyli decyzja o 8 000 zł jest z nim spójna, ale **bez zapasu na trzecią iterację płytki**. To jest pozycja do przeliczenia w audycie razem z harmonogramem.

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
