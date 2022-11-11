def introduction(): 
    """ 
    Displays a little introduction, 
    build a string litteral and, 
    ask if the person would like to start the game
    """ 

    name = input("Enter your name:\n ")
    print(f"Hi there {name} welcome to our anger-personality-test\n")
    print("You will be asked a set of questions and your answer will need to be a number on the scale of 10")
    print("Make sure not to type in a number higher than 10 or your results will be inaccurate")
    print("If at any time you would like to start over just click the Run Program button above the terminal ")
    return name


def begin():
    """ 
    Asks the player if he/she wants to start the game
    """ 

    print("Are you ready to find out your angertype?")

    start = input(" y/n :")
    
    if start == "y": 
        print("Great well let's go\n")
    elif start == "n" : 
        print(" Thats too bad, if you cange your mind let us know!")
        main()
    else: 
        print("Oh Oh, that is not a valid input")
        begin()



def quizz(): 
    """ 
    The function that holds all questions, 
    also builds a list for score. 
    The loop will display the questions and answer input
    """
    score = []
    questions = ("When your friend annoys you, do you tell him/her?:",
     "When the waiter is rude, do you complain?", 
     "When the food comes out different than you ordered, will you send it back? ",
      "Do you get frustrated while driving?",
       "Would you tell the truth even when it will hurt? ",
       "When your employer tells you to be quiet, would you listen?",
       "When a customer is behaving like a spoiled brat, would you point this out? ",
       "Do you have arguments with your peers often? ")

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
    print(quest + " \n ") 
    print("Choose a number on a scale of 0 to 10.\n")

    
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
    Matches the score with right type, 
    print right anger-type
    """
    cool = "Wow it seems like you are as cool as icecream. Even though it is great to be in control nobody likes to relate to a statue/n Also your anger is the force for change, don't let it die!"
    warrior = "You seem to have a warrior like state of mind. You know when to loose your cool to address that what needs change.\n But you also know when to maintain your cool."
    hothead = "You are overheated most of the time, we could call you dynamite. Bring back the 10 sec count before expressing your anger!"
    off-the-chart = "Ooops, your score seems to be off the charts. Did you type in numbers higher than 10? Let's start all the way from the top!"
    print("\nCalculating your angertype.....\n")

    if int(number) <= 24: 
        return cool
    elif int(number) <= 56: 
        return warrior
    elif int(number) <= 81:
        return hothead
    else: 
        return off-the-chart 

def main(): 
    """ 
    Calls all the main functions for the game
    """

    user = introduction()
    begin()
    total_score= quizz()
    person = result(total_score)
    print(person)

main()

















    
    

