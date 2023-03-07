def solution(s):
    answer = ''
    lst = list(map(int, s.split(' ')))
    lst.sort()
    s = f'{lst[0]} {lst[-1]}'
    
    return s