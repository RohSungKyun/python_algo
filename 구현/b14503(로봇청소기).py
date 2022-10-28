import sys
read = sys.stdin.readline

n, m = map(int, read().split()) # 세로 가로 크기
# d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 의미
r, c, d = map(int, read().split())

# 0은 빈칸, 1은 벽을 의미
graph = []
visited = [[False]*m for _ in range(n)]
for i in range(n):
    graph.append(list(map(int, read().split())))

visited[r][c] = True
count=1

def turn_left():
    if d==0: 
        r = r-1

    if d==1: 
        c = c+1
    if d==2: 
        r = r+1
    if d==3: 
        c = c-1


def robot():
    while True:
        dr, dc = [0, 1, -1, 0], [1, 0, 0, -1]
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0<=nr<m and 0<=nc<n and visited[nr][nc]==False and graph[nr][nc]==0:
                turn_left()
            if 0<=nr<m and 0<=nc<n and visited[nr][nc]==False and graph[nr][nc]==1:
                
