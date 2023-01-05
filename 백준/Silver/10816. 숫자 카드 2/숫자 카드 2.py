N = int(input())
lst1 = list(map(int, input().split()))
M = int(input())
lst2 = list(map(int, input().split()))

arr1 = [0] * 10000001
arr2 = [0] * 10000001

for i in range(N):
  if lst1[i] >= 0:
    arr1[lst1[i]] += 1
  else:
    arr2[lst1[i]] += 1

for j in range(M):
  if lst2[j] >= 0:
    print(arr1[lst2[j]], end=' ')
  else:
    print(arr2[lst2[j]], end=' ')