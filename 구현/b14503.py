# 로봇 청소기
# 현재칸이 청소되어 있지 않을 경우 현재칸을 청소한다.
# 현재 칸 기준 4방향이 모두 청소되어있을 경우 1. 바라보는 방향을 유지한채 후진한다. 2. 뒤쪽칸이 벽이면 작동을 멈춘다.abs
# 4방향 중 청소되지 않은 빈칸이 있을 경우 1. 반시계 방향으로 회전, 2. 바라보는 방향이 청소x면 전진, 3. 현재칸을 청소한다로 돌아간다.
# 0은 청소x, 1은 벽을 의미한다.

from collections import deque
import sys
read = sys.stdin.readline

n, m = map(int, read().split())
r, c, d = map(int, read().split())
# 0 : 북, 1 : 동, 2 : 남, 3 : 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = []
for i in range(n):
    graph.append(list(map(int, read().split())))

visited = [[False]*m for _ in range(n)]
flag = 0

def bfs():
    global cnt
    global d
    global flag
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            d = (d-1)%4 # 1씩 감소시켜 반시계 방향으로 탐색
            nx, ny = x+dx[d], y+dy[d]

            if graph[nx][ny]==0 and not visited[nx][ny]: # 어차피 벽이 1로 둘러싸여 0<=nx<m and 0<=ny<n 로 범위 제한을 두면 오류가 뜬다.
                cnt+=1
                visited[nx][ny] = True
                queue.append((nx, ny))
                break

            if i == 3: # 모든 방향을 탐색한 경우
                nx, ny = x-dx[d], y-dy[d] # 방향을 유지한 채 후진
                if graph[nx][ny] == 1:
                    flag = 1
                else:
                    queue.append((nx, ny))
        if flag:
            break
bfs()
print(cnt)