import sys, heapq
read = sys.stdin.readline
t = int(read())
heap = []
# 비어있는 배열을 제거하고 출력하라고 하는 경우 따로 처리를 해줘야 한다.
for i in range(t):
    num = int(read())
    if num!=0:
        heapq.heappush(heap, num)
    else:
        if len(heap)!=0:
            print(heapq.heappop(heap))
        else:
            print(0)
