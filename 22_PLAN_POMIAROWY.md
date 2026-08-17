# 22 — Plan pomiarowy

**Data:** 17 sierpnia 2026

**Po co ten plik istnieje osobno.** `[fakt]` W arkuszu inżynierskim ISEF sekcja *Execution: Construction and Testing* jest warta **20 punktów** i punktuje wprost, czy prototyp był **testowany w wielu warunkach i próbach**. `[fakt]` Sekcja *Creativity & Potential Impact* — kolejne 20 — jest oceniana wg wytycznych przez *„research outcomes and analysis"*. Razem 40 ze 100 punktów zależy od tego pliku, a nie od tego, czy urządzenie ładnie wygląda.

`[fakt]` Do tego obserwacja z analizy stawki Explory: **żaden z 21 finalistów 2026 nie miał na plakacie pomiarów z niepewnościami.** Ten plik jest planem zajęcia miejsca, którego nikt nie zajmuje.

---

## 1. Zasada nadrzędna: warunek kontrolny na tym samym sprzęcie

**Jedyną zmienną między warunkiem badanym a kontrolnym jest źródło informacji o położeniu.** Ten sam wirnik, ten sam stojan, ten sam stopień mocy, te same nastawy regulatora, ta sama szczelina nominalna, ta sama temperatura, ta sama sesja pomiarowa.

`[wniosek]` To jest zapożyczone świadomie: projekt ENBM074 (2026) zdobył drugą nagrodę ISEF **strukturą eksperymentu**, nie sprzętem — warunek kontrolny na tym samym sprzęcie, próby randomizowane i kontrbalansowane, replikacja, poprawka na wielokrotne porównania, rozmiar efektu, test mechanizmu. Sekcja 9.2 handbooka zakazuje kopiowania **rozwiązania** tamtego projektu. **Nie zakazuje kopiowania rzemiosła** — i tu kopiuję rzemiosło.

**Randomizacja i kontrbalansowanie w tym projekcie znaczą konkretnie:** kolejność warunków (czujnik / estymator 1 / estymator 2) losowana w każdej sesji, a nie stała; połowa sesji zaczyna od czujnika, połowa od estymatora. Powód: stanowisko dryfuje termicznie w trakcie sesji, a stała kolejność wpisałaby dryf w wynik jako efekt metody.

---

## 2. Wielkości mierzone — rok 1

| # | Wielkość | Jednostka | Metoda |
|---|---|---|---|
| P1 | szum położenia przy nieruchomym wirniku | µm RMS + gęstość widmowa | zapis 60 s, min. 10 kHz |
| P2 | **sztywność statyczna** | N/mm | znane masy przez krążek linowy, przemieszczenie z czujnika |
| P3 | **sztywność dynamiczna (podatność)** | µm/N vs Hz | cewka pomocnicza jako siłownik zakłócający, przemiatanie |
| P4 | **transmitancja pętli otwartej** | dB, ° | przemiatany sinus wstrzykiwany w pętlę z mikrokontrolera |
| P5 | **zapas wzmocnienia i zapas fazy** | dB, ° | z P4 |
| P6 | pasmo zamkniętej pętli | Hz | z P4 |
| P7 | odpowiedź skokowa: przeregulowanie, czas ustalania | %, ms | skok zadanego położenia |
| P8 | maksymalne obciążenie statyczne do utraty lewitacji | N | obciążanie do zerwania |
| P9 | pobór mocy | W | pomiar na zasilaniu stopnia mocy |
| P10 | odpowiedź na niewyważenie vs prędkość obrotowa | µm vs obr/min | przemiatanie prędkości |
| P11 | dryf położenia przy nagrzewaniu | µm vs °C | 60 min od zimnego startu |

**Charakterystyka samego czujnika** (faza 2, przed zamknięciem pętli): czułość, liniowość, histereza, rozdzielczość, pasmo, dryf termiczny, wrażliwość na materiał celu. Osobna karta.

---

## 3. Warunki, w których to się mierzy

`[wniosek]` Punkty za *Execution* nie idą za jednym pomiarem, tylko za siatką.

| Zmienna niezależna | Poziomy |
|---|---|
| prędkość obrotowa | 0, potem 5–6 poziomów do maksimum |
| obciążenie statyczne | 0, 25, 50, 75% maksimum z P8 |
| szczelina nominalna | 2 ustawienia |
| nastawy regulatora | 3 zestawy: bezpieczny, nominalny, agresywny |
| temperatura stojana | zimny start, ustalona |
| **źródło położenia** | **czujnik / estymator 1 / estymator 2** (rok 2) |

**Liczba prób:** minimum **5 niezależnych powtórzeń** każdego punktu, gdzie „niezależne" znaczy **z ponownym opuszczeniem wirnika na łożyska zapasowe i ponownym poderwaniem**. Powtórzenie bez zerwania lewitacji nie jest niezależne i nie liczy się jako próba — bo nie zawiera zmienności ustawienia, która jest realnym składnikiem rozrzutu.

---

## 4. Budżet niepewności

`[wniosek]` Bez tego wszystkie liczby wyżej są dekoracją. Do policzenia i **wpisania na plakat**, nie do trzymania w zeszycie.

| Źródło | Jak oszacowane |
|---|---|
| kalibracja czujnika: wzorzec | działka i powtarzalność stolika mikrometrycznego |
| kalibracja czujnika: reszta dopasowania | odchylenie od prostej/wielomianu na przejeździe w obu kierunkach |
| dryf termiczny w trakcie sesji | z P11, przeniesione na czas trwania sesji |
| siła zakłócająca | niepewność masy × *g*, plus tarcie krążka — **do zmierzenia, nie do pominięcia** |
| kwantyzacja i szum przetwornika | z karty katalogowej + pomiar przy zwartym wejściu |
| powtarzalność montażu | rozrzut między 5 niezależnymi poderwaniami |

**Wynik podawany jako średnia ± niepewność rozszerzona, z podaną liczbą prób.** Nie „około 12 µm".

---

## 5. Rok 2 — eksperymenty rozdzielające mechanizm

To jest część, która odróżnia projekt „zmierzyłem, że jest gorzej" od projektu „zmierzyłem, o ile jest gorzej **i dlaczego**". Każdy wiersz to hipoteza z przewidywaniem, które da się obalić.

| Hipoteza o dominującym ograniczniku | Interwencja | Przewidywanie, jeśli hipoteza prawdziwa |
|---|---|---|
| **opóźnienie filtrów demodulacji** (opisane ograniczenie nr 2) | zmiana pasma filtru demodulacji w 4 krokach | zapas fazy zmienia się monotonicznie z pasmem; przy szerokim filtrze rośnie szum, przy wąskim spada zapas |
| **nasycenie magnetyczne** (nr 3) | zmiana prądu podkładu w 4 krokach | błąd estymaty rośnie nieliniowo powyżej progu; przy małym prądzie podkładu znika |
| **prądy wirowe w rdzeniu** | rdzeń lity vs pakietowany, oraz zmiana częstotliwości PWM | błąd zależy od częstotliwości; różnica między rdzeniami istotna |
| **sprzężenie skrośne osi** (nr 4) | pobudzenie jednej osi, pomiar błędu estymaty w drugiej | błąd w osi niepobudzanej skorelowany z pobudzeniem |

`[wniosek]` **Jeżeli żadna interwencja nie przesunie wyniku — to też jest wynik** i oznacza, że ogranicznik leży poza czterema hipotezami. Wtedy raportuje się cztery obalone hipotezy, co jest uczciwą i publikowalną treścią, a nie porażką.

**Poprawka na wielokrotne porównania** przy czterech rodzinach testów — do zastosowania i do wpisania w metodykę.

---

## 6. Co by znaczyło, że projekt się nie udał

Zapisane teraz, na zimno, żeby nie było później naginania.

| Wynik | Interpretacja | Czy nadaje się na konkurs |
|---|---|---|
| estymator gorszy od czujnika o zmierzoną wartość, mechanizm wskazany | **wynik zgodny z literaturą, oczekiwany** | **tak, to jest teza główna** |
| estymator porównywalny z czujnikiem | wynik mocniejszy niż zapowiada literatura | tak, bardzo |
| estymator nie utrzymuje lewitacji w ogóle, powód zmierzony | ograniczenie opisane w literaturze potwierdzone ilościowo na tanim sprzęcie | tak |
| estymator nie działa i **nie wiadomo dlaczego** | **to jest jedyna prawdziwa porażka** | nie — i dlatego sekcja 5 istnieje |
| stanowisko nie lewituje wcale | porażka wykonawcza, nie badawcza | nie — obsługiwane drabinką w `23_RYZYKA.md` |

**Zobowiązanie:** wynik raportowany jest taki, jaki wyszedł. `[fakt]` Standardy etyczne Explory (Załącznik nr 1, oparte na Kodeksie Etyki Pracownika Naukowego PAN) wymagają krytycyzmu wobec własnych wyników i nieprzekraczania obszaru własnej kompetencji; bazowanie na nieprawdziwych danych dyskwalifikuje na każdym etapie.

---

## 7. Dziennik

`[fakt]` Norma dokumentacyjna silnych wpisów inżynierskich w Explory to **dziennik postępu budowy z wersjonowanymi zdjęciami**, nie tabela na plakacie.

Prowadzony od fazy 0, jeden wpis na sesję warsztatową: data, co zrobione, co nie wyszło, zdjęcie. **Wpisy o tym, co nie wyszło, są ważniejsze od wpisów o sukcesach** — w rozmowie z jurorem ISEF pytanie „co poszło nie tak i co z tym zrobiłeś" pada częściej niż pytanie o wynik, a jest warte części z 25 punktów za rozmowę.

Dziennik jest jednocześnie **dowodem, że praca jest własna**, i materiałem na Form 7 w roku drugim.
