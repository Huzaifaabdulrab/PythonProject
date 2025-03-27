import random

def hangman():
    """ Hangman game where user guesses a word within 5 attempts. """

    # Taking user's name input
    while True:
        user_name = input("Hii! What is your name? ").title()
        if user_name:
            print(f"🎉 Welcome {user_name} to the Hangman Game! 🎉")
            print("Guess the word within 5 attempts.")
            break
        else:
            print("⛔ Please enter your name!")

    # List of words with hints
    hangman_questions = [
        {"word": "APPLE", "hint": "A fruit that keeps the doctor away. A_ _ L _"},
        {"word": "TABLE", "hint": "You use it to place things on. T _ B _ E"},
        {"word": "TRAIN", "hint": "A vehicle that runs on tracks. T _ _ I N"},
        {"word": "RIVER", "hint": "A large natural stream of water. R _ _ E R"},
        {"word": "MOUSE", "hint": "A small device used with a computer. M _ _ S E"},
        {"word": "HOUSE", "hint": "A place where people live. H _ _ S E"},
        {"word": "CLOUD", "hint": "It floats in the sky and brings rain. C _ _ U D"},
        {"word": "PLANE", "hint": "A vehicle that flies in the air. P _ _ N E"},
        {"word": "BREAD", "hint": "You eat this with butter or jam. B _ _ A D"},
        {"word": "LIGHT", "hint": "The opposite of 'dark'. L _ _ H T"}
    ]

    # Selecting a random word
    random_ques = random.choice(hangman_questions)
    max_attempts = 5  # Maximum attempts allowed
    attempts = 0  # Count of attempts used

    print(f"Hint: {random_ques['hint']}")  # Display hint

    # User guessing loop
    while attempts < max_attempts:
        user_guess = input("Your Guess: ").upper()  # Convert input to uppercase

        if user_guess == random_ques["word"]:  # Check if guess is correct
            print(f"🎉 You have guessed the word correctly in {attempts} attempts! 🎉")
            break
        else:
            attempts += 1
            print(f"❌ Wrong guess! Attempts left: {max_attempts - attempts}")

    # If user fails after all attempts
    if attempts == max_attempts:
        print(f"❌ Out of attempts! The correct word was: {random_ques['word']}")

# Run the game if this file is executed directly
if __name__ == "__main__":
    hangman()
