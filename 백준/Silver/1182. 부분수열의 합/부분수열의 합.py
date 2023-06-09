from itertools import combinations

N, S = map(int, input().split())
lst = list(map(int, input().split()))

answer = 0
for i in range(1, N+1):
    for box in combinations(lst, i):
        if sum(list(box)) == S:
            answer += 1

print(answer)