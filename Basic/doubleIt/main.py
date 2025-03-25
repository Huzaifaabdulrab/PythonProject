

def double_it():
    # Get user name input
    user_name = input("Hii, What is your Name? ")
    
    # Get user number input
    try:
        next_question = int(input(f"Hii {user_name}, Enter your number and I will double it: "))
        print(f"Double of {next_question} is {next_question * 2}")
    except ValueError:
        print("Please enter a valid number.")

# Call the function

if __name__ == "__main__":
    double_it()
 