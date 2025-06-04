# G32-Display480x320
ESPHome Projekt für ein JC3248W535 Display zur Verwendung mit einem Otto Wilde G32 Gasgrill.

![PXL_20250531_101818315 MP~2](https://github.com/user-attachments/assets/67b9ae62-9454-436c-98f0-ceb2c0f3f85f)

Das Gerät baut eine Bluetooth Verbindung zum G32 aus. Es liest dann diverse Daten aus dem G32 aus, stellt sie auf dem Display grafisch dar und stellt sie über Wifi dem Home Assistant zur Verfügung.

Zusätzlich kann es eine Verbindung zu einem Meater+ (nur mit exakt diesem Typ getestet!) Grillthermometer aufbauen und auch dessen Daten (Kerntemperatur und Garraumtemperatur) anzeigen und zum HA weiterleiten. Die Auswertung der Temperaturen ist experimentell, da zum Bluetooth Protokoll des Meater+ mWn keine Doku zur Verfügung steht.

Die Hardware des JC3248W535 stellt einen Anschluß für einen externen Lithium Akku zur Verfügung. Dessen Spannung kann ausgelesen werden und wird vom Display ausgewertet. Bei Unterschreiten eines bestimmten SOC wird im Display ein Icon einer leeren Batterie eingeblendet.

Zusätzlich kann im JC3248W535 ein Piezo-Summer (Typen ohne eingebaute Elektronik!) angeschlossen werden. Ich benutze hier nicht den mit Speaker bezweichneten 2-poligen Anschluß (dieser wird über einen eingebauten I²C Chip angesteuert und ist aufwändiger in der Benutzung) sondern die GPIOs I9 und I14 auf dem 8-poligen Steckverbinder. Der Summer wird an diversen Stellen genutzt, so z.B. bei Aufbau und Verlust der Verbindung zu Wifi und BT oder auch bei temperaturwarnungen (more to follow ...).



