import math


def split_check(total, number_of_people):
    if number_of_people <= 1:
        raise ValueError("More than one person is required to split a check")
    return math.ceil(total / number_of_people)


try:
    group_size = int(input('How Many People came?\n'))
    total_due = float(input('What was the total amount\n'))
    amount_due = split_check(total=total_due, number_of_people=group_size)
except ValueError as err:
    print('Please use a number')
    print(f'{err}')
else:
    print(f'Each person owes ${amount_due}')
