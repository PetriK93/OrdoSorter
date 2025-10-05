from tkinter import filedialog

def select_folder(arrow_label, folder_label, initial_dir=None):
    """Open folder selection dialog and show arrow if folder is selected."""
    folder_path = filedialog.askdirectory(
        title="Select a folder to scan and reorganize.",
        initialdir=initial_dir
    )

    if folder_path:
        # Show the arrow
        arrow_label.place(relx=0.5, rely=0.7, anchor="center")
        # Update label text
        folder_label.configure(text="Folder selected ✅")
        print(f"Selected folder: {folder_path}")
    else:
        # Hide arrow and reset label if cancelled
        arrow_label.place_forget()
        folder_label.configure(text="Select folder")

    return folder_path
