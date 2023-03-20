# (a, b) a는 부쪽으로부터 떨어진 칸, b는 서쪽으로부터 떨어진 칸
# 1. 현재 위치에서 왼쪽으로 회전, 2. 가본적이 없다면 전진, 있다면 회전만 수행, 3. 네곳이 모두 가봤거나 바다이면 현재방향에서 1칸 뒤로, 뒤가 바다이면 정지
# 0: 육지, 1: 바다
# 0: 북, 1: 동, 2: 남, 3:서

import sys
read = sys.stdin.readline

n, m =  map(int, read().split())
x, y, direction = map(int, read().split())
graph = [list(read().split()) for _ in range(n)]
visit = [[0]*m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def turn_left(): # 방향체크 왼쪽 회전 함수
    global direction
    direction-=1
    if direction == -1:
        direction = 3

ans = 1
turn_time =0
while True:
    turn_left()
    nx, ny = x+dx[direction], y+dy[direction]

    if graph[nx][ny]==0 and visit[nx][ny]==0:
        ans+=1
        visit[nx][ny]=1
        x = nx
        y = ny
        continue
    else:
        turn_time+=1
    
    if turn_time==4:
        nx = x-dx[direction]
        ny = y-dy[direction]
        if graph[nx][ny]==0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(ans)

    