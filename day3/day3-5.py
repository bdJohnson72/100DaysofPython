name = input("What is the first name?\n").lower()
name2 = input("What is the second name? \n").lower()

total = 0

total += name.count("t")
total += name2.count("t")
total += name.count("r")
total += name2.count("r")
total += name.count("u")
total += name2.count("u")
total += name.count("e")
total += name2.count("e")
total += name.count("l")
total += name2.count("l")
total += name.count("o")
total += name2.count("o")
total += name.count("v")
total += name2.count("v")
total += name.count("e")
total += name2.count("e")

print(total)