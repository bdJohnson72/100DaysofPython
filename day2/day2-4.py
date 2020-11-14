total = float(input("What was the bill? \n"))
group_size = int(input("How many people were in the group? \n"))
tip = float(input("How much do you want to tip? \n"))

result = round((total + (total * tip)) / group_size, 2)

print(f"everyone owes {result}")