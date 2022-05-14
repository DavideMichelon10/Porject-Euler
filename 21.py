import numpy as np

def sum_of_divisors(num):
    sum = 0
    for i in range(1, int(num / 2) + 1):
        if num % i == 0:
            sum = sum + i
    return sum

ammicables = set()
for i in range(10000):
    first = sum_of_divisors(i)
    second = sum_of_divisors(first)

    if second == i and first != second:
        ammicables.add(i)

sum = 0
for ammicable in ammicables:
    sum += ammicable

print(sum)
