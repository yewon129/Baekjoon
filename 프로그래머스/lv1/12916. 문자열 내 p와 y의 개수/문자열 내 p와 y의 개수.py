def solution(s):
    answer = True
    s = s.lower()
    cnt_y = 0
    cnt_p = 0
    for i in s:
        if i == 'y':
            cnt_y += 1
        elif i == 'p':
            cnt_p += 1
    
    if cnt_y == cnt_p:
        return True
    else:
        return False