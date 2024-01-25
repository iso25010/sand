# Python

import tkinter as tk
import tkinter.filedialog as fd
import pickle

# Create the root window
root = tk.Tk()

# Set the window size
root.geometry("400x300")

# Create a dictionary to store the entries
entries = {}

# Create Entry widgets for key and value input
key_entry = tk.Entry(root)
value_entry = tk.Entry(root)

# Position the Entry widgets in the same row and make them fill the width of the window
key_entry.grid(row=0, column=0, sticky='ew')
value_entry.grid(row=0, column=1, sticky='ew')

# Create Listbox widgets for displaying keys and values
keys_listbox = tk.Listbox(root)
values_listbox = tk.Listbox(root)

# Position the Listbox widgets below the Entry widgets
keys_listbox.grid(row=1, column=0, sticky='ew')
values_listbox.grid(row=1, column=1, sticky='ew')

# Function to update the dictionary and the Listbox widgets
def update_dict():
    # Get the key and value from the Entry widgets
    key = key_entry.get()
    value = value_entry.get()

    # Add the key and value to the dictionary
    entries[key] = value

    # Clear the Listbox widgets
    keys_listbox.delete(0, tk.END)
    values_listbox.delete(0, tk.END)

    # Add the keys and values to the Listbox widgets
    for key, value in entries.items():
        keys_listbox.insert(tk.END, key)
        values_listbox.insert(tk.END, value)

    # Clear the Entry widgets
    key_entry.delete(0, tk.END)
    value_entry.delete(0, tk.END)

    # Set the focus back to the key Entry widget
    key_entry.focus_set()

# Function to save the dictionary to a file
def save_dict():
    # Ask the user to choose a directory
    directory = fd.askdirectory()

    # If the user didn't cancel the dialog
    if directory:
        # Open a file in the chosen directory
        with open(f'{directory}/dictionary.pkl', 'wb') as f:
            # Save the dictionary to the file in pickle format
            pickle.dump(entries, f)

# Create Button widgets for updating the dictionary and saving the dictionary
update_button = tk.Button(root, text="Update", command=update_dict)
save_button = tk.Button(root, text="Save", command=save_dict)

# Position the Button widgets below the Listbox widgets
update_button.grid(row=2, column=0)
save_button.grid(row=2, column=1)

# Function to load the dictionary from a file
def load_dict():
    # Ask the user to choose a file
    file_path = fd.askopenfilename()

    # If the user didn't cancel the dialog
    if file_path:
        with open(file_path, 'rb') as f:
            global entries
            entries = pickle.load(f)
            update_listboxes()

# Create a Button widget for loading the dictionary
load_button = tk.Button(root, text="Load", command=load_dict)

# Position the Load button next to the Save button
load_button.grid(row=3, column=1, sticky='ew')

# Function to update the Listbox widgets with the keys and values of the dictionary
def update_listboxes():
    # Clear the Listbox widgets
    keys_listbox.delete(0, tk.END)
    values_listbox.delete(0, tk.END)

    # Add the keys and values to the Listbox widgets
    for key, value in entries.items():
        keys_listbox.insert(tk.END, key)
        values_listbox.insert(tk.END, value)

# Configure the grid to expand properly when the window is resized
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

# Start the application
root.mainloop()