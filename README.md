# G32-Display480x320
ESPHome Projekt für ein JC3248W535 Display zur Verwendung mit einem Otto Wilde G32 Gasgrill.

![PXL_20250531_101818315 MP~2](https://github.com/user-attachments/assets/67b9ae62-9454-436c-98f0-ceb2c0f3f85f)

Das Gerät baut eine Bluetooth Verbindung zum G32 auf (Bluetooth muss am Grill zugelassen sein). Es liest dann diverse Daten aus dem G32 aus, stellt sie auf dem Display grafisch dar und über Wifi dem Home Assistant als Entitäten zur Verfügung.
Nach der Programmierung über ESPHome kann das Gerät auch stand-alone mit dem Grill benutzt werden. Es muss nicht zwingend mit Home Assistant verbunden sein!

Zusätzlich kann das Gerät eine Bluetooth Verbindung zu einem Meater+ (nur mit exakt diesem Typ getestet!) Grillthermometer aufbauen und auch dessen Daten (Kerntemperatur und Garraumtemperatur) auf dem Display anzeigen und zum HA weiterleiten. Die Auswertung der Temperaturen ist experimentell, da zum Bluetooth Protokoll des Meater+ mWn keine Doku zur Verfügung steht.

Die Hardware des JC3248W535 stellt einen Anschluß für einen externen Lithium Akku mit integrierter Ladeschaltung zur Verfügung. Die Spannung des Akkus wird gemessen und ausgewertet. Bei Unterschreiten eines bestimmten SOC (aus der Entladespannung abgeleitet) wird im Display ein Icon einer leeren Batterie eingeblendet.

Zusätzlich kann im JC3248W535 ein Piezo-Summer (nur Typen ohne eingebaute Elektronik!) angeschlossen werden. Ich benutze hier nicht den mit Speaker bezweichneten 2-poligen Anschluß (dieser wird über einen eingebauten I²C Chip angesteuert und ist aufwändiger in der Benutzung) sondern die GPIOs 9 und 14 auf dem 8-poligen Steckverbinder. Der Summer wird an diversen Stellen genutzt, so z.B. bei Aufbau und Verlust der Verbindung zu Wifi und BT oder auch bei Temperaturwarnungen (more to follow ...).



