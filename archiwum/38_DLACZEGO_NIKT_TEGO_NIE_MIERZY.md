# 38 — Dlaczego pola nikt nie tyka. Odpowiedź z trzech źródeł, jedna zła wiadomość

**Data:** 21 sierpnia 2026
**Pytanie użytkownika:** *„dlaczego potylica jest tak często omijana, trochę to podejrzliwe. Wiesz, skoro ledwo kto to tyka, to musi być jakiś powód. I oby to nie była dla nas zła wiadomość."*

**Pytanie jest trafne i było dziurą w audycie.** `35` i `36` sprawdziły **czy** ktoś to zmierzył. Żaden nie sprawdził **dlaczego nie**. To są dwie różne rzeczy: puste pole może być luką albo ślepą uliczką, a dotąd zakładałem pierwsze bez sprawdzenia.

---

## 0. Odpowiedź w trzech zdaniach

**Potylica nie jest omijana — jest standardem dla SSVEP.** Omijane jest co innego: **stawianie elektrody odniesienia blisko potylicy**. Powód jest udokumentowany i **nie jest ślepą uliczką: przez sześćdziesiąt lat nikt nie musiał tego pytania zadawać**, bo każdy miał dość elektrod, żeby problem zniknął obliczeniowo.

**Ale jedna zła wiadomość jest i jest konkretna:** okolica podpotyliczna, w której musiałaby leżeć elektroda odniesienia modułu, **nie jest elektrycznie cicha**. Ma trzech nazwanych mieszkańców i jeden z nich reaguje na bodziec wzrokowy.

---

## 1. Powód pierwszy: problem odniesienia jest w tej dziedzinie rozwiązywany **obliczeniowo**, a nie przez umiejscowienie

`[fakt, abstrakt odczytany]` **Yao D., Qin Y., Hu S., Dong L., Bringas Vega M.L., Valdés Sosa P.A.** — *„Which Reference Should We Use for EEG and ERP practice?"*, **Brain Topography 32(4):530–549, 2019, PMID 31037477**. Przeglądowa praca autorstwa twórcy techniki REST.

> „Which reference is appropriate for the scalp ERP and EEG studies? **This unsettled problem still inspires unceasing debate.** The ideal reference should be the one with zero or constant potential but unfortunately **it is well known that no point on the body fulfills this condition.** Consequently, **more than ten references are used** in the present EEG-ERP studies. **This diversity seriously undermines the reproducibility and comparability of results across laboratories.**"

Autorzy dzielą stosowane odniesienia na dwie klasy:

| Klasa | Przykłady | **Czego wymaga** |
|---|---|---|
| jednobiegunowe, budujące odniesienie neutralne | **REST**, **średnia po elektrodach (AR)**, połączone wyrostki sutkowate | **wielu elektrod pokrywających głowę** |
| niejednobiegunowe | **montaż dwubiegunowy**, **laplasjan** | dwóch albo czterech sąsiadów |

`[fakt]` Wymaganie gęstości jest w literaturze postawione wprost: **PMID 26305167**, *„Estimating a neutral reference for electroencephalographic recordings: **the importance of using a high-density montage** and a realistic head model"*.

`[wniosek]` **To jest sedno odpowiedzi.** Dziedzina rozwiązała problem odniesienia **przekształceniem po fakcie**: rejestruje się 32–128 kanałów wobec dowolnego odniesienia, a potem przelicza na REST albo średnią. Przy takim postępowaniu **fizyczne umiejscowienie odniesienia przestaje mieć znaczenie** — bo i tak zostanie zastąpione.

**Ale wszystkie te przekształcenia wymagają elektrod, których moduł potyliczny nie ma.** Przy dwóch albo trzech kanałach REST nie działa, średnia po elektrodach nie istnieje, połączone sutkowate wymagają dwóch przewodów za uszy. **Zostaje to, co fizycznie postawimy — i pytanie, które dziedzina odsunęła obliczeniowo, wraca jako pytanie konstrukcyjne.**

## 2. Powód drugi: dziedzina powiedziała wprost, że tego nie bada — dwadzieścia lat temu

`[fakt, abstrakt odczytany]` **Choi S.H., Lee M., Wang Y., Hong B.** (Kyungpook National University), *„Estimation of optimal location of EEG reference electrode for motor imagery based BCI using fMRI"*, **EMBC 2006, PMID 17946448**:

> „it is important to determine suitable locations for the EEG electrodes according to brain activity **as well as the location of reference electrode of the EEG, while most of conventional studies do not much consider about the location of the reference electrode.**"

Wynik: dla wyobrażenia ruchu najlepszym odniesieniem okazała się **dodatkowa okolica ruchowa (SMA)**, wybrana na podstawie fMRI, i poprawiła działanie interfejsu.

`[wniosek]` **Pytanie zostało zadane raz, dla innego paradygmatu, w 2006 roku, i nikt go nie powtórzył dla SSVEP.** Zdanie „most conventional studies do not much consider about the location of the reference electrode" jest **cytowalnym potwierdzeniem luki, wypowiedzianym przez kogoś innego** — i jest lepsze niż jakiekolwiek własne „nie znalazłem".

## 3. Powód trzeci: gdy odniesienie jest blisko, to nie jest już „odniesienie" tylko drugi kanał czynny

`[fakt, abstrakt odczytany]` **Joyce C., Rossion B.**, *„The face-sensitive N170 and VPP components manifest the same brain processes: the effect of reference electrode site"*, **Clin Neurophysiol 116(11):2613–2631, 2005, PMID 16214404**. Ten sam sygnał, przeliczony na pięć różnych odniesień, daje **dwa różne »komponenty« o odwrotnych amplitudach** — N170 i VPP okazują się tym samym zjawiskiem widzianym przez dwa odniesienia.

`[wniosek]` Elektrofizjologia wie od dawna, że **położenie odniesienia zmienia mierzony sygnał pierwszorzędowo, a nie o kilka procent.** Dlatego standardem zostały miejsca możliwie „obojętne" — płatek ucha i wyrostek sutkowaty, czyli **nad kością, daleko od mięśni i poza obszarem czynnym**. Nie dlatego, że ktoś zmierzył, o ile są lepsze od bliższych. Dlatego, że są **bezpieczne**, a skoro przewód i tak biegnie do czepka, nic nie kosztują.

**Nic nie kosztują dopiero wtedy, gdy urządzenie ma czepek.** W module noszonym kosztują całą formę urządzenia — i to jest jedyny powód, dla którego ktokolwiek musi to pytanie zadać.

---

## 4. Zła wiadomość, i jest konkretna: okolica podpotyliczna nie jest cicha

Sprawdziłem, co fizycznie leży pod skórą tam, gdzie musiałaby usiąść elektroda odniesienia modułu. **Trzech mieszkańców, każdy z nazwanym źródłem.**

### 4.1 Mięśnie karku

`[fakt]` **Goncharova I.I., McFarland D.J., Vaughan T.M., Wolpaw J.R.**, *„EMG contamination of EEG: spectral and topographical characteristics"*, **Clin Neurophysiol 114(9):1580–1593, 2003, PMID 12948787**, 25 osób, 64 elektrody:

> „**While EMG contamination is greatest at the periphery of the scalp near the active muscles**, even weak contractions can produce EMG that **obscures or mimics EEG alpha, mu, or beta rhythms over the entire scalp.**"
> „EMG spectra often have **peaks in the beta frequency range that resemble EEG beta peaks.**"

`[wniosek]` Grzbiet podpotyliczny **jest** obrzeżem czaszki i **jest** blisko mięśnia. To dokładnie ten opis.

### 4.2 Móżdżek — i to jest znalezisko, którego się nie spodziewałem

`[fakt, abstrakt odczytany]` **Todd N.P.M., Govender S., Colebatch J.G.**, *„The human electrocerebellogram (ECeG) recorded non-invasively using scalp electrodes"*, **Neurosci Lett 682:124–131, 2018, PMID 29886131**.

Elektrody nad tylnym dołem czaszki (położenie **CB1/CB2, około 5% poniżej i przyśrodkowo od PO9/PO10** układu 10-10) rejestrują aktywność móżdżku. To jest **dokładnie okolica, w której siedziałoby odniesienie modułu**. I dalej:

> „We also found that **visual stimulation, in the form of visual motion in particular, was effective in increasing the high-frequency power in CB electrodes, including in beta (14–30 Hz) and gamma**, compared with electrodes over the occipital and frontal cortex."

`[wniosek]` **To jest najpoważniejsza pojedyncza zła wiadomość, jaką ten projekt dostał od czasu pracy Li i in. 2025.** Elektroda odniesienia postawiona poniżej inionu może **sama nieść sygnał reagujący na bodziec wzrokowy**, w paśmie beta — czyli tam, gdzie leżą **drugie harmoniczne SSVEP**. W montażu różnicowym taki sygnał **odejmuje się od sygnału użytecznego**, i to w sposób zależny od częstotliwości.

**Czego to nie znaczy:** ECeG mierzono przy **ruchu wzrokowym**, przy sześciu osobach, w pozycji leżącej, w pasmach głównie powyżej 80 Hz. Przeniesienie na migotanie 8–18 Hz jest `[domysł]`, nie fakt. **Ale przesłanka jest na tyle konkretna, że nie wolno jej pominąć.**

### 4.3 Samo pole SSVEP

Zmierzone i opisane w `14_REANALIZA.md` §5: różnicowanie dwóch elektrod nad korą wzrokową kasuje potencjał wywołany razem z zakłóceniem, bo pole jest rozległe i gładkie.

---

## 5. Test rozstrzygający dwa mechanizmy — wykonany dzisiaj, wynik połowiczny

`[wniosek]` Mechanizmy z §4.2 i §4.3 dają **różne przewidywania**, więc dają się rozdzielić pomiarem:

- **gładkie pole** kasuje podstawową i harmoniczne **podobnie** → strata mniej więcej niezależna od częstotliwości
- **zanieczyszczenie odniesienia sygnałem wzrokowym z móżdżku** siedzi w paśmie beta → strata **wyraźnie większa dla drugiej harmonicznej** niż dla podstawowej

Policzyłem SNR w prążku bodźca i w prążku drugiej harmonicznej, dla montaży z odniesieniem odległym i zwartych, na danych Kołodzieja. Kod: `analiza/harmoniczne.py`.

| Montaż | SNR przy f₀ [dB] | SNR przy 2f₀ [dB] |
|---|---|---|
| odniesienie odległe, Oz sam | **6,93** | 0,11 |
| odniesienie odległe, średnia trzech kanałów | **7,48** | −0,04 |
| zwarty O1−Oz | 3,93 | −0,03 |
| zwarty O2−Oz | 4,75 | 0,12 |
| zwarty laplasjan | 4,01 | −0,03 |

**Strata montażu zwartego wobec odniesienia odległego:**

| Montaż | strata przy f₀ | strata przy 2f₀ |
|---|---|---|
| zwarty O1−Oz | **−3,55 dB** | 0,01 dB |
| zwarty O2−Oz | **−2,73 dB** | 0,16 dB |
| zwarty laplasjan | **−3,47 dB** | 0,01 dB |

### 5.1 Co ten test dał, a czego nie dał — mówię wprost

**Dał liczbę, której projekt nie miał:** `[fakt, pomiar własny]` **montaż zwarty kosztuje 2,7–3,6 dB stosunku sygnału do szumu w prążku bodźca.** To jest wielkość fizyczna, niezależna od klasyfikatora, i dokłada się do znanych już strat dokładności (9,3–24,5 pp) i przepustowości (41% szczytowego ITR).

**Nie rozstrzygnął mechanizmu, i powód jest banalny: w tym zbiorze nie ma czego mierzyć przy drugiej harmonicznej.** SNR przy 2f₀ wynosi **−0,04 do +0,16 dB we wszystkich montażach naraz**, czyli harmonicznej praktycznie nie ma nawet przy odniesieniu odległym. **Nie można stracić czegoś, czego nie było.** Test jest ograniczony podłogą, nie rozstrzyga i **nie wolno go raportować jako dowodu, że mechanizm móżdżkowy nie działa.**

`[wniosek]` Przyczyna jest zresztą znana i zapisana: Kołodziej użył **7, 8 i 9 Hz**, czyli harmoniczne wypadają na 14–18 Hz, a `15_PROJEKT.md` §2.4 odrzucił to pasmo jako złe. **Ten test właśnie potwierdził tę decyzję z zupełnie innej strony niż pierwotny argument o rytmie alfa.**

### 5.2 Co z tego wchodzi do planu pomiarowego

Zestaw częstotliwości z `16_PLAN_EKSPERYMENTALNY.md` §3.2 — **8,0 do 17,8 Hz z krokiem 1,4 Hz** — daje drugie harmoniczne w paśmie **16,0–35,6 Hz**, czyli w beta i na granicy gamma. **To jest dokładnie pasmo, w którym ECeG reaguje na bodziec wzrokowy.** Dobór zrobiony pod kolizje harmonicznych okazuje się przypadkowo trafiony także pod ten test.

**Nowa pozycja planu, koszt zerowy:** przy każdej sesji raportować **SNR osobno dla podstawowej i dla drugiej harmonicznej, dla każdego położenia odniesienia.** To zamienia ryzyko z §4.2 w **wynik** — niezależnie od tego, w którą stronę wypadnie:

- **strata rośnie z harmoniczną** → mechanizm to zanieczyszczenie odniesienia; wniosek konstrukcyjny: odniesienie musi wyjść ponad ionion, nie pod niego
- **strata niezależna od częstotliwości** → mechanizm to gładkie pole; wniosek: liczy się odległość, nie kierunek
- **oba** → rozkład na dwie składowe i to jest najciekawszy z możliwych wyników

`[wniosek]` **To jest test mechanizmu w rozumieniu arkusza ISEF** (`ISEF_ARKUSZE_OCENY.md`, `Execution`: *„tested in multiple conditions/trials"*, oraz rzemiosło z ENBM074: test rozdzielający, nie tylko test wyniku). Kosztuje jedną kolumnę w tabeli.

---

## 6. Bilans: czy to zła wiadomość

**Dla wiedzy o polu — dobra.** Pytanie „dlaczego nikt tego nie mierzy" miało trzy możliwe odpowiedzi: (a) bo to ślepa uliczka, (b) bo odpowiedź jest znana skądinąd, (c) bo nikt nie musiał. **Odpowiedź to (c), z dokumentacją:** dziedzina rozwiązała problem odniesienia obliczeniowo, a to wymaga wielu elektrod. Przy dwóch kanałach rozwiązanie nie działa i pytanie wraca.

**Dla projektu — mieszana, i trzeba to zapisać uczciwie:**

| | |
|---|---|
| **na plus** | luka potwierdzona **cudzym zdaniem** (Choi 2006), a nie własnym przeszukaniem; problem nazwany **„unsettled"** w przeglądzie z 2019; własna nowa liczba: **2,7–3,6 dB** |
| **na minus** | **okolica podpotyliczna ma trzech mieszkańców**, w tym jednego reagującego na bodziec wzrokowy w paśmie harmonicznych. Ryzyko, że najlepsze osiągalne odniesienie „w module" okaże się **istotnie gorsze, niż zakłada drabinka**, jest realne |
| **na plus mimo minusa** | to ryzyko **jest zmierzalne tym samym stanowiskiem**, bez dodatkowego sprzętu, i zamienia się w wynik niezależnie od znaku |

**Czego to nie zmienia:** twierdzenia, pytania, planu ani budżetu. Zgodnie z ustaleniem — nie ruszam.

**Co dopisuję do ryzyk:** nowe **R12**.

---

## 7. R12 — odniesienie w module siedzi nad móżdżkiem i nad mięśniem karku

| | |
|---|---|
| **prawdopodobieństwo, że wpływa mierzalnie** | `[domysł]` **40–60%** — trzy niezależne przesłanki (EMG karku, ECeG, gładkie pole), żadna zmierzona dla tej konfiguracji |
| **sterowalność** | **średnia** — położenie odniesienia jest zmienną projektu, więc odpowiedzią na złą wiadomość jest przesunięcie elektrody, a nie porzucenie pytania |
| **koszt porażki** | **niski dla twierdzenia, średni dla formy urządzenia.** Twierdzenie brzmi „wyznaczam najmniejszą odległość, przy której przepustowość się nie załamuje" — jeżeli ta odległość wypadnie **powyżej inionu albo za uchem**, to jest **wynik**, a nie porażka. Traci się na tym gabaryt, nie pomiar |
| **kiedy się rozstrzyga** | pierwsza własna sesja z pełnym zestawem odniesień, **wiosna 2027** |

**Plan awaryjny:** decyzja 6 (`DECYZJE.md`) dopuszcza już wyprowadzenie odniesienia cienkim przewodem na wyrostek sutkowaty. `[wniosek]` Jeżeli R12 się ziści, **projekt ma gotową odpowiedź konstrukcyjną i nie traci ani twierdzenia, ani demonstracji** — zmienia się jedno położenie elektrody i jedno zdanie o gabarycie.

---

## 8. Zadania

| # | Zadanie | Termin |
|---|---|---|
| **P23** | **raportować SNR osobno dla f₀ i 2f₀** przy każdym położeniu odniesienia — test rozdzielający mechanizmy (§5.2). Koszt: jedna kolumna | do planu pomiarowego |
| **P24** | **R12 wpisane do `17_RYZYKA.md`**; przy pierwszej sesji sprawdzić, czy elektroda odniesienia poniżej inionu wykazuje odpowiedź na bodziec | wiosna 2027 |
| **P25** | do sekcji o stanie wiedzy: **cytat Choi 2006** („most conventional studies do not much consider…") i **Yao 2019** („unsettled problem (…) more than ten references are used") — to jest uzasadnienie luki cudzą ręką, mocniejsze niż własne przeszukanie | z P12 |
