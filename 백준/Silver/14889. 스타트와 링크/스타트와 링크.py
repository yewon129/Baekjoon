from itertools import combinations

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

minV = 10000000000

for lst in list(combinations(range(N), N//2)):
    start = 0
    link = 0
    box = []
    for i in range(N):
        if i not in lst:
            box.append(i)
    for i,j in combinations(lst, 2):
        start += arr[i][j] + arr[j][i]

    for i, j in combinations(box,2):
        link += arr[i][j] + arr[j][i]

    if abs(start-link) < minV:
        minV = abs(start-link)

    if minV == 0:
        break

print(minV)