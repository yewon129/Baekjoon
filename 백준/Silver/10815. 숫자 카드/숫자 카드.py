N = int(input())
lst = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))

lst.sort()

def binary(list, target, start, end):
    while start <= end:
        mid = (start+end) // 2

        if list[mid] == target:
            return 1
        elif list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in range(M):
    print(binary(lst, arr[i], 0, N-1), end=' ')