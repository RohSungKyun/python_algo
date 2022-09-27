import copy
import sys
read = sys.stdin.readline
n, m = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(n)]
graph_copy = copy.deepcopy(graph)
dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]
max_area =0 

def dfs(x, y, virus):
    virus[x][y] = 2 #바이러스 감염
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m and virus[nx][ny]==0:
            virus[nx][ny]=2
            dfs(nx, ny, virus)

def wall(start, cnt):
    global max_area
    
    if cnt==3:
        virus = copy.deepcopy(graph_copy)
        for i in range(n):
            for j in range(m):
                if virus[i][j]==2:
                    dfs(i, j, virus)
        safe_area = sum( _.count(0) for _ in virus)
        max_area = max(max_area, safe_area)
    else:
        for i in range(start, n*m):
            r = i//m
            c = i % m
            if graph_copy[r][c]==0:
                graph_copy[r][c]=1
                wall(i, cnt+1)
                graph_copy[r][c]=0

wall(0, 0)
print(max_area)
