# check which prime numbers divides the num is 0
import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0: return False
    return True

max = 0    
NUMBER = 600851475143

for i in range(1, int(math.sqrt(NUMBER))):
    if is_prime(i) and NUMBER % i == 0:
        max = i
print(max)

# get all primes numbers, starting from the biggest divide NUMBER: the first with % 0 is the res