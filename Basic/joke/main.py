import random

# List of funny jokes
jokes = [
    "Why don’t skeletons fight each other? Because they don’t have the guts!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised!",
    "Why don’t scientists trust atoms? Because they make up everything!",
    "I'm on a whiskey diet. I've lost three days already!",
    "Parallel lines have so much in common. It’s a shame they’ll never meet."
]

def tell_joke():
    """ Selects and returns a random joke from the list. """
    return random.choice(jokes)

# Display the first joke
print("\n🤖 Here's a joke for you:")
print(tell_joke())
print("************************************")

# Loop to keep telling jokes until the user quits
while True:
    print("1. Tell me another joke")
    print("2. Quit")

    choice = input("Choose an option (1 or 2): ").strip()
    
    if choice == "1":
        print("************************************")
        print(tell_joke())
        print("************************************")
    elif choice == "2":
        print("Goodbye! 👋")
        break
    else:
        print("\n❌ Invalid input! Please press 1 or 2.")

if __name__ == "__main__":
    tell_joke()
