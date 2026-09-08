# Daily Taktgeber – Projektübersicht

Diese Datei beschreibt Idee, Aufbau und innere Struktur des Projekts. Sie
richtet sich an alle, die den **Daily Taktgeber** weiterentwickeln wollen –
Menschen wie auch KI-Werkzeuge, die sich schnell einen vollständigen Überblick
verschaffen müssen, ohne die gesamte Codebasis Zeile für Zeile zu lesen.

Kurzbeschreibung für Nutzer steht in der [README.md](README.md), die Historie
im [CHANGELOG.md](CHANGELOG.md).

---

## 1. Idee

Der Daily Taktgeber ist ein Werkzeug für agile Teams, um das tägliche Stand-up
(**Daily Stand-up**) fair, strukturiert und in der vorgegebenen Zeit
durchzuführen. Zwei Grundprobleme werden gelöst:

1. **Reihenfolge:** Wer redet wann? Der Taktgeber würfelt jeden Tag eine neue,
   zufällige Reihenfolge der anwesenden Teammitglieder.
2. **Zeit:** Die Gesamtdauer des Dailys wird gleichmäßig auf die aktiven
   Personen aufgeteilt (z. B. 15 min / 5 Personen = 3 min pro Person). Ein
   Timer zeigt die verbleibende Zeit an und warnt bei Überziehung.

Rund um diesen Kern gibt es mehrere **Anzeigemodi**, die denselben Ablauf
unterschiedlich inszenieren (nüchterne Liste bis animierte Slotmaschine),
zweisprachige Bedienung, frei wählbares Farbthema, optionale Sounds, saisonale
Verzierungen und Barrierefreiheit.

### Leitprinzipien

- **Kein Backend, keine Abhängigkeiten.** Die gesamte Anwendung ist **eine
  einzige HTML-Datei** (`daily_timer.html`) mit eingebettetem CSS und
  JavaScript. Kein Build-Schritt, kein Framework, keine externen Laufzeit-
  Bibliotheken. Öffnen im Browser genügt.
- **Datenschutz by Design.** Team-Stammdaten und Einstellungen liegen
  ausschließlich lokal im Browser (`localStorage`). Es werden keine Daten
  übertragen.
- **Offlinefähig (PWA).** Ein Service Worker cacht die App-Shell; nach dem
  ersten Laden funktioniert alles ohne Netz. Auch Sounds werden im Browser
  erzeugt (Web Audio), es werden keine Audiodateien geladen.
- **Aus einem Guss.** Die gesamte Oberfläche wird aus **einem** Grundton
  (Farbton + Sättigung) berechnet; Helligkeitsabstufungen erzeugt die App
  selbst, sodass jede Farbe lesbar bleibt.

---

## 2. Dateistruktur

```
daily-shuffler/
├── daily_timer.html        Die komplette Anwendung (HTML + CSS + JS in einer Datei)
├── sw.js                   Service Worker: Offline-Caching und Update-Banner
├── manifest.webmanifest    PWA-Manifest (Name, Icons, Farben, Anzeigemodus)
├── icons/                  App-Icons (192/512, maskable, Apple-Touch, Favicon)
├── social-preview.svg      Vorschaubild für Social-Media-/Repo-Karten
├── scripts/
│   └── generate_icons.py   Hilfsskript, das die PNG-Icons erzeugt
├── README.md               Nutzer-Dokumentation (Features, Bedienung)
├── PROJECT.md              Diese Datei (Architektur/Struktur)
├── CHANGELOG.md            Versionshistorie
└── LICENSE                 GNU GPL v3
```

Die einzige Datei, die den eigentlichen App-Code enthält, ist
`daily_timer.html`. Alles andere ist Beiwerk für PWA, Icons und Doku.

---

## 3. Aufbau von `daily_timer.html`

Die Datei ist in drei Abschnitte gegliedert: `<style>` (CSS), `<body>` (Markup)
und `<script>` (Logik). Innerhalb jedes Abschnitts trennen Kommentarbanner
(`/* --- ... --- */` bzw. `// --- ... ---`) klar benannte Bereiche.

### 3.1 CSS (`<style>`)

- **Design-Tokens (`:root`):** Eine einzige Quelle der Wahrheit für Flächen,
  Akzent, Tiefe und Spaltenbreite. Zentrale Variablen: `--brand-h` (Farbton),
  `--brand-sat` (Sättigungsfaktor) und `--col-width` (Standard-Spaltenbreite
  340 px). Nahezu alle Farben sind `hsl(var(--brand-h), calc(... * var(--brand-sat)), L%)`,
  sodass ein Themenwechsel nur zwei Variablen ändert.
- **UI-Komponenten:** Buttons, Teilnehmerauswahl, Timer-Pille, Teamliste.
- **Ansichts-CSS:** je ein Block pro Anzeigemodus (Slotmaschine, EV-Roadtrip,
  Glücksrad, Kartenspiel, Abfahrtstafel, Linienplan, Fokus).
- **Saisonale Themes:** Karneval, Ostern, Halloween, Winter – jeweils pro
  Ansicht ergänzt.
- **Modale Dialoge, PWA-Banner, Einstellungs-Overlay.**

### 3.2 Markup (`<body>`)

Ein gemeinsamer Kopf (Titel, Teilnehmerauswahl, Timer-Pille) und darunter **je
ein Container pro Ansicht**, gekennzeichnet mit `data-view="…"`. Sichtbar ist
immer nur genau einer; `showView(mode)` blendet den passenden ein und alle
anderen aus (gesteuert über das `data-view`-Attribut, nicht über handgepflegte
Einzel-Sichtbarkeiten). Dazu kommen die Modale (Einstellungen, Anleitung) und
die PWA-Banner.

Die Timer-Pille (`#timerContainer`) ist **global** und wird von allen Ansichten
gemeinsam genutzt; links und rechts sitzen zwei Symbol-Slots
(`#timerIconLeft` / `#timerIconRight`) für die Overtime-Anzeige.

### 3.3 Logik (`<script>`)

Der Code ist in Module gegliedert (jeweils durch `// --- Name ---` markiert):

| Modul | Aufgabe |
|-------|---------|
| **Configuration & Constants** | View-Mode-Konstanten, `localStorage`-Schlüssel, `SUPPORTED_LANGS`, Modus-Gruppen (`DRAW_ONE_BY_ONE_MODES`, `STEP_THROUGH_MODES`). |
| **Theme** | Grundton lesen/setzen, aus einer Farbe `--brand-h`/`--brand-sat` ableiten, persistieren. |
| **Accessibility & Motion** | `prefersReducedMotion()`, Sprecheransagen für Screenreader. |
| **i18n** | `translations` (de/en), `t(key, vars)` für Übersetzung + Platzhalter, Sprachumschaltung live ohne Neuladen. |
| **Application State** | Laufende Reihenfolge (`currentShuffledList`), `activeIndex`, `viewMode`, Timer-Werte, pro-Ansicht-Zustände. |
| **DOM Elements** | Zwischengespeicherte Referenzen auf die wichtigsten Knoten. |
| **Sound** | Alle Klänge werden per Web Audio erzeugt (keine Dateien). Ein Registry-Objekt hält pro Ansicht eigene Klänge; `playSound()` / `playSoundThrottled()`. Ab Werk aus. |
| **Timer** | `startTimer()`, `tick()`, `updateTimerDisplay()`. Setzt Farbstufen (20/15/10/5 s) und ruft die aktualisierenden View-Funktionen. Überziehung (`timeRemainingSeconds < 0`) schaltet den Overtime-Zustand. |
| **Core Logic** | `shuffle()` (Fisher-Yates), `pickNextParticipantIndex()` (u. a. „Erstes Mitglied zum Schluss“), Weiter/Zurück, `finishDaily()`, Konfetti. |
| **View-Module** | Je ein Modul pro Ansicht: `displayXxxTeam()` (aufbauen), `updateXxxView()` (pro Sekunde), `resetXxx()` (zurück zur Auswahl) plus ansichtsspezifische Animationen. |
| **Season** | `resolveSeasonEvent()` (Datum → Event, mit Entwickler-Override), `applySeason()`. |
| **Initialization** | `loadInitialConfig()`, Service-Worker-Registrierung, Event-Listener (u. a. Tastatursteuerung), Start beim `DOMContentLoaded`. |

---

## 4. Anzeigemodi (Views)

Jede Ansicht ist ein eigenes View-Modul mit gleichem Vertrag und wird über die
`VIEW_MODE_*`-Konstante identifiziert:

| Konstante | Ansicht | Kurzbeschreibung |
|-----------|---------|------------------|
| `classic` | Klassisch | Reihenfolge als Liste, aktuelle Person hervorgehoben. |
| `slot` | Slotmaschine | Animierte Walze mit Hebel, lost den nächsten Sprecher aus. |
| `ev` | Roadtrip (E-Auto) | E-Auto fährt die Strecke, Batterie = Redezeit, Schildkröte = knapp/vorbei. |
| `wheel` | Glücksrad | Buntes Rad dreht sich, per Klick wird gezogen. |
| `card` | Kartenspiel | Namenskarten fliegen auf den Stapel, mit Sonderkarten. |
| `flap` | Abfahrtstafel | Fallblatt-Tafel wie am Bahnhof; die ganze Reihenfolge bleibt sichtbar. |
| `line` | Linienplan | Reihenfolge als Strecke; der Zug fährt während der Redezeit zur nächsten Haltestelle. |
| `focus` | Fokus | Ruhig: großer Name plus ablaufende Sanduhr. |

Zwei Ablauf-Familien:

- **Schrittweise (`STEP_THROUGH_MODES`):** klassisch, EV, Linie, Fokus – die
  komplette Reihenfolge steht sofort, Weiter/Zurück bewegt den Fokus.
- **Einzeln aufdecken (`DRAW_ONE_BY_ONE_MODES`):** Slot, Glücksrad, Kartenspiel,
  Abfahrtstafel – die nächste Person wird pro Klick/Leertaste gezogen.

### Overtime-Signale

Läuft die Redezeit ab (`timeRemainingSeconds < 0`), zeigt jede Ansicht das auf
eigene Weise:

- **Timer-Pille:** Zwei Emojis neben der Uhr, pro Ansicht thematisch passend
  (siehe `OVERTIME_ICONS` in `toggleOvertimeIcons`). Die klassische Ansicht
  behält den explodierenden Kopf und den Wecker.
- **EV:** Statt der Emojis erscheint die Schildkröte im Auto-Bereich.
- **Abfahrtstafel:** Die Zeile der aktuellen Person schlägt von Gelb auf Rot um
  (`is-late`), die Statusspalte wechselt auf **„verspätet“**.
- **Fokus:** Der Sand färbt sich rot.

---

## 5. Zentrale Konzepte

- **Ein Grundton → ganze Oberfläche.** Farbwahl setzt nur `--brand-h` und
  `--brand-sat`; die Helligkeitsstufen stecken fest in den CSS-Regeln. Bewusst
  *nicht* eingefärbt: Glücksrad-Segmente, Spielkarten, saisonale Verzierungen
  und die Warnsymbole (Rot = Zeit vorbei), die eine feste Bedeutung tragen.
- **i18n.** `t('key')` liest aus `translations[currentLang]`; Platzhalter wie
  `{name}` werden über den zweiten Parameter ersetzt. Statische Texte tragen
  `data-i18n`-Attribute und werden beim Sprachwechsel neu gesetzt.
- **Persistenz.** Alles über `localStorage` mit eigenen Schlüsseln
  (View-Modus, Sprache, Theme, Sound, Stammdaten, Entwickler-Override). Jeder
  Zugriff ist in `try/catch` gekapselt, damit ein blockierter Speicher die App
  nicht lahmlegt.
- **Barrierefreiheit.** Sprecherwechsel werden angesagt; Dialoge sind per Tab
  und **Esc** bedienbar; bei „reduzierte Bewegung“ entfallen Animationen (die
  Ansichten prüfen `prefersReducedMotion()`).

---

## 6. PWA & Versionierung

- `manifest.webmanifest` beschreibt Name, Icons, Farben und Anzeigemodus.
- `sw.js` cacht die App-Shell (`CORE_ASSETS`) und liefert sie *cache-first*
  aus. Beim Aktivieren werden alte Caches gelöscht.
- **Versionierung:** Die Konstante `CACHE_VERSION` in `sw.js` ist die
  Release-Nummer. Sie zu erhöhen ändert die Bytes von `sw.js`, wodurch der
  Browser einen neuen Worker registriert und die App das
  „Neue Version verfügbar“-Banner zeigt. **Bei jeder Auslieferung
  `CACHE_VERSION` hochzählen und einen Eintrag im `CHANGELOG.md` ergänzen.**

---

## 7. Weiterentwicklung – typische Aufgaben

- **Neue Ansicht hinzufügen:** `VIEW_MODE_*`-Konstante ergänzen, in die
  Modus-Gruppen einsortieren, Container mit `data-view` im Markup anlegen,
  CSS-Block + View-Modul (`displayXxxTeam` / `updateXxxView` / `resetXxx`)
  schreiben, Radio-Button in den Einstellungen und i18n-Texte ergänzen, ggf.
  Sound und Overtime-Signal (inkl. Eintrag in `OVERTIME_ICONS`) hinzufügen.
- **Text/Sprache ändern:** In `translations` (de **und** en) anpassen; im
  Markup `data-i18n` verwenden.
- **Farben/Design:** Über die `--brand-*`-Tokens bzw. die ansichtsspezifischen
  CSS-Blöcke; feste Bedeutungsfarben (Rot = Überziehung) beibehalten.
- **Release:** `CACHE_VERSION` in `sw.js` erhöhen und `CHANGELOG.md` ergänzen.
