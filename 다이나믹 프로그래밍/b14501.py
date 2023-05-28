# 퇴사
# 기간에 따라 상담을 건너뛸 필요가 있다. n 기간 안에서만 이루어 져야 한다.

import sys
read = sys.stdin.readline

n = int(read())
arr = []

for i in range(n):
    t, p = map(int, read().split())
    arr.append([t, p])

# 최대 이익 이므로 가격을 테이블에 저장
dp = [0]*(n+1)

"""
# bottom-up 방식
for i in range(n):
    for j in  range(i+arr[i][0], n+1):
        if dp[j] < dp[i] + arr[i][1]:
            dp[j] = dp[i] + arr[i][1]

print(dp[-1])"""

#  top-down 방식 (역순으로 내려옴)

for i in range(n-1, -1, -1):
    if i+arr[i][0] > n: # i일에 상담하는 것이 상담일을 초과할 경우
        dp[i] = dp[i+1] # 이전 결과를 그대로 저장
    else:
        dp[i] = max(dp[i+1], arr[i][1] + dp[i+arr[i][0]])

print(dp[0])
print(dp)