import sys
from collections import deque

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
read = sys.stdin.readline

h, w = map(int, read().split())
graph=[]
for i in range(h):
    graph.append(list(map(int, read().split())))

def bfs():
    queue = deque()
    queue.append([0, 0])
    visited = [[False]*w for i in range(h)]
    cnt=0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<h and 0<=ny<w:
                if graph[nx][ny] == 0 and visited[nx][ny] == False:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                elif graph[nx][ny] == 1 and visited[nx][ny] == False:
                    graph[nx][ny] = 0 # 녹았으므로 0으로 바꿔줌
                    cnt+=1
                    visited[nx][ny] = True
    return cnt
time=0
result=[]
while True:
    cnt = bfs()
    result.append(cnt)
    if cnt==0: # 모두 녹아서 cnt가 0으로 리턴됨
        break
    time+=1
print(time)
print(result[-2]) # 녹기 한시간 전 결과 출력