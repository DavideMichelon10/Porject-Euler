def get_next_number(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n +1

def get_number_of_chain_elements(n,number_elements,  counter = 0):
    while n != 1:
        counter += 1
        if n in number_elements:
            return counter + number_elements[n] - 1 
        n = get_next_number(n)
    return counter + 1

LIMIT = 1000000
number = 1

# save for each number the number of elements to reach 1
number_chain_elements = {}

final_num = {
    'number_produces_max': 0,
    'max': 0
}

while number < LIMIT:
    number_chain_el = get_number_of_chain_elements(number, number_chain_elements)
    number_chain_elements[number] = number_chain_el
    if  number_chain_el > final_num['max']:
        final_num['max'] =number_chain_el
        final_num['number_produces_max'] = number
    number += 1
    
print(final_num['number_produces_max'])