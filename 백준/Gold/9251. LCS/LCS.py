from itertools import combinations
from copy import deepcopy
first = str(input())
second = str(input())

lcs = [[0]*(len(second)+1) for _ in range(len(first)+1)]

maxV = 0
for i in range(1,len(first)+1):
    for j in range(1,len(second)+1):
        if first[i-1] != second[j-1]:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
        else:
            lcs[i][j] = lcs[i-1][j-1] + 1
        if maxV < lcs[i][j]:
            maxV = lcs[i][j]
print(maxV)