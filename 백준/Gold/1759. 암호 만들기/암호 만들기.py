from itertools import combinations

L, C = map(int, input().split())
lst = list(map(str, input().split()))

v = []
c = []
for i in range(C):
    if lst[i] in ['a','i','e','o','u']:
        v.append(lst[i])
    else:
        c.append(lst[i])

box = list(combinations(lst, L))
answer = []
for i in range(len(box)):
    box[i] = list(box[i])
    num_v = 0
    num_c = 0
    box[i].sort()
    for j in range(len(box[i])):
        if box[i][j] in v:
            num_v += 1
        elif box[i][j] in c:
            num_c += 1
        if num_v >= 1 and num_c >= 2:
            answer.append(box[i])
            break

answer.sort()
for i in range(len(answer)):
    for j in range(len(answer[i])):
        print(answer[i][j], end='')
    print()