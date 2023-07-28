# 안전영역
# 물에 잠기지 않는 안전영역의 최대갯수를 구해야 함
# 아무지역도 물에 잠기지 않을 수도 있다.

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

def bfs(x): # 강수량의 정보를 인자로 받아온다.
    queue = deque()
    queue.append([0, 0])
    # 물에 잠기는 경우를 체크해야 함.
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] >= x and not visited[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = True
