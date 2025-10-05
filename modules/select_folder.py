from tkinter import filedialog

def select_folder(arrow_label, folder_label, selected_folder_label, folder_path, initial_dir=None):
    """Open folder selection dialog and show arrow if folder is selected."""
    folder_path = filedialog.askdirectory(
    title="Select a folder to scan and reorganize.",
    initialdir=initial_dir
    )

    # If a folder is chosen, make the arrow visible and change the text.
    if folder_path:
        arrow_label.place(relx=0.5, rely=0.7, anchor="center")
        folder_label.configure(text="Folder selected ✅")
        selected_folder_label.configure(text=f"Folder: {folder_path}")
        print(f"Selected folder: {folder_path}")
    else:
        # Hide arrow and reset label if cancelled
        arrow_label.place_forget()
        selected_folder_label.configure(text="")
        folder_label.configure(text="Select folder")

    return folder_path
