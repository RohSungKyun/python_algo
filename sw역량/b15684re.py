import sys
read = sys.stdin.readline

n, m, h = map(int, read().split())
graph = [[False]*n for _ in range(h)]
for i in range(m):
    a, b = map(int, read().split())
    graph[a-1][b-1] = True
ans = 4

def check():
    for i in range(n):
        now = i
        for j in range(h):
            if graph[j][now]:
                now += 1
            elif graph[j][now-1]:
                now -= 1 
        if now != i :
            return False
    return True

def dfs(cnt, x, y):
    global ans
    if check():
        ans = min(cnt, ans)
        return 
    elif cnt == 3 or cnt >= ans:
        return
    
    for i in range(x, h):
        if i == x:
            now = y
        else:
            now = 0
        for j in range(now, n-1):
            if not graph[i][j] and not graph[i][j+1]:
                if graph[i][j-1]:
                    continue
                graph[i][j] = True
                dfs(cnt+1, i, j+2)
                graph[i][j] = False

dfs(0, 0, 0)
if ans == 4:
    ans = -1
print(ans)
