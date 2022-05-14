import numpy as np

fact = 1
for i in range(1, 101):
    fact = fact * i

arr = [int(n) for n in str(fact)]
print(np.sum(arr))

 