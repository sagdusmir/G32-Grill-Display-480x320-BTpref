# G32 Connected Grill Monitor and Display

This is a fork of https://github.com/JBecker32/G32-Display-480x320-BT.

Alternative version with the previous UI [Original Design](https://github.com/sagdusmir/G32-Grill-Display-480x320-BTpref/tree/BTpref)

The main focus is its use as a mobile grill monitor and thus also as a replacement for the Otto Wilde app / Otto Wilde Grill Buddy. The connection is made via Bluetooth Low Energy (BLE) and therefore requires no login or any OW servers at all. Tested with firmware v.1.4.5 (old firmware "v13" is known to be NOT compatible!).

The hardware used, software installation, and all other details for this project are identical to the original and are very well documented there, including pictures. The base is an ESP32 with the touchscreen display "JC3248W535C".

[Case by so99hero](https://www.thingiverse.com/thing:7127557)

[Case (remixed by me)](https://www.thingiverse.com/thing:7182655)


What’s different?

* integration with Home Assistant is now optional
* no source code modifications required (only for setting the Home Assistant API token)
* most settings can be configured directly via the device’s touchscreen (unfortunately the Home Assistant "API encryption key" cannot be updated dynamically - this must set at compile time)
* adjustments to the user interface


## Features

* **Temperatures:** displays temperatures for up to 4 grill zones and 4 external temperature probes
* **Gas level monitoring:** reads the weight determined by the "Gas Buddy"
* **Alarms:** temperature alarms can be set for zones and temperature sensors, which can also be signaled acoustically via an integrated optional beeper (touch on the vizualisation of a zone or temp probe)
* **Timer:** set a countdown timer after which an acoustic alarm sounds (touch the top center)
* **Display mode:** the two previously existing display modes have been merged into one (numbers + arcs)
* **Status:** visualize connection status (WLAN/BLE) and information from the grill itself
* **Battery (optional):** the state of charge (SOC) of an installed internal battery can be displayed
* **Configuration:** various settings can be changed directly on the grill monitor via the touchscreen (touch the top left)
* **MEATER®** tip temperatures of connected sensors (1–4) are displayed instead of the G32 values, if available


## What’s still missing?
* **Gas Buddy:** calibration of a new gas bottle
* **G32 light:** setting the brightness when the light should turn on

## History
* [2025-12-09] BTpref-retro 2.2.0
   - color theme can now be selected in the settings without changing the source code
* [2025-12-06] BTpref-retro 2.1.1
   - load font files from github - so now the software is only a single yaml file again
* [2025-12-04] BTpref-retro 2.1.0
   - updates for ESPHome 2025.11.3
   - automatic version check
* [2025-11-30] BTpref-retro 2.0.4
   - enable warning sign when gas tank level / soc level is low
* [2025-11-28] BTpref-retro 2.0.1
   - retro style
   - combine numbers and arcs into a single view
   - overall improved touch sensitive areas / usability 
   - ability the easily change color theme (requires flashing the device)
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

Other releases: see https://github.com/JBecker32/G32-Display-480x320-BT/releases

## Impressions

![device_assembly](https://github.com/user-attachments/assets/e1ed5b51-65a1-48ba-af6a-0f25a4d720d0)
![BTpref-retro2 0 0-main_view_cyan](https://github.com/user-attachments/assets/32d1266b-2c4c-46a6-880c-3ed1884f341f)
![BTpref-retro2 0 1-main_view_red_light](https://github.com/user-attachments/assets/555efccb-7f62-41be-9de1-9237aa4ffe6c)
![BTpref-retro2 0 1-main_view_white](https://github.com/user-attachments/assets/1ba5c8ff-0080-4f08-b29d-0a2fba34e5e9)

![BTpref-retro2 0 0-main_view_amber](https://github.com/user-attachments/assets/18bd5f68-c9b2-402b-b71a-66e80dac2365)

Some colors do look better in real life, than they do in pictures.  :)

![BTpref-retro2 0 0-temp_alarm](https://github.com/user-attachments/assets/750c4b4f-d1fe-4853-b18c-f6d65a70f349)
![BTpref-retro2 0 0-timer](https://github.com/user-attachments/assets/daa7dc4d-ddb1-45dc-b47e-e539bdda1212)
![BTpref-retro2 0 0-mac_address](https://github.com/user-attachments/assets/4508c643-026a-40ec-a457-311dd6bc7bcf)
![BTpref-retro2 0 0-wifi](https://github.com/user-attachments/assets/7dc43028-4d93-4fbe-bbe2-c1864379c14e)
![BTpref-retro2 0 0-options](https://github.com/user-attachments/assets/19b3319a-d9f6-4726-be54-1720253332d5)
![BTpref-retro2 0 0-warnings](https://github.com/user-attachments/assets/1e46b379-1476-4764-b74a-f269498abbbd)
![BTpref-retro2 2 0-display](https://github.com/user-attachments/assets/6d8f0b91-ae05-4f82-b3d8-83a30ff6e5a7)
![BTpref-retro2 0 0-meater](https://github.com/user-attachments/assets/0d8408ab-4244-4838-aa5d-c71464d69ddc)
![BTpref-retro2 1 0-version](https://github.com/user-attachments/assets/a2dd64ca-0ce5-44a7-b69c-8b4dc60d78ce)


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
