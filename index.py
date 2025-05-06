import random

def choose_difficulty():
    print("Choose difficulty level:")
    print("1. Easy (10 tries)")
    print("2. Medium (7 tries)")
    print("3. Hard (5 tries)")

    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == '1':
            return 10
        elif choice == '2':
            return 7
        elif choice == '3':
            return 5
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def play_game():
    secret_number = random.randint(1, 100)
    tries = choose_difficulty()

    print("\nI'm thinking of a number between 1 and 100.")
    print(f"You have {tries} tries to guess it.")

    for guess_count in range(1, tries + 1):
        while True:
            try:
                guess = int(input(f"Guess #{guess_count}: "))
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"🎉 Congratulations! You guessed it in {guess_count} tries!")
            break
        # Hint system
        if abs(guess - secret_number) <= 5:
            print("Hint: You're very close!")
        elif abs(guess - secret_number) <= 10:
            print("Hint: Close!")

    else:
        print(f"😢 Out of tries! The number was {secret_number}.")

def main():
    print("🎮 Welcome to the Improved Guess the Number Game!")
    while True:
        play_game()
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye.")
            break

# Start the game
main()
