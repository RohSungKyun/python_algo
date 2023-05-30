# 평범한 배낭문제
# 냅색 알고리즘 : 직접 표를 그리면 이해하기 쉽다.
import sys
read = sys.stdin.readline

n, k = map(int, read().split()) # 물건의 수, 견딜 수 있는 최대 무게
arr = [[0, 0]] # 코드의 가독성이 좋게 0번쨰 인덱스는 0,0을 넣어준다.

for i in range(n):
    arr.append(list(map(int, read().split())))
dp = [[0]*(k+1) for _ in range(n)] # 이중 for 문을 위한 dp테이블

for i in range(1, n+1):
    w = arr[i][0]
    v = arr[i][1]
    for j in range(1, k+1): # 현재 확인하고자 하는 무게j
        if j<w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[n][k])
