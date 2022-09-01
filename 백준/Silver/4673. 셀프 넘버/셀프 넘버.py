numbers = set(range(1, 10001))
nums = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    nums.add(i)

answers = sorted(numbers - nums)
for k in answers:
    print(k)