# PRZEKAZANIE — start nowej sesji

**Data:** 15 sierpnia 2026, wieczór — **wersja druga**
**Po co ten plik:** poprzednia wersja mówiła nowej sesji, że etap 1 został wykonany bez dostępu do sieci i co trzeba domknąć. **Zostało domknięte.** Ta wersja mówi, co zastajesz teraz i od czego zacząć etap 2.

---

## 1. Stan: etap 1 ZAMKNIĘTY

Sesja z 15 VIII wieczorem miała pełny dostęp do sieci i wykonała wszystkie dziewięć pozycji z sekcji 3 poprzedniej wersji tego pliku.

**Odczytane w oryginale:**
- *International Rules for Pre-College Science Research 2026–2027*, Society for Science, 46 stron
- *Regulamin Konkursu Explory*, Fundacja Zaawansowanych Technologii, 11 stron
- *ISEF Grand Award Judging Criteria*, oba arkusze
- baza abstraktów Society for Science — **pełny abstrakt ENBM074 (2026)** oraz liczby projektów EEG za lata 2014–2026
- oficjalna lista finalistów Explory 2026 i pełna lista 133 projektów półfinałowych
- **12 prac naukowych** (abstrakty przez PubMed E-utilities)
- karta katalogowa ADS1299

**Wynik: szesnaście korekt, `KOREKTY.md` K-020…K-035.**

---

## 2. Co przeczytać i w jakiej kolejności

1. **`CLAUDE.md`** — zasady współpracy, obowiązują bezwzględnie
2. **`00_STRESZCZENIE.md`** — sekcja 0 mówi w pięciu punktach, co się zmieniło. Jeżeli masz przeczytać jedną rzecz, to tę
3. **`HANDBOOK.md`** — zlecenie, z pięcioma wstawkami „POPRAWKA"
4. **`KOREKTY.md`** — K-020…K-035 to ta sesja. **Trzy z nich zmieniają decyzje projektowe**
5. reszta wg potrzeby, nawigacja w `00_STRESZCZENIE.md` sekcja 6

---

## 3. Co jest otwarte — i czyja to decyzja

### 3.1 Czeka na użytkownika, blokuje etap 2

| # | Decyzja | Gdzie | Uwaga |
|---|---|---|---|
| 1 | **C2 — w czym „lepsze od komercyjnych"** | `00_STRESZCZENIE.md` 1.2 | **rekomendacja poprzedniej sesji WYCOFANA** — stała na liczbie nieaktualnej o osiem lat (K-028). Trzy warianty mają porównywalny status. **Nie rozstrzygać tego za użytkownika drugi raz** |
| 2 | **umiejscowienie elektrod** | `09_UMIEJSCOWIENIE.md` | argument za potylicą osłabł po K-028. Rekomendacja bez zmian: zrobić z geometrii zmienną mierzoną |
| 3 | skala widoczności / gabarytu | `06` sekcja 4 | zatwierdzić albo poprawić |
| 4 | E1 — potwierdzenie korekty K-001 | `00_PYTANIA_I_LUKI.md` 1.1 | 8 miesięcy do El-Robo-Mech, nie 14 |

### 3.2 Do zrobienia poza komputerem, jesień 2026

1. **rozmowa z dyrekcją szkoły** o powołaniu komisji IRB (nauczyciel inny niż opiekun + dyrektor + pielęgniarka lub psycholog). Najdłuższy proces w harmonogramie formalnym
2. **mail do FZT** — czy organizator prowadzi SRC pełniące funkcję IRB. Może skasować punkt 1
3. **mail do FZT i do Funduszu ZDOLNI** — czy start w Explory i EUCYS można łączyć
4. **pisemna zgoda opiekuna** na Adult Sponsor i Direct Supervisor

### 3.3 Pozycje merytoryczne otwarte

| Co | Dlaczego |
|---|---|
| **pełne teksty prac w otwartym dostępie** — SpiralE (PMC10349124), Kappel (PMC5553928), Lee (PMC8688416) | odczytane są abstrakty, nie pełne teksty. Te trzy da się przeczytać za darmo i **na nich stoi najwięcej twierdzeń** |
| licencje publicznych zbiorów danych | wymagają otwarcia stron z danymi. **Przed użyciem czegokolwiek** |
| `02_MECHANIZMY.md` | **jedyny plik treściowy nieweryfikowany źródłowo w tej sesji.** Zawiera wyjaśnienia mechanizmów fizycznych, nie liczby, więc ryzyko jest niższe — ale nie zerowe |
| Explory 2016–2024, liczby projektów neuro | archiwalne listy są aplikacjami renderowanymi w przeglądarce; przeglądarka w tym środowisku nie ma dostępu do sieci (patrz sekcja 5) |
| regulamin ISEF 2027–2028 | jeszcze nie istnieje, ~połowa 2027. **Przeczytać wtedy od nowa** |
| regulamin El-Robo-Mech XII i OITwEiM 2026/27 | ukażą się jesienią 2026 |

---

## 4. Pułapki — zaktualizowane

Poprzednia wersja wymieniała K-012/K-018, K-014, K-015, K-016, K-019 i nazywała wspólny wzorzec: **budowanie mocnego twierdzenia na własnym założeniu, bez sprawdzenia**.

**Ta sesja pokazała, że wzorzec ma drugą, gorszą odmianę: budowanie mocnego twierdzenia na cudzym streszczeniu, bez sprawdzenia.** Trzy najpoważniejsze wpadki tej sesji to K-026, K-027 i K-028 — wszystkie polegały na tym, że streszczenie mówiło coś podobnego do prawdy, a oryginał mówił coś innego.

**Konkretne reguły, które z tego zostają:**

1. **Przy każdej liczbie z literatury podawać liczbę badanych.** Liczba „16,6 bit/min" wyglądała solidnie, dopóki nie okazało się, że pochodzi z badania na **czterech osobach** (K-031)
2. **Sprawdzać rok publikacji, zanim się uzna coś za stan techniki.** Liczby opisujące „pułap formy dousznej" pochodziły z 2015 i 2022, a praca z 2023 przesunęła go o rząd wielkości (K-028)
3. **Zgodność trzech streszczeń nie jest weryfikacją.** CMRR układu ADS1299 był oznaczony jako „najpewniejsza liczba w pliku, trzy niezależne opisy" i był błędny o 10 dB (K-030)
4. **Twierdzenie „nie znalazłem, więc nie ma" jest zakazane bez podania, gdzie się szukało.** K-027 obalił takie twierdzenie jednym zapytaniem w PubMed
5. **Szukać także najwcześniejszej pracy, nie tylko najświeższej.** Rola sEMG jako źródła sterowania wyglądała na zamkniętą w 2025; pierwszeństwo jest z **2014** (`04` sekcja 4)

---

## 5. Sprawy techniczne środowiska

- **sieć: działa.** To środowisko ma pełny dostęp wychodzący. Zweryfikowane na `societyforscience.org`, `explory.pl`, `pubmed.ncbi.nlm.nih.gov`, `ti.com`, `isef.net`, `sspcdn.blob.core.windows.net`
- **przeglądarka nie działa.** Chromium jest zainstalowany, ale nie ma dostępu do sieci nawet przez proxy (`ERR_CONNECTION_RESET`). **Skutek: stron renderowanych po stronie klienta nie da się odczytać.** Dotyczy `final.explory.pl` i archiwalnych stron Explory. Obejście, które zadziałało: szukać danych w metatagach (`isef.net`), w plikach PDF publikowanych obok strony (`Wyniki_Polfinal_2026.pdf`), albo w formularzach POST (`abstracts.societyforscience.org`)
- **PubMed przez E-utilities działa i jest najlepszym kanałem do literatury.** Indeksuje także IEEE TBioCAS i IEEE TBME, więc obejmuje literaturę układową. Skrypty pomocnicze zostały w katalogu tymczasowym sesji i **nie są w repozytorium** — trzeba je napisać od nowa, to kilkanaście linijek
- **`pypdf` wymaga naprawy `cffi`** przed użyciem: `pip install --force-reinstall cffi`. Bez tego wysypuje się na module kryptograficznym
- **gałąź:** ta sesja pracuje na `claude/verify-complete-docs-mmu2qn`. Repozytorium ma też `main` i `claude/oto-handbook-instrukcje-g3e7hd`. **Commituj na gałąź, na której wylądowałeś, i nie zajmuj użytkownika gałęziami** — pisze z telefonu

---

## 6. Jedno zdanie na koniec

Etap 1 jest zamknięty i jego wynik jest **inny**, niż wyglądał rano: formalności są łatwiejsze, konkurencja na Explory prawie nie istnieje, konkurencja na ISEF rośnie szybko, a forma douszna ma pułap o rząd wielkości wyżej, niż zakładaliśmy — w warstwie, w której użytkownik jest mocny. **Etap 2 można zaczynać, ale nie od miejsca, w którym rano się wydawało, że się kończy.**
