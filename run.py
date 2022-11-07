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

def result(value): 
    if int(value) == range(1, 3): 
        print("cold")
    elif int(value) == range(3, 6): 
        print("warrior")
    else: 
        print("hottie")

# person = result(total)
# print(result)
    
    

