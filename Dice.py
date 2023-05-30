import random

def roll_dice():
    return random.randint (1,6)

roll_again = input("wanna roll the dice? (yes/no)")

if roll_again.lower() == "yes":
    dice_roll = roll_dice()
    print("Okay *Shakes* Here's the number", dice_roll)

else:
    print("Okay next restart when u wanna roll it")