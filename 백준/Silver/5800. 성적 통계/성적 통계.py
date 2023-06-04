K = int(input())

for c in range(1, K+1):
    lst = list(map(int, input().split()))
    n = lst[0]
    lst = lst[1:]
    lst.sort(reverse=True)
    maxV = lst[0]
    minV = lst[-1]
    gap = 0
    for i in range(1,n):
        g = lst[i-1] - lst[i]
        if g > gap:
            gap = g


    print(f'Class {c}')
    print(f'Max {maxV}, Min {minV}, Largest gap {gap}')