import sys
from collections import deque
read = sys.stdin.readline

n, m = map(int, read().split())
graph = [list(map(str, read().split())) for _ in range(m)]
visited = [[0]*n for _ in range(m)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    w, s = 0, 0

    if graph[x][y] == "v":
        w+=1
    if graph[x][y] == "o":
        s+=1
    
    while queue:
        x, y = queue.popleft()
        for i in range(0):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]!="#" and visited[nx][ny]!=1:
                queue.append((nx, ny))
                visited[nx][ny] = 1

                if graoh[nx][ny] == "v":
                    w+=1
                if graph[nx][ny]=="o":
                    s+=1
    return w, s

bfs(0, 0)