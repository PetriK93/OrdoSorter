from tkinter import filedialog

def select_folder():
    """Open folder selection and return the selected path."""
    folder_path = filedialog.askdirectory(title="Select a folder to scan and reorganize.")
    return folder_path