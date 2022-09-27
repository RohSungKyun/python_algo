import sys
import copy
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

n, m  = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(n)]
dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]
graph_copy = copy.deepcopy(graph)
max_safe=0
def dfs(x, y, section): # 벽이 모두 선택된 경우 도는 dfs
    section[x][y] = 2 # 바이러스 퍼뜨리기
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
            dfs(nx, ny, section)

def find_wall(start, count):
    global safe_area

    section = copy.deepcopy(graph_copy)
    if count==3:
        for i in range(n):
            for j in range(m):
                if section[i][j]==2:
                    dfs(i, j, section)
        safe_area = sum(_.count(0) for _ in section)
        max_safe = max(max_safe, safe_area)

    else: # 벽이 3개가 아닌 경우 완전탐색(브루트포스)
        for i in range(start, n*m):
            r = i//m # 십의 자리수는 행
            c = i%m # 일의 자리수는 열
            if graph_copy[r][c]==0:
                graph_copy[r][c]=1 # 벽으로 선택
                find_wall(i, count+1) # 다음벽 탐색
                graph_copy[r][c]=0

find_wall(0, 0)
print(max_safe)