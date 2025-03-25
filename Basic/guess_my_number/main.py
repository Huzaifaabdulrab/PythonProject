import random  # Importing the random module

# Generating a random number between 1 and 10
number = random.randrange(1, 10)
print(number)  # (Optional) Printing the number for debugging


def guess_my_number():
    """This function allows the user to guess a randomly generated number."""
    
    print("Number Guessing Game")  # Displaying the game title
    
    while True:
        user_name = input("Hi! What is your name: ")  # Asking the user for their name
        if user_name:  # Checking if the user has entered a name
            while True:
                try:
                    # Prompting the user to guess a number between 1 and 10
                    user_num = int(input("Guess a number between 1 and 10: "))  
                    
                    if user_num == number:
                        print(f"Yes {user_name}, You guessed it right!")  # Message for correct guess
                        break  # Exiting the loop if the guess is correct
                    else:
                        print(f"Sorry {user_name}, You guessed it wrong. Try again!")  # Message for incorrect guess
                except ValueError:
                    print("Invalid input! Please enter a number between 1 and 10.")  # Handling invalid input
                    
            break  # Breaking the loop once the user has guessed the number
        else:
            print("Please enter your name first")  # Asking the user to enter their name

# Calling the function
guess_my_number()

