
import random


def play_game():
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("\n=== Number Guessing Game ===")
    print("Guess a number between 1 and 100.")
    print(f"You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if not 1 <= guess <= 100:
            print("Enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess == secret:
            print(f"Correct! You won in {attempts} attempts.")
            return

        if guess < secret:
            print("Too low!")
        else:
            print("Too high!")

        print(f"Attempts remaining: {max_attempts - attempts}")

    print(f"Game over! The answer was {secret}.")


def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()

        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
