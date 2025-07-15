# ➿ Line Following Robot Projects

This folder contains two line-following robot programs created with UiFlow 2.0, using the M5Stack system and infrared reflective sensors. One version includes an ultrasonic sensor for obstacle detection.

## 📁 Contents

- `line_follower_closed_loop.m5f2`: Line-following robot for a closed-loop track (no start or end).  
  No ultrasonic sensor is used in this version.

- `line_follower_with_goal_ultrasonic.m5f2`: Line-following robot that follows a path with a defined start and end.  
  Includes an ultrasonic sensor to detect obstacles and stop the robot accordingly.

## 🎯 Objective

Introduce students to basic robotics and logical control by building a robot capable of following a line using IR sensors, with optional obstacle detection.

## 🧰 Requirements

**Hardware:**

- M5Stack Core2  
- 2× M5Stack IR Reflective Sensors  
- M5Stack GoPlus2 module  
- M5Stack Bottom2 base  
- PbHUB Unit  
- ExtPort for Core2  
- Magnetic charger  
- (Optional) M5Stack Ultrasonic Sensor (GPIO version)

**Software:**

- UiFlow 2.0  
- `.m5f2` files to be loaded via the UiFlow IDE

## 🧪 Instructions

1. Build the robot using the M5Stack components and connect sensors as follows:
   - IR Sensors via PbHUB to ports 0 and 1
   - (Optional) Ultrasonic Sensor to port 4
2. Upload one of the two `.m5f2` programs depending on your circuit.
3. Run and observe the robot's behavior:
   - In the closed loop version, it will follow continuously.
   - In the version with start and end, it will stop at the end or when an obstacle is detected.

## 📜 License

This project is licensed under the terms of the  
**Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**.

🔗 [Read the full license](https://creativecommons.org/licenses/by-nc-sa/4.0/)

![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)
