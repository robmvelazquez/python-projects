import random

def roll_dice():
    # generate a random number between 1 and 6
    result = random.randint(1, 6)
    return result

# call the roll_dice() function to roll the die
print("You rolled a", roll_dice())
