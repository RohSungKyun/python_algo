import sys
read = sys.stdin.readline

n, m = map(int, read().split())

visit = [False]*(n+1)
tmp = []

def dfs():
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return
    for i in range(1, n+1):
        if visit[i]:
            continue
        visit[i] = True
        tmp.append(i)
        dfs()
        tmp.pop()
        visit[i] = False

dfs()