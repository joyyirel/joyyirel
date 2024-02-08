# Write the code ↓ to read user's input for two operands and selected operation.
# NOTE: The two operands must be read as floats.
print("Simple Calculator for Alf")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")





# Write the code ↓ to perform the calculations based on the selected operation.
result = None
if operator == '+':
    result = num1 + num2
if operator == '-':
    result = num1 - num2
if operator == '*':
    result = num1 * num2
if operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero!")
if result is None:
    print("Error: Invalid operator!")
# Write the code ↓ to display the result.
if result is not None:
    print(f"{num1} {operator} {num2} = {result}")
# Select and employ a string concatenation method based on your personal preference and comfort level.







