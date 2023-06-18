# 3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수
# 점화식 도출
# n = 2 : 3
# n = 4 : 11
# n = 6 : dp[4]*dp[2] + dp[2]*2 + 2 = 41
# n = 8 : dp[6]*dp[2] + dp[4]*2 + dp[2]*2 + 2 = 153
# ... dp[n] = dp[n-2]*3 + dp[n-4]*2 + dp[n-8]*2... + 2
import sys
read = sys.stdin.readline

n = int(read())
dp = [0]*(n+1)


if n%2 != 0:
    print(0)
else:
    dp[2]=3
    for i in range(4, n+1, 2):
        dp[i] += dp[i-2]*3 + 2
        for j in range(2, i-2, 2):
            dp[i] += dp[j]*2
    print(dp[n])