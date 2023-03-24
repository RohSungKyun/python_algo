# 연결요소의 개수 dfs
# 방향 없는 그래프, 연결요소의 개수를 구하는 프로그램을 작성
import sys
read = sys.stdin.readline

n, m = map(int, read().split())
graph = [[] for _ in range(n+1)]
visit = [False]*(n+1)

for i in range(m):
    u, v = map(int, read().split())
    graph[u].append(v)
    graph[v].append(u) # 방향이 없으므로 양방향으로 저장(그래프에 연결관계가 포함되도록 저장) 노드의 형태로 연결됨

def dfs(start): # 연결 요소를 도는 dfs
    visit[start] = True
    for i in graph[start]:
        if not visit[i]: # 방문x 인 경우
            visit[i] = True # 방문을 체크
            dfs(i) # 해당 위치에서 다시 탐색
cnt = 0
for j in range(1, n+1):
    if not visit[j]:
        dfs(j)
        cnt+=1

print(cnt)