# ISEF — badania z udziałem ludzi

**Zadanie 4d nr 2 oraz pozycja 1 z sekcji 3 `PRZEKAZANIE.md`.** Handbook, sekcja 5.5: „najbardziej prawdopodobna przyczyna dyskwalifikacji na technikalium w całym projekcie".

---

## 0. Status tego pliku — ZMIENIONY 15 VIII 2026, wieczór

**[fakt] Oryginał regulaminu został odczytany w całości.**

Źródło: *International Rules for Pre-College Science Research: Guidelines for Science and Engineering Fairs **2026–2027***, Society for Science, 46 stron, pobrane z `sspcdn.blob.core.windows.net/files/Documents/SEP/ISEF/2027/Rules/Book.pdf` dnia 15 VIII 2026. Uzupełniająco: strony `societyforscience.org/isef/international-rules/human-participants/` i `.../roles-and-responsibilities-of-students-and-adults/`.

**To jest rocznik 2026–2027, czyli regulamin edycji prowadzącej do ISEF 2027.** Regulamin edycji 2027–2028 (prowadzącej do ISEF **2028**, czyli naszej) jeszcze nie istnieje — ukaże się prawdopodobnie ~połowa 2027 `[wniosek]`. Struktura reguł jest stabilna między latami `[wniosek, na podstawie porównania z brzmieniem cytowanym w materiałach z lat 2024–2026]`, ale **daty i numery formularzy trzeba będzie sprawdzić ponownie po publikacji rocznika 2027–2028**. To jedyna rzecz, która w tym pliku pozostaje otwarta.

Poprzednia wersja tego pliku była zbudowana ze streszczeń wyszukiwarki. **Trzy jej ustalenia okazały się błędne** — patrz `KOREKTY.md` K-020, K-021, K-022.

---

## 1. Badanie na sobie — ZWOLNIONE, i znam dokładny warunek

To była pozycja `[luka]` nr 2 z sekcji 4c/B5 `00_PYTANIA_I_LUKI.md` i pozycja 7 z listy zamkniętej poprzedniej wersji.

**[fakt, cytat z oryginału]** Sekcja *EXEMPT STUDIES (DO NOT REQUIRE IRB PRE-APPROVAL OR HUMAN PARTICIPANTS PAPERWORK)*, pozycja 1:

> „Student-designed Invention, Prototype, Computer Applications, Engineering/Design Project or Consumer Product Testing in which the student researcher (or researchers if a team) is the only person testing the invention, prototype, computer application or consumer product **and the testing does not pose a health or safety hazard**."

Podpunkt b tej samej pozycji określa, co zwolnienie łamie:

> „IRB review and pre-approval is required if the project involves more than the student researcher (or single adult guardian serving as the sole tester) or **any introduction of a human variable or factor** in the testing of a consumer product/invention/prototype/application (e.g., amount of sleep, strength or endurance of tester, etc.)."

### 1.1 Dwa warunki, nie jeden — i drugi jest groźniejszy

Poprzednia wersja tego pliku znała tylko warunek „brak ryzyka" i wokół niego zbudowała cały niepokój. **Warunek drugi — „żadnej zmiennej ludzkiej" — jest dla tego projektu trudniejszy do spełnienia i został przeoczony.**

| Wariant pomiaru | Czy zwolniony | Dlaczego |
|---|---|---|
| noszę własne urządzenie, mierzę szum toru, impedancję, jakość sygnału | **tak** | jestem jedynym badanym, brak zmiennej ludzkiej |
| noszę własne urządzenie, mierzę dokładność klasyfikacji SSVEP na sobie | **tak** `[wniosek]` | jw. — mierzona jest własność urządzenia, nie osoby |
| porównuję dwie geometrie elektrod **na sobie** | **tak** `[wniosek]` | zmienna jest po stronie urządzenia, nie człowieka |
| mierzę, jak wynik zmienia się od zmęczenia, pory dnia, wyspania | **NIE** | to jest wprost wymieniona „human variable" (`amount of sleep`) |
| ktokolwiek poza mną zakłada urządzenie | **NIE** | wprost |
| ankieta „czy widać, że to masz na sobie" wśród widzów na stoisku | **NIE** | patrz sekcja 1.2 |

**[wniosek] Konsekwencja projektowa, konkretna:** eksperyment ze `09_UMIEJSCOWIENIE.md` sekcja 5b — jeden tor analogowy, dwie wiązki elektrodowe, porównanie geometrii — **mieści się w zwolnieniu, dopóki badanym jestem tylko ja**. To jest dobra wiadomość: najważniejsza kampania pomiarowa projektu nie wymaga formalności.

**[wniosek] Konsekwencja, która psuje jeden pomysł:** metryka „stabilność w ciągu dnia" z wariantu 2 twierdzenia (`00_STRESZCZENIE.md` sekcja 1.2) ociera się o zmienną ludzką. Mierzenie dryfu jakości sygnału w czasie noszenia — bezpieczne. Mierzenie, jak wynik zależy od wyspania badanego — **nie**. Granicę trzeba trzymać świadomie przy projektowaniu planu eksperymentalnego.

### 1.2 Pułapka, której nie było w poprzedniej wersji

**[fakt, cytat]** Reguła 7a sekcji *RULES*:

> „IRB review and pre-approval is required when the student-designed invention, prototype, application, etc. is tested by human participants other than the student researcher(s) … **This includes surveys conducted regarding potential use or opinions of the invention or consumer product by the general public.**"

Skala widoczności z `06_TABELA_PARAMETROW.md` sekcja 4 zawiera propozycję: *„zdjęcie osoby w urządzeniu, pytanie do widza »gdzie ono jest«"* jako pomiar zamieniający kolumnę opiniową w liczbę. **To jest ankieta opinii publicznej o wynalazku i wymaga uprzedniej zgody IRB.** Nie wolno tego zrobić spontanicznie na stoisku.

Wyjątek zapisany w tej samej regule: *„This is not intended to apply to receiving professional feedback from experts in the field of study prior to experimentation"* — konsultacja z bratem albo z opiekunem naukowym nie jest badaniem.

---

## 2. Urządzenie elektryczne przy głowie — NIE ma osobnej kategorii ryzyka

To była pozycja 5 z listy zamkniętej i **najważniejsza niedomknięta pozycja całego etapu 1**.

**[fakt] Odpowiedź: w regulaminie ISEF nie istnieje osobna kategoria ryzyka dla urządzeń elektrycznych mających kontakt z ciałem człowieka.** Przeczytałem w tym celu całą sekcję *Hazardous Chemicals, Activities or Devices Rules* (strony 18–19 oryginału). Jej zakres, wyliczony w nagłówku sekcji:

> „Includes DEA-controlled substances, prescription drugs, alcohol & tobacco, firearms and explosives, radiation, lasers, drones, vapes etc."

Definicja czynności niebezpiecznej z tej samej sekcji:

> „Hazardous activities are those that involve a level of risk **above and beyond that encountered in the student's everyday life**."

**[wniosek] Urządzenie rejestrujące EEG, zasilane bateryjnie, o napięciach roboczych rzędu jednostek woltów, nie mieści się w żadnej z wyliczonych kategorii i nie przekracza ryzyka dnia codziennego** — słuchawki douszne i aparaty słuchowe są przedmiotami codziennego użytku o tej samej klasie kontaktu elektrycznego. Ocena ryzyka pozostaje po stronie IRB szkolnego (sekcja 3), ale nie ma reguły, która przesądzałaby ją z góry na niekorzyść.

### 2.1 Rozróżnienie, na którym to stoi — i które trzeba mieć zapisane

**Rejestracja, nie stymulacja.** Regulamin zakazuje uczniom *„performing medical procedures on human participants"* i wymaga nadzoru licencjonowanego pracownika ochrony zdrowia przy diagnostyce i terapii. Urządzenie **podające** prąd do głowy (tDCS, tACS) byłoby zupełnie inną rozmową — prawdopodobnie procedurą medyczną. Urządzenie **mierzące** napięcie na skórze nią nie jest.

To rozróżnienie trzeba mieć w Research Plan wypisane jednym zdaniem, nie improwizowane przed komisją.

### 2.2 Gdzie elektryka JEST regulowana — w regulaminie stoiska

**[fakt]** Osobne reguły elektryczne istnieją, ale dotyczą **ekspozycji na stoisku**, nie badań. *ISEF Display & Safety Regulations*, sekcja *Electrical Regulations*:

- „No exposed live circuits **over 36 volts** are allowed."
- „Electrical devices must be protectively enclosed. Any enclosure must be non-combustible."
- „An insulating grommet is required at the point where any wire or cable enters any enclosure."
- „There must be an accessible, clearly visible on/off switch."
- zakazane na stoisku: „Batteries with open-top cells or wet cells or **battery packs over 100 watt-hour capacity**"

**[wniosek] Projekt spełnia to bez wysiłku** — pracuje na jednostkach woltów i baterii o pojemności rzędu watogodziny. Wymóg obudowy i wyłącznika to kilka zdań w dokumentacji konstrukcyjnej, nie ograniczenie projektowe.

**[fakt] Jedna rzecz do zaplanowania, bo jest nieoczywista:** *„Projects competing at ISEF must have an exhibit that … is visible during all operable hours of the exhibit hall **without reliance on electricity or internet connections**."* Plakat i ekspozycja muszą być czytelne bez prądu. Demonstracja na żywo jest dozwolona i zasilanie jest dostępne, ale **stoisko nie może istnieć wyłącznie jako demo**.

### 2.3 Wymóg z handbooka obowiązuje niezależnie

Sekcja 12 handbooka, bez zmian i nienegocjowalna: zasilanie bateryjne albo izolacja galwaniczna od sieci, jako warunek wstępny konstrukcji. Regulamin ISEF tego nie wymaga wprost dla badań, ale wymaga dla stoiska, a zdrowy rozsądek wymaga zawsze.

---

## 3. Role dorosłych — dwie z trzech informacji z poprzedniej wersji były błędne

**[fakt, cytaty z sekcji *Roles & Responsibilities of Students and Adults*]**

| Rola | Próg formalny | Co robi |
|---|---|---|
| **Adult Sponsor** | „a teacher, parent, professor, and/or other professional scientist" — **bez wymogu stopnia** | ocena ryzyka razem z uczniem, przegląd formularzy, Formularz 1 |
| **Qualified Scientist (QS)** | „Earned a doctoral/professional degree in a scientific discipline related to student's area of research **AND/OR** Individual with **extensive experience and expertise** in the student's area of research" | zatwierdza plan badawczy **przed** startem, nadzór, Formularz 2B |
| **Direct Supervisor (DS)** | „**Does not need an advanced degree**"; musi znać projekt i przyjąć potrzebne szkolenie; „May also serve as the Adult Sponsor" | bezpośredni nadzór nad eksperymentem, Formularz 3 |

**Poprawka nr 1 (K-020):** poprzednia wersja podawała, że Qualified Scientist **wymaga doktoratu**. To nieprawda — regulamin dopuszcza alternatywę „rozległe doświadczenie i wiedza ekspercka" i łączy oba warunki spójnikiem `AND/OR`. **Brat kończący studia inżynierskie i pracujący w firmie produkującej precyzyjną elektronikę jest realnym kandydatem na QS w części sprzętowej** `[wniosek]` — o ile ktoś zechce to poświadczyć. To zmienia ocenę ryzyka formalnego z sekcji 3 `00_PYTANIA_I_LUKI.md` z wysokiego na średnie.

**Poprawka nr 2 (K-021):** rola nazywa się **Direct Supervisor**, nie „Designated Supervisor", i **nie jest wyznaczana przez Qualified Scientist** jako jego przedłużenie w ogólności. DS jest wymagany w szczególności wtedy, gdy QS mieszka gdzie indziej („May live elsewhere and not be local to the student, in which case, a Direct Supervisor must be appointed"). DS nie potrzebuje żadnego stopnia i **może być tą samą osobą co Adult Sponsor**.

**Wniosek operacyjny:** opiekun szkolny ze stopniem magistra spokojnie obsadza **Adult Sponsor** i **Direct Supervisor** jednocześnie. QS jest potrzebny tylko wtedy, gdy zażąda go IRB.

---

## 4. Czego poprzednia wersja w ogóle nie wiedziała — IRB trzeba ZBUDOWAĆ

**[fakt]** To jest najbardziej konkretna pozycja harmonogramowa, jaka wyszła z odczytania oryginału, i nie było jej w żadnym wcześniejszym dokumencie.

IRB to nie jest instytucja, do której się pisze. **Dla projektu prowadzonego w szkole i w domu IRB musi zostać powołane przy szkole**, a jego skład jest określony co do osoby:

> „An IRB must consist of a minimum of three members including the following:
> • An educator (**not the teacher that is serving as the Adult Sponsor**)
> • A school administrator (preferably principal or vice principal)
> • **A medical or mental health professional.** The medical or mental health professional may be a medical doctor, nurse practitioner, physician's assistant, doctor of pharmacy, registered nurse, psychologist, licensed social worker or licensed clinical professional counselor."

Dodatkowo, konflikt interesów: „no Adult Sponsor, parent or other relative of the student, the Qualified Scientist, or Direct Supervisor who oversees the project, may serve on the IRB". Czyli opiekun projektu **nie może** zasiadać w komisji oceniającej ten projekt, i **brat też nie**.

**[wniosek] Co to znaczy praktycznie:** żeby przebadać choćby jednego kolegę z klasy, trzeba mieć w szkole trzyosobową komisję, w tym pielęgniarkę szkolną albo psychologa szkolnego (oba zawody są na liście dopuszczonych) oraz dyrektora lub wicedyrektora. **To jest do zorganizowania w polskiej szkole** — pielęgniarka i psycholog zwykle są — ale wymaga rozmowy z dyrekcją, a nie wypełnienia formularza. I musi być zrobione **przed** pierwszym pomiarem na kimkolwiek innym niż autor.

Alternatywa przewidziana regulaminem: „If necessary, the local or ISEF-affiliated SRC can serve as an IRB as long as it has the required membership." Dla uczestnika z Polski afiliowanym targiem jest Explory/FZT — **czy FZT prowadzi SRC pełniące funkcję IRB, jest pytaniem do organizatora i pozostaje `[luka]`.** To jedno konkretne pytanie mailem na `konkurs@fzt.org.pl` może zaoszczędzić całą tę procedurę.

---

## 5. Formularze — komplet, z numeracją rocznika 2026–2027

**[fakt]** Dla **każdego** projektu, niezależnie od tematu:

| Formularz | Kiedy |
|---|---|
| Checklist for Adult Sponsor (1) | **przed** eksperymentem |
| Student Checklist (1A) | **przed** eksperymentem |
| Research Plan / Project Addendum | **przed** eksperymentem |
| Approval Form (1B) | — |
| Student Support Disclosure Form (2A) | — |
| Regulated Research Institution Form (2C) | jeśli praca poza domem i szkołą, **po** eksperymencie |
| Continuation/Research Progression Form (7) | jeśli kontynuacja |

Dodatkowo dla badań z udziałem ludzi (czyli **nie** w naszym wariancie zwolnionym): Human Participants Form (4), zgody, kopie ankiet, Qualified Scientist Form (2B) gdy wymagany, Risk Assessment (3) gdy wymagany.

**Pozycja niejednoznaczna, zapisuję ją jako niejednoznaczną, a nie rozstrzygam:** reguła 8 sekcji *Documentation and Approval* mówi „Projects that involve the testing of any student-designed invention, prototypes or consumer product **requires Risk Assessment Form 3**", bez zastrzeżenia o zwolnieniu. Jednocześnie nagłówek sekcji *Exempt Studies* mówi, że projekty zwolnione nie wymagają „human participants paperwork". Formularz 3 jest formularzem oceny ryzyka, nie formularzem badań na ludziach. **[wniosek] Interpretacja bezpieczna: wypełnić Formularz 3 mimo zwolnienia.** Kosztuje jedną stronę papieru, a jego brak jest kategorią błędu, która dyskwalifikuje. Nie ma powodu oszczędzać tutaj.

---

## 6. Reguła 12 miesięcy — brzmi INACZEJ, niż podaje handbook

**[fakt, dwa cytaty z rocznika 2026–2027]**

Sekcja *Eligibility/Limitations*, punkt 4:
> „Each student is only allowed to enter one project. That project may include no more than 12 months of continuous research and **may not include research performed before January 2026**."

Sekcja *Continuation/Research Progression of Projects*, punkt 3:
> „Students will be judged only on laboratory experiment/data collection performed over **12 continuous months beginning no earlier than January 2026 and ending May 2027**."

**Czego tu nie ma: liczby osiemnaście.** Handbook, sekcja 5.4, podaje „zakaz wykorzystywania badań wykonanych wcześniej niż 18 miesięcy przed ISEF". Tej reguły w oryginale nie ma. Reguła jest zakotwiczona w **kalendarzu**, nie w odstępie od imprezy: styczeń roku poprzedzającego ISEF jako najwcześniejszy start, maj roku ISEF jako najpóźniejszy koniec, dwanaście ciągłych miesięcy do wyboru wewnątrz tego okna. Wpis `KOREKTY.md` **K-023**.

### 6.1 Przełożenie na nasz rocznik

`[wniosek, silny — wzorzec z jednego rocznika, do potwierdzenia po publikacji reguł 2027–2028]` Dla ISEF maj 2028 okno wyniesie **styczeń 2027 – maj 2028**, z dowolnym ciągłym dwunastomiesięcznym blokiem w środku.

To zmienia ostrzeżenie z K-006 i trzeba je postawić na nowo:

| Wydarzenie | Data | Czy mieści się w oknie |
|---|---|---|
| El-Robo-Mech (albo zamiennik) | ~IV 2027 | **tak, mieści się** — po styczniu 2027 |
| półfinał Explory | V–VI 2027 | **tak** |
| finał Explory | X 2027 | **tak** |
| ISEF | V 2028 | koniec okna |

**Ale blok ma dwanaście miesięcy, a od kwietnia 2027 do maja 2028 jest trzynaście.** Czyli: albo blok biegnie ~V 2027 – V 2028 i wtedy pomiary z kwietnia 2027 wypadają poza nim, albo blok biegnie I–XII 2027 i wtedy nic po grudniu 2027 się nie liczy.

**[wniosek] Rozstrzygnięcie praktyczne:** formalną kampanię pomiarową pod ISEF prowadzić od **maja 2027**. Wszystko wcześniejsze — cały rok szkolny 2026/2027, nauka PCB, prototypy, pomiary rozpoznawcze — traktować jako **prace rozwojowe przed kampanią**, nie jako dane do ISEF. Materiał na El-Robo-Mech i na półfinał Explory może pochodzić z tego wcześniejszego okresu bez żadnego problemu, bo tamte konkursy reguły 12 miesięcy nie mają (`HANDBOOK.md` sekcja 4.13, potwierdzone w regulaminie Explory — nie ma tam żadnego ograniczenia czasowego).

To jest **łagodniejsze** niż ostrzeżenie z K-006: nie „wszystko trzeba będzie powtórzyć", tylko „kampania pod ISEF ma swój własny start i jest nim maj 2027".

---

## 7. Terminarz wsteczny — przeliczony na twardych regułach

| Kiedy | Co | Skąd ten termin |
|---|---|---|
| **jesień 2026** | rozmowa z dyrekcją szkoły: czy da się powołać IRB w składzie edukator + dyrektor + pielęgniarka/psycholog | najdłuższy proces zależny od kogoś z zewnątrz, sekcja 4 |
| jesień 2026 | pisemna zgoda opiekuna szkolnego na rolę **Adult Sponsor** i **Direct Supervisor** | tanie, bez terminu, zdejmuje ryzyko |
| jesień 2026 | mail do FZT: czy organizator prowadzi SRC/IRB dla polskich uczestników | jedno pytanie, może skasować całą sekcję 4 |
| **cały rok szk. 2026/27** | pomiary **wyłącznie na sobie** — zwolnione, bez formalności | sekcja 1 |
| do 28 II 2027 | zgłoszenie do Explory | regulamin Explory §6 pkt 10 |
| ~IV 2027 | prototyp działający, konkurs zewnętrzny | `08` sekcja 4 |
| **przed V 2027** | Research Plan napisany, Formularze 1, 1A, 1B, 2A, 3 podpisane | muszą istnieć **przed** startem kampanii |
| **V 2027** | **start formalnej kampanii pomiarowej pod ISEF** | okno 12 miesięcy, sekcja 6.1 |
| **przed kampanią na grupie** | zgoda IRB, Formularz 4, zgody rodziców badanych niepełnoletnich | sekcja 1, bezwzględnie **przed** pierwszym pomiarem |
| X 2027 | finał Explory | regulamin Explory §6 |
| V 2028 | ISEF | — |
| **po publikacji reguł 2027–2028** (~poł. 2027) | przeczytać rocznik od nowa, sprawdzić daty i numery formularzy | jedyna pozycja otwarta w tym pliku |

---

## 8. Bilans — co się zmieniło względem poprzedniej wersji

| Pozycja | Było (streszczenia) | Jest (oryginał) |
|---|---|---|
| badanie na sobie | „prawdopodobnie zwolnione", warunek: brak ryzyka | **zwolnione**, dwa warunki: brak ryzyka **i brak zmiennej ludzkiej** |
| urządzenie elektryczne przy głowie | `[luka]`, „najważniejsza niedomknięta pozycja", potencjalnie dyskwalifikująca | **nie ma takiej kategorii ryzyka.** Reguły elektryczne dotyczą stoiska, próg 36 V |
| Qualified Scientist | wymaga doktoratu | doktorat **albo** rozległe doświadczenie. K-020 |
| Designated Supervisor | wyznaczany przez QS | nazywa się **Direct Supervisor**, bez wymogu stopnia, może być Adult Sponsorem. K-021 |
| IRB | traktowane jak instytucja zewnętrzna | **trzeba je powołać przy szkole**, skład określony co do osoby. Nowe |
| reguła 12/18 miesięcy | 12 mies. ciągłych + zakaz danych starszych niż 18 mies. | 12 mies. ciągłych w oknie **I roku N-1 – V roku N**. Osiemnastu miesięcy nie ma. K-023 |
| ankieta o widoczności na stoisku | pomysł na pomiar | **wymaga uprzedniej zgody IRB.** Nowe |

**Ocena ryzyka formalnego całego projektu: obniżona z „najbardziej prawdopodobna przyczyna dyskwalifikacji" na „do załatwienia jesienią 2026, jedna rozmowa z dyrekcją i jeden mail".**

Zdanie z sekcji 5.5 handbooka o dyskwalifikacji na technikalium było **ostrożnym domysłem, który się nie potwierdził**. Zostawiam je w handbooku z adnotacją, bo ostrożność była uzasadniona przy braku dostępu do źródła — ale nie należy już planować pod nią harmonogramu.
