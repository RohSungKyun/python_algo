# 동전 2
# 추가된 조건 : 사용한 동전의 최소 개수, 불가능한 경우 -1 을 도출해야 한다.


import sys
read = sys.stdin.readline

n, k = map(int, read().split())
coins = []
dp = [10001 for _ in range(k+1)] # dp에는 동전의 최소개수를 저장
dp[0] = 0 # 0을 만드는 동전의 최소 개수는 0이다.

for i in range(n):
    coins.append(int(read()))

for coin in coins:
    for i in range(coin, k+1): # coin으로 k를 만드는 최소개수
        if dp[i]>0:
            dp[i] = min(dp[i], dp[i-coin] + 1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
