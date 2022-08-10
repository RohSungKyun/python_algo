n, m = map(int, input().split())

# arr =[]
# visit = [False]*(n+1)

# def dfs(x):
#     if x == m:
#         print(' '.join(map(str, arr)))
#         return
#     t=1
#     if x>0:
#         t=arr[x-1]+1
#     for i in range(t, n+1): # visit길이 까지
#         if(visit[i]==False):
#             visit[i] = True # 노드 사용 체크
#             arr.append(i)
#             dfs(x+1)
#             visit[i] = False
#             arr.pop()

# dfs(0)

check =[]
def dfs(x):
    if len(check) == m:
        print(' '.join(map(str, check)))
    
    for i in range(x, n+1):
        if i not in check:
            check.append(i)
            dfs(i+1) # 리프노드에 도달할 때까지 반복 
            check.pop() # 도달했을 경우 backtrack

dfs(1)

