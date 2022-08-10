n, m = map(int, input().split())
ans=[]

def dfs(x):
    if len(ans) == m:
        print(*ans)
        return
    
    for i in range(1, n+1):
        ans.append(i)
        dfs(x+1)
        ans.pop() # backtrack

dfs(0)