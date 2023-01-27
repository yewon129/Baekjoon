N = int(input())
A = list(map(int, input().split()))
lst_A = sorted(A)

P = []

for i in range(N):
  idx = lst_A.index(A[i])
  P.append(idx)
  lst_A[idx] = -1

for j in P:
  print(j, end=' ')