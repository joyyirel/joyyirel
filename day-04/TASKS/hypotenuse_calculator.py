import math

# Write the code ↓ to read the lengths of the two shorter sides of a right-angled triangle from the user.
# Be cautious when reading input of various data types.
print("Hypotenuse for ALF")

side1 = float(input("PLease, enter the length of the side A: "))
side2 = float(input("Please, enter the length of the side B: "))


# Write the code ↓ to calculate the hypotenuse using the Pythagorean theorem.
# The Pythagorean theorem: c^2 = a^2 + b^2, where c is the hypotenuse.
def calculate_hypotenuse(side1, side2):
    return math.sqrt(side1 ** 2 + side2 ** 2)




# Write the code ↓ to display the calculated hypotenuse.
# Select and employ a string concatenation method based on your personal preference and comfort level.
if side1 < 0 or side2 < 0:
    print("Error: Please enter non-negative value.")
else:
    hypotenuse = calculate_hypotenuse(side1, side2)
    print("The hypotenuse of right-angled triangle is {:.2f}".format(hypotenuse))





