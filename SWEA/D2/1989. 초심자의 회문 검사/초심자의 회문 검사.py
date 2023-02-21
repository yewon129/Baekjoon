T = int(input())

for tc in range(1, T+1):
  word = str(input())
  ans = 1
  for i in range(len(word)//2):
    if word[i] != word[-1-i]:
      ans = 0
      break
  
  print(f'#{tc} {ans}')