n, m = map(int, input().split())

def factorial(n):
    if n == 1 or n ==  2:
        return n
    else:
        return n * factorial(n-1)

print(factorial(n)//factorial(m)//factorial(n-m))