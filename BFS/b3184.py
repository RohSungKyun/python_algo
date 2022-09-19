from collections import deque
import sys
read = sys.stdin.readline
#  '.' (점)은 빈 필드를 의미하며, 글자 '#'는 울타리를, 'o'는 양, 'v'는 늑대를 의미
n, m = map(int, read().split())

graph = [list(map(str, read().split())) for _ in range(m)]
visited = [[0]*n for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    global w, s

    queue = deque()
    queue.append((x, y))
    visited[x][y] == 1
    
    if graph[x][y]=='v':
        w+=1
    if graph[x][y]=='o':
        s+=1
    
    while queue:
        tmp = queue.popleft()
        for i in range(4):
            nx = tmp[0]+dx[i]
            ny = tmp[1]+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]!='#' and visited[nx][ny]==0:
                queue.append((nx, ny))
                visited[nx][ny]=1


cntW, cntS = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j]!='#' and visited[i][j]==0:
            w, s = 0, 0
            cnt = bfs(i, j)
            if s>w:
                w=0
            else:
                s=0
            cntS+=s
            cntW+=w
print(cntW, cntS)