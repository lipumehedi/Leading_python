import random

choices = ["rock", "paper", "scissors"]

user = input("Enter your choice (rock/paper/scissors): ").lower()
computer = random.choice(choices)

print(f"\nYou chose: {user}")
print(f"Computer chose: {computer}")

if user == computer:
    print("It's a Tie!")
    
elif user == "rock":
    if computer == "scissors":
        print("You Win! 🎉")
    else: 
        print("You Lose! 🥲")

elif user == "paper":
    if computer == "rock":
        print("You Win! 🎉")
    else:
        print("You Lose! 🥲")

elif user == "scissors":
    if computer == "paper":
        print("You Win! 🎉")
    else:
        print("You Lose! 🥲")

else:
    print("Invalid choice! Please chose rock, paper or scissors.")