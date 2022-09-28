one_term = second_term = 1
number = one_term + second_term
i = 2

while len(str(number)) < 1000:

    number = one_term + two_term
    two_term = one_term
    one_term = number
    i += 1

print(i)