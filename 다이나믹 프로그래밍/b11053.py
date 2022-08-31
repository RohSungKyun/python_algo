import sys
read = sys.stdin.readline
n = int(read())
a = list(map(int, read().split()))

dp = [0]*(n+1)

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp)+1)