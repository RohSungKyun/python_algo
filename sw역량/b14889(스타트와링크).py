# 양팀의 능력치 차이가 최소가 되도록 한다.

import sys
read = sys.stdin.readline
n = int(read())
graph = [list(map(int, read().split())) for _ in range(n)]
min_val = float('inf')
visited = [False for _ in range(n)] # 노드 깊이 방문여부

def dfs(depth, idx):
    global min_val

    if depth == n//2:
        s, l =  0, 0
        for i in range(n):
            for j in range(n):
                if not visited[i] and not visited[j]:
                    s+=graph[i][j]
                elif visited[i] and visited[j]:
                    l+=graph[i][j]
        min_val = min(min_val, abs(s-l))
        return

    for i in range(idx, n):
        if not visited[i]:
               visited[i] = True
               dfs(depth+1, idx+1)
               visited[i] = False
               
dfs(0, 0)
print(min_val)
