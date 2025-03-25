import random

n_number :int = 10
min_number : int = 1
max_number : int = 100

def random_number():
    
    for i in range(n_number):
        value = random.randint(min_number , max_number)
        print(value)


if __name__ == "__main__":
    random_number()