import sys
read = sys.stdin.readline
# 유기농 배추
sys.setrecursionlimit(10000)
t = int(read())

def dfs(x, y):
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<m and 0<=ny<n and graph[ny][nx]==1:
            graph[ny][nx] = -1
            dfs(nx, ny)

for _ in range(t):
    m, n, k = map(int, read().split()) # 가로, 세로, 배추의 개수
    graph = [[0]*m for _ in range(n)]
    cnt=0
    for i in range(k):
        x, y = map(int, read().split())
        graph[y][x] = 1
    
    for i in range(m):
        for j in range(n):
            if graph[j][i]==1:
                dfs(i, j)
                cnt+=1
    print(cnt)