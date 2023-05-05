N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x: (x[1], x[0]))
i = 1
cnt = 1
while i < len(arr):
    if arr[i-1][1] <= arr[i][0]:
        cnt += 1
        i += 1
    else:
        arr.pop(i)

print(cnt)