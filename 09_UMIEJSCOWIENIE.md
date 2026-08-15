# 09 — Gdzie ma być interfejs

**Status: decyzja otwarta.** Do 15 VIII 2026 była zamknięta bez postawienia pytania — patrz `KOREKTY.md` K-019.

Ten plik istnieje, bo forma „za uchem, wielkości aparatu słuchowego" była traktowana jak ograniczenie wejściowe, a jest jedną z możliwych odpowiedzi na rzeczywiste wymaganie. Rzeczywiste wymaganie brzmi: **niewidoczne albo nierozpoznawalne jako sprzęt, wygodne do noszenia, zero hełmów.**

---

## 1. Dlaczego to pytanie jest ważniejsze niż wyglądało

Miejsce elektrody decyduje o tym, jaki sygnał w ogóle istnieje. Wzmacniacz i algorytm mogą wycisnąć to, co dotarło; nie mogą wytworzyć tego, czego nie ma.

**Kluczowa obserwacja, która wychodzi dopiero po zestawieniu liczb z `06_TABELA_PARAMETROW.md`:**

Najlepszy paradygmat sterowania dyskretnego pod względem przepustowości to **SSVEP**. Jego generator leży w korze wzrokowej, czyli **na potylicy**. Obecne założenie umieszcza elektrody **maksymalnie daleko od tego źródła** — po przeciwnej stronie głowy.

| Gdzie | ITR dla SSVEP |
|---|---|
| potylica (Oz/O1/O2) | **~70–92 bit/min** |
| skroń (T7/T8) | 6,4 bit/min |
| ucho, online | 11–16,6 bit/min |

`[wniosek, streszczenie]`. **Różnica pięcio- do piętnastokrotna jest w całości kosztem umiejscowienia**, nie jakości wykonania. To nie jest strata, którą odrabia się lepszym torem analogowym.

**Wniosek [wniosek]:** w wersji zausznej projekt z góry oddaje rząd wielkości wydajności, żeby spełnić wymaganie estetyczne. To może być świadomy wybór — ale musi być wyborem, a nie skutkiem ubocznym.

---

## 2. Porównanie miejsc

Skala widoczności wg `06_TABELA_PARAMETROW.md` sekcja 4: **0** = niewidoczne z 2 m, **1** = widoczne, ale nierozpoznawalne jako sprzęt, **3–4** = rozpoznawalny sprzęt na głowie.

| Miejsce | Jaki sygnał dostępny | Widoczność | Mocowanie | Włosy | Główne zakłócenie |
|---|---|---|---|---|---|
| **kanał słuchowy** (in-ear) | alfa pewnie; słuchowe niepewnie; SSVEP słabo; ruch marginalnie | **0–1** | **bardzo dobre** — kanał trzyma wkładkę | brak | żwacz i mięsień skroniowy tuż obok; **artefakty szczękowe gorsze niż na skalpie** |
| **za uchem / wyrostek sutkowaty** | jak wyżej, nieco większy rozstaw elektrod | **1** | **bardzo dobre** — małżowina jako zaczep. Dlatego tam żyją aparaty słuchowe | minimalne | mięsień skroniowy, mięśnie karku |
| **wokół małżowiny** (cEEGrid) | jw., 10 elektrod, sprawdzone w literaturze | **1** | dobre, ale na klej | minimalne | jw. |
| **potylica** (Oz/O1/O2) | **SSVEP maksymalny; alfa najsilniejsza na całej głowie** | **0, jeżeli włosy zakrywają**; 3 jeżeli nie | **trudne** — brak naturalnego zaczepu | **główna przeszkoda** dla elektrod suchych | mięśnie karku przy ruchach głowy |
| **kark, poniżej potylicy** | SSVEP słabszy niż z Oz, ale bliżej niż ucho | 0–1 przy krótkiej fryzurze | średnie | zależy od fryzury | mięśnie karku silniej |
| **czoło** (Fp1/Fp2) | frontalne i EOG; **do sterowania mało** | 1 w oprawkach, 3 samodzielnie | dobre | brak | mięśnie mimiczne, mruganie |
| **oprawki okularów** | czoło + skroń + zauszne | **1** — wygląda jak okulary | **bardzo dobre** | brak | jw. |
| **ciemię** (C3/Cz/C4) | wyobrażenie ruchu, sterowanie ciągłe | **4** — wymaga czapki | wymaga opaski lub czapki | tak | — |

---

## 3. Potylica — pełny rozbiór, bo to jest realna alternatywa

### 3.1 Co przemawia za

- **odzyskuje rząd wielkości ITR** dla SSVEP, patrz sekcja 1
- alfa potyliczna jest najsilniejszym rytmem, jaki EEG w ogóle rejestruje — czyli **rezerwa na paradygmat zapasowy**, gdyby SSVEP odpadł
- **może być bardziej niewidoczne niż zausznik, nie mniej.** Rzecz schowana pod włosami z tyłu głowy to stopień 0. Aparat słuchowy to stopień 1. Wymaganie „zero hełmów" nie mówi „przy uchu", tylko „nie ma być widać"
- większy dostępny rozstaw elektrod (O1–O2 to kilka centymetrów) → lepszy stosunek sygnału do szumu przy tym samym torze

### 3.2 Co przemawia przeciw

- **włosy.** To jest główny problem inżynierski. Elektrody suche przez włosy wymagają szpilek lub pazurków, docisku, i mają gorszy oraz mniej stabilny kontakt niż na skórze gołej. Impedancje, które mam zmierzone (4 kΩ mokra, ~450 kΩ sucha), dotyczą **kanału słuchowego, czyli skóry bez włosów** — dla owłosionej potylicy będzie gorzej `[wniosek]`
- **mocowanie.** Za uchem jest małżowina, w kanale jest sam kanał. Na potylicy nie ma się o co zaczepić. Zostaje: cienki łuk pod włosami z tyłu głowy, klej (tak trzyma się cEEGrid), albo wpięcie we włosy
- **mięśnie karku.** Zamiast szczęki dostajemy prostowniki karku. `[domysł, do sprawdzenia]` możliwe, że to zakłócenie jest **rzadsze**, bo mówi się i żuje stale, a kark napina się przy ruchach głowy — ale to jest domysł i wymaga pomiaru, nie założenia
- **SSVEP wymaga patrzenia na migający obiekt**, więc traci się argument „działa przy zamkniętych oczach" i wchodzi się w bezpośrednie porównanie z eye trackingiem

### 3.3 Wariant hybrydowy, który wygląda najciekawiej

`[domysł]` **Zausznik jako moduł elektroniki i elektroda odniesienia, cienki łuk pod włosami z tyłu głowy, elektrody czynne na potylicy.**

Dlaczego to się składa:
- wyrostek sutkowaty za uchem to **klasyczna pozycja elektrody odniesienia** w EEG — czyli i tak jej tam potrzebujemy
- małżowina daje zaczep mechaniczny dla całości i miejsce na baterię oraz płytkę
- łuk biegnie z tyłu głowy, **pod włosami**, nie przez czoło i nie przez czubek — to nie jest opaska w rozumieniu Muse
- rozstaw potylica ↔ wyrostek sutkowaty jest duży, więc amplituda różnicowa duża

To zachowuje mocne strony formy zausznej (mocowanie, elektronika, brak włosów pod referencją) i odzyskuje sygnał, którego przy uchu nie ma.

**Czego nie wiem i co decyduje, czy to działa:** czy przy fryzurze użytkownika łuk z tyłu głowy jest niewidoczny. To pytanie do użytkownika, nie do literatury.

---

## 4. Sprzężenie, którego wcześniej nie postawiłem

**Miejsce i oś projektu nie są niezależnymi decyzjami.** To jest najważniejsza rzecz w tym pliku.

| Umiejscowienie | Dominujące zakłócenie | Jaka oś projektu z tego wynika |
|---|---|---|
| ucho / zausznik | EMG szczęki i EOG, udokumentowane jako **gorsze niż na skalpie** (Kappel 2017) | **analogowa kompensacja artefaktów mięśniowo-ocznych** — obecny kandydat |
| potylica | kontakt elektrody przez włosy, artefakty ruchowe, stabilność mechaniczna | **elektroda sucha i mocowanie odporne na ruch** — też problem opisany jako otwarty w przeglądach 2025–2026 |
| wariant hybrydowy | oba, w różnych punktach | do wyboru — albo obie warstwy, jeżeli starczy czasu |

**Konsekwencja:** obecna oś projektu (kompensacja analogowa EMG/EOG) jest sensowna **dlatego, że urządzenie jest przy uchu**. Przeniesienie na potylicę nie unieważnia projektu, ale **wymaga wyprowadzenia osi od nowa** — nie da się jej przenieść mechanicznie, bo problem szczęki tam nie dominuje.

Obie osie mają pokrycie w literaturze jako problemy otwarte (`04_LUKI_ZAPISANE.md` sekcja 1.1: redukcja artefaktów ruchowych, sprzężenie mechaniczno-elektryczne, dobór materiałów). Żadna nie jest z góry lepsza.

---

## 5. Czego nie da się rozstrzygnąć bez użytkownika

1. **fryzura** — czy z tyłu głowy da się cokolwiek schować. Determinuje, czy potylica ma widoczność 0 czy 3
2. **czy urządzenie ma być jednym elementem**, czy może być rozłożone (zausznik + łuk)
3. **klej do skóry** — cEEGrid trzyma się na kleju i to jest sprawdzona droga; czy dopuszczalne na kilka godzin dziennie
4. **co jest ważniejsze, jeżeli się rozjadą:** absolutna niewidoczność czy wygoda przy wielogodzinnym noszeniu

Pytania 1–4 postawione użytkownikowi 15 VIII 2026.

---

## 6. Co zostaje niezależnie od wyboru miejsca

- **elektrody nad korą ruchową (C3/Cz/C4) pozostają wykluczone** — wymagają czapki, stopień widoczności 4. Ustalenie „odczyt dyskretny" trzyma się niezależnie od tego pliku
- **wymaganie bezpieczeństwa** z sekcji 12 handbooka: zasilanie bateryjne albo izolacja galwaniczna, niezależnie od umiejscowienia
- **twierdzenie pomiarowe zamiast twierdzenia o pierwszeństwie** — patrz `00_STRESZCZENIE.md` sekcja 1.1
</content>
