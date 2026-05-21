# MY-first-hackpad ⌨️

My first ever custom-designed macropad! This is a 5-key mechanical keyboard designed from scratch for various programmable inputs. 

I am totally new to the world of hardware innovation and custom keyboards, and designed this entire casing, PCB, and 3D model using my trusty potato PC. It was tiring, but this repository contains all the necessary production files, CAD models, and PCB schematics for anyone who wants to build one too.

## 🛠️ Features
* **5-Key Layout:** Perfect for custom shortcuts, media controls, or gaming macros.
* **Custom 3D Printed Enclosure:** A two-part case (Base and Top Plate) designed in Fusion 360, featuring a sleek side-profile USB-C pass-through.
* **Custom PCB:** Designed in KiCad to perfectly fit standard mechanical switches and through-hole LEDs.

## 📦 Bill of Materials (BOM)
To build this exact macropad, you will need the following hardware:

**Core Electronics:**
* 1x Seeed Studio XIAO RP2040 Microcontroller
* 5x MX-Compatible Mechanical Switches (e.g., Redragon Linear Reds)
* 2x 3mm standard through-hole LEDs
* 2x 220Ω (or 240Ω) 1/4W through-hole resistors
* 1x Custom PCB (Order using the provided KiCad files)

**Hardware & Enclosure:**
* 1x 3D Printed Bottom Case (PLA/PETG)
* 1x 3D Printed Top Cover (PLA/PETG)
* 4x M2 Machine Screws (4mm - 5mm length)
* 5x 1u Mechanical Keycaps
* 1x USB-C Data Cable

## 📂 Repository Contents
* `/macropad - design.f3d` - The master editable Fusion 360 CAD file.
* `/macropad_backcover.3mf` - The 3D printable base enclosure.
* `/macropad_top_cover.3mf` - The 3D printable top switch plate.
* `macropad.kicad_*` - The raw KiCad schematic and PCB layout files.

## 🚀 Next Steps (Firmware)
*Working on the RP2040 code to map the keys to specific macros!*
