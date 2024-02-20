#!/usr/bin/python3

# The following program reads contents in a file.

# We need to import the Path object from the pathlib module.
from pathlib import Path

# We build a Path object(instance) representing pi_digits.txt file
path = Path('pi_million_digits.txt')

# We call the read_text() method to read the entire contents of the pi_digits.txt file.
contents = path.read_text().rstrip() # method chaining
# print(contents)
# # We can split a long string into a set of lines using the splitlines() method
# lines = contents.splitlines()

# We can now start modifying our text file after reading it into memory.
pi_string = '' # this will be a long string of our file's contents without a whitespace
for line in contents.splitlines():
    pi_string += line.lstrip()

# Checking if your birthday appears anywhere in the digits of pi.
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi.")
else:
    print("Your birthday does not appear in the first million digits of pi.")