# 동전의 가치의 합이 k가 되도록 하는 모든 경우의 수
# 동전의 재사용 가능
# 

import sys
read = sys.stdin.readline

n, k = map(int, read().split())
dp = [0 for i in range(k+1)]
dp[0] = 1 # k짜리 코인 1개만 이용하는 경우
coin = []
for i in range(n):
    coin.append(int(read()))

for i in coin:
    for j in range(i, k+1):
        dp[j] += dp[j-i]
print(dp[k])


