import sys
read = sys.stdin.readline
# 마신 후 다시 원래 자리로, 세 잔을 연속해서 마실 수 없다.
n = int(read())
dp = [0]*10001
wines=[0]*10001
for i in range(n):
    wines[i] = int(read())

dp[0] = wines[0]
dp[1] = wines[0]+wines[1] # 2까지는 최대값이 두칸을 연속으로 간 경우이므로 더해 준다.
dp[2] = max(wines[2]+wines[0], wines[1]+wines[2], dp[1])
for i in range(3, n):
    dp[i] = max(dp[i-2]+wines[i], dp[i-3]+wines[i]+wines[i-1], dp[i-1])

print(max(dp))