# Kontekst projektu — czytaj to pierwsze

Użytkownik: Julek. **Odpowiadaj po polsku.**

## Co czytać, w tej kolejności

1. **`HANDBOOK.md`** — jedyne źródło kontekstu. Zasady współpracy, cel, kalendarz, ściągawka Explory i ISEF, historia odrzuconych kierunków, rejestr wcześniejszych błędów, opis zlecenia. **Przeczytaj w całości, zanim cokolwiek zrobisz.**
2. **`00_PYTANIA_I_LUKI.md`** — luki i sprzeczności znalezione w handbooku, odpowiedzi użytkownika z dwóch rund pytań, oraz **lista 12 zadań weryfikacyjnych na etap 1 z priorytetami** (sekcja 4d).
3. **`KOREKTY.md`** — rejestr błędów. Dopisuj każdy nowy.
4. **`README.md`** — stan prac i struktura docelowa.

## Zadanie bieżące

**Etap 1 handbooka: przemiał literatury.** Pełny zakres, bez skrótów, bez pracy w ratach. Pliki docelowe wymienione w `README.md`.

Kolejność startowa — sekcja 4d pliku `00_PYTANIA_I_LUKI.md`. Trzy pierwsze pozycje mogą wywrócić plan, a nie tylko go poprawić:
1. który finał Explory wyłania reprezentację na ISEF 2028
2. wymogi ISEF wobec badań na sobie i wobec opiekuna naukowego
3. czy sprzętowe usuwanie zakłóceń mięśniowo-ocznych przy uchu jest już zajęte

## Ustalenia wiążące, nie do podważania bez nowego argumentu

- kierunek: **nieinwazyjny interfejs neuralny**. **Umiejscowienie: DECYZJA OTWARTA** — forma zauszna była założeniem, nie wymaganiem. Rzeczywiste wymaganie: niewidoczne albo nierozpoznawalne jako sprzęt, zero hełmów. Porównanie miejsc i cztery pytania: `09_UMIEJSCOWIENIE.md`, błąd opisany w `KOREKTY.md` K-019
- zdolność: **sterowanie, nie komunikacja**
- **odczyt dyskretny, zachowanie sterowanego obiektu ciągłe** — odczyt ciągły wymusza elektrody nad korą ruchową, czyli hełm, co łamie twarde wymaganie
- sEMG/EOG: dopuszczone jako **kanał odniesienia do usuwania zakłóceń**, nie jako źródło sterowania
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
- **etap 1 wymaga środowiska z `Network access: Full`.** Przy poziomie `Trusted` zablokowane są bazy publikacji, strony konkursów i wyszukiwarki naukowe — sprawdzone empirycznie 15 VIII 2026, szczegóły w `00_PYTANIA_I_LUKI.md` sekcja 0
