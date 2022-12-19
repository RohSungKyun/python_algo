import sys
# 1, 2, 3 더하기 + 이 문제는 규칙을 찾는 것이 중요하다. d[n] = d[n-3]+d[n-2]+d[n-1]
# 1 = 1
# 2 = 1+1, 2 =>2
# 3 = 1+1+1, 1+2, 2+1, 3 => 4

# 4 = 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1 =>7 => 1+2+4 => dp(n-3)+dp(n-2)+dp(n-1)

read = sys.stdin.readline

dp = [0]*11
dp[0] = 1
dp[1] = 2
dp[2] = 4

T = int(read())
for i in range(T):
    n = int(read())
    for j in range(3, n):
        dp[j] = dp[j-3]+dp[j-2]+dp[j-1]
    print(dp[n-1])

