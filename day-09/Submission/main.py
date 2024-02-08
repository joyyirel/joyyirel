with open("story.txt", "r") as file:
    lines = file.readlines()
    
    numlines = len(lines)
    
    print("Number of lines in 'story.txt':", numlines)
