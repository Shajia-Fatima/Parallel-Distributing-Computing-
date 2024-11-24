# calculator.py

def perform_operation(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid Operation."

while True:
    try:
        # Input numbers and operation
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter operation (+, -, *, /): ")

        # Perform calculation
        result = perform_operation(num1, num2, operator)

        # Display the result
        print("Result:", result)
    except ValueError:
        print("Error: Invalid input. Please enter numerical values.")

    # Ask if the user wants to continue
    repeat = input("Do you want to perform another calculation? (yes/no): ").lower()
    if repeat != 'yes':
        print("Goodbye!")
        break
