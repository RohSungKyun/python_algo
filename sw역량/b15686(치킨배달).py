# 치킨거리 : 집과 가장 가까운 치킨집의 거리(도시의 치킨거리는 해당 거리의 총합)
# 거리는 유클리드 거리로 구한다.
# 도시의 치킨거리를 줄일 수 있는 방법
# 1은 집, 2는 치킨집이다.
# m<=치킨집개수 <=13

import sys
read = sys.stdin.readline
n, m = map(int, read().split())
graph = []
for _ in range(n):
    tmp = list(map(int, read().split()))
    graph.append(tmp)

