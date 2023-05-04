# bfs 소 그림(적록색약)
import sys
from collections import deque
read = sys.stdin.readline

# 소는 빨강과 초록을 구분하지 못한다.
n = int(read())
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
graph = []
for i in range(n):
    graph.append(list(map(str, read().rstrip())))

queue = deque()
queue.append((0,0))
