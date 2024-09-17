import exiftool
import subprocess
import tkinter as tk
from tkinter import filedialog


def get_exif_data(file_path):

    exiftool_path = r"C:\ExifTool\exiftool.exe"
    try:

        command = [
            exiftool_path,
            '-EXIF:DateTimeOriginal',
            '-EXIF:CreateDate',
            '-XMP:CameraModel',
            '-EXIF:Artist',
            '-EXIF:Copyright',
            file_path
        ]
        print(f"Running command: {' '.join(command)}")  # Log the command for debugging

        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        print(f"Command output:\n{result.stdout}")
        if result.stderr:
            print(f"Command error:\n{result.stderr}")


        metadata = result.stdout.split('\n')
        metadata_dict = {}

        for line in metadata:
            if line.strip():
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata_dict[key.strip()] = value.strip()

        return metadata_dict

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def select_files_and_extract_metadata():
    """Open a file dialog to select image files and print their metadata."""
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(
        title="Select Image Files",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif *.bmp *.tiff")]
    )

    if not file_paths:
        print("No files selected.")
        return

    for file_path in file_paths:
        file_name = file_path.split('/')[-1]
        metadata = get_exif_data(file_path)

        if metadata:
            print(f"\n/{file_name}:")
            print(f"  EXIF:DateTimeOriginal: {metadata.get('Date/Time Original', 'N/A')}")
            print(f"  EXIF:CreateDate: {metadata.get('Create Date', 'N/A')}")
            print(f"  XMP:CameraModel: {metadata.get('Camera Model', 'N/A')}")
            print(f"  EXIF:Artist: {metadata.get('Artist', 'N/A')}")
            print(f"  EXIF:Copyright: {metadata.get('Copyright', 'N/A')}")
        else:
            print(f"No metadata found for {file_name}")


if __name__ == "__main__":
    select_files_and_extract_metadata()
