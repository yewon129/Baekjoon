T = int(input())

zero = [1, 0, 1]
one = [0,1,1]

def func(n):
    length = len(zero)
    if length <= n:
        for i in range(length, n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])

for _ in range(T):
    n = int(input())
    func(n)
    print(zero[n], one[n])