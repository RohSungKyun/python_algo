import sys
from collections import deque
read = sys.stdin.readline

n, m = map(int, read().split())
graph = [list(map(str, read().strip())) for _ in range(n)] # 해당 문제는 "공백 구분이 없기" 때문에 strip을 사용해줘야 함(여기서 애를 먹음) 
visited = [[0]*m for _ in range(n)]


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
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]!='#' and visited[nx][ny]!=1:
                queue.append((nx, ny))
                visited[nx][ny] = 1

                if graph[nx][ny] == "v":
                    w+=1
                    
                if graph[nx][ny]=="o":
                    s+=1
                    
    return w, s

cnt1, cnt2 =0, 0

for i in range(n):
    for j in range(m):
        if graph[i][j]!='#' and visited[i][j]!=1:
            
            tmp = bfs(i, j)
            w, s = tmp[0], tmp[1]
            if tmp[0]<tmp[1]: # 만약 양이 더 많을 경우
                w=0
            else:
                s=0
                
            cnt1+=w
            cnt2+=s

print(cnt2, cnt1)