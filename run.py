import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("anger-test-results")



def introduction(): 
    """ 
    Displays a little introduction, 
    build a string litteral and, 
    ask if the person would like to start the game
    """ 

    name = input("Enter your name:\n ")
    print(f"Hi there [bold purple]{name}[/], welcome to our [bold orange3]Anger-Personality-Test[/]\n")
    print("You will be asked a set of questions and your answer will need to be a number on the scale of 10")
    print("If at any time you would like to [red1]exit[/], just press [red1]q[/]")
    return name


def begin():
    """ 
    Asks the player if he/she wants to start the game
    """ 

    print("Are you ready to find out your [bold orange3]ANGER TYPE?[/]")

    start = input("y/n :\n")
    
    if start == "y": 
        print("Great well let's go\n")
    elif start == "n" : 
        print("Thats too bad, if you cange your mind let us know!")
        main()
    else: 
        print("[white on red]Oh Oh, that is not a valid input[/]")
        begin()



def quizz(): 
    """ 
    The function that holds all questions, 
    also builds a list for score. 
    The loop will display the questions and answer input
    """
    score = []
    questions = ("[bold black on light_salmon1] When your friend annoys you, do you tell him/her? [/]",
     "[bold black on light_salmon1] When the waiter is rude, do you complain? [/]", 
     "[bold black on light_salmon1] When the food comes out different than you ordered, will you send it back? [/]",
      "[bold black on light_salmon1] Do you get frustrated while driving? [/]",
       "[bold black on light_salmon1] Would you tell the truth even when it will hurt people? [/] ",
       "[bold black on light_salmon1] When your employer gives you a useless assignment, would you refuse? [/]",
       "[bold black on light_salmon1] When a customer is behaving like a spoiled brat, would you point this out? [/] ",
       "[bold black on light_salmon1] Do you have arguments with your peers often? [/]")

    for q in questions: 
        value = get_answer(q)
        score.append(value) 

    total = sum(score)
    return total 

def get_answer(quest): 

    """ 
    Prints the question.
    Checks the input to be a number, 
    if the num is between 1 -10.
    If not raise an error and if correct,
    returns the number
    """
    print(" \n" + quest + " \n ") 
    print("Choose a number on a scale of 1 to 10.")

    # thank god to stack overflow

    while True:
        answer = input("1 = Never 10 = Always:\n")
        if answer.isdigit() and 1 <= int(answer) <= 10:
            return int(answer)
            break
        elif answer == "q": 
            exit()
        else:
            print("[white on red]Oh oh, that is not a valid input[/]")
      


def result(number): 

    """ 
    Matches the score with right type, 
    print right anger-type
    """

    cool = "[bold bright_cyan]Wow it seems that you are as COOL as ICECREAM.\nEven though it is great to be in control nobody likes to relate to a statue\nAlso your anger is the force for change, don't let it die![/]"
    warrior = "[bold green]You seem to have a WARRIOR-LIKE state of mind.\nYou know when to lose your cool to address, that what needs change.\nBut you also know when to control your emotion to adjust to the situation.[/]"
    hothead = "[bold red]You are overheated most of the time, we could call you DYNAMITE.\nBring back the 10 second count before expressing your anger![/]"
    
    print("\nCalculating your angertype.....\n")

    if int(number) <= 24: 
        return cool
    elif int(number) <= 56: 
        return warrior
    else:
        return hothead
    

def store_data(val1, val2): 

    """ 
    Ask's the user if their name and test results can be stored. 
    When the answer is yes, the data will be pushed to, 
    an external google sheet. 
    """
    data = []
    data.append(val1)
    data.append(val2)
    to_update = SHEET.worksheet("results")

    while True:
        print("\nCan we store these results for our statistics?") 
        permission = input("y/n :\n ")
        if permission == "y":
            print("\nLogging your results...")
            to_update.append_row(data)
            print("\nThank you for taking the test, and have a great day!")
            break
        elif permission == "n": 
            print("\nOkay we will not store your results.")
            print("Have a good day!")
            break
        else: 
            print("[white on red]Oh oh that is not a valid input[/]")

    
    



def main(): 
    """ 
    Calls all the main functions for the game
    """

    user = introduction()
    begin()
    total_score = quizz()
    person = result(total_score)
    print(person)
    store_data(user, total_score)
    
    
main()
























    
    

