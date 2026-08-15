# KOREKTY — rejestr błędów i poprawek

Zgodnie z sekcją 2.2 handbooka. Każdy wyłapany błąd ląduje tutaj z datą, treścią i poprawką.

Format wpisu: data | źródło błędu | co było źle | poprawka | kto wyłapał

---

## 2026-08-15

### K-001 — błąd arytmetyczny w handbooku, sekcja 3

**Co było źle:** „Do działającego prototypu ~14 miesięcy (El-Robo-Mech)".

**Poprawka:** od 14 VIII 2026 do ~15 IV 2027 jest **8 miesięcy**. Czternaście miesięcy to dystans do finału krajowego Explory w X 2027. Liczba 21 miesięcy do ISEF jest poprawna, 6,5 miesiąca do zamknięcia zgłoszeń też.

**Konsekwencja:** margines do pierwszego twardego terminu sprzętowego jest o 43% krótszy, niż podaje handbook, przy projekcie wymagającym nauki projektowania PCB od zera.

**Kto wyłapał:** Claude Code, przy drugim czytaniu wg sekcji 14.

---

### K-002 — luka z sekcji 4.2 była domknięta w tym samym akapicie

**Co było źle:** „[luka] Dokładna data kwalifikacji dla edycji 2027 — do zweryfikowania" postawiona zaraz po podaniu reguły, która ją rozstrzyga.

**Poprawka:** reguła przesunięcia o rok daje 1 I 2006 dla edycji 2027. Użytkownik, rocznik ok. 2010, spełnia z zapasem czterech lat. Luka schodzi z listy priorytetów do drobiazgu potwierdzanego przy zgłoszeniu.

**Kto wyłapał:** Claude Code.

---

### K-003 — sekcja 5.3 skleja trzy sita w jedną liczbę

**Co było źle:** „~300 zgłoszeń → ~3 miejsca w reprezentacji, rzędu 1%" użyte jako wskaźnik decyzyjny.

**Poprawka:** rozbicie na szanse warunkowe: zgłoszenie → półfinał ~50%, półfinał → finał ~14–17%, finał → reprezentacja ~12–14%.

**Konsekwencja strategiczna:** wąskie gardło jest w przejściu półfinał → finał, ocenianym w trzech czwartych po kryteriach zależnych od znajomości literatury i jakości prezentacji, nie po sprzęcie. Etap 1 nie jest przygotowaniem do właściwej pracy — jest bezpośrednio punktowany w najwęższym miejscu lejka.

**Kto wyłapał:** Claude Code.

---

### K-004 — liczby 65 i 3 wpm bez oznaczenia pewności

**Co było źle:** sekcja 9.2 oznacza projekt ENBM074 i autorstwo jako `[fakt]`, ale kluczowe liczby (~65 słów/min wobec ~3) nie mają żadnego znacznika, mimo że pochodzą z relacji ustnej.

**Poprawka:** obie liczby dostają status `[domysł]` do czasu odczytania pełnego abstraktu. W `/06_TABELA_PARAMETROW.md` musi istnieć kolumna „skąd ta liczba".

**Kto wyłapał:** Claude Code.

---

### K-005 — wniosek o składzie jury oparty na danych o edycję za wczesnych

**Co było źle:** sekcja 4.10 wyciąga wniosek „korzystne dla projektu na styku elektroniki i neurotechnologii" ze składu jury edycji 2026, podczas gdy nasza edycja to 2027. Ten sam handbook zaznacza, że 15 z 17 nazwisk pochodzi z jednego źródła.

**Poprawka:** wniosek zachowany, ale zdegradowany z przesłanki strategicznej do obserwacji. Nie budować na nim żadnej decyzji.

**Kto wyłapał:** Claude Code.

---

### K-006 — reguła 12/18 miesięcy nie została przełożona na daty

**Co było źle:** sekcja 5.4 podaje regułę i zaleca rezerwowanie zasobów jednorazowych „po czerwcu 2027", ale nie wylicza okna i nie sprawdza, co się z nim zderza.

**Poprawka:** przy ISEF ~V 2028 osiemnaście miesięcy wstecz to ~XI 2026, a okno dwunastu miesięcy ciągłych kończące się przy ISEF to ~V 2027 – V 2028. Handbook nie rozstrzyga, jak te dwie reguły się składają — do sprawdzenia w oryginale International Rules.

**Konsekwencja pominięta w handbooku:** pomiary pokazane na El-Robo-Mech (IV 2027) i w półfinale Explory (V–VI 2027) wypadają przed oknem albo na jego krawędzi i będą wymagały powtórzenia. Finał Explory (X 2027) mieści się w oknie. To pozycja harmonogramowa do wpisania w plan, nie niespodzianka na marzec 2028.

**Kto wyłapał:** Claude Code.

---

### K-007 — założenie, że finał X 2027 wysyła na ISEF V 2028, nie jest sprawdzone

**Co było źle:** cała teza „jeden strzał" z sekcji 3 stoi na tym założeniu, nigdzie niepopartym cytatem z regulaminu.

**Poprawka:** przeklasyfikowane na `[luka]` o najwyższej stawce. Jeżeli reprezentacja na ISEF 2028 została wyłoniona już na GEW X 2026, właściwym celem jest ISEF 2029 i cała ocena sensowności przedsięwzięcia wygląda inaczej.

**Status:** do sprawdzenia jako pierwsze po odblokowaniu dostępu do sieci.

**Kto wyłapał:** Claude Code.

---

### K-008 — nierozstrzygnięty rodzaj gramatyczny przy autorstwie ENBM074

**Co było źle:** handbook konsekwentnie używa rodzaju żeńskiego („autorka", „wygrała"). Jedno znalezione źródło wtórne używa rodzaju męskiego. Nie mam ustalenia.

**Poprawka:** do czasu potwierdzenia piszę neutralnie. Bez znaczenia merytorycznego, ale nie powielam nieustalonego szczegółu o realnej osobie.

**Kto wyłapał:** Claude Code.
