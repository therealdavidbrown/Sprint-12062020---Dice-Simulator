import random
line = "_______________________________________________________________________________\n"
print("Welcome to\n \nDICE ROLL SIM 11\nThese go up to eleven.\n"+line)
print("This game is your one-size-fits-all for random number generationin games. You can generate random numbers for any polyhedral die, and it supports any number of dice.\nEven 11 eleven-sided dice"+line)
# Welcomes the user to the game. '11' and "these go up to eleven" is a gratuitous reference to This Is Spinal Tap, one of the greatest movies of all time

def roll(nDice, nSides): # function for rolling dice, takes the number of dice, and the number of sides of each die into account
    for i in range(nDice):
        print(random.randrange(0, nSides) + 1)

play_game = input('Are you ready to roll the dice? Enter Yes or No.').lower() 
if play_game.lower()[0] == 'y':
    game_on = True # variable for while loop, avoids the program from running forever and getting stuck in a loop
    
while game_on == True:
    nDice = int(input('how many dice are there? Enter an integer.')) # asks the user the number of dice
    nSides = int(input("how many sides does each die have?"))# asks the user for the number of sides for each die
    roll(nDice, nSides)# rolls the dice
    play_game = input('Do you wish to play again? Enter yes or no.')# asks the user each time they wish to roll the dice, this helps with each turn in the game
    if play_game.lower()[0] == 'n': # checks if the user said no to rolling again
        game_on = False # ends the while loop
else: print("Thanks for making DICE ROLL SIM 11 your dice simulator of choice. We look forward to seeing you again!") # while else loop that thanks the user for their... use... of the program
        
