import sys
read = sys.stdin.readline

n = int(read())
m = int(read())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
# 무방향 그래프일 경우 양방향으로 움직일 수 있으므로 
# graph[v] 에 u를 graph[u]에 v를 추가

for i in range(m):
    u, v = map(int, read().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    global cnt
    cnt+=1    
    visited[v] = True
    for i in range(len(graph[v])): # graph에서 인덱스(현재노드)에 연결된 노드들을 탐색
        if visited[graph[v][i]] == False: # 방문한 적이 없을 경우
            dfs(graph[v][i]) # 해당 노드에서 dfs돌리기

cnt=0
dfs(1)
print(cnt-1)