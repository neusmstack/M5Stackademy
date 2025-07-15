# MAIN_README.md

# Generator of Solids of Revolution

This project explores the generation of solids of revolution from flat shapes using M5Stack technology. It evolves through three versions:

** Directory Generator of revolution solids
│
├── MAIN_README.md
├── Blocs
│   └── V0
│       └── Generator_of_Solids_of_Revolution.m5f2
├── images
│   ├── V0
│   ├── V1
│   └── V2


## 📦 Project Versions

### 🟡 Version 0 – Color Sensor Prototype (UIFlow 2.0)
- Uses a color sensor to identify shapes based on LEGO colors.
- Controlled via UIFlow 2.0 blocks.
- Generates basic solids visually.

➡️ See [`V0_ColorSensor/`](./V0_ColorSensor/)

---

### 🟠 Version 1 – RFID + Motor DC + Glass Display
- Uses RFID cards to identify shapes.
- Displays the UID, the shape, and the generated solid on a Glass Display.
- Activates a DC motor for physical solid generation.
- Communication between two Atom controllers using TCP/IP (client-server architecture).

➡️ See [`V1_RFID_Motor/`](./V1_RFID_Motor/)

---

### 🔸 Version 2 – RFID + Motor DC + 3D Fan (Coming Soon)
- Adds a 3D fan controlled by the server.
- Builds upon Version 1, adding physical visualization with airflow.

➡️ See [`V2_RFID_Motor_Fan/`](./V2_RFID_Motor_Fan/)

---

## 🎥 Demonstration Videos

- [▶️ Right Triangle generating a Cone](https://youtube.com/shorts/lGFexTR9pc4)
- [▶️ Circle generating a Sphere](https://www.youtube.com/shorts/_j-W3fwHpbI)

---

## 📸 Project Images

Each version includes its own set of images in its folder.

---

## 🔜 Upcoming Expansion

- **AlgebraLab**: Solving equations using a Rubik’s Cube as an interactive tool.

---

## 📙 Author

**Neus Morla Arias**  
📧 neusmstack@gmail.com

---
