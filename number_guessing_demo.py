# import libraries
import random 

# declare variables
smallest_guess = 1
biggest_guess = 20
number_to_guess = random.randint(smallest_guess, biggest_guess)
guess = 0

# tell the player what to guess
print("The number to guess is between {} and {}".format(smallest_guess, biggest_guess))
    
# game logic 
while (guess != number_to_guess): # keeps game going until player guesses correctly
    
    # tell player to guess and take in their guess as *input* 
    guess = int(input("Enter a guess (whole numbers ONLY): "))
    
    # check the guess
    if (guess == number_to_guess):
        print("That's correct! You win!")
    elif (guess < number_to_guess):
        print("That's too low! Try again.")
    elif (guess > number_to_guess):
        print("That's too high! Try again.")