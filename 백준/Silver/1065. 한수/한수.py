N = int(input())

cnt = 0
if N < 100:
    print(N)
else:
    cnt += 99
    for i in range(100, N+1):
        nums = list(map(int, str(i)))
        if nums[0] - nums[1] == nums[1] - nums[2]:
            cnt += 1
    print(cnt)