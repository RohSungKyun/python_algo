import sys
read = sys.stdin.readline
t = int(read())

for _ in range(t):
    n, m = map(int, read().split())
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 1: # 서쪽 사이트가 1개라면
                dp[i][j] = j
                continue
            if i == j: # 사이트의 수가 같다면
                dp[i][j] = 1
            else:
                if j > i:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    print(dp[n][m])
