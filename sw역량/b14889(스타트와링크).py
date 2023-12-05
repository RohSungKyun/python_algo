import sys
from itertools import combinations

read = sys.stdin.readline

n = int(read())
graph = [list(map(int, read().split())) for _ in range(n)]
min_val = float('inf')

people = [range(n)]
members = list(combinations(people, n//2)) # people을 n//2명의 팀으로 나누는 조합들

for group in members:
    link = list(set(people) - set(group)) # 선택되지 않은 나머지 group
    s_sum, l_sum = 0, 0
    
    link_combination = list(combinations(link, 2))
    start_combination = list(combinations(list(group), 2))

    for x, y in link_combination:
        l_sum += graph[x][y] + graph[y][x]
    
    for x, y in start_combination:
        s_sum += graph[x][y] + graph[y][x]
    
    if min_val > abs(s_sum-l_sum):
        min_val = abs(s_sum-l_sum)
        if min_val == 0:
            print(0)
            exit()
print(min_val)

"""
visited = [False for _ in range(n)]
def dfs(depth, idx):
    global min_val
    if depth == n//2:
        s, l = 0, 0
        for i in range(n):
            for j in range(n):
                if not visited[i] and not visited[j]:
                    s+=graph[i][j]
                elif visited[i] and visited[j]:
                    l+=graph[i][j]
        if abs(l-s)<min_val:
            min_val = min(min_val, abs(s-l))
            if min_val == 0:
                print(0)
                exit()

    for d in range(idx, n):
        if not visited[d]:
            visited[d] = True
            dfs(depth+1, idx+1)
            visited[d] = False
dfs(0, 0)
print(min_val)
"""

