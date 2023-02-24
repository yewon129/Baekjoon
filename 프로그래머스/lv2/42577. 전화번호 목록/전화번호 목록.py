def solution(phone_book):
    answer = True
    N = len(phone_book)
    if N == 1:
        return True
    phone_book.sort()
    for i in range(N-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
    return answer