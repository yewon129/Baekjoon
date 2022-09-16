n = int(input())

lst = [[1, str(input())]]
for i in range(1,n):
    name = str(input())
    flag = 0
    for j in range(len(lst)):
        if lst[j][1] == name:
            lst[j][0] += 1
            flag = 1
            break
    if flag == 0:
        lst.append([1, name])

lst.sort(key=lambda x: (-x[0], x[1]))
print(lst[0][1])