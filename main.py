import tkinter as tk
import customtkinter as ctk
from PIL import Image
from modules.select_folder import select_folder
from modules.organize_folder import organize_folder

# Set default appearance mode & color theme.
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Import images.
logo = "assets/logo_image.png"
folder = "assets/folder_image.png"
arrow = "assets/arrow_image2.png"
organize = "assets/organize_image2.png"

# Theme colors. Dark / Light.
dark_colors = {
    "background": "#0D1117",
    "button": "#00B5F0"
}

light_colors = {
    "background": "pink",
    "button": "white"
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
    text_color="white",
    font=("Arial", 16)
)

selected_folder_label = ctk.CTkLabel(
    app,
    text="",
    text_color="white",
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
    text_color="white",
    font=("Arial", 16)
)

# Widget placement.
logo_label.place(relx=0.5, rely=0.25, anchor="center")
folder_button.place(relx=0.25, rely=0.7, anchor="center")
folder_label.place(relx=0.25, rely=0.83, anchor="center")
selected_folder_label.place(relx=0.5, rely=0.94, anchor="center")
organize_button.place(relx=0.75, rely=0.7, anchor="center")
organize_label.place(relx=0.75, rely=0.83, anchor="center")

# Make sure the buttons are always at the top layer.
folder_button.lift()
organize_button.lift()


app.mainloop()