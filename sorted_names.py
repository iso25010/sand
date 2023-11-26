# Python

# List of names
names = ['Karel', 'Petr', 'Jana', 'Honza', 'Zuzka', 'Pavel', 'Jirka', 'Klara', 'Ondra', 'Eva']

# Print the list of names with their lengths
print([[name, len(name)] for name in names])

# Sort the names by their lengths and print the sorted list
sorted_names = sorted(names, key=len)
print(sorted_names)