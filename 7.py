import math
MAX_ARRAY_LENGTH = 10001
def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0: return False
    return True

primes = []
i = 2
while len(primes) < MAX_ARRAY_LENGTH:
    if is_prime(i):
        primes.append(i)
    i = i+1
print(primes[-1])
