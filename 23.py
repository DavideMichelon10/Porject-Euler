import math
import time
start_time = time.time()

UPPER = 28123
def is_abundant(num):
    divisors_sum = 0
    for i in range(1, int(math.sqrt((num)) +1)):
        if num % i == 0:
            if i == math.sqrt(num) or i == 1:
                divisors_sum += i
            else:
                 divisors_sum = divisors_sum + i + num / i 
    return divisors_sum > num

def list_of__adbs_sum(abdundants, upper):
    sums = set()
    first = 0
    
    while first < len(abdundants):
        second = 0
        while second < len(abdundants):
            val = abdundants[first] + abdundants[second]
            if val < upper:
                sums.add(val)
            second += 1
        first += 1
        
    return sums

abundants = []
sum = 0

for n in range(1, UPPER):
    if is_abundant(n):
        abundants.append(n)

sums = list_of__adbs_sum(abundants, UPPER)

for n in range(1, 28123):
    if n not in sums:
        sum += n
print('Result: {} execution time: {}'.format(sum, time.time() - start_time))