def solution(n, s):
    answer = []
    if s // n == 0:
        return [-1]
    if n == 1:
        return [s]
    if s % n == 0:
        return [s // n for _ in range(n)]
    else:
        lst = [s//n] * n 
        s %= n
        for i in range(s):
            lst[i] += 1        
        return sorted(lst)