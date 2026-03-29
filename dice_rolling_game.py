# Loop
    # Ask: Roll the dice?
    # If user enters y
    #   Ask user to how many dice you want to roll.
    #   User asked n
    #   Generate N random numbers and print them.
    #   Print them
    # If user enters n
    #   Print thank you message
    #   Terminate
    # Else
    #   Print invalid choice.      

import random

def RollDice():
    
    while True:
        choice=input("Roll the dice? (y/n):").lower()
        if choice=='y':
            num_rolls=int(input("How many dice you want to roll: "))
            for i in range(num_rolls):
                dice=random.randint(1,6)
                print(f"Dice {i+1}:{dice}")
        elif choice=='n':
            print("Thanks for playing!")    
            break
        else:
            print('Invalid choice!')

RollDice()


 


















