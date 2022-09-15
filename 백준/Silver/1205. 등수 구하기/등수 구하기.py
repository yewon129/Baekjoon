N, new, P = map(int, input().split())
if N == 0:
    print(1)
else:
    lst = list(map(int, input().split()))
    lst.append(new)
    lst.sort(reverse=True)
    if lst.index(new) + 1 > P:
        print(-1)
    else:
        if N == P and new == lst[-1]:
            print(-1)
        else:
            print(lst.index(new)+1)
