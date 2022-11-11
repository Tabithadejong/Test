
def quizz(): 
    """ 
    The function that holds all questions, 
    plus builds a list for score. 
    """
    score = []
    questions = ("Q1", " Q2", " Q3", " Q4", " Q5",)

    for q in questions: 
        value = get_answer(q)
        score.append(value) 

    total = sum(score)
    return total 

def get_answer(quest): 

    """ 
    Checks the input to be a number, 
    if not raise a type error and if correct,
    returns the number
    """
    print(quest) 
    print("Choose a number on a scale of 1 to 10.\n")

    
    while True:
        try:
            answer = int(input("1 = Never and 10 = Always:\n"))
        except ValueError:
            print("\nWhat you have entered is not a valid number.\n ")  
            print("Make sure your number is between 1 and 10 otherwise your results will be off the charts.")
            print("Try again.")
        else: 
            return answer 
      


def result(number): 
    """ 
    Calculate the total score, 
    print right anger-type
    """
    cool = "The coolest"
    warrior = "Neutral"
    hothead = "angry"

    print("Calculating your angertype.....")

    if int(number) <= 10: 
        return cool
    elif int(number) <= 17: 
        return warrior
    else: 
        return hothead

def main(): 
    """ 
    Calls all the main functions for the game
    """

    total_score= quizz()
    person = result(total_score)
    print(person)

main()





#def story(): 

"""
Make a story with user input
""" 

    #name= input("Type a name:")
    #object = input("type an object: ")
    #day = input("type a day")

    #print(f"when {name} was picking up an {object} just because it was {day}")









    
    

