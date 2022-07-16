N, X = map(int, input().split())
lst= list(map(int, input().split()))

for x in lst:
    if x < X:
        print(x, end=" ")