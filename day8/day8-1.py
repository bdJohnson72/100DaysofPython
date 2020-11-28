def greet(name, location):
    print(f'Helllo {name} How is {location}?')
    print(f'Isn\'t Python fun {name}?')


def paint_calculator(height, width, coverage):
    cans_to_buy = round((height * width)  / coverage)
    print(f'You need {cans_to_buy} cans of paint.')


paint_calculator(height=51, width=17, coverage=5)