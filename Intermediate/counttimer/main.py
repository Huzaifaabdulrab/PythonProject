import time
import winsound

def count_timer(second):
    """ Countdown timer that beeps when time reaches zero. """

    print("⏳ Welcome to Countdown Timer App!")

    # Loop to display countdown
    for i in range(second, -1, -1):
        print(i)  # Show remaining time
        time.sleep(1)  # Wait for 1 second

    # Play beep sound when countdown ends
    winsound.Beep(2300, 1200)  

# Take user input for countdown duration
user_input = int(input("Enter your time in seconds: "))

if __name__ == "__main__":
    count_timer(user_input)
