def solution(n, lost, reserve):
    answer = 0
    all = [1] * (n+2)
    all[0], all[-1] = -1, -1
    for i in lost:
        all[i] -= 1
    for j in reserve:
        all[j] += 1
    for k in range(1, n+1):
        if all[k] == 2:
            if all[k-1] == 0:
                all[k] -= 1
                all[k-1] += 1
            elif all[k+1] == 0:
                all[k] -= 1
                all[k+1] += 1
                
    answer += all.count(1)
    answer += all.count(2)
                    
    
    return answer