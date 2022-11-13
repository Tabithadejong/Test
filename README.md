# Anger Type Personality Test
This Anger Type Personality test is a Python terminal, which runs in the Code Institute mock terminal on Heroku.
It is a questionnaire which will track the user input to find out how they relate to anger within themselves.
 
[Here is the link to the deployed project]("")
 
 
## How it works
 
The questionnaire is a list of day to day examples of situations that might trigger one's anger or frustration. The user is asked to think about what they would do in these situations. All the questions are scale questions, meaning the user needs to put in a number on the scale of 10 depending on their reaction to the sketched situation. The program will keep track of their score and will reveal their behavioral pattern at the end of the questionnaire.
 
![Picture of the terminal in action] ()
 
## Features
 
 
### Existing Features
 
- A welcome message with user input to address the user personal
![picture of welcome message]()
- The option to start the game
![picture of commence message]()
- The questionnaire form with 8 scale questions
![picture of questions]()
- User input throughout the form to have the user really interact with the program
  - Keeping track of user input and adding it to scores
  - Checking user input for validity
  - When input does not meet requirements an error message will be thrown
  ![picture of error message]()
  - At any given time while answering questions the user has the option to exit the form
  ![picture of q option]()
- Personal result display
  - The result is styled according to the score of the user
- Storage of the results after permission
  - There is an option to reject storage
  - When agreed to storage the results will be logged to an external sheet
 
 
### Future Features
 
In the near future it would be an option to ask for contact details from each user. According to their results different offers could be made to them personally. Anger management courses or rather emotional expression training for example. These marketing strategies can be marketed with or through a third party.
 
## Data Model
 
The data input is requested in the terminal. Then the data is stored and analyzed in the background. The end results and user name are highlighted and pushed to an external google sheet. This way numerous analytics can be done on the results.
 
## Testing
 
The personality test has been through extensive testing in the following ways.
- Linter testing in the local terminal
- The deployed Heroku terminal
- Inserting wrong input for example string instead of numbers and visa versa
- Checking the google sheet for updated scores
 
 
### Bugs
 
#### Fixed Bugs
 
- Before deployment
  - The user input was held by a while loop which in turn had a `TRY, EXCEPT, ELSE` statement for checking the user input and raising a custom error. Only in this way the scale from 1 - 10 could not also be validated so I had to change it to a proper `IF` statement.
- After deployment
  - The rich import for adding colors inside the terminal was not picked up by the pip installment in the requirements.txt. This had to be added manually.
  - Due to a mistake in the code logic the main function was called twice in the program meaning the form would repeat itself after first completion. This is corrected.
 
 
#### Unfixed Bugs
 
There are no remaining bugs.
 
 
### Validator Testing
 
I have used a linter inside local terminal; pycodestyle
- No errors were found
 
 
## Deployment
 
This project was deployed using Code Institute's mock terminal for Heroku
 
- Steps that have been taken;
  - Create repository on github
  - Create a Heroku App
  - Adding in credentials needed for deployment
  - Add buildpack `Python` and `NodeJs`
  - Link the Heroku app to github repository
  - Then Deploy
 
 
## Credits
 
- Code institute for the mock terminal
- Code institute for teaching me Python
- Mentor for tipping me to style the mock terminal
- Slack channel where fellow students would help troubleshoot during denial of rich module afte deployment
- [Website for color pallet to be used with rich import]("https://rich.readthedocs.io/en/stable/appendix/colors.html")
- The snippet of code that helped me check for range of input and type of input at the same time;
[Link to stack-overflow]("https://stackoverflow.com/questions/19821273/limiting-user-input-to-a-range-in-python")
![picture of the code snippet]("")
 

