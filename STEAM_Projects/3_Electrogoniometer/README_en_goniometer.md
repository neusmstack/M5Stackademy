
# Electrogoniometer with M5Stack

This project implements an **educational electrogoniometer** using the **M5Stack Fire** module, an IMU unit, a servo motor, a CardKB, and a laser module. It allows angle measurement and height calculation using trigonometric principles, with keyboard input and integrated screen display.

## Components used

- M5Stack Fire
- PAHUB Unit (SKU: U040)
- IMU Unit (SKU: U095)
- 8 Servos Unit (SKU: U165)
- SG90 Servo (connected to channel 7)
- CardKB Unit (mini keyboard)
- Mechanical activation laser module
- Integrated screen (M5Stack)

## Functionalities

- Angle calibration (pitch offset)
- Smooth arm movement using the servo
- Keyboard input for:
  - Distance measured with the laser
  - Height from ground to device base
- Ground height calculation:
  ```
  angle_radian = |angle_real| * π / 180
  calculated_height = length * sin(angle_radian)
  total_height = base_height + calculated_height
  ```
- Rounded values displayed (mm for heights, rad for angle)
- Clear, step-by-step user interface

## IMPORTANT WARNING ⚠️

A **critical inconsistency** has been detected in the operation of **UiFlow 2.0**:

> When **Custom mode (Python code editing)** is activated, the system **stops executing the visual block logic**, even though the blocks remain visible.

This can cause:

- Calculation inconsistencies (e.g., duplicated radian conversion)
- Outdated or incorrect visual data
- Loss of functionality programmed with blocks

**We recommend**:

1. Develop the full logic using blocks and verify its behavior
2. Only enable Custom mode at the end, for final adjustments
3. Review that the generated Python code does not duplicate operations already performed by the blocks

This warning will be formally documented and sent to M5Stack developers for evaluation and correction in future versions.

## Credit

Project by **Neus Morlà Arias**, designed for educational integration of trigonometry using M5Stack technology.

## Repository

[Full project on GitHub](https://github.com/neusmstack/goniometre-m5stack)



---

For more details, check the main code file `Electrogoniometre_Fix.py`.
