N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

lst = [0] * N

for i in range(N-1):
    for j in range(i+1, N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            lst[i] += 1
        elif arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
            lst[j] += 1

for num in lst:
    print(num + 1, end=" ")