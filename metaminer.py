import exiftool
import tkinter as tk
from tkinter import filedialog
import json


def metaminer(image_path):

    exiftool_path = r"C:\ExifTool\exiftool.exe"
    with exiftool.ExifTool(executable=exiftool_path) as et:
        metadata_json = et.execute("-j", image_path)
        metadata = json.loads(metadata_json)[0]
    return metadata


def upload_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select an image file",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.tiff;*.bmp;*.gif")])

    if not file_path:
        print("No file selected")
        return

    metadata = metaminer(file_path)

    for tag, value in metadata.items():
        print(f"{tag}: {value}")


if __name__ == "__main__":
    upload_image()
