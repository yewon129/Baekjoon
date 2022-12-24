a, b = map(int, input().split())

def func(a, b):
    while b:
        mod = b
        b = a % b
        a = mod
    return a

print(a*b//func(a, b))