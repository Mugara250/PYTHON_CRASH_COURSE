#!/usr/bin/python3

from name_function import get_formatted_name

print("Enter 'q' to quit.")
while True:
    first = input("\nEnter your first name please: ")
    if first == 'q':
        break
    last = input("Enter your last name please: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\n\tNeatly formatted name: {formatted_name}")