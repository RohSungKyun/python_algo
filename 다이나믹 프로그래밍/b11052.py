import sys
read = sys.stdin.readline
# 카드 i개 팩은 pi의 가격으로 구매 가능 => 최대의 가격을 써서 카드를 구매하고자 함

n = int(read())
p = [0]+list(map(int, read().split())) # 배열의 처음은 계산에서 생략한다.
dp = [0]*(n+1)

# 점화식 dp[i] = dp[i-j]+p[j]
for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j]+p[j])

print(dp[i])