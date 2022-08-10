# 15649 n과 m(1)
import sys
# 1부터 n 까지의 자연수, m 개를 중복없이 고름
# m 은 깊이가 된다.
n, m = map(int, input().split())


nums = [i for i in range(1, n+1)]
result = []
visit = [False]*(n+1)

def dfs():
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    for i in nums:
        if visit[i]:
            continue
        visit[i] = True
        result.append(i)
        dfs()
        result.pop()
        visit[i] = False

dfs()