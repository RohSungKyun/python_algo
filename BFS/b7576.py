# 토마토 쉬운거
import sys
from collections import deque
read = sys.stdin.readline

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
queue = deque()
graph=[]
m, n = map(int, read().split())

# 익어있는 위치를 파악을 해야한다.

for i in range(n):
    tmp =[] # 빈리스트로 초기화
    tmp = list(map(int, read().split()))
    graph.append(tmp)
    for j in range(m):
        if graph[i][j]==1:
            queue.append([i, j])
            tx = i # n
            ty = j # m


while queue:
    a, b = queue.popleft()
    for i in range(4):
        nx = a+dx[i]
        ny = b+dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
            queue.append([nx, ny])
            graph[nx][ny] = graph[a][b] + 1

day = 0
for i in graph:
    for j in i:
        if j==0:
            print(-1)
            exit()
    day = max(day, max(i))

print(day-1)
