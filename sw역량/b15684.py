# 사다리 조작
# n 개의 세로선과 h개의 가로점선이 주어진다.
# a, b에서 b, b+1의 세로선에 a위치에 가로선을 긋는다는 의미
# 백트래킹 조건(dfs) : 사다리를 3개 이상 놓을 경우

import sys
read = sys.stdin.readline

def check(): # 제자리로 돌아오는지 체크하는 함수
    for i in range(n): # 모든 세로선
        now = i
        for j in range(h):
            if graph[j][now]: # 오른쪽 가는 선
                now+=1
            elif i>0 and graph[j][now-1]: # 왼쪽 가는 선
                now-=1
        if now!=i:
            return False
    return True

def dfs(cnt, x, y):
    global ans

    if check(): # 백 트래킹
        ans = min(ans, cnt)
        return
    elif cnt == 3 or cnt>=ans:
        return
    
    for i in range(x, h): # 가로선을 놓을 수 있는 행
        if i == x: # 현재 행
            now = y # 이어서 탐색
        else: # 바뀐 행
            now = 0 # 처음부터 탐색
        
        for j in range(now, n-1): # 열 탐색
            if not graph[i][j] and not graph[i][j+1]: # 오른쪽에 없을 경우
                if j>0 and graph[i][j-1]: # 왼쪽에 존재할 경우 다음탐색
                    continue
                graph[i][j] = True
                dfs(cnt+1, i, j+2)
                graph[i][j] = False


n, m, h = map(int, read().split())
graph = [[False]*n for _ in range(h)]

for i in range(m):
    a, b = map(int, read().split())
    graph[a-1][b-1] = True

ans = 4
dfs(0, 0, 0)
if ans>4:
    print(-1)
else:
    print(ans)
