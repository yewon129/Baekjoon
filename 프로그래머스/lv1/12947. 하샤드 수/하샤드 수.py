def solution(x):
    num = str(x)
    sumV = 0
    for i in range(len(num)):
        sumV += int(num[i])
    
    if x % sumV == 0:
        return True
    else:
        return False