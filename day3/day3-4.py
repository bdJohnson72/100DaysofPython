SMALL_PIZZA = 15.00
MEDIUM_PIZZA = 20.00
LARGE_PIZZA = 25.00

SMALL_PEPPERONI = 2.0
MED_LARGE_PEPPERONI = 3.0
EXTRA_CHEESE = 1.0

total = 0

size = input("What size pizza do you want ? S, M or L?\n")
if size.lower() == "S":
    total += SMALL_PIZZA
elif size.lower() == "M":
    total += MEDIUM_PIZZA
else:
    total += LARGE_PIZZA

pepperoni = input("Do you want pepperoni? Enter Y or N\n")
if pepperoni.lower() == "Y":
    if size.lower() == "S":
        total += SMALL_PEPPERONI
    else:
        total += MED_LARGE_PEPPERONI

more_cheese = input("Do you want extra cheese? Y or N\n")
if more_cheese.lower() == "Y":
    total += EXTRA_CHEESE

print(f"Thanks for your order the total is {total}")



