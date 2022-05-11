number = 0
START = 100
END = 1000
def is_pal(num):
    digits = [int(x) for x in str(num)]

    if len(digits) % 2 != 0:
        pos_center = int(len(digits)/2)
        del digits[pos_center]

    for i in range(0, int (len(digits) / 2)):
        if digits[i] != digits[-(i+1)]:
            return False
    return True

number = 0
for i in range(END):
    for j in range(END):
        prod = i*j

        if is_pal(prod):
            if prod > number:
                number = prod

print(number)
