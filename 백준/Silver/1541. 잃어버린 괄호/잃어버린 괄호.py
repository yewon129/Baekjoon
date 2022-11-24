lst = list(map(str, input()))
# [5 5 - 5 0 + 4 0]
num = []
char = []
# [55, 50, 40]
# [-, +]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
i = 0
while i < len(lst):
    if lst[i] in numbers:
        j = i
        n = []
        while j < len(lst) and lst[j] != '+' and lst[j] != '-':
            n.append(lst[j])
            j += 1
        s = ''
        for k in range(len(n)):
            s = s + n[k]
        num.append(int(s))
        i = j

    else:
        char.append(lst[i])
        i += 1

i = 0
while '+' in char:
    if char[i] == '-':
        i += 1
    if char[i] == '+':
        num[i] += num[i + 1]
        char.pop(i)
        num.pop(i+1)

i = 0
while char:
    num[i] -= num[i+1]
    char.pop(0)
    num.pop(1)

print(num[0])