def solution(s, n):
    answer = ''
    # print(ord('a'))
    # print(ord('z'))
    for c in s:
        if c == ' ':
            answer = answer + ' '
        else:
            num = ord(c) + n
            if 65 <= ord(c) <= 90 and num > 90:
                num -= 26
            if 97 <= ord(c) <= 122 and num > 122:
                num -= 26
            answer = answer + chr(num)

    return answer