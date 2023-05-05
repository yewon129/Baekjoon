N = int(input())
arr = [0] * N
for i in range(N):
    n, m = map(int, input().split())
    arr[i] = [n, m]

arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:x[1])
cnt = 1
i = 1
while i < len(arr):
    if arr[i-1][1] <= arr[i][0]:
        cnt += 1
        i += 1
    else:
        arr.pop(i)

print(cnt)