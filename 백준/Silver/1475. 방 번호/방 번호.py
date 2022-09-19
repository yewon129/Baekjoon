lst = list(map(int, input()))

arr = [0] * 9
for i in range(len(lst)):
    if lst[i] == 6 or lst[i] == 9:
        arr[6] += 1
    else:
        arr[lst[i]] += 1

if arr[6] % 2 == 0:
    arr[6] = arr[6] // 2
else:
    arr[6] = arr[6] // 2 + 1

print(max(arr))