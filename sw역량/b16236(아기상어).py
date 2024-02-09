# n x n 공간에 물고기 m마리와 아기상어 1마리가 있다.
# 상어의 크기는 2이고 상하좌우로 이동
# 크기가 본인 이하인 경우 지나갈 수 있다. 작으면 먹을 수도 있다.
# 거리가 가까운 물고기가 여러마리라면 가장 위에 있는 거로, 그런 경우가 여러마리인 경우 가장 왼쪽으로 이동.
# 9는 상어가 있는 위치

import sys
from collections import deque
read = sys.stdin.readline

n = int(read())
graph = []
visited = [[-1]*n for _ in range(n)]
sx, sy = 0, 0

fishlst = []
for i in range(n):
    tmp = list(map(int, read().split()))
    graph.append(tmp)
    for j in range(n):
        if graph[i][j] == '9': # 물고기 위치 기록
            visited[i][j] = 1
            sx = i
            sy = j
        elif graph[i][j] != '0': # 해당 칸에 물고기가 존재, 리스트에 추가
            fishlst.append([i, j])

def find_fish(x, y): # 물고기의 거리를 기록
    queue = deque()
    queue.append((x, y))
    dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]
    dist = 1

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0<=nx<n and 0<=ny<n and size >= graph[nx][ny] and visited[nx][ny] == -1: # 이동할 수 있는 곳이라면
                visited[nx][ny] = dist
                if graph[nx][ny] < size and (nx, ny) in fishlst:
                    find_fish.append((nx, ny))
                else:
                    queue.append((nx, ny))
        
        if not find_fish:
            dist+=1
        else:
            return sorted(find_fish), dist # 함수 배열 정렬 문제
    return find_fish, 0 # 아무데도 갈 수 없을 때.
# ========================================

def solve():
    global sx, sy, size
    size, cnt, time = 2, 0, 0 # 크기, 먹은 물고기의 수, 시간
    while True:
        tmp, distance = find_fish(sx, sy) # 상어의 위치와 거리를 받아온다.

        if tmp: # 가장 위 왼쪽 물고기 부터 -> 위 함수에서 정렬이면 해결
            graph[sx][sy] = 0
            sx, sy = tmp[0] # 제일 가깝고 왼쪽위 물고기 위치로 갱신
            time += distance
            cnt+=1
            fishlst.remove((sx, sy)) # 물고기를 먹었으므로 삭제
            arr[sx][st] = 9 # 위치 갱신

            if cnt == size:
                size +=1   
                cnt = 0

        else:
            return time

print(solve())

