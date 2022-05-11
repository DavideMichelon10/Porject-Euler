array = [1,2]
TRESHOLD = 4000000

while array[-1] < TRESHOLD:
    array.append(array[-1] + array [-2])

sum = 0
for val in array:
    if val % 2 == 0:
        sum = sum + val

print(sum)
