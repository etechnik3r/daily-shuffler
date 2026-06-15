# ⏱️ Daily Taktgeber 🎲

Ein leichtgewichtiges, webbasiertes Tool für agile Teams, um Daily Stand-up Meetings fair, strukturiert und in der vorgegebenen Zeit durchzuführen. Der Taktgeber mischt die Reihenfolge der Teilnehmer zufällig und teilt die zur Verfügung stehende Gesamtzeit automatisch gerecht auf.

Da das Tool ohne Backend auskommt und Daten nur lokal speichert, ist es besonders schnell und datenschutzfreundlich.

## ✨ Features

- **Zufallsgenerator:** Bestimmt jeden Tag eine neue, faire Reihenfolge der Teammitglieder.
- **Abwesenheits-Checkliste:** Mit einem Klick können fehlende Teilnehmer (Urlaub/Krankheit) für das aktuelle Daily abgewählt werden.
- **Smart Timer:** Berechnet die Zeit pro Person automatisch (z.B. 15 Minuten Gesamtzeit / 5 aktive Personen = 3 Minuten pro Person).
- **Fünf Anzeigemodi:** Klassische Liste, animierte Slotmaschine, Roadtrip-Ansicht mit E-Auto, das bunte Glücksrad oder das Kartenspiel (siehe unten).
- **Visuelles Feedback:** Der Timer ändert seine Farbe bei nahendem Zeitende (Gelb &rarr; Orange &rarr; Rot) und zeigt bei Überziehung einen Overtime-Indikator an.
- **Zweisprachig:** Die komplette Oberfläche ist auf Deutsch und Englisch verfügbar — umschaltbar in den Einstellungen, live und ohne Neuladen.
- **Saisonale Events:** Im Oktober (Halloween 🎃) und Dezember (Winter ❄️) bekommen alle Ansichten automatisch ein passendes Thema.
- **Touch-tauglich:** Ein „Nächster Teilnehmer“-Button ersetzt die Leertaste auf Geräten ohne Tastatur.
- **Konfetti:** Wenn alle durch sind, wird das Daily mit grünem Haken und Konfettiregen beendet. 🎉
- **Privacy by Design:** Es gibt kein Backend. Die Team-Stammdaten und Einstellungen werden ausschließlich lokal in deinem Browser (`Local Storage`) gespeichert.
- **Tastatursteuerung:** Bequeme Navigation durch das Meeting ganz ohne Maus.

## 🖥️ Anzeigemodi

In den Einstellungen wählst du zwischen fünf Darstellungen:

- **Klassische Ansicht:** Die gewürfelte Reihenfolge als Liste; wer dran ist, wird hervorgehoben.
- **Slotmaschinen-Ansicht:** Eine animierte Walze mit Hebel lost den nächsten Sprecher aus — inklusive Gewinner-Historie.
- **Roadtrip-Ansicht (E-Auto):** Ein graues VW-ID.3-Auto fährt pro Sprecher die Strecke bis zur Zielflagge ab. Die Batterieanzeige (SoC) zeigt die verbleibende Redezeit; bei knapper Zeit erscheinen nacheinander Warnsymbole (Batterie gelb &rarr; Schildkröte gelb &rarr; Schildkröte rot). Ist die Batterie leer, bleibt das Auto stehen. Die Reihenfolge mit den nächsten Teilnehmern wird darunter angezeigt.
- **Glücksrad-Ansicht:** Ein buntes Rad mit allen Namen dreht sich und lost per Klick auf „Drehen" (oder Leertaste) nacheinander den nächsten Sprecher aus. Bereits gezogene Namen werden abgedunkelt, der Timer pro Person läuft wie gewohnt, und eine Gewinner-Historie zeigt die bisherige Reihenfolge.
- **Kartenspiel-Ansicht:** Für jeden Sprecher fliegt eine bunte Namenskarte auf den Stapel (per Klick auf „Nächste Karte" oder Leertaste); der Timer pro Person läuft wie in der klassischen Ansicht. Dazwischen tauchen Sonderkarten auf – „Aussetzen" schiebt die betroffene Person ans Ende der Runde, „+2", „+4" und „Wende" sind reine Show. Stilistisch an bekannte Kartenspiele angelehnt, aber bewusst eigenständig gestaltet (eigene Symbole/Farben, keine Marken).

## 🚀 Live Demo / Nutzung

Da das Projekt aus einer einzigen HTML-Datei besteht, kann es direkt im Browser ausgeführt werden.

👉 [Hier geht es zur Live-Version](https://etechnik3r.github.io/daily-shuffler/daily_timer.html)

## ⚙️ Einstellungen (Konfiguration)

Klicke im Tool auf **Einstellungen**, um deine Stammdaten anzupassen:

- **Sprache:** Deutsch oder Englisch.
- **Daily-Dauer:** Gib die Gesamtzeit deines Meetings in Minuten an (Standard: 15).
- **Team-Mitglieder:** Trage die Namen deines Teams ein (getrennt durch Kommas oder Zeilenumbrüche).
- **Anzeigemodus:** Klassisch, Slotmaschine, Roadtrip (E-Auto), Glücksrad oder Kartenspiel.
- **Entwickler-Optionen** (ausklappbar): Saison-Override zum Testen der Halloween-/Winter-Themes unabhängig vom Systemdatum sowie ein Schnelltest-Button, der den laufenden Timer auf 3 Sekunden setzt.

Diese Daten bleiben für deinen nächsten Besuch im Browser gespeichert.

## ⌨️ Tastenkürzel

Sobald das Daily gestartet wurde (Klick auf *„Würfeln“*), kannst du das Tool bequem mit der Tastatur bedienen:

- <kbd>Leertaste</kbd> (`Space`): Springt zum nächsten Teammitglied und setzt den Timer zurück.
- <kbd>Shift</kbd> + <kbd>Leertaste</kbd> (oder <kbd>Strg</kbd> + <kbd>Leertaste</kbd>): Springt zum vorherigen Teammitglied (Rückgängig-Funktion).
