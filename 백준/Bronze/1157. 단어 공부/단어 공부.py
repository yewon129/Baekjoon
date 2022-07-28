lst = str(input())
lst = lst.lower()

box = []
count = []
for alp in lst:
    if alp  not in box:
        box.append(alp)
        count.append(1)
    else:
        count[box.index(alp)] += 1

flag = 0
for i in count:
    if max(count) == i:
        flag += 1

if flag > 1:
    print('?')
else:
    print(box[count.index(max(count))].upper())