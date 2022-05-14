alphabet = ["A","B","C","D", "E", "F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
with open('22_names.txt', 'r') as f:
    names = f.read()

names = names.replace('"','').split(",")
names.sort()

def get_values_word(word):
    sum = 0
    for char in word:
        sum += alphabet.index(char) + 1
    return sum
sum = 0

for index, value in enumerate(names):
    sum += get_values_word(value) * (index + 1)

print(sum)
