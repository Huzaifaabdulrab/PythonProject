import random

def number_guess_user():
    """
    Number Guessing Game where the user has to guess a randomly generated number 
    between 1 and 100.
    """
    while True:
        # Generate a random number between 1 and 100
        secret_num = random.randint(1, 100)  
        attempts = 0

        print("\n🎯 Welcome to the Number Guessing Game!")
        print("I have selected a number between 1 and 100. Can you guess it?")
        
        while True:
            try:
                # User input
                user_guess = int(input("Enter your guess: "))
                attempts += 1

                # Check if guess is too high
                if user_guess > secret_num:
                    print("📉 Too high! Try again.")

                # Check if guess is too low
                elif user_guess < secret_num:
                    print("📈 Too low! Try again.")

                # Correct guess
                else:
                    print(f"🎉 Congratulations! You found the number in {attempts} attempts.")
                    break  # Exit loop if guessed correctly

            except ValueError:
                print("⛔ Please enter a valid number!")  # Handle invalid input

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! 👋")
            break  # Exit game loop

if __name__ == "__main__":
    number_guess_user()
