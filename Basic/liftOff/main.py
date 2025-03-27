import time

def lift_off():
    """ Countdown from 10 to 1, then print 'Liftoff!' """
    for i in range(10, 0, -1):  # Countdown from 10 to 1
        print(i)
        time.sleep(1)  # Pause for 1 second between numbers

    print("Liftoff!")  # Print after countdown completes

if __name__ == "__main__":
    lift_off()
