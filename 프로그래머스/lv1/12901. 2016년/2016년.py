def solution(a, b):
    answer = ''
    months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    num = 0
    for i in range(1, a):
        num += months[i]
    num += b
    days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    answer = days[num % 7]
    return answer