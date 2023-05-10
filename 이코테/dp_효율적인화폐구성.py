

import sys
read = sys.stdin.readline

n, m = map(int, read().split())
dp = [10001]*(m+1) # 초기화 : 10001은 특정 금액을 만들 수 있는 화폐 구성이 가능하지 않다는 것.
dp[0] = 0
arr = []

for i in range(n):
    arr.append(int(read()))

for i in range(n): # 각 화폐 단위 별로 테이블에 저장
    for j in range(arr[i], m+1):
        if dp[j - arr[i]] != 10001:
            dp[j] = min(dp[j], dp[j - arr[i]]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])


