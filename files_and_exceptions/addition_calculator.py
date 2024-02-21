#!/usr/bin/python3

# Addition calculator
print("Add any two numbers of your choice.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond Number: ")
    if second_number == 'q':
        break
# Error Handling
    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print('Enter an integer value please instead of a string!')
    else:
        print(result)