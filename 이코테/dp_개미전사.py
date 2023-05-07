# 개미가 정찰병에게 들키지 않고 약탈하기 위해서는 한칸 이상 떨어진 식량창고를 약탈해야 한다.
# 일직선상 최대한 많은 식량을 얻기를 원한다.
import sys
read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().split()))
dp = [0]*1001

dp[1] = max(arr[0], arr[1])
for i in range(n):
    dp[i] = max(dp[i-1], dp[i-2]+arr[i]) # 경우의 수는 두 개 i-1번째 창고를 털거나, i-2번째 창고를 털거나

print(dp[n-1])