import math
# For every exact divisor up to the square root, there is a corresponding divisor above the square root. 
def get_number_of_divisors(val, i = 0):
    for n in range(2, int(math.sqrt(val) + 1)):
        if val % n == 0:
            # +2 bc n and val/n
            i = i+2
    # +2 bc always n and 1
    return i+2

i = 0
val = 0
max = 0
while True:
    val = val + i
    div = get_number_of_divisors(val)
    if div > max:
        max = div
    if div > 500:
            break
    i = i + 1

print(val)

#not 842161320