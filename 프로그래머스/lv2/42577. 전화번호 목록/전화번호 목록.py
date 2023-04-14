def solution(phone_book):
    if len(phone_book) == 1:
        return True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        flag = 0
        for j in range(len(phone_book[i])):
            if phone_book[i][j] != phone_book[i+1][j]:
                flag = 1
                break
        if flag == 0:
            return False
    return True