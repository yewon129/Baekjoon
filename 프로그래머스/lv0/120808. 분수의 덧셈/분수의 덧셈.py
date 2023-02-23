def solution(numer1, denom1, numer2, denom2):
    a = numer1 * denom2 + numer2 * denom1
    b = denom1 * denom2
    n = min(a,b)
    while n:
        if a % n == 0 and b % n == 0:
            a //= n
            b //= n
        n -= 1
    answer = [a, b]
    return answer