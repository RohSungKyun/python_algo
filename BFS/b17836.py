import sys
from collections import deque

read = sys.stdin.readline

n, m, t = map(int, read().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, read().split())))

print(graph)
