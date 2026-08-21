# Concept of Operations (ConOps) — Orteza kolana ze sterowanym sprzęgłem i biernym magazynowaniem energii

*Projekt konkursowy. Explory — primary (zgłoszenie do 28 lutego 2027, finał październik 2027), El-Robo-Mech — równolegle (ten sam projekt, dopuszczalne), ISEF — cel docelowy (maj 2028).*

*Wersja 0.1 — 8 sierpnia 2026. Dokument założycielski. Powstał po odrzuceniu projektu drona poszukiwawczo-ratowniczego; przyczyną odrzucenia była niemożność obrony deklarowanej zdolności (akustyka docierała po termowizji, czyli potwierdzała zamiast wykrywać).*

---

## 1. Cel i zakres dokumentu

Dokument opisuje koncepcję działania ortezy kolana, która magazynuje energię mechaniczną w sprężynie podczas zginania stawu pod obciążeniem i oddaje ją podczas prostowania, przy czym **moment zaczepienia sprężyny jest sterowany elektronicznie**, a nie ustalony na stałe.

Zakres obejmuje: zasadę działania, dwie tezy projektu, budżet mechaniczny, plan walidacji, ograniczenia i zgodność formalną. Nie obejmuje: szczegółów konstrukcyjnych mechanizmu (do rozstrzygnięcia po testach stanowiskowych), projektu PCB, doboru materiałów.

**Konwencja oznaczania pewności** (przeniesiona z ConOps drona, sprawdziła się):
- **[D]** — dane z zweryfikowanego źródła pierwotnego lub karty katalogowej
- **[W]** — wniosek z modelu fizycznego lub analogii
- **[L]** — szacunek własny wypełniający lukę, do zastąpienia pomiarem

Żadna liczba bez oznaczenia nie trafia do materiałów zgłoszeniowych.

---

## 2. Problem

**[D]** Zwyrodnienie stawu kolanowego dotyka ogromnej i rosnącej populacji. Czynności, które wypadają jako pierwsze, to wstawanie z krzesła oraz wchodzenie i schodzenie po schodach — nie chodzenie po płaskim.

**[D]** Kolano dostarcza największy moment ze wszystkich stawów kończyny dolnej podczas podnoszenia środka masy ciała przy wstawaniu (*Extending the Benefits of Parallel Elasticity across Multiple Actuation Tasks*, arXiv:2409.08889).

**[D]** Wstanie z krzesła udaje się, gdy suma szczytowych momentów biodra i kolana przekracza **1,53 Nm/kg**. Wartość 1,5 Nm/kg lub niższa wskazuje na potrzebę rehabilitacji (*BioMedical Engineering OnLine* 6:26).

To jest twardy próg, a nie miękka trudność. Osoba poniżej progu po prostu nie wstaje.

### Użytkownik docelowy jest **powyżej** progu — i to zmienia metrykę

**Korekta wprowadzona w sierpniu 2026.** Wcześniejsza wersja tego dokumentu przyjmowała przekroczenie progu 1,53 Nm/kg jako główny wskaźnik skuteczności. To jest miara dla osoby, która **nie może** wstać. Użytkownik pierwotny tego projektu wstaje bez trudu — **płaci za to bólem**.

**Mechanizm bólu jest tożsamy z mechanizmem momentu, nie jest osobnym zjawiskiem.** Siła ściskająca staw pochodzi w przeważającej części nie z ciężaru ciała, lecz z mięśnia czworogłowego, który ciągnąc rzepkę dociska ją do kości udowej. Im większy moment musi wytworzyć mięsień, tym większy docisk. Przy zniszczonej chrząstce ten docisk jest źródłem bólu. Orteza przejmująca część momentu zmniejsza wymaganą siłę mięśnia, a przez to docisk.

**Łańcuch dowodowy:** mniejsza aktywność mięśnia czworogłowego → mniejszy docisk w stawie → mniejszy bodziec bólowy. **Ogniwo pierwsze mierzymy sami; ogniwa drugie i trzecie bierzemy z literatury.**

Tak też pozycjonuje się konkurencja: **[D]** Spring Loaded raportuje odciążenie stawu ponad 40%, opisywane w badaniach niezależnych jako odpowiednik utraty kilkunastu kilogramów masy ciała; **[D]** Roam podaje dla Ascend średnią redukcję bólu rzędu 46%. Żadna z firm nie deklaruje „umożliwiamy wstawanie" — obie mówią „boli mniej".

**Wniosek:** grupa docelowa to osoby sprawne ruchowo, u których czynność jest wykonalna, ale bolesna. Osoby poniżej progu są ciężej dotknięte i urządzenie bierne obsługuje je gorzej (patrz sekcja 9).

**Istniejące opcje i ich koszt:**
- **[D]** Ascend (Roam Robotics): ok. 7000 USD, aktywne wspomaganie pneumatyczne, wymaga plecaka z pompą i akumulatorem (SmartPack).
- **[D]** Levitation / Spring Loaded OA: bierna sprężyna cieczowa, bez zasilania, regulacja ręcznym pokrętłem. Cena porównywalna, w Polsce brak refundacji.
- Zwykła orteza stabilizująca: nie dodaje siły.

**Luka, w którą wchodzi projekt:** pomiędzy urządzeniem biernym z ręczną regulacją a urządzeniem aktywnym z plecakiem nie ma nic. I żadne z nich nie jest w zasięgu cenowym pojedynczego użytkownika w Polsce.

---

## 3. Zasada działania

Sprężyna umieszczona równolegle do stawu kolanowego. Podczas zginania pod obciążeniem (siadanie, schodzenie ze schodu, przyjęcie ciężaru ciała) energia trafia do sprężyny. Podczas prostowania wraca.

**Rdzeniem urządzenia nie jest sprężyna, tylko sprzęgło.** Sprzęgło decyduje, w którym momencie zakresu ruchu sprężyna zostaje zaczepiona i kiedy zostaje zwolniona.

**Konsekwencja energetyczna, kluczowa dla całej konstrukcji:** ponieważ sprężyna magazynuje energię samego użytkownika, elektronika nie zasila ruchu — zasila wyłącznie decyzję. **[D]** Collins i wsp. (*Nature* 2015) piszą wprost, że urządzenie zasilane mogłoby przybliżyć się do niezasilanego, zużywając pomijalne ilości energii wyłącznie do sterowania momentem załączania elementów mechanicznych, takich jak sprzęgła.

**[W]** Pobór rzędu miliwatów, nie watów. **Brak plecaka, brak saszetki — całość elektroniki mieści się na samej ortezie.** To jest bezpośrednia odpowiedź na główną wadę użytkową rozwiązań aktywnych.

**Warunek, od którego to zależy:** mechanizm sprzęgła musi trzymać obciążenie **mechanicznie**, a element elektryczny może je jedynie zwalniać. Sprzęgło wymagające prądu do utrzymania siły unieważnia całą architekturę i cofa projekt do plecaka. To jest jedyny punkt, w którym projekt może umrzeć konstrukcyjnie — dlatego jest testowany jako pierwszy, przed jakimkolwiek innym wydatkiem (sekcja 10).

---

## 4. Dwie tezy projektu

Obie wynikają z ograniczeń **przyznanych przez autorów istniejących prac**, nie z braku znalezienia pracy. To rozróżnienie jest istotne: luka, której nie znalazłem, jest luką w moim przeszukaniu; luka, którą autor sam wpisał do swojej pracy, jest luką w dziedzinie.

### Teza 1 — dobór momentu zaczepienia zamiast doboru sztywności

**Przyznane ograniczenie:** **[D]** KAIST (X-tights, *Frontiers in Bioengineering* 2020) dobrał sztywność gum tak, by magazynowały wystarczająco energii, **ale nie przezwyciężały całkowicie siły grawitacji potrzebnej do siadania**. Czyli celowe osłabienie, bo sprężyna zawsze załączona przeszkadza. **[D]** Praca arXiv:2409.08889 istnieje wyłącznie po to, by dobrać sztywność i napięcie wstępne zmniejszające moment przy wstawaniu **bez pogorszenia** chodu i schodów. **[D]** Spring Loaded przerzuca ten kompromis na użytkownika przez ręczne pokrętło.

**Teza:** przy sprzęgle nie dobiera się sztywności, tylko **kąt zaczepienia w zakresie ruchu**. Ta sama sprężyna złapana przy 90° zgięcia i przy 20° daje inny profil wspomagania. Kompromis, którego trzy zespoły nie mogły usunąć, znika — nie przez lepszy dobór, tylko przez usunięcie założenia, że sprężyna jest zawsze zaczepiona w tym samym miejscu.

### Teza 2 — pomiar sprawności przeniesienia momentu

**Przyznane ograniczenie:** **[D]** Roam Robotics ma **trzy osobne patenty** wyłącznie na wykrywanie złego dopasowania siłownika (US 10 780 012, US 10 966 895, US 11 266 561). Rozwiązanie jest programowe: urządzenie wykrywa, że dopasowanie jest złe. Nie mierzy, ile momentu ucieka. **[D]** KnExo atakuje ten sam problem geometrycznie (mechanizm krzywkowy, redukcja niedopasowania osi o 51%). **[D]** Spring Loaded podkreśla system pasków zapobiegający zsuwaniu się jako osobną cechę produktu.

Trzy niezależne zespoły, ten sam problem, trzy różne obejścia. **Żaden nie podaje, jaki procent zadanego momentu faktycznie dociera do stawu.**

**Teza:** urządzenie mierzy w sposób ciągły **sprawność przeniesienia momentu** — stosunek momentu dostarczonego do kończyny do momentu wytworzonego przez sprężynę.

**Dlaczego to jest najmocniejszy element projektu:** wynik jest niezależny od tej konkretnej konstrukcji. Jeśli okaże się, że przez tkankę miękką przechodzi np. 60% zadanego momentu, jest to liczba obowiązująca każdą ortezę tego typu. To jest różnica między „zbudowałem" a „ustaliłem", i tylko drugie liczy się na ISEF.

**Konsekwencja konstrukcyjna:** pomiar wchodzi w pętlę sterowania — sprzęgło może korygować zaczep, gdy wykryje ucieczkę momentu.

**Konsekwencja prezentacyjna:** na stoisku dwa wykresy obok siebie — moment zadany i moment dostarczony — rysowane na żywo, gdy juror zakłada urządzenie.

---

## 5. Sformułowanie nowatorstwa (do użycia dosłownie)

*Wielotrybowe, sterowane sprzęgło w ortezie kolana występuje w literaturze jako projekt koncepcyjny lub jako urządzenie badawcze o kosztach laboratoryjnych. Produkty dostępne dla pacjenta są albo bierne z ręczną regulacją, albo aktywne z zewnętrznym źródłem zasilania. Nie znaleziono zbudowanego i zmierzonego urządzenia wielotrybowego w klasie kosztowej dostępnej dla pojedynczego użytkownika, ani opublikowanej wartości sprawności przeniesienia momentu przez interfejs orteza–kończyna. Wkładem jest integracja, wykonanie, pomiar i benchmark — nie zasada działania.*

**Zastrzeżenie metodologiczne do zamknięcia przed zgłoszeniem:** deklaracja musi brzmieć „nie znaleziono w bazach X, Y, Z, stan na [data]", nigdy „nie istnieje". Bazy do przeszukania przed lutym 2027: Google Scholar, IEEE Xplore, Scopus, Espacenet, Google Patents, cytowania w przód dla Collins 2015, Irby 1999 i przeglądu MDPI *Machines* 10(10):865.

---

## 6. Budżet mechaniczny

### 6.1 Moment wymagany

**[D]** Szczytowy moment na kolanie przy wstawaniu: **0,51–1,97 Nm/kg** (zależnie od strategii ruchu).
**[D]** Moment prostowników kolana przy schodzeniu ze schodów, wiek 50–75: **0,70 Nm/kg** (masa prawidłowa), **0,98 Nm/kg** (nadwaga).

**[L]** Dla użytkownika 85 kg, przy założeniu wartości środkowej 1,0 Nm/kg: około **85 Nm** szczytowo przy wstawaniu.

**[L]** Cel projektowy: dostarczyć **30–50%** tej wartości, czyli **25–43 Nm**. Uzasadnienie: KnExo osiąga 25–31% masy ciała jako wspomaganie i jest to wartość odczuwalna; przekroczenie 50% grozi tym, że urządzenie przejmuje ruch zamiast go wspomagać, co jest niepożądane u osoby z zachowaną kontrolą.

**Do zastąpienia pomiarem:** rzeczywista masa użytkownika i rzeczywista wartość progowa dla niego.

### 6.2 Energia

**[L]** Do policzenia po ustaleniu skoku sprężyny i ramienia dźwigni. Punkt odniesienia: **[D]** Collins i wsp. raportują dla sprzęgniętej sprężyny w stawie skokowym pracę rzędu 2,6 J na krok.

### 6.3 Masa

**[D]** Ascend: ok. 1,1 kg całości, z czego ok. 0,23 kg to dołożona robotyka; dostarcza ok. 50% mocy zdrowego kolana.
**[D]** Swift (Roam): problemem jest masa przy stawie — 4,5 kg na tułowiu i 0,45 kg na stopie mają porównywalny wpływ metaboliczny.

**[L]** Cel: poniżej 1,5 kg. **[W]** Pobicie 1,1 kg przy zapleczu domowym jest mało prawdopodobne — masa nie powinna być deklarowana jako oś przewagi.

### 6.4 Zasilanie

**[D]** Sprzęgła elektroadhezyjne: 0,6 mW przy chodzeniu (masa 11 g, 100 N); wersja rozwinięta 3,2 mW przy 190 N i 15 g, ponad 3 mln cykli.
**[W]** Sprzęgło mechaniczne z zapadką: pobór wyłącznie w chwili przełączania, zero w stanie zablokowanym.
**[L]** Budżet całkowity z czujnikami i mikrokontrolerem: rząd 10–50 mW średnio. Akumulator wielkości pudełka zapałek starczy na dziesiątki godzin.

**Do zastąpienia pomiarem** po wyborze sprzęgła i czujników.

---

## 7. Podsystemy

### 7.1 Sprzęgło — warianty i kryteria

| Wariant | Moment trzymający | Pobór w stanie trzymania | Wykonalność domowa | Uwagi |
|---|---|---|---|---|
| **Zapadka mechaniczna** | Bardzo wysoki | Zero | **Wysoka** | Regulacja skokowa (co ząb). Problem: zwolnienie pod obciążeniem |
| **Sprzęgło zwojowe** | Bardzo wysoki przy małej masie | Zero | Średnia | **[D]** Stosowane w ortezach kolana od 1999 (Irby i wsp., *IEEE Trans. Rehabil. Eng.* 7(2)). Wymaga precyzyjnej sprężyny |
| **Przekładnia planetarna** | Wysoki | Niski | Niska | **[D]** Przegląd MDPI wskazuje ją jako konieczną przy wymogu dużego momentu i małej masy |
| **Elektroadhezyjne** | 100–190 N | 0,6–3,2 mW | Bardzo niska | Wysokie napięcie, podatność na przebicie dielektryka, wrażliwość na wilgoć i pot |
| **Ciecz magnetoreologiczna** | Średni | Stały pobór | Niska | **[D]** Zastosowane w kolanowym egzoszkielecie quasi-biernym (2026) |

**Decyzja wstępna:** start od **zapadki**, z sprzęgłem zwojowym jako ścieżką rozwojową. Uzasadnienie: jedyny wariant wykonalny drukiem 3D i lutownicą, zerowy pobór w stanie trzymania, największy zapas momentu.

**Otwarte pytanie krytyczne:** ile siły wymaga zwolnienie obciążonej zapadki. Odpowiedź decyduje o istnieniu projektu. Test — sekcja 10.

### 7.2 Rozpoznawanie zamiaru

**Przyznane ograniczenie:** **[D]** Roam ma dwa patenty na rozpoznawanie zamiaru ze **zmienną czułością** (US 11 351 083, US 11 872 181), przełączaną sygnałem od użytkownika. To jest przyznanie, że automatyczne rozpoznanie jest zawodne.

**[D]** Cała literatura o sprzęgłach kolanowych działa na fazie cyklu chodu (przyjęcie obciążenia / wymach). Wstawanie z fotela nie ma cyklu.

**Przyjęte rozwiązanie: czujnik obciążenia w podeszwie, nie w ortezie.** Zanim kolano zacznie się prostować przy wstawaniu, tułów pochyla się do przodu i ciężar przenosi się na stopy. To jest mierzalne **zanim** kolano się poruszy — a sprzęgło musi zadziałać przed ruchem, nie w jego trakcie. Rozkład obciążenia stopy przy schodach różni się od rozkładu przy wstawaniu, więc ten sam czujnik rozróżnia tryby.

**[L]** Wymagany czas reakcji: poniżej 100 ms od wykrycia do zaczepienia. Do zweryfikowania pomiarem.

### 7.3 Pomiar sprawności przeniesienia (teza 2)

**Zasada:** równolegle mierzone są dwie wielkości — moment wytworzony przez sprężynę (z jej ugięcia i znanej charakterystyki) oraz rzeczywisty nacisk lub przemieszczenie na interfejsie mankiet–kończyna.

**[L]** Metoda pomiaru do rozstrzygnięcia: czujniki nacisku w mankietach, tensometry na ramionach ortezy albo pomiar przemieszczenia mankietu względem skóry. Każda ma inne wady. **Do przetestowania w sierpniu–wrześniu, równolegle ze sprzęgłem** — bo to jest drugi filar projektu, nie dodatek.

**Jeśli okaże się, że tego nie da się wiarygodnie zmierzyć prostymi środkami**, teza 2 upada i trzeba wrócić do rozmowy o tym, czym ją zastąpić. Lepiej we wrześniu niż w kwietniu.

---

## 8. Tryby pracy i zakres na edycję 2027

**Decyzja wiążąca (sierpień 2026): projekt realizowany jednoosobowo.** Konsekwencją jest zawężenie zakresu konkursowego do **jednego trybu**. Uzasadnienie w sekcji 11.

| Tryb | Wyzwalacz | Zachowanie sprzęgła | Zakres |
|---|---|---|---|
| **Siadanie** | Wzrost obciążenia pięt + zginanie kolana pod obciążeniem | Zaczep wczesny, kontrolowane pochłanianie energii | **W zakresie — edycja 2027** |
| **Wstawanie** | Przeniesienie ciężaru na przód stopy przy zgiętym kolanie | Utrzymanie zaczepu, oddanie energii przy prostowaniu | **W zakresie — edycja 2027** |
| **Bezczynność / siedzenie** | Brak obciążenia | Rozłączenie, uśpienie elektroniki | **W zakresie — edycja 2027** |
| **Zwolnienie awaryjne** | Utrata zasilania, przycisk, anomalia | Rozłączenie mechaniczne, bezwarunkowe | **W zakresie — przed pierwszym założeniem na człowieka** |
| **Schody w dół** | Obciążenie przodostopia przy zginaniu | Zaczep, hamowanie | Warunkowo — tylko jeśli zostanie czas po działającej wersji podstawowej |
| **Schody w górę** | Obciążenie przodostopia przy prostowaniu | Oddanie | Warunkowo — jw. |
| **Chód po płaskim** | Cykliczny wzorzec obciążenia | **Pełne rozłączenie** | **Poza horyzontem konkursowym** |

**Dlaczego chód wypada, a nie jest tylko odłożony.** Dwa niezależne powody. Po pierwsze techniczny: chód wymaga czystego rozłączenia w fazie wymachu i to jest znany punkt zapalny całej dziedziny — **[D]** praca z 2026 o sprzęgle magnetoreologicznym przypisuje przewagę nad wynikiem Collinsa właśnie pełnemu rozłączeniu w wymachu; **[D]** ogólna diagnoza: bierne egzoszkielety z magazynowaniem energii poprawiają ekonomię chodu, ale zwykle psują kinematykę wymachu. Po drugie korzyściowy: zakres zgięcia kolana w chodzie po płaskim jest mały, więc magazynowanie energii jest z natury ograniczone.

Czyli chód to najwyższa trudność przy najmniejszej korzyści. Zostaje w dokumencie jako kierunek rozwoju, nie jako obietnica.

**Konsekwencja dla narracji przy stoisku:** „robi jedną rzecz i robi ją porządnie" jest mocniejsze niż trzy tryby, z których dwa ledwo działają. Wielotryb był tezą wymagającą zespołu.

---

## 9. Świadomie poza zakresem

- **Wspomaganie osoby bez zachowanej siły mięśniowej.** Bierna sprężyna oddaje tylko energię, którą użytkownik w nią włożył. **[D]** Roam deklaruje to samo ograniczenie dla Ascend — celują w osoby z zachowaną kontrolą ruchu.
- **Staw usztywniony chirurgicznie lub o silnie ograniczonym zakresie zgięcia.** Brak zgięcia pod obciążeniem = brak magazynowania energii. Urządzenie jest w tym przypadku bezużyteczne. *(Ograniczenie zidentyfikowane na realnym przypadku w rodzinie.)*
- **Deklaracja poprawy chodu po płaskim jako głównej zdolności.** Kolano zgina się tam o kilkanaście stopni pod obciążeniem — droga do zmagazynowania energii jest mała. **[D]** Collins osiągnął 7% redukcji kosztu metabolicznego na stawie **skokowym**, u osób zdrowych. Nie przenosić tej liczby na kolano.
- **Deklaracje kliniczne.** Żadnego „redukuje ból o X%", żadnych ekstrapolacji na liczbę osób, które uniknęłyby operacji. Projekt raportuje mechanikę, nie efekt zdrowotny.
- **Zastosowania militarne.** Zakaz regulaminowy Explory i El-Robo-Mech. Nie odwoływać się do produktu Forge firmy Roam Robotics w żadnych materiałach — jest to sprzęt dla armii USA. Odwołanie właściwe: **Ascend**, wersja medyczna tej samej technologii.
- **Masa jako oś przewagi.** Ascend waży ok. 1,1 kg. Nie deklarować pobicia tej wartości.

---

## 10. Plan walidacji i metryki

### Etap 0 — sierpień/wrzesień 2026, koszt kilkuset złotych
**Test sprzęgła na stanowisku.** Zapadka trzymająca zadany moment, zwalniana małym elementem. Mierzone: moment utrzymania, siła wymagana do zwolnienia pod obciążeniem, zależność siły zwolnienia od geometrii zęba.
**Kryterium przejścia:** siła zwolnienia mieszcząca się w zasięgu mikroserwa lub małego elektromagnesu.
**Jeśli nie przejdzie:** zmiana wariantu sprzęgła albo zmiana projektu.

Równolegle: wstępny test metody pomiaru sprawności przeniesienia.

### Etap 1 — jesień 2026
Pierwsza wersja mechaniki. Charakterystyka sprężyny na stanowisku, powtarzalność zaczepiania, czas przełączenia.

### Etap 2 — zima 2026/27, przed zgłoszeniem
Urządzenie zakładane na nogę. **Platforma siłowa własnej konstrukcji** (cztery tensometry + HX711) pod krzesłem: pomiar siły potrzebnej do wstania z ortezą i bez, na tej samej osobie, tego samego dnia.
**Zgłoszenie do Explory do 28 lutego 2027 — projekt nie musi być ukończony.**

### Etap 3 — wiosna–lato 2027
Wielokrotne powtórzenia, więcej niż jeden użytkownik, pomiar sprawności przeniesienia, dane z całodziennego noszenia.

### Etap 4 — jesień 2027
Finał Explory, październik 2027. Stanowisko z platformą siłową jako eksponatem.

### Metryki
- Moment dostarczony do kończyny [Nm] i moment zadany przez sprężynę [Nm]
- **Sprawność przeniesienia momentu [%]** — główna metryka projektu
- **Redukcja aktywności mięśnia czworogłowego [%]** przy tej samej czynności, z ortezą i bez — **główny wskaźnik skuteczności**. Pomiar elektromiograficzny powierzchniowy (elektrody na skórze, nieinwazyjny). Porównanie wyłącznie **wewnątrz jednej sesji**: te same elektrody, ta sama osoba, ta sama czynność, bez zdejmowania elektrod między próbami. **[L]** Moduł pomiarowy rzędu 150–250 zł
- Redukcja siły potrzebnej do wstania [%] wobec tej samej osoby bez ortezy (platforma tensometryczna pod krzesłem)
- Czas reakcji sprzęgła [ms] od wykrycia zamiaru do zaczepienia
- Liczba fałszywych zaczepień na godzinę noszenia
- Pobór energii [mW] średni i w chwili przełączania
- Masa całkowita [g]
- Koszt materiałowy [PLN] wobec cen produktów komercyjnych

**Ablacja obowiązkowa:** to samo urządzenie, ta sama osoba, ta sama czynność, sprzęgło aktywne i wyłączone. Bez tego każda liczba wygląda na dobraną.

**Wykluczone z raportowania:** jakiekolwiek wskaźniki bólu, poprawy jakości życia, uniknięcia operacji.

---

## 10A. Walidacja zewnętrzna — największa luka projektu

*Sekcja dopisana po przeglądzie 29 projektów finałowych i rezerwowych edycji 2026 (przegląd własny, sierpień 2026).*

**Ustalenie, które to wymusiło.** Najmocniejszy projekt inżynierski tamtej edycji (MAPPER, autonomiczny pojazd F1Tenth, zespół 3-osobowy) nie miał na plakacie **ani jednego pomiaru z niepewnością ani porównania z odniesieniem**. Zamiast tego miał **sześć podiów w sześciu startach zawodów** i otwarte repozytorium.

**[W]** Wniosek: nie musieli udowadniać, że urządzenie działa, bo udowodnił to ktoś inny, niezależnie, sześć razy. To jest waluta silniejsza od własnego pomiaru, bo nie da się jej podważyć zarzutem o stronniczość.

**Dla ortezy nie istnieje odpowiednik obwodu zawodów.** To jest realna słabość strukturalna tego projektu i wymaga świadomej kompensacji. Substytuty, w kolejności siły:

1. **Pisemna ocena fizjoterapeuty lub ortopedy** — po zbadaniu urządzenia, na papierze, z podpisem. Najbliższy odpowiednik walidacji zewnętrznej. **Status: obowiązkowy, nie opcjonalny.** Kontakt nawiązać we wrześniu 2026, nie wiosną 2027 — patrz niżej.
2. **Tabela porównawcza z produktami komercyjnymi** (sekcja 10, tabela). **[W]** W przeglądzie 29 projektów najwyżej 1–2 porównywały się z istniejącymi rozwiązaniami. Darmowy wyróżnik.
3. **Otwarte repozytorium** — modele, kod, dokumentacja, dziennik. Koszt zero, sygnalizuje weryfikowalność.
4. **El-Robo-Mech przed finałem Explory**, jeśli terminy pozwolą — wynik z niezależnego konkursu jest najbliższy „podium". **[L]** Do sprawdzenia: termin edycji El-Robo-Mech względem października 2027.

**Fizjoterapeuta jako źródło danych wejściowych, nie recenzent.** Pierwsza rozmowa ma się odbyć **przed** projektowaniem mechaniki, bo zmieni konstrukcję: przy jakim kącie zgięcia pacjenci faktycznie mają problem, dlaczego zdejmują ortezy, czego nigdy nie robić przy uszkodzonym stawie. Recenzja gotowego urządzenia to osobne, późniejsze zadanie.

---

## 10B. Strategia prezentacji — plakat nie jest miejscem na wykresy

*Sekcja dopisana po tym samym przeglądzie. Koryguje wcześniejsze założenie robocze.*

**Błąd skorygowany:** wcześniejsza wersja tego dokumentu zakładała, że wyniki pomiarów są główną walutą Explory i mają trafić na plakat. Przegląd tego nie potwierdza.

**Rozkład zaobserwowany w edycji 2026** (29 projektów, kategoryzacja własna): 3 projekty bez jakichkolwiek liczb i badań, 2 ze wzmianką o pomiarach, 4 z liczbami opisowymi, 4 z dokładnymi pomiarami, 7 pośrednich, 4 wzorcowe opisy badawcze, **2 wzorcowe opisy inżynierskie (realnie 1)**.

**[W]** Wzorcowa dokumentacja koncentruje się w biologii, chemii i medycynie — bo tam badanie **jest** projektem. Dla projektu inżynierskiego odpowiednikiem sekcji metodologicznej okazuje się **dziennik postępu budowy**, nie tabela wyników. Plakat MAPPER-a w sekcji „opis badań" zawiera chronologię kwartałów: podwozie i druk, potem napęd i LiDAR i pierwsze jazdy, potem symulator.

**[fakt]** Zgodne z tym, co wygrywa: 7 na 10 Nagród Głównych w edycjach 2016–2025 poszło do projektów inżynieryjno-konstrukcyjnych, mimo że dokumentacja biologiczna jest lepsza. Przy stoisku działające urządzenie bije lepiej udokumentowane badanie.

**Wynikające zasady:**

- **Na plakacie:** problem w jednym zdaniu, zdjęcia urządzenia, funkcje, plansza „pokolenia urządzenia", jedna–dwie liczby wyniku. **Żadnych wykresów.**
- **Dziennik progresji awansuje z zabezpieczenia prawnego na główny materiał prezentacyjny.** Zdjęcia wersji 1, 2, 3 z jednym zdaniem o tym, co się poprawiło. **Fotografować także wersje nieudane** — u MAPPER-a jeden z trzech wniosków był negatywny („bez zakłóceń w treningu model padał w rzeczywistości") i to czyta się jako rzetelność mocniej niż tabela.
- **Liczby typu nakładu i skali działają lepiej niż pomiary:** liczba godzin pracy, liczba zbudowanych wersji, liczba cykli sprzęgła bez uszkodzenia.
- **Wykresy i tabele w segregatorze na stoisku**, na pytania jurora. **[fakt]** Kryteria oceny obejmują „znajomość zastosowanych metod i założeń" — to jest oceniane z rozmowy, nie z plansz.
- **Format „czego się nauczyliśmy"** — trzy ponumerowane wnioski, w tym co najmniej jeden o tym, co nie zadziałało.

**Co się NIE zmienia:** pomiar sprzęgła i moment wyliczony dla masy użytkownika są **narzędziami projektowymi**, nie materiałem prezentacyjnym. Bez nich nie da się dobrać sprężyny — a źle dobrana sprężyna to albo urządzenie bezużyteczne, albo niebezpieczne. Ponadto **na ISEF pomiary są obowiązkowe**: tam ocenia ekspert dziedzinowy, który zapyta o próbę, procedurę i niepewność.

**Próg wejścia do finału jest niższy, niż zakładano.** **[W]** W kategorii bez liczb i badań znalazł się m.in. projekt lokalizatora rowerowego, którego wnioski sprowadzały się do tego, że płytka wyszła, autor nauczył się lutować drobne elementy i urządzenie mieści się na ramie, choć zabrakło miejsca na baterię — projekt przeszedł do finału i nie głosami publiczności. Konsekwencja praktyczna: **zgłoszenie lutowe nie jest wąskim gardłem.** Wysiłek przenosi się na to, co stoi na stoisku w październiku 2027.

**Krajobraz konkurencyjny (edycja 2026):** *Kolano Pneumatyczne* było **jedynym** urządzeniem wspomagającym / medyczno-inżynieryjnym w całej stawce. Jury nie zobaczy „kolejnej rzeczy na kolano" — zobaczy pojedynczy precedens. To osłabia ryzyko kolizji z sekcji 12 o jeden stopień.

---

## 11. Ograniczenia i założenia

- Urządzenie zakłada zachowaną wolicjonalną kontrolę ruchu i zakres zgięcia kolana wystarczający do zmagazynowania energii.
- Skuteczność zależy krytycznie od dopasowania mankietów — to nie jest szczegół wykonawczy, tylko zmienna pomiarowa (teza 2).
- Testy z jednym użytkownikiem nie pozwalają na wnioski o populacji. Każdy wynik opisywany jako pomiar na osobie, nie jako wynik badania.
- Sprzęgło z zapadką daje regulację skokową, nie płynną.
- **[W]** Wilgoć i pot są problemem dla wariantów elektrycznych sprzęgła; wariant mechaniczny jest na to odporny.
- **Projekt jednoosobowy, 14 miesięcy do finału.** Odniesienie: MAPPER to 3 osoby i 18 miesięcy. **[fakt]** Indywidualne zwycięstwa są normą (Węgrzyn 2023, Pająk 2025), więc solo niczego nie przekreśla — ale wymusza zawężenie zakresu do jednego trybu (sekcja 8) i rezygnację z równoległych wątków. Każda dołożona funkcja odbiera czas jakości wykonania, a jakość wykonania jest tym, co przy stoisku widać.

---

## 12. Ryzyka

| Ryzyko | Wpływ | Mitygacja |
|---|---|---|
| **Zwolnienie obciążonej zapadki wymaga zbyt dużej siły** | **Krytyczny — koniec projektu w tej formie** | Test stanowiskowy jako pierwsze zadanie, sierpień 2026, przed jakimkolwiek zakupem |
| Sprawności przeniesienia nie da się wiarygodnie zmierzyć prostymi środkami | Wysoki — upada teza 2 | Test metody równolegle ze sprzęgłem, wrzesień 2026 |
| Nagłe zwolnienie sprężyny w nieoczekiwanym momencie | **Krytyczny — bezpieczeństwo użytkownika** | Mechaniczne rozłączenie awaryjne w wersji pierwszej, nie w drugiej. Ogranicznik energii. Testy początkowo bez obciążenia ciałem |
| Kolizja z projektem *Kolano Pneumatyczne* (finał Explory 2026) | Średni | Tamten projekt jest bierny, bez sprzęgła i bez danych pomiarowych. Różnicę wyeksponować wprost w dokumentacji, nie przemilczeć |
| Brak zgody IRB przed rozpoczęciem zbierania danych od innych osób | **Krytyczny — dyskwalifikacja z ISEF, nieodwracalna** | Procedura uruchomiona przez mentora przed pierwszym pomiarem z udziałem innej osoby (sekcja 13) |
| Nieznalezienie pracy, która istnieje | Średni | Przeszukanie wielu baz przed zgłoszeniem; deklaracja zawsze jako „nie znaleziono w bazach X, Y, Z" |
| Brak drukarki 3D na starcie | Niski | Etap 0 wykonalny z części drukowanych na zlecenie |
| **Brak walidacji zewnętrznej** (nie istnieje obwód zawodów dla ortez) | **Wysoki — słabość strukturalna wobec konkurencji z wynikami z zawodów** | Sekcja 10A: pisemna ocena fizjoterapeuty, tabela porównawcza, otwarte repozytorium, El-Robo-Mech przed Explory |
| **Rozmycie zakresu przy pracy solo** — dokładanie trybów kosztem jakości wykonania | Wysoki | Zakres zamrożony w sekcji 8. Schody dopiero po działającej wersji podstawowej. Chód poza horyzontem |
| Brak kontaktu z fizjoterapeutą przed projektowaniem mechaniki | Średni — konstrukcja projektowana na domysłach | Kontakt we wrześniu 2026 jako źródło wymagań, nie jako recenzja gotowej rzeczy |

---

## 13. Zgodność formalna

### 13.1 ISEF — udział ludzi w badaniu

**[D]** Każdy projekt, w którym ktokolwiek poza samym badaczem testuje prototyp lub dostarcza danych, jest badaniem z udziałem ludzi i wymaga **zatwierdzenia przez IRB przed rozpoczęciem zbierania danych**. Szkolne IRB to minimum trzy osoby, w tym pracownik ochrony zdrowia lub zdrowia psychicznego. Braku zgody nie da się naprawić po fakcie.

**Dotyczy:** każdego pomiaru z udziałem ojca, dziadka, fizjoterapeuty lub innego testera.

**Nie dotyczy:** nieformalnej rozmowy o objawach, prowadzonej dla zrozumienia problemu, jeśli nie jest rejestrowana jako dane badawcze. **Granica jest cienka — moment przejścia od rozmowy do pomiaru jest momentem, przed którym musi być zgoda.**

**Kolejność działań:**
1. Mentor uruchamia powołanie szkolnego IRB.
2. Research Plan opisujący procedurę pomiarów.
3. Formularz ISEF 4 (Human Participants) plus wzory zgód.
4. Zatwierdzenie **przed** pierwszym pomiarem z udziałem innej osoby.
5. Każda zmiana Research Planu wymaga ponownego zatwierdzenia.

**[L]** Do zweryfikowania: czy Explory wymaga analogicznej procedury. Regulamin zakazuje wyłącznie badań **inwazyjnych**; testy noszenia ortezy inwazyjne nie są.

### 13.2 Ochrona danych

Nagrania wideo i dane pomiarowe od osób testujących to dane osobowe. Do rozstrzygnięcia przed pierwszym pomiarem: podstawa prawna, okres przechowywania, sposób anonimizacji materiału w prezentacji konkursowej.

### 13.3 Bezpieczeństwo

Urządzenie magazynuje energię mechaniczną i przenosi siłę na staw. **Mechanizm rozłączenia awaryjnego jest wymogiem wersji pierwszej.** Pierwsze testy z obciążeniem prowadzone na stanowisku, nie na człowieku.

---

## 14. Cel Zrównoważonego Rozwoju

**Cel 3 — Dobre zdrowie i jakość życia.**

**[D]** Wymóg regulaminowy Explory (§4 pkt 4) — każdy projekt musi wskazać jeden główny cel. Standard oceny (§7 pkt 3c): znać cel i wykazać związek, pokazać odpowiedź na konkretny problem, uzasadnić pozytywny wpływ. Nie trzeba „spełniać celu w 100%".

**Konkretny problem, nie ogólnik:**
- **[L]** Czas oczekiwania na endoprotezoplastykę kolana w Polsce — do ustalenia z danych NFZ. **Zadanie na wrzesień 2026.**
- **[D]** Roam opisuje lukę: osoby, dla których operacja jest za wcześnie lub niemożliwa, a dla których nie ma nic pomiędzy lekami przeciwbólowymi a stołem operacyjnym.
- Dostępność: urządzenia komercyjne kosztują ok. 28 000 zł i nie są w Polsce refundowane. Różnica między „istnieje" a „istnieje dla mnie".
- **[L]** Koszt upadków u osób starszych i rola osłabionego kolana — do uzupełnienia danymi.

---

## 15. Harmonogram

| Termin | Kamień milowy |
|---|---|
| **sierpień 2026** | Test sprzęgła. Rozmowa z użytkownikiem. Obliczenie momentu docelowego. **Dziennik progresji od dnia pierwszego** |
| wrzesień 2026 | **Kontakt z fizjoterapeutą — jako źródło wymagań, przed projektowaniem mechaniki.** Test metody pomiaru sprawności przeniesienia. Rubryka SDG z danymi NFZ. Uruchomienie procedury IRB |
| paź–gru 2026 | Wersja 1 mechaniki, charakterystyka na stanowisku. Zwolnienie awaryjne. Otwarte repozytorium założone |
| styczeń 2027 | Wersja 2. Pierwsze pomiary porównawcze na platformie tensometrycznej |
| **28 lutego 2027** | **Zgłoszenie do Explory + El-Robo-Mech** (projekt nie musi być ukończony; próg wejścia niski — sekcja 10B) |
| marzec 2027 | Wersja 3. Pomiary elektromiograficzne z ortezą i bez. Materiał wideo — służy zarówno El-Robo-Mech, jak i półfinałowi Explory |
| **ok. 14–17 kwietnia 2027** | **El-Robo-Mech — twardy kamień milowy.** Wymaga **działającego prototypu**. Jedyna dostępna walidacja zewnętrzna przed finałem Explory (sekcja 10A). **[L]** Data oszacowana z poprzednich edycji — zweryfikować regulamin |
| maj–czerwiec 2027 | Półfinał Explory: plakat wg zasad z 10B, wideo, wystąpienie. Materiały w większości gotowe z kwietnia |
| lato 2027 | **Pisemna ocena fizjoterapeuty.** Dane całodzienne. Tabela porównawcza wypełniona liczbami. Schody — tylko jeśli wersja podstawowa działa |
| wrzesień 2027 | Stanowisko demonstracyjne (krzesło tensometryczne) jako eksponat. Plansza „pokolenia urządzenia". Segregator z wykresami na pytania |
| **20–23 października 2027** | **Finał Explory, Gdynia** |
| maj 2028 | ISEF — jeśli kwalifikacja. **Tu pomiary są obowiązkowe**, inaczej niż na Explory |

**Uwaga o kalendarzu:** matura maj 2029. Edycja Explory 2028 prowadziłaby do ISEF w maju 2029, czyli w miesiącu matury. **Edycja 2027 to jedyne czyste okno na ISEF.**

---

## 16. Otwarte pytania

- Siła zwolnienia obciążonej zapadki w funkcji geometrii zęba — **rozstrzyga o istnieniu projektu**
- Metoda pomiaru sprawności przeniesienia momentu wykonalna prostymi środkami
- Czy istnieje opublikowana wartość sprawności przeniesienia — przeszukanie w bazach poza dotychczasowymi
- Kategoria ISEF: Biomedical Engineering czy Robotics / Engineering Mechanics (aktualne liczebności do sprawdzenia w 2027)
- Czy zespół *Kolana Pneumatycznego* wraca w edycji 2027
- Dane NFZ o kolejkach na endoprotezoplastykę
- Czy Explory wymaga procedury analogicznej do IRB
- **Termin edycji El-Robo-Mech względem października 2027** — czy da się mieć wynik z niezależnego konkursu przed finałem Explory (sekcja 10A, substytut walidacji zewnętrznej)
- Czy wśród laureatów Nagrody Głównej i nagród SDG z ostatnich edycji występują pomiary — przegląd objął finalistów 2026, nie laureatów z lat wcześniejszych; źródła trudno dostępne

---

## Załącznik A — rejestr korekt

*Prowadzony od pierwszej wersji, żeby żaden zweryfikowany błąd nie wrócił przy kolejnej rundzie przeglądu.*

| # | Błąd | Stan faktyczny | Data |
|---|---|---|---|
| 1 | Zakaz Explory dotyczy wszystkich badań z udziałem ludzi | §4 pkt 5 zakazuje wyłącznie badań **inwazyjnych**; testy noszenia są dopuszczalne | sierpień 2026 |
| 2 | „Kolano Pneumatyczne" to proteza dla osoby po amputacji | To orteza magazynująca energię — bezpośrednia kolizja tematyczna, nie odległa | sierpień 2026 |
| 3 | Sterowane sprzęgło w ortezie kolana to luka w dziedzinie | Zajęte: Irby i wsp. 1999 (sprzęgło zwojowe w ortezie kolana), przegląd MDPI 2022, patenty US 9 788 985 i US 12 465 543. Teza przeformułowana na koszt + pomiar + integrację | sierpień 2026 |
| 4 | Forge (Roam Robotics) jako punkt odniesienia | Forge to produkt dla armii USA — odwołanie zakazane regulaminem. Właściwy punkt odniesienia: **Ascend** | sierpień 2026 |
| 5 | Wyniki pomiarów są główną walutą Explory i mają trafić na plakat | Przegląd 29 projektów edycji 2026: wzorcowa dokumentacja pomiarowa występuje głównie w biologii i chemii. Dla inżynierii odpowiednikiem metodologii jest **dziennik postępu budowy**. Plakat bez wykresów — patrz sekcja 10B | sierpień 2026 |
| 6 | Próg wejścia do finału wymaga dopracowanego zgłoszenia | Do finału 2026 przeszedł projekt, którego wnioski sprowadzały się do „płytka wyszła, nauczyłem się lutować, zabrakło miejsca na baterię". Zgłoszenie lutowe nie jest wąskim gardłem | sierpień 2026 |
| 7 | Kolizja tematyczna z *Kolanem Pneumatycznym* jest głównym ryzykiem konkurencyjnym | Kolano było **jedynym** urządzeniem wspomagającym w całej stawce 2026. Jury zobaczy pojedynczy precedens, nie zatłoczoną kategorię. Ryzyko obniżone o stopień | sierpień 2026 |
| 8 | Walidacja własnymi pomiarami wystarcza | Najmocniejszy projekt inżynierski 2026 opierał wiarygodność na **6 podiach w 6 startach zawodów**, nie na pomiarach. Dla ortezy brak odpowiednika — luka wymaga świadomej kompensacji, sekcja 10A | sierpień 2026 |
| 9 | ConOps drona napisany przez autora projektu | Napisany przez model. Styl i struktura obu dokumentów pochodzą z tego samego źródła — nie traktować podobieństwa jako potwierdzenia | sierpień 2026 |
| 10 | Głównym wskaźnikiem skuteczności jest przekroczenie progu 1,53 Nm/kg | To miara dla osoby, która **nie może** wstać. Użytkownik docelowy wstaje, ale z bólem. Właściwa metryka: **redukcja aktywności mięśnia czworogłowego** przy tej samej czynności. Tak też pozycjonują się Roam i Spring Loaded | sierpień 2026 |
| 11 | El-Robo-Mech jako termin dodatkowy, poza ścieżką krytyczną | Wypada ok. 14–17 kwietnia 2027, czyli **przed** półfinałem Explory. Wymaga działającego prototypu i staje się twardym kamieniem milowym oraz jedyną dostępną walidacją zewnętrzną | sierpień 2026 |
