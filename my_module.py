def reverse_text(text):
    return text[::-1]


text_to_reverse = input("Enter text to be reverse: ")
reversed_text = reverse_text(text_to_reverse)

print(f"Here is the text reversed {reversed_text}!")

import re
def is_valid_number(number):
    pattern = r'^-?\d+(\.\d+)?$'
    return re.match(pattern, number) is not None

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = input("Enter first number: ")
        # check for valid input
        while not is_valid_number(num1):
            print("Please enter numbers only")
            num1 = input("Enter first number: ")
        num1 = float(num1)

        num2 = input("Enter second number: ")
        # check for valid input
        while not is_valid_number(num2):
            print("Please enter numbers only")
            num2 = input("Enter second number: ")
        num2 = float(num2)

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")

    elif choice == 'quit':
        return

    else:
        print("Invalid choice")
        calculator()

if __name__ == "__main__":
    calculator()
