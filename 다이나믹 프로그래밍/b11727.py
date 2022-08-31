import sys
read  = sys.stdin.readline
n = int(read())

dp = [0]*(n+1)

dp[1] = 1
if n != 1:
    dp[2] = 3 # 2x2타일이 생겼음

for i in range(3, n+1):
    dp[i] = dp[i-1] + 2*dp[i-2]
print(dp[n]%10007)
