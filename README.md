# G32 Connected Grill Monitor and Display

This is a fork of https://github.com/JBecker32/G32-Display-480x320-BT.

The main focus is its use as a mobile grill monitor and thus also as a replacement for the Otto Wilde app / Otto Wilde Grill Buddy. The connection is made via Bluetooth Low Energy (BLE) and therefore requires no login or any OW servers at all. Tested with firmware v.1.4.5 (old firmware "v13" is NOT compatible!).

The hardware used, software installation, and all other details for this project are identical to the original and are very well documented there, including pictures. The base is an ESP32 with the touchscreen display "JC3248W535C".

Alternative version with the previous UI [Original Design](https://github.com/sagdusmir/G32-Grill-Display-480x320-BTpref/tree/feature/BTpref)

[Case by so99hero](https://www.thingiverse.com/thing:7127557)

[Case (remix)](https://www.thingiverse.com/thing:7182655)


What’s different?

* integration with Home Assistant is now optional
* no source code modifications required (only for setting the Home Assistant API token)
* most settings can be configured directly via the device’s touchscreen
* adjustments to the user interface


## Features

* **Temperatures:** displays temperatures for up to 4 grill zones and 4 external temperature probes
* **Gas level monitoring:** reads the weight determined by the "Gas Buddy"
* **Alarms:** temperature alarms can be set for zones and sensors, which can also be signaled acoustically via an integrated optional beeper (touch on the gauge)
* **Timer:** set a countdown time after which an acoustic alarm sounds (touch the top center)
* **Display mode:** the two previously existing display modes have been merged into one
* **Status:** visuylize connection status (WLAN/BLE) and information from the grill itself
* **Battery (optional):** the state of charge (SOC) of an installed internal battery can be displayed
* **Configuration:** various settings can be made directly on the grill monitor via the touchscreen (touch the top left)
* **MEATER®** core temperatures of connected sensors (1–4) are displayed instead of the G32 values, if available


## What’s still missing?
* **Gas Buddy:** calibration of a new gas bottle
* **G32 light:** setting the brightness when light is turned on

## History
* [2025-11-28] BTpref-retro 2.0.0
   - retro style
   - combine numbers and arcs into a single view
   - overall improved touch sensitive areas / usability 
   - ability the easily change color theme
* [2025-11-26] BTpref 1.6.8
   - fixes for G32 reconnect
   - fixes for HA values (especially decimal places)
* [2025-11-12] BTpref 1.6.7
   - usability if WiFi password configuration improved
   - revised Meater configuration page
* [2025-11-06] BTpref 1.6.6
   - delete individual Meater MAC addresses by touching the respective address
* [2025-10-28] BTpref 1.6.5
   - improved Meater accuracy
   - Meater battery level is now shown in the arc view
* [2025-10-24] BTpref 1.6.0
   - Meater support (Meater "Plus" should also work)
* [2025-10-23] BTpref 1.5.4
   - visual hint when G32 MAC scan was successful
* [2025-10-20] BTpref 1.5.3
   - typo in the WiFi settings UI
* [2025-10-19] BTpref 1.5.2
   - fixed position status bar top/bottom
   - countdown timer combined with optional clock display (top center)
   - new UI for setting temperature alarms
   - on-device configuration screen available via the "G32 Connected" text in the top status bar
   - HA integration is now fully optional but still available

Previous releases: see https://github.com/JBecker32/G32-Display-480x320-BT/releases

## Impressions
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

# Acknowledgments
This project would not have been possible without the work of the community. Special thanks go to:

[JBecker32/G32-Display-480x320-HACS](https://github.com/JBecker32/G32-Display-480x320-HACS)

[JBecker32/G32-Display-480x320-BT](https://github.com/JBecker32/G32-Display-480x320-BT)

[JBecker32/G32-Display480x480](https://github.com/JBecker32/G32-Display480x480)

[fschwarz86/g32](https://github.com/fschwarz86/g32)

[ralmoe/g32-docker-client](https://github.com/ralmoe/g32-docker-client)

[MortenVinding/MEATER.yaml (accuracy)](https://gist.github.com/MortenVinding/a513c0094d0df41a4425612257b3cabc)
[so99hero/Standalone Case JC3248W535C](https://www.thingiverse.com/thing:7127557)


# Disclaimer
This is third-party software developed by the community and is not officially developed or supported by Otto Wilde GmbH. Use at your own risk.
