# 가로 n, 세로 2의 직사각형을 1x2, 2x1, 2x2의 덮개를 이용해 채우는 것
# 바닥을 채우는 모든 경우의 수를 796796으로 나눈 나머지를 출력
# <타일링 유형>
import sys
read = sys.stdin.readline
n = int(read())

dp = [0]*1001

dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = (dp[i-1]+dp[i-2]*2)%796796

print(dp[n])