file = open('user_info.txt', 'w')

info = input("Enter your name: ")

file.write(info)

file.close()
