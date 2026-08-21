# ⏱️ Daily Taktgeber 🎲

Ein leichtgewichtiges, webbasiertes Tool für agile Teams, um Daily Stand-up Meetings fair, strukturiert und in der vorgegebenen Zeit durchzuführen. Der Taktgeber mischt die Reihenfolge der Teilnehmer zufällig und teilt die zur Verfügung stehende Gesamtzeit automatisch gerecht auf.

Da das Tool ohne Backend auskommt und Daten nur lokal speichert, ist es besonders schnell und datenschutzfreundlich.

## ✨ Features

- **Zufallsgenerator:** Bestimmt jeden Tag eine neue, faire Reihenfolge der Teammitglieder.
- **Abwesenheits-Checkliste:** Mit einem Klick können fehlende Teilnehmer (Urlaub/Krankheit) für das aktuelle Daily abgewählt werden.
- **Smart Timer:** Berechnet die Zeit pro Person automatisch (z.B. 15 Minuten Gesamtzeit / 5 aktive Personen = 3 Minuten pro Person).
- **Acht Anzeigemodi:** Klassische Liste, animierte Slotmaschine, Roadtrip-Ansicht mit E-Auto, das bunte Glücksrad, das Kartenspiel, die Abfahrtstafel, der Linienplan oder die ruhige Fokus-Ansicht (siehe unten).
- **Visuelles Feedback:** Der Timer ändert seine Farbe bei nahendem Zeitende (Gelb &rarr; Orange &rarr; Rot) und zeigt bei Überziehung einen Overtime-Indikator an.
- **Freie Farbwahl:** Die gesamte Oberfläche wird aus **einem** Grundton berechnet. Neben dem klassischen Blau stehen vier Voreinstellungen (Waldgrün, Terrakotta, Pflaume, Petrol) und ein Farbwähler für jede beliebige Farbe bereit — Flächen, Verläufe, Ränder und Schatten passen sich automatisch an.
- **Barrierefrei bedienbar:** Bildschirmleser bekommen jeden Sprecherwechsel angesagt, die Dialoge lassen sich mit Tabulator und **Esc** bedienen, und wer im Betriebssystem reduzierte Bewegung eingestellt hat, sieht die Ergebnisse ohne Dreh- und Flug-Animationen.
- **Zweisprachig:** Die komplette Oberfläche ist auf Deutsch und Englisch verfügbar — umschaltbar in den Einstellungen, live und ohne Neuladen.
- **Saisonale Events:** Rund ums Jahr bekommen alle Ansichten automatisch ein passendes Thema – im Februar (Karneval 🎉), im April (Ostern 🥚), im Oktober (Halloween 🎃) und im Dezember (Winter ❄️).
- **Touch-tauglich:** Ein „Nächster Teilnehmer“-Button ersetzt die Leertaste auf Geräten ohne Tastatur.
- **Konfetti:** Wenn alle durch sind, wird das Daily mit grünem Haken und Konfettiregen beendet. 🎉
- **Installierbar & Offline (PWA):** Der Taktgeber ist eine Progressive Web App. Über den **„App installieren"**-Button in den Einstellungen (erscheint, sobald der Browser die Installation anbietet) landet das Tool als eigene App auf dem Homescreen und läuft danach auch ohne Internet. Neue Versionen werden im Hintergrund gefunden und über ein dezentes **„Neu laden"**-Banner angeboten – ohne das laufende Daily zu unterbrechen.
- **Privacy by Design:** Es gibt kein Backend. Die Team-Stammdaten und Einstellungen werden ausschließlich lokal in deinem Browser (`Local Storage`) gespeichert.
- **Tastatursteuerung:** Bequeme Navigation durch das Meeting ganz ohne Maus.

## 🖥️ Anzeigemodi

In den Einstellungen wählst du zwischen acht Darstellungen:

- **Klassische Ansicht:** Die gewürfelte Reihenfolge als Liste; wer dran ist, wird hervorgehoben.
- **Slotmaschinen-Ansicht:** Eine animierte Walze mit Hebel lost den nächsten Sprecher aus — inklusive Gewinner-Historie.
- **Roadtrip-Ansicht (E-Auto):** Ein graues Elektroauto fährt pro Sprecher die Strecke bis zur Zielflagge ab. Die Batterieanzeige (SoC) zeigt die verbleibende Redezeit; bei knapper Zeit erscheinen nacheinander Warnsymbole (Batterie gelb &rarr; Schildkröte gelb &rarr; Schildkröte rot). Ist die Batterie leer, bleibt das Auto stehen. Die Reihenfolge mit den nächsten Teilnehmern wird darunter angezeigt.
- **Glücksrad-Ansicht:** Ein buntes Rad mit allen Namen dreht sich und lost per Klick auf „Drehen" (oder Leertaste) nacheinander den nächsten Sprecher aus. Bereits gezogene Namen werden abgedunkelt, der Timer pro Person läuft wie gewohnt, und eine Gewinner-Historie zeigt die bisherige Reihenfolge.
- **Kartenspiel-Ansicht:** Für jeden Sprecher fliegt eine bunte Namenskarte auf den Stapel (per Klick auf „Nächste Karte" oder Leertaste); der Timer pro Person läuft wie in der klassischen Ansicht. Lange Namen werden automatisch verkleinert, sodass sie immer auf eine Zeile passen. Dazwischen tauchen Sonderkarten mit großen, gut erkennbaren Symbolen auf – „Aussetzen" schiebt die betroffene Person ans Ende der Runde, „+2", „+4" und „Wende" sind reine Show. Stilistisch an bekannte Kartenspiele angelehnt, aber bewusst eigenständig gestaltet (eigene Symbole/Farben, keine Marken).
- **Abfahrtstafel-Ansicht:** Eine Fallblatt-Anzeige wie am Bahnhof – Klappenschrift von der Kopfzeile bis zur Statusspalte. Pro Klick auf „Anzeige stellen" (oder Leertaste) klappert eine Zeile durch zufällige Zeichen und rastet auf dem nächsten Sprecher ein. Anders als bei der Slotmaschine bleibt die komplette Reihenfolge sichtbar: erledigte Zeilen sind abgedunkelt, die übrigen warten als leere Klappen. Die Tafel hat von Anfang an ihre volle Höhe und wächst beim Aufdecken nicht nach. Gelb ist der einzige Akzent und bedeutet genau eines: diese Person ist jetzt dran – während des Klapperns bleibt die Zeile grau, das Einrasten *ist* der Farbwechsel.
- **Linienplan-Ansicht:** Die gewürfelte Reihenfolge als Strecke. Jede Person ist eine Haltestelle, ganz unten liegt die Endstation. Der Zug fährt während der Redezeit von der aktuellen zur nächsten Haltestelle – die Position auf der Strecke zeigt damit gleichzeitig die Restzeit der Person und den Fortschritt des gesamten Dailys.
- **Fokus-Ansicht:** Bewusst ruhig und ohne Ablenkung: der Name des Sprechers groß, darunter eine Sanduhr, deren Sand in Echtzeit vom oberen in den unteren Kolben rieselt. Dazu dezent „3 von 8" und wer als Nächstes kommt. Bei Überziehung färbt sich der Sand rot.

## 🚀 Live Demo / Nutzung

Da das Projekt aus einer einzigen HTML-Datei besteht, kann es direkt im Browser ausgeführt werden.

👉 [Hier geht es zur Live-Version](https://etechnik3r.github.io/daily-shuffler/daily_timer.html)

## ⚙️ Einstellungen (Konfiguration)

Klicke im Tool auf **Einstellungen**, um deine Stammdaten anzupassen:

- **Sprache:** Deutsch oder Englisch.
- **Daily-Dauer:** Gib die Gesamtzeit deines Meetings in Minuten an (Standard: 15).
- **Team-Mitglieder:** Trage die Namen deines Teams ein, getrennt durch Kommas, Semikolons oder Zeilenumbrüche. Leerzeichen trennen *nicht*, mehrteilige Namen wie „Anna Maria“ bleiben also eine Person. Das Eingabefeld zeigt ein ganzes Team ohne Scrollen und lässt sich bei Bedarf nach unten aufziehen.
- **Erstes Mitglied der Liste kommt zum Schluss:** Ist diese Option aktiv, wird der zuerst eingetragene Name erst in den letzten 20 % der Reihenfolge gezogen – praktisch für alle, die das Daily abschließen (Moderation, Scrum Master). Die Regel gilt in allen Ansichten; bei kleinen Teams ist es schlicht der letzte Platz. Fehlt die Person heute, läuft die Runde ganz normal.
- **Farbthema:** Klassisch (Blau), Waldgrün, Terrakotta, Pflaume, Petrol — oder eine eigene Farbe über den Farbwähler. Aus der Wahl werden Farbton und Sättigung übernommen; die Helligkeitsabstufungen für Flächen, Text, Ränder und Schatten erzeugt die App selbst, sodass jede Farbe lesbar bleibt. Bewusst *nicht* eingefärbt werden die Glücksrad-Segmente, die Spielkarten, die saisonalen Verzierungen und die Warnsymbole des E-Autos — die sind absichtlich bunt bzw. tragen eine feste Bedeutung (Rot = Zeit vorbei).
- **Anzeigemodus:** Klassisch, Slotmaschine, Roadtrip (E-Auto), Glücksrad, Kartenspiel, Abfahrtstafel, Linienplan oder Fokus.
- **Entwickler-Optionen** (ausklappbar): Saison-Override zum Testen der Karneval-, Oster-, Halloween- und Winter-Themes unabhängig vom Systemdatum sowie ein Schnelltest-Button, der den laufenden Timer auf 3 Sekunden setzt.

Diese Daten bleiben für deinen nächsten Besuch im Browser gespeichert.

## ⌨️ Tastenkürzel

Sobald das Daily gestartet wurde (Klick auf *„Würfeln“*), kannst du das Tool bequem mit der Tastatur bedienen:

- <kbd>Leertaste</kbd> (`Space`): Springt zum nächsten Teammitglied und setzt den Timer zurück.
- <kbd>Shift</kbd> + <kbd>Leertaste</kbd> (oder <kbd>Strg</kbd> + <kbd>Leertaste</kbd>): Springt zum vorherigen Teammitglied (Rückgängig-Funktion).
- <kbd>Esc</kbd>: Schließt Einstellungen und Anleitung.

Liegt der Fokus auf einer Schaltfläche, löst die Leertaste diese Schaltfläche aus — die Kürzel greifen also nur, wenn nichts anderes im Weg steht.
