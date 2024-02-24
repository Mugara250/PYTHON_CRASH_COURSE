#!/usr/bin/python3

from pathlib import Path
import json
# # A program that stores information(a list of numbers) using json.dumps()

# # List of numbers to be stored
# numbers = [1, 2, 3, 4, 5, 6]

# path = Path('numbers.json')

# # json.dumps() converts the list into a JSON-formatted string and returns it.
# contents = json.dumps(numbers)

# # Write it to the numbers.json file i.e. store it
# path.write_text(contents)


# Another program can be written to read the contents of the numbers.json back into memory

path = Path('numbers.json')

# Read the file contents
contents = path.read_text()

# json.loads converts and returns our file contents as a Python list
numbers = json.loads(contents)
# Display the file contents
print(numbers)