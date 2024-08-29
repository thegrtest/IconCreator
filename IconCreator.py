import tkinter as tk
from tkinter import filedialog
from PIL import Image

def select_image_and_convert():
    # Create a Tkinter root window (it won't be shown)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open a file dialog for the user to select an image file
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )

    # If the user selects a file, proceed to convert it
    if file_path:
        # Open the selected image file
        img = Image.open(file_path)

        # Define the output .ico file path
        ico_path = filedialog.asksaveasfilename(
            title="Save as",
            defaultextension=".ico",
            filetypes=[("ICO Files", "*.ico")]
        )

        # Convert and save the image as an .ico file
        if ico_path:
            img.save(ico_path, format='ICO', sizes=[(256, 256)])
            print(f"Image successfully converted to: {ico_path}")
        else:
            print("Save operation was canceled.")
    else:
        print("No file selected.")

if __name__ == "__main__":
    select_image_and_convert()
