# 09 — Gdzie ma być interfejs

**Status: decyzja otwarta.** Do 15 VIII 2026 była zamknięta bez postawienia pytania — patrz `KOREKTY.md` K-019.

Ten plik istnieje, bo forma „za uchem, wielkości aparatu słuchowego" była traktowana jak ograniczenie wejściowe, a jest jedną z możliwych odpowiedzi na rzeczywiste wymaganie. Rzeczywiste wymaganie brzmi: **niewidoczne albo nierozpoznawalne jako sprzęt, wygodne do noszenia, zero hełmów.**

---

## 1. Dlaczego to pytanie jest ważniejsze niż wyglądało

Miejsce elektrody decyduje o tym, jaki sygnał w ogóle istnieje. Wzmacniacz i algorytm mogą wycisnąć to, co dotarło; nie mogą wytworzyć tego, czego nie ma.

**Kluczowa obserwacja, która wychodzi dopiero po zestawieniu liczb z `06_TABELA_PARAMETROW.md`:**

Najlepszy paradygmat sterowania dyskretnego pod względem przepustowości to **SSVEP**. Jego generator leży w korze wzrokowej, czyli **na potylicy**. Obecne założenie umieszcza elektrody **maksymalnie daleko od tego źródła** — po przeciwnej stronie głowy.

| Gdzie | ITR dla SSVEP |
|---|---|
| potylica (Oz/O1/O2) | **~70–92 bit/min** |
| skroń (T7/T8) | 6,4 bit/min |
| ucho, online | 11–16,6 bit/min |

`[wniosek, streszczenie]`. **Różnica pięcio- do piętnastokrotna jest w całości kosztem umiejscowienia**, nie jakości wykonania. To nie jest strata, którą odrabia się lepszym torem analogowym.

**Wniosek [wniosek]:** w wersji zausznej projekt z góry oddaje rząd wielkości wydajności, żeby spełnić wymaganie estetyczne. To może być świadomy wybór — ale musi być wyborem, a nie skutkiem ubocznym.

---

## 2. Porównanie miejsc

Skala widoczności wg `06_TABELA_PARAMETROW.md` sekcja 4: **0** = niewidoczne z 2 m, **1** = widoczne, ale nierozpoznawalne jako sprzęt, **3–4** = rozpoznawalny sprzęt na głowie.

| Miejsce | Jaki sygnał dostępny | Widoczność | Mocowanie | Włosy | Główne zakłócenie |
|---|---|---|---|---|---|
| **kanał słuchowy** (in-ear) | alfa pewnie; słuchowe niepewnie; SSVEP słabo; ruch marginalnie | **0–1** | **bardzo dobre** — kanał trzyma wkładkę | brak | żwacz i mięsień skroniowy tuż obok; **artefakty szczękowe gorsze niż na skalpie** |
| **za uchem / wyrostek sutkowaty** | jak wyżej, nieco większy rozstaw elektrod | **1** | **bardzo dobre** — małżowina jako zaczep. Dlatego tam żyją aparaty słuchowe | minimalne | mięsień skroniowy, mięśnie karku |
| **wokół małżowiny** (cEEGrid) | jw., 10 elektrod, sprawdzone w literaturze | **1** | dobre, ale na klej | minimalne | jw. |
| **potylica** (Oz/O1/O2) | **SSVEP maksymalny; alfa najsilniejsza na całej głowie** | **0, jeżeli włosy zakrywają**; 3 jeżeli nie | **trudne** — brak naturalnego zaczepu | **główna przeszkoda** dla elektrod suchych | mięśnie karku przy ruchach głowy |
| **kark, poniżej potylicy** | SSVEP słabszy niż z Oz, ale bliżej niż ucho | 0–1 przy krótkiej fryzurze | średnie | zależy od fryzury | mięśnie karku silniej |
| **czoło** (Fp1/Fp2) | frontalne i EOG; **do sterowania mało** | 1 w oprawkach, 3 samodzielnie | dobre | brak | mięśnie mimiczne, mruganie |
| **oprawki okularów** | czoło + skroń + zauszne | **1** — wygląda jak okulary | **bardzo dobre** | brak | jw. |
| **ciemię** (C3/Cz/C4) | wyobrażenie ruchu, sterowanie ciągłe | **4** — wymaga czapki | wymaga opaski lub czapki | tak | — |

---

## 3. Potylica — pełny rozbiór, bo to jest realna alternatywa

### 3.1 Co przemawia za

- **odzyskuje rząd wielkości ITR** dla SSVEP, patrz sekcja 1
- alfa potyliczna jest najsilniejszym rytmem, jaki EEG w ogóle rejestruje — czyli **rezerwa na paradygmat zapasowy**, gdyby SSVEP odpadł
- **widoczność przestała być przeszkodą** — użytkownik rozstrzygnął (sekcja 5a), że kilka małych elementów z tyłu głowy przechodzi, także widocznych. Ten argument nie musi już opierać się na chowaniu pod włosami
- większy dostępny rozstaw elektrod (O1–O2 to kilka centymetrów) → lepszy stosunek sygnału do szumu przy tym samym torze

### 3.2 Co przemawia przeciw

- **włosy.** Po odpowiedziach z sekcji 5a to jest **jedyny poważny zarzut, jaki został** — i jest inżynierski, nie estetyczny. Elektrody suche przez włosy wymagają szpilek lub pazurków, docisku, i mają gorszy oraz mniej stabilny kontakt niż na skórze gołej. Impedancje, które mam zebrane (4 kΩ mokra, ~450 kΩ sucha), dotyczą **kanału słuchowego, czyli skóry bez włosów** — dla owłosionej potylicy będzie gorzej `[wniosek]`. **To jest pozycja do zmierzenia w pierwszej kampanii, nie do rozstrzygnięcia teraz**
- **mocowanie.** Za uchem jest małżowina, w kanale jest sam kanał. Na potylicy nie ma się o co zaczepić. Zostaje: cienki łuk pod włosami z tyłu głowy, klej (tak trzyma się cEEGrid), albo wpięcie we włosy
- **mięśnie karku.** Zamiast szczęki dostajemy prostowniki karku. `[domysł, do sprawdzenia]` możliwe, że to zakłócenie jest **rzadsze**, bo mówi się i żuje stale, a kark napina się przy ruchach głowy — ale to jest domysł i wymaga pomiaru, nie założenia
- **SSVEP wymaga patrzenia na migający obiekt**, więc traci się argument „działa przy zamkniętych oczach" i wchodzi się w bezpośrednie porównanie z eye trackingiem

### 3.3 Wariant hybrydowy, który wygląda najciekawiej

`[domysł]` **Zausznik jako moduł elektroniki i elektroda odniesienia, cienki łuk pod włosami z tyłu głowy, elektrody czynne na potylicy.**

Dlaczego to się składa:
- wyrostek sutkowaty za uchem to **klasyczna pozycja elektrody odniesienia** w EEG — czyli i tak jej tam potrzebujemy
- małżowina daje zaczep mechaniczny dla całości i miejsce na baterię oraz płytkę
- łuk biegnie z tyłu głowy, nie przez czoło i nie przez czubek — mieści się w granicy z sekcji 5a
- rozstaw potylica ↔ wyrostek sutkowaty jest duży, więc amplituda różnicowa duża

To zachowuje mocne strony formy zausznej (mocowanie, elektronika, brak włosów pod referencją) i odzyskuje sygnał, którego przy uchu nie ma.

**Rozstrzygnięte 15 VIII 2026:** widoczność łuku nie jest przeszkodą (sekcja 5a). Otwarte pozostaje jedno — **kontakt elektrody przez włosy** — i to jest pytanie do pomiaru, nie do użytkownika.

---

## 4. Sprzężenie, którego wcześniej nie postawiłem

**Miejsce i oś projektu nie są niezależnymi decyzjami.** To jest najważniejsza rzecz w tym pliku.

| Umiejscowienie | Dominujące zakłócenie | Jaka oś projektu z tego wynika |
|---|---|---|
| ucho / zausznik | EMG szczęki i EOG, udokumentowane jako **gorsze niż na skalpie** (Kappel 2017) | **analogowa kompensacja artefaktów mięśniowo-ocznych** — obecny kandydat |
| potylica | kontakt elektrody przez włosy, artefakty ruchowe, stabilność mechaniczna | **elektroda sucha i mocowanie odporne na ruch** — też problem opisany jako otwarty w przeglądach 2025–2026 |
| wariant hybrydowy | oba, w różnych punktach | do wyboru — albo obie warstwy, jeżeli starczy czasu |

**Konsekwencja:** obecna oś projektu (kompensacja analogowa EMG/EOG) jest sensowna **dlatego, że urządzenie jest przy uchu**. Przeniesienie na potylicę nie unieważnia projektu, ale **wymaga wyprowadzenia osi od nowa** — nie da się jej przenieść mechanicznie, bo problem szczęki tam nie dominuje.

Obie osie mają pokrycie w literaturze jako problemy otwarte (`04_LUKI_ZAPISANE.md` sekcja 1.1: redukcja artefaktów ruchowych, sprzężenie mechaniczno-elektryczne, dobór materiałów). Żadna nie jest z góry lepsza.

---

## 5. Czego nie da się rozstrzygnąć bez użytkownika

Pytania postawione i **odpowiedziane 15 VIII 2026** — patrz sekcja 5a.

---

## 6. Co zostaje niezależnie od wyboru miejsca

- **elektrody nad korą ruchową (C3/Cz/C4) pozostają wykluczone** — wymagają czapki, stopień widoczności 4. Ustalenie „odczyt dyskretny" trzyma się niezależnie od tego pliku
- **wymaganie bezpieczeństwa** z sekcji 12 handbooka: zasilanie bateryjne albo izolacja galwaniczna, niezależnie od umiejscowienia
- **twierdzenie pomiarowe zamiast twierdzenia o pierwszeństwie** — patrz `00_STRESZCZENIE.md` sekcja 1.1


---

## 5a. Odpowiedzi użytkownika, 15 VIII 2026 — ograniczenie jest luźniejsze, niż je stawiałem

### Widoczność: kryterium to gabaryt, nie widoczność

Odpowiedź dosłowna: *„może być nawet widoczne. Te moje kategoryczne »nie« co do widoczności dotyczyło kasków itd., a jeden lub kilka elementów z tyłu głowy aż tak tego nie psuje. Pod warunkiem, że będą mniejsze, a nie cała stacja pomiarowa."*

**To jest przeformułowanie wymagania, nie jego złagodzenie o stopień.** Przez cały etap 1 optymalizowałem pod „niewidoczne", podczas gdy rzeczywiste ograniczenie brzmi **„nie może być klocem"**. Konsekwencje:

- **potylica jest otwarta bezwarunkowo** — nie zależy już od tego, czy włosy ją zakryją
- kilka małych elementów jest dopuszczalne, więc **wariant rozłożony nie jest obciążony estetycznie**
- odpada cała gałąź rozumowania o chowaniu urządzenia pod włosami

**Propozycja definicji operacyjnej, do potwierdzenia:**

| Przechodzi | Nie przechodzi |
|---|---|
| moduł do rozmiaru aparatu słuchowego lub słuchawki dousznej | cokolwiek wielkości pudełka |
| kilka takich modułów, także z tyłu głowy | konstrukcja przechodząca **nad czubkiem głowy albo przez czoło** |
| cienki przewód lub łuk między modułami, przy głowie | pasek pod brodą, opaska czołowa |
| łączna masa noszona rzędu kilkudziesięciu gramów | plecak, pasek, moduł zewnętrzny na kablu |

**Twarda granica, powtórzona przez użytkownika dwa razy: żadnych kasków.**

### Priorytet przy konflikcie

*„Na start nie schodźmy z żadnej. Ale jak już nic ci nie wyjdzie, to w pierwszej kolejności tnij trochę na niewidoczności. Ale pamiętaj, żadnych kasków."*

Kolejność ustępstw, wiążąca dla etapu 2: **1) gabaryt i widoczność, 2) wygoda długiego noszenia, 3) nigdy — konstrukcja typu hełm.** Każde zejście zapisywane z powodem, zgodnie z sekcją 11 handbooka.

### Mocowanie: klej wyłącznie jako wariant testowy

To rozstrzygnięcie jest lepsze, niż wyglądało w pytaniu, bo **rozdziela dwa dowody, które inaczej by się mieszały**:

| Wariant | Do czego | Co dowodzi |
|---|---|---|
| **klejony**, elektrody płaskie + plaster medyczny | kampania pomiarowa | jakość **toru analogowego i elektrod** przy kontakcie bliskim ideału. Mocowanie przestaje być zmienną zakłócającą |
| **mechaniczny**, docelowy | urządzenie noszone | jakość **mocowania** — o ile pogarsza wynik względem wariantu klejonego |

Koszt: dwie konstrukcje. Ale wariant klejony jest tani (elektrody płaskie i plaster), a różnica między nimi **jest wynikiem pomiarowym, nie stratą** — pokazuje, ile kosztuje wygoda. To jest dokładnie ten typ liczby, który punktuje sekcja Execution arkusza inżynierskiego ISEF.

---

## 5b. Zwarty czy rozłożony — różnica, o którą pytał użytkownik

### Porównanie

| | **Jeden zwarty element** | **Rozłożony (zausznik + łuk + potylica)** |
|---|---|---|
| **rozstaw elektrod** | 2–6 cm w obrębie modułu | **do kilkunastu cm** (potylica ↔ wyrostek sutkowaty) |
| **amplituda różnicowa** | mała — bliskie punkty na skalpie mają podobny potencjał | **duża. To jest główny zysk i on jest fizyczny** |
| **referencja** | lokalna, blisko elektrody czynnej → **zjada część sygnału** | wyrostek sutkowaty, czyli klasyczna pozycja referencji, daleko od źródła wzrokowego |
| **elektronika i bateria** | musi siedzieć tam, gdzie elektrody | **można odsunąć do ucha.** Przetwornica i radio to źródła zakłóceń przy sygnale mikrowoltowym — oddalenie ich od elektrod czynnych jest realną przewagą |
| **przewody** | brak, więc brak artefaktów od ruchu przewodu | **łuk to przewód**: efekt tryboelektryczny przy zginaniu i antena dla 50 Hz. Do rozwiązania ekranowaniem i prowadzeniem, ale **to jest praca do wykonania**, nie drobiazg |
| **mocowanie** | jeden punkt, na potylicy nie ma o co zaczepić | dwa punkty, przy czym **małżowina daje kotwicę mechaniczną** |
| **nakład pracy** | mniejszy | ~1,5–2×, ale **nie trudniejszy jakościowo** — mieści się w warsztacie z sekcji 1 handbooka |
| **pokaz na stoisku** | wygląda jak produkt | wymaga zdania wyjaśnienia, ale wygląda na przemyślane inżyniersko |

### Rekomendacja: nie wybierać teraz, zrobić z tego zmienną mierzoną

**Jeden tor analogowy ze złączem, dwie wiązki elektrodowe: zauszna i zauszno-potyliczna. Ten sam paradygmat, ten sam wzmacniacz, ta sama osoba, dwie geometrie, pomiar.**

Dlaczego to jest lepsze niż wybór z góry:

1. **Zamienia moją pomyłkę w wynik.** Decyzja, którą podjąłem założeniem (K-019), zostaje podjęta pomiarem. Różnica ITR między geometriami to liczba, której nikt w tym projekcie nie musi zgadywać
2. **Jest to publikowalna forma.** Literatura ma prace porównujące równolegle skalp, okolicę wokółuszną i kanał słuchowy (arXiv 2505.14478), a przegląd z 2026 wskazuje **brak standaryzacji konfiguracji i referencji w ear-EEG** jako lukę otwartą (`04_LUKI_ZAPISANE.md` sekcja 1.2)
3. **Zabezpiecza przed porażką jednej gałęzi.** Jeżeli łuk okaże się nie do opanowania szumowo, zostaje wariant zwarty i pomiar, który pokazuje dlaczego
4. **Punktuje wprost w arkuszu inżynierskim ISEF**, sekcja Execution: testowanie w wielu warunkach i próbach

**Koszt tej drogi:** złącze w torze analogowym jest dodatkowym miejscem na zakłócenia i rezystancję przejścia. Trzeba je wybrać świadomie i zmierzyć jego wpływ osobno. To jest znany problem, nie niespodzianka.

---

## 6a. Co się zmienia w reszcie dokumentacji po tych odpowiedziach

- **`06_TABELA_PARAMETROW.md` sekcja 4** — skala widoczności przestaje być skalą widoczności, staje się skalą gabarytu. Próg akceptacji przesuwa się ze stopnia 1 na „nie kloc, nie hełm"
- **oś projektu** — nadal nierozstrzygnięta i nadal sprzężona z miejscem (sekcja 4). Kampania porównawcza z 5b **dostarczy danych do jej wyboru**, zamiast wymuszać wybór przed pomiarem
- **`00_STRESZCZENIE.md` sekcja 1.2** — teza „nie da się wygrać w przepustowości" była **poprawna dla ucha i nieprawdziwa dla projektu**. Przy dostępnej potylicy SSVEP wraca do gry jako paradygmat o realnym ITR
