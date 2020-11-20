heights =  [180, 124, 165, 173, 189, 169, 146]

total_height = 0

for height in heights:
    total_height += height;

print(f"The average height is {round(total_height / len(heights))} ")

#accumulator
total = 0
for number in range(1, 101):
    total += number
print(total)

