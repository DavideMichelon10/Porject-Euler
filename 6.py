sum_squared = 0
squared_of_sum = 0

for i in range(1, 101):
    squared_of_sum = squared_of_sum + i
    sum_squared = sum_squared + i*i

squared_of_sum = squared_of_sum*squared_of_sum
print(squared_of_sum - sum_squared)