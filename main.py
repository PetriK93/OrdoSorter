import tkinter as tk
import customtkinter as ctk
from PIL import Image
import json
import os
from modules.select_folder import select_folder
from modules.organize_folder import organize_folder

SETTINGS_FILE = "settings.json"

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {"theme": "dark"}  # default if file missing or corrupt

def save_settings(settings):
    try:
        with open(SETTINGS_FILE, "w") as f:
            json.dump(settings, f, indent=4)
    except IOError:
        print("Warning: Could not save settings.")

# Load saved settings (theme)
settings = load_settings()
current_theme = settings.get("theme", "dark")
ctk.set_appearance_mode(current_theme.capitalize())

# Import images.
logo = "assets/logo_image.png"
dark_mode = "assets/dark_mode_icon.png"
light_mode = "assets/light_mode_icon.png"
folder = "assets/folder_image.png"
arrow = "assets/arrow_image.png"
organize = "assets/organize_image.png"

# Theme colors. Dark / Light.
dark_colors = {
    "background": "#0D1117",
    "button": "#00B5F0",
    "text": "white"
}

light_colors = {
    "background": "pink",
    "button": "white",
    "text": "black"
}

# Your selected folder.
selected_folder = None

def on_select_folder():
    global selected_folder
    # Pass the previous folder as initial_dir to start there
    selected_folder = select_folder(arrow_label, folder_label, selected_folder_label, selected_folder, initial_dir=selected_folder)
    
def on_organize_folder():
    if selected_folder:
        print(f"Organizing: {selected_folder}")
        organize_folder(selected_folder, organize_label)
    else:
        print("No folder selected!")
        
def change_theme():
    global current_theme

    # Toggle between modes
    if ctk.get_appearance_mode().lower() == "dark":
        ctk.set_appearance_mode("Light")
        current_theme = "light"
    else:
        ctk.set_appearance_mode("Dark")
        current_theme = "dark"

    # Save new theme
    settings["theme"] = current_theme
    save_settings(settings)

    # Pick colors for the new theme
    colors = dark_colors if current_theme == "dark" else light_colors

    # Apply background color
    app.configure(fg_color=colors["background"])

    # Apply text color from theme dictionary
    for label in (folder_label, selected_folder_label, organize_label):
        label.configure(text_color=colors["text"])


# Set colors based on the current color mode.
current_mode = ctk.get_appearance_mode()
colors = dark_colors if current_mode.lower() == "dark" else light_colors

# Create the main window.
app = ctk.CTk()
app.geometry("400x400")
app.title("OrdoSorter")
app.resizable(False, False)
app.configure(fg_color=colors["background"])

# Create images.
logo_image = ctk.CTkImage(
    light_image=Image.open(logo),
    dark_image=Image.open(logo),
    size=(150, 150)
)

color_mode_image = ctk.CTkImage(
    light_image=Image.open(light_mode),
    dark_image=Image.open(dark_mode),
    size=(35, 35)
)

folder_image = ctk.CTkImage(
    light_image=Image.open(folder),
    dark_image=Image.open(folder),
    size=(75, 75),
)

arrow_image = ctk.CTkImage(
    light_image=Image.open(arrow),
    dark_image=Image.open(arrow),
    size=(38, 38)
)

organize_image = ctk.CTkImage(
    light_image=Image.open(organize),
    dark_image=Image.open(organize),
    size=(75, 75)
)

# Widgets.
logo_label = ctk.CTkLabel(
    app,
    image=logo_image,
    text=""
)

color_mode_button = ctk.CTkButton(
    app,
    image=color_mode_image,
    text="",
    fg_color="transparent",
    hover="transparent",
    command=change_theme
)

folder_button = ctk.CTkButton(
    app,
    image=folder_image,
    text="",
    command=on_select_folder,
    fg_color="transparent"
)

folder_label = ctk.CTkLabel(
    app,
    text="Select folder",
    text_color=colors["text"],
    font=("Arial", 16)
)

selected_folder_label = ctk.CTkLabel(
    app,
    text="",
    text_color=colors["text"],
    font=("Arial", 11),
    wraplength=380
)

arrow_label = ctk.CTkLabel(
    app,
    image=arrow_image,
    text=""
)

organize_button = ctk.CTkButton(
    app,
    image=organize_image,
    text="",
    fg_color="transparent",
    command=on_organize_folder
)

organize_label = ctk.CTkLabel(
    app,
    text="Organize folder",
    text_color=colors["text"],
    font=("Arial", 16)
)

# Widget placement.
logo_label.place(relx=0.5, rely=0.25, anchor="center")
color_mode_button.place(relx=0.92, rely=0.08, anchor="center")
folder_button.place(relx=0.25, rely=0.7, anchor="center")
folder_label.place(relx=0.25, rely=0.83, anchor="center")
selected_folder_label.place(relx=0.5, rely=0.94, anchor="center")
organize_button.place(relx=0.75, rely=0.7, anchor="center")
organize_label.place(relx=0.75, rely=0.83, anchor="center")

# Make sure the buttons are always at the top layer.
folder_button.lift()
organize_button.lift()


app.mainloop()