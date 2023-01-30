T = int(input())

def gcd(a, b):
  while b != 0:
    r = a % b
    a = b
    b = r
  return a

def lcm(a, b):
  return (a * b) // gcd(a, b)

for tc in range(T):
  A, B = map(int, input().split())
  if A > B:
    ans = lcm(A, B)
  else:
    ans = lcm(B, A)
  
  print(ans)