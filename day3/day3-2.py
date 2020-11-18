height = int(input("What is your height in inches? \n"))
weight = int(input("What is your weight in pounds? \n"))


def bmi(height, weight):
    return weight * 703 / height ** 2


# f string

bmi_value = bmi(height, weight)

print(f"Your BMI is {bmi_value}")
if bmi_value > 35:
    print("Damn you gonna die fatty")
elif bmi_value >= 30:
    print("getting pretty heavy there chubs")
elif bmi_value >=25:
    print("Might need to drop a couple of pounds")
elif bmi_value >= 20:
    print("Looking good")
else:
    print("Eat something")
