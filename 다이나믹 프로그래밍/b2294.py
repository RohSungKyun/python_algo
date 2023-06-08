# 동전 2
# 추가된 조건 : 사용한 동전의 최소 개수, 불가능한 경우 -1 을 도출해야 한다.


import sys
read = sys.stdin.readline

n, k = map(int, read().split())
coin = []
dp = [0 for _ in range(k+1)] # dp에는 동전의 최소개수를 저장
dp[0] = 0 # 0을 만드는 동전의 최소 개수는 0이다.

for i in range(n):
    coin.append(int(read()))

for i in coin:
    for j in range(i, k+1):
        if dp[j] >0:
            dp[j] = min(dp[i], dp[j-i]+1)
print(dp[k])


