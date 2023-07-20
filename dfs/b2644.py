# 촌수계산
import sys
read = sys.stdin.readline
n = int(read())
p1 , p2 = map(int, read().split())
m = int(read())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    x, y = map(int, read().split())
    graph[x].append(y)
    graph[y].append(x)

print(graph)
