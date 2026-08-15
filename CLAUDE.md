# Kontekst projektu — czytaj to pierwsze

Użytkownik: Julek. **Odpowiadaj po polsku.**

## Co czytać, w tej kolejności

1. **`HANDBOOK.md`** — jedyne źródło kontekstu. Zasady współpracy, cel, kalendarz, ściągawka Explory i ISEF, historia odrzuconych kierunków, rejestr wcześniejszych błędów, opis zlecenia. **Przeczytaj w całości, zanim cokolwiek zrobisz.**
2. **`00_PYTANIA_I_LUKI.md`** — luki i sprzeczności znalezione w handbooku, odpowiedzi użytkownika z dwóch rund pytań, oraz **lista 12 zadań weryfikacyjnych na etap 1 z priorytetami** (sekcja 4d).
3. **`KOREKTY.md`** — rejestr błędów. Dopisuj każdy nowy.
4. **`README.md`** — stan prac i struktura docelowa.

## Zadanie bieżące

**Etap 1 ZAMKNIĘTY 15 VIII 2026 wieczorem.** Wszystkie źródła odczytane w oryginale, szesnaście korekt w `KOREKTY.md` (K-020…K-035). Trzy pozycje startowe rozstrzygnięte:
1. finał Explory X 2027 → ISEF V 2028 — **potwierdzone cytatem z regulaminu**, §8 pkt 7c
2. badanie na sobie **zwolnione** z uprzedniej zgody komisji; osobnej kategorii ryzyka dla urządzeń elektrycznych **nie ma**; Qualified Scientist **nie wymaga doktoratu**
3. oś projektu: wersja ogólna zajęta od 1983, analogowa dla artefaktów ruchowych od 2019. **Twierdzenie musi być pomiarowe, nie o pierwszeństwie**

**Etap 2: opracowanie projektu.** Czeka na cztery decyzje użytkownika — `README.md`, sekcja „Decyzje czekające na użytkownika". **Nie rozstrzygaj C2 samodzielnie** — poprzednia rekomendacja została wycofana, bo stała na błędnej liczbie (K-028).

Zacznij od `00_STRESZCZENIE.md` sekcja 0 i od `PRZEKAZANIE.md`.

## Ustalenia wiążące, nie do podważania bez nowego argumentu

- kierunek: **nieinwazyjny interfejs neuralny**. **Umiejscowienie: DECYZJA OTWARTA** — forma zauszna była założeniem, nie wymaganiem. Rzeczywiste wymaganie: niewidoczne albo nierozpoznawalne jako sprzęt, zero hełmów. Porównanie miejsc i cztery pytania: `09_UMIEJSCOWIENIE.md`, błąd opisany w `KOREKTY.md` K-019
- zdolność: **sterowanie, nie komunikacja**
- **odczyt dyskretny, zachowanie sterowanego obiektu ciągłe** — odczyt ciągły wymusza elektrody nad korą ruchową, czyli hełm, co łamie twarde wymaganie
- sEMG/EOG: dopuszczone jako **kanał odniesienia do usuwania zakłóceń**, nie jako źródło sterowania. **Doprecyzowanie po K-026: chodzi o EMG szczęki. Mrugnięcie przy uchu nie psuje sygnału i nie wymaga kompensacji**
- projekt referencyjny ENBM074: **dowód istnienia, nie wzorzec.** Nie proponuj wariantów tamtego rozwiązania, nie ustawiaj tamtego wyniku jako progu. Patrz sekcja 9.2 handbooka
- badani: najpierw sam autor; grupa dopiero po zgodzie komisji ISEF
- programowanie dopuszczone jako oś projektu, ale nie rozdmuchuj go ponad to, czego wymaga twierdzenie

## Zasady, których łamanie kosztowało miesiące

Pełna lista w sekcjach 2.1 i 2.2 handbooka. Skrót:

- **znaczniki pewności przy każdym stwierdzeniu:** `[fakt]` `[wniosek]` `[domysł]` `[luka]`. Jeżeli większość odpowiedzi to zgadywanie — powiedz to w pierwszym zdaniu
- **zakaz „nie da się"** bez kompletu trzech: który parametr się nie spina (liczba), wersja projektu z tym parametrem poza pętlą, pomiar przeżywający tę zmianę
- **nie pracuj w ratach.** Zakaz kończenia zdaniem „sprawdzę to w następnej wiadomości"
- **weryfikuj 2–3 razy** każdą liczbę, na której cokolwiek stoi. Jedno źródło — oznacz to przy twierdzeniu, nie w przypisie
- **nie zaczynaj od przyznania racji.** Ale nie podważaj odruchowo, kiedy rozumowanie jest prawidłowe
- **bez emotek**
- zwroty zakazane: „Świetne pytanie", „Masz całkowitą rację", „To ma głęboki sens", „Absolutnie", „Zdecydowanie"
- **dokumentacja żyje w plikach.** Jeżeli ustalenie z handbooka okaże się błędne — popraw handbook, nie tylko odpowiedź, i dopisz wpis do `KOREKTY.md`
- użytkownik jest licealistą drugiej klasy. Zna fizykę i matematykę szkolną, nie zna terminologii neurofizjologicznej. **Każdy termin użyty pierwszy raz dostaje wyjaśnienie**

## Uwagi praktyczne

- użytkownik często pisze z telefonu — nie zlecaj mu czynności wymagających przełączania się między aplikacjami, jeżeli da się je wykonać po twojej stronie
- repozytorium ma dwie gałęzie o identycznej treści: `main` i `claude/oto-handbook-instrukcje-g3e7hd`. `main` została dodana 15 VIII 2026 tylko po to, żeby formularz nowej sesji się nie wykrzaczał. **Commituj na tę gałąź, na której wylądowałeś, i nie zajmuj użytkownika gałęziami** — pisze z telefonu
- **środowisko z `Network access: Full` jest konieczne** i to repozytorium było już raz zablokowane brakiem dostępu. Sprawdzaj sieć na starcie: `https://www.societyforscience.org/isef/international-rules/human-participants/`. Przy 403 albo `EGRESS_BLOCKED` — przerwij i powiedz
- **przeglądarka (Chromium) nie ma dostępu do sieci nawet przez proxy.** Stron renderowanych po stronie klienta nie odczytasz. Obejścia, które działają: metatagi, pliki PDF publikowane obok strony, formularze POST. Szczegóły w `PRZEKAZANIE.md` sekcja 5
- **najlepszy kanał do literatury: PubMed przez E-utilities NCBI.** Indeksuje też IEEE TBioCAS i TBME, więc obejmuje literaturę układową, nie tylko medyczną
