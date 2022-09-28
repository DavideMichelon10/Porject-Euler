import math
import time
start_time = time.time()
def is_prime(n):
    if n<0:
        return False
    if n==0 or n==1 or n==2:
        return True

    is_prime = True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            is_prime = False
    
    return is_prime

max=0
first=0
second=0
for a in range(-1000, 1000):
    for b in range(-1001, 1001, 2):
        counter = 0
        for n in range(0, 500000):
            val = n*n+ a*n + b
            if n==0 and is_prime(b):
                counter+=1
            elif is_prime(val):
                counter=counter+1
            else:
                if counter > max: 
                    max=counter
                    first=a
                    second=b
                break
print(first*second)
print("--- %s seconds ---" % (time.time() - start_time))

