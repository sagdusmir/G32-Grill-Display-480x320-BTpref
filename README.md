# G32 Connected Grill Monitor and Display

![GitHub Tag](https://img.shields.io/github/v/tag/sagdusmir/G32-Grill-Display-480x320-BTpref)
![GitHub Release Date](https://img.shields.io/github/release-date/sagdusmir/G32-Grill-Display-480x320-BTpref)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/t/sagdusmir/G32-Grill-Display-480x320-BTpref/main)
![GitHub License](https://img.shields.io/github/license/sagdusmir/G32-Grill-Display-480x320-BTpref)

This repository started as a fork of https://github.com/JBecker32/G32-Display-480x320-BT, but has since undergone several improvements and changes can no longer be synced without effort.

Focus: **mobile, cloud independent replacement** for the official Otto Wilde app / Grill Buddy — no cloud login, no Otto Wilde servers, Home Assistant totally optional. Direct BLE connection to the grill (tested with firmware **v1.4.5**; older "v13" not compatible).

# Table of Contents

1. [Features](#features)

   - [Implemented functionality](#implemented-functionality)  
   - [What is missing?](#what-is-missing)
3. [Hardware BOM](#hardware-bom)
4. [Uploading the software to the ESP](#uploading-the-software-to-the-esp)
5. [Troubleshooting](#troubleshooting)
6. [Impressions](#impressions)
7. [Acknowledgments](#acknowledgments)
8. [Disclaimer](#disclaimer)

## Features

### Implemented functionality

- Real-time temperatures for up to **4 grill zones** + **4 external probes**
- **Gas level** monitoring (if GasBuddy is installed)
- **Alarms** — visual + optional acoustic (buzzer/speaker) for temperature limits and timer
- **Countdown timer** with alert
- Touchscreen configuration
  - tap top-left "G32 Connected" for entering the settings screen
  - tap top-middle clock / timer to setup a countdown timer
  - tap gauges to configure a temperature alarm
- Multiple **color schemes** (predefined + easy to add your own)
- **Connection & status icons** (BLE, WiFi, lid open, light on, battery SOC)
- **Optional battery monitoring** the state of charge (SOC) of an installed internal battery can be displayed
- **Optional MEATER® integration** shows tip temperatures & battery SOC instead of G32 probes when connected. Starting with BTpref-retro2.4.6 there is an alert if temperature specs are exceeded.
- **Optional Home Assistant (optional)** connectivity to exposed most of the measurements

See [changelog.md](changelog.md).

### What is missing?
* **Meater 2 plus (aka PRO) support:** at the moment Meater 2 plus are not supported, yet
* **Gas Buddy:** calibration of a new gas bottle
* **G32 light:** setting the brightness level for turning on the light in the lid


## Hardware BOM
 * __JC3248W535C__ (ESP32-S3 Development Board with WiFi, Bluetooth, and a 480x320 Pixel 3,5" touchscreen)
 * optional: a buzzer or a speaker
   * buzzer (default)
     * a passive piezo buzzer (piezo 10085 passive, piezo 12085 passive)
     * a JST 1.25 2pin connector cable
   * speaker (needs minor adjustments in the yaml)
     * a small 8Ohm / 1W speaker with a JST 1.25 2pin connector
 * optional: battery (1 cell LiPo/Li-Ion with protection circuit and JST 1.25 2pin connector __with correct polarity__). 2000mAh to 3000mAh recommended.
 * optional: one of these 3d printed cases and 4 machine screws (M2x4mm, or M2x6mm)
   * [Case by so99hero](https://www.thingiverse.com/thing:7127557)
   * [Case (remixed by me)](https://www.thingiverse.com/thing:7182655)
     that also includes a variant that can be hung to any OW module handle and an additional model that allows you to retrofit an existing case with the detachable hanger.

The total cost should be around 35€ if you have a friend with a 3d printer. Some items might not be available individually, but only in packs of several.


## Uploading the software to the ESP

1. Install ESPHome CLI
   ```bash
   pip install esphome
   ```
2. Clone this repository and change directory into that folder
3. Connect the JC3248W535C via USB
4. ```bash
   esphome run g32-display.yaml
   ```

## Troubleshooting

1. During validation of the yaml file, you might see something like `[max_connections] is an invalid option for [esp32_ble]`. The "max_connections" option has been moved from "esp32_ble_tracker:" to "esp32_ble:". Both variants are included in the YAML and you need to switch to the other variant by adding / removing a comment (#). Do not mess up the indentation. This is caused by a breaking change in esphome.

2. If compiling and flashing the ESP32 succeeds, but the screen is looking distorted (the left portion is partially readable while the right portion shows mostly pixel noise"), simply look at the "dimensions" in the "display" section and swap the values for "width:" and "height:". This is caused by a breaking change in esphome.


## Impressions
<img alt="device_assembly" src="https://github.com/user-attachments/assets/8faf2f34-4d98-47f2-9512-1f92ef224469" width="400">
<img alt="BTpref-retro2 0 0-main_view_cyan" src="https://github.com/user-attachments/assets/eca960b4-9641-4546-98c3-ed16e00ab826" width="400">

<img alt="BTpref-retro2 0 1-main_view_red_light" src="https://github.com/user-attachments/assets/b4afa697-324f-45b4-bcb8-1dc0c5bc71a7" width="265">
<img alt="BTpref-retro2 0 1-main_view_white" src="https://github.com/user-attachments/assets/27741973-4c46-4147-9b32-293e49b56a55" width="265">
<img alt="BTpref-retro2 0 0-main_view_amber" src="https://github.com/user-attachments/assets/6b80e574-6c00-42c9-ad54-8ba93f749827" width="265">
<img alt="BTpref-retro2 0 0-temp_alarm" src="https://github.com/user-attachments/assets/73363a1c-2063-4b14-b969-901baaf50088" width="265">
<img alt="BTpref-retro2 0 0-timer" src="https://github.com/user-attachments/assets/fe0e1212-1340-475d-b816-25a6abb685c0" width="265">
<img alt="BTpref-retro2 0 0-mac_address" src="https://github.com/user-attachments/assets/bd0b3435-790f-4acd-af92-3104471958ae" width="265">
<img alt="BTpref-retro2 3 0-wifi" src="https://github.com/user-attachments/assets/35becd29-fdcb-43d7-98a9-295b38a00ef4" width="265">
<img alt="BTpref-retro2 4 3-options" src="https://github.com/user-attachments/assets/981a29ef-3c3d-4a92-9003-8a9c90a8ab68" width="265">
<img alt="BTpref-retro2 3 1-warnings" src="https://github.com/user-attachments/assets/6b73301e-6cd6-405d-8f65-c555cd4398c3" width="265">
<img alt="BTpref-retro2 2 0-display" src="https://github.com/user-attachments/assets/8848e7dd-ddc9-4c12-a840-eedf1176ef42" width="265">
<img alt="BTpref-retro2 0 0-meater" src="https://github.com/user-attachments/assets/344972be-d253-450e-8157-0753d1509755" width="265">
<img alt="BTpref-retro2 4 3-version" src="https://github.com/user-attachments/assets/4b1173f1-c7a9-4835-a2b9-284c4aa8aa36" width="265">
<img alt="BTpref-retro2 4 0-reduced-temp-alarm-info" src="https://github.com/user-attachments/assets/94bd44cf-5bbd-4d45-9673-ba5b1ec7d3ea" width="265">
<img alt="BTpref-retro2 4 1-battery-3000mAh" src="https://github.com/user-attachments/assets/7e3d7d21-d101-47aa-9158-14b8208d6a8e" width="265">


## Acknowledgments
This project would not have been possible without the work of the community. Special thanks go to:

[JBecker32/G32-Display-480x320-HACS](https://github.com/JBecker32/G32-Display-480x320-HACS)

[JBecker32/G32-Display-480x320-BT](https://github.com/JBecker32/G32-Display-480x320-BT)

[JBecker32/G32-Display480x480](https://github.com/JBecker32/G32-Display480x480)

[fschwarz86/g32](https://github.com/fschwarz86/g32)

[ralmoe/g32-docker-client](https://github.com/ralmoe/g32-docker-client)

[MortenVinding/MEATER.yaml (accuracy)](https://gist.github.com/MortenVinding/a513c0094d0df41a4425612257b3cabc)

[so99hero/Standalone Case JC3248W535C](https://www.thingiverse.com/thing:7127557)


## Disclaimer
This is third-party software developed by the community and is not officially developed or supported by Otto Wilde GmbH. Use at your own risk.
