# 구멍 : 0, 칸막이 : 1
# 생성되는 아이스크림의 개수를 구하시오 -> 연결 요소의 개수를 구하시오
# 모든 노드를 체크해야함 -> dfs

import sys
read = sys.stdin.readline

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
n, m = map(int, read().split())
graph = [list(map(int, read().strip())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
space = False

def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 and visited[nx][ny] == False:
            visited[nx][ny] = True
            x, y = nx, ny
            dfs(x, y)
    return
 

ans = 0

for i in range(n):
    for j in range(m):
        if graph[i][j]==0 and visited[i][j] == False: # 현재 위치가 0이고 방문x
            print(i, j)
            dfs(i, j)
            ans+=1
print(ans)