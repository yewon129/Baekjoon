lst = [int(input()) for _ in range(9)]

cnt = sum(lst)
for i in range(9):
    cnt -= lst[i]
    for j in range(i+1, 9):
        cnt -= lst[j]
        if cnt == 100:
            lst.pop(j)
            lst.pop(i)
            break
        cnt += lst[j]
    else:
        cnt += lst[i]
        continue
    break

for k in lst:
    print(k)