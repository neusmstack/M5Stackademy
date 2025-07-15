# 📦 Custom Blocks for UiFlow 2.0

This folder contains documentation and guidance for creating, editing, and uploading custom blocks for UiFlow 2.0. These blocks extend the functionality of M5Stack devices using Python code and a graphical interface.

---

## 🎯 Objective

Provide clear, organized resources for designing custom blocks with:

- Block Designer (M5Stack tool)
- Manual editing of `block.py` and `block.json`
- Compatibility with UiFlow 2.0 IDE

---

## 🧰 Requirements

- M5Stack device (e.g., Core2, Atom, StickC, etc.)
- M5Stack account and access to [UiFlow 2.0 IDE](https://uiflow2.m5stack.com/)
- Visual Studio Code or a text editor
- Basic knowledge of Python
- Internet connection (to use UiFlow IDE)

---

## 📂 Folder Structure

Each custom block should have its own folder, named according to the block’s function.

```plaintext
nom_del_bloc/
├── block.json      → Fitxer JSON amb la descripció del bloc (interfície i paràmetres)
├── block.py        → Fitxer amb el codi Python que s’executa quan es fa servir el bloc
├── icon.png        → Icona del bloc (mida recomanada: 40x40 px)

```

## 🛠️ Steps to Use a Custom Block in UiFlow 2.0
- Open UiFlow 2.0 IDE

- Go to "My Blocks" (blocs personalitzats)

- Click “Upload Block” or “Add from GitHub”

- Import the .m5b2 file or the folder containing block.py and block.json

- The block will now appear in the Custom category

## 🧪 Tips for Developing

- Use meaningful names and icons

- Always test blocks on the actual device

- Validate JSON syntax with online tools

- Keep block.py as simple and readable as possible

- Include examples and README.md files in each folder if sharing publicly

## 📜 License

This project is licensed under the terms of the  
**Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**.

You are free to:
- ✅ **Share** — copy and redistribute the material in any medium or format  
- ✅ **Adapt** — remix, transform, and build upon the material  
  as long as you follow the license terms:

### Conditions:
- 🧾 **Attribution** — You must give appropriate credit (Neus),  
  provide a link to the license, and indicate if changes were made.
- 🚫 **NonCommercial** — You may not use the material for commercial purposes.
- 🔁 **ShareAlike** — If you remix, transform, or build upon the material,  
  you must distribute your contributions under the same license.

🔗 [Read the full license](https://creativecommons.org/licenses/by-nc-sa/4.0/)

![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)

> 📦 This is part of the [neusmstack GitHub](https://github.com/neusmstack) educational projects.
