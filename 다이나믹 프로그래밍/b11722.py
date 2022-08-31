import sys
read = sys.stdin.readline
n = int(read())
nums = list(map(int, read().split()))[::-1] # 이전 문제에서 배열을 뒤집으면 똑같다
dp = [0]*(n+1)

for i in range(n):
    tmp = 0
    for j in range(i):
        if nums[i]>nums[j]:
            tmp = max(tmp, dp[j])
    dp[i] = tmp+1
print(max(dp))