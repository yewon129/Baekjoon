import copy
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
box = []
box = copy.deepcopy(lst)

box = sorted(list(set(box)))
dic = {box[i] : i for i in range(len(box))}

for i in range(N):
    print(dic[lst[i]], end=' ')