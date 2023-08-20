# 스타트링크
from collections import deque
import sys
read = sys.stdin.readline

f, s, g, u, d = map(int, read().split())
visited = [0]*(f+1)

def bfs():
    queue = deque()
    queue.append((s))
    visited[s] = 1

    while queue:
        tmp = queue.popleft()
        for i in [tmp+u, tmp-d]:
            if 1<=i<=f and not visited[i]:
                visited[i] = visited[tmp]+1
                queue.append((i))
    

bfs()

if visited[g]:
    print(visited[g]-1)
else:
    print('use the stairs')