# G32 Connected Grill Monitor Display

Dies ist ein Fork von https://github.com/JBecker32/G32-Display-480x320-BT.

Im Vordergrund steht der Einsatz als mobiler Grill Monitor and damit auch der Ersatz der Otto Wilde App / des Otto Wilde Grill Buddy. Die Verbindung erfolgt über Bluetooth Low Energy (BLE) und benötigt damit keinerlei Login oder gar die Server von OW.

Verwendete Hardware, Software Installation und sonstige Details für dieses Projekt entsprechen dem Original und sind dort sehr gut dokumentiert und auch anhand von Bildern visualisiert. Basis ist ein ESP mit Tochscreen-Display "JC3248W535C".

[Gehäuse von so99hero](https://www.thingiverse.com/thing:7127557)

[Gehäuse (remix)](https://www.thingiverse.com/thing:7182655)


Was ist anders?

* Anbindung an Home Asssistant ist nun optional
* Anpassungen an der Software sind nicht zwingend erforderlich (nur für Home Assistant API)
* vieles lässt sich direkt über das Tochdisplay am Gerät konfigurieren
* Anpassungen an der Benutzeroberfläche


## Features

* **Temperaturen:** Zeigt Temperaturen für bis zu 4 Grillzonen und 4 externe Temperatursensoren an
* **Gas-Level-Überwachung:** liest das vom "Gas Buddy" ermittelte Gewicht aus
* **Alarme:** Für Zonen und Sensoren lassen sich Temperatur-Alarme setzen, die auch über einen integrierten Beeper (optional) akkustisch signalisiert werden (über Sensor bzw. Zone)
* **Timer:** Festlegen einer Zeit, nach der ein akkustischer Alarm ertönt (oben mittig)
* **Darstellungsarten:** zwei unterschiedlichen Ansichten (horizontal wischen)
* **Status:** Auf dem Display werden neben Verbindungsstatus (WLAN/BLE) vom Grill Monitor auch Informationen des Grills angezeigt
* **Akku (Optional):** Der Ladezustand (SOC) eines optional angeschlossenen Akkus kann angezeigt werden
* **Konfiguration:** Diverse Einstellungen sind über den Touchscreen des Grill Monitors selbst vornehmbar (oben links)
* **MEATER®** Kerntemperaturen verbundener Sensoren (1-4) werden anstelle der Werte des G32 dargestellt


## Was fehlt?
* **Gas Buddy:** Einmessen der Gasflasche

## Historie
* [2025-11-12] BTpref 1.6.7
   - WiFi Passwort einfacher korrekt einzugeben
   - Meater Konfigurationsseite überarbeitet
* [2025-11-06] BTpref 1.6.6
   - Löschen einzelner Meater MAC Adressen bei Touch auf die entsprechende Adresse
* [2025-10-28] BTpref 1.6.5
   - verbessterte Meater Genauigkeit
   - Meater Batterie Level in der Arc Ansicht
* [2025-10-24] BTpref 1.6.0
   - Meater Unterstützung (Meater "Plus" sollten auch funktionieren)
* [2025-10-23] BTpref 1.5.4
   - Anzeige, falls G32 MAC Scan erfolgreich war
* [2025-10-20] BTpref 1.5.3
   - Tippfelhler in der UI der WIFI Einstellungen
* [2025-10-19] BTpref 1.5.2
   - feststehende Statusanzeige oben / unten
   - Timer ist mit der optionalen Uhrzeitanzeige (oben mittig) vereint
   - andere UI zum Einstellen von Temperaturalarmen
   - Konfiguration am Gerät selbst über "G32 Connected" Schriftzug in der oberen Statuszeile
   - HA Integration ist weitestgehend noch vorhanden – ungetestet

Vorherige Releases siehe https://github.com/JBecker32/G32-Display-480x320-BT/releases

## Impressionen
![device_assembly](https://github.com/user-attachments/assets/e1ed5b51-65a1-48ba-af6a-0f25a4d720d0)
![BTpref1 5 0-arc-view](https://github.com/user-attachments/assets/df7cd09a-7bf0-4658-a1f5-c7aee666faed)
![BTpref1 5 0-temp-alarm](https://github.com/user-attachments/assets/2e1a6204-c80d-4cc5-ab94-dba9e09b86f0)
![BTpref1 5 0-timer](https://github.com/user-attachments/assets/db585171-27aa-4cb7-a043-48e60d43d88e)
![BTpref1 5 0-mac_address](https://github.com/user-attachments/assets/1835a792-66a5-44ac-a83f-4d439dd1e440)
![BTpref1 5 2b-wifi](https://github.com/user-attachments/assets/52e46c23-6388-4631-b8a8-9d760ec48c1a)
![BTpref1 5 0-options](https://github.com/user-attachments/assets/e239b53a-f514-45f7-bb1e-a49f2928d9c0)
![BTpref1 5 0-warnings](https://github.com/user-attachments/assets/640a62a2-c2cb-423e-9729-244513d95b0e)
![BTpref1 5 0-display](https://github.com/user-attachments/assets/628dbb8d-dd4b-4a6f-ab9b-d35b26bd6fbc)
![BTpref1 6 0-meater](https://github.com/user-attachments/assets/37d671f4-4aa4-48b3-984d-0332f5cd7c76)

# Danksagungen
Dieses Projekt wäre ohne die Leistungen der Community nicht möglich gewesen. Besonderer Dank gilt:

[JBecker32/G32-Display-480x320-HACS](https://github.com/JBecker32/G32-Display-480x320-HACS)

[JBecker32/G32-Display-480x320-BT](https://github.com/JBecker32/G32-Display-480x320-BT)

[JBecker32/G32-Display480x480](https://github.com/JBecker32/G32-Display480x480)

[fschwarz86/g32](https://github.com/fschwarz86/g32)

[ralmoe/g32-docker-client](https://github.com/ralmoe/g32-docker-client)

[MortenVinding/MEATER.yaml (accuracy)](https://gist.github.com/MortenVinding/a513c0094d0df41a4425612257b3cabc)
[so99hero/Standalone Case JC3248W535C](https://www.thingiverse.com/thing:7127557)


# Haftungsausschluss
Dies ist eine Drittanbieter-Software, die von der Community entwickelt wurde und nicht offiziell von der Otto Wilde GmbH entwickelt oder unterstützt wird. Nutzung auf eigene Gefahr.
