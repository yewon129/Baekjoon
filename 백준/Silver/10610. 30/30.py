lst = list(map(int,input()))

lst.sort(reverse=True)
if lst[-1] != 0:
  print(-1)
else:
  if sum(lst) % 3 != 0:
    print(-1)
  else:
    for i in lst:
      print(i, end='')