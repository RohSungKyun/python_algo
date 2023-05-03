# 추가된 옵션 : 비내림차순
import sys
read = sys.stdin.readline

n, m = map(int, read().split())
ans=[]

def dfs(x):
    if len(ans) == m:
        print(*ans)
        return
    
    for i in range(x, n+1):
        ans.append(i)
        dfs(i)
        ans.pop() # backtrack

dfs(1)