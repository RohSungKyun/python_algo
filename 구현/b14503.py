# 로봇 청소기
# 현재칸이 청소되어 있지 않을 경우 현재칸을 청소한다.
# 현재 칸 기준 4방향이 모두 청소되어있을 경우 1. 바라보는 방향을 유지한채 후진한다. 2. 뒤쪽칸이 벽이면 작동을 멈춘다.abs
# 4방향 중 청소되지 않은 빈칸이 있을 경우 1. 반시계 방향으로 회전, 2. 바라보는 방향이 청소x면 전진, 3. 현재칸을 청소한다로 돌아간다.
# 0은 청소x, 1은 벽을 의미한다.

from collections import deque
import sys
read = sys.stdin.readline

n, m = map(int, read().split())
a, b, d = map(int, read().split())
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
graph = []
visited = [[False]*m for _ in range(n)]

