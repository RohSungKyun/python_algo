import sys
from collections import deque

read = sys.stdin.readline

n = int(read())
graph = [list(map(int, read().split())) for _ in range(n)]

shark = ()
size = 2
eatcnt = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark = (i, j)
            graph[i][j] = 0


def bfs():
    global shark, box, size, eatcnt
    visited = [[False]*n for _ in range(n)]
    queue = deque()
    sx, sy = shark
    queue.append((sx, sy, 0))
    visited[sx][sy] = True
    dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]

    fish_x = n
    fish_t = n*n
    fish = [] # 물고기의 y값을 저장

    while queue:
        x, y, t = queue.popleft()
        if t >= fish_t: # 발견했었던 물고기의 시간보다 초과 
            break
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if graph[nx][ny]==0 or graph[nx][ny] == size:
                    queue.append((nx, ny, t+1))
                    visited[nx][ny] = True
                
                elif graph[nx][ny] < size:
                    
                    visited[nx][ny] = True
                    # 거리가 같은 물고기라면
                    if nx<=fish_x: # 가까운 물고기가 여러마리면 위에있는 (x가 작은(좌표평면생각 x))물고기 선택
                        fish.append(ny)
                        fish_x, fish_t = nx, t+1
        if len(fish)==0: # 먹을 수 있는 물고기 x
            return -1
        
        fish_y = min(fish) # 가장 왼쪽에 있는 (y가 작은)
        graph[fish_x][fish_y] = 0
        eatcnt +=1
        
        if eatcnt == size:
            size+=1
            eatcnt=0
        shark = (fish_x, fish_y)

        return fish_t # 걸린시간

time = 0
while True:
    result = bfs()
    if result == -1:
        break
    time+=result

print(time)

