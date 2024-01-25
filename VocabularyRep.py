# Python
import tkinter as tk
import tkinter.filedialog as fd
import pickle




# Create the root window
root = tk.Tk()

# Set the window size
root.geometry("800x400")

# Create a dictionary to store the entries
entries = {}

# Create two Entry widgets
key_entry = tk.Entry(root)
value_entry = tk.Entry(root)


# Position the Entry widgets in the same row and make them fill the width of the window
key_entry.grid(row=0, column=0, sticky='ew')
value_entry.grid(row=0, column=1, sticky='ew')

# Function to update the dictionary
def update_dict():
    key = key_entry.get()
    value = value_entry.get()
    entries[key] = value

    # Update the Listbox widgets with the keys and values of the dictionary
    keys_listbox.delete(0, tk.END)
    values_listbox.delete(0, tk.END)
    for key, value in entries.items():
        keys_listbox.insert(tk.END, key)
        values_listbox.insert(tk.END, value)

    # Clear the entry fields
    key_entry.delete(0, tk.END)
    value_entry.delete(0, tk.END)

    # Set the focus back to the first entry field
    key_entry.focus_set()

# Function to save the dictionary to a file
def save_dict():
    # Ask the user to choose a directory
    directory = fd.askdirectory()

    # If the user didn't cancel the dialog
    if directory:
        with open(f'{directory}/dictionary.pkl', 'wb') as f:
            pickle.dump(entries, f)


# Create a Button widget
commit_button = tk.Button(root, text="Commit", command=update_dict)

# Position the Button widget below the Entry widgets
commit_button.grid(row=1, column=0, columnspan=2)

# Create two Listbox widgets
keys_listbox = tk.Listbox(root)
values_listbox = tk.Listbox(root)

# Position the Listbox widgets below the Button widget
keys_listbox.grid(row=3, column=0, sticky='ew')
values_listbox.grid(row=3, column=1, sticky='ew')


# Create a Button widget for saving the dictionary
save_button = tk.Button(root, text="Save", command=save_dict)

# Position the Save button next to the Commit button
save_button.grid(row=1, column=2)

# Configure the grid to expand properly when the window is resized
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)


# Start the application
root.mainloop()