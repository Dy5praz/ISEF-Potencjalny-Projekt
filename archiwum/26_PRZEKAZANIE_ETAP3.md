# 26 — Przekazanie: stan na koniec etapu 2

**Data:** 16 sierpnia 2026, koniec dnia
**Zastępuje:** `PRZEKAZANIE.md`, który dotyczy etapu 1 i **zawiera nieaktualną oś projektu**.

---

## 1. Pierwsza rzecz do zrobienia w nowej rozmowie

**Zapytaj użytkownika, czy wracamy do preprintu z reanalizy.** Wstrzymany jego decyzją 16 VIII 2026, z wyraźnym poleceniem: *„Trzymaj go jako pierwszą rzecz w pamięci jak wrócimy do tego w innej konwersacji."*

**Materiał jest gotowy w około 80%:** `14_REANALIZA.md` plus odtwarzalny kod w `analiza/`, dane na licencji CC-BY, wynik nieoczywisty (przyrost +9 pp należy do Cz, nie do kanału szczękowego), siedem prac tła z `25_AUDYT_OPENAIRE.md` do zacytowania.

**Po co:** to jest jedyna rzecz z całego projektu, która **nie zależy od sprzętu, od konkursu ani od tego, czy SSVEP u autora działa**, a wprost służy celowi nadrzędnemu.

---

## 2. Cel nadrzędny — zmieniony 16 VIII 2026

**Studia za granicą, najpewniej w Stanach. Explory i ISEF są środkiem, nie celem.**

| Ścieżka | Prawdopodobieństwo | Sterowalność |
|---|---|---|
| wyjazd na ISEF | ~14% | niska — decyduje jury |
| **dorobek: urządzenie + odtwarzalne badanie + preprint** | **~50–60%** | **wysoka — zależy od autora** |

**Optymalizować pod dorobek.** `[fakt]` ISEF maj 2028 wypada **przed** aplikacjami (matura V 2029 → aplikacje jesień 2028), więc i wynik konkursowy, i preprint zdążą wejść do dokumentów.

`[luka]` SAT, TOEFL, terminy, pomoc finansowa, need-blind wobec need-aware — **nieustalone, poza dotychczasowym zakresem pracy.**

---

## 3. Zasada nadrzędna: od arkuszy, nie od luki

**K-075, największy błąd całej dotychczasowej pracy.**

`[fakt]` Arkusz inżynierski ISEF: Research Problem 10, Design and Methodology 15, Execution 20, Creativity & Potential Impact 20, **Presentation 35**. **Rubryki „nowość" nie ma.** Explory: innowacyjność 10 pkt na 40 w półfinale, **zero w finale**.

**Optymalizowaliśmy pod kryterium warte najwyżej 10 punktów na 100 i trzykrotnie pod nie przebudowywaliśmy projekt.**

**Odtąd: zaczynaj od tego, co arkusze punktują.** Luka jest dodatkiem, nie warunkiem.

**Praktyczny skutek, który wypadł z tej analizy i którego nikt wcześniej nie nazwał:** `[wniosek]` **ćwiczenie prezentacji po angielsku jest wyżej punktowaną inwestycją niż druga wersja płytki** (`23_NOTY.md` §4.1).

---

## 4. Stan projektu w jednym akapicie

Interfejs SSVEP w zwartym module potylicznym. **Oś: zależność przepustowości od odległości elektrody odniesienia**, czyli od gabarytu urządzenia. Twierdzenie **pomiarowe**, nie o pierwszeństwie. Efekt przewidywany z reanalizy cudzych danych: **9–24 pp**, w szczytowym ITR **41%**. Sprzęt, plan pomiarowy, budżet i harmonogram **gotowe i niezmienione** przez cały dzień korekt.

**Co jest zrobione naprawdę:** reanaliza z odtworzeniem tabeli autorów co do trzeciego miejsca po przecinku i działający pipeline FBCCA/SVM. **To jedyny własny wynik, jaki ten projekt ma — i pierwszy, jaki którykolwiek z czterech kierunków w ogóle wyprodukował.**

---

## 5. Czego nie wolno powtórzyć — wzorce błędów z 16 VIII

Dziewięć korekt jednego dnia, K-089…K-075. Wzorce, nie pojedyncze pomyłki:

1. **Redukcja czegoś złożonego do jednego zdania, a potem operowanie tym zdaniem zamiast oryginałem.** Dwa razy: „Cz i szczęka" → sama szczęka (K-089); dwie tezy ortezy → jedna (K-073)
2. **Znacznik `[fakt, pełny tekst odczytany]` bez odczytania pełnego tekstu** (K-090). Zbiór danych był publiczny i podany w tej samej pracy
3. **Podanie wymyślonej liczby pod znacznikiem `[domysł]`** (K-071). Znacznik pewności nie usprawiedliwia zmyślenia — cena OpenBCI była do odczytania jednym zapytaniem
4. **„Zero trafień" bez kontroli pozytywnej** (K-074). Złapane dwa razy jednego dnia: arXiv i OpenAIRE. Bez kontroli zero jest artefaktem składni, nie wynikiem
5. **Przeszukiwanie własnym słownictwem zamiast słownictwem dziedziny** (K-074). Dziedzina mówi „monopolar versus bipolar", „lead selection"; ja pytałem o „reference electrode distance"
6. **Optymalizowanie pod kryterium, którego nie ma w arkuszu** (K-075)

**Reguła operacyjna wynikająca z 1 i 2: zanim uznasz kierunek za zamknięty, przeczytaj jego dokument źródłowy, a nie własne streszczenie.**

---

## 6. Otwarte pozycje

### Po stronie użytkownika, wrzesień 2026
- mail do FZT (SRC jako IRB + łączenie z EUCYS)
- rozmowa z dyrekcją o komisji IRB — **plan awaryjny na R1, nie formalność**
- pisemna zgoda opiekuna na Adult Sponsor i Direct Supervisor
- szukanie używanego Cytona, **decyzja do 30 IX**; mail do `sales@openbci.com` o dystrybutora w UE i cło

### Po stronie modelu
- regulaminy El-Robo-Mech XII i OITwEiM, gdy się ukażą jesienią
- monitorowanie konkurencji co dwa miesiące
- **przy powrocie: preprint (sekcja 1)**

### Punkt decyzyjny
**Przesiew E0, październik 2026, dwadzieścia minut.** Rozstrzyga R1 **oraz** to, czy projektem pozostaje interfejs, czy orteza (`22_POROWNANIE.md` §4.2, `23_NOTY.md` §3.2).

---

## 7. Sprawy techniczne środowiska

- **sieć działa**, poza dwoma wyjątkami stałymi: **OpenAlex i Semantic Scholar zwracają HTTP 429** z adresu tego środowiska, niezależnie od backoffu i puli „polite". **Obejście: OpenAIRE** (`api.openaire.eu`, parametr `keywords` wymaga wszystkich słów naraz) **i DOAJ**
- **przeglądarka nie ma dostępu do sieci** — stron renderowanych po stronie klienta nie odczytasz. Działa: `products.json` w sklepach Shopify, `policies/*` tamże, PubMed E-utilities, Europe PMC, Crossref, arXiv, Google Patents przez `xhr/query`
- **`analiza/`** uruchamialne od zera: `pip install numpy scipy scikit-learn h5py`, zmienna `EEG_DATA` wskazuje katalog z rozpakowanymi S01–S12

---

## 8. Zasada dostarczania — złamana trzykrotnie, teraz twarda

**Użytkownik pracuje z telefonu.** Każdy powstały albo istotnie zmieniony plik **trafia do rozmowy narzędziem do wysyłania plików**, w tej samej wiadomości, w której o nim piszesz. **Commit i push to archiwizacja, nie dostarczenie.** Odsyłanie do repozytorium po treść jest zakazane (K-070, `CLAUDE.md`).
