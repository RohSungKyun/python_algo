import sys
read = sys.stdin.readline
t = int(read())

for _ in range(t):
    dp = [[0]*2 for _ in range(41)]
    dp[0], dp[1] = [1, 0], [0, 1]
    n = int(read())
    for i in range(2, n+1):
        dp[i][0] = dp[i-2][0]+dp[i-1][0]
        dp[i][1] = dp[i-2][1]+dp[i-1][1]
    print(*dp[n])
