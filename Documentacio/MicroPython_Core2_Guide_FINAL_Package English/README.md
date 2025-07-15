# MicroPython on M5Stack Core2

This repository contains a complete step-by-step guide to install the official MicroPython firmware on the M5Stack Core2 device. It is intended for educators, students, and makers who want to work directly with Python using Thonny or another IDE.

## Files

- `Micropython Core2 Guide.pdf`: A detailed PDF tutorial on how to erase the flash and install MicroPython on the M5Stack Core2.
- `README.md`: This file.

## Summary of Steps

1. **Install `esptool.py`** using `pip install esptool`
2. **Identify the serial port** (e.g. `/dev/tty.usbserial-XXXXX`)
3. **Erase the flash** with `esptool.py`
4. **Download the latest MicroPython firmware** from [micropython.org](https://micropython.org/download/esp32/)
5. **Write the firmware** using `esptool.py write_flash`
6. **Open Thonny**, select the interpreter as *MicroPython (ESP32)*, and connect

## Requirements

- M5Stack Core2
- USB-C cable
- Mac with Python 3
- Thonny IDE or similar

## License

This guide is provided under the MIT License. Feel free to use, modify, and share it freely.
