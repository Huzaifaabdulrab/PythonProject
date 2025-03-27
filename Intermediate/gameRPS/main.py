import random

def game_RPS():
    """ Rock, Paper, Scissors game where the user plays against the computer. """

    # List of possible choices
    choices = ["rock", "paper", "scissors"]

    # Taking user input
    user_choice = input("Enter Your Choice (rock, paper, scissors): ").lower()

    # Computer randomly selects one option
    computer_choice = random.choice(choices)

    # Display computer's choice
    print(f"Computer chose: {computer_choice}")

    # Check for a tie
    if user_choice == computer_choice:
        print("It's a tie!")
    
    # Check for winning conditions
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("🎉 You win!")
    else:
        print("❌ Computer wins!")

# Start the game
if __name__ == "__main__":
    game_RPS()
