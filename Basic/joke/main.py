import random

jokes = [
    "Why don’t skeletons fight each other? Because they don’t have the guts!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised!",
    "Why don’t scientists trust atoms? Because they make up everything!",
    "I'm on a whiskey diet. I've lost three days already!",
    "Parallel lines have so much in common. It’s a shame they’ll never meet."
]

def tell_joke():
    return random.choice(jokes)

print("\n🤖 Here's a joke for you:")
print(tell_joke())
print("************************************")

while True:
    print("1. Tell me another joke :")
    print("2. Quit :")

    choice = input("Choose An Option 1, 2  : ").strip()
    if choice == "1":
        print("************************************")
        print(tell_joke())
        print("************************************")
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("\n❌ Invalid input! Please press 1, 2, or 3.")

if __name__ == "__main__":
    tell_joke()
