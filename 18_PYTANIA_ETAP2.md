# 18 — Pytania do Ciebie, etap 2, runda 1

**Data:** 16 sierpnia 2026
**Zasada:** pytania grupami, konkretne, **po wykonaniu własnej pracy, nigdy zamiast niej** (`HANDBOOK.md` §2.2). Praca jest w plikach `14`–`17`. Żadne z tych pytań nie blokuje dalszej roboty — na każde mam wariant domyślny i mogę go przyjąć, jeśli nie chcesz się teraz tym zajmować.

---

## P1 — oś projektu. Jedyne pytanie, które naprawdę wymaga Twojej decyzji

**Co się stało:** zbiór danych, na którym stoi oś projektu, okazał się publiczny. Pobrałem go i policzyłem. **Przyrost +9 pp, wokół którego zbudowaliśmy twierdzenie, pochodzi od elektrody Cz na czubku głowy, a nie od kanału szczękowego.** Szczęka dokłada około **0,3 punktu procentowego**. Sprawdzone dwoma niezależnymi klasyfikatorami, po odtworzeniu tabeli autorów co do trzeciego miejsca po przecinku.

Rozbiór: `14_REANALIZA.md`. Rejestr błędu: `KOREKTY.md` K-051.

**Trzy warianty:**

| | Co robimy | Wielkość mierzonego efektu | Ile osób trzeba, żeby to wykryć |
|---|---|---|---|
| **A — zmiana osi** (rekomendacja) | mierzymy, jak przepustowość zależy od **odległości elektrody odniesienia** od potylicy, czyli od gabarytu modułu | **9–24 pp** | **jedna, powtórzeniami** |
| B — stara oś bez zmian | mierzymy kompensację artefaktu szczękowego | 0,2–0,4 pp | rzędu 3000 |
| **C — nie decydować teraz** | budujemy sprzęt, który obsługuje obie, i wybieramy po pierwszych własnych pomiarach | — | — |

**Moja rekomendacja: C, z domyślnym przechyleniem na A.** Powód jest ten sam, dla którego zgodziłeś się nie wybierać umiejscowienia założeniem: **sprzęt nie zmienia się ani o jeden element** między A i B (`15_PROJEKT.md` §1.4), więc odłożenie decyzji nic nie kosztuje, a decyzja podjęta po własnym pomiarze jest warta więcej niż podjęta teraz.

**Czego potrzebuję: „A", „B" albo „C".** Jeżeli nic nie odpiszesz, idę dalej wariantem C i piszę wszystko tak, żeby obie osie były otwarte.

---

## P2 — czy wolno wyprowadzić sam przewód odniesienia za ucho

**Dlaczego pytam:** decyzja 2 zamknęła umiejscowienie na module zwartym, **bez łuku i bez zausznika**. Pomiar pokazał, że elektroda odniesienia **wewnątrz** modułu kosztuje 9–24 pp dokładności — bo dwie bliskie elektrody nad korą wzrokową widzą ten sam sygnał i odejmowanie kasuje go razem z zakłóceniem.

**Rozróżnienie, którego wtedy nie zrobiłem:** K-036 odrzucał **drugie miejsce elektrod aktywnych** (drugi zestaw czujników). Nie odrzucał **pojedynczej elektrody odniesienia na cienkim przewodzie**. Twoja tabela gabarytowa z decyzji 3 dopuszcza wprost: *„cienki przewód lub łuk między modułami, przy głowie"* — przechodzi.

**Pytanie: czy jeden cienki przewód od modułu potylicznego do elektrody za uchem (wyrostek sutkowaty) mieści się w Twojej granicy?**

- **jeżeli tak** — mamy pełny zakres pomiarowy od 2 do 10 cm i projekt ma o co pytać
- **jeżeli nie** — zakres kończy się na ~4 cm (kark poniżej guzowatości potylicznej, nadal w obrysie modułu), pomiar dalej ma sens, ale **prawdopodobnie zmierzymy, że urządzenie w tej formie traci kilkanaście punktów procentowych** i to będzie główny wynik projektu. **To też jest uczciwy wynik**, tylko mniej wygodny do sprzedania

**Wariant domyślny, jeżeli nie odpiszesz:** projektuję złącze tak, żeby przewód odniesienia dało się wpiąć albo nie wpinać. Koszt: jedno gniazdo.

---

## P3 — trzy rzeczy, których nie da się załatwić po mojej stronie

Bez zmian od etapu 1, ale teraz jedna z nich zmieniła wagę.

1. **Mail do FZT** (`konkurs@fzt.org.pl`): czy organizator prowadzi SRC pełniące funkcję komisji IRB dla polskich uczestników ISEF. **Plus drugie pytanie w tym samym mailu:** czy start w Explory można łączyć z EUCYS.
2. **Rozmowa z dyrekcją o komisji IRB.** **Ta pozycja urosła** — nie jest już „na wszelki wypadek". Jest planem awaryjnym na ryzyko R1: u 10–30% ludzi SSVEP praktycznie nie działa, a w danych, które analizowałem, jedna osoba na dwanaście miała 40% dokładności przy poziomie losowym 33%. **Jeżeli Ty okażesz się takim przypadkiem, jedyną drogą dalej jest badanie kogoś innego, a to wymaga komisji.**
3. **Pisemna zgoda opiekuna szkolnego** na role Adult Sponsor i Direct Supervisor. Magister wystarcza. Tanie, bez terminu.

**Czego potrzebuję: nic teraz.** To jest lista na wrzesień–październik. Zapisuję ją, żeby nie wypadła z pola widzenia.

---

## P4 — sprzęt pomiarowy. Pytanie B3 z etapu 1, nadal bez odpowiedzi

Jedyna luka z etapu 1, która realnie blokuje część planu. Bez przyrządu o niskim szumie własnym nie da się **udowodnić**, że własny wzmacniacz działa — a dowód jest połową twierdzenia w rubryce `Execution`.

**Konkretnie, co jest w domu albo do pożyczenia przez brata:** oscyloskop (jaki, jakie pasmo), generator sygnałowy, zasilacz laboratoryjny, multimetr (jaki), karta pomiarowa, stacja lutownicza z regulacją.

**Wariant domyślny, jeżeli nie odpiszesz:** zakładam, że nie ma nic poza multimetrem i stacją lutowniczą, i planuję pomiar szumu **samym torem** (zwarte wejście, RMS z próbek przetwornika 24‑bitowego — `03_SCIANY_FIZYCZNE.md` §6). Wtedy CMRR i jitter podaję jako wartości katalogowe ADS1299 **z jawnym zaznaczeniem, że nie są własnym pomiarem**. To jest słabsze i wolałbym tego uniknąć.

**Terminowo:** to nie jest pilne. Przyrząd jest potrzebny na gotową płytkę, czyli **luty 2027**. Zasób „brat" jest jednorazowy i planuję go właśnie na wtedy, nie wcześniej.

---

## P5 — budżet, i tym razem z liczbami po mojej stronie

W etapie 1 świadomie nie ustaliłeś budżetu: *„najpierw opracowanie, potem ocena kosztu"*. Opracowanie jest, więc podaję koszt.

| | Kwota |
|---|---|
| platforma odniesienia (OpenBCI, elektrody, stymulator), jesień 2026 | 2 800–4 000 zł |
| własny tor analogowy (ADS1299, PCB, obudowa, elektrody), wiosna 2027 | 1 600–2 800 zł |
| rezerwa 30% na drugą serię płytek | 1 300–2 000 zł |
| **razem** | **5 700–8 800 zł** |

**Ceny są rzędem wielkości, nie ofertą** — sklepy renderują ceny po stronie klienta, a przeglądarka w tym środowisku nie ma sieci. Jedyna pozycja odczytana u producenta: ADS1299 w cenniku TI, **45,9–69,8 USD**.

**Pytanie nie brzmi „ile masz".** Brzmi: **czy największa pojedyncza pozycja, czyli ~3 000 zł na kupioną platformę odniesienia, jest do przyjęcia.** Bo to jest pierwsze miejsce, które ktoś by ciął, a cięcie go oznacza przyjęcie ryzyka R2 — że przy pierwszej nieudanej rejestracji nie będzie wiadomo, czy zawiódł wzmacniacz, elektrody, bodziec, czy klasyfikator. **Bez punktu odniesienia pierwsza porażka jest nierozstrzygalna i kosztuje miesiące.**

**Wariant domyślny:** planuję z platformą kupioną.

---

## Co robię dalej, niezależnie od Twoich odpowiedzi

Żeby było jasne, że to nie jest praca w ratach — oto co jest do zrobienia i co nie czeka na Ciebie:

1. **Przeszukanie Crossref, arXiv i patentów dla nowej osi.** Dla nowej osi zrobiłem tylko PubMed. To jest dokładnie ten błąd, który `PRZEKAZANIE.md` §5 wymienia jako wzorzec numer 1 — zmiana konfiguracji bez powtórzenia audytu. **Zgłaszam go na sobie, zanim kosztował**, i domykam przed jakimkolwiek zakupem
2. **TRCA i krzywa dokładność–czas** na danych Kołodzieja — dokończenie toru B
3. **Tabela kolizji harmonicznych** dla ośmiu proponowanych częstotliwości bodźca
4. Regulaminy **El-Robo-Mech XII** i **OITwEiM 2026/27**, gdy się ukażą jesienią
