##### import libraries ####
import random

#### Make your variables ####
lowest_number = 1  # smallest number that can be chosen
biggest_number = 100 # biggest number that can be chosen
number_to_guess = random # hint: we need to use the "randint" method. it picks a random number between a lowest value and a highest value (lowest, highest)
player_guess = 0 # the number the player has chosen. what should it be before they choose one?

##### tell the player what to guess between ####
print("The number is between a and b").MethodName(a,b)  # hint: inside the " ", we put {} where we want to put in a variable. After the "", we need the .format method - (lowest, highest)

#### game logic ####
while(): #this loop should run as long as the player hasn't guessed the number.. how do we tell the code that? hint: we need a conditional in the parentheses!
    
    # tell player to guess and take in their guess as *input*
    guess = int() # hint: it goes inside the parentheses- putting int() here allows us to turn the player's response into a number

    # check the guess
    if(right here!): # what should we check first? - condition 1
        print("Correct!")
    elif(): # we use "elif" when we need to check something else - condition 2
        print("Too high!")# print out the right response 
    # write condition 3 here!
        print("Too...")# print out the right response