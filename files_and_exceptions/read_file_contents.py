#!/usr/bin/python3

# Importing the Path object from pathlib library.
from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text().rstrip()
# # Printing the contents once by reading in the entire file.
# print(f"{contents}\n")

# Printing the contents once by storing the lines in a list and then looping over each line
for line in contents.splitlines():
    modified_line = line.replace('Python', 'C')
    print(modified_line)
        