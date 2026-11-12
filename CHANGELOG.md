# Changelog

Alle nennenswerten Änderungen am **Daily Taktgeber** werden in dieser Datei
festgehalten.

Das Format orientiert sich an [Keep a Changelog](https://keepachangelog.com/de/1.0.0/).
Als Versionsnummer dient die `CACHE_VERSION` aus dem Service Worker
[`sw.js`](sw.js): Sie wird bei jeder Veröffentlichung erhöht, wechselt dadurch
den Cache-Namen und löst im laufenden Betrieb das „Neue Version verfügbar“-Banner
aus. **Merkregel:** Bei jeder Änderung, die ausgeliefert wird, `CACHE_VERSION`
hochzählen *und* hier einen Eintrag ergänzen.

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
