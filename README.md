# G32 Connected Grill Monitor and Display

![GitHub Tag](https://img.shields.io/github/v/tag/sagdusmir/G32-Grill-Display-480x320-BTpref)
![GitHub Release Date](https://img.shields.io/github/release-date/sagdusmir/G32-Grill-Display-480x320-BTpref)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/t/sagdusmir/G32-Grill-Display-480x320-BTpref/main)
![GitHub License](https://img.shields.io/github/license/sagdusmir/G32-Grill-Display-480x320-BTpref)
![Grill make](https://img.shields.io/badge/grill-OW_G32_Connected-critical)
![HA support](https://img.shields.io/badge/Home_Assistant-supported-informational)


This repository started as a fork of https://github.com/JBecker32/G32-Display-480x320-BT and has since been heavily reworked with several improvements and can no longer be synced easily.

Focus: **mobile, cloud-independent replacement** for the official Otto Wilde app / Grill Buddy — no cloud login, no Otto Wilde servers, Home Assistant totally optional. Direct BLE connection to the grill (tested with firmware **v1.4.5**; older "v13" not compatible).

<img alt="Teaser" src="https://github.com/user-attachments/assets/0f5f5065-4ec5-47f8-8567-3b7de9df23e4" width="200">
Assembled device with the case for attaching it to OW Module handles.

# Table of Contents

1. [Features](#features)
   - [Implemented functionality](#implemented-functionality)  
   - [What is missing?](#what-is-missing)
3. [Hardware](#hardware)
   - [BOM](#bom)
   - [Component Details](#component-details)
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
* **Meater 2 plus (aka PRO) support:** __Meater 2 Plus__ units are not supported yet
* **Gas Buddy:** calibration of a new gas bottle
* **G32 light:** setting the brightness level for turning on the light in the lid


## Hardware
### BOM

| Component                            | Qty | Source                                   | Costs        |
|--------------------------------------|-----|------------------------------------------|--------------|
| ESP32 Dev Board                      | 1   | Amazon, AliExpress                       |   ~17€ - 27€ |
| Case                                 | 1   | friend with a 3D Printer                 |    A beer    |
| Screws                               | 4   | hardware store, ebay, Amazon, AliExpress |       ~1€    |
| Battery (optional)                   | 1   | Amazon, AliExpress                       |       ~9€    |   
| Buzzer / Speaker (optional)          | 1   | AliExpress, Amazon, eBay                 |       ~2€    |
| Double-Sided mirror tape (optional)  | ?   | Amazon, eBay                             |       ~0€    |
| Connection Cable                     | 1   | your existing collection of cables       |       ~0€    |

The total cost should be around 35-40€ if you have a friend with a 3d printer. Some items might not be available individually, but only in packs of several.

### Component Details

* __ESP32 Dev Board__<br>
  You need a "__JC3248W535C__". It is equipped with an ESP32-S3, WiFi, Bluetooth, a 480x320 Pixel 3,5" touchscreen and everything you need. No additional memory card required.

* __Case__<br>
 For a 3D model of a case for the JC3248W535C you can take a look at on of these:
   * [Case by so99hero](https://www.thingiverse.com/thing:7127557)
   * [Case by so99hero (remixed by sagdusmir)](https://www.thingiverse.com/thing:7182655)<br>
     This one features minor adjustments to support the USB-C port and reduce clearance for the power button.<br>
     There is also a variant to hang the case directly to any front facing handles of the OW Modules.

  Note: Mounting the display requires you to remove the plastic cover at the back of the display.

* __Screws__<br>
  Either M2x6mm or M2x4mm should work fine. 

* __Battery__<br>
  You can add a 3.7V LiPo/Li-Ion Battery (1 cell) with a JST 1.25 2pin connector (__watch out for correct polarity__) – see images. A capacity of 2000mAh to 3000mAh is recommended and of course it should have protection circuitry built in. This connects directly to the "BAT" (P5) connector.

* __Buzzer / Speaker__<br>
  You can choose to connect either a buzzer or a speaker:
  * A passive piezo buzzer.<br>These do not seem to be available with a JST1.25 2pin connector. So you might need to solder a JST 1.25 2pin connector cable obtained separately to the buzzer leads. Additional work, and probably additional costs. This connects to the GPIO (P2) connector to pins IO9 and IO14.
  * A small 8Ohm / 1W speaker with a JST1.25 2pin connector.<br>This usually results in a slightly higher volume and a more pleasant sound. Getting one with the proper connector saves you some work. This connects directly to the "SPEAK" (P6) connector. If you have a DIY JST1.25 assortment, you can do a custom 8 pin connector that nicely fits P6. But a 2pin connector will do fine.

  
  Note: Take the available space into consideration. The passive buzzer is configured by default in the YAML. Switching to the speaker requires manually enabling / disabling some settings in the YAML.

* __Cable__<br>
  Any USB-C to USB-C / USB-A with data lines will do for charging and flashing the ESP32.


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
<img alt="In action 1" src="https://github.com/user-attachments/assets/2cc83a7c-75c3-4c01-b1db-8f422a5380da" width="265">
<img alt="In Action 2" src="https://github.com/user-attachments/assets/6baaa8af-9068-4675-aac9-c1b00c2df483" width="265">



## Acknowledgments
This project would not have been possible without the work of the community. Special thanks go to:

[JBecker32/G32-Display-480x320-BT](https://github.com/JBecker32/G32-Display-480x320-BT) (the original software project)

[fschwarz86/g32](https://github.com/fschwarz86/g32)

[ralmoe/g32-docker-client](https://github.com/ralmoe/g32-docker-client)

[MortenVinding/MEATER.yaml](https://gist.github.com/MortenVinding/a513c0094d0df41a4425612257b3cabc) (Meater® accuracy)

[so99hero/Standalone Case JC3248W535C](https://www.thingiverse.com/thing:7127557)


## Disclaimer
This is third-party software developed by the community and is not officially developed or supported by Otto Wilde GmbH. Use at your own risk.
