import time

def story_generator():
    """
    A simple interactive story generator that takes user input
    to create a fun, personalized short story.
    """

    while True:
        # Ask for the user's name
        userInput = input("Hi, how are you? What is your name: ").strip()
        if not userInput:
            print("⛔ Please enter your name!")  # Validation for empty input
            continue  

        while True:
            # Ask for an adjective to describe the morning
            adjective = input("Describe the morning (e.g., beautiful, mysterious): ").strip()
            if not adjective:
                print("⛔ Please enter a description of the morning.")
                continue  

            # Ask for a place
            place = input("Enter a place (e.g., park, forest, market): ").strip()
            if not place:
                print("⛔ Please enter a place.")
                continue

            # Ask for a noun (an object)
            noun = input("Name an object (e.g., box, book, lamp): ").strip()
            if not noun:
                print("⛔ Please enter an object.")
                continue

            # Ask for a verb (an action)
            verb = input("Enter an action (e.g., dance, sing, jump): ").strip()
            if not verb:
                print("⛔ Please enter an action.")
                continue

            # Ask for an animal
            animal = input("Name an animal (e.g., cat, monkey, bird): ").strip()
            if not animal:
                print("⛔ Please enter an animal.")
                continue

            # Generate and print the story
            story = f"\nOne {adjective} morning, {userInput} went to the {place} and found a {noun} that could {verb} like a {animal}."
            print(story)
            print(f"This story is created by {userInput}")

            # Ask if the user wants to play again
            again = input("Do you want to play again (yes/no) : ").strip().lower()
            if again != 'yes':
                print("Thanks for creating!")
                time.sleep(1)  # Adding a small delay before exiting
                return

# Run the program if this file is executed directly
if __name__ == "__main__":
    story_generator()
