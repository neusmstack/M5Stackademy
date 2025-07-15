
# V1/README.md

# V1 – Generator of Solids of Revolution (RFID + Motor DC + Glass Display)

## 🛠️ Overview

In this version, two M5Stack Atom controllers communicate over TCP/IP:

- **RFID reader** identifies flat shapes.
- **Glass Display** shows UID, shape, and generated solid.
- **DC Motor** rotates to generate physical solids.

## 📅 Hardware Setup

- **Client:**  
  - Controller: Atom S3R  
  - RFID Unit (U031-B)  
  - Motion Base V1.2 (A090-V12)

- **Server:**  
  - Controller: Atom S3R with CAM M12  
  - Glass Display Unit (U135)

## 📉 Communication

- WiFi TCP/IP (Client sends UID to Server).
- Server shows UID, shape, solid on Glass Display.
- Special RFID card triggers motor activation.

## 🎥 Demonstration Videos

- [▶️ Video: Triangle to Cone](https://youtube.com/shorts/lGFexTR9pc4)
- [▶️ Video: Circle to Sphere](https://www.youtube.com/shorts/_j-W3fwHpbI)

## 📸 Example Images

## 📌 Version V1: RFID + Motor + Glass Display

System using RFID cards, DC motor, and Glass display. Programmed with Python.

### System Overview:

- Client setup (Motion base + RFID reader):

![motion_base_client](../images/V1/motion_base_client_RFID_unit.jpg)

- Server display with Glass Unit:

![display_server](../images/V1/display_&_server.jpg)

### RFID Cards Detected:

| Circle | Right Triangle | Rectangle | Trapezoid |
|--------|----------------|-----------|-----------|
| ![circle](../images/V1/RFID_CARD_circle.jpg) | ![triangle](../images/V1/RFID_CARD_right_triangle.jpg) | ![rectangle](../images/V1/RFID_CARD_rectangle.jpg) | ![trapezoid](../images/V1/RFID_CARD_trapezoid.jpg) |

### Generated Shapes (example):

- Generator process:

![generator](../images/V1/Generator.jpg)


![Glass Display](./Images/V1/display.jpg)  
![Motor Action](./Images/V1/motor.jpg)

## 📙 Author

**Neus Morla Arias**  
📧 neusmstack@gmail.com

---
