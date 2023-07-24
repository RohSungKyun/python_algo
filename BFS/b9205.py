# 맥주마시면서 걸어가기
# 박스에는 맥주 20개가 들어있으며 20개 이상을 채울 수 없다. => 1000미터를 갈 수 있음.
# 50미터에 한병씩 마신다.
import sys
from collections import deque

read = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append([home_x, home_y])
    while queue:
        a, b = queue.popleft()
        # 맨해튼 거리로 두 점 사이의 거리가 1000이하일 경우 happy출력. 
        if abs(a - festival_x) + abs(b-festival_y)<=1000:
            print('happy')
            return
        for i in range(n):
            if not visited[i]: # 해당 편의점에 방문하지 않을 경우
                nx, ny = graph[i] # 해당 편의점의 좌표를 뽑아온다.
                if abs(a-nx)+abs(b-ny)<=1000: # 해당 편의점에 방문할 수 있다면
                    visited[i] = 1
                    queue.append([nx, ny])
    print('sad')

t = int(read())

for _ in range(t):
    graph = []
    n = int(read())
    home_x, home_y = map(int, read().split())
    for i in range(n):
        x, y = map(int, read().split())
        graph.append([x, y])
    festival_x, festival_y = map(int, read().split())
    visited = [0 for _ in range(n+1)]
    bfs()
    
