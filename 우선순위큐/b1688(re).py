import sys
import heapq
input = sys.stdin.readline
N = int(input())
leftheap =[] # 중앙값보다 작은 값들
rightheap = [] # 중앙값보다 큰 값들
answer = []
for _ in range(N):
    i = int(input())
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, (-i,i))    #leftheap은 최대 힙으로 구현해야 하므로 / 
    else:
        heapq.heappush(rightheap, (i,i)) # 오른쪽과 왼쪽의 원소값을 바꿔준다.
    if rightheap and leftheap[0][1] > rightheap[0][0]:
        min = heapq.heappop(rightheap)[0]
        max = heapq.heappop(leftheap)[1]
        heapq.heappush(leftheap, (-min,min))
        heapq.heappush(rightheap, (max,max))

    answer.append(leftheap[0][1])
for j in answer:
    print(j)
