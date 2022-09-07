N =int(input())
arr =[-1] + list(map(int, input().split()))
M = int(input())


def change(n):
    if arr[n] == 0:
        arr[n] = 1
    else:
        arr[n] = 0

for _ in range(M):
    sex, num = map(int, input().split())
    if sex == 1:
        for i in range(num, N+1, num):
            change(i)
    else:
        change(num)
        for k in range(N//2):
            if num + k > N or num - k < 1:
                break
            if arr[num+k] == arr[num-k]:
                change(num + k)
                change(num - k)
            else:
                break

for i in range(1, N+1):
    print(arr[i], end = " ")
    if i % 20 == 0:
        print()