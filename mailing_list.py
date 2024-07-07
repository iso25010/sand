import tkinter as tk
from tkinter import filedialog
from pathlib import Path

# Function to open a CSV file using a file dialog
def open_csv_file():
	# Create a root window and hide it
	root = tk.Tk()
	root.withdraw()

	# Show an open file dialog and get the selected file path
	file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

	# Check if a file was selected
	if file_path:
		# Use the Path class to open the file
		path = Path(file_path)
		with path.open(encoding='utf-8') as file:
			# Read the content of the file
			content = file.read()
			return content


def read_txt_file(content):
          # the entities in the list are separated by a semicolon
    entities = content.split(";")
    print(entities)
      
    # Create a new list to store the first and last names
    first_last_names = [split_string(entity) for entity in entities]

    print(first_last_names)
    return first_last_names




# Function to slipt a string into two parts and return the first part
# The parts are separated by a left square bracket 
def split_string(string):
    # Split the string into two parts
    parts = string.split("[")
    first_last_name = parts[0]
    # Remove the last space character 
    first_last_name = first_last_name[:-1]
    # Return the first part
    return first_last_name
	
def write_txt_file(entities):
    # Create a new file to write the entities
    with open("mailing_list.txt", "w", encoding='utf-8') as file:
        # Write each entity to the file in one line
        for entity in entities:
            if entity:
                  file.write(entity+';')
		
	

# Call the function to open a CSV file
content=open_csv_file()
entities=  read_txt_file(content)
write_txt_file(entities)


