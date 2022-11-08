
def quizz(): 
    """ 
    The function that holds all questions, 
    keeps track of score
    """
    score = []

    print("When your partner would lie to you would you be angry?:")
    while True:
        try:
            answer1 = int(input("Put in a number between 1=Never and 10=Always:\n"))
        except ValueError:
            print("\nWhat you have entered is not a valid number, try again.")
        else:
            score.append(answer1) 
            break 
    print("Question 2:")
    while True:
        try:
            answer2 = float(input("Put in a number between 1=Never and 10=Always:\n"))
        except ValueError:
            print("\nWhat you have entered is not a valid number, try again.")
        else:
            score.append(answer2)
            break 

    total = sum(score)
    print(total) 
        


def result(number): 
    """ 
    Calculate the total score, 
    print right anger-type
    """

    result = float((number))

    if result <= 10: 
        print("yes")
    elif result <= 17: 
        print("no")
    else: 
        print("maybe baby")


total_score= quizz()
person = result(total_score)
print(person)




#def story(): 

"""
Make a story with user input
""" 

    #name= input("Type a name:")
    #object = input("type an object: ")
    #day = input("type a day")

    #print(f"when {name} was picking up an {object} just because it was {day}")









    
    

