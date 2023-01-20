n=int(input())
answer=5
nums = list(int(input()) for _ in range(n))

for i in range(n):
    cnt1=4
    cnt2=4
    for j in range(n):
        if nums[i]+5>nums[j] and nums[i]<nums[j]:
            cnt1-=1
        elif nums[i]-5<nums[j] and nums[i]>nums[j]:
            cnt2-=1
    answer=min(answer, cnt1, cnt2)
print(answer)