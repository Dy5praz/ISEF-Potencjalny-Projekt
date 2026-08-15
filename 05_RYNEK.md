# 05 — Rynek komercyjny: baseline

**Zakres wg sekcji 10.E handbooka.** Co można dziś kupić, za ile, z jakimi parametrami. To jest punkt odniesienia, względem którego użytkownik chce być lepszy, więc musi być **zmierzony, nie opisany hasłowo**.

**Zastrzeżenie źródłowe:** ceny pochodzą ze streszczeń wyszukiwarki, nie ze sklepów. Sekcja 4 pokazuje, dlaczego przy cenach ten kanał jest szczególnie zawodny. **Każda cena w tym pliku wymaga potwierdzenia na stronie producenta przed użyciem w jakimkolwiek zestawieniu.**

---

## 1. Sprzęt badawczy i deweloperski

| Produkt | Producent | Kanały | Cena | Uwagi |
|---|---|---|---|---|
| **Cyton** | OpenBCI | 8 | modułowy, cena zależy od zestawu | rdzeń: ADS1299. Otwarty sprzęt i oprogramowanie. **Najbliższy punkt odniesienia dla własnej konstrukcji** |
| Cyton + Daisy | OpenBCI | 16 | — | |
| **EPOC X** | Emotiv | 14 | **999 USD** wg strony producenta | patrz sekcja 4 — sprzeczność cenowa |
| **Insight** | Emotiv | 5 | **499 USD** wg strony producenta | |
| systemy badawcze | g.tec | do 64+ | rząd dziesiątek tys. EUR | klasa laboratoryjna, poza budżetem |
| DSI | Wearable Sensing | 7–24 | rząd dziesiątek tys. USD | elektrody suche, klasa laboratoryjna |

## 2. Sprzęt konsumencki — opaski i słuchawki

| Produkt | Producent | Forma | Cena | Widoczne? |
|---|---|---|---|---|
| **Muse S Athena** | Interaxon | opaska na głowę | ~400–500 USD `[wniosek, streszczenie]` | tak, wyraźnie |
| **MW75 Neuro** | Neurable | słuchawki nauszne | **699 USD** | wygląda jak słuchawki |
| **Smartbuds** | NextSense | douszne, w pełni bezprzewodowe | **399,99 USD**, przedsprzedaż 249 USD | wygląda jak słuchawki douszne |
| **Guardian 4** | IDUN Technologies | douszne | brak ceny publicznej | j.w. |
| **Naox Wave** | NAOX | douszne | zapowiedź | j.w. |

**Ustalenia o tym rynku [wniosek, streszczenie]:**
- **NextSense Smartbuds** — start sprzedaży **9 lutego 2026**, deklarowane jako pierwsze w pełni bezprzewodowe słuchawki EEG. **6 czujników EEG**. Spin-off z Alphabet X, runda A 16 mln USD. Zastosowanie docelowe: sen
- **IDUN Guardian 4** — czwarta generacja platformy dousznej, we współpracy z Analog Devices, prezentacja na CES 2025. Certyfikacja CE i FCC planowana na **II kw. 2026**. Wyjścia to „wskaźniki gotowości poznawczej" i szacunki obciążenia, nie surowy sygnał
- **Neurable MW75 Neuro** — pozycjonowane jako słuchawki premium ze śledzeniem skupienia, **nie jako narzędzie badawcze**

**[wniosek] Wniosek dla twierdzenia projektu, ważny:** **żaden z produktów dousznych i zausznych na tym rynku nie jest interfejsem sterującym.** Wszystkie mierzą stan: sen, skupienie, obciążenie poznawcze. Sterowanie w formie dousznej **nie ma odpowiednika komercyjnego**.

To działa w obie strony i trzeba widzieć obie:
- **za:** baseline dla wariantu 1 z sekcji 2.1 `00_PYTANIA_I_LUKI.md` („przewaga przy stałej widoczności") jest **pusty albo bardzo słaby**. Nie trzeba bić NextSense na ITR, bo NextSense nie podaje ITR — nie robi sterowania
- **przeciw:** juror zapyta, dlaczego nikt tego nie robi. Odpowiedź „bo się nie da" jest zła. Odpowiedź „bo rynek konsumencki celuje w sen i skupienie, gdzie wystarcza alfa, a sterowanie wymaga innej klasy sygnału i innego toru" — jest dobra, i wynika z `03_SCIANY_FIZYCZNE.md` sekcja 3.1

---

## 3. Rynek inwazyjny — dla kontekstu, nie jako baseline

Nie kupuje się tego, ale jurorzy będą o to pytać.

| Firma | Stan na sierpień 2026 |
|---|---|
| **Neuralink** | badanie PRIME, **21 uczestników** na początku 2026 (12 we wrześniu 2025); USA, Kanada, Wielka Brytania, ZEA |
| **Synchron** | Stentrode; COMMAND: 6 pacjentów, 12 mies., zero poważnych zdarzeń niepożądanych; badanie rejestracyjne zapowiedziane na 2026 |
| **Precision Neuroscience** | **510(k) FDA w IV 2025** na rejestrację śródoperacyjną do 30 dni |
| **Blackrock Neurotech** | Utah array; deklaruje ponad 40 wszczepień u ludzi |

Wszystkie `[wniosek, streszczenie]`. Uwaga: liczby o „rynku BCI wartym 400 mld USD" z materiałów branżowych **odrzucam jako niewiarygodne** — to blog konsultingowy bez metodologii, najniższa pozycja w hierarchii z sekcji 13 handbooka.

---

## 4. Sprzeczność cenowa — przykład, dlaczego ten kanał wymaga ostrożności

Wyszukiwarka zwróciła dla Emotiv EPOC X **dwie ceny**:

| Źródło | Cena | Wiarygodność |
|---|---|---|
| emotiv.com (strona producenta) | **999 USD** | wysoka — producent o własnym produkcie |
| biohackeratlas.com | **99 USD** | **niska** — witryna afiliacyjna, prawdopodobnie błąd lub przynęta |

Różnica dziesięciokrotna. Przyjmuję 999 USD wg hierarchii źródeł z sekcji 13 handbooka.

**Po co ten przykład w dokumencie:** żeby było widać, jak wygląda błąd, którego ten etap **nie mógł wykluczyć systemowo**. Gdyby chodziło o parametr, na którym coś stoi, a nie o cenę widoczną gołym okiem jako absurd, przeszedłby niezauważony. To jest konkretna, mierzalna cena pracy bez dostępu do źródeł.

---

## 5. Zadanie 4d nr 7 — materiały i druk do kontaktu ze skórą

Decyzja zakupowa czeka od rundy drugiej. **Rekomendacja z K-011 potwierdzona.**

### 5.1 Technologia druku

`[wniosek, kilka źródeł zgodnych]` Obudowy aparatów słuchowych i wkładek dousznych wykonuje się przemysłowo **stereolitografią (SLA) lub DLP**, nie FDM. Powód podawany w materiałach branżowych: wymagania co do wykończenia powierzchni i szybkości produkcji.

Przeciwko FDM w tym zastosowaniu:
- warstwy zbierające zabrudzenia — istotne przy urządzeniu noszonym w uchu godzinami
- gorsze odwzorowanie drobnych krzywizn — a wkładka douszna to sama krzywizna
- uboga oferta materiałów z certyfikatem kontaktu ze skórą

**Włókno węglowe (PA12-CF z porzuconego projektu drona) jest tu przeciwskuteczne:** ścierne i sztywne, przy zerowej potrzebie sztywności.

### 5.2 Certyfikaty

Norma: **ISO 10993**. Dla kontaktu z nienaruszoną skórą wymagane minimum to `[wniosek, streszczenie]`:
- **ISO 10993-5** — cytotoksyczność
- **ISO 10993-10** — podrażnienie i uczulenie

Materiały branżowe do aparatów słuchowych: seria **E-Shell** (EnvisionTEC/ETEC) — E-Shell 300, 600 (miękkie wkładki i końcówki), 3000 (obudowy i otoplastyka). Deklarowane jako CE i biokompatybilne klasy IIa wg ISO 10993.

### 5.3 Ocena dostępności dla amatora — i tu jest problem

`[fakt, na podstawie zebranego materiału]` Znalezione rozwiązania certyfikowane są **przemysłowe**: materiały przeznaczone do drukarek profesjonalnych, sprzedawane w kanale B2B.

`[luka]` **Nie ustaliłem, czy istnieje żywica z certyfikatem ISO 10993-5/-10 dostępna dla osoby prywatnej w Polsce, w rozsądnej cenie, do zwykłej drukarki MSLA.** To jest pytanie zakupowe, nie naukowe, i wymaga sprawdzenia sklepów — czego nie zrobię bez sieci.

**Obejście, gdyby certyfikowana żywica okazała się niedostępna [domysł, do sprawdzenia w etapie 2]:** warstwa pośrednia między wydrukiem a skórą — silikonowa końcówka douszna klasy medycznej z rynku aparatów słuchowych, gotowa i tania, na wydrukowanym korpusie nośnym. Wtedy certyfikat dotyczy elementu kupionego, a wydruk nie dotyka skóry. **Bezpieczeństwo kontaktu jest warunkiem wstępnym konstrukcji wg sekcji 12 handbooka, nie sprawą do rozwiązania na końcu** — więc ta ścieżka musi być rozstrzygnięta, zanim powstanie pierwszy prototyp noszony.

### 5.4 Rekomendacja zakupowa — bez zmian

**Wstrzymać zakup Qidi Q2.** Przy formie zausznej właściwy zestaw to tania drukarka żywiczna (MSLA) plus ewentualnie zwykły FDM na oprzyrządowanie i uchwyty, łącznie taniej niż jedna Q2. Q2 pozostaje sensowna wyłącznie, jeżeli wróci projekt drona — osobna decyzja, nie ta.

---

## 6. Baseline w liczbach — co konkretnie trzeba pobić albo obejść

| Wymiar | Stan komercyjny | Nasza pozycja |
|---|---|---|
| ITR w formie dousznej | **nie istnieje** — żaden produkt nie robi sterowania | pole puste, ale to nie jest zaproszenie |
| ITR w formie widocznej | SSVEP z czapki: dziesiątki bit/min | **nie do pobicia w formie zausznej**, `03` sekcja 3 |
| cena | 400–1000 USD za konsumenckie douszne | osiągalna |
| czas montażu | słuchawki: sekundy | to jest wymiar, w którym forma zauszna **wygrywa z czapką** |
| kanały | 5–6 (NextSense), 14 (EPOC X) | porównywalne |
| widoczność | douszne wyglądają jak słuchawki | równorzędnie |
| **surowy dostęp do sygnału** | konsumenckie oddają wskaźniki, **nie surowy sygnał** | **tu mamy przewagę strukturalną** |

**[wniosek] Ostatni wiersz jest ważniejszy, niż wygląda.** NextSense i IDUN oddają „wskaźnik gotowości poznawczej", a nie mikrowolty. Oznacza to, że **nikt z zewnątrz nie może zweryfikować ani powtórzyć ich wyników** — a projekt otwarty, z surowym sygnałem i opublikowanym zbiorem danych, może. To jest wymiar przewagi, którego nie da się kupić za pieniądze i który arkusze oceny punktują wprost.
</content>
