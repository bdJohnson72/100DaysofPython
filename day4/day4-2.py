import random

seed = input("Give me a seed number\n")
random.seed(seed)

random_number = random.randint(1, 2)

if random_number == 1:
    print("That is heads")
else:
    print("That is tails")