import sys, heapq
# 배열의 첫째 항과 다음 줄의 모두와 비교하여 교체하는 구조
# 마지막에 길이 n을 유지하면서 남은 0번째 값이 n번째로 큰 수 이다.
read = sys.stdin.readline
n = int(read())

heap = list(map(int, read().split()))
for _ in range(n-1):
    for i in list(map(int, read().split())):
        if i > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, i)

print(heap[0])
