score =[]

print("Question 1:")
while True:
    try:
        answer1 = float(input("Enter your first number:\n"))
    except ValueError:
        print("\nWhat you have entered is not a valid number, try again.")
    else:
        score.append(answer1)
        break 
print("Question 2:")
while True:
    try:
        answer2 = float(input("Enter your first number:\n"))
    except ValueError:
        print("\nWhat you have entered is not a valid number, try again.")
    else:
        score.append(answer2)
        break 

print(score)   

