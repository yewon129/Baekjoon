T = 10
for n in range(1, T+1):
    tc = int(input())
    ladder = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]  # 양 옆에 [0]을 더해서 인덱스 에러 방지
 
    di = [-1, 0, 0]  # 상 좌 우
    dj = [0, -1, 1]
 
    x = 99
    for j in range(1, 101):
        if ladder[x][j] == 2:
            y = j
            break
 
    x = 98  # ladder[99][y]는 2일것이기 때문에 위로 한칸 올라가서 진행 
    while x > 0:
        if -1 <= x < 101 and -1 <= y < 101:
            if ladder[x][y] == 1:
                if ladder[x][y-1] == 1:  # 왼쪽에 1이 있으면 왼쪽으로 진행 후, 이전의 사다리를 지움
                    ladder[x][y] = 0
                    x, y = x + di[1], y + dj[1]
                elif ladder[x][y+1] == 1:  # 오른쪽이 1이면 오른쪽으로 진행 후, 이전의 사다리 지움
                    ladder[x][y] = 0
                    x, y = x + di[2], y + dj[2]
                elif ladder[x-1][y] == 1:  # 좌우 1 없으면 위로 진행
                    x, y = x + di[0], y+dj[0]
 
    print(f'#{tc} {y-1}')