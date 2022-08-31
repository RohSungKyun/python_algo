# 다이나믹 프로그래밍, 비트마스킹, dfs
import sys
read = sys.stdin.readline
n = int(read())

graph=[]
for _ in range(n):
    graph.append(list(map(int, read().split())))

print(graph)