height = int(input("What is your height in inches? \n"))
weight = int(input("What is your weight in pounds? \n"))


def bmi(height, weight):
    return weight * 703 / height ** 2


# f string

print(f"Your BMI is {bmi(height, weight)}")
