# Banker Roulette Challenge

import random

names_as_csv = input("Give me a list of names as a CSV.\n")

names_list = names_as_csv.split(', ')
print(names_list)

print(f'{random.choice(names_list)} will pay the bill')
