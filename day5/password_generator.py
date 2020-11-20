# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []
totalChoices = nr_letters + nr_numbers + nr_symbols
print(f'total choices = {totalChoices}')


def randomize_inputs():
    return random.randint(1, 3)


def random_letter():
    return random.choice(letters)


def random_symbol():
    return random.choice(symbols)


def random_number():
    return random.choice(numbers)


def generate_password():
    global nr_letters
    global nr_numbers
    global nr_symbols
    print(f'starting values are letters {nr_letters} symbolns {nr_symbols} numbers {nr_numbers}')
    random_choice = randomize_inputs()
    print(f"the rand0m choice = {random_choice}")
    if random_choice == 1 and nr_letters > 0:
        password.append(random_letter())
        print(f'number of letters {nr_letters}')
        print(random_choice)
        nr_letters - 1

    if random_choice == 2 and nr_symbols > 0:
        password.append(random_symbol())
        print(f'number of symbols {nr_symbols}')
        nr_symbols - 1


    if random_choice == 3 and nr_numbers > 0:
        password.append(random_number())
        print(f"number of numbers = {nr_numbers}")
        nr_numbers - 1


for choice in range(totalChoices):
    #print(choice)
    #print(f'in the for loop {totalChoices}')
    generate_password()


print(str(password).strip('b '))
text = (', '.join(map(str, password)))
print(text.replace(", ", ""))
print(len(password))
