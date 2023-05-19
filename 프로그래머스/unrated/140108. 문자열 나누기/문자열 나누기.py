def solution(s):
    answer = 0
    while s:
        x = s[0]
        cnt_s = 1
        cnt_d = 0
        flag = 0
        for i in range(1, len(s)):
            if s[i] == x:
                cnt_s += 1
            else:
                cnt_d += 1
            if cnt_s == cnt_d:
                answer += 1
                s = s[i+1:]
                flag = 1
                break
        if flag == 0:
            answer += 1
            break
    return answer