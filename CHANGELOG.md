# Changelog

Alle nennenswerten Änderungen am **Daily Taktgeber** werden in dieser Datei
festgehalten.

Das Format orientiert sich an [Keep a Changelog](https://keepachangelog.com/de/1.0.0/).
Als Versionsnummer dient die `CACHE_VERSION` aus dem Service Worker
[`sw.js`](sw.js): Sie wird bei jeder Veröffentlichung erhöht, wechselt dadurch
den Cache-Namen und löst im laufenden Betrieb das „Neue Version verfügbar“-Banner
aus. **Merkregel:** Bei jeder Änderung, die ausgeliefert wird, `CACHE_VERSION`
hochzählen *und* hier einen Eintrag ergänzen.

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
