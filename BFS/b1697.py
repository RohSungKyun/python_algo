import sys
from collections import deque
read = sys.stdin.readline
n, k = map(int, read().split())
#  위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동

visited = [0 for _ in range(100001)] # 움직인 시간이 저장될 것

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        tmp = queue.popleft()

        if tmp == k:
            print(visited[tmp])
            break

        for i in (tmp+1, tmp-1, tmp*2):
            if 0<=i<100001 and not visited[i]:
                visited[i] = visited[tmp] + 1
                queue.append(i)

bfs()


        
