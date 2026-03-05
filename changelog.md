# Changelog
* [2026-03-05] BTpref-retro 2.4.10
   - rollback of some core pinning that introduced weird behavior
* [2026-02-20] BTpref-retro 2.4.9
   - updated compatibility to esphome 2026.2.0
   - add small icon if countdown timer is enabled or active
* [2026-02-16] BTpref-retro 2.4.8
   - release should now contain yaml artifacts for buzzer / speaker
   - fix: silence warning sign in the first seconds after boot
* [2026-02-07] BTpref-retro 2.4.7
   - removed ntp servers altogether (thanks @JBecker32, and @fschwarz86 for pointing that out)
   - bugfix: color schemes with dedicated color for icon and text shadows
   - new color scheme "white (clean)" that demonstrates setting the icon and text shadows to black
* [2026-02-02] BTpref-retro 2.4.6
   - new alerts if Meater reading exceeds specification (tip: 100°C, ambient: 275°C)
   - color themes now have a dedicated color for shadows of symbols and text
   - all shadows of symbols and text can be forced to black by using a new substitution FORCE_SHADOW_COLOR_TO_BLACK
* [2026-02-01] BTpref-retro 2.4.5
   - hotfix: switch sntp servers for getting the accurate daytime
* [2026-01-29] BTpref-retro 2.4.4
   - bugfix: solo Meater reports 0 instead of the probe ID
* [2026-01-28] BTpref-retro 2.4.3
   - option to hide gas buddy readings
* [2026-01-28] BTpref-retro 2.4.2
   - minor UI tweaks and possibly performance inprovements
* [2026-01-21] BTpref-retro 2.4.1
   - configuration to make use of the speaker header and the external DAC for nicer and slightly louder audio
* [2026-01-11] BTpref-retro 2.4.0
   - reduced UI with increased temperature font size if temperature alarms are disabled
   - new option in settings: "dynamic temp. warning info"
     will automatically switch between old UI and reduced UI depending on if a temperature alarm was configured (disabled by default).
   - bugfix: scanning for meater probes does not reset all mac addresses any more
* [2025-12-19] BTpref-retro 2.3.3
   - gas level indicator bar segmentation now makes sense
* [2025-12-14] BTpref-retro 2.3.2
   - more color schemes
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
