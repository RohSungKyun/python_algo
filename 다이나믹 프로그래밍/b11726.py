import sys
read = sys.stdin.readline

n = int(read())

dp = [0]*(n+1)
dp[1] = 1
if n !=1:
    dp[2] = 2 #default로 2로 설정

for i in range(3, n+1):
    dp[i] = dp[i-1]+dp[i-2] # 규칙 : 이전 값과 그 전의 값의 합의 방법의 개수가 같다.(점화식)
print(dp[n]%10007)


