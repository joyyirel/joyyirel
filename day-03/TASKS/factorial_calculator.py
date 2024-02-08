# Write the code ↓ to read the user's input for a non-negative integer.
# Be cautious when reading input of various data types.
print("Factorial Calculator for ALF")
num = int(input("Please, enter a non-negative integer: "))




# Write the code ↓ to calculate the factorial of the user-defined integer using a loop.
if num < 0:
    print("Error: Please enter a non-negative integer.")
else:
    result = 1
    for i in range(1, num + 1):
        result *= i


# Write the code ↓ to display the factorial result.
    print("The factorial of", num, "is:", result)
# Select and employ a string concatenation method based on your personal preference and comfort level.





