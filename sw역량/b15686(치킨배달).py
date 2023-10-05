# 치킨거리 : 집과 가장 가까운 치킨집의 거리(도시의 치킨거리는 해당 거리의 총합)
# 거리는 유클리드 거리로 구한다.
# 도시의 치킨거리를 줄일 수 있는 방법
# 1은 집, 2는 치킨집이다.
# m<=치킨집개수 <=13

import sys
from itertools import combinations
read = sys.stdin.readline
n, m = map(int, read().split())
graph = []
house = []
chick = []
result = sys.maxsize

for _ in range(n):
    tmp = list(map(int, read().split()))
    graph.append(tmp)



for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append([i, j])
        if graph[i][j] == 2:
            chick.append([i, j])

for c in combinations(chick, m):
    tmp = 0
    for h in house:
        chick_length = sys.maxsize
        for j in range(m):
            chick_length = min(chick_length, abs(h[0]-c[j][0])+abs(h[1]-c[j][1]))
        tmp += chick_length
    result = min(result, tmp)

print(result)