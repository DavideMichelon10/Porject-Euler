SUP = 1000

for i in range(1, SUP):
    for j in range(1, SUP):
        for z in range(1, SUP):
            if i + j + z == 1000 and z > j > i:
                if i*i + j*j == z*z:
                    print(i*j*z)