# OrdoSorter

![Preview](https://github.com/user-attachments/assets/fc2705a9-05ce-4f64-b183-4d50144e1b6f)

## 📖 Introduction

OrdoSorter is a desktop tool built with Python for organizing files automatically.  
It scans a folder of your choice, categorizes files by type, and neatly places them into subfolders (e.g., Images, Videos, Documents).

The app also includes a clean dark/light mode interface with saved preferences so your theme choice persists between sessions.

---

## ✨ Features

🗂 Choose any folder to organize.

🔎 Automatically detect file types and categorize them.

📁 Create and place files into dedicated subfolders:

- Images
- Videos
- Text files
- And more…

🌗 Dark and light mode toggle with saved settings.

✅ Success and warning dialogs for guidance.

---

## 🚀 Installation

1. Clone the repository

   git clone https://github.com/PetriK93/OrdoSorter.git  
   cd OrdoSorter

2. Create a virtual environment (optional but recommended)

   python -m venv venv  
   source venv/bin/activate # On Linux / macOS  
   venv\Scripts\activate # On Windows

3. Install dependencies

   pip install customtkinter pillow

4. Run the app

   python main.py

   ***

## 💻 How to use the app

Choose a folder containing files you want to organize.

The app will scan and categorize files by type.

Subfolders are automatically created for each file type.

Files are moved into their corresponding folders.

Switch between dark and light mode — your choice is saved for next time! 🎉

---

## 📦 Dependencies

Python 3.12.10

os

tkinter

customtkinter

pillow

shutil

json

---

## 📝 License

This project is open source under the MIT License.
