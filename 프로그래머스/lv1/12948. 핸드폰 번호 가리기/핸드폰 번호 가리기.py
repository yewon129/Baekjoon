def solution(phone_number):
    N = len(phone_number)
    answer = '*'*(N-4) + phone_number[-4:]
    return answer