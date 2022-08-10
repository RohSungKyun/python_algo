import sys

n = int(sys.stdin.readline())
arr = [i for i in range(1, n+1)]
result = []

def dfs(depth, v):
    # base case
    if depth == len(arr): # 리프노드에 도달했을 경우
        result.append(v)
        return
    
    for num in arr:
        tmp=v[:]
        if num not in tmp:
            tmp.append(num)
            dfs(depth+1, tmp)
        
dfs(0, [])
for res in result:
    print(' '.join(map(str, res)))