lst = []
for i in range(1, 9):
    lst.append([int(input()), i])
lst.sort()
box = []
cnt = 0
for j in range(3, 8):
    cnt += lst[j][0]
    box.append(lst[j][1])

print(cnt)
box.sort()
for k in range(5):
    print(box[k], end=' ')