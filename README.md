# ⏱️ Daily Taktgeber 🎲

Ein leichtgewichtiges, webbasiertes Tool für agile Teams, um Daily Stand-up Meetings fair, strukturiert und in der vorgegebenen Zeit durchzuführen. Der Taktgeber mischt die Reihenfolge der Teilnehmer zufällig und teilt die zur Verfügung stehende Gesamtzeit automatisch gerecht auf.

Da das Tool ohne Backend auskommt und Daten nur lokal speichert, ist es besonders schnell und datenschutzfreundlich.

## ✨ Features

- **Zufallsgenerator:** Bestimmt jeden Tag eine neue, faire Reihenfolge der Teammitglieder.
- **Abwesenheits-Checkliste:** Mit einem Klick können fehlende Teilnehmer (Urlaub/Krankheit) für das aktuelle Daily abgewählt werden.
- **Smart Timer:** Berechnet die Zeit pro Person automatisch (z.B. 15 Minuten Gesamtzeit / 5 aktive Personen = 3 Minuten pro Person).
- **Visuelles Feedback:** Der Timer ändert seine Farbe bei nahendem Zeitende (Gelb &rarr; Orange &rarr; Rot) und zeigt bei Überziehung einen Overtime-Indikator (🤯/⏰) an.
- **Privacy by Design:** Es gibt kein Backend. Die Team-Stammdaten und Zeiteinstellungen werden ausschließlich lokal in deinem Browser (`Local Storage`) gespeichert.
- **Tastatursteuerung:** Bequeme Navigation durch das Meeting ganz ohne Maus.

## 🚀 Live Demo / Nutzung

Da das Projekt aus einer einzigen HTML-Datei besteht, kann es direkt im Browser ausgeführt werden.

👉 [Hier geht es zur Live-Version](https://etechnik3r.github.io/daily-shuffler/daily_timer.html)

## ⚙️ Einstellungen (Konfiguration)

Klicke im Tool auf **Einstellungen**, um deine Stammdaten anzupassen:

- **Daily-Dauer:** Gib die Gesamtzeit deines Meetings in Minuten an (Standard: 15).
- **Team-Mitglieder:** Trage die Namen deines Teams ein (getrennt durch Kommas oder Zeilenumbrüche).

Diese Daten bleiben für deinen nächsten Besuch im Browser gespeichert.

## ⌨️ Tastenkürzel

Sobald das Daily gestartet wurde (Klick auf *"Würfeln"*), kannst du das Tool bequem mit der Tastatur bedienen:

- <kbd>Leertaste</kbd> (`Space`): Springt zum nächsten Teammitglied und setzt den Timer zurück.
- <kbd>Shift</kbd> + <kbd>Leertaste</kbd> (oder <kbd>Strg</kbd> + <kbd>Leertaste</kbd>): Springt zum vorherigen Teammitglied (Rückgängig-Funktion).
