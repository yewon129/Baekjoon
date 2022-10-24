N = int(input())
arr = [[0] * 101 for _ in range(101)]

for _ in range(N):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            if arr[i][j] == 0:
                arr[i][j] += 1


ans = 0
for x in arr:
    ans += x.count(1)

print(ans)