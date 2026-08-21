# 02 — Twierdzenie, metryka i granice

**Stan na 21 sierpnia 2026.** Ten plik zawiera **wyłącznie stan obowiązujący.** Historia zmian twierdzenia: `11_EWOLUCJA.md`.

---

## 1. Zdanie obowiązujące

> **Mierzę, o ile spada dokładność i przepustowość interfejsu SSVEP, gdy elektroda odniesienia musi zmieścić się w module noszonym na potylicy zamiast leżeć w miejscu standardowym, i wyznaczam najmniejszą odległość odniesienia od kory wzrokowej, przy której przepustowość jeszcze się nie załamuje — na jednym własnym torze analogowym, tą samą osobą, tym samym paradygmatem.**

**Zmienna niezależna jest dwuwymiarowa:**

| Wymiar | Zakres |
|---|---|
| **odległość** odniesienia od Oz | ~2, ~3,5, ~7, ~10 cm |
| **kierunek** | **w górę (POz)** wobec **w dół (podpotyliczny)**, przy zbliżonej odległości |

**Zmienne zależne:** dokładność klasyfikacji, **ITR wg wzoru Wolpawa**, SNR w prążku bodźca **i osobno w prążku drugiej harmonicznej**, impedancja kontaktu.

## 2. Metryka — i jeden bezwzględny zakaz

**Dokładność oraz ITR w bit/min wg Wolpawa, zawsze z podaniem N (liczba celów), P (dokładność) i t (czas na decyzję, z jawną konwencją liczenia).**

**Zakaz: nigdy słowa na minutę.** To jest jedyny mechaniczny strażnik granicy z projektem referencyjnym ENBM074 (2026). W chwili, gdy w materiałach pojawi się „słów na minutę", projekt staje się wariantem cudzej pracy.

**Zakaz drugi, wynikający z pierwszego: nigdy dokładność bez podanego N.** `[fakt]` Najlepszy przykład, dlaczego — praca w *PNAS* podaje **96,4%**, ale przy **dwóch celach**, co daje sufit ~17 bit/min, czyli **mniej niż jednokanałowa para POz−Oz przy czterdziestu celach**.

## 3. Punkt odniesienia

**Wewnętrzny, i to jest oś twierdzenia:** ten sam tor analogowy, ta sama osoba, ta sama sesja, **dwa położenia elektrody odniesienia**.

**Porównanie prowadzi się wobec dwóch baz naraz, nie jednej:**
1. montaż wielokanałowy z odniesieniem odległym — **górna granica**
2. **pojedynczy kanał z odniesieniem odległym — dolna granica**

`[fakt]` Powód drugiej bazy: Li i in. 2025 zmierzyli, że montaż dwubiegunowy POz−Oz **bije** pojedynczy kanał Oz z odniesieniem na czole (**68,25% wobec 37,65%**), podczas gdy reanaliza danych Kołodzieja pokazuje, że dwubiegunowy **przegrywa** z montażem trzykanałowym (48,8–64,0% wobec 73,3%). **Obie liczby są prawdziwe i dotyczą różnych porównań.** Bez drugiej bazy własny wynik da się przedstawić jako sprzeczny z opublikowaną pracą.

**Kupiony OpenBCI nie jest punktem odniesienia twierdzenia.** Pełni dwie role: test, czy SSVEP działa u autora, oraz ubezpieczenie, gdyby własny tor nie zadziałał.

## 4. Przewidywanie zapisane z góry

`[wniosek, wyprowadzenie z cudzych pomiarów — nie pomiar]` Pole SSVEP ma strukturę falową: fale biegnące o **λ > 15–20 cm**, propagujące się **potylica → przedczołowie** (Srinivasan i in. 2006, 110 elektrod; Thorpe i in. 2007). Dla pary elektrod odległej o `d` **wzdłuż osi propagacji** amplituda różnicy wynosi:

> **`|2 · sin(π·d/λ)|`**, względem amplitudy pojedynczej elektrody

| d | λ = 15 cm | λ = 20 cm |
|---|---|---|
| 2,0 cm | 0,81 | 0,62 |
| **3,5 cm (Oz–POz)** | **1,34** | **1,04** |
| 7,0 cm | 1,99 | 1,78 |

**Trzy przewidywania, wszystkie testowalne planem, który już istnieje:**

1. **strata zależy od `d/λ`, nie od samego `d`** — więc **musi zmieniać się z częstotliwością bodźca**. Zestaw 8,0–17,8 Hz przechodzi przez trzy różne reżimy falowe
2. **istnieje optimum odległości przy `d ≈ λ/2`** (7–10 cm, poza modułem); przy 3,5 cm jest się na ~70% maksimum, przy 2 cm na ~40%
3. **kierunek daje efekt większy niż odległość** — para 3,5 cm wzdłuż osi bije parę 7 cm w poprzek

`[luka]` **Czego ten model nie obejmuje:** źródeł lokalnych, rozmycia przez czaszkę, zanieczyszczeń z R12. Jest **najprostszym możliwym**, nie kompletnym. Wchodzi jako **przewidywanie**, nie jako opis.

## 5. Czym to twierdzenie NIE jest

- **nie jest twierdzeniem o pierwszeństwie.** Zakaz słowa „pierwszy" w materiałach obowiązuje bez wyjątku. Dobór odprowadzeń dla SSVEP badano od 2005 roku
- **nie jest twierdzeniem, że wygoda kosztuje.** Li i in. 2025 pokazali system noszalny bez straty; różnica polega na tym, **co** zostało zmniejszone — protokół przygotowania czy montaż
- **nie jest twierdzeniem o pobiciu kogokolwiek.** Imperial College robi 102 bit/min za £20
- **nie jest twierdzeniem o wynalezieniu elektrody ani modułu** — oba pola są gęsto zajęte, także patentowo

## 6. Dlaczego to twierdzenie przeżywa

1. **cudza publikacja go nie unieważnia** — degraduje z „nowe" na „potwierdzone niezależnie", a arkusz inżynierski ISEF **nie ma rubryki nowości**
2. **nie ma wyniku, który by je obalił** — jest tylko wynik, który zmienia jego znak. Mały koszt zwarcia to **lepsza** wiadomość o urządzeniu
3. **efekt jest o dwa rzędy wielkości większy** niż ten, który odpadł: 9–24 pp zamiast 0,2 pp
4. **uzasadnienie nie brzmi „nikt tego nie zrobił", tylko „trzy opublikowane wyniki są sprzeczne i nikt ich nie pogodził"** — a to jest odporne na znalezienie czwartej pracy

## 7. Trzy odpowiedzi przygotowane na pytania jurora

**„Czemu nie robisz tego, co DSTF-Net?"** (Yan i in. 2026, rekonstrukcja sygnału potylicznego z czołowego siecią neuronową)
> *Tamto rozwiązuje przypadek, w którym potylicy nie da się użyć w ogóle — pacjent leży, ma ubytek kości albo stabilizator. Wymaga sieci uczonej na parach sygnałów. Mój problem jest inny: potylica jest dostępna, tylko urządzenie musi być małe. Na to sieć nie odpowiada, bo pytanie brzmi, gdzie postawić elektrodę, a nie jak odtworzyć sygnał, którego nie ma.*

**„Czemu Twój sprzęt kosztuje więcej niż tamten za £20?"**
> *Tamto urządzenie ma dowieść, że da się tanio, i jest przeznaczone do masowego rozdawania w celach edukacyjnych. Moje ma zmierzyć zależność — a do tego potrzeba ośmiu kanałów rejestrowanych jednocześnie i znanej charakterystyki toru, czego tamto nie podaje.*

**„Przecież to wynika z fizyki objętościowego przewodzenia."**
> *Kierunek efektu owszem, wielkość nie. Różnica między −5 pp a −24 pp decyduje o tym, czy urządzenie w danym gabarycie ma sens, a fizyka jej nie podaje. Do tego dwie opublikowane prace dają dla tej samej operacji przeciwne znaki — Diez 2010 i Li 2025 mówią, że dwubiegunowy jest lepszy, moja reanaliza cudzych danych mówi, że gorszy. Skoro znaki są przeciwne, „to wynika z fizyki" przestaje być odpowiedzią.*

## 8. Kryterium porażki, zapisane przed pomiarem

**Twierdzenie upada, jeżeli:** spadek przepustowości na całym zakresie 2–10 cm wyniesie **poniżej 3 pp** i nie będzie monotoniczny **ani** zależny od kierunku. Wtedy nie ma czego mierzyć i wynik brzmi „położenie odniesienia nie ma znaczenia w tym zakresie" — co jest wynikiem negatywnym, **raportowanym w całości**.

`[fakt]` Wybieranie po fakcie metryki, która wypadła najlepiej, jest wymienione w Załączniku nr 1 regulaminu Explory jako naruszenie standardów etycznych.
