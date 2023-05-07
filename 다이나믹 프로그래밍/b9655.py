# 돌게임
# 돌을 1개 또는 3개를 가져갈 수 있다. 마지막 돌을 가져가는 사람이 이기게 된다.
# 두 사람이 완벽하게 게임을 함 : 최소 횟수로 끝을 냄
# 상근이가 먼저 시작

import sys
read = sys.stdin.readline

n = int(read())
dp = [0]*1001
dp[1] = 1

for i in range(2, n+1): # 보텀업 방식이용
    dp[i] = dp[i-1]+1 # 1씩 빼기

    if i>=3: # 3 이상이라면

        dp[i] = min(dp[i], dp[i-3]+1)

if dp[n]%2 == 0:
    print("CY")
else:
    print("SK")

