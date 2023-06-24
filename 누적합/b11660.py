# 구간 합 구하기 5 + 다이나믹 프로그래밍
# x, y까지의 구간합을 구할려면 (x, y-1) + (x-1, y) - (x-1, y-1)로 저장해 나간다.
import sys
read = sys.stdin.readline

n, m = map(int, read().split())
graph = []
prefix_sum = [[0]*(n+1) for _ in range(n+1)]


for _ in range(n):
    graph.append(list(map(int, read().split())))

for i in range(1, n+1):
    for j in range(1, n+1):
        prefix_sum[i][j] = prefix_sum[i][j-1] + prefix_sum[i-1][j] - prefix_sum[i-1][j-1] + graph[i-1][j-1] # 마지막에 채우는 그래프의 값
 
for _ in range(m):
    x1, y1, x2, y2 = map(int, read().split()) # x1, y1 ~ x2, y2까지
    result = prefix_sum[x2][y2] - prefix_sum[x2][y1-1] - prefix_sum[x1-1][y2] + prefix_sum[x1-1][y1-1]
    print(result)

