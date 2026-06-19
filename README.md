# CybdoClock!!

14 by 14 letter word clock / calendar / whatever, powered by esp32-c6!

<img width="2560" height="1440" alt="27 past 5" src="https://github.com/user-attachments/assets/0558c6f2-5239-46e9-8453-80313466b66c" />

Word clocks are arguably better and cooler than normal analog or digital clocks, but they are way too expensive comercially for a decent product, and even then there's not much customisation to it (the only one i could find was over 1000 dollars and could only show the time in 5 minute increments). CybdoClock was made to be able to show time down to the minute, in multiple formats, all while being customisable and allowing for different uses. The face plate can be swapped to show different languages or formats, and a calendar faceplate is coming soon!

# zine page
pdf at `./zine.pdf`
<img width="534" height="818" alt="image" src="https://github.com/user-attachments/assets/be40bba1-352e-4f5d-9d3c-d2c90453df65" />

# Features
- native wifi, bluetooth and matter over thread capabilities
- support for custom faceplates with an easy to update firmware dict
- NTP time sync via wifi
- wall-mountable via command strips
- stand included for desktop use

# Usage
- flash circuitpython 10 onto the ESP-32 via USB-C.
- Copy the firmware folder onto the CIRCUITPY drive, and create settings.toml using settings.toml.example.
- install all requirements in requirements.txt using `circup install -r requirements.txt`

CybdoClock will now turn on and sync to NTP once connected to a USB power source!

# Firmware
CybdoClock runs off CircuitPython 10.x, and code can be found under `./firmware/`

# Technical Documentation

CybdoClock is powered by a 14x14 LED matrix. NOTE: CybdoClock refreshes vertically, and defaults to left -> right. This is a hardware limitation, and overrides in firmware could cause permanent damage to components.

## Shift Registers

While the provided firmware uses the adafruit library and pins, a custom firmware can interface with the pins by sending the following serial data:



| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Row 14 | Row 13 | Row 12 | Row 11 | Row 10 | Row 9 | Row 8 | NC | Row 7 | Row 6 | Row 5 | Row 4 | Row 3 | Row 2 | Row 1 | NC | Col 14 | Col 13 | Col 12 | Col 11 | Col 10 | Col 9 | Col 8 | NC | Col 7 | Col 6 | Col 5 | Col 4 | Col 3 | Col 2 | Col 1 | NC |
## Schematics

Please note - the net labels for columns and rows do not reflect their physical layouts, nor does the layout of the matrix in the schematic
a pdf can be found at `./schematics.pdf`
<img width="1351" height="864" alt="image" src="https://github.com/user-attachments/assets/8d7649a5-bf39-45a2-81ce-b339dc9c71e9" />


## PCB
<img width="556" height="554" alt="image" src="https://github.com/user-attachments/assets/1ac996b9-7231-4dca-a0b5-96ceeca7c38d" />


# Acknowledgements
 - [KiCad](https://www.kicad.org)
 - [Hack Club Fallout](https://fallout.hackclub.com)
 - [pcb2blender](https://github.com/30350n/pcb2blender)
 - [Blender](https://blender.org)
 - [CircuitPython](https://circuitpython.org/)
