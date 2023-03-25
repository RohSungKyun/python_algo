# 1 : 길, 0 : 괴물
import sys
from collections import deque
read = sys.stdin.readline

n, m = map(int, read().split())
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
graph = [list(map(int, read().strip())) for _ in range(n)]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:

                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(bfs(0, 0))
