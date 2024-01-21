# 서로 다른 무게의 볼링공을 고르는 경우의 수
# 시간복잡도 해결

import sys
read = sys.stdin.readline

n, m = map(int, read().split())
balls = list(map(int, read().split()))

weight = [0]*11 # 무게는 10까지 존재함
for ball in balls: # 무게별 볼링공의 개수
    weight[ball]+=1

result = 0
for i in range(1, m):
    n -= weight[i] # a가 선택할 경우의 수 제거
    result += weight[i]*n

print(result)

# =========================================================

# 시간복잡도 O(N^2)
"""ans = 0
for i in range(n-1):
    for j in range(i, n):
        if balls[i] != balls[j]:
            ans+=1

print(ans)
"""