def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if ord(i) not in range(48, 58):
                return False
    else:
         return False       
    return True