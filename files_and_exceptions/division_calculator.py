#!/usr/bin/python3

# Calculator
print("\nGive me two numbers and I'll divide them.")
print("\nEnter 'q' to quit.")
while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break

    second_number = input("\nSecond Number: ")
    if second_number == 'q':
        break
    
    # Handling the ZeroDivisionError exception
    try:
        result = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can not divide by zero!")
    else:
        print(result)