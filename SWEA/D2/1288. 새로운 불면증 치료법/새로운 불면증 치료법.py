T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    k = 0
    while len(arr) > 0:
        k += 1
        number = N * k
        while number != 0:
            if (number % 10) in arr:
                arr.remove(number % 10)
            number = number // 10

    print(f'#{tc} {N * k}')

