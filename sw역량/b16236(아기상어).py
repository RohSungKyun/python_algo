# n x n 공간에 물고기 m마리와 아기상어 1마리가 있다.
# 상어의 크기는 2이고 상하좌우로 이동
# 자기보다 큰 물고기가 있는 칸은 지나갈 수 없다.
# 거리가 가까운 물고기가 여러마리라면 가장 위에 있는 거로, 그런 경우가 여러마리인 경우 가장 왼쪽으로 이동.
# 9는 상어가 있는 위치

import sys
read = sys.stdin.readline

n = int(read())
graph = []
for _ in range(n):
    tmp = list(map(int, read().split()))
    graph.append(tmp)

dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]
bs = 1
time = 0


