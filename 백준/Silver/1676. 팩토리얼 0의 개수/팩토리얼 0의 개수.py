import math
factorial = list(str(math.factorial(int(input()))))
N = len(factorial) - 1
cnt = 0
while True:
    if factorial[N] == '0':
        cnt += 1
        N -= 1
    else:
        break
print(cnt)