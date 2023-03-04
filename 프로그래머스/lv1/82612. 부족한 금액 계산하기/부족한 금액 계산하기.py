def solution(price, money, count):
    need = 0
    cnt = 0
    while cnt < count:
        cnt += 1
        need += cnt * price
    answer = need - money
    if answer < 0:
        answer = 0
    return answer