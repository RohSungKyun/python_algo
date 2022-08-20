import sys
import heapq
read = sys.stdin.readline
# 비교횟수를 최소로 구하는 그리디 우선순위 큐 문제
# n개의 뭉치가 있으면 n-1번 비교하게 된다.
n = int(read())
heap=[]
stack=[]

for _ in range(n):
    heapq.heappush(heap, int(read()))

for i in range(n-1):
    x = heapq.heappop(heap) # 첫번째로 작은 뭉치
    y = heapq.heappop(heap) # 두 번째로 작은 뭉치
    heapq.heappush(heap, x+y)
    stack.append(x+y)

print(sum(stack))