import sys, heapq

read = sys.stdin.readline
n = int(read())

heap = list(map(int, read().split()))
for _ in range(n-1):
    for i in list(map(int, read().split())):
        if i > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, i)

print(heap[0])
