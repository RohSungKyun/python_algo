import sys
from collections import deque
read = sys.stdin.readline

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

n, m, t = map(int, read().split())

graph = [list(map(int, read().split())) for i in range(n)]


def bfs():
    global sword
    visited = [[0]*m for i in range(n)]
    queue = deque()
    queue.append((0, 0, 0)) # x, y, time
    visited[0][0] = 1
    while queue:
        tmp = queue.popleft()
        x = tmp[0]
        y = tmp[1]
        time = tmp[2]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]!=1 and visited[nx][ny]==0: # 여기서 graph를 ==0이 아니라 !=1로 해야함 2가 있기 때문
                if nx == n-1 and ny == m-1:
                    return time+1
                if graph[nx][ny]==2:
                    sword = abs(n-1-nx) + abs(m-1-ny) + time+1
                visited[nx][ny] = 1
                queue.append((nx, ny, time+1))
    return float('inf')

sword = float('inf')
ans = min(bfs(), sword)
if ans == sys.maxsize or ans>t:
    print("Fail")
else:
    print(ans)