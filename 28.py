def compute_sum(dimension):
    h=2
    num=1
    sum=1
    while(h < dimension):
        for i in range(4):
            
            num = num+h
            sum+=num
        h=h+2
    return sum

print(compute_sum(1001))