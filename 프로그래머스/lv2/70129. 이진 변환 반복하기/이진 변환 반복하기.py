def solution(s):
    change = 0
    num = 0
    while 1:
        if s == '1':
            break
        num += s.count('0')
        s = s.replace('0', '').strip()
        n = len(s)
        change += 1
        temp = bin(n)
        s = temp[2:]
    return [change, num]
