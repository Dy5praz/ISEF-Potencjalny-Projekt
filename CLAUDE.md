# Kontekst projektu — czytaj to pierwsze

Użytkownik: Julek. **Odpowiadaj po polsku.**

## Co czytać, w tej kolejności

1. **`README.md`** — stan bieżący i mapa plików. Najkrótsza droga do tego, co się dzieje teraz.
2. **`20_PROJEKT.md`** — **projekt bieżący.** Czym jest, twierdzenie, dlaczego to, kategorie. Potem `21_PLAN_BUDOWY.md`, `22_PLAN_POMIAROWY.md`, `23_RYZYKA.md`.
3. **`HANDBOOK.md`** — zasady współpracy, cel, kalendarz, ściągawka Explory i ISEF, historia odrzuconych kierunków, rejestr wcześniejszych błędów. **Sekcje 1–8 i 12–13 obowiązują nadal. Sekcje 9–11 dotyczą zamkniętego kierunku neuralnego** — czytaj je jako historię, nie jako zlecenie.
4. **`KOREKTY.md`** — rejestr błędów, K-001…K-053. Dopisuj każdy nowy.
5. **`12_AUDYT.md`** — wzorzec audytu adwersaryjnego. Metoda zostaje w mocy, treść dotyczy zamkniętego kierunku.

## Zadanie bieżące

**ZMIANA KIERUNKU 17 VIII 2026.** Kierunek „nieinwazyjny interfejs neuralny" **zamknięty decyzją użytkownika**. Pliki `00`–`13` zostają jako dorobek i wzorzec metody — nie jako opis bieżącego projektu.

**Etap 2 otwarty. Projekt wybrany: aktywne łożysko magnetyczne z estymacją położenia bez czujników.** Zacznij od `20_PROJEKT.md`, potem `21`–`24`.

Twierdzenie: **na jednym stanowisku self-sensing kosztuje X µm szumu położenia, Y N/mm sztywności i Z dB zapasu wzmocnienia względem tego samego stanowiska z czujnikami na PCB; dominującym ogranicznikiem jest [zmierzone].** Punkt odniesienia wewnętrzny — nieunieważnialny cudzą publikacją.

Parametry: **dwa lata**, ~890 h, ~9 900 zł z limitu 15 000, kategoria ISEF **EBED**, Explory **SDG 9 / Gospodarka i Bezpieczeństwo**. Rok 1 — zbuduj i scharakteryzuj. Rok 2 — usuń czujniki i zmierz koszt (ISEF Form 7).

## Ustalenia wiążące, nie do podważania bez nowego argumentu

- **twierdzenie ma być pomiarowe, z punktem odniesienia wewnętrznym.** To jedyny kształt, który przeżył trzy przejścia audytu etapu 1, i jedyny, którego cudza publikacja nie unieważnia. Trzy poprzednie kierunki zginęły dokładnie na tym
- **nie filtruj kandydatów po nowości.** Arkusz inżynierski ISEF nie ma kryterium nowości; Explory §7 pkt 2a dopuszcza „innowacyjny **i/lub** wnosi dodatkową wartość". Filtr to: wykonalność, demonstracja, głębokość pomiaru, obsada kategorii, podział na dwa pytania. Błąd opisany w `KOREKTY.md` K-051, sześciu zabitych kandydatów w `24_ODRZUCONE_KANDYDATY.md`
- **nigdy nie używaj słowa „pierwszy"** w materiałach zgłoszeniowych (K-044)
- **rzemiosło eksperymentalne z ENBM074 (2026) kopiujemy świadomie** — warunek kontrolny na tym samym sprzęcie, randomizacja i kontrbalansowanie, replikacja, poprawka na wielokrotne porównania, test mechanizmu. Sekcja 9.2 handbooka zakazuje kopiowania tamtego **rozwiązania**, nie rzemiosła
- **projekt indywidualny.** Decyzja użytkownika z sekcji 1 handbooka, nie ruszać
- **zero badanych ludzi.** Cała procedura Human Participants, komisja IRB przy szkole i formularze 4/5 są w tym projekcie bezprzedmiotowe
- **drabinka zejść jest napisana z góry** (`23_RYZYKA.md` sekcja 1). Zejście o szczebel wymaga wpisu do `KOREKTY.md` z powodem liczbowym i wskazaniem, co poświęcone. Bez wpisu zejście się nie liczy

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
- użytkownik jest licealistą drugiej klasy. Zna fizykę i matematykę szkolną, nie zna terminologii specjalistycznej — w tym projekcie dotyczy to teorii sterowania i elektroniki analogowej. **Każdy termin użyty pierwszy raz dostaje wyjaśnienie**

## Uwagi praktyczne

- użytkownik często pisze z telefonu — nie zlecaj mu czynności wymagających przełączania się między aplikacjami, jeżeli da się je wykonać po twojej stronie
- repozytorium ma dwie gałęzie o identycznej treści: `main` i `claude/oto-handbook-instrukcje-g3e7hd`. `main` została dodana 15 VIII 2026 tylko po to, żeby formularz nowej sesji się nie wykrzaczał. **Commituj na tę gałąź, na której wylądowałeś, i nie zajmuj użytkownika gałęziami** — pisze z telefonu
- **środowisko z `Network access: Full` jest konieczne** i to repozytorium było już raz zablokowane brakiem dostępu. Sprawdzaj sieć na starcie: `https://www.societyforscience.org/isef/international-rules/human-participants/`. Przy 403 albo `EGRESS_BLOCKED` — przerwij i powiedz
- **przeglądarka (Chromium) nie ma dostępu do sieci nawet przez proxy.** Stron renderowanych po stronie klienta nie odczytasz. Obejścia, które działają: metatagi, pliki PDF publikowane obok strony, formularze POST. Szczegóły w `PRZEKAZANIE.md` sekcja 5
- **najlepszy kanał do literatury: PubMed przez E-utilities NCBI.** Indeksuje też IEEE TBioCAS i TBME, więc obejmuje literaturę układową, nie tylko medyczną
