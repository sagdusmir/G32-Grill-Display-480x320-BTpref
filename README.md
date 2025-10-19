# G32 Connected Grill Monitor Display

Dies is ein Fork von https://github.com/JBecker32/G32-Display-480x320-BT.

Im Vordergrund steht der Einsatz als mobiler Grill Monitor and damit auch der Ersatz der Otto Wilde App / des Otto Wilde Grill Buddy.

Verwendete Hardware, Software Installation und sonstige Details für dieses Projekt entsprechen dem Original und sind dort sehr gut dokumentiert und auch anhand von Bildern visualisiert.


Was ist anders?

* kein Fokus auf die Anbindung an Home Asssistant
* Anpassungen an der Software sind nicht zwingend notwendig
* vieles lässt sich direkt über das Tochdisplay am Gerät konfigurieren
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
* **Gas Buddy:** Einmessen der Gasflasche
* **Meater:** Verwendung von Meater / Meater+ als Temperatursensoren

## Historie
* [2025-10-19] BTpref 1.5.1
   - feststehende Statusanzeige oben / unten
   - Timer ist mit der optionalen Uhrzeitanzeige (oben mittig) vereint
   - andere UI zum Einstellen von Temperaturalarmen
   - Konfiguration an Gerät selbst über "G32 Connected" Schriftzug in der oberen Statuszeile
   - HA Integration ist weitestgehend noch vorhanden – ungetestet

Vorherige Releases siehe https://github.com/JBecker32/G32-Display-480x320-BT/releases

## Impressionen
![device_assembly](https://github.com/user-attachments/assets/e1ed5b51-65a1-48ba-af6a-0f25a4d720d0)
![BTpref1 5 0-arc-view](https://github.com/user-attachments/assets/df7cd09a-7bf0-4658-a1f5-c7aee666faed)
![BTpref1 5 0-temp-alarm](https://github.com/user-attachments/assets/2e1a6204-c80d-4cc5-ab94-dba9e09b86f0)
![BTpref1 5 0-mac_address](https://github.com/user-attachments/assets/1835a792-66a5-44ac-a83f-4d439dd1e440)
![BTpref1 5 0-wifi](https://github.com/user-attachments/assets/f8b703cd-6cc8-4902-8594-2603a53e50a4)
![BTpref1 5 0-options](https://github.com/user-attachments/assets/e239b53a-f514-45f7-bb1e-a49f2928d9c0)
![BTpref1 5 0-warnings](https://github.com/user-attachments/assets/640a62a2-c2cb-423e-9729-244513d95b0e)
![BTpref1 5 0-display](https://github.com/user-attachments/assets/628dbb8d-dd4b-4a6f-ab9b-d35b26bd6fbc)
