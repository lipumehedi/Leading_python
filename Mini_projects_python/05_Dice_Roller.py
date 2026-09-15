import random

def roll_dice():
    """Rolls a dice and returns a random number between 1 and 6."""
    return random.randint(1, 6)

print("🎲 Welcome to Dice Roller! 🎲")

while True:
    choice = input("Press Enter to roll the dice (or 'q' to quit): ")
    if choice.lower() == 'q':
        print("Thanks for playing! Goodbye.")
        break
    result = roll_dice()
    print(f"You rolled: {result}")