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

total = sum(score)
print(total)

def result(number): 

    result = int(number)

    if result <= 10: 
        print("yes")
    elif result <= 17: 
        print("no")
    else: 
        print("maybe baby")

    """
    if int(number) >= 1 and int(number) >= 10: 
        print("cold")
    elif int(number) >= 10 and int(number) >= 20: 
        print("warrior")
    else: 
        print("hottie")

    """

person = result(total)
print(result)
    
    

