values = { 0:'',
    1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
    6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 
    11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 
    15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
    20:'Twenty', 30:'Thirty', 40: 'Forty', 50:'Fifty', 60:'Sixty', 70: 'Seventy', 
    80:'Eighty', 90:'Ninety', 1000: 'onethousand'
}

def mat_2_digits(first, second):

    if int(str(first) + str(second)) in values: 
        return len(values[int(str(first) + str(second))])

    first = int(str(first) + '0')
    return len(values[second]) + len(values[first])


def mat_3_digits(n):
    first, second, third = [int(x) for x in str(n)]
    if second == 0 and third == 0:
        return len(values[first]) + 7
    # 10 stands for: hundred + and
    return mat_2_digits(second, third) + len(values[first]) + 10

sum = 0
for i in range(1, 1001):
    if i in values:
        print(i, len(values[i]))
        sum += len(values[i])
    
    elif len(str(i)) == 2:
        first, second = [int(x) for x in str(i)]
        sum += mat_2_digits(first, second)

    elif len(str(i)) == 3:
        sum += mat_3_digits(i)

print(sum)