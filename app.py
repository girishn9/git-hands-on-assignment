import random

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"You rolled {dice1} and {dice2} (Total: {dice1 + dice2})")

roll_dice()
