def prime_checker(number, counter=2):
    if (number <= 2):
        return True if (number == 2) else False
    if (number % counter == 0):
        return False
    if counter * counter > number:
        return True

    return prime_checker(number, counter + 1)


result = prime_checker(83)
print(result)
