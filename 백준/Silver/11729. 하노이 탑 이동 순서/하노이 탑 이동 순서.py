N = int(input())

lst = [[i for i in range(N,0, -1)], [], []]

def count(N):
    if N == 1:
        return 1
    else:
        return count(N-1) * 2 + 1

def f(a, b, n):
    if n == 1:
        print(a, b)
        return
    else:
        lst = [1, 2, 3]
        lst.pop(lst.index(a))
        lst.pop(lst.index(b))
        for c in lst:
            f(a, c, n-1)
            f(a, b, 1)
            f(c, b, n-1)

print(count(N))
f(1, 3, N)
