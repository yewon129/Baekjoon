def solution(N, number):
    answer = -1
    dp = []
    if number == 1:
        return 1
    
    for i in range(1, 9):
        box = set()
        box.add(int(str(N)*i))
        for j in range(0, i-1):
            for op1 in dp[j]:
                for op2 in dp[-j-1]:
                    box.add(op1 - op2)
                    box.add(op1 + op2)
                    box.add(op1 * op2)
                    if op2 != 0:
                        box.add(op1 // op2)
        if number in box:
            answer = i
            break
        
        dp.append(list(box))
    
    return answer