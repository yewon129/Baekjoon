N = int(input())
lst = set(list(map(int, input().split())))
lst = list(lst)
lst.sort()
for i in lst:
    print(i, end=' ')
