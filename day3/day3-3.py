# solve for leap year

year = int(input("What is the year\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("That is a leap year")
    else:
        print("Not a leap year")
else:
    print("sorry not a leap year")
