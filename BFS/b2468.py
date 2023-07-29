# 안전영역
# 물에 잠기지 않는 안전영역의 최대갯수를 구해야 함
# 아무지역도 물에 잠기지 않을 수도 있다. (모든 지역이 높이가 같을 경우거나 모두 0일 경우 예외 처리 해주기)

from collections import deque
import sys
read = sys.stdin.readline

n = int(read())
visited = [[False]*n for _ in range(n)]
graph = []
for _ in range(n):
    tmp = list(map(int, read().split()))
    graph.append(tmp)
dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]
max_height = max(map(max, graph))

def bfs(height, a, b): # 강수량의 정보를 인자로 받아온다.
    global cnt
    queue = deque()
    queue.append([a, b])
    # 물에 잠기는 경우를 체크해야 함.
    while queue: # 안전구역을 체크해준다.
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] > height and not visited[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = True
    cnt+=1

# 강수량을 1 ~ (최대높이 - 1) 까지 모두 가정하여 비교해봐야 함.
max_cnt = 0
cnt = 0
for h in range(1, max_height):
    visited = visited = [[False]*n for _ in range(n)] # 초기화
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and not visited[i][j]:
                bfs(h, i, j)
    if max_cnt < cnt:
        max_cnt = cnt

if max_cnt == 0:
    print(1)
else:
    print(max_cnt)
                