score =[]

print("Question 1:")
while True:
    try:
        answer1 = int(input("Enter your first number:\n"))
    except ValueError:
        print("\nWhat you have entered is not a valid number, try again.")
    else:
        if answer1 <= 10:
            score.append(answer1)
        else: 
            raise ValueError("Input needs to be under 10")   
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

print("Question3") 

while True:
    answer3 = int(input("type here:"))
    if answer3 >= 11 : 
        raise ValueError("number must be under 10:")
    else: 
        print("well done:")
        

score.append(answer3)

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


person = result(total)
print(result)


def ask_for_contact(): 
    """ 
    Ask for personal contact details, 
    and push them to a sheet 
    """

    print("would you like to recieve news on angermanagement training? leave us your details.")
    input("yes/no")
    name = input("Your Name is: ")
    phone= input("Your phone number is:")
    mail = input("email is:")
    print(f"Thank you {name} we will ring you soon at {phone}")

ask_for_contact()






    
    

