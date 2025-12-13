# G32 Connected Grill Monitor and Display

This is a fork of https://github.com/JBecker32/G32-Display-480x320-BT

and is designed to be used with a JC3248W535C display module (display, touchscreen, and ESP32 in one nice package).

The main focus is its use as a mobile grill monitor and thus also as a replacement for the Otto Wilde app / Otto Wilde Grill Buddy. The connection is made via Bluetooth Low Energy (BLE) and therefore requires no login or any OW servers at all. Tested with firmware v.1.4.5 (old firmware "v13" is known to be NOT compatible!).

The hardware used, software installation, and all other details for this project are identical to the original and are very well documented there, including pictures. The base is an ESP32 with the touchscreen display "JC3248W535C".

[Case by so99hero](https://www.thingiverse.com/thing:7127557)

[Case (remixed by me)](https://www.thingiverse.com/thing:7182655)


What’s different?

* integration with Home Assistant is now optional
* no source code modifications required (only for setting the Home Assistant API token)
* most settings can be configured directly via the device’s touchscreen (unfortunately the Home Assistant "API encryption key" cannot be updated dynamically - this must be known at compile time)
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
* [2025-12-12] BTpref-retro 2.3.0
   - allow configuring the OTA password in the settings
* [2025-12-09] BTpref-retro 2.2.0
   - color scheme can now be selected in the settings without changing the source code
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

## Uploading the software to the ESP ##

- Install the 'esphome' command line tool
- download this repository
- connect the JC3248W535C
- 'esphome run g32-display.yaml'
  

## Impressions
![device_assembly](https://github.com/user-attachments/assets/8faf2f34-4d98-47f2-9512-1f92ef224469)
![BTpref-retro2 0 0-main_view_cyan](https://github.com/user-attachments/assets/eca960b4-9641-4546-98c3-ed16e00ab826)
![BTpref-retro2 0 1-main_view_red_light](https://github.com/user-attachments/assets/b4afa697-324f-45b4-bcb8-1dc0c5bc71a7)
![BTpref-retro2 0 1-main_view_white](https://github.com/user-attachments/assets/27741973-4c46-4147-9b32-293e49b56a55)
![BTpref-retro2 0 0-main_view_amber](https://github.com/user-attachments/assets/6b80e574-6c00-42c9-ad54-8ba93f749827)
![BTpref-retro2 0 0-temp_alarm](https://github.com/user-attachments/assets/73363a1c-2063-4b14-b969-901baaf50088)
![BTpref-retro2 0 0-timer](https://github.com/user-attachments/assets/fe0e1212-1340-475d-b816-25a6abb685c0)
![BTpref-retro2 0 0-mac_address](https://github.com/user-attachments/assets/bd0b3435-790f-4acd-af92-3104471958ae)
![BTpref-retro2 3 0-wifi](https://github.com/user-attachments/assets/35becd29-fdcb-43d7-98a9-295b38a00ef4)
![BTpref-retro2 3 1-options](https://github.com/user-attachments/assets/b6e9c2d8-9c50-45ff-9c59-34328ca54e4e)
![BTpref-retro2 3 1-warnings](https://github.com/user-attachments/assets/6b73301e-6cd6-405d-8f65-c555cd4398c3)
![BTpref-retro2 2 0-display](https://github.com/user-attachments/assets/8848e7dd-ddc9-4c12-a840-eedf1176ef42)
![BTpref-retro2 0 0-meater](https://github.com/user-attachments/assets/344972be-d253-450e-8157-0753d1509755)
![BTpref-retro2 1 0-version](https://github.com/user-attachments/assets/cc267afa-6d3d-407d-ba66-0fad921ef926)


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
