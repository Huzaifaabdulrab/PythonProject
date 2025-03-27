def number_guess_computer():
    """
    This is a Number Guessing Game where the **computer** tries to guess the number 
    the user is thinking of using a binary search approach.
    """
    low = 1  # Lower bound of the guessing range
    high = 100  # Upper bound of the guessing range
    attempts = 0  # Counter for attempts

    print("🤖 Think of a number between 1 and 100, and I will try to guess it!")

    while True:
        # Computer's guess (middle of the range)
        computer_guess = (low + high) // 2
        attempts += 1

        print(f"My guess is: {computer_guess}")

        # Ask the user if the guess is correct
        user_input = input("Is my guess (higher / lower / correct)? ").strip().lower()

        if user_input == "higher":
            low = computer_guess + 1  # Update lower bound if guess was too low
        elif user_input == "lower":
            high = computer_guess - 1  # Update upper bound if guess was too high
        elif user_input == "correct":
            print(f"🎉 Yay! I guessed it in {attempts} attempts!")
            break  # End the game
        else:
            print("⛔ Invalid input! Please enter 'higher', 'lower', or 'correct'.")

if __name__ == "__main__":
    number_guess_computer()
