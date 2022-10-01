from collections import deque
import sys
read = sys.stdin.readline

n, k = map(int, read().split())
MAX =100001
visited = [-1]*MAX

q = deque()
q.append(n)
visited[n]=0

while q:
    tmp = q.popleft()
    if tmp==k:
        print(visited[tmp])
        break
    if 0<=tmp*2<MAX and visited[tmp*2] == -1:
        q.appendleft(tmp*2)
        visited[tmp*2] = visited[tmp]
    if 0<=tmp+1<MAX and visited[tmp+1] == -1:
        q.append(tmp+1)
        visited[tmp+1] = visited[tmp]+1
    if 0<=tmp-1<MAX and visited[tmp-1] == -1:
        q.append(tmp-1)
        visited[tmp-1] = visited[tmp]+1
