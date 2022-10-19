import sys
read = sys.stdin.readline
# 3으로 나누어 떨어지면 3으로나누고, 2일 경우 2로 나눈다. 1을 빼는 3가지 연산이 가능

n  = int(read())
dp = [0]*(n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1]+1
    if i%2==0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i%3==0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[-1])