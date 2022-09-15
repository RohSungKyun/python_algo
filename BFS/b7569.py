# 토마토
import sys
from collections import deque
read = sys.stdin.readline

# 위, 아래, 오른쪽, 왼쪽, 앞, 뒤 6가지 고려
# 익은 토마토가 주변 토마토에 영향을 줄때 모두익는 최소일수를 구하여라

m, n, h = map(int, read().split())

dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

graph = []
queue = deque()

for i in range(h):
    tmp=[]
    for j in range(n):
        tmp.append(list(map(int, read().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                queue.append([i, j, k])
    graph.append(tmp)

while queue:
    x, y, z = queue.popleft()

    for i in range(6):
        nx = x+dx[i]
        ny = y+dy[i]
        nz = z+dz[i]
        if 0<=nx<h and 0<=ny<n and 0<=nz<m and graph[nx][ny][nz]==0:
            queue.append([nx, ny, nz])
            graph[nx][ny][nz] = graph[x][y][z]+1 # day수 갱신을 위해 카운트
print(graph)
day=0
for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit()
        day = max(day, max(j))

print(day-1)


