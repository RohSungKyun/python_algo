import sys
from collections import deque

read = sys.stdin.readline()
n = int(read())

graph = [list(map(int, read().split())) for _ in range(n)]
visited = [[-1]*n for _ in range(n)]

