# ESPHome G32 Grill Monitor Display

Dieses ESPHome-Projekt verwandelt ein JC3248W535C Touchscreen-Display in einen hochentwickelten Monitor für Ihren Otto Wilde G32 Grill. Es verbindet sich direkt über Bluetooth (BLE) mit dem Grill, um Echtzeitdaten abzurufen und bietet eine reichhaltige, über LVGL erstellte Benutzeroberfläche zur Visualisierung aller wichtigen Grillinformationen.

Die Benutzeroberfläche ist in zwei Hauptansichten unterteilt, zwischen denen durch Wischen (Swipen) gewechselt werden kann:
1.  **Arc-Ansicht:** Eine farbenfrohe, grafische Darstellung der Temperaturen mit kreisförmigen Bögen.
![PXL_20250831_100654796 RAW-01 MP COVER](https://github.com/user-attachments/assets/9ac30cfc-e850-4c15-8dfb-55084be17deb)


2.  **Zahlen-Ansicht:** Eine schlichte, zahlenbasierte Ansicht, mit Ausnahme der Icons und Alarme grau-weiß.
![PXL_20250831_100641609 RAW-01 MP COVER](https://github.com/user-attachments/assets/cf56bf26-64fc-4241-9dc1-1dac0125bc5f)

* (in Ermangelung guter Fotos sind dieses die Ansichten der HACS Variante. Daher fehlt das Bluetooth-Symbol!)
* Hier sind für die Zonen 2 und 3 Temperaturlimits von 300°C gesetzt.
* Die externen Sensoren 1 und 3 sind am Grill eingesteckt. 
* Der Sensor 1 hat ein Temperaturlimit von 20°C und die aktuelle Temperatur von 29°C überschreitet das Limit, daher rot.
* Gas ist unter dem eingestellten Limit, daher in der Statuszeile das rote 'Ausrufungszeichen' und der Balken ist rot (ansonsten grün oder grau in der Zahlenansicht).
* Der grüne 'Pfeil nach oben' in der Statuszeile zeigt eine offene Haube, der gelbe Blitz eine aktive Innebeleuchtung.
* Daneben das grüne WIFI Symbol für die Verbindung zu Home Assistant und das Symbol für den zu 51% geladenen Akku.
* Die Uhrzeit wird nur angezeigt, wenn eine aktive Verbindung zu einem Home Assistant besteht!

## ✨ Features

* **Echtzeit-Überwachung:** Zeigt Temperaturen für bis zu 4 Grillzonen und 4 externe Temperatursensoren an.
* **Gas-Level-Anzeige:** Überwacht den Füllstand des Gasbuddy in Prozent und Gramm, inklusive einer visuellen Leiste.
* **Temperaturalarme:** Setzen Sie individuelle Temperaturlimits für jede Zone und jeden Sensor. Bei Überschreitung wird ein akustischer Alarm über den integrierten Beeper ausgelöst.
* **Zwei Display-Modi:** Wechseln Sie durch Wischen zwischen einer grafischen "Arc"-Ansicht und einer minimalistischen "Zahlen"-Ansicht.
* **Status-Symbole:** Icons auf dem Display zeigen den Verbindungsstatus von WLAN und Bluetooth sowie den Zustand von Grillhaube und Licht an.
* **Home Assistant Integration:** Nahtlose Einbindung in Home Assistant über die ESPHome API.
* **Umfassend anpassbar:** Passen Sie Farben, Texte, Anzeigeelemente und Schwellenwerte direkt in der YAML-Datei an Ihre Wünsche an.
* **Batterieüberwachung (Optional):** Zeigt den Ladezustand (SOC) eines optional angeschlossenen Akkus an.
* **Fallback-WLAN:** Erstellt einen eigenen Access Point, falls die Verbindung zum primären WLAN fehlschlägt.

## 🛠️ Hardware-Voraussetzungen

Dieses Projekt ist für eine bestimmte Kombination aus Mikrocontroller und Display konzipiert.

* **Display:** Ein **JC3248W535C 480x320 Pixel** LCD-Display 
* **(Optional) Beeper/Lautsprecher:** Ein kleiner passiver Piezo Beeper zur Ausgabe von Alarmtönen.
* **(Optional) Akku:** Ein LiPo/Li-Ion-Akku zur mobilen Stromversorgung.

## 🛠️ Materialliste (inklusive optionaler Bauteile)

Folgende Bauteile werden für ein Display benötigt (da Links schnell veralten habe ich Suchoptionen angegeben):

* **Display:** **JC3248W535C** Unter dieser Bezeichnung bei Amazon (~25-35€) oder Aliexpress (~19-30€) suchen. Alle Displays mit exakt dieser Bezeichnung sind in der Hardware vollkommen identisch und funktionieren mit der Firmware.
* **Gehäuse:** 3D-Druck-Gehäuse. Sehr gut geeignet: [Standalone Case JC3248W535C](https://www.thingiverse.com/thing:7127557) Das Gehäuse erlaubt den Betrieb in steil stehender Form oder flach liegender Form (Anpassung in der Firmware erforderlich). Hinten im Gehäuse befindet sich ein 'Taster', mit dem bei Akkubetrieb das Display ausgeschaltet werden kann (Druck > 8 Sekunden). Und natürlich auch wieder eingeschaltet (Druck > 0.2 Sekunden).  
* **(Optional) Akku:** Ein LiPo/Li-Ion-Akku zur mobilen Stromversorgung. Sehr gut verwendbar sind fertig konfektionierte Lithium Polymer Akkus mit z.B. 2000mAh mit JST 1.25mm Stecker. Bei Amozon suchen nach '2000mAh 1.25'. Bitte auf die 1.25mm Stecker achten und auf die Polung (mit dem Displayanschluß vergleichen). Alle von mir bestellten Akkus hatten bisher die korrekte Polarität, manche werden aber auch mit 'umgekehrte Polarität' beworben und sind **nicht** geeignet!
Alternativ kann jede 18650 Akkuzelle verwendet werden. Diese gibt es mit Kapazitäten bis ~3500mAh. Benötigt wird dann zusätzlich ein kurzes (~10cm) Kabel mit JST 1.25mm Stecker (suchen nach 'JST 1.25 2 Pin'). 20-25 Stück kosten ~5-6€ (kaum einzeln verfügbar). Das Kabel am Display in den Akku-Anschluß einstecken und prüfen ob rot auf + und schwarz auf - liegt und den Akku polrichtig anlöten. Alle mir bekannten Kabel sind aber korrekt belegt gewesen.         
* **(Optional) Beeper/Lautsprecher:** Ein kleiner passiver Piezo Beeper zur Ausgabe von Alarmtönen. Bei Amazon suchen nach 'Piezo 10085 passiv' oder 'Piezo 12085 passiv'. Geeignet sind nahezu alle **passiven** Buzzer, am Besten klein mit z.B. 10-12mm Durchmesser (10085 = 10mm, 12085 = 12mm). Auch hier gibt es meistens 5-50 Stück für 5-10€. Für den Anschluß benötigt man das gleiche Kabel wie für den Akku (JST 1.25 2 Pin 10cm Kabel). Das Kabel wird am Display auf die 2 Pins IO9 und IO14 von P2 gesteckt. 

## ⚙️ Installation & Konfiguration

### Voraussetzungen
1. **ESPHome** als Add-on in Home Assistant oder als eigenständige Installation.
2. Optional: eine laufende **Home Assistant** Instanz. Die Daten des Grills werden dann in den Home Assistant übergeben. 

### Installationsschritte

1.  **Neues Gerät in ESPHome erstellen:**
    * Gehen Sie zum ESPHome Dashboard.
    * Klicken Sie auf "+ NEW DEVICE" und folgen Sie den Anweisungen. Dies ist notwendig, um einen `api_encryption_key` und ein `ota_password` zu generieren. Notieren Sie sich diese Werte.

2.  **YAML-Datei konfigurieren:**
    * Laden Sie die Datei `g32-display.yaml` herunter und kopieren Sie sie in Ihr `/esphome`-Verzeichnis.
    * Öffnen Sie die Datei und passen Sie den oberen `substitutions`-Abschnitt an Ihre Bedürfnisse an. Dies ist der einzige Bereich, den Sie bearbeiten müssen.

3.  **Firmware kompilieren und hochladen:**
    * **Erstes Flashen:** Verbinden Sie Ihr Display über USB mit dem Computer, auf dem ESPHome läuft. Klicken Sie im ESPHome-Dashboard auf "Install" und wählen Sie die USB-Option.
    * **Zukünftige Updates:** Sobald das Gerät im Netzwerk ist, können Sie Updates drahtlos (OTA) durchführen, indem Sie auf "Install" und "Wirelessly" klicken.

### Benutzerkonfiguration (`substitutions`)

Passen Sie die folgenden Variablen in der YAML-Datei an:

| Variable | Beispielwert | Beschreibung |
| :--- | :--- | :--- |
| `name` | `g32-display-bt` | Der Name Ihres Geräts, wie er in ESPHome und Home Assistant angezeigt wird. Keine Leer- oder Sonderzeichen. |
| `g32_mac_address` | `94:E6:86:xx:yy:zz`| **WICHTIG:** Die Bluetooth-MAC-Adresse Ihres G32 Grills. (Siehe Hinweis unten) |
| `wifi_ssid` | `!secret wifi_ssid` | Der Name (SSID) Ihres WLAN-Netzwerks. |
| `wifi_password` | `!secret wifi_password` | Das Passwort für Ihr WLAN-Netzwerk. |
| `api_encryption_key` | `"E1f...U6k="` | Der Verschlüsselungsschlüssel aus dem in Schritt 1 erstellten ESPHome-Gerät. |
| `ota_password` | `"398...701a"` | Das Passwort für drahtlose Updates aus dem in Schritt 1 erstellten ESPHome-Gerät. |
| `ap_ssid` | `"G32 Display..."`| Der Name des Fallback-WLAN-Hotspots. |
| `ap_password` | `"4Lyt...DNh"` | Das Passwort für den Fallback-Hotspot. |
| `Zone_Text` | `"Zone "` | Der Präfix-Text für die Grillzonen (ergibt "Zone 1", "Zone 2" usw.). |
| `Sensor_Text` | `"Sensor "` | Der Präfix-Text für die externen Sensoren. |
| `Zone_Arc_Color` | `"0xff0000"` | Farbe (Hex-Code) der Temperatur-Bögen für die Zonen. |
| `Sensor_Arc_Color`| `"0xffff00"` | Farbe (Hex-Code) der Temperatur-Bögen für die Sensoren. |
| `Hide_Battery_Symbol`| `'false'` | Setzen Sie auf `'true'`, wenn Sie kein Akku-Symbol anzeigen möchten. |
| `Min_SOC` | `"25"` | Der Akku-Prozentsatz, unter dem das Symbol rot angezeigt wird. |
| `Hide_Inactive_Sensors`| `'false'` | Setzen Sie auf `'true'`, um inaktive Sensoren komplett auszublenden. |
| `Enable_Temperature_Limits`| `'true'` | Setzen Sie auf `'false'`, um die Funktion zum Setzen von Temperaturlimits zu deaktivieren. |
| `Sensor1_Max` | `"130"` | Maximale einstellbare Temperatur für Sensor 1 (z.B. für Kerntemperatur). |
| `Beeper_interval`| `"5s"` | Das Zeitintervall für Alarmmeldungen des Lautsprechers. |
| `Show_Time` | `'true'` | Setzen Sie auf `'true'`, um die Uhrzeit (von Home Assistant synchronisiert) anzuzeigen. |
| `Show_Arcs_Page` | `'true'` | Legt fest, ob die grafische "Arc"-Seite angezeigt werden soll. |
| `Show_Numbers_Page`| `'true'` | Legt fest, ob die "Zahlen"-Seite angezeigt werden soll. |

> **💡 So finden Sie die MAC-Adresse Ihres Grills:**
> Wenn Sie die MAC-Adresse Ihres G32 nicht kennen, können Sie sie mit diesem Projekt selbst finden.
> 1.  Entfernen Sie die Kommentarzeichen (`#`) vor den Zeilen des `esp32_ble_tracker:` in der YAML-Datei.
> 2.  Installieren Sie die Firmware auf Ihrem ESP32.
> 3.  Öffnen Sie die "Logs" für das Gerät im ESPHome-Dashboard.
> 4.  Schalten Sie Ihren G32 Grill ein. In den Logs sollte eine Meldung erscheinen, die mit "G32 gefunden" beginnt und die MAC-Adresse anzeigt.
> 5.  Kopieren Sie diese Adresse in das Feld `g32_mac_address`.
> 6.  Kommentieren Sie den `esp32_ble_tracker:`-Block wieder aus, um Ressourcen zu sparen.

## 🕹️ Bedienung

* **Seiten wechseln:** Wischen Sie auf dem Display nach links oder rechts, um zwischen der "Arc"-Ansicht und der "Zahlen"-Ansicht zu wechseln (sofern beide aktiviert sind).
* **Temperaturlimit setzen:** Tippen Sie auf eine Temperaturanzeige (entweder in der Arc- oder der Zahlen-Ansicht). Es öffnet sich eine neue Seite, auf der Sie mit den Tasten `+` / `-` oder dem Schieberegler ein Temperaturlimit festlegen können. Bestätigen Sie mit "OK".
* **Bildschirm aufwecken:** Wenn der Bildschirm nach der eingestellten Zeit in den Ruhezustand wechselt (Bildschirm aus), tippen Sie einfach einmal auf das Display, um ihn wieder zu aktivieren.
* **ACHTUNG:** Der Touchscreen dieses Displays ist leider nicht sehr 'genau' und neigt zusätzlich zu 'Sprüngen'. Er hat auch einen toten Bereich zu den Rändern hin. Daher ist die Bedienung manchmal etwas 'hakelig' und/oder die Bedienelemente müssen etwas außerhalb ihrer Mitte gedrückt werden. Das Swipen zwischen den Fenstern macht man am Besten in dem freien Bereich zwischen den oberen Zonen und den unterene Sensoren, also in etwa auf Linie mit dem Schriftzug "Temperatursensoren".  
