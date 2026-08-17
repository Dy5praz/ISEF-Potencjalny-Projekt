# 21 — Plan budowy, kalendarz, budżet

**Data:** 17 sierpnia 2026
**Wymiar czasu:** wyznaczony przeze mnie, zgodnie z poleceniem użytkownika.

---

## 1. Decyzja o czasie i horyzoncie

**Dwa lata. Rok pierwszy 10 h/tydzień, rok drugi średnio 6 h/tydzień ze zjazdem do 3 h na wiosnę 2029.**

| Okres | h/tydzień | Suma |
|---|---|---|
| IX 2026 – VIII 2027 | 10 | ~480 h |
| IX 2027 – VIII 2028 | 6 | ~290 h |
| IX 2028 – IV 2029 | 4, zjazd do 2 od III 2029 | ~120 h |
| **razem** | | **~890 h** |

**Uzasadnienie horyzontu dwuletniego, nie rocznego:**

`[fakt]` Explory nie ma reguły dwunastu miesięcy, a formularz zgłoszeniowy wprost pyta o zgłoszenie projektu w poprzednich edycjach i o to, jak się rozwinął. Kontynuacja jest proceduralnie przewidziana.

`[wniosek]` Dwa cykle Explory to **dwa niezależne podejścia do najwęższego miejsca całego lejka**, i to jest jedyna rzecz, która realnie podnosi szanse. Drugie podejście jest mocniejsze od pierwszego, bo projekt jest dojrzalszy, a autor zna stawkę i format.

**Uzasadnienie rozkładu godzin:** rok pierwszy jest gęsty, bo w nim mieści się cała budowa i nauka projektowania płytek. Rok drugi jest rzadszy, bo składa się z pomiarów, pisania i konkursów — czynności, które nie wymagają długich bloków przy stole warsztatowym. **Wiosna 2029 jest chroniona pod maturę.**

---

## 2. Kalendarz z twardymi terminami

| Kiedy | Co | Typ |
|---|---|---|
| **IX 2026 – 28 II 2027** | okno zgłoszeń Explory 2027 | twardy, zewnętrzny |
| I 2027 | otwiera się okno 12 miesięcy dla ISEF 2028 (wzorzec „before January") | twardy |
| do 31 III 2027 | wyniki kwalifikacji Explory | zewnętrzny |
| ~20 IV 2027 | OITwEiM — prace i wideo | twardy, wybrany |
| **5 V – 30 VI 2027** | **półfinał Explory, online: plakat + wideo** | **twardy, wąskie gardło** |
| **X 2027** | finał Explory, Gdynia | twardy |
| IX 2027 – 28 II 2028 | okno zgłoszeń Explory 2028 (kontynuacja) | twardy |
| I 2028 | otwiera się okno 12 miesięcy dla ISEF 2029 | twardy |
| ~9–15 V 2028 | **ISEF 2028**, jeżeli reprezentacja | zewnętrzny |
| V–VI 2028 | półfinał Explory 2028 | twardy |
| X 2028 | finał Explory 2028 | twardy |
| **4–6 V 2029** | **matura obowiązkowa — nie koliduje z ISEF** | twardy |
| ~7–21 V 2029 | rozszerzenia — **kolidują częściowo** | twardy |
| ~V 2029 | ISEF 2029, jeżeli reprezentacja | zewnętrzny |

**Pozycja do załatwienia jesienią 2028, nie w kwietniu 2029:** `[luka]` pismo do dyrektora OKE o termin dodatkowy dla rozszerzeń kolidujących z ISEF. Przepis mówi o przyczynach **losowych lub zdrowotnych**, a zaplanowany wyjazd trudno tak nazwać — **nie zakładam, że zostanie przyznany.** Plan zapasowy: zdać rozszerzenia kolidujące w terminie głównym i zrezygnować z tych, które wypadają dokładnie w dniach ISEF, o ile nie są potrzebne do rekrutacji.

---

## 3. Fazy

### Faza 0 — IX 2026, ~40 h. Rozpoznanie, zanim cokolwiek kupisz

1. **Przeczytać cztery pozycje w oryginale**, nie w streszczeniu:
   - przegląd self-sensing AMB (2025) — po to, żeby znać wypisane ograniczenia z pierwszej ręki
   - przegląd strategii sterowania AMB (2025)
   - praca o czujniku prądów wirowych na PCB — po to, żeby nie projektować cewki od zera
   - praca MIT o zestawach maglev do nauczania sterowania — po to, żeby ukraść gotową ścieżkę na poziom zerowy
2. **Sprawdzić jedną rzecz, która jest teraz luką:** czy istnieje praca zestawiająca estymację z tętnienia PWM i estymację ze wstrzykiwania HF **na jednym stanowisku**. Kanały: PubMed E-utilities, arXiv API, Crossref API (indeksuje IEEE), baza konferencji ISMB. **Jeżeli istnieje — projekt się nie zmienia**, zmienia się tylko sposób opisania wkładu w materiałach.
3. Nauka KiCada na czymś, co nie jest tym projektem. Jedna prosta płytka od początku do końca, zamówiona i zlutowana.
4. Zakupy z długim czasem dostawy.

**Kamień milowy:** jedna własna płytka, którą da się wziąć do ręki, i cztery przeczytane prace.

### Faza 1 — X–XI 2026, ~80 h. Poziom zerowy: coś lewituje

Jedna oś, pionowo. Elektromagnes, stalowa kula albo krążek, dowolny czujnik położenia (na tym etapie może być Halla albo optyczny — tani i bez ambicji), regulator PID na mikrokontrolerze.

**To jest faza odcięcia ryzyka i musi się skończyć sukcesem, zanim ruszy cokolwiek droższego.**

**Kamień milowy:** przedmiot wisi w powietrzu, a Ty masz z tego wykres odpowiedzi skokowej — nie film, wykres.

### Faza 2 — XI 2026 – I 2027, ~100 h. Własny czujnik na płytce

Projekt, zamówienie i pomiar czujnika prądów wirowych na PCB. Kalibracja wobec stolika mikrometrycznego.

Charakteryzacja czujnika, i to jest pierwszy poważny wynik pomiarowy projektu:

| Wielkość | Jak mierzona |
|---|---|
| czułość i liniowość | stolik mikrometryczny, przejazd w obu kierunkach, histereza |
| rozdzielczość i szum | zapis przy nieruchomym celu, odchylenie standardowe, gęstość widmowa |
| pasmo | pobudzenie mechaniczne o znanej częstotliwości |
| dryf temperaturowy | nagrzewanie stojana, zapis wskazania przy nieruchomym celu |
| wrażliwość na materiał celu | dwa–trzy różne materiały |

**Kamień milowy:** karta katalogowa własnego czujnika, napisana tak jak pisze się karty katalogowe. To jest dokument, który na stoisku robi różnicę.

### Faza 3 — II–IV 2027, ~100 h. Stanowisko dwuosiowe

Stojan wielobiegunowy, wirnik, stopień mocy z pomiarem prądu, sterownik, dwie osie w zamkniętej pętli, łożyska zapasowe, osłona.

**Zgłoszenie do Explory wychodzi w tej fazie, najpóźniej 28 II 2027.** `[fakt]` Regulamin nie wymaga ukończonego projektu przy zgłoszeniu, a kryteria etapu I to znajomość tematu, wartość dodana i zastosowanie praktyczne — spełnialne stanem z fazy 2.

**OITwEiM: prace do ~20 IV 2027.** Etap centralny wymaga działającego prototypu, czyli tego samego przedmiotu. Ta sama praca, inny konkurs, przywileje rekrutacyjne.

**Kamień milowy:** wirnik wisi w dwóch osiach, sterowany własną elektroniką, z własnymi czujnikami.

### Faza 4 — V–VI 2027, ~60 h. Półfinał Explory

`[fakt]` Półfinał jest w całości online, a wymogiem jest **plakat/infografika oraz krótkie wideo**. Efekt „to naprawdę wisi w powietrzu" nie działa przez stoisko, bo stoiska nie ma — **wideo jest jedynym nośnikiem efektu demonstracyjnego w najwęższym miejscu całego lejka**.

**Wideo traktować jak osobny produkt z własnym terminem.** Wirnik lewitujący i obracający się w pierwszych dziesięciu sekundach, wyjaśnienie dopiero potem. Jury ma ponad sto projektów do obejrzenia.

Równolegle: **start formalnej kampanii pomiarowej pod ISEF 2028** (okno otwarte od I 2027, blok ciągły 12 miesięcy kończący się przed V 2028).

### Faza 5 — VII–IX 2027, ~100 h. Kampania pomiarowa roku 1

Pełna charakteryzacja wg `22_PLAN_POMIAROWY.md`. Dołożenie obrotu.

**Kamień milowy:** komplet charakterystyk z niepewnościami. To jest rzecz, której nie ma żaden finalista Explory.

### Faza 6 — X 2027. Finał Explory

Stoisko z działającym stanowiskiem. Przećwiczona odpowiedź na pytanie „czym to się różni od tego, co robi Skarbek/SKF/Danfoss".

### Rok 2 — IX 2027 – V 2029

| Okres | h | Zawartość |
|---|---|---|
| IX–XII 2027 | ~70 | estymator nr 1: położenie z nachylenia tętnienia PWM. Tor pomiaru prądu o odpowiednim paśmie — to jest zadanie analogowe, nie programistyczne |
| I–II 2028 | ~50 | **zgłoszenie Explory 2028 do 28 II** jako kontynuacja. Estymator nr 2: wstrzykiwanie HF i demodulacja |
| III–IV 2028 | ~50 | OITwEiM po raz drugi. Przygotowanie pod ISEF 2028 |
| V 2028 | — | **ISEF 2028**, jeżeli reprezentacja. Form 7 nie jest potrzebny — to pierwszy rok |
| VI–IX 2028 | ~90 | **kampania porównawcza**: te same pomiary co w roku 1, dla obu estymatorów. Eksperymenty rozdzielające mechanizm |
| X 2028 | — | finał Explory 2028 |
| XI 2028 – II 2029 | ~60 | opracowanie, **Form 7** z wykazaniem, co jest nowe, przygotowanie pod ISEF 2029 |
| III–V 2029 | ~30 | matura ma pierwszeństwo |

---

## 4. Budżet

`[domysł]` Ceny orientacyjne, sierpień 2026, złote. Weryfikować przy zakupie.

### 4.1 Sprzęt projektu

| Pozycja | Faza | Koszt |
|---|---|---|
| rdzenie elektromagnesów, blachy, drut nawojowy | 1, 3 | 600 |
| wirnik: wał + pakiet blach + wyważenie | 3 | 600 |
| stopień mocy: MOSFETy, sterowniki bramek, pomiar prądu | 1, 3 | 500 |
| mikrokontrolery i płytki rozwojowe | 1, 3 | 400 |
| **produkcja płytek, ~6 iteracji** | 2, 3, rok 2 | **1 200** |
| układy scalone do pomiaru indukcyjności, elementy bierne | 2 | 300 |
| stolik mikrometryczny do kalibracji | 2 | 400 |
| silnik BLDC ze sterownikiem, sprzęgło | 5 | 300 |
| łożyska zapasowe, osłona poliwęglanowa, płyta bazowa | 3, 5 | 500 |
| części drukowane, żywica, filament | całość | 400 |
| obróbka mechaniczna zlecona | 3 | 600 |
| **razem sprzęt** | | **5 800** |

### 4.2 Przyrządy pomiarowe

| Pozycja | Koszt | Uwaga |
|---|---|---|
| zasilacz laboratoryjny regulowany | 400 | konieczny od fazy 1 |
| oscyloskop 2-kanałowy, używany albo USB | 1 800 | **największa pojedyncza pozycja** |
| multimetr stołowy | 400 | |
| generator funkcyjny | 0 | **niepotrzebny — patrz niżej** |
| **razem przyrządy** | **2 600** | |

**Rzecz, która oszczędza pieniądze i jednocześnie jest lepsza metodycznie:** charakterystykę częstotliwościową zamkniętej pętli mierzy się **wstrzykując przemiatany sygnał sinusoidalny do wnętrza pętli z samego mikrokontrolera** i licząc transmitancję z zapisanych danych. Nie trzeba analizatora ani generatora, a wynik jest dokładnie tym, czym się chwalą układy przemysłowe. **Ta metoda ma być w projekcie od początku, nie jako oszczędność, tylko jako metoda.**

### 4.3 Podsumowanie i rezerwa

| | Kwota |
|---|---|
| sprzęt projektu | 5 800 |
| przyrządy | 2 600 |
| rok drugi: rewizje płytek, szybszy tor prądowy | 1 500 |
| **suma** | **9 900** |
| **rezerwa do limitu 15 000** | **5 100** |

**Rezerwy nie planuję wydać.** Jest na to, że dwie płytki wyjdą źle, że rdzeń trzeba będzie przewinąć i że wirnik trzeba będzie wyważyć drugi raz. `[wniosek]` Projekt sprzętowy bez rezerwy 30–50% kończy się porzuceniem w połowie.

---

## 5. Zasoby zewnętrzne — plan ich zużycia

`[fakt, z sekcji 1 handbooka]` Brat kończy studia inżynierskie i pracuje w firmie produkującej precyzyjną elektronikę.

**To jest zasób jednorazowy i ma być zużyty świadomie, nie przypadkiem.** Trzy rzeczy, o które warto prosić, w kolejności wartości:

1. **Niezależna weryfikacja własnego czujnika** — jeden pomiar przemieszczenia przyrządem klasy laboratoryjnej, wobec którego skalibrujesz swoją płytkę. **To jest najcenniejsza rzecz w całej liście**, bo zamienia „mój czujnik pokazuje" w „mój czujnik pokazuje, sprawdzone wobec przyrządu wzorcowego" — i to jest zdanie, które w rozmowie z jurorem ISEF waży więcej niż cała reszta stoiska.
2. **Przegląd projektu płytki przed zamówieniem**, dwa razy: czujnik i stopień mocy. Kosztuje go godzinę, oszczędza Ci iterację i trzy tygodnie.
3. **Wyważenie wirnika** albo dostęp do kogoś, kto to robi.

**O co nie prosić:** żeby coś za Ciebie zaprojektował albo zbudował. `[fakt]` Standardy etyczne Explory (Załącznik nr 1, Kodeks Etyki PAN) oraz ISEF wymagają, żeby praca była własna, a udział osób trzecich był deklarowany. Konsultacja jest dozwolona i normalna; wykonanie nie.

`[luka]` Członek rodziny pracujący w R&D nad generatorami plazmy RF i DC — **dla tego projektu nieistotny**. Zapisuję, żeby nie szukać na siłę zastosowania.

---

## 6. Czego uczysz się po drodze, niezależnie od wyniku konkursowego

Zapisane, bo to jest realna wartość ścieżki nawet przy porażce na każdym sicie:

- projektowanie płytek dwu- i czterowarstwowych, w tym tor analogowy małosygnałowy i stopień mocy
- projektowanie i pomiar czujnika, kalibracja wobec wzorca, budżet niepewności
- teoria sterowania w praktyce: identyfikacja obiektu, projekt regulatora, zapasy stabilności, pomiar charakterystyki częstotliwościowej
- elektronika mocy: mostki, sterowanie bramek, pomiar prądu, PWM
- obróbka i montaż mechaniczny z tolerancjami rzędu setnych milimetra

`[wniosek]` To jest zestaw, który sam w sobie jest mocniejszym materiałem do aplikacji na uczelnię techniczną niż wynik konkursowy średniego szczebla — bo daje się opowiedzieć w eseju i obronić w rozmowie.
