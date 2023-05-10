def solution(n, m):
    k = max(n,m)
    l = min(n,m)
    flag_k = 0
    flag_l = 0
    while 1:
        if k % n == 0 and k % m == 0:
            flag_k = 1
        else:
            k += 1
        if n % l == 0 and m % l == 0:
            flag_l = 1
        else:
            l -= 1
        if flag_k == 1 and flag_l == 1:
            break
    return [l,k]