# Write the code ↓ to read user's input.
# Be cautious when reading input of various data types.
print("PUP Enrollment form")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
average = float(input("Enter your previous general weighted average: "))
member = input("Are you a member of AWS cloud club? (yes/no): ").lower() == 'yes'

# Write the code ↓ to display the user's personal information.
print("\n")
print("Name: " + name)
print("Age: " + str(age)) 
print("Average: " + str(average))  
print("AWS cloud club member: " + ("yes" if member else "no"))  
# Select and employ a string concatenation method based on your personal preference and comfort level.





