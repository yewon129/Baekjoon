def solution(n):
    n = str(n)
    lst = []
    for i in range(len(n)-1, -1, -1):
        lst.append(int(n[i]))
    return lst