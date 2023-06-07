import sys
read = sys.stdin.readline

t = int(read())

for _ in range(t):
    n = int(read())
    dp = [0]*(101)

    # init dp table
    dp[0] = dp[1] = dp[2] = 1
    dp[3] = dp[4] = 2
    if n < 6:
        print(dp)
        print(dp[n-1])
    else:
        for i in range(4, n):
            dp[i] = dp[i-3] + dp[i-2]
        print(dp[n-1])