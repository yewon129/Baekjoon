def solution(prices):
    N = len(prices)
    answer = [0] * N
    i = 0
    for i in range(N-1):
        for j in range(i+1, N):
            answer[i] += 1
            if prices[i] > prices[j]:
                break
    answer[-1] = 0
    return answer