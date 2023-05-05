def solution(board):
    answer = 0
    n = len(board[0])
    d = [[0,1], [1,0], [0,-1], [-1,0],[-1,-1],[1,1],[-1,1],[1,-1]]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for di, dj in d:
                    ni, nj = i+di, j+dj
                    if 0<=ni<n and 0<=nj<n and board[ni][nj] == 0:
                        board[ni][nj] = 2
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1
    return answer