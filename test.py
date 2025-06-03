import tkinter as tk
from tkinter import filedialog

def browse_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    root.update()
    root.destroy()
    if file_path:
        print("Selected file:", file_path)
    else:
        print("No file selected.")

if __name__ == "__main__":
    browse_image()
