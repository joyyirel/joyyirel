# Write the code ↓ to prompt the user to enter a word.
# Be cautious when reading input of various data types.
print("Vowel Counter for ALF")

string = input("Enter a string: ")





# Write the code ↓ to count the number of vowels in the entered word.
# Utilize string functions to iterate through the characters and identify vowels.
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count
# Write the code ↓ to display the count of vowels in the word.
# Select and employ a string concatenation method based on your personal preference and comfort level.
num_vowels = count_vowels(string)
print("Number of vowels in the string '{}': {}".format(string, num_vowels))        





