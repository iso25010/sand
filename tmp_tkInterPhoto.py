# Python

import tkinter as tk
from tkinter import filedialog, PhotoImage

# Create the root window
root = tk.Tk()

# Create a Label widget to display the picture
picture_label = tk.Label(root)
picture_label.pack()

# Function to load a picture
def load_picture():
    # Ask the user to choose a picture
    file_path = filedialog.askopenfilename(filetypes=[('Image Files *.gif;*.pgm;*.ppm;*.png', '*.*')])

    # If the user didn't cancel the dialog
    if file_path:
        # Load the picture and set it as the image of the Label widget
        photo = PhotoImage(file=file_path)
        picture_label.config(image=photo)
        picture_label.image = photo  # Keep a reference to the image to prevent it from being garbage collected

# Create a Button widget to load a picture
load_button = tk.Button(root, text="Load a picture", command=load_picture)
load_button.pack()

# Start the application
root.mainloop()