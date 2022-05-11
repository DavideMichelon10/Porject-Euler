import math

SUP = 2000000
sum = 0

def is_prime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

for i in range(2, SUP):
    if is_prime(i):
        sum = sum + i

print(sum)

# not 37550402023