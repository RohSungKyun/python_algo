# 바뀐 조건 : 사전순(중복없이, 오름차순)

import sys
read = sys.stdin.readline

n, m = map(int, read().split())
num = list(map(int, read().split()))
num.sort()
visit = [False]*(n+1)
tmp = []

def dfs():
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return
    for i in range(n):
        if visit[i] :
            continue
        visit[i] = True # 중복제거
        tmp.append(num[i])
        dfs()
        visit[i] = False
        tmp.pop()

dfs()