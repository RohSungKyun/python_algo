# 우선순위큐, 그리디
import sys, heapq

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    heapq.heappush(heap, tuple(map(int, input().split())))

answer = 0
rooms = []
while heap:
    start, end = heapq.heappop(heap)
    if rooms:
        if min(rooms) <= start:
            rooms[0] = end
            continue
    rooms.append(end)
    if len(rooms) > answer:
        answer = len(rooms)

print(answer)
