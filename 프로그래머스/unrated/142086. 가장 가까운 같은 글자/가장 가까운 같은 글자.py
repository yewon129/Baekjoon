def solution(s):
    answer = [-1]*len(s)
    for i in range(len(s)):
        box = s[:i]
        for j in range(i-1, -1,-1):
            if box[j] == s[i]:
                answer[i] = i-j
                break
    return answer