import random


def main() -> None:
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    target = random.randint(1, 100)
    attempts = 0

    while True:
        guess_text = input("Enter your guess: ").strip()

        if not guess_text.isdigit():
            print("Please enter a valid whole number.")
            continue

        guess = int(guess_text)
        attempts += 1

        if guess < target:
            print("Too low! Try again.")
        elif guess > target:
            print("Too high! Try again.")
        else:
            print(f"Nice! You guessed the number in {attempts} attempts.")
            break


if __name__ == "__main__":
    main()
