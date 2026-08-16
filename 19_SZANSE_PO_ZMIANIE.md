# 19 — Szanse po zmianie osi

**Data:** 16 sierpnia 2026
**Podstawa:** `HANDBOOK.md` §11 punkt 4 — *„ocena szans osobno dla Explory i osobno dla ISEF, z rozbiciem na etapy"*.
**Po co osobny plik:** liczby w `11_OCENA_SZANS.md` i `13_PODNIESIENIE_SZANS.md` §8.2 były liczone dla **starej osi**. Oś się zmieniła, więc ocena wymaga rewizji, a nie przepisania.

---

## 1. Co się zmieniło i w którą stronę

### Na korzyść

| Zmiana | Waga |
|---|---|
| **wielkość mierzonego efektu: 0,3 pp → 9–24 pp** | **największa.** To jest różnica między projektem, który prawdopodobnie nie zmierzy nic, a takim, który prawie na pewno zmierzy coś |
| **prior art czysty w trzech bazach** dla nowej osi, wobec starej osi z nazwanym konkurentem | średnia |
| **reanaliza cudzych danych jako materiał na rubryki** | **niedoceniana i duża** — patrz §2 |
| **sprzęt się uprościł** o jedną elektrodę, i to tę leżącą najbardziej niewygodnie (twarz) | mała |
| efekt wykrywalny **na jednej osobie**, więc kampania nie zależy od komisji IRB | średnia |

### Na niekorzyść

| Zmiana | Waga |
|---|---|
| **wariant C: brak jednego zdania twierdzenia do pierwszych pomiarów** | średnia, z terminem 31 XII 2026 (R11) |
| **R4 podniesione z 15% na 25%** — nie wiadomo, czy strata montażu przeżyje pod TRCA (§6B pliku `14`) | średnia |
| **nowa oś mierzy KOSZT, nie przewagę** — patrz §3, bo to jest realne napięcie | **duża** |

---

## 2. Rzecz, która podnosi szanse najbardziej, i nie jest sprzętem

**Reanaliza z `14_REANALIZA.md` jest sama w sobie mocnym materiałem konkursowym** i to w rubrykach, które są punktowane wprost:

| Kryterium | Gdzie | Co wnosi reanaliza |
|---|---|---|
| „znajomość dotychczasowych badań w dziedzinie" (0–10) | **Explory, półfinał** | nie streszczenie cudzej pracy, tylko **odtworzenie jej wyniku z surowych danych i wskazanie, co z niej naprawdę wynika** |
| `Research Problem` (10 pkt) | **ISEF, arkusz inżynierski** | problem wyprowadzony z **własnego pomiaru na cudzych danych**, a nie z akapitu „w literaturze brakuje" |
| „znajomość zastosowanych metod i założeń" (0–10) | Explory, półfinał | pipeline zwalidowany wobec publikacji co do trzeciego miejsca po przecinku |
| `Creativity` (20 pkt) | ISEF | dwie kontrybucje zamiast jednej (`13` §5) |

`[wniosek]` **Licealista, który odtworzył wynik recenzowanej pracy z jej surowych danych i pokazał, że powszechna interpretacja tego wyniku jest błędna, ma na starcie coś, czego nie ma prawie nikt w stawce.** To nie wymaga ani złotówki, ani działającego prototypu, i jest **już zrobione**.

**Ostrzeżenie do tego akapitu:** to jest atut tylko wtedy, gdy reanaliza jest **wstępem do własnego pomiaru**, a nie zamiast niego. Sama reanaliza to projekt czysto obliczeniowy, przed którym ostrzega `HANDBOOK.md` §9.4.

---

## 3. Napięcie, którego nie wolno zamieść — nowa oś mierzy koszt

Decyzja C2 ustawiła kształt twierdzenia jako: *„przepustowość porównywalna z układem wielolektrodowym przy module zwartym zamiast opaski"*. Czyli **przewaga**.

**Nowa oś mierzy coś przeciwnego:** ile przepustowości **traci się** przez zejście do modułu zwartego. Jeżeli wyjdzie 41% ITR, wynik brzmi „forma noszalna jest droga" — prawda, użyteczna, publikowalna, ale **nie jest to „lepsze od komercyjnych"**, czego użytkownik chciał od początku (`HANDBOOK.md` §9.1).

**Rozwiązanie, i jest uczciwe, a nie retoryczne:** twierdzenie formułuje się jako **wyznaczenie progu**, nie jako pomiar straty — tak jak już stoi w `15_PROJEKT.md` §1.1:

> *wyznaczam najmniejszą odległość elektrody odniesienia, przy której układ zachowuje przepustowość montażu z odniesieniem odległym — czyli najmniejszy gabaryt, przy którym urządzenie noszalne jeszcze działa*

To jest **reguła projektowa**, czyli produkt dodatni: coś, czego przed projektem nie było, a po projekcie jest, i z czego może skorzystać każdy budujący noszalny interfejs SSVEP. `[wniosek]` **Zdolność, nie pomiar** — czyli dokładnie to rozróżnienie, którego brak handbook wymienia jako mój błąd numer 9.

**Warunek, żeby to nie było naciąganiem:** próg musi istnieć. Jeżeli spadek okaże się gładki i monotoniczny bez progu, twierdzenie trzeba przeformułować na krzywą kompromisu (gabaryt wobec przepustowości), co jest słabsze narracyjnie, ale nadal jest regułą projektową. **Zapisuję to teraz, przed pomiarem.**

---

## 4. Przeliczenie

Punkt wyjścia: tabela z `13_PODNIESIENIE_SZANS.md` §8.2. Zmieniam tylko te wiersze, na które zmiana osi realnie wpływa.

| Wynik | `13` §8.2 | **Po zmianie osi** | Dlaczego |
|---|---|---|---|
| kwalifikacja do półfinału Explory | 85% | **88%** | rubryka „znajomość dotychczasowych badań" wzmocniona reanalizą; etap I ocenia znajomość tematu, nie prototyp |
| awans do finału Explory | 39% | **42%** | jw. plus dwie kontrybucje zamiast jednej |
| reprezentacja na ISEF | 16% | **17%** | bez istotnej zmiany — o tym decyduje prezentacja i stawka, nie oś |
| Nagroda Zrównoważonego Rozwoju | 6,5% | 7% | |
| Nagroda Główna Explory | 6% | 6% | bez zmian |
| jakakolwiek nagroda finansowa Explory | 17% | **18%** | |
| jakakolwiek nagroda na ISEF | 10% | **11%** | mocniejszy `Research Problem`, EBED bez zmian |
| Grand Award w kategorii ISEF | 6,4% | **7%** | |
| miejsce I–II na ISEF | 2,8% | **3%** | |
| **jakikolwiek wymierny sukces konkursowy** | 58% | **63%** | **największa zmiana i najbardziej uzasadniona** |

### Dlaczego ostatni wiersz rośnie najmocniej

`[wniosek]` „Wymierny sukces" wymaga przede wszystkim tego, żeby **projekt cokolwiek zmierzył**. Przy starej osi efekt do wykrycia wynosił 0,3 pp przy rozrzucie 8 pp — czyli najbardziej prawdopodobnym wynikiem kampanii było **„nic nie wyszło"**, i to niezależnie od jakości wykonania. Przy 9–24 pp prawdopodobieństwo, że kampania da jakąkolwiek liczbę nadającą się na plakat, jest bardzo wysokie.

**To jest właściwa miara tej zmiany:** nie „projekt stał się lepszy", tylko **„projekt przestał być skazany na wynik zerowy"**.

### Czego te liczby nie obejmują

`[luka]` Największa niepewność nie leży w osi, tylko w **R1** — u 10–30% ludzi SSVEP praktycznie nie działa, a plan do maja 2027 jest jednoosobowy. **Wszystkie liczby powyżej są warunkowe wobec tego, że autor nie jest takim przypadkiem.** Bezwarunkowo trzeba je przemnożyć przez ~0,8. Rozstrzygnięcie: **październik 2026, jedno popołudnie**.

---

## 5. Trzy wymiary, nie same szanse

Handbook §2.2 wymaga oceny w trzech wymiarach.

| | Stara oś | **Nowa oś** |
|---|---|---|
| **prawdopodobieństwo** | wynik zerowy najbardziej prawdopodobny | wynik niezerowy prawie pewny, jeśli sprzęt zadziała |
| **sterowalność** | niska — efekt 0,3 pp nie zależy od jakości wykonania, tylko od fizjologii | **wysoka** — efekt zależy od geometrii, którą projektuje i wykonuje autor |
| **koszt porażki** | miesiące pracy i wynik nieraportowalny | **niski** — każdy wynik jest raportowalny, bo mierzy się koszt formy, a nie istnienie przewagi |

**Największa poprawa jest w sterowalności**, i to jest ten wymiar, który handbook każe ważyć osobno od prawdopodobieństwa. Nowa oś oddaje wynik w ręce tego, kto lutuje.

---

## 6. Kiedy tę ocenę trzeba będzie zrewidować

1. **po pierwszym własnym pomiarze (X 2026)** — rozstrzyga R1, czyli mnożnik 0,8
2. **po pomiarze pod TRCA na własnym stanowisku** — rozstrzyga R4, czyli czy przewidywanie 9–24 pp w ogóle się utrzymuje
3. **po wyborze osi (do 31 XII 2026)** — dopóki trwa wariant C, twierdzenie nie ma jednego zdania

**Do tego czasu te liczby są prognozą, nie pomiarem, i tak je traktować.**
