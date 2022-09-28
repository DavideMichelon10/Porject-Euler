LIMIT = 1000000
numbers = [0,1,2,3,4,5,6,7,8,9]

def check_num_composed_of_numbers(num, numbers):

    num_splitted = [s for s in str(num)]
    print(len(num_splitted))
    print(len(numbers))
    print(num_splitted[0])
    if num_splitted[0] == 0:
        if len(num_splitted)-1 != len(numbers):
            return False
    elif len(num_splitted) != len(numbers):
        return False
    
    for n in numbers:
        if n not in num_splitted:
            return False
    
    return True


i = 0
num = 123456789
print(check_num_composed_of_numbers(num, numbers))
# while True:
#     if check_num_composed_of_numbers(num, numbers):
#         i+=1
#     if i == LIMIT:
#         break
#     # print(i)
#     num+=1

print(num)