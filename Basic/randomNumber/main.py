import random

# Number of random numbers to generate
n_number: int = 10  
# Minimum and maximum range for random numbers
min_number: int = 1  
max_number: int = 100  

def random_number():
    """ Generates and prints 'n_number' random numbers within the given range. """
    
    for i in range(n_number):
        value = random.randint(min_number, max_number)  # Generate random number
        print(value)  # Print the generated number

if __name__ == "__main__":
    random_number()
