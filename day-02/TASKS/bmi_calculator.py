# BMI - NUTRITIONAL STATUS GUIDE
"""
    BMI         NUTRITIONAL STATUS

BELOW 18.5         UNDERWEIGHT
18.5 - 24.9       NORMAL WEIGHT
25.0 - 29.9        OVERWEIGHT
ABOVE 30.0          OBESITY
"""
 
# Write the code ↓ to read user's height and weight.
# Be cautious when reading input of various data types.
print("BMI Calculator for ALF")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Write the code ↓ to perform the calculations of user's BMI and categorize its status.
bmi = weight / (height ** 2)

status = None
if bmi < 18.5:
    status = "Underweight"
if 18.5 <= bmi <= 24.9:
    status = "Normal weight"
if 25.0 <= bmi <= 29.9:
    status = "Overweight"
if bmi >= 30.0:
    status = "Obesity"

# Write the code ↓ to display the user's BMI and its classification.
print("Height: {:.2f}".format(height))
print("Weight: {:.2f}".format(weight))
print("BMI: {:.2f}".format(bmi))
print("Nutritional Status:", status)
# Select and employ a string concatenation method based on your personal preference and comfort level.
# Use :.2f format specifier when printing the BMI value to display the BMI with only two decimal places.







