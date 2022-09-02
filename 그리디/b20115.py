import sys
read = sys.stdin.readline
n = int(read())
nums = list(map(int, read().split()))

nums = sorted(nums)[::-1]
ans=0

for i in range(len(nums)):
    if ans == 0:
        ans = nums[0]
        continue
    ans = ans+(nums[i]/2)
print(ans)
    