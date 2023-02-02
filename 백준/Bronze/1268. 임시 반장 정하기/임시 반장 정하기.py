N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
students = [[0] * N for _ in range(N)]

for i in range(5):
  for j in range(N):
    for k in range(j+1, N):
      if lst[j][i] == lst[k][i]:
        students[k][j] = 1
        students[j][k] = 1

cnt = []
for s in students:
  cnt.append(s.count(1))

print(cnt.index(max(cnt)) + 1)