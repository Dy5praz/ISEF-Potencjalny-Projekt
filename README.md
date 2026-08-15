# ISEF — nieinwazyjny interfejs neuralny

Repozytorium robocze projektu. Dokumentacja żyje tutaj, nie w wątkach rozmowy.

**Cel:** Explory 2027 → reprezentacja Polski na Regeneron ISEF, maj 2028.

---

## Stan na 15 sierpnia 2026

| Etap | Status |
|---|---|
| Sekcja 14 handbooka — drugie czytanie, luki i pytania | **zrobione** → `00_PYTANIA_I_LUKI.md` |
| Odpowiedzi użytkownika na pytania A/B/C | **zebrane** → `00_PYTANIA_I_LUKI.md` sekcja 4b |
| Etap 1 — przemiał literatury | **zablokowany do czasu przełączenia sieci na Full**, patrz `00_PYTANIA_I_LUKI.md` sekcja 0 i 4b/A1 |

### Ustalenia kierunkowe (15 VIII 2026)

- **zdolność:** sterowanie **dyskretne** (skończony zbiór komend), nie komunikacja i nie sterowanie ciągłe
- **sEMG/EOG:** dopuszczone jako **kanał odniesienia do usuwania zakłóceń** w torze analogowym; jako źródło sterowania odłożone, nie odrzucone
- **czas:** 10 h/tydz. → ~350 h do El-Robo-Mech, ~910 h do ISEF
- **budżet:** świadomie nieustalony, decyzja po opracowaniu

### Żeby ruszyć dalej

`claude.ai/code` → ikona chmurki nad polem wiadomości → zębatka przy środowisku → **Network access: Full** → zapisz → **nowa sesja** na gałęzi `claude/oto-handbook-instrukcje-g3e7hd` z poleceniem „rób etap 1".
| Etap 2 — opracowanie projektu | przed nim etap 1 |

---

## Struktura docelowa

| Plik | Zawartość | Status |
|---|---|---|
| `00_PYTANIA_I_LUKI.md` | luki, sprzeczności, pytania do użytkownika | gotowy |
| `00_STRESZCZENIE.md` | 2 strony, co z etapu 1 wynika | — |
| `01_HISTORIA.md` | rozwój technologii inwazyjnych i nieinwazyjnych, z datami | — |
| `02_MECHANIZMY.md` | mechanizm fizyczny każdej klasy rozwiązań, po polsku, każdy termin z definicją | — |
| `03_SCIANY_FIZYCZNE.md` | co uznano za niemożliwe, z rozróżnieniem fizyczne / technologiczne | — |
| `04_LUKI_ZAPISANE.md` | sekcje „future work" i „open challenges" z cytatami i namiarami | — |
| `05_RYNEK.md` | baseline komercyjny: co, za ile, z jakimi parametrami | — |
| `06_TABELA_PARAMETROW.md` | wspólna metryka porównawcza + kolumna widoczności urządzenia | — |
| `07_DEKODOWANIE.md` | paradygmaty, metody klasyczne i sieciowe, metryki, zbiory danych | — |
| `08_KONKURENCJA_ISEF.md` | ENBM074 i projekty pokrewne z ostatnich lat | — |
| `ZRODLA.md` | pełna bibliografia z oceną wiarygodności | — |
| `KOREKTY.md` | rejestr błędów i poprawek | prowadzony |

---

## Zasady obowiązujące w każdym pliku

Znaczniki pewności przy każdym stwierdzeniu:

- `[fakt]` — twarde dowody, źródło sprawdzone
- `[wniosek]` — silne wnioskowanie z faktów
- `[domysł]` — uzupełnianie luki, spekulacja
- `[luka]` — wiadomo, że nie wiadomo

Każda liczba, na której cokolwiek się opiera: 2–3 niezależne źródła. Jedno źródło — oznaczone wyraźnie przy twierdzeniu, nie w przypisie.

Hierarchia przy sprzeczności: dokument regulaminowy > publikacja recenzowana > preprint > materiał prasowy > blog/forum.
