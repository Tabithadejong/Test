def introduction(): 
    """ 
    Displays a little introduction, 
    build a string litteral and, 
    ask if the person would like to start the game
    """ 

    name = input("Enter your name: ")
    print(f" Hi there {name} welcome to our anger-personality-test\n")
    print("You will be asked a set of questions and your answer will need to be a number on the scale of 10")
    print("Make sure not to type in a number higher than 10 or your results will be inaccurate")
    print("If at any time you would like to start over just click the Run Program button above the terminal ")
    begin()


def begin():
    """ 
    Asks the player if he/she wants to start the game
    """ 

    print("Are you ready to find out your angertype?")

    start = input(" y/n :")
    
    if start == "y": 
        print("Great well let's go\n")
        total_score= quizz()
    elif start == "n" : 
        print(" Thats too bad, if you cange your mind let us know!")
    else: 
        print("Oh Oh, that is not a valid input")
        begin()



def quizz(): 
    """ 
    The function that holds all questions, 
    plus builds a list for score. 
    """
    score = []
    questions = ("When your friend annoys you, do you tell him/her?:",
     " Q2", " Q3", " Q4", " Q5",)

    for q in questions: 
        value = get_answer(q)
        score.append(value) 

    total = sum(score)
    return total 

def get_answer(quest): 

    """ 
    Prints the question.
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

    introduction()
    person = result(total_score)
    print(person)

main()

















    
    

