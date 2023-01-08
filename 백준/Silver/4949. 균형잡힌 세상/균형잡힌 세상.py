while 1:
  stack = []
  lst = input()
  if lst == '.':
    break
  ans = 'yes'
  for i in range(len(lst)):
    if lst[i] == '(' or lst[i] == '[':
      stack.append(lst[i])
    elif lst[i] == ']':
      if len(stack) != 0 and stack[-1] == '[':
        stack.pop()
      else:
        ans = 'no'
        break
    elif lst[i] == ')':
      if len(stack) != 0 and stack[-1] == '(':
        stack.pop()
      else:
        ans = 'no'
  if len(stack) != 0:
    ans = 'no'
  print(ans)