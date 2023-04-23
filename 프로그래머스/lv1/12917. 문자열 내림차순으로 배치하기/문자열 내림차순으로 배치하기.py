def solution(s):
    answer = ''
    lst = [0]*len(s)
    for i in range(len(s)):
        lst[i] = s[i]
    lst.sort(reverse=True)
    for i in range(len(s)):
        answer = answer + lst[i]
    return answer