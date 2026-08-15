# PRZEKAZANIE — start nowej sesji

**Data:** 15 sierpnia 2026
**Po co ten plik:** poprzednia sesja działała bez dostępu do sieci i wykonała etap 1 na samych streszczeniach wyszukiwarki. Ten plik mówi nowej sesji, co zastała, czego temu brakuje i od czego zacząć.

---

## 1. Prompt do wklejenia w nowej sesji

> Przeczytaj `CLAUDE.md`, `HANDBOOK.md`, `PRZEKAZANIE.md`, `KOREKTY.md`, `README.md` i `00_PYTANIA_I_LUKI.md`, w tej kolejności, w całości.
>
> Pliki `00_STRESZCZENIE.md` oraz `01`–`09` istnieją, ale są **szkieletem zbudowanym bez dostępu do źródeł** — żadna praca nie została otwarta, każda liczba ma znacznik `[wniosek, streszczenie]`.
>
> **Zadanie: wykonać etap 1 w pełnym zakresie sekcji 10 handbooka.** Nie pisać tych plików od nowa — zweryfikować każdą liczbę w oryginale, uzupełnić braki, domknąć pozycje z sekcji 3 poniżej i zdjąć znaczniki `[wniosek, streszczenie]` tam, gdzie źródło zostało odczytane.
>
> **Najpierw sprawdź, czy sieć działa:** otwórz `https://www.societyforscience.org/isef/international-rules/human-participants/`. Jeżeli dostaniesz 403 albo `EGRESS_BLOCKED`, przerwij i powiedz o tym — sesja jest w niewłaściwym środowisku i dalsza praca nie ma sensu.

---

## 2. Co zastajesz i jakiego to jest statusu

| Plik | Stan |
|---|---|
| `HANDBOOK.md` | źródło zlecenia. **Ma trzy wstawki „POPRAWKA"** naniesione w etapie 1 |
| `00_PYTANIA_I_LUKI.md` | luki, dwie rundy odpowiedzi użytkownika, **lista 12 zadań weryfikacyjnych w sekcji 4d** |
| `00_STRESZCZENIE.md` | wnioski projektowe. Sekcje 1.1–1.4 powstały przy nieaktualnym założeniu o umiejscowieniu — czytać razem z `09` |
| `01`–`08` | treść etapu 1, **wszystkie liczby do weryfikacji** |
| `09_UMIEJSCOWIENIE.md` | **decyzja otwarta o miejscu na głowie.** Najnowszy plik, zawiera odpowiedzi użytkownika z 15 VIII wieczorem |
| `ISEF_HUMAN_PARTICIPANTS.md` | **najpilniejsze.** Formalności, terminarz wsteczny, siedem pozycji do odczytania |
| `ZRODLA.md` | 87 pozycji ze skalą wiarygodności A–D i listą odrzuconych. **Pozycji przeczytanych w oryginale: 0** |
| `KOREKTY.md` | K-001…K-019. **Pięć z nich to błędy poprzedniej sesji, nie handbooka** |

---

## 3. Co domknąć, w kolejności

| # | Zadanie | Gdzie | Dlaczego ten priorytet |
|---|---|---|---|
| 1 | **klasyfikacja ryzyka urządzenia elektrycznego w kontakcie z głową**; czy zwolnienie dla badania na sobie obowiązuje | `ISEF_HUMAN_PARTICIPANTS.md` sekcja 5, pozycje 5 i 7 | jedyna pozycja o **bezpośrednich konsekwencjach dyskwalifikacyjnych**. Rozstrzyga, czy jesień 2026 to nauka PCB, czy nauka PCB plus papiery |
| 2 | pełny abstrakt **ENBM074 (2026)** | `08` sekcja 2 | żeby nie wejść przypadkiem w ścieżkę, której zakazuje sekcja 9.2 handbooka. **Kod cytować z rocznikiem** — patrz K-018 |
| 3 | przegląd systematyczny: analogowa kompensacja EMG/EOG przy uchu | `04` sekcja 2 | pod tym stoi kandydat na oś projektu. Poprzednia sesja przeszukała **jeden kanał**, co nie jest dowodem nieistnienia |
| 4 | projekty neuro/EEG/BCI w finałach Explory 2016–2026, **liczby** | `08` sekcja 3 | weryfikacja argumentu z sekcji 9.3 handbooka. Nie podawać wrażenia zamiast liczb |
| 5 | oba arkusze oceny ISEF w całości | osobny plik | sekcja 5.2 handbooka. Rozbicie punktowe w handbooku **niezweryfikowane** |
| 6 | oryginały regulaminów Explory i El-Robo-Mech | `08` | dokument regulaminowy stoi najwyżej w hierarchii sekcji 13 |
| 7 | weryfikacja liczb `[wniosek, streszczenie]` w `01`–`09` | wszędzie | zdejmowanie znacznika po odczytaniu oryginału |
| 8 | alternatywy dla El-Robo-Mech dające realną walidację zewnętrzną | `08` sekcja 4.1 | **nieprzeszukane** |
| 9 | czy żywica z certyfikatem ISO 10993 jest dostępna dla amatora w Polsce | `05` sekcja 5.3 | czeka decyzja zakupowa |

**Pozycje zamknięte w etapie 1, nie powtarzać:** 4d nr 1 (kalendarz ISEF), 5 (paradygmaty przy uchu), 6 (shared control), 7 (materiały), 8 (pomiar szumu bez oscyloskopu), 9 (El-Robo-Mech).

---

## 4. Decyzje czekające na użytkownika

1. **umiejscowienie** — `09_UMIEJSCOWIENIE.md`. Rekomendacja poprzedniej sesji: uczynić z geometrii elektrod **zmienną mierzoną**, budując jeden tor analogowy ze złączem i dwie wiązki (zauszna, zauszno-potyliczna)
2. **oś projektu** — sprzężona z umiejscowieniem, patrz `09` sekcja 4. Przy uchu: kompensacja artefaktów mięśniowo-ocznych. Przy potylicy: elektroda sucha i mocowanie odporne na ruch. **Nie da się przenieść jednej na drugie miejsce**
3. **paradygmat** — SSVEP wygląda lepiej niż słuchowy, ale wymaga migającego obiektu i wchodzi w porównanie z eye trackingiem. K-015
4. **C2** — w czym „lepsze od komercyjnych". Po otwarciu potylicy wariant przepustowościowy **wraca do gry** i rekomendacja z `00_STRESZCZENIE.md` 1.2 wymaga przeliczenia
5. **E1, E3** — potwierdzenia do handbooka, `00_PYTANIA_I_LUKI.md` sekcja 4c

---

## 5. Pułapki, w które wpadła poprzednia sesja

Wszystkie opisane w `KOREKTY.md`. Skrót, żeby nie powtórzyć:

- **K-012/K-018** — podważyłem prawidłowy kod projektu na podstawie wpisu z innego rocznika, łamiąc regułę, którą sam zapisałem w tym samym akapicie. **Kody ISEF cytować wyłącznie z rocznikiem.** Nie nadpisywać poprawnej informacji ze źródła własnym wnioskiem
- **K-014** — postawiłem argument „z ucha nie widać kory ruchowej" mocniej, niż pozwalała literatura. Istnieje praca PLOS One 2025 o wykrywaniu ERD rytmu mu z ucha
- **K-015** — rekomendowałem paradygmaty słuchowe na podstawie bliskości anatomicznej; praca Frontiers 2026 pokazuje, że N1-P2 w konfiguracji dousznej nie wychodzi wiarygodnie
- **K-016** — przypisałem El-Robo-Mech rolę zewnętrznej walidacji; to konkurs o indeks, 34 laureatów
- **K-019, najpoważniejszy** — potraktowałem rozwiązanie designowe („za uchem, wielkości aparatu słuchowego") jak wymaganie wejściowe i projektowałem pod nie cały etap, zamiast zapytać, gdzie ma być interfejs, i porównać miejsca. **Koszt: opisałem jako ścianę fizyczną projektu coś, co było skutkiem niepostawionej decyzji.** Przy każdej luce designowej pytać, nie zakładać

**Wzorzec wspólny dla K-014, K-015 i K-019:** budowanie mocnego twierdzenia na własnym założeniu, bez sprawdzenia. To jest błąd nr 5 z sekcji 8 handbooka w trzech odsłonach.

---

## 6. Sprawy techniczne środowiska

- **sieć:** polityka idzie ze środowiska sesji i **sesji nie da się przenieść między środowiskami**. Poprzednia sesja siedziała w `env_01NdKrhepeQo6dVAHusCvQFj` („Projekty"), podczas gdy `Full` było ustawione na `env_01USAAMBR9QZf9W8ERvrVkEA` („Projekty Full Acess"). Nową sesję zakładać w tym drugim
- **gałąź:** cały dorobek etapu 1 jest na `claude/etap-1-8fsbpm`. Jeżeli nowa sesja pobierze `main`, zobaczy stan sprzed 15 VIII
- przy zapisie plików uważać na zabłąkane znaczniki zamykające — poprzednia sesja zostawiła `</content>` w trzynastu plikach
