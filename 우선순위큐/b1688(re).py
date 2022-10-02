import sys
import heapq
input = sys.stdin.readline
N = int(input())
leftheap =[]
rightheap = []
answer = []
for _ in range(N):
    i = int(input())
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, (-i,i))    #leftheap은 최대 힙으로 구현해야 하므로 
    else:
        heapq.heappush(rightheap, (i,i))
    if rightheap and leftheap[0][1] > rightheap[0][0]:
        min = heapq.heappop(rightheap)[0]
        max = heapq.heappop(leftheap)[1]
        heapq.heappush(leftheap, (-min,min))
        heapq.heappush(rightheap, (max,max))

    answer.append(leftheap[0][1])
for j in answer:
    print(j)
