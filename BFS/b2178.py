# 미로탈출
import sys
import collections
read = sys.stdin.readline

n, m = map(int, read().split())
graph = [list(read().rstrip()) for i in range(n)]
visited = [[0]*(m) for i in range(n)]

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

queue = collections.deque()
queue.append((0, 0))
visited[0][0] = 1

while queue:
    x, y = queue.popleft()
    if x == n-1 and y == m-1:
        print(visited[x][y])
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and graph[nx][ny]=='1':
            queue.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
    
