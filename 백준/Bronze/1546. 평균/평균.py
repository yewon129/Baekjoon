N = int(input())
lst = list(map(int, input().split()))

M = max(lst)
new = [0] * N
for i in range(N):
    new[i] = lst[i]/M * 100

print(sum(new)/N)