import sys
read = sys.stdin.readline
# 계단은 한 칸, 두 칸을 이동할 수 있다, 마지막 계단은 반드시 밟아야 한다. 연속하는 세 계단을 동시에 밟아도 안된다.

n = int(read())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]

for i in range(n):
    s[i] = int(read())

dp[0] = s[0]
dp[1] = s[0]+s[1]
dp[2] = max(s[1]+s[2], s[0] + s[2])

for i in range(3, n): # 밟은 계단이 n-2이거나 n-1인 경우를 고려해야 함
    dp[i] = max(dp[i-2]+s[i], dp[i-3]+s[i]+s[i-1])

print(dp[n-1])

