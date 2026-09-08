# 24 — Rejestr odrzuconych kierunków

**Ostatnia zmiana:** 18 sierpnia 2026. **Plik skrócony na życzenie użytkownika** — pełne dossier każdego kandydata jest w historii gita (commit `820a0b4` i wcześniejsze). Tutaj zostaje tyle, ile potrzeba, żeby nikt — łącznie ze mną w następnej sesji — nie zaproponował tego ponownie.

**Zasada:** wpis z tej listy wraca do gry **tylko z nowym argumentem**, którego nie było przy odrzuceniu.

---

## 1. Kierunek bieżący, dla porządku

**Nieinwazyjny interfejs neuralny sterowany bodźcem wzrokowym.** Rozważany od początku, chwilowo zamknięty 17 VIII 2026, **przywrócony decyzją użytkownika tego samego dnia i to jest werdykt ostateczny.** Opis: `30_POWROT_DO_INTERFEJSU.md`, parametry: `34_PARAMETRY_I_RAMY.md`.

---

## 2. Kandydaci z jednego dnia wahania, 17 VIII 2026

Siedem propozycji powstałych w czasie, gdy kierunek interfejsowy był chwilowo zamknięty. **Wszystkie odrzucone, żadna nie wraca.**

| Kandydat | Powód odrzucenia w jednym zdaniu |
|---|---|
| **aktywne łożysko magnetyczne z self-sensingiem** | **rozważane najdłużej i najgłębiej rozpisane — porzucone decyzją użytkownika na rzecz powrotu do interfejsu.** Nie miało wady merytorycznej; przegrało z tym, że interfejs jest w zasięgu jego budżetu, kontaktów i czasu |
| akustyczna kamera do wykrywania nieszczelności | Fluke ma opublikowaną metodę kwantyfikacji, rynek obsadzony; zostawało „taniej" |
| rozrzut fazowy tanich mikrofonów MEMS | zmierzone i opublikowane przez Politechnikę w Eindhoven, a mikrofony do 85 kHz są produktem katalogowym |
| fototermiczna identyfikacja czarnych tworzyw | Fraunhofer IZFP robi dokładnie to; informacja o próbach przemysłowych ukazała się trzy dni przed sesją |
| jednopikselowy obrazowacz SWIR | technika opublikowana, modulatory DMD katalogowe, do tego dwie nowe dziedziny naraz |
| tablica magnetometrów do diagnostyki ogniw | pole zajęte i finansowane, konkurencja z magnetometrami pompowanymi optycznie |
| enkoder indukcyjny na PCB | komercja dojrzała, zostawało „taniej", zero demonstracji przy stoisku |
| tomografia mionowa, obrazowanie fali milimetrowej, badanie zmęczeniowe wydruków, maszyna na cyklu termicznym | odrzucone na wykonalności i braku demonstracji, `30` sekcja 0 |

---

## 3. Kierunki odrzucone wcześniej — dron i orteza

**Zostają w dokumentacji**, opis w `HANDBOOK.md` sekcja 7. Skrót:

- **dron** — porzucony przed rozpoczęciem tej dokumentacji; zostawił po sobie punkt odniesienia o rzędzie wielkości budżetu (~15 000 zł jako „to, co było wyobrażalne") i niewykorzystaną decyzję zakupową o drukarce
- **orteza kolanowa** — odrzucona, bo po sprawdzeniu stanu techniki zostawało z niej wyłącznie „taniej", co nie jest twierdzeniem naukowym

---

## 4. Wniosek metodyczny — najważniejsza rzecz w tym pliku

Kandydaci z sekcji 2 padli, bo szukałem **nieobsadzonego problemu**. To jest błąd strukturalny: **problemy ważne ekonomicznie są z definicji obsadzone**, bo ważność przyciąga finansowanie.

Kształt, który przeżył audyt:

> **znany problem + znane rozwiązanie + konkretna wariacja inżynierska, której efektu nikt nie zmierzył, porównywana wewnętrznie: mój układ z X wobec mojego układu bez X.**

`[fakt]` Arkusz inżynierski ISEF **nie ma kryterium nowości względem literatury**; regulamin Explory §7 pkt 2a dopuszcza *„innowacyjny **i/lub** wnosi dodatkową wartość"*. Filtr to: **wykonalność, demonstracja, głębokość pomiaru, obsada kategorii, podział na dwa pytania.** Błąd opisany w `KOREKTY.md` K-051.
