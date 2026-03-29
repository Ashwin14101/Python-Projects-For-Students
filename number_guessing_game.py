# Loop
    # Ask: User to input number between 1 and 100
    # If user enters a number greater than guess number
    #   Print Too High!
    # If user enters a number smaller than guess number 
    #   Print Too Low!
    # If user enters a number the guess number
    #   Print You guessed the correct number.
    #   Terminate.

import random

number_to_guess=random.randint(1,100)
while True:
    try:
        guess = int(input('Guess the number between 1 and 100:'))

        if guess < number_to_guess:
            print('Too low!')
        elif guess > number_to_guess:
            print('Too High!')
        else:
            print('Congratulation! You guessed the Number.')
            break
    except ValueError:
        print("Please Enter a Valid Number")

    