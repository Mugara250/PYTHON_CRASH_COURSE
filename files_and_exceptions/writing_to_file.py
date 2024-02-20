#!/usr/bin/python3

""" A program that prompts the user for their name and
writes it to a file called guest.txt once they input their name.
"""
from pathlib import Path
# guest = input("What is your name? ")
# path = Path('guest.txt')
# path.write_text(guest)

""" While loop that prompts users for their names, collects
names entered, and then writes these names to a file called guest_book.txt
"""
path = Path('guest_book.txt')

prompt = "\nHi, what is your name? "
prompt += "\nEnter 'quit' if you entered your name last."

guest_names = []

while True:
    name = input(prompt)
    if name == 'quit':
        break

    print(f"Thanks {name.title()}. We'll add you to the guest book.")
    guest_names.append(name)

# Build a string where "\n" is added after each name.
file_string = ''
for name in guest_names:
    file_string += f"{name.title()}\n"

path.write_text(file_string)    

