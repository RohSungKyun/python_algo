# dfs와 bfs
# 2차원 배열을 이용(양방향)
from collections import deque

#vertex, edge, startnode
n, m, v = map(int,input().split())
# visited = [False] * (n+1) # 인덱스 0 은 사용하지 않는 부분이다.
# 인덱스와, 실숫자와의 간격때문에, 고려하는게 아직은 미숙해서 일단 뺴겠음,


# 2진 메트릭스를 통해, 노드 연결관계를 체크한다.

# 2진 메트릭스 초기화
graph = [[0]*(n+1) for _ in range(n+1)]

# 엣지와 연결된 노드를 작성한다.
for _ in range(m):
  m1, m2 = map(int, input().split())
  graph[m1][m2] = graph[m2][m1] = 1


# dfs
def dfs(start_v, visited=[]):
  visited.append(start_v) # v node에 대해 방문처리,
  print(start_v, end=" ")
  
  # start_v가 행의 값이고, i는 그 행의 요소들,
  for i in range(len(graph[start_v])):
    # 인접노드이면서, 방문을 안한 경우
    if graph[start_v][i] == 1 and i not in visited:
      dfs(i, visited)
      
# bfs
def bfs(start_v):
  visited = [start_v]
  
  queue = deque()
  queue.append(start_v)
  
  while queue:
    v = queue.popleft()
    print(v, end=" ")
    
    for w in range(len(graph[start_v])):# w는 해당 행에 있는 요소들,
      if graph[v][w] == 1 and w not in visited:
        visited.append(w)
        queue.append(w)
        
        
dfs(v)
print()
bfs(v)
