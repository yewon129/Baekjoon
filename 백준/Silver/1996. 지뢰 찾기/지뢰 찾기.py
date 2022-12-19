N = int(input())

arr = [list(map(str, input())) for _ in range(N)]

ans = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] != '.':
            ans[i][j] = '*'
        else:
            for di, dj in [(-1,-1), (-1,0), (-1,1),(0,-1), (0,1), (1,-1),(1,0), (1,1)]:
                if 0<=i+di<N and 0<=j+dj<N and arr[i+di][j+dj] != '.':
                    ans[i][j] += int(arr[i+di][j+dj])
            if ans[i][j] >= 10:
                ans[i][j] = 'M'

for i in range(N):
    for j in range(N):
        print(ans[i][j], end='')
    print()