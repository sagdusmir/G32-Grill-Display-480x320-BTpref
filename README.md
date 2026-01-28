# G32 Connected Grill Monitor and Display

This is a fork of https://github.com/JBecker32/G32-Display-480x320-BT.

The main focus is its use as a mobile grill monitor and thus also as a replacement for the Otto Wilde app / Otto Wilde Grill Buddy. The connection is made via Bluetooth Low Energy (BLE) and therefore requires no login or any OW servers at all. Tested with firmware v.1.4.5 (old firmware "v13" is known to be NOT compatible!).

The hardware used, software installation, and all other details for this project are identical to the original and are very well documented there, including pictures. The base is an ESP32 with the touchscreen display "JC3248W535C".

## Features

* **Temperatures:** displays temperatures for up to 4 grill zones and 4 external temperature probes
* **Gas level monitoring:** reads the weight determined by the "Gas Buddy"
* **Alarms:** temperature alarms can be set for zones and temperature sensors, which can also be signaled acoustically via an integrated optional beeper / speaker (touch on the vizualisation of a zone or tempterature probe)
* **Timer:** set a countdown timer after which an acoustic alarm sounds (touch the top center)
* **Status:** visualize connection status (WLAN/BLE) and information from the grill itself
* **Configuration:** various settings can be changed directly on the grill monitor via the touchscreen (touch the top left "G32 Connected" text)
* **Color Schemes:** some predefined color schemes are available in the settings and even new ones can be easily added by editing the source code
* **Battery (optional):** the state of charge (SOC) of an installed internal battery can be displayed
* **MEATER® (optional):** the tip temperatures and battery SOC of connected sensors (1–4) are displayed instead of the G32 values, if available
* **Home Assistant (optinoal):** most measurements are exposed to Home Assistant

## What’s still missing?
* **Gas Buddy:** calibration of a new gas bottle
* **G32 light:** setting the brightness level for turning on the light in the lid

## BOM (bill of materials)
 * __JC3248W535C__ (ESP32-S3 Development Board with WiFi, Bluetooth, and a 480x320 Pixel 3,5" touchscreen)
 * optional: a buzzer or a speaker
   * buzzer (default)
     * a passive piezo buzzer (piezo 10085 passive, piezo 12085 passive)
     * a JST 1.25 2pin connector cable
   * speaker (needs minor adjustments in the yaml)
     * a small 8Ohm / 1W speaker with a JST 1.25 2pin connector
 * optional: battery (1 cell LiPo/Li-Ion with protection circuit and JST 1.25 2pin connecter __with correct polarity__). 2000mAh to 3000mAh recommended.
 * optional: one of these 3d printed cases and 4 machine screws (M2x4mm, or M2x6mm)
   * [Case by so99hero](https://www.thingiverse.com/thing:7127557)
   * [Case (remixed by me)](https://www.thingiverse.com/thing:7182655)
     that also includes a variant that can be hung to any OW module handle and an additional model that allows you to retrofit an existing case with the detachable hanger.

The total cost should be around 35€ if you have a friend with a 3d printer. Some items might not be available individually, but only in packs of several.

## History
See [changelog.md](changelog.md).


## Uploading the software to the ESP ##
Option A) (more reliable, recommended)

- Install the 'esphome' command line tool
- download this repository
- connect the JC3248W535C
- 'esphome run g32-display.yaml'

Option B) (might end up in a boot loop)

- use the ESPHome Device Builder Add-on for Home Assistant to upload the g32-display.yaml config file


## Troubleshooting ##

There are currently two known issues related to using an older version of esphome.
Both of them are very easy to fix in the YAML file:

1. During validation of the yaml file, you might see something like `[max_connections] is an invalid option for [esp32_ble]`. The "max_connections" option has been moved from "esp32_ble_tracker:" to "esp32_ble:". Both variants are included in the YAML and you need to switch to the other variant by adding / removing a comment (#). Do not mess up the indentation.

2. If compiling and flashing the ESP32 succeeds, but the screen is looking distorted (the left portion is partially readable while the right portion shows mostly pixel noise"), simply look at the "dimensions" in the "display" section and swap the values for "width:" and "height:".


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
![BTpref-retro2 4 3-options](https://github.com/user-attachments/assets/981a29ef-3c3d-4a92-9003-8a9c90a8ab68)
![BTpref-retro2 3 1-warnings](https://github.com/user-attachments/assets/6b73301e-6cd6-405d-8f65-c555cd4398c3)
![BTpref-retro2 2 0-display](https://github.com/user-attachments/assets/8848e7dd-ddc9-4c12-a840-eedf1176ef42)
![BTpref-retro2 0 0-meater](https://github.com/user-attachments/assets/344972be-d253-450e-8157-0753d1509755)
![BTpref-retro2 1 0-version](https://github.com/user-attachments/assets/cc267afa-6d3d-407d-ba66-0fad921ef926)
![BTpref-retro2 4 0-reduced-temp-alarm-info](https://github.com/user-attachments/assets/94bd44cf-5bbd-4d45-9673-ba5b1ec7d3ea)
![BTpref-retro2 4 1-battery-3000mAh](https://github.com/user-attachments/assets/9570a0e2-d5f2-4427-ba55-1a06e2587391)



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
