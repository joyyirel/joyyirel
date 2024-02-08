import json

name = input("Enter your name: ")
age = input("Enter your age: ")
favorite_food = input("Enter your favorite food: ")

user_data = {
    "name": name,
    "age": age,
    "favorite_food": favorite_food
}

with open("output.json", "w") as file:
    json.dump(user_data, file)

print("Data saved to 'output.json'")
