import os
import shutil

# Path of folder to organize
folder_path = input("Enter folder path: ")

# File categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".doc", ".pptx", ".xlsx"],
    "Text": [".txt"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv", ".avi"]
}

# Check all files in folder
for file in os.listdir(folder_path):

    file_path = os.path.join(folder_path, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    moved = False

    for folder_name, extensions in file_types.items():

        for ext in extensions:

            if file.lower().endswith(ext):

                target_folder = os.path.join(folder_path, folder_name)

                # Create folder if not exists
                os.makedirs(target_folder, exist_ok=True)

                # Move file
                shutil.move(file_path,
                            os.path.join(target_folder, file))

                print(f"Moved {file} -> {folder_name}")

                moved = True
                break

        if moved:
            break

print("File organization completed!")
