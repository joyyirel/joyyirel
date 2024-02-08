# Write the code ↓ to read the user's input for a positive integer.
# Be cautious when reading input of various data types.
print("Perfect Number Determinator for ALF")
num = int(input("Please, enter a non-negative integer: "))








# Write the code ↓ to check if the entered integer is a Perfect Number using a loop.
if num < 0:
    print("Error: Please enter a non-negative integer.")
else:
    result = 1
    for i in range(1, num + 1):
        result *= i
    
    print("The factorial of", num, "is:", result)
    divisor_sum = 0
    for i in range(1, result):
        if result % i == 0:
            divisor_sum += i


# Write the code ↓ to display the Perfect Number check result.
    if divisor_sum == result:
        print("The factorial of", num, "is a perfect number.")
    else:
        print("The factorial of", num, "is not a perfect number.")
# NOTE : You can use if-else statement or ternary operator to display the result.






