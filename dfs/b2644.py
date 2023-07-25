# 촌수계산 
import sys
read = sys.stdin.readline

n = int(read()) # 사람의 수
a, b = map(int, read().split())
m = int(read()) # 관계의 수
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
ans = []

for i in range(m):
    x, y = map(int, read().split())
    graph[x].append(y)
    graph[y].append(x) # 촌수를 확인하기 위해 서로의 관계를 노드가 서로를 가리키도록 저장.

def dfs(v, cnt):
    cnt+=1
    visited[v] = True

    if v == b:
        ans.append(cnt)
        return
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i, cnt)

dfs(a, 0)
if len(ans)==0:
    print(-1)
else:
    print(ans[0]-1)