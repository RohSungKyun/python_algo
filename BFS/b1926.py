# 그림 1로 되있는 부분이 그림의 영역이다.

import sys
from collections import deque
read  = sys.stdin.readline

n, m = map(int, read().split())
dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]
graph = []
visited = [[False]*m for _ in range(n)]


for i in range(n):
    tmp = list(map(int,read().split()))
    graph.append(tmp)

def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    visited[a][b] = True
    global area
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1 and visited[nx][ny] == False:
                queue.append([nx, ny])
                visited[nx][ny] = True
                area+=1
    print(area)
cnt = 0
area=0
max_area = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == False:
            bfs(i, j)
            cnt+=1
            if max_area < area:
                max_area = area
                area = 1 # 초기화

print(cnt)
print(max_area)