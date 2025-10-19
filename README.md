# G32 Connected Grill Monitor Display

Dies is ein Fork von https://github.com/JBecker32/G32-Display-480x320-BT.

Im Vordergrund steht der Einsatz als mobiler Grill Monitor and damit auch der Ersatz der Otto Wilde App / des Otto Wilde Grill Buddy.

Verwendete Hardware, Software Installation und sonstige Details für dieses Projekt entsprechen dem Original und sind dort sehr gut dokumentiert und auch anhand von Bildern visualisiert.


Was ist anders?

* kein Fokus auf die Anbindung an Home Asssistant
* Anpassungen an der Software sind nicht zwingend notwendig
* vieles lässt sich direkt über das Tochdisplay am Gerät konfigureren
* Anpassungen an der Benutzeroberfläche


## Features

* **Temperaturen:** Zeigt Temperaturen für bis zu 4 Grillzonen und 4 externe Temperatursensoren an
* **Gas-Level-Überwachung:** liest das vom "Gas Buddy" ermittelte Gewicht aus.
* **Alarme:** Für Zonen und Sensoren lassen sich Temperatur-Alarme setzen, die auch über einen integrierten Beeper akkustisch signalisiert werden
* **Timer:** Festlegen einer Zeit, nach der ein akkustischer Alarm ertönt
* **Darstellungsarten:** zwei unterschiedlichen Ansichten
* **Status:** Auf dem Display zeigen werden neben Verbindungsstatus (WLAN/BLE) vom Grill Monitor auch Informationen des Grills angezeigt
* **Akku (Optional):** Der Ladezustand (SOC) eines optional angeschlossenen Akkus kann angezeigt werden


## Was fehlt?
* **Gas Buddy:** Einmessen der Gasflasch
* **Meater:** Verwendung von Meater / Meater+ Temperatursensoren

## Historie
* [2025-10-19] BTpref 1.5.0
   - feststehende Statusanzeige oben / unten
   - Timer ist mit der optionalen Uhrzeitanzeige (oben mittig) vereint
   - andere UI zum Einstellen von Temperaturalarmen
   - Konfiguration an Gerät selbst über "G32 Connected" Schriftzug in der oberen Statuszeile
   - HA Integration ist weitestgehend noch vorhanden – ungetestet

Vorherige Releases siehe https://github.com/JBecker32/G32-Display-480x320-BT/releases

