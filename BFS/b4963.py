import sys
from collections import deque
read = sys.stdin.readline

dx = [1, 0, -1, 0, 1, -1, 1, -1] # 대각선 포함
dy = [0, 1, 0, -1, 1, -1, -1, 1]


while True:
    queue = deque()
    w, h = map(int, read().split())
    cnt=0
    if w==0 and h==0:
        exit()
    graph = [list(map(int, read().split())) for i in range(h)]
    visited = [[0]*w for i in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1 and visited[i][j]==0:
                visited[i][j]=1
                queue.append((i, j))


                while queue:
                    tmp = queue.popleft()
                    for k in range(8):
                        nx = tmp[0]+dx[k]
                        ny = tmp[1]+dy[k]
                        if 0<=nx<h and 0<=ny<w and graph[nx][ny]==1 and visited[nx][ny]!=1:
                            visited[nx][ny] = 1
                            queue.append((nx, ny))
                cnt+=1
    print(cnt)
