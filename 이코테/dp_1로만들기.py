
import sys

read = sys.stdin.readline
x = int(read())
dp=[0]*30001

for i in range(2, x-1):
    dp[i] = dp[i-1] + 1
    if i%5==0:
        dp[i] = min(dp[i], dp[i//5]+1)
