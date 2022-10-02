import heapq, sys
read = sys.stdin.readline

T = int(read())
# 최대 힙은 중앙값 이하의 수가 오도록
# 최소 힙은 중앙값 초과의 수가 오도록 조정하면 됩니다. 이 때, 최대 힙은 내림차순 정렬, 최소 힙은 오름차순 정렬이 되도록 해야 합니다.
for i in range(T):
    m = int(read())
    heap = map(int, read().split())
    print(heap)
    
