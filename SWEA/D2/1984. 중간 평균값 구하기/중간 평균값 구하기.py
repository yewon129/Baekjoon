T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    maxV = arr[0]
    minV = arr[0]
    for number in arr:
        if minV > number:
            minV = number
        if maxV < number:
            maxV = number

    arr.remove(maxV)
    arr.remove(minV)

    total = 0
    for number in arr:
        total += number

    print(f'#{tc} {round(total/8)}')