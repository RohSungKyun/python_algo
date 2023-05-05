# bfs 소 그림(적록색약)
import sys
from collections import deque
read = sys.stdin.readline

# 소는 빨강과 초록을 구분하지 못한다.
n = int(read())

graph = []
for i in range(n):
    graph.append(list(map(str, read().rstrip())))

queue = deque()
visited = [[False]*n for _ in range(n)] 

def BFS(x, y):
    queue.append((x, y))
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

cnt1, cnt2 = 0, 0
# 적록색약이 아닌 경우
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            BFS(i, j)
            cnt1+=1

# 적록색약인 경우 그래프 구조를 바꾼다.
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

visited = [[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            BFS(i, j)
            cnt2+=1

print(cnt1, cnt2)



