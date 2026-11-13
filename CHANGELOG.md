# Changelog

Alle nennenswerten Änderungen am **Daily Taktgeber** werden in dieser Datei
festgehalten.

Das Format orientiert sich an [Keep a Changelog](https://keepachangelog.com/de/1.0.0/).
Als Versionsnummer dient die `CACHE_VERSION` aus dem Service Worker
[`sw.js`](sw.js): Sie wird bei jeder Veröffentlichung erhöht, wechselt dadurch
den Cache-Namen und löst im laufenden Betrieb das „Neue Version verfügbar“-Banner
aus. **Merkregel:** Bei jeder Änderung, die ausgeliefert wird, `CACHE_VERSION`
hochzählen *und* hier einen Eintrag ergänzen.

## [v21] – 2026-11-13

### Geändert
- **Slotmaschine – alle Namen bleiben drauf:** Gezogene Namen verschwinden
  nicht mehr von den Walzen. Gegen Ende der Runde zeigt der Automat deshalb
  nicht mehr dreimal denselben Namen.
- **Slotmaschine – nur die Gewinnlinie ist lesbar:** Jede Walze bekommt für
  jede Drehung ihre eigene Zufallsfolge. Über und unter der Gewinnlinie
  stehen nur noch Bruchstücke verschiedener Namen; es wird geprüft, dass
  dort nie zufällig ein ganzer Name entsteht. Sehr kleine Teams (bis drei
  Personen) bekommen zusätzlich Symbolfelder (★, 7). Die Walzen starten
  genau mit dem Bild, das gerade zu sehen ist – kein Sprung beim Drehen.
- **Glücksrad – klassisch und größer:** Der Lampenring und der umlaufende
  Lichtstrahl nach dem Gewinn sind entfernt. Das Rad ist deutlich größer
  (bis 420 px). Es steht jetzt in Schrägprojektion auf einem Ständer: Die
  Raddicke ist als Kante nach hinten sichtbar (Chromlippen, lackierter
  Mantel), die Säule hat eine Seitenfläche, der Sockel Deck- und
  Seitenfläche mit Chromkanten und Bodenschatten. Der Zeiger sitzt auf
  einem Chrom-Halter, die Nabe hat ebenfalls Tiefe.

## [v20] – 2026-11-13

### Geändert
- **Slotmaschine – Name als ein Wort:** Statt den Namen in Silben zu
  zerschneiden (BA·STI·AN), liegt über allen drei Walzen ein gemeinsames
  Buchstabenraster mit gleichem Abstand. Jede Walze hat gleich viele Zellen,
  die Walzengrenzen fallen immer zwischen zwei Buchstaben und der Name steht
  zentriert – er liest sich als ein gleichmäßig gesetztes Wort. Die
  Schriftgröße richtet sich nach dem breitesten Buchstaben im Spiel.
- **Glücksrad – aufgewertet auf Automaten-Niveau:** Leuchtring im
  Markenfarbton mit Chromrand und 24 Glühbirnen, die dieselben
  Lichtprogramme wie die Slotmaschine fahren (Rasen beim Drehen,
  Jackpot-Blinken beim Gewinn). Die Scheibe sitzt in einer Chromfassung, die
  Segmente sind plastisch schattiert (hell an der Nabe, dunkler zum Rand),
  Chrom-Pins am Rand, Beschriftung mit leichtem Schatten. Darüber liegt eine
  feststehende Glaskuppel-Spiegelung, beim Gewinn läuft ein Lichtstrahl
  einmal herum und der Stern in der Chrom-Nabe glüht. Der Zeiger ist ein
  3D-Tropfen auf Chromlager, der von den Pins tatsächlich ausgelenkt wird und
  zurückschnappt. Dazu ein Standfuß. Bereits gezogene Segmente werden
  entsättigt statt durchsichtig. Saisonale Farben für Zeiger, Ring und Nabe.

## [v19] – 2026-11-13

### Geändert
- **Slotmaschine – drei Walzen statt einer:** Jeder Name wird in drei Teile
  zerlegt (z. B. BA·STI·AN), jede Walze trägt einen Teil. Die äußeren Walzen
  laufen nach unten, die mittlere nach oben; sie rasten nacheinander von links
  nach rechts ein, jede mit eigenem „Klonk“ und Aufleuchten ihres Teils – erst
  mit der dritten Walze steht der Name. In Ruhe zeigt die Gewinnlinie einen
  bunten Mix aus verschiedenen Namen.
- **Größere Buchstaben:** Die Schriftgröße wird automatisch an den längsten
  Namensteil angepasst (bis 34 px) und bei Größenänderung des Fensters neu
  berechnet – kurze Teams bekommen große Lettern, lange Namen werden nie
  abgeschnitten. Die Walzen sind etwas höher (3 × 64 px).
- **Lichter mit mehr Abwechslung:** Glühbirnen in drei Farben (Gold, Rot,
  Warmweiß, saisonal angepasst) und eine zusätzliche Lichterreihe unter den
  Walzen. Im Leerlauf wechseln alle sechs Sekunden die Programme Lauflicht,
  Welle, Wechselblinken, Auffüllen und Funkeln; beim Drehen rasen die Lichter,
  beim Gewinn blinken sie im Jackpot-Takt.
  Die Bewegungsanimation (Abbremsen mit leichtem Nachfedern) ist unverändert.

## [v18] – 2026-11-12

### Geändert
- **Linienplan – komplett neu als bunter Stadtplan:** Die Linie schlängelt
  sich in Serpentinen (drei Stationen pro Reihe, Kehren an den Rändern) durch
  eine kleine Stadt mit Straßenraster, Häuserblöcken, Fluss mit glitzernder
  Strömung und Parks. Zwei weitere Linien (Orange, Magenta) kreuzen das Netz,
  auf ihnen fahren eigene kleine Züge.
- **Der Zug:** zwei Wagen mit Scheinwerfern, die einzeln der Strecke folgen
  und sich in die Kurven legen; er gleitet flüssig statt in Sekunden-
  sprüngen. Die gefahrene Strecke leuchtet in der Linienfarbe mit
  durchlaufenden Lichtpunkten, die Strecke voraus ist blass.
- **Stationen:** Die aktuelle Person bekommt ein Namensschild und poppt beim
  Wechsel auf, die nächste Station pulsiert orange, erledigte sind gefüllt.
- **Stationsschild oben:** in der Linienfarbe mit Glanz-Effekt, „Nächster
  Halt“ mit hereinspringendem Namen, Uhr und blinkende rote Verspätung bei
  Überziehung – dann glüht auch der Zug rot.
  Ablauf (Redezeit = Fahrt zur nächsten Station) unverändert.

## [v17] – 2026-11-12

### Geändert
- **Linienplan – neu als Fahrgastanzeige:** Die Ansicht sieht jetzt aus wie
  der Bildschirm in einer modernen U-Bahn: dunkles Display im Rahmen mit
  Glasspiegelung. Kopfzeile mit Liniensymbol, **„Nächster Halt“** (wer als
  Nächstes dran ist, der Name gleitet beim Wechsel herein), Uhrzeit mit
  blinkendem Doppelpunkt und bei Überziehung einer roten **Verspätung**
  („+0:12“). Am Ende steht dort „Endstation“.
- **Strecke:** Gefahrener Abschnitt grau, die Strecke voraus in der
  Linienfarbe mit durchlaufendem Lichtimpuls; Zug in Draufsicht mit
  Lichtschweif; aktuelle Station leuchtet mit Lichtband, die nächste pulsiert.
  Ablauf und Zugbewegung (Redezeit = Fahrt zur nächsten Station) unverändert.

## [v16] – 2026-11-12

### Geändert
- **Roadtrip-Ansicht – Auto nach Vorlage:** Seitenprofil nach dem echten ID.3
  neu gezeichnet: flache, weit nach vorn gezogene Frontscheibe, sehr kurze
  Haube, Dach mit Spoiler, schräge Heckklappe, Fensterband mit Knick am
  hinteren Seitenfenster, ums Eck laufendes Rücklicht, langer Radstand und
  große Räder mit Fünf-V-Speichen-Alus. Hellgrau, ohne Herstellerlogo.
- **Räder rollen realistisch:** Der Drehwinkel folgt der tatsächlich
  gefahrenen Strecke (Weg / Radradius) und läuft über alle Sprecher weiter
  vorwärts; nur beim Boost wirbeln sie kurz. Die Fahrtwind-Linien erscheinen
  nur noch beim Boost.

## [v15] – 2026-11-12

### Geändert
- **Roadtrip-Ansicht – feste Landschaft:** Hügel und Mittellinie laufen nicht
  mehr mit. Das Auto fährt über die stehende Straße auf Zielflagge und
  Ladesäule zu, so passt die Bewegung zur Szene. Nur die Wolken ziehen.
- **Roadtrip-Ansicht – neues Auto:** Grauer Kompakt-Stromer im Stil eines
  ID.3 – kurze Front, lang geneigte Frontscheibe, schwarzes Dach mit
  Glasband, silberne C-Säule mit Wabenmuster, schwarze Beplankung, LED-Licht.
  Felgen als Fünf-Doppelspeichen-Alus mit Felgenhorn, Bremsscheibe und
  Nabendeckel. Ohne Herstellerlogo.

## [v14] – 2026-11-12

### Geändert
- **Roadtrip-Ansicht – neue Szene:** Himmel mit Sonne und ziehenden Wolken,
  zwei Hügel-Ebenen, die beim Fahren mit Parallaxe vorbeiziehen, Straße mit
  Randlinien, Grünstreifen und laufender Mittellinie sowie eine Ladesäule
  neben der Zielflagge.
- **Roadtrip-Ansicht – neues Auto:** Lack im Grundton mit Verlauf, getönte
  Scheiben mit Spiegelung, LED-Scheinwerfer, Rücklicht, Alufelgen,
  Bodenschatten und leichtes Federn beim Fahren; beim Wechsel Fahrtwind-Linien
  und ein dynamischerer Boost.
- **Roadtrip-Ansicht – Akku:** Dunkles Gehäuse mit zehn Segmenten, glänzender
  Ladebalken mit Energie-Schimmer; die Farbstufen (grün/gelb/rot) und
  Schwellen bleiben gleich.
- **Saison:** Halloween als Nachtfahrt unter der Mondsichel mit Scheinwerfer-
  kegel, Winter mit verschneiten Hügeln.
- Die Warnsymbole (Akku, Schildkröte) sind unverändert.

## [v13] – 2026-11-12

### Geändert
- **Slotmaschine:** Das Marquee zeigt nur noch Lichter – zwei Reihen, die
  gegenläufig laufen; das „777“-Schild entfällt.
- **Slotmaschine – Hebel:** Ein Klick auf den Hebel dreht die Walze, genau wie
  der Drehen-Button (nur wenn dieser aktiv ist, also nicht während einer
  Drehung oder nach Rundenende).
- **Winter-Saison:** Die Schneehaube auf dem Automaten ist jetzt wellig mit
  kleinen Tropfen statt eines glatten Balkens.

## [v12] – 2026-11-12

### Geändert
- **Slotmaschine – neues Gehäuse:** Die Ansicht ist jetzt als echter
  Spielautomat gebaut: verchromtes Gehäuse im Grundton, Marquee mit
  Lauflichtern und „777“, gewölbte Walze hinter Glas mit Payline-Pfeilen,
  seitlicher Hebel, der sich zum Betrachter hin nach unten zieht und
  zurückfedert, sowie eine Münzschale. Effekte: rasende Lichter und
  Bewegungsunschärfe beim Drehen, beim Einrasten blinkende Lichter, leuchtende
  Payline, Glanz über das Glas und Münzen in der Schale. Die Walze ruht mit
  einem Namen auf der Payline statt am oberen Rand.
  Ablauf, Ziehung, Timer, Sounds und angezeigte Inhalte sind unverändert; bei
  „reduzierte Bewegung“ entfallen Lauflicht, Unschärfe und Münzen.

## [v11] – 2026-09-08

### Hinzugefügt
- **Abfahrtstafel – Verspätung:** Zieht die aktuelle Person über ihre Redezeit,
  färbt sich ihre komplette Zeile von Gelb auf **Rot** und die Statusspalte
  wechselt von „jetzt“ auf **„verspätet“**. Die Statusspalte reserviert dafür
  von Anfang an die nötige Breite, damit das Brett beim Umschlagen nicht neu
  umbricht; die Tafel selbst darf dafür etwas breiter werden.
- **Ansichts-spezifische Overtime-Icons:** Die beiden Symbole neben der Uhr, die
  eine Überziehung anzeigen, passen sich jetzt der jeweiligen Ansicht an
  (Abfahrtstafel: abgefahrener Zug 🚆💨, Slotmaschine 🎰💸, Glücksrad 🎡😵,
  Kartenspiel 🃏✋, Linienplan 🚇💨, Fokus ⌛⏳). Die klassische Ansicht behält
  den explodierenden Kopf und den Wecker 🤯⏰; die Roadtrip-Ansicht signalisiert
  die Überziehung weiterhin über ihre Schildkröte.
- **Projekt-Dokumentation:** Neue Datei [`PROJECT.md`](PROJECT.md) beschreibt
  Idee, Architektur und Dateistruktur des Projekts, damit sich Menschen (und
  andere KI-Werkzeuge) schnell einlesen und die App weiterentwickeln können.
- **Changelog:** Diese Datei. Ab jetzt wird jede Auslieferung hier dokumentiert.

## [v10] – 2026-08-21

### Hinzugefügt
- **Drei neue Ansichten:** Abfahrtstafel (Fallblatt-Tafel), Linienplan und die
  ruhige Fokus-Ansicht mit Sanduhr.
- **Sounds für alle Ansichten** (optional, ab Werk aus): jede Ansicht mit ihrem
  eigenen, im Browser erzeugten Klang, plus Warnton und Schluss-Fanfare.
- **Einstellung „Erstes Mitglied der Liste kommt zum Schluss“** und ein
  breiteres Einstellungs-Overlay.

### Geändert
- Diverse Designanpassungen und Feinschliff über alle Ansichten hinweg.

## Frühere Versionen

Vor Einführung dieses Changelogs; rekonstruiert aus der Git-Historie.

- **2026-07-07 – PWA-Unterstützung:** Progressive Web App mit Offline-Caching,
  „App installieren“-Button und „Neu laden“-Banner (Einführung von `sw.js` und
  der `CACHE_VERSION`-Versionierung).
- **2026-06-16 – Kartenspiel & Saison-Events:** Verbessertes Karten-Layout,
  saisonale Themes (u. a. Karneval, Ostern).
- **2026-06-15 – Kartenspiel-Ansicht** als 5. Visualisierung, inkl.
  „Aussetzen“-Automatik und „Nochmal spielen“.
- **2026-06-15 – Glücksrad-Ansicht** als 4. Visualisierung, mit Hervorhebung des
  aktuellen Ziehens und Timer pro Person.
- **2026-06-11 – Roadtrip-Ansicht (E-Auto)** mit Batterieanzeige, Warn­symbolen,
  saisonalen Events und Entwickler-Optionen.
- **2026-06-10 – Slotmaschinen-Ansicht** und zweisprachige Oberfläche
  (Deutsch/Englisch, i18n-System).
- **2026-05-27 – Erste Veröffentlichung:** klassische Ansicht mit Zufalls­reihen­folge,
  Anwesenheits-Checkliste und Smart Timer; GPL-v3-Lizenz.
