# 맥주마시면서 걸어가기
# 박스에는 맥주 20개가 들어있으며 20개 이상을 채울 수 없다.
# 50미터에 한병씩 마신다.
import sys
from collections import deque

read = sys.stdin.readline

def bfs():
    queue = deqeue
    queue.append([home_x, home_y])
    while queue:
        a, b = queue.popleft()




t = int(read())
graph = []
for _ in range(t):
    n = int(read())
    home_x, home_y = map(int, read().split())
    festival_x, festival_y = map(int, read().split())
    
