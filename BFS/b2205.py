# 벽 부수고 이동하기
# 가중치가 없는 최단 경로는 무조건 bfs + 벽을 부순적이 있는가도 따로 체크해야 한다.
import sys
from collections import deque
read = sys.stdin.readline
dx=[-1, 0, 1, 0]
dy=[0, -1, 0, 1]

n, m = map(int, read().split())

graph = [list(read()) for i in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)] # [0, 0]*m * n

# visited[x][y][벽부쉈는가?]

def bfs():
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    while queue:
        x, y, cnt = queue.popleft()
        if x==n-1 and y==m-1:
            print(visited[x][y][cnt])
            exit() # 함수를 종료해준다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny][cnt]: # 0=flase, 1 = true 즉, 범위 안이고 방문한 적이 없다면
                if graph[nx][ny] == '0':
                    visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                    queue.append((nx, ny, cnt))

                if graph[nx][ny] == '1' and cnt == 0: # 벽이 위치해 있고 벽을 부순 적이 없다면?
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))
    print(-1)

bfs()


