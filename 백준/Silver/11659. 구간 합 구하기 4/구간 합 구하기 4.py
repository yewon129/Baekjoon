N, M = map(int, input().split())
lst = list(map(int, input().split()))
sum_nums = [0 for _ in range(N)]

for i in range(N):
    if i == 0:
        sum_nums[i] = lst[i]
    else:
        sum_nums[i] = sum_nums[i-1] + lst[i]

for _ in range(M):
    a, b = map(int, input().split())
    if a == 1:
        print(sum_nums[b-1])
    else:
        print(sum_nums[b-1]- sum_nums[a-2])