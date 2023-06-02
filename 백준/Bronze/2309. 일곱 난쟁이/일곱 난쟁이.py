from itertools import combinations

lst = list(int(input()) for _ in range(9))

for lst in combinations(lst, 7):
    cnt = 0
    for i in lst:
        cnt += i
    if cnt == 100:
        lst = list(lst)
        lst.sort()
        for k in lst:
            print(k)
        break