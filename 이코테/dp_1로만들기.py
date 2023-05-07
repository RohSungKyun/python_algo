# 5로 나누기, 3으로 나누기, 2로 나누기, 1빼기
# 1로 만드는 횟수의 최솟값
# 1<= x <= 30000
import sys

read = sys.stdin.readline
x = int(read())
dp=[0]*30001 # dp[1] = 0

for i in range(2, x+1):
    dp[i] = dp[i-1] + 1 # 현재의 수에서 1을 빼는 경우

    if i%5==0:
        dp[i] = min(dp[i], dp[i//5]+1)

    if i%3==0:
        dp[i] = min(dp[i], dp[i//3]+1)

    if i%2==0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[x]) 
