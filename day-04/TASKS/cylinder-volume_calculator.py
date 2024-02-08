import math

# Write the code ↓ to read the radius and height of a cylinder from the user.
# Be cautious when reading input of various data types.
print("Cylinder-Volume Calculator for ALF")
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))



# Write the code ↓ to calculate the volume of the cylinder using the formula V = πr^2h.
# Formula to calculate the volume (V) of a cylinder:
# V = π * r^2 * h
if radius < 0 or height < 0:
    print("Error: Please enter non-negative values for radius and height.")
else:
    volume = math.pi * radius ** 2 * height
  
# Write the code ↓ to display the calculated volume with 2 decimal places.
    print("The volume of the cylinder is {:.2f}".format(volume))
# Select and employ a string concatenation method based on your personal preference and comfort level.





