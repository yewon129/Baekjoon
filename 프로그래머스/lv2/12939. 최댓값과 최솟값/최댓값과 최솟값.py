def solution(s):
    answer = ''
    lst = list(map(int, s.split(' ')))
    s = f'{min(lst)} {max(lst)}'
    
    return s