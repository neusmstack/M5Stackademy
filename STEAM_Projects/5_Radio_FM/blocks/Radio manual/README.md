# FM Radio Manual Simple

Projecte: **Sintonitzador Manual de Ràdio FM amb M5Stack Fire**  
**Autora:** Neus Morla Arias  
**Contacte:** neusmstack@gmail.com  
**Empresa:** [www.m5stack.com](https://www.m5stack.com)

---

## 📻 Descripció del projecte

Aquesta versió permet controlar manualment la freqüència d’una ràdio FM (basada en el mòdul TEA5767) mitjançant el girador **Angle Unit**, mostrant el valor de la freqüència en una pantalla M5Stack Fire. El sistema és totalment estable i el so resultant és net.

---

## 🛠️ Requeriments

- **M5Stack Fire**
- **Angle Unit (Port B)**
- **TEA5767 (a través del PaHUB)**
- **PaHUB (Port A)**

---

## 🔌 Connexions

| Dispositiu  | Connexió             |
| ------------| -------------------- |
| Angle Unit  | Port B del Fire      |
| PaHUB       | Port A del Fire      |
| TEA5767     | Canal 0 del PaHUB    |

> **Nota:** El PaHUB és necessari per gestionar múltiples dispositius I2C.

---

## 📂 Fitxers del projecte

- **main.py** : codi principal del projecte.
- **FMRadioMem.py** (opcional): llibreria de gestió de memòria d'emissores (no essencial en mode manual simple).

---

## 🚀 Instruccions d’ús

1. **Carrega** els fitxers al dispositiu amb **Pymakr** o **UIFlow**.
2. **Engega** el M5Stack Fire.
3. **Gira** el control **Angle Unit** per variar la freqüència.
4. La freqüència actual s’indica a la pantalla.
5. El so de la ràdio s’ajusta en temps real.

---

## ⚙️ Configuració tècnica destacada

- Mida del pas de sintonia: **0.05 MHz**
- Rang de freqüències: **87.5 MHz a 108.0 MHz**
- Visualització amb **un decimal**.

---

## 📋 Notes addicionals

- El sistema funciona completament offline.
- No es guarden emissores (mode simple).
- Versió ideal per a demostracions ràpides.

---

## 📞 Suport

Per qualsevol dubte o consulta:

- **Autora:** Neus Morla Arias  
- **Email:** neusmstack@gmail.com  
- **Empresa:** [www.m5stack.com](https://www.m5stack.com)
