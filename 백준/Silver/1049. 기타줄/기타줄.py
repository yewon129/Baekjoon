N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]

pack = sorted(lst, key=lambda x : x[0])
one = sorted(lst, key=lambda x : x[1])


minV = lst[0][0]*N

if pack[0][0] <= one[0][1]*6:
  minV = pack[0][0] * (N//6) + one[0][1] * (N % 6)
  if pack[0][0] < one[0][1] * (N%6):
    minV = pack[0][0] * (N//6 + 1)
else:
  minV = one[0][1] * N

print(minV)