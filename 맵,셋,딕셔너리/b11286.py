# 절댓값이 가장 작은값을 출력하는 것이다
import sys, heapq
read = sys.stdin.readline
n = int(read())
heap = []

for i in range(n):
    x = int(read())
    if x==0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        if x<0:
            heapq.heappush(heap, (x*-1, x)) # 음수인 경우
        else:
            heapq.heappush(heap, (x, x))