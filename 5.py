def check_divisible_one_to_twenty(num):
    for i in range(11,20):
        if num % i != 0:
            return False

num_found = False

i= 10
while True:
    if check_divisible_one_to_twenty(i):
        break
    i = i+1

print(i)