import os
import shutil
from tkinter import messagebox

def organize_folder(selected_folder, organize_label):
    """Define file type categories and organize them into their
    own subfolders."""
    
    # Ask for confirmation
    confirm = messagebox.askyesno(
        "Confirm Organize",
        f"Are you sure you want to organize all files in:\n{selected_folder}?"
    )
    if not confirm:
        organize_label.configure(text="Organization cancelled ❌")
        return
    
    categories = {
        "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
        "Text Files": [".txt", ".doc", ".docx", ".rtf"],
        "PDFs": [".pdf"],
        "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a"]
    }

    # Make sure the folder exists
    if not os.path.exists(selected_folder):
        print(f"The folder '{selected_folder}' does not exist.")
        return

    # Loop through all files in the folder
    for filename in os.listdir(selected_folder):
        file_path = os.path.join(selected_folder, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get the file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        # Find the appropriate category
        moved = False
        for category, extensions in categories.items():
            if ext in extensions:
                category_folder = os.path.join(selected_folder, category)
                
                # Create category folder if it doesn't exist
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                
                # Move file to category folder
                shutil.move(file_path, os.path.join(category_folder, filename))
                moved = True
                break
        
        # Uncategorized files are moved into the "Others" folder.
        if not moved:
            others_folder = os.path.join(selected_folder, "Others")
            if not os.path.exists(others_folder):
                os.makedirs(others_folder)
            shutil.move(file_path, os.path.join(others_folder, filename))
            
    # Update the label text.
    organize_label.configure(text="Folder organized ✅")
    print(f"Files in '{selected_folder}' have been organized.")
